# Agentic Engineering v3 — The Control Room

Status: Investigation.

This document follows `v3-vision.md`, `v3-execution-architecture.md`,
`v3-execution-2-architecture.md`, and `v3-execution-3-architecture.md`.

Those documents built up the execution architecture experiment by
experiment: the three-layer separation, the boundary between
orchestration and engineering lifecycle, and the requirement for an
interactive pause/resume mechanism at human gates.

This document names and consolidates the responsibility that keeps
recurring across all three experiments: **Control Room**.

It does not introduce new evidence. It defines what Control Room is
responsible for, where it sits relative to skills, workers, and
runtime infrastructure, what state it needs to coordinate, and which
parts remain unresolved.

This is not a finalized implementation design.

## Core model

Control Room is a coordination/orchestration responsibility layer
above the existing Agentic Engineering skills.

Today, the ChatGPT project effectively acts as the Control Room
through conversation state:

```text
You
  ↓
ChatGPT / Control Room
  ↓
lab-it / plan-it / implement-it / review-it / ship-it
```

The emerging durable model, based on the useOrbit experiments, is:

```text
You
  ↓
Control Room
  ↓
execution runtime
  ↓
workers
```

The rest of this document describes what each layer in that second
diagram is responsible for.

## Control Room

Control Room coordinates execution state and decisions. That includes:

- reading the current issue dependency graph;
- recalculating readiness after meaningful state changes;
- deciding which dependency-ready work can form an execution wave;
- launching or requesting isolated workers;
- tracking worker lifecycle state;
- knowing which workers are implementing, waiting, completed,
  blocked, or failed;
- surfacing human decisions when a worker reaches a human approval
  boundary;
- resuming the specific worker after a human decision;
- coordinating integration;
- distinguishing worker completion from integration readiness;
- presenting the next actionable decision to the human.

### Ownership distinction

Control Room does not replace `plan-it` or `implement-it`. It sits
between the human and the skills, consuming what planning produces and
coordinating what implementation executes.

```text
plan-it
    defines or maintains the engineering dependency graph.

Control Room
    consumes that graph, evaluates readiness, forms execution
    waves, and tracks execution state.

implement-it
    owns the lifecycle for one implementation worker.
```

This mirrors the boundary already established in
`v3-execution-2-architecture.md`:

> Control Room coordinates engineering skills. It does not replace
> their lifecycle contracts.

## Workers

Workers are normal engineering agents, not a separate methodology.

A worker receives:

- an issue;
- a repository;
- a branch/worktree;
- approved context;
- applicable skills;
- applicable stack companions.

It then runs the normal engineering lifecycle — specifically, normal
`implement-it`. There is no separate "parallel implement-it".

This distinction matters because the experiments in
`v3-execution-3-architecture.md` showed that unattended background
workers can accidentally bypass normal human gates when the
orchestration layer has no way to pause and resume them at those
gates. The fix is not a lighter-weight lifecycle for workers. It is
giving the orchestration layer the ability to pause a normal
`implement-it` run at a gate and resume it afterward.

## Runtime

The runtime is execution infrastructure, not methodology.

Possible runtime responsibilities:

- create worktrees;
- create branches;
- launch sessions;
- track sessions/workers;
- pause;
- resume;
- send messages;
- collect results;
- clean up workspaces;
- potentially perform mechanical merge/integration operations.

Herdr is an example of the kind of runtime companion discussed in
`v3-execution-architecture.md`. It is not a formal dependency, and
this document does not claim a final architecture for it. Another
runtime could provide the same capabilities without changing the
Control Room methodology.

## Skills

Skills remain the reusable engineering methodology:

- `lab-it`
- `plan-it`
- `implement-it`
- `review-it`
- `ship-it`

Control Room coordinates skills and workers. It does not replace them.
The engineering lifecycle, gate semantics, and approval requirements
stay owned by the skills, exactly as established in
`v3-execution-2-architecture.md` and `v3-execution-3-architecture.md`.

## State model

The prior execution architecture documents distinguish worker state
from wave state. That distinction carries forward here, refined
slightly with the terminology surfaced in the later experiments.

These are candidate models, not final contracts.

### Candidate worker states

```text
READY
RUNNING
REVIEW_IMPLEMENTATION
WAITING_HUMAN
RESUMING
COMMIT_PLAN
PUSH_READY
CLOSED
FAILED
BLOCKED
```

### Candidate wave states

```text
PLANNED
RUNNING
WAITING_ON_HUMAN
PARTIALLY_COMPLETE
READY_FOR_INTEGRATION
INTEGRATING
VERIFYING
COMPLETE
BLOCKED
```

Neither list should be read as an accepted state machine. They are
working vocabulary for describing what Control Room needs to track.

## Human gates

The parallel experiments recorded in `v3-execution-2-architecture.md`
and `v3-execution-3-architecture.md` are the evidence base for this
section.

Established observations:

- `#339` demonstrated that the normal single-issue lifecycle works.
- `#346`–`#348` demonstrated isolated parallel workers and exposed
  merge/shared-file conflicts.
- `#328`–`#330` demonstrated that parallel workers can bypass the
  normal human approval flow when the orchestration setup is
  unattended.
- `#332`–`#333` demonstrated that even explicitly saying "preserve the
  normal implement-it lifecycle" is insufficient when an unattended
  worker has no mechanism to pause at a human gate and resume
  afterward.

The key architectural conclusion, first stated in
`v3-execution-3-architecture.md`, is:

> An unattended worker cannot perform a real human approval.

Therefore the orchestration layer needs a mechanism for:

```text
worker reaches human gate
    ↓
worker reports "human decision required"
    ↓
Control Room surfaces the decision
    ↓
human approves/rejects
    ↓
Control Room resumes that specific worker
```

The earlier documents used **Gate 1** and **Gate 2** as the internal
lifecycle identifiers for these boundaries. Later discussion surfaced
more human-facing terminology for the same two boundaries:

- **Review implementation** (Gate 1)
- **Commit plan** (Gate 2)

Both sets of names refer to the same underlying approval points. Use
the human-facing terms when describing what a human is being asked to
do, and keep Gate 1 / Gate 2 as internal lifecycle identifiers where
that is more convenient.

One worker waiting for a human must not stop the others from
progressing. For example:

```text
#328  Review implementation → waiting for human
#329  Implementing
#330  Commit plan → waiting for human
```

This is the concurrent-lifecycle model already described in
`v3-execution-3-architecture.md`: Control Room tracks each worker's
position independently and surfaces only the decisions that are
actually ready.

## Integration

Integration stays separate from worker lifecycle completion, as
established in `v3-execution-2-architecture.md`.

For example:

```text
#328 worker complete
#329 worker complete
#330 waiting at Review implementation

Integration:
#328/#329 may be eligible
#330 is not yet eligible
```

Whether integration should happen incrementally as workers become
eligible, or only after an entire wave completes, remains an open
architecture question. Neither prior document settled it, and this
document does not attempt to.

## Agent vs skill vs runtime

The current discussion has surfaced several possible implementation
forms for Control Room, without settling on one:

- Control Room as a coordinator/orchestrator responsibility;
- a possible Control Room **skill** containing reusable execution
  rules;
- a possible Control Room **agent** holding execution state and
  coordinating workers;
- a **runtime companion** providing process/worktree/session
  mechanics.

None of these should be treated as decided. The current evidence only
supports defining Control Room as a responsibility/layer first — what
it must do, not what artifact implements it.

The eventual implementation form (skill, agent, service, or some
combination) remains an open question for later experiments, in
keeping with the open question already recorded in `v3-vision.md`:

> What is the execution-layer artifact?

## Architectural diagrams

Coordination and worker execution, for one wave:

```text
CONTROL ROOM
coordination + state
         │
  dependency graph
         │
   execution wave
         │
  ┌──────┼──────┐
  ▼      ▼      ▼
Worker A Worker B Worker C
  │      │      │
implement-it for each worker
  │      │      │
human gate / running / human gate
  │      │      │
  └──── decisions ────┘
         │
    integration
         │
   combined verify
```

The broader layering, consistent with `v3-execution-architecture.md`:

```text
Agentic Engineering skills
          ↓
     Control Room
          ↓
   Execution runtime
          ↓
  Workers / sessions / worktrees
```

Control Room sits above the runtime. Workers are execution instances
that still run the existing engineering methodology; they are not a
separate layer of methodology.

## Evidence

This document does not introduce new evidence. It draws only on
observations already recorded in the v3 research:

- `#339` established the normal single-issue lifecycle as a clean
  baseline.
- `#346`–`#348` demonstrated isolated parallel workers and exposed
  merge conflicts/shared-resource issues
  (`v3-execution-2-architecture.md`).
- `#328`–`#330` demonstrated parallel workers but bypassed normal
  human approvals (`v3-execution-2-architecture.md`).
- `#332`–`#333` demonstrated that even an explicit "preserve the
  normal implement-it lifecycle" instruction did not preserve human
  gates, because unattended workers had no pause/resume mechanism
  (`v3-execution-3-architecture.md`).

## Open questions

- What is the smallest viable Control Room runtime?
- Should Control Room ultimately be implemented as an agent, a skill,
  a service, or a combination?
- What exact worker-to-Control-Room protocol represents "human
  approval required"?
- How does pause/resume work across real runtimes?
- Where should worker lifecycle state persist?
- Where should merge/integration ownership live?
- Should Control Room inspect likely file/resource conflicts before
  launching a wave?
- What context is shared across workers versus isolated?
- How should partial failure affect the rest of a wave?
- Should integration happen incrementally or only after wave
  completion?

## Guiding principle

Control Room should evolve the same way the rest of Agentic
Engineering evolved:

```text
Observed behavior
    ↓
Evidence
    ↓
Explicit decision
    ↓
Reusable rule
```

Naming the Control Room responsibility does not settle its
implementation. It gives the ongoing experiments a shared vocabulary
for what they are testing.
