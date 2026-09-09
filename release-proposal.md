# Agentic Engineering v2.0.2 — Release Proposal

**Status: proposal only. Not approved. No tag, draft release, published release, PR, or deployment
has been created for it.** Publication is a separate, later, explicitly authorized action.

## Proposed tag and title

Tag `v2.0.2`; release title **"Agentic Engineering v2.0.2"**.

## Release candidate — exact target SHA

**`c9d73eae5d459f5f0ea62d55d82e5368c46acdb3`**, resolved and confirmed as `origin/main`'s tip before
this proposal was written (`git fetch` then `git rev-parse HEAD` / `git rev-parse origin/main`, both
matching). Compared with [v2.0.1](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.1)
(`0b74e5c`). This is the last commit in this release's scope — all four extractions below
(`document-it`, `implement-it`, `ship-it`, `plan-it`) are approved as of this commit.

**This proposal document's own commit is deliberately not the release candidate.** Committing and
pushing this file lands as a new commit after `c9d73ea`; the tag target named above stays `c9d73ea`
regardless — the proposal describes a release of the reviewed code that precedes it, not of itself.

## Why this remains a patch, not a minor or major release

No skill was added or removed — the same seven skills published at `v2.0.1` (`document-it`,
`implement-it`, `lab-it`, `laravel-inertia-stack`, `plan-it`, `review-it`, `ship-it`) are the only
seven in this release too. No skill's frontmatter `description` (its activation trigger), ownership
boundary, or entry contract changed — confirmed byte-for-byte identical in every touched `SKILL.md`.
Four new files were added, one per extraction (`document-it/rules/authoring.md`,
`implement-it/rules/activation-ordering.md`, `ship-it/rules/milestone-lifecycle.md`,
`plan-it/rules/verification-checkpoints.md`), each a supporting rule file inside an already-existing
skill's own directory: every procedure they contain already existed in `v2.0.1`, and each still
loads only when its own unchanged trigger condition applies, kept visible in the file that hands off
to it. No runtime skill behavior changed. The remaining content is maintainer tooling and
documentation with no consumer-facing effect.

## Complete proposed release-note text

> ## Agentic Engineering v2.0.2
>
> A patch release: internal reorganization of four skills' largest rule files into focused,
> conditionally-loaded supporting files, plus new maintainer tooling and documentation. No skill was
> added, removed, or renamed; no skill's activation, ownership, or entry contract changed; no
> runtime skill behavior changed.
>
> ### Changed (internal reorganization, same behavior)
>
> - **`document-it`** — format-selection, new-guide-writing, and existing-guide-update procedures
>   moved from `SKILL.md` into `rules/authoring.md`. `SKILL.md` states each procedure's own trigger
>   and hands off to it.
> - **`implement-it`** — the activation-risk commit-ordering procedure moved from
>   `rules/verification.md` into `rules/activation-ordering.md`. `verification.md` still checks
>   every commit against runtime activation and hands off only once that check finds an effect.
> - **`ship-it`** — shared delivery-lifecycle guidance (recognizing a delivery milestone, the
>   Backlog exemption, the milestone description's scope contract, and why closure and release don't
>   gate each other) moved from `rules/milestone-completion.md` into `rules/milestone-lifecycle.md`.
>   `milestone-completion.md` keeps only the closure gate itself.
> - **`plan-it`** — guidance on what a verification checkpoint should ask for inside a multi-group
>   issue moved from `rules/issue-conventions.md` into `rules/verification-checkpoints.md`,
>   consulted only once an issue's Tasks actually span multiple implementation groups.
>
> Each extracted file is a routed-to reference already reachable from its own skill. Nothing a
> consuming project does differently, and every extracted procedure's trigger condition still
> appears in the file that hands off to it.
>
> ### Added (maintainer tooling and documentation)
>
> - `scripts/measure_skill_context.py` and `docs/skill-context-workflows.json`: a reproducible way
>   to measure each skill's file sizes and modeled per-workflow context totals, replacing the
>   previous dated measurement tables in `docs/skill-context.md`.
> - `test-contracts.md`: contributor-readable behavior contracts and a framework-independent testing
>   strategy, alongside the existing `scenarios.md` audit record.
> - Every affected skill's `README.md` and architecture dossier (`artifacts/`) reconciled to reflect
>   the new files and current routing.
>
> ### Install / update
>
> ```shell
> npx skills update <your already-installed skill names> -p -y
> ```
>
> No new skill names are introduced in this release; an ordinary refresh is sufficient. The four new
> supporting files above live inside their existing skill's own directory and load automatically per
> that skill's own routing — there is no extra install step. To pin the exact tagged contents once
> this release publishes:
>
> ```shell
> npx skills add elieandraos/agentic-engineering#v2.0.2
> ```
>
> ### Validation and its limits
>
> Every changed file was reviewed against its prior source, with cross-file references,
> `git diff --check`, and Markdown-link resolution checked across the touched set. Each extraction's
> preserved wording was checked against its pre-extraction source before being treated as complete.
> `scripts/measure_skill_context.py` was re-run after each change and reproduces every configured
> workflow total without error.
>
> This release makes claims about two different kinds of number, and not a third: a **measured file
> size** is a direct character count of one file's actual current content; a **modeled workflow
> total** is an arithmetic sum of such counts standing in for a hypothetical sequence of files a task
> might load, not an observed cost. Neither is **observed session consumption** — an actual agent
> session's measured token usage — which this work did not produce for any workflow. No claim of an
> overall or universal token saving is made, and no live skill invocation, consuming-project
> installation, or browser session was exercised as part of this validation.
>
> ### Known deferred (not in this release)
>
> An optional extraction of `implement-it/rules/verification.md`'s reproducible-install guidance,
> and other conditional extraction candidates surfaced during this work, remain unassessed and
> unimplemented — deferred to a future pass, not resolved here.

## What remains unresolved

Human authorization to publish is the only open decision: this proposal creates no tag and no
GitHub release. Target SHA, scope, and release-note text are settled as of `c9d73ea`.
