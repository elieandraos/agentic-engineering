# Agentic Engineering v3 — Execution Experiment

Status: Investigation.

This document records the first real execution-layer experiment built from the v3 architecture discussion.

It follows:

- `v3-vision.md` — why v3 exists.
- `v3-execution-architecture.md` — the execution architecture currently being investigated.

This document is about what actually happened when we tried parallel execution in a real useOrbit milestone.

It is evidence, not a final architecture.

## The experiment

Phase 26 in useOrbit reached a point where three issues were ready at the same time:

- #346 — Documents tab
- #347 — Notes tab
- #348 — Settlements placeholder

They were independent in the dependency graph and all depended on the already-closed #336 Medical pages issue.

The experiment was intentionally simple:

> Run #346, #347, and #348 as three isolated workers.

The goal was not to design a complete orchestration system first.

The goal was to observe what the current environment could already do.

## What happened

The execution followed this shape:

```text
Three ready issues

        ↓

Three isolated worktrees
Three branches

        ↓

Three workers running in parallel

        ↓

Three completed implementations

        ↓

Merge into the active feature branch

        ↓

Verification

        ↓

Push
```

The three workers ran independently and each completed a normal implementation flow for its assigned issue.

The parent session then merged the three branches into the shared feature branch.

## What worked

### Worktree isolation worked

Each issue received its own branch and isolated worktree.

This allowed the three implementations to proceed at the same time without sharing a working tree.

The workers were able to perform normal implementation work, tests, formatting, and commits independently.

### Parallel execution was real

The three workers ran concurrently rather than being simulated as three sequential tasks.

The parallel execution window was bounded by the slowest worker.

This produced real wall-clock savings compared with running the same issues one after another.

### The dependency graph was useful

All three issues were already ready.

The execution layer did not need a new planning system to discover the wave.

The existing GitHub dependency graph provided enough information to identify candidate parallel work.

This supports the v3 idea that planning can remain responsible for engineering dependencies while the execution layer consumes the resulting graph.

## What did not work cleanly

### Dependency readiness is not merge safety

The three issues were dependency-independent, but they all modified the same file:

```text
PolicyMedicalDetailShell.vue
```

Each worker added a different tab.

The branches therefore conflicted during integration even though the dependency graph allowed them to run at the same time.

The conflicts were small and were resolved cleanly, but the experiment exposed an important distinction:

> A dependency graph tells us whether work can begin independently. It does not by itself prove that the results can be merged without coordination.

This suggests that a future execution layer may need both a dependency graph and some awareness of likely file conflicts or shared resources.

### Scope still belongs to engineering review

One worker (#347) made broader changes than the issue required while implementing the Notes tab.

The worker widened shared prop typing and generalized note-related frontend pieces in addition to adding the requested tab.

The implementation still completed successfully, but the example reinforces an important boundary:

> Parallel execution does not replace implementation review.

A worker can execute successfully while still producing scope that needs review before final milestone acceptance.

## What the human workflow suggests

The experiment also clarified how parallel execution should probably fit around the existing engineering workflow.

The preferred flow is not a second parallel methodology.

The preferred model is:

```text
Ready wave

        ↓

Create isolated workers

        ↓

Workers implement in parallel

        ↓

Merge worker branches into the active feature branch

        ↓

Continue the normal engineering workflow

        ↓

Verification

        ↓

Gate 1

        ↓

Human reviews the integrated diff

        ↓

Gate 2

        ↓

Commit / push / review / issue closure
```

This is a human preference observed from the experiment, not yet a Control Room rule.

The important idea is that parallelism should accelerate implementation while keeping the existing engineering gates intact.

## Human gates remain an open question

This experiment did not fully test a parallel human-gate model.

The workers completed their own work and the parent session integrated their branches afterward.

It therefore did not establish whether future orchestration should:

- expose Gate 1 separately for each worker,
- aggregate a whole wave into one review boundary,
- or use a hybrid model.

That should be tested deliberately rather than decided from this run.

The current evidence suggests a useful direction:

> Parallel workers can accelerate implementation, but the integrated result should return to the normal engineering gates before final acceptance.

## Worktrees and runtime ownership

The experiment also raises a more concrete runtime question.

The workers were able to create isolated worktrees and branches automatically.

That is execution mechanics rather than engineering methodology.

A future runtime companion could therefore own operations such as:

- create the worker workspace,
- create the branch,
- launch the worker session,
- track the worker,
- collect its result,
- merge or hand off the branch,
- clean up the workspace.

Control Room would still decide:

- which issues should run,
- whether the wave is safe,
- which worker role applies,
- and when the resulting work enters the normal engineering gates.

This is still an architectural hypothesis, but the experiment gives it a concrete basis.

## What steward-it told us

Steward-it correctly behaved as a session reconstruction and diagnostic tool.

It measured the execution, reconstructed phases, identified wasted work, classified findings, and reported evidence from the session log.

The experiment should not treat the absence of a new orchestration recommendation in a plain stewardship report as proof that steward-it itself is missing orchestration behavior.

Its role today is to explain what happened.

Whether orchestration-specific analysis should become part of its future responsibilities remains an open v3 question.

## What we know now

The first experiment provides several concrete observations.

1. The current environment can run multiple implementation workers in isolated worktrees at the same time.
2. Existing issue dependencies are enough to identify a first parallel wave.
3. Parallel workers can finish independently and return branches for integration.
4. Dependency independence does not guarantee merge independence.
5. Shared-file conflicts can be small and manageable when workers are instructed to keep changes additive.
6. A successful parallel implementation still needs the normal engineering review and verification boundaries.
7. Runtime operations such as worktree creation and worker lifecycle are distinct from the engineering methodology.
8. Human approval behavior for a whole parallel wave remains insufficiently tested.

## What remains open

The experiment is deliberately small.

It does not answer the full v3 architecture.

Questions for future experiments include:

- Should Control Room inspect likely file conflicts before launching a wave?
- Should all workers in a wave stop at the same engineering gate, or can they progress independently?
- Where should merge and integration ownership live?
- Should workers ever merge their own results?
- Should the parent Control Room perform integration, or should the runtime companion provide it?
- How should scope expansion by one worker affect the rest of a wave?
- Can worker capabilities be restricted by the runtime rather than only by prompts?
- What context should be shared across workers and what context should stay isolated?
- How should worker completion be summarized back to the human?

## The next experiment

The next useful experiment should keep the methodology stable and change only one execution variable.

For example:

```text
Run a ready wave
→ isolate workers
→ complete implementation
→ integrate
→ return to the normal engineering gates
```

Then measure:

- wall-clock savings,
- human waiting time,
- merge effort,
- review effort,
- verification effort,
- context usage,
- and any new coordination problems.

Do not build a large orchestration framework yet.

Let repeated experiments determine which parts become reusable execution methodology and which belong only to a particular runtime.

## Guiding principle

The execution layer should evolve the same way Agentic Engineering evolved:

```text
Observed behavior

↓

Evidence

↓

Explicit decision

↓

Reusable rule
```

This experiment is one piece of evidence.

It is not the final answer.