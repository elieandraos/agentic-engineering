# Orchestration Extraction Watchlist

Status: Investigation. Do not implement an orchestrator from this document.

This document records a possible future extraction first discovered while investigating parallel implementation in useOrbit and now also observed across lifecycle stages during normal post-v2.2.0 work. It exists to prevent two opposite mistakes:

1. forcing coordination responsibility into specialist engineering skills merely because those skills participate in the workflow; and
2. inventing an orchestration architecture before repeated evidence shows one is needed.

Parallel execution exposed the first strong cross-worker cases. A later Phase 26 review exposed a different signal without parallel workers: the coordinating context had to route raw human observations into `lab-it`, preserve surrounding PR/milestone state, retain separate project/stack/methodology evidence, and define the later handoff to `plan-it`. See `lifecycle-orchestration-evidence.md`.

The current strategy remains evidence-first: keep specialist skills correct and focused, observe coordination that remains above or between them, then extract only stable repeated responsibility.

## Evidence boundary

The #354/#355 experiment is one parallel wave on one runtime: Claude Code.

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

Observed once.

The parent inspected multiple ready issues and judged #354/#355 safe to run concurrently because their expected implementation surfaces were disjoint.

This is relational: one worker cannot determine whether its work is safe to execute concurrently without knowledge of the other candidate work.

Current skills can determine readiness and recommend one next issue, but do not define selection of a concurrent-safe subset.

Watch for recurrence before extracting it.

### Convergence sequencing

Observed once.

Parallel isolated worktrees required separate worker branches. The parent then sequenced those approved results back into the shared milestone branch.

The current one-working-branch milestone rule does not describe this case.

This may become parallel-aware `implement-it`/lifecycle policy rather than orchestration. Correct the skills and repeat the experiment before deciding.

**Settled after Smoke Test 3** (`parallel-final-reconciliation.md`): sequencing itself — converging
approved commits onto the milestone branch, one at a time, once durable commits exist — is no longer an
open judgment call requiring parent reasoning each time; it is now normal mechanical progression that
never shortens or bypasses push-readiness, issue-closure, or their validation. *Which* context actually
performs that convergence remains open and belongs here, as a Control Room/runtime question, not to the
skill. What remains genuinely open, and still requires human judgment rather than a mechanical default,
narrows to: a real merge conflict, unexpected drift in the milestone branch's tip, a stale or
partially-invalidated approval, or ambiguity about the correct convergence target — none of which any of
the three smoke tests has yet exercised.

### Combined-state verification

Observed as a gap, and confirmed recurring: Smoke Test 2 produced the same gap independently, under a
corrected parallel-aware `sequencing.md` (`smoke-test-2.md`; `responsibility-boundaries.md`'s "Combined
verification"). This is now the strongest recurrence evidence of any candidate on this watchlist — the
same gap, twice, under two different skill-correction states.

Each worker verified its own branch, but neither run re-verified the final combined state with one
explicit decision before implementation-review.

Verification of the union inherently requires knowledge beyond either worker's isolated change.

**Escalated further by Smoke Test 3** (`smoke-test-3.md`): attempted for real for the first time — a
full, fresh, uncommitted-union regression pass actually ran and passed, before any worker's Review
implementation — but using a mechanism that diverged from the validated procedure
(`combined-candidate.md`) in ways that happened not to matter only because that wave was file-disjoint.
This remains the single strongest recurring candidate on this watchlist across all three smoke tests,
and is still not promoted past "watch" — one real attempt with a divergent mechanism is evidence of how
it goes when tried, not a second clean success confirming a stable, repeatable procedure. The wave-level
run/skip framing question this run also surfaced is now settled as a final decision, not left open — see
`parallel-final-reconciliation.md`.

**Policy now decided, mechanism still open.** After Smoke Test 2, the research position changed: a
parallel worker no longer gets its own full-suite run/skip choice at all (targeted + narrowest broader
regression + `review-it` is sufficient per worker); the full suite instead runs once, required, against
one assembled combined candidate state, before the implementation-review checkpoint — see `vision.md`'s
updated "Verification model" and `responsibility-boundaries.md`. This is a policy decision, not yet a
skill change and not yet validated by any smoke test. The genuinely unresolved part is narrower than
"who owns combined verification": it is *how* to assemble that combined candidate from several still-
uncommitted, isolated workers without creating a durable commit ahead of the existing Review
implementation/Commit plan approvals — investigated in `combined-candidate.md`. This may still naturally
belong to existing milestone/Ship progression, to a new explicit parent-session step, or to something
else; do not assign ownership prematurely, and do not treat the mechanism as solved by either smoke
test's convergence behavior, which only ever ran after commits already existed and were approved.

### Cross-worker lifecycle judgment

Thin but real.

The runtime knew that one worker had completed while another was running. Runtime status itself required no parent reasoning.

The potential higher-level responsibility is deciding what should happen when workers occupy different lifecycle states.

For example:

```text
Worker A → Review implementation → waiting
Worker B → implementing
Worker C → Commit plan → waiting
```

No real run has yet exercised this state with valid skill-owned gates.

### Cross-skill lifecycle routing and knowledge-boundary coordination

Observed once outside parallel execution during normal post-v2.2.0 useOrbit work. See `lifecycle-orchestration-evidence.md`.

Raw Phase 26 review feedback contained file-level observations and proposed solutions, but the useful next action required coordination before `lab-it` began: challenge premature solution framing, group observations into architecture themes, preserve the open PR/milestone context, route unresolved architecture through Lab before Plan, and retain resulting evidence separately for project decisions, `laravel-inertia-stack`, and portable Agentic Engineering.

This is not evidence that those responsibilities belong inside `lab-it`. Lab owns the architecture investigation itself. The candidate orchestration responsibility is knowing **where the work is in the lifecycle, which specialist stage is needed next, what surrounding state must survive the handoff, and which knowledge boundary each resulting finding belongs to**.

This broadens the orchestration hypothesis beyond cross-worker coordination. It does not yet clear the extraction bar: one natural non-parallel occurrence is evidence to retain and watch for recurrence across Lab → Plan → Implement → Review → Ship.

## Candidate responsibilities with insufficient evidence

### Human decision routing

Not observed.

The #354/#355 workers never surfaced Review implementation or Commit plan. Therefore the parent never had to receive a decision from one worker, present it to the human, and route the response back to that exact worker.

This is one of the most orchestrator-shaped hypotheses, but currently has zero direct supporting execution evidence.

The next smoke test should exercise it deliberately.

### Human-facing decision presentation

Now has direct supporting evidence, from Smoke Test 2 (`smoke-test-2.md`), distinct from "Human decision
routing" above: routing is about getting the right answer back to the right worker; this is about how
the evidence a skill already produced gets *worded* for the human in between.

In that run, `review-it` produced substantive, specific findings for two of the three workers (a
`policiesCount`-derivation and route-placement scope note; a renewal-window judgment call), and both the
worker's own report and the parent's relay of it wrapped that substance in internal methodology
vocabulary — "Gate 1," "Gate 2," rule-file names — rather than plain statements of what was checked and
what decision was needed. The substance itself mostly survived the compression in this run; the
vocabulary and compactness did not match what a human operating the workflow actually needs.

This shows a coordinating parent does receive skill-owned results and must decide how to surface them —
which is plausibly, eventually, an orchestrator-shaped responsibility. It is not extracted now: a single
run's presentation gap is not repeated evidence, and this watchlist's own bar (below) requires seeing a
responsibility recur before treating it as a real candidate. It is also not a reason to move review
semantics or findings out of `review-it` — `review-it` continues to own *what* the review found; this
watch item is only about *how* an already-correct result gets presented, and that boundary should stay
sharp as more evidence accumulates.

The next smoke test should observe whether this recurs, and whether it recurs identically for a
single-worker (non-parallel) `implement-it` run — nothing about the underlying gap is inherently
parallel-specific; parallel execution only made the parent/presentation boundary easier to see.

### Gate-specific worker resumption

Not observed.

The interrupted Life worker was recovered, but that was process/workspace recovery, not resumption from a human gate.

Do not treat the two as equivalent.

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

The development sequence is:

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

The next smoke tests should answer:

- Can a background worker surface Review implementation and genuinely wait?
- Can the human approve one waiting worker while siblings continue or remain paused?
- Can the correct worker resume without another worker being affected?
- Does decision routing require explicit orchestration machinery or does the runtime make it trivial?
- What branch/convergence rule survives repeated parallel waves?
- Where does combined verification fit most naturally in the existing lifecycle?
- What happens with actual file overlap or a convergence conflict?
- Does interrupted-worker recovery need portable methodology, or is runtime-specific recovery plus existing approval-validity checking sufficient?
- Which of these responsibilities recur often enough to justify extraction?

## Current conclusion

The evidence supports investigating orchestration, not implementing it.

Parallel implementation is now canonical in v2.2.0, so the observation target is broader than parallel execution alone: watch normal project work for coordination that remains necessary across workers, lifecycle stages, or knowledge boundaries after the specialist skills themselves are correct.

Only repeated evidence should justify removing responsibilities from skills and placing them into a higher-level Control Room/orchestrator.
