# Sequencing

## Discovered work: sequence by the finding's own scope, not the planned-batch template

The backend/TDD-before-frontend convention below governs **planned feature work** — a whole capability's issues drafted together, with a real dependency graph running across the batch. A standalone Discovered-work issue (`rules/discovered-work.md`) is not automatically subject to it just because it happened to surface while a feature or milestone was in progress.

- Sequence a discovered finding according to its own actual dependency graph and scope — nothing more.
- A frontend-only discovered bug with no backend prerequisite is implemented directly. It does not wait for, or get paired with, a backend batch that doesn't exist for it.
- A backend-only discovered defect proceeds without inventing a frontend batch to go alongside it.
- The backend/TDD-before-frontend convention still applies when the discovered finding is genuinely part of a larger planned capability already being batched that way — e.g. a gap discovered in a feature whose backend and frontend issues are still being drafted together. The test: is this finding actually entangled with that capability's own dependency graph, or did it just happen to surface while working on it? Only the former inherits the batching convention.

Phase 22's three findings are the evidence this rule was extracted from, not a checklist to replay: #294 (stale `register()` references in two Vue files) was purely frontend, with no backend dependency to wait on. #295 (the silent 2FA reset) and #296 (the Inertia response mismatch, plus its small flash-message fix) were both backend-only, sequenced and implemented as their own single coherent issue with no frontend batch manufactured to match the planned-feature template. None of the three needed — or got — a two-batch structure; each was sequenced by what it actually depended on.

## Backend/TDD first, frontend second — as separate batches, shaped by the feature's dependency graph

Backend/TDD work is drafted, created, and implemented before any frontend/UI issue — for both resource-shaped and capability-shaped features. An example from this project: Phase 17's history (issues #198–#210) is the resource-shaped template — every backend/TDD issue landed before any frontend/UI issue — and Phase 21 (Notifications, cross-cutting) confirms the same discipline holds for capability-shaped features too, even though the batch composition looks different there. There's no fixed "one issue per CRUD layer":

1. **Batch 1 — backend/TDD.**
   - Resource feature (`rules/resource-feature-checklist.md`, Classification A/C): migrations, models, policies, requests, resources, actions, controllers, routes, seeders, and their tests. Vue pages can stay minimal stubs at this stage if useful for manually poking at the endpoint — that's what Phase 17 did.
   - Cross-cutting capability (`rules/capability-checklist.md`, Classification B/D): a shared-infrastructure issue first — landable and testable in isolation, no user-visible change — then the integration issues that depend on it, each wiring one concrete business event or capability into that infrastructure. Questions 2–7 in `rules/capability-checklist.md` determine this batch's shape; nominal cleanup issues (renames, tenancy fixes) that surface along the way are their own small issues, not folded into a bigger one.
2. **Batch 2 — frontend/UI wiring.** Drafted only after `rules/design-reconciliation.md` (when frontend is in scope at all — see that file's "conditional, not universal" note), so any design-vs-shipped-app disagreements are resolved before these issues are written.
   - Resource feature: real Vue pages, empty states, filters, mobile/desktop structure, plus UI wiring for backend capability that already exists (e.g. Archive/Unarchive frontend wiring is its own issue, not assumed to ride along with the backend one).
   - Cross-cutting capability: shared frontend plumbing (types/registry/listener fixes) first, then any shared UI component, then per-page/per-resource integration issues — never interleaved ahead of the backend capability they consume.

Dependencies determine the exact shape and count in both cases — don't force a feature into a fixed issue-per-layer template just to match a prior feature's count.

## Draft first, create only on explicit approval — two separate review surfaces

Default posture: build canonical issue definitions for the full milestone before creating anything (see `SKILL.md` — canonical definitions are the source of truth, never a previously rendered preview). Review happens in two stages, detailed in `rules/review.md`:

- **Content review** — a full rendered draft (title, labels, dependencies, context, tasks, acceptance criteria) generated from the canonical definitions, immediately validated with `rules/review.md`'s issue-body content integrity check before it's shown, so the user reviews scope, acceptance criteria, and self-containedness together — not a draft that still has planning-only references or thin Context in it.
- **Final creation review** — after any revision, re-run `rules/review.md`'s canonical structural-integrity check against the (revised) canonical definitions, render the compact manifest, then run `rules/review.md`'s rendered-manifest integrity check against that render before showing it. Never a full re-render, and never an unvalidated manifest — a manifest that fails this check is not shown; it's regenerated and re-checked.

Immediately before `gh issue create` or `gh issue edit` actually runs — after manifest approval, right at the point of truth — render each issue body from its canonical definition one more time and re-run issue-body content integrity against it. A revision applied between content review and final approval could have reintroduced a problem the first pass already caught; this second pass is what stops it from ever reaching GitHub.

Don't run `gh issue create` until the user has explicitly approved the compact manifest and every issue body has passed issue-body content integrity. An example from this project: both Phase 17's gap-filling issues (#211–#223) and Phase 21's issues (#274–#284) were actually handled this way — drafted, shown, confirmed, then created.

This skill's responsibility ends at issue creation. Commit structure and commit message conventions belong to whichever implementation skill picks up the approved issue — see `SKILL.md`'s closing note.
