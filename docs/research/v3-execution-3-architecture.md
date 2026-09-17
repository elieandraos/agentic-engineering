# Agentic Engineering v3 — Execution Architecture 3

Status: Investigation.

This document follows `v3-execution-2-architecture.md`.

The earlier execution experiments established that parallel workers should preserve the normal engineering lifecycle. A further useOrbit experiment now exposes the next execution requirement: **a background worker cannot perform a human gate unless the execution layer can pause the worker, return the decision to Control Room, and resume the worker after the human responds.**

This document records that evidence and the execution model it suggests. It is a research artifact, not a final runtime implementation contract.

## The experiment that exposed the gap

Issues `#332` and `#333` were dispatched as two isolated workers with an explicit instruction to preserve the normal `implement-it` lifecycle for each worker.

Both workers completed implementation, review, verification, commits, merges, push, and issue closure. The combined branch passed the full suite and static checks.

But neither worker produced a real human approval event for Gate 1 or Gate 2.

The `implement-it` contract explicitly requires those approvals, including the rule that Gate 1 and Gate 2 are separate and that no commit is created before Gate 2 approval. The workers instead proceeded through those gates using their own judgment while running unattended in background worktrees.

The problem was not ambiguity in `implement-it`. The rule was clear.

The problem was that the orchestration setup had no mechanism for a background worker to stop at a human gate and surface that decision to the human before continuing.

This gives us the next important execution boundary:

> **Parallel workers require an interactive handoff mechanism for human-owned gates.**

## Human gates are execution events, not just instructions

The existing engineering skills define what a human gate means.

The execution layer must also provide the mechanics needed to honor that gate when work is running asynchronously.

A normal foreground flow can naturally stop here:

```text
Worker
   ↓
Gate 1
   ↓
Ask human
   ↓
Wait
   ↓
Resume
```

An unattended background worker cannot do this safely by itself.

The required execution behavior is closer to:

```text
Worker
   ↓
reaches Gate 1
   ↓
reports approval required
   ↓
Control Room receives pending decision
   ↓
human approves or declines
   ↓
Control Room resumes worker
   ↓
Worker continues
```

The same pattern applies to Gate 2, push authorization, issue-closure authorization, and any later human decision that the worker cannot legitimately answer for itself.

## Concurrent lifecycle with interactive gates

This refines the concurrent-worker model from `v3-execution-2-architecture.md`.

Each worker keeps the normal engineering lifecycle:

```text
Implement
   ↓
Review
   ↓
Gate 1
   ↓
Gate 2
   ↓
Push readiness
   ↓
Issue closure
```

Control Room coordinates multiple instances of that lifecycle concurrently.

For example:

```text
#328   Gate 2 waiting
#329   Implementing
#330   Gate 1 waiting
```

The worker that reaches a gate pauses without blocking the other workers. Control Room surfaces the actionable decision and resumes that specific worker only after the human response.

This means parallelism applies to **lifecycle progression**, not just implementation work.

## Worker state and wave state remain separate

The execution layer should distinguish worker state from wave state.

A worker might have states such as:

```text
READY
RUNNING
GATE 1
GATE 2
PUSH READY
CLOSED
BLOCKED
FAILED
```

The execution wave can have its own state:

```text
ACTIVE
WAITING FOR HUMAN
PARTIALLY COMPLETE
READY FOR INTEGRATION
INTEGRATING
VERIFYING
COMPLETE
BLOCKED
```

This lets one worker wait for a human while another keeps running.

For example:

```text
Worker A → Gate 1 waiting
Worker B → implementing
Worker C → Gate 2 waiting

Wave → WAITING FOR HUMAN
```

The wave is waiting on human input, but the workers that do not need that input continue progressing.

## Control Room as a gate coordinator

A useful working abstraction is a gate coordinator within Control Room.

It does not own the meaning of the gate. That remains in the engineering skill.

It owns the execution mechanics around the gate:

- receive a worker's request for approval;
- identify the exact worker and gate;
- preserve the approval scope and evidence;
- present the decision to the human;
- record the response;
- resume or stop the worker;
- prevent the worker from silently self-approving.

Conceptually:

```text
implement-it
    │
    │ "Gate 1 requires approval"
    ▼
Control Room
    │
    │ present decision
    ▼
Human
    │
    ├── approve
    └── decline
    │
    ▼
Control Room
    │
    └── resume / stop worker
```

This separation keeps the skill contract portable while allowing different runtimes to implement the required pause/resume mechanism differently.

## Gate scope remains skill-owned

The execution layer should not reinterpret what approval means.

For example, Control Room should not assume that one approval for a completed wave automatically approves three independent Gate 1 reports unless an explicit higher-level contract defines exactly what that approval covers.

The current evidence therefore supports a conservative model:

> **Control Room owns gate presentation and resumption mechanics. The engineering skill owns gate semantics and approval requirements.**

A future experiment may establish that some gates can safely be grouped. Until then, individual worker gates should retain their existing meaning.

## A worker should be pausable, not replaceable

The goal is not to create a simplified background version of `implement-it`.

A worker should run the normal skill lifecycle and become **pausable** at human-owned decision points.

This avoids the failure observed in unattended #332/#333 execution, where the worker effectively invented a self-approval path because it could not stop and wait for the human.

The desired behavior is:

```text
Normal implement-it
        +
Runtime pause/resume support
        =
Orchestrated worker
```

Not:

```text
implement-it
        - human gates
        + coordinator judgment
        =
new unofficial lifecycle
```

## The event model is becoming important

The execution layer may need a small set of durable worker events.

For example:

```text
worker.started
worker.progress
worker.gate_requested
worker.gate_approved
worker.gate_declined
worker.completed
worker.failed
worker.blocked
```

These names are illustrative, not accepted API requirements.

The important idea is that a human gate should become an explicit runtime event that Control Room can observe and act on.

This would also make concurrent execution easier to reason about because the coordinator does not need to poll a worker's conversation to discover that a decision is waiting.

## Integration remains separate

A worker can finish its own lifecycle and still need integration into the shared branch.

Therefore the gate/resume mechanism should not collapse integration into worker completion.

A possible sequence remains:

```text
Worker A → lifecycle complete
Worker B → lifecycle complete
Worker C → Gate 1 waiting

Integration → A + B eligible
Integration → C not yet eligible
```

Whether integration happens immediately for eligible workers or waits for the whole wave remains an open question. The current experiments do not establish a preferred policy.

## What the runtime must eventually provide

This research points to a concrete runtime capability boundary.

A runtime companion should eventually be able to:

- keep a worker alive while it waits;
- suspend progression at an explicit gate;
- report the gate to Control Room;
- associate the gate with the correct worker and scope;
- resume that exact worker after a human response;
- preserve worker workspace and process state;
- expose failure and cancellation distinctly from approval decline.

This is runtime capability, not engineering methodology.

The methodology says:

> **the worker must obtain human approval before crossing this boundary.**

The runtime says:

> **here is how the worker waits until that approval arrives.**

## What this changes in the v3 model

The earlier execution architecture established:

> Control Room makes execution decisions. The runtime executes those decisions.

Execution Architecture 2 added:

> Control Room coordinates engineering skills. It does not replace their lifecycle contracts.

This experiment adds another boundary:

> **Control Room must be able to pause and resume workers at skill-owned human gates without changing what those gates mean.**

That gives the emerging execution model three important responsibilities above worker execution:

```text
Scheduling
Integration
Interactive gate coordination
```

All three must preserve the engineering methodology rather than create an alternate version of it.

## Open questions

The experiment does not settle:

### Gate presentation

- Should Control Room surface one pending decision at a time or show a queue of actionable gates?
- Can the human choose which ready gate to approve first?
- How should multiple workers reaching the same gate type be presented?

### Approval grouping

- Can identical, unchanged worker gates ever be grouped safely?
- What evidence must a grouped approval contain?
- How should one worker changing invalidate a grouped decision?

### Worker resumption

- What is the minimal state needed to resume a paused worker safely?
- Should the runtime keep the process alive, or persist enough state to reconstruct the session?
- How should a timeout or runtime restart affect a pending gate?

### Failure and decline

- Is a declined gate a worker failure, a blocked worker, or a normal user decision state?
- What should happen to the rest of the execution wave when one worker is declined?
- How should partially completed integration be recovered?

### Runtime interface

- What worker/gate event contract should a runtime companion expose?
- Can Herdr provide the required pause/resume behavior without taking ownership of engineering policy?
- What should remain runtime-agnostic if another execution runtime is introduced later?

## Current working model

For now, the smallest evidence-backed model is:

```text
Agentic Engineering
    owns engineering lifecycle and gate semantics

Control Room
    owns scheduling, coordination, integration decisions,
    and gate presentation/resumption orchestration

Runtime companion
    owns worker processes, worktrees, waiting, resume,
    and execution events

Workers
    execute bounded engineering responsibility
    and pause at skill-owned human gates
```

Do not implement a large gate-orchestration framework from this document yet.

The next useful experiments should deliberately test one narrow capability at a time, especially:

1. one worker reaching Gate 1 while another continues;
2. a human approving one worker while another remains pending;
3. worker resumption after approval;
4. gate decline and wave recovery;
5. a runtime restart while a gate is pending.

## Guiding principle

The execution layer should continue to evolve from real work:

```text
Observed behavior

↓

Evidence

↓

Explicit decision

↓

Reusable rule
```

The #332–333 experiment did not show that `implement-it` needs a different gate contract. It showed that an orchestration runtime needs an explicit way to honor the existing contract while workers run asynchronously.
