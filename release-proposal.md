# Agentic Engineering v2.0.2 — Release Proposal

**Status: proposal only. Not approved. No tag, draft release, published release, PR, or deployment
has been created for it.** Publication is a separate, later, explicitly authorized action.

## Proposed tag and title

Tag `v2.0.2`; release title exactly `v2.0.2`.

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
Four new supporting rule files were added, one per extraction, each inside an already-existing
skill's own directory. Existing responsibilities, approvals, and verification requirements were
preserved, confirmed through source review. The remaining content is maintainer tooling and
documentation with no consumer-facing effect.

The optional extraction of `implement-it/rules/verification.md`'s reproducible-install guidance was
separately considered and left together rather than split out; that is a closed assessment, not an
open item for this release.

## Complete proposed release-note text

> Clearer supporting rules, a reproducible context-measurement tool, and expanded documentation.
>
> ### What changed
>
> - **Supporting rules.** Separated conditional planning, implementation, and delivery guidance in
>   `document-it`, `implement-it`, `ship-it`, and `plan-it` into focused, conditionally-loaded files.
>   Existing responsibilities, approvals, and verification requirements were preserved, confirmed
>   through source review.
> - **Context guide.** Replaced dated measurement tables with a reproducible script and explicit
>   per-workflow definitions for estimating each skill's context cost.
> - **Documentation.** Added a contributor-facing behavior-contract catalogue and a
>   framework-independent testing strategy. Updated skill READMEs and architecture guides to match
>   the current file layout.
>
> ### Install / update
>
> ```shell
> npx skills add 'elieandraos/agentic-engineering#v2.0.2'
> ```
>
> Select the skills and agent targets your project uses. Refresh complete skill directories to
> include the new supporting files.
>
> ### Validation
>
> Checked through source review and the measurement script's output. Measured file sizes, modeled
> per-workflow totals, and actual session consumption remain distinct measures; this release reports
> the first two only. Live skill execution and consumer installation were not included in the
> recorded validation.

## What remains unresolved

Human authorization to publish is the only open decision: this proposal creates no tag and no
GitHub release. Target SHA, scope, and release-note text are settled as of `c9d73ea`, pending final
review.
