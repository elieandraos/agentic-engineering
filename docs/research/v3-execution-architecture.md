# Agentic Engineering v3 — Execution Architecture

Status: Investigation.

This document follows `v3-vision.md`.

The vision asks whether Agentic Engineering needs an execution layer above the engineering methodology. This document describes the execution architecture that is emerging from that investigation.

It is a working model, not a final implementation contract.

## The core separation

Agentic Engineering is the engineering methodology.

It owns how software work is investigated, planned, implemented, reviewed, shipped, documented, and improved.

Control Room is the execution methodology.

It owns how that engineering work is coordinated:

- what should happen next
- which work is ready
- which worker should do it
- how work is parallelized
- which human gate applies
- when execution should wait or stop
- how results are collected

The execution runtime is something else again.

It owns the mechanics needed to make those decisions happen:

- creating workers
- creating worktrees
- launching sessions
- multiplexing processes
- waiting and resuming
- messaging
- restoring workspaces
- collecting runtime results

This gives us three layers.

```text
Engineering Intelligence

Control Room

    ↓

Execution Runtime

    ↓

Workers
```

The names may change as the implementation becomes clearer. The separation is the important part.

## A second methodology

The existing system already has a useful pattern.

Engineering methodology:

```text
Lab → Plan → Implement → Review → Ship
```

Stack companions provide implementation knowledge for that methodology.

Examples:

- Laravel / Inertia / Vue
- Nuxt
- Supabase

The execution layer can use the same pattern.

Execution methodology:

```text
Control Room
```

Runtime companions provide execution knowledge for that methodology.

Examples under investigation:

- Herdr
- tmux
- Claude Code
- other future runtimes

The important point is that a runtime companion is not the execution methodology itself.

It explains how to realize the execution methodology on a particular runtime.

## Control Room

The current GPT Project is already acting as a Control Room.

It does more than scheduling.

It can:

- act as a principal engineering decision partner
- investigate architecture and domain behavior
- challenge unnecessary scope
- plan work
- review implementation
- steward sessions
- decide when not to automate
- coordinate repositories
- prepare worker handoffs
- decide which methodology or stack knowledge applies

This means Control Room should not be reduced to a process launcher.

The important distinction is:

> Control Room makes execution decisions. The runtime executes those decisions.

## Runtime companions

Herdr is the first runtime that makes the execution-layer idea concrete, but the architecture should not depend on Herdr.

Herdr can be treated as a runtime companion to Control Room.

Conceptually:

```text
Control Room
    ↓
Runtime companion
    ↓
Herdr
    ↓
workers, worktrees, sessions
```

Another runtime could eventually provide the same execution capabilities without changing the execution methodology.

For example:

```text
Control Room
   ├── Herdr companion
   ├── tmux companion
   └── another runtime companion
```

This is the execution equivalent of stack companions.

The methodology remains portable.

Only the runtime-specific implementation changes.

## Herdr's role

Herdr should not learn the engineering methodology as product logic.

It should provide runtime capabilities such as:

- create a worker
- create or attach to a worktree
- launch a session
- resume a session
- wait for completion
- send messages
- collect results
- restore the execution workspace

Agentic Engineering can tell the runtime what kind of worker is needed and what the worker must accomplish.

Herdr decides how to create that worker in its own runtime.

This keeps the boundary clean.

```text
Agentic Engineering

What should the worker do?

        ↓

Control Room

Which worker should run now?

        ↓

Runtime companion

How do we launch it here?

        ↓

Herdr

Create the actual runtime objects.
```

## Workers

Workers are intentionally narrow.

A worker should receive the context required to perform one bounded piece of engineering work.

Typical inputs:

- one issue
- one repository
- one worktree
- engineering skills
- applicable stack companions
- any approved decisions and constraints

Typical output:

- engineering work
- verification results
- a clear completion or escalation report

The worker should not become another Control Room.

Its job is to execute the assigned engineering responsibility.

This keeps orchestration reasoning above the worker and implementation work inside the worker.

## Roles versus runtime agents

A useful future abstraction may be a small set of engineering execution roles.

For example:

```text
Implement Agent
Review Agent
Plan Agent
Research Agent
```

Each role would define things such as:

- purpose
- inputs
- outputs
- engineering skills
- stack companions
- human gates
- boundaries

The runtime would then map that role onto its own runtime agent.

Conceptually:

```text
Agentic Engineering

Implement Agent

        ↓

Runtime companion

        ↓

Herdr runtime agent

        ↓

Claude Code session
```

The names and exact artifact format remain open.

The important rule is that the engineering role should not depend on Herdr's command syntax.

## Dependency graphs and execution waves

Planning already produces a dependency graph.

For example:

```text
        A
      /   \
     B     C
    / \     \
   D   E     F
```

Today, implementation often progresses one issue at a time.

The graph already contains the information needed for parallel execution.

A future Control Room could transform it into waves:

```text
Wave 1
A

Wave 2
B  C

Wave 3
D  E  F
```

The important point is that parallel execution should be a consequence of the dependency graph, not a separate planning system.

Control Room can decide which ready work to launch and when.

Workers then execute those issues independently when the architecture permits it.

## Parallelism is not free

The goal is not to create as many workers as possible.

Before parallel execution becomes automatic, the system needs to understand at least:

- dependency readiness
- likely file conflicts
- shared resources
- human approval boundaries
- verification boundaries
- worktree isolation
- how results are combined

A useful execution wave is one where work can safely proceed in parallel without weakening the engineering methodology.

## Human gates remain

The execution layer does not remove human approval.

Current gates include:

- plan approval
- issue creation approval
- Implement Gate 1
- Implement Gate 2
- push authorization
- issue closure confirmation
- milestone PR readiness
- PR approval
- release

Parallel execution changes when workers operate.

It does not automatically change who approves what.

Future experiments may show that some approvals can move from individual issues to an execution wave, but that should be earned through evidence.

## Context and worker isolation

One reason to introduce an execution layer is to reduce repeated context work.

Today, long sessions can repeatedly carry:

- repository discovery
- engineering skill context
- stack companion context
- orchestration discussion
- human decision history

A future Control Room can give each worker only the context it needs while keeping shared coordination state above the worker.

The goal is not to minimize context at all costs.

The goal is:

- less repeated discovery
- less unnecessary context carryover
- clearer issue-specific context
- isolated worker workspaces
- predictable startup cost

Measure first.

Optimize second.

## Control Room versus runtime

A useful boundary test is simple.

If a decision answers:

> What should happen?

it belongs in Control Room or the engineering methodology.

If a decision answers:

> How do we make that happen on this runtime?

it belongs in the runtime companion.

Examples:

| Responsibility | Layer |
|---|---|
| Which issue should run next? | Control Room |
| Can two issues run in parallel? | Control Room |
| Which worker role should be used? | Control Room |
| Which engineering skills apply? | Agentic Engineering |
| Which Laravel rules apply? | Laravel companion |
| How do I create the isolated worktree? | Runtime companion |
| How do I launch the worker process? | Runtime companion |
| How do I resume the session? | Runtime companion |
| How should the engineering issue be implemented? | Worker + Agentic Engineering |

This boundary protects portability.

## Agentic Engineering should not absorb runtime commands

A common failure mode would be to put Herdr-specific commands directly into engineering skills.

For example, `implement-it` should not become a Herdr manual.

Instead:

```text
implement-it

This issue requires an isolated worker.

        ↓

Control Room / runtime companion

Launch the worker using the current runtime.
```

That keeps the engineering methodology reusable across runtimes.

The same principle already exists between stack companions and engineering skills.

## Possible repository artifacts

The discussion raised possible artifacts such as:

```text
control-room/

agents/

implement.md
review.md
planner.md

runtime-companions/

herdr/
tmux/
claude-code/
```

These are examples, not an accepted repository structure.

The exact artifact is intentionally unresolved.

Possible forms include:

- Markdown role definitions
- orchestration guides
- runtime manifests
- configuration
- scripts
- a dedicated execution package
- project instructions

The first real orchestration experiment should tell us what is actually reusable.

## What remains uncertain

The architecture is becoming clearer, but several decisions should remain open.

### Control Room

- Does Control Room remain a project-level responsibility layer, or become a versioned artifact?
- Which parts can be shared across projects?
- Which decisions should always remain human-led?

### Agents

- Are long-lived workers useful, or should workers remain issue-scoped?
- How much context should a worker own?
- Can workers safely be reused across issues?
- Do implementation and review need different worker roles?

### Runtime companions

- What must a runtime companion provide?
- Is a companion only documentation, or does it include executable configuration?
- How should a runtime expose worktrees, sessions, waiting, and messaging?
- How should another runtime implement the same execution methodology?

### Worktrees

- When should worktrees be created?
- When should they be reused?
- When should they be destroyed?
- Which cleanup guarantees are required?

### Orchestration

- How should ready waves be selected?
- How should potential file conflicts be detected?
- How should worker outputs be collected?
- Which work can truly run concurrently?
- Which steps must remain sequential because of human gates or shared state?

## What should happen next

Do not turn this architecture into a large implementation yet.

The next step should be a focused Lab investigation around one real orchestration experiment.

That experiment should use the current useOrbit workflow and answer a small set of concrete questions:

1. Can Control Room select a dependency-ready wave safely?
2. Can a runtime launch isolated workers from that decision?
3. Can workers receive the right engineering skills and stack companions without repeated setup?
4. Can results return to Control Room cleanly?
5. Where do human gates belong when multiple workers are active?
6. What context is shared, and what should stay worker-specific?

Herdr is a useful first runtime for this experiment because it already provides the kinds of execution primitives under discussion.

But the experiment should validate the architecture, not assume that Herdr is the architecture.

## Guiding principle

The execution layer should evolve the same way Agentic Engineering evolved.

```text
Observed behavior

↓

Evidence

↓

Explicit decision

↓

Reusable rule
```

Do not build a large execution framework because the architecture looks elegant on paper.

Build the smallest real orchestration experiment, measure it, and let the reusable boundaries emerge from successful use.
