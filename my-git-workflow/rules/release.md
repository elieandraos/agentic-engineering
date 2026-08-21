# Release

> A release summarizes the merged change at a release-level altitude — the same relationship a PR
> has to the commits inside it, one level up. Just as a PR doesn't replay every commit message, a
> release doesn't replay every PR description.

This phase starts once a PR has been successfully merged — not when work finishes, not when the
last commit lands. It was extracted from one real end-to-end run: PR #298 (Phase 22 — Authentication
& 2FA) merged to `main`, then released as `v0.17.0 — Authentication & 2FA`. PR creation and merge
strategy are still not owned by this skill (see `SKILL.md`'s "Left for later versions") — this phase
simply begins from "a PR merged," however that happened.

## 1. Discover the release policy before proposing anything

Do not assume a versioning scheme, a release mechanism, a tag type, or a hosting platform. Find out
what this repository actually does, in this order:

1. **Look for an explicit policy first.** A documented versioning/release policy, changelog-tooling
   config, a `VERSION` file, semantic-release config, or anything else the repository states
   outright. If one exists, it wins — don't override a stated policy with inferred history.
2. **Otherwise, infer from the repository's established release artifacts and history.** Tags,
   hosted releases, changelog files, package-registry versions — whatever the repository actually
   has. Read enough of it to name the pattern with evidence, not guess at one after skimming two
   examples.
3. **If the evidence is ambiguous or conflicting** — no policy file, thin or inconsistent history,
   two competing conventions — stop and ask the human rather than inventing one. This is the same
   "genuine unknown" stop `rules/review-gates.md` already applies elsewhere in this skill, extended
   here to release policy.

### What this repository's evidence shows

No policy file exists here — the version lives only in git tags and GitHub Releases, not in
`composer.json` or `package.json` (neither carries a `version` field). Discovered by inspecting
history (21 prior releases before this one): lightweight tags (`vMAJOR.MINOR.PATCH`) placed on the
merge commit of the PR that completed the milestone, published as GitHub Releases via
`gh release create`, with no release-automation workflow — `.github/workflows/` only runs lint and
tests. This is this repository's discovered adapter, not a rule to carry into a project whose
evidence points somewhere else.

## 2. Understand the release being made

Before drafting anything, determine the release's primary theme and the meaningful outcomes it
bundles — not by counting commits, files, or lines changed.

> Release size is not a versioning rule. Line count, commit count, and file count decide nothing
> about version importance; the project's release policy does.

A release may represent a user-facing capability, infrastructure/architecture work, hardening or
reliability work, UX/maintenance polish, or a mixture of these — and a release can legitimately
bundle several related areas even when it has one primary theme in its title. This repository's own
history is the evidence for that range, not a hypothetical:

| Shape | Example(s) |
|---|---|
| Feature/capability | `v0.13.0 — Carriers`, `v0.15.0 — Invite Members` |
| Infrastructure/architecture | `v0.11.1 — Tags Infrastructure` |
| Hardening/maintenance/polish | `v0.10.1 — Document Uploads Hardening`, `v0.11.2 — UI Polish` |
| Upgrade/reliability-heavy | `v0.12.1 — Pest 5 Upgrade` |
| Simplification/refactor with a security improvement | `v0.11.3 — Tags Simplified` |
| Multi-area | `v0.9.0 — Document Uploads & Notifications` |

`v0.17.0 — Authentication & 2FA` is itself multi-area under one theme: organization provisioning,
2FA enrollment, organization-wide enforcement, admin/operator reset, and three runtime bug fixes —
one release because they shipped as one merged PR completing one milestone, not because they were
mechanically similar in size.

## 3. Draft release notes at release-level altitude

Release notes describe what the release delivers, not how the code implements it. Group outcomes by
meaningful area — not by commit, not by file — and include infrastructure/technical changes only
when they carry real architectural, operational, reliability, or future-capability significance to
a reader, not just because they happened to land in the same PR.

Do not replay commit messages or issue titles verbatim. `v0.17.0`'s own drafting process is the
evidence for the gap between "technically accurate" and "release-level": the first pass correctly
grouped outcomes into five sections but still leaned on implementation language as the headline fact
("Fortify TOTP", "middleware", the `organizations:provision` Artisan command by name). The approved
revision pushed the same five sections up a level instead — recovery codes and the login-time
challenge described as what a member experiences, interrupted enrollment and visible enforcement
feedback described as what changes about the organization-enforcement experience, three runtime
issues summarized as outcomes under Bug Fixes rather than re-explained as notification/middleware
internals. Same underlying facts, judged at the altitude a release reads at, not a commit diff.

The release title identifies the version plus its primary theme, in whatever syntax the project's
discovered convention actually uses (step 1) — don't invent a title dialect the repository's history
doesn't show.

## 4. Human approval before publication

Draft the proposed version, the tag target (which commit), the release title, and the full release
body — then stop. This mirrors the two pre-merge review gates (`rules/review-gates.md`): approval of
the release *content* is not implicit in the merge having happened, and approving one wording tweak
is not the same as pre-approving everything else. If the human requests a change — even one
sentence, as happened with `v0.17.0`'s Owner-recovery bullet — revise and confirm the exact final
text before running any publish command. Do not tag or publish anything before this approval is
explicit.

## 5. Publish using the project's established mechanism

Use whatever release mechanism step 1 actually discovered — don't default to git tags, GitHub
Releases, or any other specific tooling absent evidence for this project. Preserve the established
tag/release semantics (tag type, what commit it targets, draft vs. published, prerelease flag)
unless the human explicitly asks for something different this time. Do not add deployment triggers,
rollback machinery, prerelease channels, or changelog automation the repository shows no evidence of
wanting — that's inventing release machinery, exactly what this phase exists to avoid.

### What this repository's evidence shows

```
git tag <version> <merge-commit-sha>
git push origin <version>
gh release create <version> --title "<title>" --target main --notes-file <approved-body>
```

A lightweight tag on the PR's merge commit, then a published (non-draft, non-prerelease) GitHub
Release built from that tag — what was actually run for `v0.17.0`. An adapter fact for this
repository, not a template to reuse verbatim in a project whose discovery step (step 1) turns up
something else.

## 6. Post-publication validation

Never treat a publish command's successful exit code as proof anything actually landed correctly —
the same discipline `rules/issue-closure.md` already applies to every GitHub mutation in this skill,
extended here to releases. Re-fetch the tag and the release from the source of truth discovered in
step 1, and validate at minimum:

- version/tag name
- tag target commit (does it point at the commit approved in step 4?)
- release title
- release body (matches the approved draft, including any last-minute wording change)
- published/draft/prerelease state, where the mechanism has one

Report the result compactly — what was created, and a field-by-field confirmation — not a re-print
of the whole release body. A mismatch on any field is something to report and fix, not a detail to
gloss over because the publish command didn't error.

## What this step does not do

It does not close issues — that already happened, per issue, during `rules/issue-closure.md`, before
the PR was even opened. It does not decide whether or how a PR gets created or merged — this skill
still has no evidence-backed convention for that (see `SKILL.md`'s "Left for later versions"); this
phase simply starts from "a PR merged," however that happened. It does not invent deployment,
rollback, prerelease-channel, or changelog-automation behavior beyond what step 1 actually found
evidence for.
