# Agentic Engineering v3 — Execution Architecture 2

Status: Investigation.

This document follows `v3-execution-architecture.md`.

The first execution architecture describes the separation between engineering methodology, Control Room, runtime companions, and workers. Real useOrbit orchestration experiments now give us enough evidence to refine one important boundary: **orchestration can coordinate workers, but it must not silently redefine the engineering lifecycle owned by the skills those workers execute.**

This document records that evidence and the execution contract it suggests. It is a research artifact, not a final runtime implementation contract.

## What the first orchestration experiments showed

Two parallel implementation experiments have now been run in useOrbit.

### Experiment 1 — shared integration surface

Issues `#346`, `#347`, and `#348` were dispatched as three isolated workers.

All three worked independently and then returned to the shared feature branch. Each worker touched `PolicyMedicalDetailShell.vue`, so the integration step produced small, expected merge conflicts.

The experiment demonstrated:

- isolated worktrees can execute independent issues concurrently;
- the coordinator can collect completed worker branches;
- predictable shared-file conflicts can be resolved during integration;
- a combined verification pass can validate the merged result.

The important limitation was that the experiment still left the human approval lifecycle mostly outside the worker orchestration question.

### Experiment 2 — independent backend surfaces

Issues `#328`, `#329`, and `#330` were dispatched as three isolated workers.

These issues had the same architectural shape but independent backend files, so they were a cleaner parallel batch than `#346–348`.

The workers completed concurrently. Their branches were merged into `feat/policies-http-frontend`, with two small route-file conflicts resolved during integration. The coordinator then ran the combined verification: the full Pest suite, Pint, and the frontend build all passed.

The parallel execution itself worked well. The important finding was elsewhere.

## The orchestration boundary that failed

The coordinator instructed each worker to reach a **committed and issue-closed** state while also telling it not to push its branch.

That shortcut bypassed the existing `implement-it` lifecycle.

The workers followed the instruction correctly. They completed implementation, testing, review, commits, and local issue closure. But the owning `implement-it` rules require remote reachability before issue closure, and issue closure is explicitly a human-authorized action.

The result happened to be safe because every branch was later merged successfully and the combined branch was verified before being pushed. The execution was therefore successful in outcome, but the orchestration contract was wrong at decision time.

The important lesson is:

> **A coordinator may change how work is scheduled and integrated. It must not silently waive or reinterpret human gates owned by the engineering skills.**

If a different worker had failed to merge, or the integration step had been abandoned, GitHub could have contained closed issues whose implementation was not present on the shared branch.

Nothing should depend on that later success to make the earlier authorization decision valid.

## Three layers, three ownership boundaries

The existing execution architecture separates three layers:

```text
Agentic Engineering
        ↓
Control Room
        ↓
Execution Runtime
        ↓
Workers
```

The experiments suggest a more precise responsibility split.

### Agentic Engineering owns

- engineering methodology;
- issue lifecycle rules;
- verification requirements;
- implementation and review contracts;
- commit boundaries;
- human approval semantics;
- issue-closure preconditions;
- stack-specific engineering knowledge.

These remain true whether an issue runs alone or as part of a parallel wave.

### Control Room owns

- selecting dependency-ready work;
- deciding whether work can safely run in parallel;
- selecting worker roles;
- creating execution waves;
- assigning issues to workers;
- collecting worker results;
- coordinating integration;
- deciding when execution should wait;
- presenting the appropriate human decision point.

Control Room may coordinate the engineering lifecycle. It should not invent a second lifecycle beneath it.

### Runtime companions own

- worktree creation;
- branch/workspace mechanics;
- worker process creation;
- session launch and resume;
- waiting and messaging;
- cleanup;
- runtime result collection.

The runtime should not decide whether an engineering gate is satisfied.

## Workers remain skill-owned

A worker may be an execution object created by Control Room, but its engineering responsibility still comes from the selected skill.

For an implementation worker, the relevant contract remains `implement-it`.

Conceptually:

```text
Control Room
    │
    │ assign issue #328
    ▼
Implementation worker
    │
    │ execute
    ▼
implement-it contract
    │
    ├── implementation
    ├── verification
    ├── review-it
    ├── Gate 1
    ├── Gate 2
    ├── push readiness
    └── issue closure
```

The coordinator may decide **when** that worker runs and **where** its branch is integrated. It should not quietly delete steps from the worker's engineering contract.

## Parallelism does not automatically flatten human gates

Parallel execution creates a natural temptation to replace several issue-level approvals with one wave-level approval.

That may eventually be a useful optimization, but it is not automatically valid.

The current evidence supports a conservative rule:

> **Parallelism changes scheduling, not authorization.**

A future orchestration design may discover that some gates can be safely grouped. For example, an integration gate could potentially review several completed worker results together. But such a change needs an explicit contract that answers:

- what exactly the human is approving;
- which worker outputs are included;
- which worker-level approvals remain individual;
- whether push and issue closure are still separately authorized;
- what happens when one worker changes after the group approval;
- how a partial failure affects the rest of the wave.

Until those questions are settled, the orchestrator should preserve the existing skill-owned gate semantics.

## Integration is a separate responsibility

The experiments also suggest that **integration is not the same thing as implementation**.

A worker can finish a valid issue while its branch is still outside the shared feature branch.

The coordinator therefore needs an integration phase that can:

1. identify completed worker branches;
2. verify the expected issue/result mapping;
3. merge compatible branches;
4. resolve authorized integration conflicts;
5. re-run the appropriate combined verification;
6. present the resulting integrated state for the next human decision.

This phase should not be hidden inside worker implementation prompts.

The first experiment showed why. Three workers can each be correct while their branches still require coordination before becoming one coherent feature branch.

## A better execution shape

The observed work suggests this model:

```text
                 Control Room
                      │
              dependency graph
                      │
                execution wave
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Worker A    Worker B    Worker C
       issue 328   issue 329   issue 330
          │           │           │
      skill-owned skill-owned skill-owned
       lifecycle   lifecycle   lifecycle
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Integration
                      │
             combined verification
                      │
               human decision
                      │
                 next action
```

The diagram deliberately keeps the worker lifecycle intact while moving scheduling and integration above it.

## Partial failure becomes a first-class problem

A parallel wave is more complicated than three serial issues even when every worker uses the same skill.

The coordinator must be able to represent states such as:

```text
A complete
B complete
C failed
```

or:

```text
A complete
B waiting for human decision
C complete
```

The correct response is not to pretend that the wave succeeded or to close every issue uniformly.

Instead, Control Room needs to know:

- which workers are complete;
- which are blocked;
- which branches are safe to integrate;
- which human decision is currently required;
- which downstream issues remain blocked;
- whether completed work should be preserved or discarded.

This is one reason orchestration is a methodology rather than merely a process launcher.

## Worktree and branch ownership

The experiments also clarified a useful distinction.

A worker should normally own:

- its worktree;
- its topic branch;
- its issue-specific implementation;
- its local verification state.

Control Room should own:

- the selection of the worker;
- the execution wave;
- integration into the shared feature branch;
- the combined verification decision;
- the final progression of the milestone.

This avoids turning shared branches into shared worker workspaces.

It also gives the coordinator a stable way to compare worker outcomes before integration.

## Context propagation remains useful

The earlier `#326 → #327` experiment gives a complementary result.

A completed issue established an architectural decision. That decision was propagated to `#327`. A fresh implementation session fetched the issue and its comments, explicitly acknowledged the decision before writing code, and applied it.

This means orchestration should not need to carry the entire previous conversation into a worker.

A good worker handoff can instead contain:

- the issue;
- applicable propagated decisions;
- relevant constraints;
- the repository/branch/worktree context;
- the required engineering skills.

The worker can then independently re-read authoritative issue context before implementation.

## What this changes in the v3 model

The first architecture already said:

> Control Room makes execution decisions. The runtime executes those decisions.

The experiments add another boundary:

> **Control Room coordinates engineering skills. It does not replace their lifecycle contracts.**

That gives the execution layer three important responsibilities:

```text
Scheduling
Integration
Preservation of engineering boundaries
```

A runtime can execute worktrees and sessions. It cannot decide that a human approval no longer matters merely because three workers are running concurrently.

## What remains open

The experiments do not yet settle the following questions:

### Wave-level gates

- Can some individual gates be safely grouped?
- Which gates must remain issue-specific?
- Can one human approval cover a set of unchanged worker results?
- How should later changes invalidate a grouped approval?

### Worker completion contracts

- What exact state should a worker return?
- Must every worker push its topic branch before closure?
- Should issue closure ever happen outside the worker's normal lifecycle?
- Can the worker stop before closure and hand that responsibility back to Control Room?

### Integration

- Should branches be merged immediately as workers finish, or after the whole wave completes?
- Who owns merge-conflict resolution?
- Which verification belongs to each worker and which belongs to the integrated feature branch?
- How should partially integrated waves recover?

### Runtime

- Which runtime primitives are required to support these contracts?
- Does Herdr need an explicit notion of worker roles and result states?
- What should a runtime companion expose without absorbing engineering policy?

## Current working model

For now, the smallest evidence-backed model is:

```text
Agentic Engineering
    owns the engineering lifecycle

Control Room
    owns scheduling and coordination

Runtime companion
    owns execution mechanics

Workers
    execute bounded engineering responsibility

Integration
    combines worker results without weakening their contracts
```

Do not implement a large orchestration framework from this document yet.

The next useful experiments should deliberately test the unresolved seams, especially:

1. parallel workers with one worker failing;
2. grouped versus individual human gates;
3. integration before all workers finish versus integration after the whole wave;
4. explicit worker result contracts;
5. recovery from a partially integrated wave.

## Guiding principle

The execution layer should evolve from real work:

```text
Observed behavior

↓

Evidence

↓

Explicit decision

↓

Reusable rule
```

The `#328–330` experiment did not show that `implement-it` needs to change. It showed that the layer above it needs to respect what `implement-it` already owns.
