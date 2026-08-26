---
name: my-feature-planning
description: "Plans a feature end-to-end into GitHub milestone/label metadata and a reviewed, drafted set of issues — classify, scope, draft, review, and create only after approval. Trigger when asked to plan, scope, or scaffold a feature, or to turn an approved plan.md initiative into milestones/issues. When `my-architecture-laboratory` has already produced an approved, initiative-specific `plan.md` section, treat it as canonical input instead of re-deriving decisions from conversation — see `rules/plan-md-input.md`. Also trigger when an unexpected finding needs investigation before deciding whether it's issue-worthy — see `rules/discovered-work.md`. This skill only plans, drafts, and reviews GitHub milestones/issues; it does not implement code, and does not produce or amend `plan.md` itself (that's `my-architecture-laboratory`'s job). See `README.md` for a plain-English walkthrough."
---

# My Feature Planning

Personal workflow for turning "let's build a feature" into a milestone and a reviewed, drafted set of
GitHub issues. The methodology — classify, scope, reconcile design, draft, review, sequence, create —
is portable across GitHub-based projects; each consuming project supplies its own stack conventions
inside that shape. See `README.md` for the plain-English walkthrough and reasoning.

## Two work origins

- **Planned work** — scope is already understood or approved: a feature ask in conversation, or an
  approved `plan.md` section (`rules/plan-md-input.md`). Enters the pipeline below at classification.
- **Discovered work** — starts from an unexpected finding (implementation, code review, manual
  testing, production/debugging, another workflow) with scope not yet known. Runs
  `rules/discovered-work.md`'s investigation first; only a validated finding enters the pipeline.

Both origins converge on the same canonical-issue pipeline and the same review bar — Discovered work
never gets a lighter-weight issue.

## Pipeline

1. Consume an approved `plan.md` input when one exists (`rules/plan-md-input.md`); otherwise skip to
   classification.
2. Classify the feature — resource/CRUD, cross-cutting capability, extension, or refactor
   (`rules/feature-classification.md`).
3. Load the matching scope checklist and resolve every applicable question
   (`rules/resource-feature-checklist.md` or `rules/capability-checklist.md`).
4. When frontend/UI is in scope, reconcile the project's available design artifacts against the
   shipped application and any approved architecture decisions (`rules/design-reconciliation.md`).
5. Draft canonical issue definitions (`rules/issue-conventions.md`).
6. Sequence the work by its actual dependency graph and run the review pass
   (`rules/sequencing.md`, `rules/review.md`).
7. Propose milestone/labels and get explicit human approval before creating anything.
8. Create GitHub issues in dependency-safe order and validate every mutation by reading state back.

## Non-negotiable contracts

- An approved `plan.md`'s locked decisions are never re-litigated during planning.
- Canonical issue definitions are the source of truth — every rendered draft, the compact manifest,
  and every `gh issue create` call are generated fresh from them, never from a prior render.
- A created GitHub issue must stand alone — understandable even if `plan.md`, the planning
  conversation, and this skill's own prior output all disappeared.
- Two review surfaces gate creation — a full content review, then a final compact-manifest/metadata
  approval — and nothing (no milestone, label, or issue) is created until both are approved.
- Every issue body is re-validated against its canonical definition immediately before it touches
  GitHub, and every mutation is re-fetched from GitHub and validated again afterward, at creation and
  on any later change — a `gh` command succeeding is never treated as proof by itself.

Full mechanics for all of the above: `rules/review.md`.

## What it owns

Feature classification, scope discovery, discovered-work investigation/triage, design reconciliation,
issue drafting, dependency-aware sequencing, review, milestone/label proposals, and GitHub issue
creation after approval.

## What it does not own

Application implementation, framework-specific conventions, test implementation details, commit
structure/messages, fixing a defect it discovers, and deciding when a milestone closes.

## Rule index

- `rules/plan-md-input.md` — consuming an approved `plan.md` section as canonical input.
- `rules/discovered-work.md` — investigating an unexpected finding before it's classified.
- `rules/feature-classification.md` — which shape a feature is, and which checklist applies.
- `rules/resource-feature-checklist.md` / `rules/capability-checklist.md` — shape-specific scope
  questions.
- `rules/design-reconciliation.md` — reconciling design artifacts against the shipped app when UI is
  in scope.
- `rules/issue-conventions.md` — issue format, and milestone/label proposal-and-approval.
- `rules/sequencing.md` — batch order and dependency-driven sequencing.
- `rules/review.md` — issue quality, structural/rendered/content integrity, and post-mutation
  validation.

## Handoff

Planning's responsibility ends at issue creation. Once an issue is approved and implementation
starts, switch to the consuming project's own implementation skills — never write code from this
skill alone.
