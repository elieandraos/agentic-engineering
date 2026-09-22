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

Then it invokes `review-it` and reaches Review implementation with that evidence. A parallel worker does not make its own full-project-suite run/skip choice — that choice belongs to combined verification, below, not to the individual worker.

**Updated after Smoke Test 2** (see `smoke-test-2.md`, `responsibility-boundaries.md`'s "Combined verification"): both smoke tests showed the same gap — the final combined branch state was never verified with one explicit, deliberate decision. The corrected sequencing is combined verification *before* the implementation-review checkpoint, not after commits are already approved and converged:

```text
Worker A
targeted + broader verification
review-it
"ready" — still uncommitted
        \
         \
          combined candidate state (uncommitted)
         /
        /
Worker B
targeted + broader verification
review-it
"ready" — still uncommitted
          │
          ▼
full project suite — once, required (not a skip choice)
          │
          ▼
implementation-review checkpoint
(each worker's review-it summary + verification evidence + combined result)
          │
          ▼
human manual review + explicit approval, per worker
          │
          ▼
Commit plan(s) → human approval → durable commits
```

**Superseded by Smoke Test 3's live evidence and the resulting final decision** (see
`parallel-final-reconciliation.md`): this is a full-suite decision for the whole wave, not per worker —
but it is a human run-or-skip choice, made once for the wave, not a mandatory-run requirement. A live
run's own presentation reopened the "mandatory" framing this paragraph originally stated, and the human
ratified the run-or-skip framing when asked; the final reconciliation records that as the settled
position going forward, alongside the existing per-issue full-suite choice `verification.md` already
defines for one worker running alone, which this does not change.

The exact commands and test scopes remain stack/project-specific. useOrbit's Pest counts and filters are evidence, not portable methodology.

**What this does not yet solve.** Constructing that combined candidate state safely — from several isolated workers' still-uncommitted changes, without creating a durable commit before Review implementation and Commit plan approval — is an open mechanism question, not a solved one. Neither smoke test's convergence behavior answers it: both only ever converged *after* commits already existed and were already approved. See `combined-candidate.md` for the mechanism investigation. Where the resulting step ultimately belongs in the existing lifecycle (a `ship-it` addition, an explicit parent-session step, something else) also remains under investigation. Do not assign either the mechanism or its ownership to a new orchestrator merely because two experiments exposed the gap.

## Branch and worktree direction

The current delivery-milestone rule assumes implementation happens directly on one shared working branch.

That assumption does not fit simultaneous isolated worktrees because Git cannot have the same branch checked out in multiple worktrees at once.

The #354/#355 experiment showed a practical candidate:

- retain the milestone/shared working branch as the convergence target;
- give each concurrent worker an isolated worktree and temporary issue branch;
- keep each worker bounded to its issue;
- converge approved worker commits back onto the shared working branch;
- verify the combined state before shared delivery.

**Settled by the final reconciliation after Smoke Test 3** (`parallel-final-reconciliation.md`):
convergence mechanics being unresolved is not a reason to delay authorizing or launching a wave — it
only becomes relevant once durable, approved commits exist. Once that point is reached, converging
sequentially onto the milestone branch is normal mechanical progression that never shortens or bypasses
push-readiness, issue-closure, or their validation, stopping only for a genuine conflict, drift, stale
approval, or ambiguous target. This is now a small, additive `sequencing.md` clarification. *Which*
context actually carries convergence out remains deliberately open — a runtime/Control Room question
(`responsibility-boundaries.md`'s "Convergence execution"), not encoded in the skill.

## Existing lifecycle ownership remains

Parallelism must not create a new lifecycle stage between Implement and Ship.

Push, issue closure, milestone progression, PR readiness, and release should continue through their existing Agentic Engineering ownership.

The parallel experiment exposed places where the parent session bypassed those procedures. That is evidence to preserve and correctly invoke the existing contracts, not evidence for replacing them.

## Human-facing presentation

Skills own engineering semantics and results — what `review-it` found, what verification ran, what a
commit plan proposes. A coordinating parent (today's session, potentially a future orchestrator) owns
how those already-correct results are surfaced to the human at each lifecycle checkpoint.

> Human-facing lifecycle checkpoints should preserve the substance of skill results while hiding
> internal methodology mechanics the human does not need to operate the workflow.

A second real-work run surfaced this distinction directly: lifecycle mechanics were correct, but the
reports a human actually saw carried internal identifiers (gate numbers, rule-file names) that add no
engineering information for someone deciding whether to approve. This is a presentation concern, not a
reason to change what any skill decides or reports internally, and not evidence for a fixed message
template or UI protocol yet — see `orchestration.md`'s watchlist for the current, evidence-gated status
of this as a possible future responsibility. The distinction is not inherently parallel-specific; a
single-worker session hits the same checkpoints and would benefit from the same presentation care.

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

**Status after Smoke Test 3:** the goals below have been exercised across Smoke Tests 2 and 3; see
`parallel-final-reconciliation.md` for the reconciled final position and what remains open (narrower
validation questions, not a fresh goal list). Left below as the historical record of what this
document asked for before either test ran.

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
