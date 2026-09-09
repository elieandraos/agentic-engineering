#!/usr/bin/env python3
"""Measure Unicode-character context cost of skills/ and modeled workflows.

Read-only: this script only reads files under skills/ and the workflow
config, and queries git state. It never writes or modifies anything.

Frontmatter descriptions are parsed strictly: only a single-line,
double-quoted YAML scalar (`description: "..."`, closing on the same
physical line, escapes limited to \\" \\\\ \\n \\t \\r) is supported. Any
other form -- multi-line, unquoted, single-quoted, block-scalar, an
unrecognized escape, more than one `description:` line in the frontmatter,
or no frontmatter block at all -- raises a clear error naming the file and
the reason, rather than guessing or silently falling back to scanning the
rest of the file (which could otherwise match an unrelated `description:`
line written as prose or an example in the body).

Git-ignored files under skills/ and docs/ are excluded from every measured
total; if git-ignored status can't be determined, the script says so rather
than silently measuring (or silently skipping) that content. A failed git
status check is reported as "consistency unknown," never as "clean."

Usage:
    scripts/measure_skill_context.py                  # compact summary
    scripts/measure_skill_context.py --detail <skill>  # per-file breakdown for one skill
    scripts/measure_skill_context.py --detail all       # per-file breakdown for every skill
    scripts/measure_skill_context.py --workflow <name>  # file-by-file breakdown for one workflow

See docs/skill-context.md for what these figures mean and don't mean.
"""

import argparse
import json
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
WORKFLOWS_CONFIG = REPO_ROOT / "docs" / "skill-context-workflows.json"

FRONTMATTER_DELIM = "---"
DESCRIPTION_ESCAPES = {'"': '"', "\\": "\\", "n": "\n", "t": "\t", "r": "\r"}


class UnsupportedFrontmatter(ValueError):
    """Raised when a SKILL.md's frontmatter isn't a form this script parses."""


def char_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8"))


def rough_tokens(chars: int) -> int:
    return round(chars / 4)


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


@lru_cache(maxsize=1)
def get_ignored_files():
    """Resolved paths git considers ignored under skills/ and docs/, or None if unknown."""
    try:
        out = git("ls-files", "--others", "--ignored", "--exclude-standard", "--", "skills", "docs")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return frozenset((REPO_ROOT / line).resolve() for line in out.splitlines() if line)


def is_ignored(path: Path) -> bool:
    """True only when git-ignored status is known and confirmed. Unknown status is not
    treated as ignored -- see main()'s own warning when status can't be determined."""
    ignored = get_ignored_files()
    if ignored is None:
        return False
    return path.resolve() in ignored


# --- Frontmatter description parsing -----------------------------------------------

def extract_frontmatter_block(content: str, path: Path) -> str:
    lines = content.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_DELIM:
        raise UnsupportedFrontmatter(f"{path}: file does not start with a '---' frontmatter delimiter")
    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_DELIM:
            end_index = i
            break
    if end_index is None:
        raise UnsupportedFrontmatter(f"{path}: no closing '---' frontmatter delimiter found")
    return "\n".join(lines[1:end_index])


def decode_double_quoted_scalar(raw: str, path: Path) -> str:
    out = []
    i = 0
    while i < len(raw):
        ch = raw[i]
        if ch == "\\":
            if i + 1 >= len(raw):
                raise UnsupportedFrontmatter(f"{path}: description ends with a dangling backslash")
            nxt = raw[i + 1]
            if nxt not in DESCRIPTION_ESCAPES:
                raise UnsupportedFrontmatter(
                    f"{path}: unsupported escape sequence '\\{nxt}' in description"
                )
            out.append(DESCRIPTION_ESCAPES[nxt])
            i += 2
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def description_chars(skill_md: Path) -> int:
    content = skill_md.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter_block(content, skill_md)
    desc_lines = [line for line in frontmatter.splitlines() if line.startswith("description:")]
    if not desc_lines:
        raise UnsupportedFrontmatter(f"{skill_md}: no 'description:' field found in frontmatter")
    if len(desc_lines) > 1:
        raise UnsupportedFrontmatter(f"{skill_md}: multiple 'description:' lines found in frontmatter")

    value_part = desc_lines[0][len("description:"):].strip()
    if not value_part.startswith('"'):
        raise UnsupportedFrontmatter(
            f"{skill_md}: description is not a single-line double-quoted scalar "
            f"(only that form is supported)"
        )

    body = value_part[1:]
    escape = False
    end_index = None
    for i, ch in enumerate(body):
        if escape:
            escape = False
            continue
        if ch == "\\":
            escape = True
            continue
        if ch == '"':
            end_index = i
            break
    if end_index is None:
        raise UnsupportedFrontmatter(
            f"{skill_md}: description has no closing quote on its own line "
            f"(a multi-line description is not a supported form)"
        )

    raw = body[:end_index]
    trailing = body[end_index + 1:]
    if trailing.strip():
        raise UnsupportedFrontmatter(
            f"{skill_md}: unexpected content after the closing quote: {trailing!r}"
        )

    decoded = decode_double_quoted_scalar(raw, skill_md)
    return len(decoded)


# --- Discovery and measurement -------------------------------------------------------

def discover_skills():
    """Return {skill_name: skill_dir} for every non-ignored skills/<name>/SKILL.md found."""
    skills = {}
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        if is_ignored(skill_md):
            continue
        skills[skill_md.parent.name] = skill_md.parent
    return skills


def skill_files(skill_dir: Path):
    """All non-ignored files under one skill directory, as Paths, largest first."""
    files = [p for p in skill_dir.rglob("*") if p.is_file() and not is_ignored(p)]
    return sorted(files, key=char_count, reverse=True)


def per_skill_summary(skills):
    """Return list of dicts: name, discovery, entrypoint, supporting, readme, file counts."""
    rows = []
    for name, skill_dir in skills.items():
        skill_md = skill_dir / "SKILL.md"
        readme = skill_dir / "README.md"
        entrypoint_chars = char_count(skill_md)
        discovery = description_chars(skill_md)
        readme_exists = readme.is_file() and not is_ignored(readme)
        readme_chars = char_count(readme) if readme_exists else 0
        supporting_chars = 0
        supporting_count = 0
        for p in skill_dir.rglob("*"):
            if not p.is_file() or is_ignored(p):
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
                "readme_exists": readme_exists,
            }
        )
    return rows


def report_revision():
    """Print the source revision and whether it's known to match the measured files.

    Returns True if consistency is confirmed clean, False if confirmed dirty, and
    None if consistency could not be determined (git unavailable, or the status
    check itself failed) -- callers must not treat None as "clean."
    """
    try:
        sha = git("rev-parse", "HEAD")
        short_sha = git("rev-parse", "--short", "HEAD")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Source revision: unknown (not a git checkout, or git unavailable)")
        return None
    try:
        dirty = git("status", "--porcelain", "--", "skills", "docs/skill-context-workflows.json")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(
            f"Source revision: {sha} ({short_sha}) -- "
            f"consistency UNKNOWN: the git status check itself failed"
        )
        return None
    if dirty:
        print(f"Source revision: {sha} ({short_sha}) -- MEASURED INPUTS DIFFER FROM THIS REVISION:")
        for line in dirty.splitlines():
            print(f"  {line}")
        return False
    print(f"Source revision: {sha} ({short_sha}) -- measured inputs match this revision")
    return True


def load_workflows():
    if not WORKFLOWS_CONFIG.is_file():
        print(f"error: workflow config not found: {WORKFLOWS_CONFIG}", file=sys.stderr)
        sys.exit(1)
    return json.loads(WORKFLOWS_CONFIG.read_text(encoding="utf-8"))


def resolve_workflow_files(file_list, workflow_name):
    """Resolve a workflow's configured file list, deduplicating by resolved path
    identity (so 'skills/x/SKILL.md' and './skills/x/SKILL.md' count once), and
    failing clearly on any path that's missing or git-ignored."""
    resolved = []
    seen = set()
    missing = []
    ignored = []
    for rel in file_list:
        path = REPO_ROOT / rel
        if not path.is_file():
            missing.append(rel)
            continue
        if is_ignored(path):
            ignored.append(rel)
            continue
        key = path.resolve()
        if key in seen:
            continue
        seen.add(key)
        resolved.append((rel, path))
    if missing or ignored:
        if missing:
            print(f"error: workflow '{workflow_name}' names missing file(s):", file=sys.stderr)
            for rel in missing:
                print(f"  {rel}", file=sys.stderr)
        if ignored:
            print(f"error: workflow '{workflow_name}' names git-ignored file(s):", file=sys.stderr)
            for rel in ignored:
                print(f"  {rel}", file=sys.stderr)
        sys.exit(1)
    return resolved


def workflow_total(file_list, workflow_name):
    resolved = resolve_workflow_files(file_list, workflow_name)
    total = sum(char_count(p) for _, p in resolved)
    return total, resolved


# --- Reporting ------------------------------------------------------------------------

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
    print("  entrypoint  = SKILL.md (frontmatter + body). This report models it as loading as")
    print("                one whole unit once activated -- an assumption this document makes,")
    print("                not an observed or guaranteed runtime mechanic.")
    print("  supporting  = every non-ignored file under rules/, blueprints/, templates/, etc.")
    print("                (not README.md). Modeled as loading only on demand -- this total is")
    print("                not what any single workflow loads.")
    print("  readme      = README.md, when present and not git-ignored. Modeled as loaded only")
    print("                if the skill's own SKILL.md text points to it.")
    print("  files       = count of files in the supporting total")
    print("  Run --detail <skill> for the file-by-file breakdown behind these totals.")

    total_chars = sum(r["entrypoint"] + r["supporting"] + r["readme"] for r in rows)
    total_files = sum(1 + r["supporting_count"] + (1 if r["readme_exists"] else 0) for r in rows)
    print()
    print(
        f"Repository-wide total (every non-ignored file under skills/, whether or not any "
        f"single workflow loads it): {total_chars} characters across {total_files} files "
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
    print("Modeled workflow estimates (explicit file lists, deduplicated by resolved path;")
    print(f"seeded from {WORKFLOWS_CONFIG.relative_to(REPO_ROOT)}. Each file is assumed to load")
    print("in full -- these are arithmetic over named files under that assumption, not an")
    print("observed session's actual token usage):")
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

    try:
        report_revision()
        if get_ignored_files() is None:
            print(
                "warning: could not determine git-ignored files (git unavailable or not a "
                "checkout) -- measured totals may include content that would otherwise be excluded"
            )

        skills = discover_skills()
        if not skills:
            print(f"error: no skills found under {SKILLS_DIR}", file=sys.stderr)
            sys.exit(1)

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
    except UnsupportedFrontmatter as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
