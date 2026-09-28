# Orchestration Extraction Watchlist

Status: Investigation. Do not implement an orchestrator from this document.

This document records a possible future extraction first discovered while investigating parallel implementation in useOrbit and now also observed across lifecycle stages during normal post-v2.2.0 work. It exists to prevent two opposite mistakes:

1. forcing coordination responsibility into specialist engineering skills merely because those skills participate in the workflow; and
2. inventing an orchestration architecture before repeated evidence shows one is needed.

Parallel execution exposed the first strong cross-worker cases. A later Phase 26 review exposed a different signal without parallel workers: the coordinating context had to route raw human observations into `lab-it`, preserve surrounding PR/milestone state, retain separate project/stack/methodology evidence, and define the later handoff to `plan-it`. See `lifecycle-orchestration-evidence.md`.

The current strategy remains evidence-first: keep specialist skills correct and focused, observe coordination that remains above or between them, then extract only stable repeated responsibility.

## Evidence boundary

The evidence now spans three designed smoke-test waves and one normal post-v2.2.0 parallel wave, all on one runtime: Claude Code.

It showed that Claude Code natively handled much of what earlier research had tentatively called an execution or Control Room layer:

- parallel agents;
- isolated worktrees;
- independent contexts;
- live worker status;
- completion handback;
- interrupted-worktree preservation;
- enough runtime identity to support parent-led recovery.

It also showed that several failures attributed initially to orchestration were actually existing lifecycle responsibilities that were bypassed:

- `review-it` before Review implementation;
- explicit Review implementation approval;
- explicit Commit plan approval;
- push-readiness procedure;
- issue-closure procedure.

Do not extract those responsibilities upward. Preserve their existing skill ownership.

## Candidate cross-worker responsibilities

The audit identified a smaller residue that genuinely required knowledge beyond one issue.

### Concurrent-safe issue selection

Observed initially in the #354/#355 wave and again during normal post-v2.2.0 Phase 26 sequencing.

The original parallel experiment required the human to originate the idea of running several ready issues concurrently. After v2.2.0 shipped, a fresh normal-use session reconstructed thirteen dependency-ready Phase 26 issues correctly but still recommended only one issue. Inspection showed this was faithful to `sequencing.md`: the rule supported parallel execution after explicit human authorization but told the skill to recommend one ready issue by default.

This exposed a methodology/discoverability gap rather than a failure of the parallel worker lifecycle. A human should still authorize concurrency, but should not have to remember that parallel execution exists before the methodology can surface it.

The candidate correction is intentionally small: milestone sequencing may recommend a safe concurrent subset when expected overlap is low and concurrency would materially help, while explicit human authorization remains mandatory before the parallel path begins.

This responsibility is still relational: judging a safe subset requires knowledge across candidate issues. Today it remains in `implement-it` because that skill owns milestone sequencing. If a Control Room is later extracted, repeated evidence may move this cross-issue recommendation upward rather than duplicating it.

### Convergence sequencing

Observed repeatedly across the smoke tests and again in the normal Phase 26 four-issue wave. Parallel isolated worktrees required separate worker branches, and approved results converged sequentially back into the shared milestone branch.

**Settled after Smoke Test 3** (`parallel-final-reconciliation.md`): sequencing itself — converging
approved commits onto the milestone branch, one at a time, once durable commits exist — is no longer an
open judgment call requiring parent reasoning each time; it is now normal mechanical progression that
never shortens or bypasses push-readiness, issue-closure, or their validation. *Which* context actually
performs that convergence remains open and belongs here, as a Control Room/runtime question, not to the
skill. What remains genuinely open, and still requires human judgment rather than a mechanical default,
narrows to: a real merge conflict, unexpected drift in the milestone branch's tip, a stale or
partially-invalidated approval, or ambiguity about the correct convergence target — none of which the three smoke tests or the later normal Phase 26 wave exercised.

### Combined-state verification

The policy gap is settled in v2.2.0: concurrent workers perform their own targeted/quality verification and `review-it`, then the wave gets one human-controlled combined full-suite run/skip decision before Review implementation. The worker skill deliberately does not prescribe how the combined candidate is assembled or which context runs it.

Mechanism evidence has now progressed through the smoke tests and one normal post-release wave:

- Smoke Tests 1–2 exposed the missing combined-state boundary.
- Smoke Test 3 ran a fresh uncommitted-union suite successfully, but with a looser assembly mechanism that was safe only because the wave was file-disjoint.
- The normal Phase 26 four-issue wave (`phase26-normal-parallel-wave.md`) again assembled a disposable uncommitted union, ran `1331/1331` fresh with TIA disabled, removed the combined worktree, and later verified the converged 47-file result through per-worker/final-state equivalence checks.

This is now repeated evidence that a coordinating context can provide combined-candidate verification without creating premature implementation commits. It still does not justify putting a Git patch/worktree recipe into portable `implement-it`: assembly, dependency preparation, generated state, and final equivalence checks remain runtime/project-sensitive.

The open question has therefore narrowed from whether combined verification can work to **which runtime/Control Room capability should own safe combined-candidate assembly and environment preparation across stacks and runtimes**. Keep `combined-candidate.md` as mechanism research rather than portable procedure.


### Cross-worker lifecycle judgment

Now directly observed in normal post-v2.2.0 work. See `phase26-normal-parallel-wave.md`.

Four workers became ready at different times. The parent absorbed those asynchronous completions, routed one worker-specific product decision while siblings continued, waited for the wave synchronization point before combined verification, then batched the later human gates.

The runtime supplied completion/resumption mechanics; the coordinating parent decided what those states meant for wave progression. This is stronger evidence than merely observing worker status: the parent had to preserve issue identity, wave readiness, and pending human decisions across different worker lifecycle states.

### Cross-skill lifecycle routing and knowledge-boundary coordination

Observed once outside parallel execution during normal post-v2.2.0 useOrbit work. See `lifecycle-orchestration-evidence.md`.

Raw Phase 26 review feedback contained file-level observations and proposed solutions, but the useful next action required coordination before `lab-it` began: challenge premature solution framing, group observations into architecture themes, preserve the open PR/milestone context, route unresolved architecture through Lab before Plan, and retain resulting evidence separately for project decisions, `laravel-inertia-stack`, and portable Agentic Engineering.

This is not evidence that those responsibilities belong inside `lab-it`. Lab owns the architecture investigation itself. The candidate orchestration responsibility is knowing **where the work is in the lifecycle, which specialist stage is needed next, what surrounding state must survive the handoff, and which knowledge boundary each resulting finding belongs to**.

This broadens the orchestration hypothesis beyond cross-worker coordination. It does not yet clear the extraction bar: one natural non-parallel occurrence is evidence to retain and watch for recurrence across Lab → Plan → Implement → Review → Ship.

### Two dimensions of orchestration

Current evidence now suggests two distinct dimensions of the same possible Control Room layer.

```text
vertical lifecycle coordination
Lab -> Plan -> Implement -> Review -> Ship

horizontal execution coordination
Worker A | Worker B | Worker C
```

The horizontal dimension became visible first through parallel implementation: synchronization, combined-state decisions, decision presentation/routing, and convergence awareness.

The vertical dimension became visible during normal Phase 26 review without parallel workers: preserve project/lifecycle state across specialist stages, select the appropriate next stage, reconcile specialist output with unresolved human decisions, and retain evidence across project, stack, and portable-methodology knowledge boundaries.

These are evidence categories, not a proposed architecture. A future Control Room may coordinate both, or later evidence may show that some responsibilities belong elsewhere.

### Specialist skills versus coordinating context

The emerging boundary is:

> The coordinating layer understands where the engineering journey is, what specialist work is needed next, what context and decisions must survive the handoff, and what happens after that work completes. A specialist skill owns how to perform its engineering stage correctly.

The Phase 26 Lab -> Plan flow provides concrete evidence:

- `lab-it` investigated architecture and produced evidence-backed decisions;
- `plan-it` converted approved intent into implementation-ready issues;
- the coordinating context preserved the open PR/milestone state, separated Phase 26 corrections from Backlog product/convention decisions, challenged accidental planning constraints, retained stack/methodology evidence, and enforced the stop before implementation.

This does not make project management, product decisions, or stewardship themselves orchestration responsibilities. It is evidence that routing and preserving those boundaries may be.

### Evidence is not execution policy

Observed during the same Phase 26 sequencing discussion.

The coordinating session remembered two post-convergence findings from earlier research — a stale Vite manifest and leftover worker worktrees — and promoted them into proposed operational steps: rebuild the Vite manifest before merging and remove worker worktrees afterward.

Those findings had deliberately been retained as unresolved runtime/provisioning evidence, not adopted as portable procedure. The leap is therefore a useful boundary signal:

> A retained finding or watch item is evidence to consider, not an instruction to execute, unless a later decision has promoted it into current guidance.

Do not patch a specialist skill from this single occurrence. Watch whether future coordinating contexts similarly confuse research state with active methodology. A future Control Room may need a clearer distinction between current rules, project state, and research/watch evidence.

## Candidate responsibilities still under investigation

### Human decision routing

Now directly observed during the normal Phase 26 four-issue wave (`phase26-normal-parallel-wave.md`).

The #373 worker surfaced a product wording choice while three siblings continued. The parent presented that choice to the human, received `Export`, resumed the correct worker, and that worker changed and re-verified only its own implementation before returning to candidate-ready. The later combined suite included the human-approved result.

This is direct evidence for a coordinating responsibility distinct from the worker's own engineering semantics: receive a worker-specific decision, preserve its identity while other work continues, present it coherently, and route the answer back to the correct execution context.

### Human-facing decision presentation

Repeated and now observed in normal post-release work, not only smoke tests. See `phase26-normal-parallel-wave.md`.

The normal four-issue wave showed that batching itself works well: the parent waited for all workers before the combined-verification choice, presented four per-issue Review implementation decisions in one interaction, batched all four Commit-plan approvals, and later batched closure choices.

The remaining problem is evidence preservation at the decision boundary. Review implementation was compressed too aggressively: none of the four presentations included the required `Activated skills:` line, and #362 never received a substantive text summary before its approval question. The parent presentation did not provide one compact summary preserving enough implementation evidence about what each worker actually changed; #362 in particular had no substantive text summary before its approval question.

By contrast, the batched Commit-plan presentation preserved the information needed for that decision: semantic grouping, order, messages, and per-issue boundaries.

This sharpens the candidate responsibility:

> Aggregate asynchronous specialist output into a compact, decision-ready human presentation without stripping away the evidence needed for the specific decision being asked.

`review-it` still owns what was found, and `implement-it` still owns what Review implementation must prove. The coordinating layer's candidate responsibility is presentation and orientation, not review semantics.

The same run also exposed a real-time orientation issue: partial worker/plan/commit batches arrived as 1/4, 2/4, 3/4 and 4/4 updates. The human found the overall UX good but occasionally lost where the wave stood. A stable compact wave-progress view is therefore worth watching as a presentation concern, without turning worker event streaming into methodology.
### Gate-specific worker resumption

Now observed in the normal Phase 26 four-issue wave. Workers stopped before Review implementation, were resumed after implementation approval to derive Commit plans, and were resumed again after Commit-plan approval to create commits. The runtime implemented "holding" by ending a worker session and later resuming it; the coordinating parent preserved which lifecycle decision unlocked which resumption.

This is evidence for coordination across human gates, while the gate semantics themselves remain owned by `implement-it`.

### Conflict handling

Not observed.

#354/#355 were deliberately non-overlapping. No merge conflict or material shared-file overlap occurred.

A future run with real overlap may expose responsibility that the current experiment could not.

### Candidate-patch propagation into isolated workers

New finding from Smoke Test 3 (`smoke-test-3.md`), not previously identified. Two of three ST3 workers
read a stale, un-patched copy of `verification.md`/`review-gates.md` because an in-progress candidate
methodology change existed only as an uncommitted diff in a main checkout's working directory — invisible
by construction to a concurrently-launched isolated `git worktree`, regardless of which absolute path a
worker happened to read from.

**Classified as runtime mechanics, not cross-worker coordination.** This is not a candidate for the
same extraction bar as decision routing or combined verification — it is about how one specific kind
of state (an uncommitted methodology change) reaches, or fails to reach, an isolated execution context,
the same category as workspace isolation itself. It is also a one-time installation-window risk, not a
standing property of the methodology: once a candidate patch is actually committed and released — as
the equivalent patch already is on this branch — no worker in any worktree fails to see it. See
`parallel-final-reconciliation.md` for why this drives no skill-file change.

## What is not orchestration

Keep these boundaries explicit.

### Worker engineering

A worker owns one issue and the normal per-issue `implement-it` lifecycle:

- implementation;
- targeted and appropriate broader verification;
- `review-it`;
- Review implementation report;
- waiting for human approval;
- Commit plan;
- waiting for human approval;
- approved commit creation;
- existing per-issue progression where the lifecycle assigns it.

Parallelism does not weaken these contracts.

### Runtime mechanics

Claude Code currently owns mechanisms such as:

- creating background agents;
- isolated runtime worktrees;
- worker/session identity;
- live status;
- task notifications;
- handback;
- preservation of an interrupted worker's workspace.

Other runtimes may provide different mechanisms.

The portable requirement is capability, not Claude Code's API or vocabulary.

### Existing lifecycle policy

Do not extract existing policy merely because the first parallel run bypassed it.

Examples:

- Review implementation semantics;
- Commit plan semantics;
- review-it's checklist and staleness rules;
- commit boundaries;
- push authorization and validation;
- issue closure;
- milestone PR/release progression.

## Portability lens

Claude Code-specific mechanisms observed include background Agent execution with isolated worktrees, runtime task notifications, live agent roster/status, terminal handback, and preserved worker workspaces after interruption.

A runtime capable of parallel Agentic Engineering would conceptually need:

- concurrent independent execution contexts;
- non-colliding workspace/branch state;
- stable worker identity;
- signaling for completion, interruption, and eventually pending human decisions;
- a return channel to the coordinating context;
- durable enough state to recover safely from interruption.

Do not design a common runtime interface from this list yet. It is derived from one runtime and one parallel wave.

Agentic Engineering methodology should remain runtime-independent.

## Extraction strategy

The original parallel-execution sequence below is historical context for how the watchlist began. With v2.2.0 shipped, evidence collection now also follows ordinary lifecycle transitions between specialist skills.

The development sequence was:

```text
1. correct parallel execution through existing skills
2. preserve existing human gates and lifecycle ownership
3. smoke-test on real consumer issues
4. collect compact evidence
5. repeat
6. identify responsibilities that remain cross-worker
7. extract only stable, repeated responsibility
```

An eventual orchestrator should be an extraction from working behavior, not a prerequisite for making the behavior work.

If extraction eventually happens, the conceptual boundary may resemble:

```text
Orchestrator
    cross-worker coordination only
             │
      ┌──────┴──────┐
      ▼             ▼
   Worker A       Worker B
   implement-it   implement-it
      │             │
      └──── runtime ┘
```

This diagram is a hypothesis boundary, not an implementation design.

Do not infer from it that the orchestrator must be:

- a skill;
- a Claude Code `.claude/agents/orchestrator.md` definition;
- a long-lived agent;
- a process;
- a service;
- a repository;
- or a specific version boundary.

Those are later artifact decisions.

## Extraction bar

A responsibility becomes a credible orchestration-extraction candidate when:

- it inherently requires context beyond one specialist skill or one worker;
- it remains necessary after the participating skills are themselves correct;
- it recurs across real project execution rather than only designed experiments;
- putting it inside a specialist skill creates awkward ownership, duplicated knowledge, or lifecycle coupling;
- it can be stated independently of Claude Code-specific mechanisms.

One experiment is evidence, not a reusable rule.

## What to observe next

Do not schedule dedicated smoke tests solely for these questions. Observe them during normal project work. Useful remaining questions include:

- What happens with actual file overlap or a convergence conflict?
- Does interrupted-worker recovery need portable methodology, or is runtime-specific recovery plus existing approval-validity checking sufficient?
- Does human decision routing remain reliable when several workers need unrelated decisions at once?
- What stable human-facing orientation is useful during longer waves without turning runtime events into methodology?
- Which runtime/Control Room capability should own safe combined-candidate assembly, environment preparation, and retirement of completed temporary workspaces?
- Which of these responsibilities recur often enough across runtimes or projects to justify extraction?

## Current conclusion

The evidence supports investigating orchestration, not implementing it.

Parallel implementation is now canonical in v2.2.0, so the observation target is broader than parallel execution alone: watch normal project work for coordination that remains necessary across workers, lifecycle stages, or knowledge boundaries after the specialist skills themselves are correct.

Only repeated evidence should justify removing responsibilities from skills and placing them into a higher-level Control Room/orchestrator.
