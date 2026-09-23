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

## Candidate responsibility

This is evidence for a broader Control Room hypothesis:

> Orchestration is not only cross-worker coordination. It may also own lifecycle routing and context across specialist skills while preserving project, stack, and portable-methodology knowledge boundaries.

A possible lifecycle shape observed here is:

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
- **Next evidence:** observe whether the same coordinating responsibilities recur naturally when moving from Lab to Plan and later through implementation/review/ship.
