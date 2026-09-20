# Parallel Implementation Vision

Status: Investigation.

This document records the current direction discovered through real use of Agentic Engineering in useOrbit. It is a working hypothesis for the next smoke tests, not an accepted release design or version commitment.

## Direction

Agentic Engineering should support parallel implementation when planning has already established that multiple issues are dependency-ready and safe to execute independently.

Parallelism is not a new engineering lifecycle.

The lifecycle remains:

```text
Lab → Plan → Implement → Review → Ship
```

The emerging model is that multiple normal implementation lifecycles may execute concurrently:

```text
                         ready issues
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
             Worker A                Worker B
             issue #A                issue #B
                 │                       │
            implement-it             implement-it
                 │                       │
                 └───────────┬───────────┘
                             │
                    combined branch state
                             │
                    combined verification
                             │
                       normal progression
```

Do not invent a separate "parallel implement-it" methodology.

## Native execution substrate

The useOrbit #354/#355 experiment showed that Claude Code already provides the execution primitives needed for parallel implementation:

- parallel background agents;
- isolated worktrees;
- independent worker contexts;
- live worker progress;
- switching into worker sessions;
- worker completion handback;
- preservation of an interrupted worker's worktree and branch;
- enough runtime identity to restart work in the preserved workspace.

Agentic Engineering should not reproduce these runtime capabilities.

A worker is an execution instance with bounded engineering ownership. In Claude Code, a normal background agent in an isolated worktree can perform that role; a custom worker-agent definition has not been shown to be necessary.

## What Agentic Engineering must preserve

Native parallel execution is useful only if the existing engineering guarantees remain intact.

Each implementation worker should own one issue and run the normal `implement-it` lifecycle.

For each worker:

```text
implement
    ↓
targeted verification
    ↓
broader relevant regression verification where appropriate
    ↓
review-it
    ↓
Review implementation
    ↓
human approval
    ↓
Commit plan
    ↓
human approval
    ↓
commit
    ↓
worker implementation complete
```

The Review implementation decision must include the worker's `review-it` result before the human performs their manual review.

Workers may progress independently. One worker waiting for a human decision must not prevent another worker from continuing.

For example:

```text
#341  Review implementation → waiting
#342  implementing
#343  Commit plan → waiting
```

Approving #341 resumes #341 only.

## Verification model

Parallel workers should not each pay the cost of proving the final combined repository state.

Each worker proves its own change with:

- required targeted verification; and
- the narrowest meaningful broader regression scope for that change.

After approved worker commits converge onto the shared working branch, the combined state is verified there.

The human-facing combined-verification decision should summarize the evidence already produced by each worker before asking whether to run the full project suite.

Conceptually:

```text
Worker A
targeted + broader verification
review-it
approved commit
        \
         \
          combined working branch
         /
        /
Worker B
targeted + broader verification
review-it
approved commit
          │
          ▼
combined verification decision
          │
          ├── run full suite
          └── skip, when the existing lifecycle permits it
```

The exact commands and test scopes remain stack/project-specific. This document does not make useOrbit's test counts or Pest filters portable methodology.

## Branch and worktree direction

The current delivery-milestone rule assumes implementation happens directly on one shared working branch.

That assumption does not fit simultaneous isolated worktrees because the same branch cannot be checked out for multiple workers at once.

The #354/#355 experiment showed a practical candidate:

- retain the milestone/shared working branch as the convergence target;
- give each concurrent worker an isolated worktree and temporary issue branch;
- keep each worker bounded to its issue;
- converge approved worker commits back onto the shared working branch;
- verify the combined state before shared delivery.

This is an emerging design, not yet an accepted `implement-it` rule. The next smoke tests must establish the smallest safe branch/convergence procedure.

## Existing lifecycle ownership remains

Parallelism must not create a new orchestration methodology between Implement and Ship.

Push, issue closure, milestone progression, PR readiness, and release should continue through their existing Agentic Engineering ownership.

The parallel experiment exposed places where the parent session bypassed those procedures. That is evidence to preserve the existing contracts, not evidence for a new lifecycle stage.

## What is not currently justified

Current evidence does not justify introducing:

- a Control Room skill;
- a Control Room agent;
- a coordinator process;
- Herdr as a dependency;
- a formal worker event protocol;
- a custom worker framework;
- a separate parallel implementation methodology.

These ideas were useful research hypotheses. Native Claude Code behavior has so far made them unnecessary for the problem under investigation.

## Next smoke-test goals

Before changing the public methodology, validate the missing behavior with another real parallel wave:

1. launch multiple dependency-ready issues as isolated workers;
2. require each worker to use normal `implement-it`;
3. require targeted and appropriate broader verification per worker;
4. require `review-it` before Review implementation;
5. surface each worker's Review implementation decision to the human independently;
6. resume only the worker whose decision was approved;
7. surface and approve each Commit plan before that worker commits;
8. converge approved worker commits onto the shared working branch;
9. present the accumulated worker verification evidence;
10. make the normal full-suite decision against the combined state;
11. preserve the existing push and issue-closure procedures, including issue task completion and validation.

## Versioning

Do not assign this work to a release version yet.

The working branch is named `improve-2.2.0` because the current evidence suggests this may be an evolution of the existing ecosystem rather than a new architectural generation. Rename the branch if later evidence supports a different version boundary.

## Guiding principle

```text
observed behavior
    ↓
evidence
    ↓
explicit decision
    ↓
reusable rule
```

The current hypothesis is intentionally small:

> Claude Code provides parallel workers. Agentic Engineering should preserve its existing engineering lifecycle when those workers execute concurrently.
