---
name: my-feature-planning
description: "Personal workflow for planning a feature end-to-end before writing any code — a brand-new CRUD resource (e.g. Carriers, Agents), a cross-cutting application capability (e.g. Notifications), or a scoped extension/refactor that deserves its own milestone. When `my-architecture-laboratory` has already produced an approved, initiative-specific `plan.md` section (its Plan Synthesis track), this skill treats it as the canonical input for architecture and locked decisions instead of re-deriving them from conversation — see `rules/plan-md-input.md`. Covers feature-shape classification, a scope checklist tailored to that shape, a design-vs-shipped-app reconciliation pass against `_design/*.jsx` mockups when frontend is involved (including reconciling against a plan.md-locked design decision, and distinguishing stale design drift from a genuine unresolved product disagreement), an explicit propose-then-approve workflow for GitHub milestone/label metadata, canonical-issue-definition drafting (titles, labels, context-first issue bodies, task checklists, acceptance criteria/tests), an issue/dependency review pass with conditional extensibility-claim validation, structural-integrity validation, and TDD-first-then-UI sequencing. Trigger when the user asks to plan, scope, or scaffold a feature; says things like \"let's plan out X\", \"create issues for X\", \"scope this feature\", \"plan the approved X from plan.md\", \"turn this plan into a milestone/issues\" — whether X is a new CRUD resource, a cross-cutting capability, or an extension/refactor. Also trigger when an unexpected finding surfaces during implementation, code review, manual smoke testing, or production/debugging that needs triage into scoped work — \"smoke testing found a bug, figure out what's going on\", \"investigate this and open an issue if one's warranted\", \"turn this finding into an issue\" — see `rules/discovered-work.md` for the investigate-before-issue intake this skill runs for that path, distinct from already-scoped feature planning. This skill only plans, drafts, and reviews GitHub milestones/issues — it does not implement Laravel code, and it does not produce or amend `plan.md` itself (that's `my-architecture-laboratory`'s job). See `README.md` for a plain-English walkthrough of the workflow and its boundaries before diving into the operational rules here and in `rules/`. Always load ALONGSIDE `my-laravel-patterns` and `laravel-best-practices` once implementation starts."
---

# My Feature Planning

Personal workflow for turning "let's build a feature" into a milestone and a reviewed, drafted set of GitHub issues. The methodology is generic — classify, scope, reconcile design, draft, review, sequence, create — with this project's conventions (Laravel/Vue patterns, milestone naming, label palette) supplying the specifics inside that shape. Examples throughout the rule files are drawn from how Carriers (Phase 17, resource-shaped) and Notifications (Phase 21, cross-cutting capability) actually played out in this project, including what Phase 17 had to retrofit after the fact and the preview-assembly failures hit twice while drafting Phase 21 — they illustrate the rules, they don't define them.

## A minimal human prompt is enough

This skill owns the workflow knowledge — detecting a `plan.md` input, recognizing a Discovered-work finding, classifying the feature, loading the right checklist, querying project metadata, drafting issue context/tasks/acceptance criteria, running review, and asking only genuinely unresolved questions. A prompt like "Plan this feature" or "Plan this initiative from the approved plan.md" is sufficient; the human doesn't need to restate the workflow, name which checklist applies, or specify the milestone/label mechanics themselves. Neither does a prompt that just reports a finding — "smoke testing found a bug, figure out what's going on and open an issue if one's warranted" is enough to trigger the Discovered-work intake below.

## Two work origins: Planned vs. Discovered

Not everything this skill drafts starts from already-understood scope.

- **Planned work** — starts from scope that's already understood or approved: a feature ask in conversation, or an approved `plan.md` section (`rules/plan-md-input.md`). Runs the workflow below unchanged, starting at classification.
- **Discovered work** — starts from evidence of something unexpected found during implementation, code review, manual smoke testing, production/debugging, or another workflow. Scope — and sometimes the underlying cause — isn't known yet at the moment it's noticed. This needs an investigation/validation pass, `rules/discovered-work.md`, before there's anything to classify. That pass ends exactly where Planned work starts: a validated finding ready to go through classification, drafting, and review below.

Both origins converge on the same canonical-issue pipeline and the same review bar (`rules/review.md`) once there's a validated finding or an approved feature ask — Discovered work doesn't get a lighter-weight issue, and none of Planned work's rules change because this path exists.

## Quick Reference

0. Discovered-work intake → `rules/discovered-work.md` — when the starting point is an unexpected finding rather than already-approved scope: don't fix the code or file an issue from the first symptom, investigate proportionally, and validate the finding before it enters the pipeline below
1. Plan.md input → `rules/plan-md-input.md` — when an approved, initiative-specific `plan.md` section exists (from `my-architecture-laboratory`'s Plan Synthesis), treat it as canonical for architecture and locked decisions; otherwise skip straight to classification
2. Feature classification → `rules/feature-classification.md` — resource/CRUD, cross-cutting capability, extension, or refactor milestone
3. Scope checklist → `rules/resource-feature-checklist.md` (shape A, or the CRUD slice of C) or `rules/capability-checklist.md` (shape B, loosely D)
4. Design reconciliation → `rules/design-reconciliation.md` — only when frontend/UI is actually in scope; also governs how a plan.md-locked design decision interacts with a `_design/*.jsx` mockup
5. Issue conventions → `rules/issue-conventions.md` — the portable `<Area/Capability>: <action or outcome>` title convention, context-first issue body, task checklists, acceptance criteria/tests, explicit milestone/label proposal-and-approval (including when an optional milestone description is warranted, and the persistent-backlog vs. delivery/phase distinction)
6. Sequencing → `rules/sequencing.md` — for planned feature work: backend/TDD batch, then frontend batch, then the two-stage approval flow; for a standalone discovered-work issue, sequence by its own dependency graph instead of that batch template
7. Review → `rules/review.md` — issue quality, dependency quality, extensibility-claim validation, canonical structural integrity (validates the issue definitions), rendered manifest integrity (validates the final manifest actually matches those definitions), issue-body content integrity (validates each rendered body is self-contained and developer-ready), post-mutation validation (validates every GitHub mutation, at creation time and on any later change, with a compact change summary)

## Canonical issue definitions are the source of truth

Maintain one canonical definition per proposed issue — sequence number, title, batch, labels, dependencies, task checklist, acceptance criteria/notes. Reason about and revise *these*, never a previously rendered preview. Every rendered output — the full content-review draft, the compact final manifest, and every `gh issue create` call — is generated fresh from the canonical definitions. Never reconstruct an issue body by copying from an earlier chat render. This is the rule that prevents the duplicated-heading / misplaced-acceptance-criteria failure hit twice while drafting Phase 21: a preview is a one-way rendering of the canonical set, not a record to re-derive it from.

Being generated from the canonical definitions doesn't make a render trustworthy by construction — rendering is still a generative step that can silently drop, duplicate, retitle, or reorder a row. The final compact manifest is therefore mechanically verified against the canonical definitions before it's ever shown — see "Rendered manifest integrity" in `rules/review.md`.

## Acceptance criteria vs. task checklists

A task checklist says **where to work** (which files/classes/tests). Acceptance criteria say **what must remain true when the issue is done** — the architectural or product guarantees planning actually surfaced (e.g. "tenant scope comes from `OrganizationContext`, never actor identity", "dispatch only after the mutation commits", "one event, two audiences, two classes"). Not every issue needs both in depth — a one-file frontend wiring issue can be tasks-only — but when planning surfaces a real invariant, it belongs in the issue as acceptance criteria, not buried in a vague "add tests" bullet.

## GitHub issues must stand alone

> A created GitHub issue must remain understandable if `plan.md`, the architecture conversation, the planning transcript, and this skill's own output all disappeared tomorrow.

`plan.md` (when it exists — `rules/plan-md-input.md`) is the upstream architecture/planning artifact; a GitHub issue is the downstream execution artifact, and the two have different lifespans. In this project specifically, `plan.md` sections get deleted once the corresponding work ships (verifiable in its own commit history — completed initiatives are routinely trimmed out), so anything an issue body needs to be understood must live in the issue itself, not behind a citation into a file that may not say that anymore by the time someone reads the issue.

The issue may briefly summarize a relevant architectural/product decision when doing so improves clarity — that's encouraged, not forbidden. What's forbidden is citing the decision instead of explaining it:

- **GOOD:** "Public self-registration is being removed because accounts will enter the system only through controlled provisioning or invitation."
- **BAD:** "Implements LOCKED decisions 1 and 5 from plan.md."

The first is understandable on its own. The second requires the reader to go find external planning context that may no longer exist. See `rules/issue-conventions.md` for the full reference-syntax rules this implies, and `rules/review.md`'s "Issue-body content integrity" for how it's mechanically validated before anything touches GitHub.

### A GitHub dependency is not an excuse to skip explaining what it provides

`Depends on #N` is a real, legitimate reference — unlike a `plan.md` decision number, the target
issue actually exists and isn't getting pruned. That legitimacy doesn't extend to the *behavior*
behind it: a dependent issue must still briefly summarize, in its own words, whatever part of the
dependency's behavior is necessary to understand the dependent issue's own scope and outcome.

- The dependency link is where the full contract lives — don't re-derive or restate it.
- The dependent issue owes the reader a concise reminder of what that dependency actually *does*
  for this issue specifically — one or two sentences, not a re-explanation of the dependency's own
  implementation.
- Don't duplicate the dependency issue's Context, Tasks, or Acceptance Criteria.
- Don't force this summary into every dependency — only when the relied-upon behavior is actually
  necessary to understand *this* issue's own outcome and user/system behavior.

The test: **could a developer understand this issue's own outcome and user/system behavior without
opening the dependency?** If the honest answer is no, the issue is doing exactly what "BAD" above
does — citing instead of explaining — just through a real `#N` instead of a fake one. See
`rules/review.md`'s "Issue-body content integrity" for how this is checked alongside the rest of
Context self-containedness.

## Every GitHub mutation is validated and summarized

Any time this skill actually touches GitHub — creating an issue, editing a body, changing a title/labels/milestone/assignee, creating a milestone or label — the mutation ends with a **compact change summary** and a **post-mutation validation pass** that re-fetches the result from GitHub and checks it, per `rules/review.md`'s "Post-mutation validation". This is not limited to the initial batch-creation moment at the end of a first planning pass: a later, narrower request against issues this skill already created (fix a body, retitle one issue, move something to a different milestone) gets exactly the same discipline — update the canonical definition, re-render, re-validate, mutate, then validate-and-summarize the result. Never report a GitHub change as done on the strength of the `gh` command succeeding alone; the proof is in reading the state back.

## Workflow

**Before step 1: is this Planned or Discovered work?** If the starting point is an unexpected finding rather than already-approved scope (implementation, code review, manual smoke testing, production/debugging, another workflow), run the Discovered-work intake (`rules/discovered-work.md`) first. Do not fix code or draft an issue from the first symptom. That intake ends with a validated finding — known/unknown boundary stated, reproduced where practical, blast radius understood, defect-vs-intended-behavior resolved, no open product/architecture question blocking scope — at which point the numbered workflow below proceeds exactly as it does for Planned work, starting at step 1. If the starting point is already-understood or approved scope, skip straight to step 1.

1. **Check for an approved `plan.md` input.** If a matching initiative-specific section exists and carries Plan Synthesis's approval marker (`rules/plan-md-input.md`), treat its architecture, locked decisions, preserved behavior, and constraints as canonical — don't reconstruct or re-litigate them from conversation. If no matching approved section exists, skip straight to classification; the rest of the workflow is unchanged either way.
2. **Classify the feature** per `rules/feature-classification.md`. This determines which checklist applies — don't apply resource assumptions (migrations, slugs, archive, exports) to a capability with no CRUD spine, and don't skip shared-infrastructure thinking on one that has none.
3. **Load the matching checklist** and resolve every applicable question explicitly (ask the user for genuinely ambiguous ones). Don't silently assume a track or question doesn't apply. When plan.md already answers a question via a locked decision, use that answer directly instead of re-asking; only genuinely open, implementation-level items get resolved fresh here (`rules/plan-md-input.md`).
4. **Reconcile `_design/`** per `rules/design-reconciliation.md` — only for issues with frontend/UI scope; backend-only or non-UI capability issues skip this entirely. If frontend design is needed but the matching file is missing or stale, ask the user rather than inventing layout. If plan.md already locked a design decision, this pass confirms nothing's moved since — it doesn't reopen the decision, and a disagreeing mockup never silently overrides it.
5. **Verify/propose milestone + labels** — query existing milestones and labels first, check applicable project conventions, then explicitly propose names/colors and show what already exists vs. what's proposed. Propose a milestone description too, but only when the milestone's intent, boundaries, exclusions, governing principles, or completion criteria aren't already clear from the title and issue set alone (`rules/issue-conventions.md`) — most milestones don't need one. Create nothing until the user approves.
6. **Build canonical issue definitions** — one per issue: `## Context` (why it exists, outcome, constraints, in/out of scope, dependencies) before `## Tasks` (where to work), with `## Acceptance Criteria` and `## Tests` added only where they earn their place — formatted per `rules/issue-conventions.md`.
7. **Sequence the work according to the feature's actual dependency graph**, using backend/TDD-before-frontend as this project's default where applicable, per `rules/sequencing.md` — batch shape follows that dependency graph, not a fixed issue count copied from a prior feature. A standalone Discovered-work issue is not forced into that batch template just because it surfaced during a feature's planning or implementation — `rules/sequencing.md`'s discovered-work carve-out applies instead unless the finding is genuinely entangled with that feature's own dependency graph.
8. **Run the review pass** — `rules/review.md`'s issue-quality, dependency-quality, and extensibility-claim checks — against the canonical definitions.
9. **Render the full draft** (title, labels, dependencies, context, tasks, acceptance criteria/tests per issue) from the canonical definitions. This is the first, substantive content-review surface — immediately run **issue-body content integrity validation** (`rules/review.md`) against every rendered body before presenting it. If any body fails, fix the *canonical definition* (never patch the rendered text) and re-render before showing the draft.
10. **Apply any requested revisions directly to the canonical definitions**, never to the rendered text.
11. **Re-run canonical structural-integrity validation** (`rules/review.md`) against the canonical definitions after every revision.
12. **Render the compact manifest, then immediately run rendered-manifest integrity validation** (`rules/review.md`) against it — a mechanical diff of the rendered rows against the current canonical definitions (count, sequence numbers, titles, order, no additions/omissions/duplicates). This runs every time the manifest is shown, including re-shows after a revision. If it fails, do not show the manifest — report which row(s) diverged, regenerate the render from the canonical definitions, and re-validate before proceeding.
13. **Show the validated compact manifest only** for the final approval pass (`# | title | labels | depends on` + a short validation summary confirming the canonical structural-integrity and rendered-manifest integrity checks passed). Don't re-render full issue bodies unless the user explicitly asks to inspect them again.
14. **Immediately before creating or updating any GitHub issue**, render the final issue body straight from its canonical definition and run **issue-body content integrity validation** (`rules/review.md`) against it one more time — the last gate before anything touches GitHub, since a revision made after step 9's check could have reintroduced a problem. If it fails, do not create/update that issue — report the exact issue and field that failed, fix the canonical definition, re-render, and re-validate.
15. **Only after the user has explicitly approved both the final compact manifest/issue set and the proposed GitHub metadata (milestone and labels), and every body has passed issue-body content integrity**, create issues via `gh issue create` in dependency-safe canonical order, generated straight from the canonical definitions.
16. **Map canonical dependencies to real GitHub issue numbers** as each issue is created, substituting them into later issue bodies — no planning-only `#N` reference survives into a created issue.
17. **Run post-mutation validation** (`rules/review.md`) — re-fetch every created/updated issue from GitHub and check it against the canonical definitions, then report a compact change summary (mutation type, per-issue one-liner, validation result). This is not a one-time step tied to initial creation: any later request that mutates an already-created Phase's issues (fixing a body, retitling, relabeling, remilestoning) ends the same way — canonical definition updated first, mutation applied, then this same validate-and-summarize pass, every time.
18. Stop. Planning's responsibility ends at issue creation — application code, implementation conventions, and commit structure/messages belong to `my-laravel-patterns` (+ `pest-testing`, `laravel-best-practices`) — load those when work on an approved issue actually begins.

Never load this skill alone when writing code — once an issue is approved and implementation starts, switch to the implementation skills instead. This skill stays self-contained for planning: it names the pieces an issue needs (FormRequest, Action, Policy, API Resource, thin Controller, factory/seeder, tests) without requiring the implementation-convention skills to be loaded during planning.
