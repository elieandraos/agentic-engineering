# Skill Consumption

A practical methodology for consuming skills published from a repository like this one: how a
project installs them, which of several consumption modes to use, how a repository-managed install
stays reproducible and reviewable over time, and how to refresh it without over- or under-validating
the result.

**Authority boundary.** This document owns the consumption lifecycle — installing, committing,
refreshing, and validating skills in a project that isn't their source repository. It does not own
skill authoring (see `skill-authoring-methodology.md`) or a specific skill's own operational
contract, which stays with that skill's own `README.md` and `SKILL.md`.

## 1. Canonical source and managed installed copies

A repository that publishes skills under a `skills/<name>/` layout at its root — this one included —
is the canonical source for those skills. A consuming project does not point its agent directly at a
clone of that source repository. Instead it installs managed copies — real files, not symlinks back
to an upstream checkout — into its own tree, conventionally under `.agents/skills/<name>/`, a path
several coding agents already treat as a shared canonical skill location.

Editing a managed copy inside a consuming project is a local override, not a contribution channel.
A change meant to persist belongs in the source repository's own `skills/<name>/` and reaches
consumers through a normal install or update, not through hand-edits under `.agents/skills/`.

## 2. Three consumption modes

- **Personal/global** — install to the user's home directory. Available across every project that
  person works in, independent of what any single project commits. Suited to individual-preference
  skills that aren't meant to be enforced project-wide.
- **Disposable project-local** — install into a project without committing the result, for a quick
  trial or a one-off task, or generate a prompt from a skill without installing anything at all.
  Nothing is added to the repository; no other contributor sees it.
- **Repository-managed (team) consumption** — install into the project and commit the result, so
  every clone and every teammate gets the identical installed skill set without each person
  installing it themselves. This is the mode the rest of this document is mostly about, because it's
  the one with durable, reviewable state.

## 3. Installing from a GitHub source

Install with the `skills` CLI, pointed at the source repository:

```bash
npx skills add <owner>/<repo>
npx skills add <owner>/<repo> --skill <skill-name>
```

The CLI discovers skills under the source's `skills/` directory (and a handful of other recognized
locations) directly from the repository's current default-branch content — no release, tag, or
package publication needs to exist first. `-s/--skill` narrows installation to named skills instead
of everything the source publishes; `-a/--agent` targets specific agent(s) (e.g. `claude-code`);
`-y/--yes` skips interactive prompts for scripted or CI use.

Authenticated private GitHub repositories can also be installed and refreshed this way, using the
operator's configured GitHub credentials — but while private, they aren't eligible for public
skills.sh discovery.

Commands throughout this document are illustrative. The specific skills and agents a project
installs are that project's own decision, not a universal list.

## 4. The repository-managed model

A repository-managed install commits four things:

- **The CLI itself**, pinned as a versioned dependency rather than always resolving `npx skills` to
  whatever is currently latest — a repository-managed install deserves the same reproducibility as
  any other pinned tool the project depends on.
- **`skills-lock.json`** at the project root, recording per installed skill its source, source type,
  path within that source, and a content hash of what was installed.
- **The managed copies** under `.agents/skills/<name>/` — the real files an agent reads. Once
  installed, nothing about using them requires network access.
- **Only the agent-discovery symlinks a project actually needs**, e.g. `.claude/skills/<name>`
  pointing at the managed copy. Don't commit symlinks for agents the project doesn't use.

## 5. Why the rest of `.claude/` stays ignored

An agent's own directory accumulates local, per-machine, per-session state — settings, local
overrides, task locks — that has no business being shared across a team or reproduced on every
clone. Only the discovery symlinks a project has deliberately chosen to manage should be tracked;
everything else stays ignored by default. A generic allow-list:

```gitignore
/.claude/*
!/.claude/skills
/.claude/skills/*
!/.claude/skills/<skill-a>
!/.claude/skills/<skill-b>
```

Each managed skill needs its own explicit `!` line. A wildcard allow over the whole `skills/`
directory would also pick up anything installed there ad hoc for personal or disposable use,
defeating the isolation the repository-managed model depends on.

## 6. Relative symlinks and fresh-clone reproducibility

Symlinks the install method creates are relative, not absolute — `.claude/skills/<name> ->
../../.agents/skills/<name>`, not a path baked to one machine's filesystem layout. A relative
symlink resolves correctly regardless of where the repository is checked out, which is what makes it
safe to commit.

Because the real files live under `.agents/skills/**` and are committed alongside their symlinks, a
fresh clone reproduces the whole installed state — canonical files and agent discovery both — with
no network call and no dependency on the source repository still being reachable at clone time.

## 7. What `skills-lock.json` proves, and what it doesn't

It proves that the files currently installed under the managed directory match a content hash
computed from the source at install or update time — that nothing has silently drifted between what
the lock file claims was installed and what's actually on disk.

It does not prove the source hasn't changed since, that a specific commit or tag was used (a GitHub
source tracks the source repository's default branch at install/update time, not a pinned ref), or
that the installed content is semantically correct for the consuming project. Reviewing what changed
and validating the affected skills after an update remains the consuming project's own
responsibility — the lock file is an integrity record, not a correctness guarantee.

## 8. A simple refresh script

Wrap the update command in a project script rather than expecting every contributor to remember the
right flags:

```json
{
  "scripts": {
    "skills:refresh": "skills update <managed-skill-a> <managed-skill-b> -p -y"
  }
}
```

`-p/--project` scopes the update to project-installed skills rather than global ones; `-y/--yes`
skips the interactive scope prompt so the script runs unattended. Naming the managed skills
explicitly keeps a refresh scoped to what the project actually installed, rather than picking up
anything unrelated.

## 9. Proportional validation after a refresh

A refresh can touch some managed skills and leave others untouched. Diff the update before
committing it, and validate only the skills whose files actually changed — re-reading their updated
rules, re-exercising whatever claim in that skill actually moved — rather than re-validating the
whole managed set on every refresh regardless of what changed.

## 10. Git history as the provenance record

A repository-managed install doesn't need a separate changelog or ledger recording when each skill
was installed or refreshed and why. The consuming project's own commit history — one commit per
install or refresh, with a message describing what changed — already is that record, and it's the
one a team is already equipped to search, blame, and diff, unlike a hand-maintained file that can
silently fall out of date.

## 11. skills.sh as an optional discovery surface

skills.sh is a public directory for finding skills by keyword or owner. It is not a prerequisite for
installing from a GitHub source — a repository never needs to be listed there before `skills add
<owner>/<repo>` works against it. Listings are populated from install telemetry for repositories
GitHub confirms are public: visibility follows real usage, not a manual submission or a special
manifest a source repository has to add.

## 12. Telemetry

The CLI reports anonymous usage telemetry, including source and skill identifiers for
confirmed-public GitHub installs. Set `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` in the installing
environment to opt out entirely.

## 13. What GitHub-source consumption does not require

Releases, tags, npm publication of the skill content itself, and a Claude Code plugin marketplace
manifest are all optional. A GitHub source installs and updates straight off its default-branch
content; a plugin manifest is one additional, opt-in discovery path the CLI also recognizes, not a
requirement for installation or for skills.sh listing.

## 14. Stack companions are installed selectively

Not every consuming project needs every skill a source repository publishes. A stack companion —
one that carries technology-specific implementation knowledge for a particular framework or stack —
is only useful to a project that actually runs on that stack. Install and commit it there, and leave
it out of projects it doesn't apply to. Portable methodology skills and a stack companion are
independent install decisions, not a bundle that travels together.
