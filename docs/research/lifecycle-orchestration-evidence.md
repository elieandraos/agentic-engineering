# Lifecycle Orchestration Evidence — Phase 26 Review Feedback

Status: Evidence. Observed during normal useOrbit work after Agentic Engineering v2.2.0 was released.

## Observation

During manual code review of useOrbit Phase 26, the human supplied raw implementation observations: repeated action/request/resource patterns, controller shape questions, authorization versus domain guards, test-data conventions, query choices, and an unexplained failing local suite.

Before `lab-it` could investigate those questions effectively, the coordinating session performed work above the Lab skill:

- treated the observations as questions rather than approved solutions;
- challenged premature abstractions such as DTOs, factories, and refactors proposed from IDE suggestions;
- grouped file-level observations into broader architecture themes;
- selected Lab before Plan because architecture decisions were still unresolved;
- preserved the active application context: open Phase 26 PR, existing milestone, and later corrective issues belonging to that milestone;
- instructed Lab to distinguish project-specific findings from reusable Laravel-stack findings and portable Agentic Engineering findings;
- preserved application delivery as the primary goal while retaining evidence for later methodology/stack improvement;
- defined the handoff boundary: Lab report and human decision first, then Plan, then implementation only after separate authorization.

## Why this is not simply lab-it

`lab-it` owns architecture investigation: inspect evidence, challenge assumptions, answer architecture questions, and produce approved intent.

The coordinating behavior above decides **when Lab is the right stage, what surrounding lifecycle state must survive the investigation, where resulting knowledge belongs, and what stage follows after human approval**. Moving all of that into `lab-it` would mix architecture investigation with lifecycle routing, project-state coordination, and stewardship across knowledge boundaries.

No parallel workers were required for this observation.

## Knowledge-boundary signal

One real application investigation can produce evidence for several destinations without making those destinations the same concern:

```text
real project work
      |
      +--> project decision / Phase 26 issues
      +--> stack-companion candidate / laravel-inertia-stack
      +--> portable methodology candidate / Agentic Engineering
```

The coordinating layer retains those lenses while the specialist skill stays focused on its own job.

## Plan-stage recurrence

The same coordinating responsibility recurred immediately after the Lab report was approved and `plan-it` produced its first issue draft.

`plan-it` correctly transformed approved architecture into implementation-ready issue content, dependencies, labels, milestones, acceptance criteria, and verification. The coordinating session still had to reconcile that specialist output with broader project and lifecycle intent:

- keep eight corrective/refactoring issues in the still-open Phase 26 milestone because they came from review of that milestone's unmerged PR;
- route the pre-existing client/carrier soft-delete behavior to Backlog because it requires a product decision rather than silently folding it into Phase 26;
- route the mixed `readonly` service/action style to a separate Backlog convention decision rather than changing one feature family locally;
- challenge test-count preservation as an accidental metric and preserve coverage intent instead;
- recognize that Plan's suggested execution waves were recommendations, not dependencies, and avoid adding redundant instructions for sequencing behavior already owned by the released methodology;
- stop after issue creation because implementation had not been authorized.

This is a second stage in the same real workflow, not a second independent project occurrence. It strengthens the shape of the candidate responsibility without yet satisfying the extraction bar.

The boundary is clearer:

- `plan-it` owns turning approved intent into coherent, implementation-ready GitHub issues;
- the coordinating layer owns reconciling that output with the surrounding lifecycle, project state, unresolved human decisions, and what should happen next.

## Candidate responsibility

This is evidence for a broader Control Room hypothesis:

> Orchestration is not only cross-worker coordination. It may also own lifecycle routing and context across specialist skills while preserving project, stack, and portable-methodology knowledge boundaries.

A lifecycle shape now observed through both Lab and Plan is:

```text
human observations
      |
      v
coordinating context
  - understand current project/lifecycle state
  - challenge premature solution framing
  - select the needed stage
  - preserve evidence destinations
      |
      v
lab-it
      |
      v
human architecture decision
      |
      v
plan-it
      |
      v
later implementation
```

This does **not** imply that an orchestrator artifact, agent, skill, or process has been selected.

## Classification

- **Observed behavior:** yes, during normal post-v2.2.0 useOrbit review.
- **Parallel-specific:** no.
- **Belongs in lab-it:** only the architecture investigation itself.
- **Orchestration candidate:** lifecycle routing, surrounding-state preservation, and cross-knowledge-boundary evidence retention.
- **Extraction status:** evidence worth retaining; do not extract yet from this single non-parallel occurrence.
- **Plan-stage recurrence:** observed within the same Phase 26 review workflow; specialist output still required lifecycle/project reconciliation above `plan-it`.
- **Next evidence:** observe whether the same coordinating responsibilities recur naturally through implementation/review/ship and in later independent workflows.
