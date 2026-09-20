# Parallel Implementation Vision

Status: Investigation.

This document records the current direction discovered through real use of Agentic Engineering in useOrbit. It is a working hypothesis for the next smoke tests, not an accepted release design or version commitment.

## Direction

Agentic Engineering should support parallel implementation when multiple issues are dependency-ready and can safely execute independently.

Parallelism is not a new engineering lifecycle.

The lifecycle remains:

```text
Lab → Plan → Implement → Review → Ship
```

The emerging model is multiple normal implementation lifecycles executing concurrently:

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

The useOrbit #354/#355 experiment showed that Claude Code already provides strong execution primitives:

- parallel background agents;
- isolated worktrees;
- independent worker contexts;
- live worker progress and roster;
- switching into worker sessions;
- worker completion handback;
- preservation of an interrupted worker's worktree and branch;
- runtime identity sufficient for a parent session to inspect and restart work in that preserved workspace.

Agentic Engineering should not reproduce these runtime capabilities.

A worker is an execution instance with bounded engineering ownership. In Claude Code, a normal background agent in an isolated worktree can perform that role; a custom worker-agent definition has not been shown to be necessary.

These mechanisms are Claude Code-specific. The portable requirement is smaller: a runtime that wants to support parallel Agentic Engineering needs concurrent isolated execution, worker identity/status, a return or signaling channel, and durable enough worker state to handle interruption safely. Do not design a runtime abstraction or adapter from one implementation.

## What Agentic Engineering already owns

The #354/#355 audit confirmed that the normal single-worker human gates are already correctly specified in current `implement-it`.

For one issue, the intended lifecycle is:

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
    │
    │ report includes review-it result
    ↓
human manual review + explicit approval
    ↓
derive Commit plan
    ↓
Commit plan
    ↓
human explicit approval
    ↓
commit
```

A clean `review-it` result is evidence for Review implementation. It is not authorization. The human approval remains required.

The #354/#355 workers bypassed these gates even though `implement-it` already required them. The strongest evidence points to contradictory delegation: the parent instructed background workers to stop only after committing, effectively framing commit as pre-authorized terminal work.

Therefore the gate semantics themselves should not be rewritten merely because the experiment failed to honor them.

## What parallel support must add or reconcile

The current skills were authored around serial execution and contain assumptions that do not fit simultaneous isolated workers.

Candidate gaps to investigate and correct include:

- determining which dependency-ready issues can safely execute concurrently;
- reconciling the one-shared-working-branch milestone rule with isolated concurrent worktrees;
- defining temporary per-worker branch/convergence behavior if repeated smoke tests support it;
- ensuring a background worker can surface an existing skill-owned human gate, pause, and resume after that specific decision;
- preserving the existing push-readiness and issue-closure procedures;
- verifying the combined branch state after approved worker results converge.

Fix these through the existing ecosystem first. Do not extract an orchestration component merely because the first parallel run required parent improvisation.

## Independent worker progression

Workers should retain normal per-issue ownership and may progress independently.

For example:

```text
#341  Review implementation → waiting
#342  implementing
#343  Commit plan → waiting
```

Approving #341 must resume #341 only. #342 should continue running and #343 should remain paused.

This exact decision-routing behavior has not yet been observed. It is a next-smoke-test requirement, not a validated runtime capability.

## Verification model

Parallel workers should prove their own changes without each paying the cost of proving the final combined repository state.

Each worker should run:

- required targeted verification; and
- the narrowest meaningful broader regression scope for its change.

Then it invokes `review-it` and reaches Review implementation with that evidence.

After approved worker commits converge onto the shared working branch, verify the combined state there. The human-facing combined-verification decision should summarize the evidence already produced by the workers before asking whether to run the full project suite.

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

The exact commands and test scopes remain stack/project-specific. useOrbit's Pest counts and filters are evidence, not portable methodology.

Where combined verification ultimately belongs in the existing lifecycle remains under investigation. Do not assign it to a new orchestrator merely because the first experiment exposed the gap.

## Branch and worktree direction

The current delivery-milestone rule assumes implementation happens directly on one shared working branch.

That assumption does not fit simultaneous isolated worktrees because Git cannot have the same branch checked out in multiple worktrees at once.

The #354/#355 experiment showed a practical candidate:

- retain the milestone/shared working branch as the convergence target;
- give each concurrent worker an isolated worktree and temporary issue branch;
- keep each worker bounded to its issue;
- converge approved worker commits back onto the shared working branch;
- verify the combined state before shared delivery.

This is an emerging design, not yet an accepted `implement-it` rule. The next smoke tests must establish the smallest safe branch/convergence procedure.

## Existing lifecycle ownership remains

Parallelism must not create a new lifecycle stage between Implement and Ship.

Push, issue closure, milestone progression, PR readiness, and release should continue through their existing Agentic Engineering ownership.

The parallel experiment exposed places where the parent session bypassed those procedures. That is evidence to preserve and correctly invoke the existing contracts, not evidence for replacing them.

## Orchestration extraction hypothesis

A small set of responsibilities remained genuinely cross-worker in the first experiment:

- judging whether multiple ready issues can safely execute concurrently;
- sequencing approved worker results into shared state;
- reasoning about verification of the combined result;
- reasoning over workers in different lifecycle states.

Other apparent orchestration responsibilities were either native runtime mechanics or existing skill responsibilities that were bypassed.

This creates an extraction hypothesis, not an architecture decision:

```text
NOW
correct parallel execution through existing skills
        ↓
smoke-test on real work
        ↓
collect evidence
        ↓
observe what remains genuinely cross-worker
        ↓
LATER, only with repeated evidence
extract stable orchestration responsibility
```

See `orchestration.md` for the watchlist and extraction criteria.

## What is not currently justified

Current evidence does not justify introducing:

- a Control Room skill;
- a Control Room agent;
- an orchestrator agent or process;
- Herdr as a dependency;
- a formal worker event protocol;
- a custom worker framework;
- runtime adapters;
- a separate parallel implementation methodology.

These remain possible future outcomes only if repeated evidence earns them.

## Next smoke-test goals

Before extracting orchestration, validate the missing behavior with another real parallel wave:

1. launch multiple dependency-ready issues as isolated workers;
2. require each worker to use normal `implement-it` without contradictory delegation;
3. require targeted and appropriate broader verification per worker;
4. require `review-it` before Review implementation;
5. surface each worker's Review implementation report, including the `review-it` result, to the human independently;
6. genuinely pause that worker for human manual review and explicit approval;
7. resume only the worker whose decision was approved;
8. surface and approve each Commit plan before that worker commits;
9. converge approved worker commits onto the shared working branch;
10. present accumulated worker verification evidence;
11. make the normal full-suite decision against the combined state;
12. preserve existing push and issue-closure procedures, including issue task completion and validation.

Also observe, rather than pre-design:

- whether decision routing is actually difficult;
- whether worker recovery belongs in per-worker lifecycle guidance or remains runtime/parent behavior;
- what happens when parallel candidates overlap or convergence conflicts;
- which cross-worker responsibilities recur across multiple waves.

## Versioning

Do not assign this work to a release version yet.

The working branch is named `improve-2.2.0` because current evidence suggests this may be an evolution of the existing ecosystem rather than a new architectural generation. Rename the branch if later evidence supports a different version boundary.

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

> Claude Code already provides a strong parallel-worker runtime. First make the existing Agentic Engineering lifecycle work correctly across those workers. Extract an orchestrator only if stable cross-worker responsibility remains after repeated real use.
