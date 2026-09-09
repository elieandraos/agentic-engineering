#!/usr/bin/env python3
"""Measure Unicode-character context cost of skills/ and modeled workflows.

Read-only: this script only reads files under skills/ and the workflow
config, and prints a report. It never writes or modifies anything.

Usage:
    scripts/measure_skill_context.py                  # compact summary
    scripts/measure_skill_context.py --detail <skill>  # per-file breakdown for one skill
    scripts/measure_skill_context.py --detail all       # per-file breakdown for every skill
    scripts/measure_skill_context.py --workflow <name>  # file-by-file breakdown for one workflow

See docs/skill-context.md for what these figures mean and don't mean.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
WORKFLOWS_CONFIG = REPO_ROOT / "docs" / "skill-context-workflows.json"

DESCRIPTION_RE = re.compile(r'^description:\s*"(.*)"\s*$', re.MULTILINE)


def char_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8"))


def rough_tokens(chars: int) -> int:
    return round(chars / 4)


def discover_skills():
    """Return {skill_name: skill_dir} for every skills/<name>/SKILL.md found."""
    skills = {}
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skills[skill_md.parent.name] = skill_md.parent
    return skills


def description_chars(skill_md: Path) -> int:
    content = skill_md.read_text(encoding="utf-8")
    m = DESCRIPTION_RE.search(content)
    if not m:
        raise ValueError(f"{skill_md}: could not find a frontmatter 'description' field")
    return len(m.group(1))


def skill_files(skill_dir: Path):
    """All files under one skill directory, as (relative_label, Path), largest first."""
    files = [p for p in skill_dir.rglob("*") if p.is_file()]
    return sorted(files, key=lambda p: char_count(p), reverse=True)


def per_skill_summary(skills):
    """Return list of dicts: name, discovery, entrypoint, supporting, readme, file_count."""
    rows = []
    for name, skill_dir in skills.items():
        skill_md = skill_dir / "SKILL.md"
        readme = skill_dir / "README.md"
        entrypoint_chars = char_count(skill_md)
        discovery = description_chars(skill_md)
        readme_chars = char_count(readme) if readme.is_file() else 0
        supporting_chars = 0
        supporting_count = 0
        for p in skill_dir.rglob("*"):
            if not p.is_file():
                continue
            if p in (skill_md, readme):
                continue
            supporting_chars += char_count(p)
            supporting_count += 1
        rows.append(
            {
                "name": name,
                "discovery": discovery,
                "entrypoint": entrypoint_chars,
                "supporting": supporting_chars,
                "supporting_count": supporting_count,
                "readme": readme_chars,
            }
        )
    return rows


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


def report_revision():
    try:
        sha = git("rev-parse", "HEAD")
        short_sha = git("rev-parse", "--short", "HEAD")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Source revision: unknown (not a git checkout, or git unavailable)")
        return
    try:
        dirty = git("status", "--porcelain", "--", "skills", "docs/skill-context-workflows.json")
    except subprocess.CalledProcessError:
        dirty = ""
    if dirty:
        print(f"Source revision: {sha} ({short_sha}) -- MEASURED INPUTS DIFFER FROM THIS REVISION:")
        for line in dirty.splitlines():
            print(f"  {line}")
    else:
        print(f"Source revision: {sha} ({short_sha}) -- measured inputs match this revision")


def load_workflows():
    if not WORKFLOWS_CONFIG.is_file():
        print(f"error: workflow config not found: {WORKFLOWS_CONFIG}", file=sys.stderr)
        sys.exit(1)
    return json.loads(WORKFLOWS_CONFIG.read_text(encoding="utf-8"))


def resolve_workflow_files(file_list, workflow_name):
    resolved = []
    seen = set()
    missing = []
    for rel in file_list:
        path = REPO_ROOT / rel
        if not path.is_file():
            missing.append(rel)
            continue
        if rel in seen:
            continue
        seen.add(rel)
        resolved.append((rel, path))
    if missing:
        print(f"error: workflow '{workflow_name}' names missing file(s):", file=sys.stderr)
        for rel in missing:
            print(f"  {rel}", file=sys.stderr)
        sys.exit(1)
    return resolved


def workflow_total(file_list, workflow_name):
    resolved = resolve_workflow_files(file_list, workflow_name)
    total = sum(char_count(p) for _, p in resolved)
    return total, resolved


def print_compact_summary(skills):
    rows = per_skill_summary(skills)
    print()
    print("Discovery metadata (frontmatter `description`, paid once per session for every")
    print("installed skill, before any activates):")
    print(f"  {'skill':<24} {'chars':>8}")
    disc_total = 0
    for r in rows:
        print(f"  {r['name']:<24} {r['discovery']:>8}")
        disc_total += r["discovery"]
    print(f"  {'TOTAL':<24} {disc_total:>8}  (~{rough_tokens(disc_total)} rough tokens)")

    print()
    print("Per-skill entrypoint and supporting content (Unicode characters):")
    print(f"  {'skill':<24} {'entrypoint':>11} {'supporting':>11} {'readme':>8} {'files':>6}")
    for r in rows:
        print(
            f"  {r['name']:<24} {r['entrypoint']:>11} {r['supporting']:>11} "
            f"{r['readme']:>8} {r['supporting_count']:>6}"
        )
    print()
    print("  entrypoint  = SKILL.md (frontmatter + body), loaded whole once activated")
    print("  supporting  = every file under rules/, blueprints/, templates/, etc. (not README.md),")
    print("                loaded only on demand -- this total is not what any single workflow loads")
    print("  readme      = README.md, human-facing; loaded by an agent only if SKILL.md says to")
    print("  files       = count of files in the supporting total")
    print("  Run --detail <skill> for the file-by-file breakdown behind these totals.")

    total_chars = sum(r["entrypoint"] + r["supporting"] + r["readme"] for r in rows)
    total_files = sum(r["supporting_count"] + 2 for r in rows)  # + SKILL.md + README.md each
    print()
    print(
        f"Repository-wide total (every file under skills/, whether or not any single "
        f"workflow loads it): {total_chars} characters across {total_files} files "
        f"(~{rough_tokens(total_chars)} rough tokens)"
    )


def print_detail(skill_name, skill_dir):
    print()
    print(f"=== {skill_name} ({skill_dir.relative_to(REPO_ROOT)}) ===")
    for p in skill_files(skill_dir):
        rel = p.relative_to(REPO_ROOT)
        c = char_count(p)
        print(f"  {c:>8}  {rel}")


def print_workflows_summary(config):
    print()
    print("Modeled workflow estimates (explicit file lists, deduplicated; whole-file reads;")
    print(f"seeded from {WORKFLOWS_CONFIG.relative_to(REPO_ROOT)} -- these are arithmetic over")
    print("named files, not an observed session's actual token usage):")
    print()
    for wf in config["workflows"]:
        total, _ = workflow_total(wf["files"], wf["name"])
        print(f"  {total:>8}  (~{rough_tokens(total):>6} tokens)  {wf['name']}")


def print_workflow_detail(config, name):
    matches = [wf for wf in config["workflows"] if wf["name"] == name]
    if not matches:
        print(f"error: no workflow named '{name}' in {WORKFLOWS_CONFIG}", file=sys.stderr)
        print("Available workflow names:", file=sys.stderr)
        for wf in config["workflows"]:
            print(f"  {wf['name']}", file=sys.stderr)
        sys.exit(1)
    wf = matches[0]
    total, resolved = workflow_total(wf["files"], wf["name"])
    print()
    print(f"=== {wf['name']} ===")
    if wf.get("notes"):
        print(f"Notes: {wf['notes']}")
    running = 0
    for rel, path in resolved:
        c = char_count(path)
        running += c
        print(f"  {c:>8}  (running total {running:>8})  {rel}")
    print(f"Total: {total} characters, ~{rough_tokens(total)} rough tokens")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--detail",
        metavar="SKILL|all",
        help="print the full file-by-file breakdown for one skill, or 'all' for every skill",
    )
    parser.add_argument(
        "--workflow",
        metavar="NAME",
        help="print the file-by-file breakdown for one modeled workflow (see docs/skill-context-workflows.json)",
    )
    args = parser.parse_args()

    skills = discover_skills()
    if not skills:
        print(f"error: no skills found under {SKILLS_DIR}", file=sys.stderr)
        sys.exit(1)

    report_revision()

    if args.workflow:
        config = load_workflows()
        print_workflow_detail(config, args.workflow)
        return

    if args.detail:
        if args.detail == "all":
            for name, skill_dir in skills.items():
                print_detail(name, skill_dir)
        elif args.detail in skills:
            print_detail(args.detail, skills[args.detail])
        else:
            print(f"error: unknown skill '{args.detail}'. Known skills: {', '.join(skills)}", file=sys.stderr)
            sys.exit(1)
        return

    print_compact_summary(skills)
    config = load_workflows()
    print_workflows_summary(config)


if __name__ == "__main__":
    main()
