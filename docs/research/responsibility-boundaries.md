# Responsibility Boundaries After Parallel Smoke Tests

Status: Investigation. This is an extraction *analysis*, not an orchestrator design. It reconciles
Smoke Test 1 (`smoke-test-1.md`) and Smoke Test 2 (`smoke-test-2.md`) into one responsibility map. It does
not modify any skill, does not create an orchestrator, agent definition, or runtime adapter, and does
not make a release/version decision.

## Purpose

After two real parallel-implementation waves, this document answers one question:

> After making individual implementation workers correct, what responsibilities belong to engineering
> skills, what belongs to the execution runtime, and what responsibilities have genuinely emerged
> above individual workers?

It inventories every responsibility observed across both smoke tests, classifies current ownership
against direct evidence, and states — separately from that — what evidence would be needed before any
responsibility moves to a new place. Artifact form for anything cross-worker (skill, agent definition,
process, service, or something else) is explicitly unresolved and out of scope here.

## Evidence base

Primary sources, all read in full for this document:

- `docs/research/smoke-test-1.md` — Smoke Test 1 forensic record (useOrbit #354/#355).
- `docs/research/smoke-test-2.md` — Smoke Test 2 forensic record (useOrbit #341/#342/#343), including
  its ST2-specific review-presentation finding.
- `docs/research/vision.md` — working hypothesis and diagrams predating both smoke tests.
- `docs/research/orchestration.md` — the extraction watchlist and its pre-ST2 evidence state.
- `docs/research/parallel-dry-run.md` — the dry-run that selected the ST2 wave and reduced the
  candidate skill patch to two files, with its own responsibility-classification table (used here as
  a predictive baseline, not as evidence in itself).
- The actual current skill text on this branch (`skills/implement-it/**`, `skills/review-it/**`,
  `skills/ship-it/**`), read directly rather than assumed, specifically: `SKILL.md`, `rules/
  sequencing.md`, `rules/review-gates.md`, `rules/verification.md`, `rules/push-readiness.md`,
  `rules/issue-closure.md`, `rules/scope.md` (review-it), and `ship-it/rules/milestone-pr-readiness.md`
  and `rules/milestone-completion.md`.

This document does not reproduce either forensic report's evidence in full; it cites specific findings
and points back to the section that established them.

## Working definitions

- **Worker.** One execution instance with bounded engineering ownership of one issue, normally
  performed by running `implement-it` (and its collaborators — `review-it`, applicable stack
  companions) to completion. "Worker" names the responsibility boundary, not a Claude Code
  implementation detail — in both smoke tests it happened to be a `general-purpose` background
  `Agent` in an isolated worktree, but nothing in this document assumes that has to remain true.
- **Runtime.** The execution mechanism a given environment supplies underneath the methodology:
  concurrent execution contexts, workspace isolation, identity/status, a signaling/return channel,
  durable-enough state to survive interruption. In both smoke tests this was Claude Code's background
  `Agent`, `isolation:"worktree"`, `SendMessage`, task notifications, and `ListAgents`/handback.
- **Skill.** Portable engineering methodology and policy — what a correct implementation, review, or
  release process requires, independent of how many workers exist or what runtime executes them.
- **Cross-worker / possible future orchestration.** A responsibility that inherently requires
  knowledge of, or coordination across, more than one worker's state or the shared branch/repository
  state, and does not fit inside one worker's own issue-scoped lifecycle. This is a candidate ownership
  category evidenced by both smoke tests — it is not assumed to require a new artifact, and if one is
  eventually justified, its *form* (skill, agent definition, process, service, or something else) is a
  separate, later decision this document does not make.

## Responsibility inventory

Responsibilities observed across ST1 and ST2, grouped by where in the lifecycle they occur:

1. Dependency/readiness inspection (per issue)
2. Deciding which ready issues can execute concurrently
3. Worker launch
4. Isolated workspace/worktree creation
5. Temporary worker branch creation
6. Worker lifecycle/status visibility
7. Implementation
8. Targeted verification
9. Broader relevant regression verification
10. `review-it`
11. Implementation-review ("Review implementation" / Gate 1) report
12. Human manual implementation approval
13. Commit planning
14. Human commit-plan approval
15. Commit creation
16. Human-facing decision presentation (how a report is worded)
17. Decision routing to the correct worker
18. Worker-specific resumption
19. Interrupted-worker recovery
20. Temporary-branch push
21. Convergence policy decision (how branches should converge)
22. Convergence execution (who actually merges/pushes)
23. Convergence sequencing/serialization across workers
24. Shared-branch state validation before mutating it
25. Combined (multi-worker) verification
26. Full-suite/skip decision — per issue, and, separately, at the combined-branch level
27. Push readiness (reachability, trailer re-check)
28. Issue closure, including "ask first"
29. Task-checkbox completion and validation
30. Next-work recommendation
31. Architectural/convention consistency across parallel workers
32. Overall human-facing lifecycle presentation

## Engineering skills

Responsibilities the evidence supports as already, correctly, owned by an existing skill — confirmed
by both the skill text and observed ST2 behavior:

| Responsibility | Skill | Evidence |
|---|---|---|
| Dependency/readiness inspection, per issue | `implement-it/rules/sequencing.md` | Recompute step ran correctly and identically across all three ST2 workers (`smoke-test-2.md`, "Next-issue recommendation" per worker) |
| Implementation | `implement-it` (+ stack companions) | Per-worker handbacks, all three ST2 workers |
| Targeted + broader regression verification | `implement-it/rules/verification.md` | Explicitly present and cited by name in every ST2 worker's report; matches the rule's own numbered procedure |
| `review-it` | `review-it` (independently callable) | Ran for all three ST2 workers (`smoke-test-2.md`, "Review and human approval" table) — a direct, confirmed reversal of ST1, where Travel skipped it entirely (`smoke-test-1.md`, "#355 Travel worker") |
| Implementation-review report + human approval | `implement-it/rules/review-gates.md` | All three ST2 workers stopped and reported, and none proceeded without explicit approval (`smoke-test-2.md` table); ST1's bypass is independently explained in `smoke-test-1.md`/`vision.md` as a delegation-prompt conflict, not a rule gap |
| Commit planning + human approval | `implement-it/rules/review-gates.md`, `rules/commit-boundaries.md` | Same evidence as above; no ST2 worker committed before its Commit-plan approval |
| Commit creation mechanics (trailer check, boundaries) | `implement-it/rules/commit-boundaries.md` | All nine ST2 commits individually trailer-checked, confirmed clean |
| Temporary issue branch, cut from the milestone branch | `implement-it/rules/sequencing.md`'s "Parallel workers" addition | The one behavioral change made before ST2; applied identically and unprompted by all three workers |
| Push readiness (reachability + trailer re-check) | `implement-it/rules/push-readiness.md` | Run, unmodified, by every ST2 worker before and after its push; ST1 bypassed this rule entirely rather than exposing a gap in it (`smoke-test-1.md`, "Parent-session post-worker behavior") |
| Issue closure, "ask first," and validation | `implement-it/rules/issue-closure.md` | All three ST2 issues closed with checkboxes independently re-verified on live GitHub (`smoke-test-2.md`, "Push and issue closure"); ST1's issues closed with checkboxes unchecked because the parent bypassed this rule, not because it was missing anything (`smoke-test-1.md`) |
| Next-work recommendation, per issue | `implement-it/rules/sequencing.md`'s recompute | All three ST2 workers independently recomputed and converged on the identical answer (#334/#344/#345) using only live GitHub state — no sibling-worker knowledge required |
| Milestone PR readiness (zero-open-issues + manual-testing sign-off) | `ship-it/rules/milestone-pr-readiness.md` | Not exercised by either smoke test (neither wave emptied its milestone), but read directly: its three conditions are stated in terms of live GitHub state and a human manual-testing answer, not an automated combined-verification run — see "Combined verification" below for why this does not make it the owner of that gap |
| Milestone closure gate | `ship-it/rules/milestone-completion.md` | Read directly: re-fetches and validates milestone state on closure; contains no automated-verification step at all |

## Worker responsibilities

Responsibilities that are per-issue, bounded, and normally *performed by running the skills above* —
listed separately because they are the shape a worker takes, not an additional policy layer:

- Owning one issue's full lifecycle end to end (implement → verify → `review-it` → both gates →
  commit → push → close → recompute).
- Reporting its own state truthfully and completely at each stop, including citing the exact rule
  text it is applying (e.g., every ST2 worker independently found and cited this repo's own prior
  `Merge issue-354-...`/`Merge issue-355-...` history as evidence, unprompted).
- **Convergence execution**, once policy and sequencing are supplied externally (see "Cross-worker
  responsibilities" below) — in ST2, each worker performed its *own* push and merge, inside its own
  worktree, once resumed and told the current shared-branch tip. This is worker-performed, not
  skill-specified: no rule in `implement-it` tells a worker how to converge; the worker executed
  ordinary git operations once the parent supplied the policy and the current state.
- Choosing execution-level technique within its own boundary — e.g., #343 independently invented the
  throwaway-branch-then-`push origin <throwaway>:<target>` technique to avoid disturbing the shared
  checkout in the main worktree, and #341/#342 reused it once the parent pointed them at it
  (`smoke-test-2.md`, "Convergence"). This is worker judgment, not skill policy, and not parent
  reasoning — no rule specifies this technique, and the parent did not invent it either.

## Runtime responsibilities

Mechanisms Claude Code supplied natively and successfully in both smoke tests. Described as portable
capability, not Claude Code's specific API, per `vision.md`'s and `orchestration.md`'s own framing:

| Claude Code mechanism | Portable capability |
|---|---|
| Background `Agent` (general-purpose, no custom worker-agent definition) | Concurrent, bounded execution context |
| `isolation:"worktree"` | Non-colliding workspace/branch state per worker |
| Task notifications / `ListAgents` | Worker identity, live status, lifecycle signaling |
| `SubagentHandback` (a worker's final/paused report) | Worker-to-parent result channel |
| `SendMessage` to a specific `agentId`, with `resumedAgentId` confirming the target | Addressable resume — a return channel that names exactly one recipient |
| Preserved worktree/branch after interruption (ST1) | Durable worker state sufficient for recovery |
| Agent resuming from its own prior transcript state | Continuation across a pause, without a portable "resume protocol" needing to be designed |

**What this means for Agentic Engineering:** none of the above should be reinvented as methodology.
`orchestration.md`'s "Human decision routing" and "Gate-specific worker resumption" watch items are
now positively observed (`smoke-test-2.md`, "Independent human-gated progression") — but the *mechanism*
that made them work was entirely this native runtime layer plus the parent's own conversational
tracking (see below), not a new methodology construct.

## Cross-worker responsibilities

The responsibilities that ST1 and/or ST2 show genuinely cannot be answered by one worker looking only
at its own issue.

### Concurrent-safe work selection

- **ST1 evidence:** observed once — the parent judged #354/#355 safe together based on disjoint
  expected surfaces (`smoke-test-1.md`; `orchestration.md`, "Concurrent-safe issue selection").
- **ST2 evidence:** not independently exercised by the run itself — the #341/#342/#343 wave was
  pre-selected by `parallel-dry-run.md` before the smoke test began, using the same kind of ad hoc
  file-disjointness investigation, with no skill rule computing or authorizing it. The run confirms
  the selection was correct in practice (zero conflicts) but adds no second independent data point for
  *how* the judgment gets made.
- **Evidence strength: REPEATED WITHIN ONE WAVE per occurrence, not REPEATED ACROSS ST1+ST2 as an
  independent decision** — the method (ad hoc human/parent investigation of file overlap) is the same
  both times, but ST2's instance was a dry-run artifact reused, not a second live decision.
- Remains outside individual workers: yes — a worker cannot see candidate sibling issues' surfaces
  from inside its own issue-scoped context.
- Not promoted further here: `orchestration.md`'s own framing (watch for recurrence) is unchanged by
  this evidence.

### Human-facing decision presentation

- **ST1 evidence:** none — no worker ever reached a gate, so no report existed to present.
- **ST2 evidence:** direct and specific. `review-it` produced substantive findings for two of three
  workers — a `policiesCount`-derivation/route-placement scope note (#343) and an explicit renewal-
  window judgment call (#342) — and both the worker's own report and the parent's relay of it wrapped
  that substance in internal vocabulary ("Gate 1," rule-file names) rather than plain statements of
  what was checked and what decision was needed (`smoke-test-2.md`, "Review and human approval," quoted
  directly there).
- **Evidence strength: OBSERVED ONCE**, but with three independent instances inside that one run (all
  three workers' reports carried the same pattern), plus the parent's own summaries repeating it.
- Distinction to hold: `review-it` continues to own *what* the review found; this is only about *how*
  an already-correct result is worded for the human. Do not move review semantics or findings out of
  `review-it`.
- Necessary knowledge: this specific instance (wording one worker's own report) does *not* strictly
  require cross-worker knowledge — a single-worker session would hit the identical wording gap, as
  `vision.md`'s own updated text now states. It is listed here because both smoke tests exercised it
  only inside a multi-worker run, not because it is inherently cross-worker.
- Not extracted: `orchestration.md`'s existing text already marks this "not extracted now... a single
  run's presentation gap is not repeated evidence." This document adds no new occurrence beyond that
  one run.

### Decision routing and worker-specific resume

- **ST1 evidence:** none — `orchestration.md` recorded this as "zero direct supporting execution
  evidence" before ST2.
- **ST2 evidence:** direct, and non-trivial. Two genuinely ambiguous human answers occurred (a
  human answer that didn't cleanly match any one worker's actual reported state) and both were
  resolved correctly (`smoke-test-2.md`, "Independent human-gated progression," with the exact quoted
  episodes). Every `SendMessage` call's `resumedAgentId` matched the intended target exactly; at no
  point did resuming one worker change a different worker's state.
- **Evidence strength: REPEATED WITHIN ONE WAVE** (two ambiguous cases inside the same run, both
  resolved correctly) — not yet REPEATED ACROSS ST1+ST2, since ST1 has zero occurrences to compare
  against.
- Inherently cross-worker: yes — routing a human answer to the *correct* one of several waiting
  workers requires knowing all their current states simultaneously; no worker skill has or needs that.
- Currently handled adequately: yes, on this one run — but `smoke-test-2.md` is explicit that the
  mechanism was "the parent session's own conversational memory... not a mechanism `implement-it`/
  `sequencing.md` defines," not a data structure or rule that guarantees correctness at higher worker
  counts or across a session restart.
- More evidence needed: yes, per both this document and `smoke-test-2.md`'s own conclusion — one run
  succeeding, including under ambiguity, is meaningfully stronger than ST1's zero occurrences, but
  short of `orchestration.md`'s "recurs across waves" bar.

### Convergence

Kept as four separate responsibilities, per the audit's own instruction not to collapse them:

- **Convergence policy** (what convergence should *look like* — push + merge into the milestone
  branch). **Human-decided, explicitly, both times it was needed.** In ST1 the parent inferred and
  performed a `git merge --no-ff` pattern itself, without asking (`smoke-test-1.md`, "Parent-session branch
  behavior" — the document explicitly calls this "not sourced from `implement-it` ... parent reasoning").
  In ST2, the exact same shape of policy ("push each temp branch and merge it into
  `feat/policies-http-frontend`") was an explicit human decision, requested by the workers and given by
  the human, not inferred by the parent (`smoke-test-2.md`, "Convergence"). **Evidence strength across both
  runs: the *policy itself* (temp-branch-then-merge) recurred identically twice, but who decided it
  changed — ST1 parent-inferred, ST2 human-decided** — this is a difference the two-file
  `sequencing.md` patch produced on purpose (it deliberately left convergence undefined so a worker
  would stop and ask, rather than letting the parent infer silently again).
- **Convergence execution** (who actually runs the merge/push). **Different between the two runs, and
  this is the sharpest finding in either report.** ST1: the parent performed both merges directly,
  itself (`smoke-test-1.md`). ST2: each *original worker*, resumed by name, performed its own push and
  merge inside its own worktree (`smoke-test-2.md`, "Convergence" — "each **original worker** was
  resumed... and performed its own push and merge itself... No fresh agent was created for
  convergence, and the parent session did not perform any merge or push directly," confirmed by
  `SendMessage` targets matching the original agent IDs). **Evidence strength: VALIDATED BEHAVIOR for
  ST2's specific shape (worker-performed), REPEATED FINDING only in the sense that "convergence
  happens somehow" recurred — the *performer* changed between runs**, so this is not simple
  recurrence of the same ownership.
- **Convergence sequencing/serialization** (ordering multiple workers' convergence to avoid a race).
  **ST1: not applicable** — the parent was a single actor performing both merges sequentially by
  construction; there was no serialization *decision* to make. **ST2: explicit and necessary** — the
  parent recognized a genuine race risk across three independently-acting workers converging onto one
  shared branch, chose an order (arrival order — whichever worker asked first was released first, not
  issue number or any other rule), and explicitly told each subsequent worker the shared branch's
  moved tip before that worker had fetched it itself (`smoke-test-2.md`, "Convergence"). **Evidence
  strength: OBSERVED ONCE**, and only because ST2 made convergence worker-performed in the first place
  — this responsibility did not exist as a distinct decision in ST1's single-actor shape.
- **Shared-branch state validation before mutating it.** Owned by the worker performing the mutation,
  both times evidence exists: in ST2, every worker fetched the shared branch fresh (not trusting a
  previously-known SHA) before merging and pushing, ran its own targeted verification against the
  merged tree, and trailer-checked the merge commit specifically (`smoke-test-2.md`, "Convergence").
  This is **worker responsibility**, exercised correctly each of three times — not cross-worker, since
  each worker only needed to validate the state it was about to mutate, using ordinary git commands.

**Do not collapse these four.** Policy is a human decision every time it has occurred; execution
became worker-owned in ST2 specifically because the skill patch made the worker stop and ask instead
of letting the parent infer silently; sequencing/serialization is the one piece that is inherently
cross-worker and was supplied only by the parent's own reasoning in ST2; state validation before
mutation is ordinary worker discipline, evidenced correctly both times it mattered.

### Combined verification

- **ST1 evidence:** a clean gap — `smoke-test-1.md` states plainly the final combined branch was never
  re-verified after both worker branches merged.
- **ST2 evidence:** the same gap, in a subtler shape. No explicit human full-suite/skip decision was
  ever presented against the truly final, fully-converged milestone branch. The closest substitute —
  the #341 worker's own 446-test run during its own convergence step — happened to run against code
  content-equivalent to the final state (because #341 converged last, after #342 and #343 had already
  landed), but it was a targeted subset the worker chose unilaterally as part of its *own* per-issue
  convergence procedure, not a combined-verification decision presented to the human, and not the
  unfiltered full suite (`smoke-test-2.md`, "Post-convergence verification" — which is explicit that this
  should not be reinterpreted as combined verification).
- **Evidence strength: REPEATED ACROSS ST1 + ST2**, in the specific sense that both runs produced this
  exact gap independently, under two different two-file-patch conditions (ST1 had no parallel-aware
  skill correction at all; ST2 had the sequencing.md patch and still produced the gap) — this is the
  strongest recurrence evidence in either document, for any candidate.
- **Why per-worker verification cannot fully own it:** each worker's targeted + broader verification
  (`implement-it/rules/verification.md`) is explicitly scoped to *its own issue's boundary* — the rule
  text itself never mentions a converged multi-worker state, and by design does not need to, since a
  worker cannot verify code it hasn't seen yet (siblings converging after it).
- **Is `ship-it`/milestone progression a credible owner?** Read directly for this document:
  `ship-it/rules/milestone-pr-readiness.md`'s three conditions are (a) zero open issues, re-queried
  from GitHub, (b) a human's direct yes/no on whether final manual testing happened, and (c) that
  testing found nothing further — there is no automated full-suite run anywhere in this rule; testing
  the manual answer is human self-report, not an automated regression check. `ship-it/rules/
  milestone-completion.md` re-fetches and validates milestone/issue state on closure and contains no
  verification step at all. **Neither is currently a credible owner of an automated combined-suite
  decision** — they own a different kind of gate (human sign-off that manual testing happened) at a
  later point in the lifecycle (after zero issues remain), not a verification decision against a
  freshly-converged branch mid-milestone, which is where this gap actually occurs (both ST1 and ST2
  converged mid-milestone, with other issues still open).
- **Is cross-worker orchestration a credible owner?** Plausibly, since verifying a union inherently
  requires knowing that union exists — but no run has ever exercised *anyone* correctly performing this
  as a deliberate decision, so there is no positive evidence to point to, only the repeated absence.
- **What remains unresolved (as a mechanism, after the policy decision below):** whether the fix is
  (a) a new explicit step somewhere in the existing lifecycle that the parent is always told to perform
  after convergence (a smaller correction than extraction), (b) a genuinely new cross-worker
  responsibility, or (c) something `ship-it`'s existing gates should absorb with a modest addition.
  `smoke-test-2.md`'s own conclusion (`Conclusion`, point 8) recommends deciding this deliberately
  before another smoke test.

#### Research decision, recorded after Smoke Test 2 (policy, not yet a skill change)

The gap above prompted an explicit interpretation change, recorded here as the current research
position for *concurrent* implementation workers specifically. This is a decision about **what
verification should happen and when**, separate from — and prior to — the still-open mechanism
question of *how* to construct a combined candidate state before any commit exists (see
`combined-candidate.md`).

**Per-worker verification.** A parallel implementation worker proves its own change with required
targeted verification, the narrowest meaningful broader regression verification, and `review-it`
against its completed implementation. A parallel worker does **not** get its own full-project-suite
run/skip decision. Running the full suite independently against several intermediate, not-yet-combined
worker states is not useful enough to justify its cost, and duplicates verification that combined
verification (below) will do once, properly, against the real union.

**Combined verification.** Once the parallel workers' candidate implementations are assembled into one
combined candidate state, the full project suite runs once against that combined state. This is a
required step for the parallel wave, not a run/skip decision — unlike the existing per-issue full-suite
choice `verification.md` already defines for a single (serial) worker, which is unaffected by this
decision. Only after the combined candidate is green should the human-facing implementation-review
checkpoint be presented. At that point the parent presents each worker's substantive `review-it`
summary and focused verification evidence in plain technical language, plus the combined full-suite
result, and asks the human to manually verify/approve each implementation before commit planning.

**Scope of this decision.** This applies only to concurrent/parallel implementation workers. It does
not silently change the normal serial/single-worker verification lifecycle — `verification.md`'s
existing full-suite run/skip decision for one worker, running alone, stays exactly as it is.

**Critical invariant, unchanged.** No durable implementation commit is created before both Review
implementation and Commit plan have received explicit human approval. This decision does not weaken
that guarantee, and no mechanism for combined verification is acceptable if it requires weakening it.

**The resulting unresolved mechanism.** Workers reach "ready" (implementation done, targeted/broader
verification passed, `review-it` run) while still uncommitted, because human approval hasn't happened
yet. Assembling several such uncommitted, isolated workers' changes into one temporary combined
repository state, in order to run the full suite against it once, without creating any durable
implementation commit ahead of the existing approvals, is not solved by anything observed in either
smoke test. ST2's temporary-branch convergence mechanism does not solve this: it only ever ran *after*
commits already existed and had already been approved (`smoke-test-2.md`, "Convergence"). This is
recorded as unresolved and investigated separately in `combined-candidate.md`.

### Next-work recommendation / ready-work selection

- Handled entirely and correctly by the existing skill (`implement-it/rules/sequencing.md`'s
  recompute), independently by all three ST2 workers, converging on an identical, correct answer
  (#334/#344/#345) each time (`smoke-test-2.md`).
- **Correction to this document's earlier framing.** An earlier pass through this analysis treated
  this as fully non-cross-worker and settled ("should clearly remain in the worker skill, no evidence
  it needs to move up"), on the grounds that the one sibling-awareness nuance observed — #343 and #342
  both separately, correctly noting that #341 already "had an active worktree/branch... likely already
  spoken for" — was derivable from public GitHub/git state (an existing branch) rather than privileged
  cross-worker visibility. That conclusion overstated what the evidence supports: it is true *in this
  run*, but it depends on the sibling's claim already being visible as a branch/commit by the time the
  recompute runs. Before any worker has pushed anything (e.g. two workers still mid-implementation, or
  one that hasn't yet created its temporary branch), the same recompute has no public signal to check
  against, and nothing in `sequencing.md` establishes what it should do then.
- **Current classification.** Keep `implement-it`'s existing per-worker recompute behavior unchanged —
  it produced the correct answer every time it was exercised, and there is no evidence it should move
  out of `sequencing.md` now. But classify next-work recommendation / ready-work selection as a
  legitimate **cross-worker extraction WATCH item**, not a settled, fully-owned worker responsibility:
  the "uses only public state" property that made ST2 look self-contained is a fact about this run's
  timing, not a guarantee `sequencing.md` enforces. Do not extract or design scheduling/orchestration
  for this now — there is exactly one wave of evidence, and it happens to be the favorable case.
- **What would strengthen or resolve this:** a future wave where a worker's recompute runs while a
  sibling's claim on a ready issue exists only in that sibling's own in-progress state (not yet a
  branch, commit, or comment visible to GitHub/git) — that would be the first real test of whether this
  remains adequately handled by public-state derivation or needs actual cross-worker knowledge.

### Architectural/convention drift

- **ST2 evidence, directly confirmed by inspecting the merged route files:** `clients.policies.index`
  landed in `routes/policies.php` (grouped by sub-resource domain, matching this repo's own
  `documents.php`/`notes.php` precedent); `agents.policies.index` and `carriers.policies.index` landed
  directly inside `routes/agents.php`/`routes/carriers.php` (grouped by owning entity, matching a
  *different* existing precedent — `carriers.branches.*`). Both choices are individually defensible
  against real prior conventions in the codebase; the three parallel workers picked two different,
  mutually inconsistent ones because none could see the others' route placement while implementing
  (`smoke-test-2.md`, "Convergence," second unexpected finding). #343's own closing comment flagged this
  as worth checking once all three landed; verified directly against the final merged state, they did
  not end up consistent, and no worker or human decision in the run performed that follow-up check.
- **ST1 evidence:** none directly comparable — #354/#355 touched genuinely separate page types with no
  shared convention decision point of this kind exposed in `smoke-test-1.md`.
- **Evidence strength: OBSERVED ONCE.**
- **Classification, per the audit's own caution against forcing ownership:** this is most precisely an
  **inherent parallelism risk specific to convention decisions with no established single precedent
  yet** — not a planning/architecture evidence problem in the `plan-it`/`lab-it` sense (the issues
  didn't fail to specify anything; both route placements were reasonable readings of real existing
  code), and not yet evidence for an orchestration responsibility, since fixing it would require either
  (a) a worker deferring a convention choice until it can see sibling precedent (which defeats
  concurrency) or (b) a reconciliation pass after convergence that no current skill or the parent
  performed in this run. **Insufficient evidence to assign ownership**; recorded as unresolved.

## Human-facing presentation

Kept as its own section per the required structure, consolidating what "Human-facing decision
presentation" above established at the level of one worker's report, plus the parent's own summaries:

- `review-it` produced real, specific substance for two of three ST2 workers (quoted directly in
  `smoke-test-2.md`, "Review and human approval"). That substance mostly survived the parent's relay in
  compressed form, but both the worker reports and the parent's own summaries to the human carried
  internal methodology vocabulary ("Gate 1," "Gate 2," rule-file names) that adds no engineering
  information for a human deciding whether to approve.
- This did not break lifecycle correctness in this run: both gates held for all three workers, nothing
  committed early, and the substance was not actually lost, only wrapped in unnecessary vocabulary.
- **Classification: a presentation finding, not automatically a skill defect.** `review-gates.md`
  itself permits internal identifiers "when precise rule references need them" but does not mandate
  exposing them in the human-facing report — so the gap is in how the parent (and, in this run, the
  workers' own reports) chose to phrase things, not in what the rule requires.
- `vision.md` and `orchestration.md` have already been updated with this finding and the boundary
  distinction (skills own engineering semantics/results; the parent, or a future orchestrator, owns how
  those results are worded for a human) — this document does not restate that update, only confirms it
  traces cleanly to ST2 evidence and adds no new occurrence beyond the one already recorded.

## Narrowing opportunities

Examined per the audit's Part 7 — where a currently-broad skill responsibility *might* eventually
narrow if a cross-worker responsibility is extracted, without proposing that extraction now:

- **`implement-it`'s next-issue recommendation.** Current owner: `implement-it/rules/sequencing.md`'s
  recompute, run per-worker. Why it made sense: for a single serial worker, "what's next" is a natural
  extension of "this issue just closed." New evidence from ST2: three workers independently ran the
  same recompute and got the identical answer, including a sibling-awareness nuance (#341's active
  branch) that happened to be derivable from public state rather than requiring genuine cross-worker
  knowledge. **This is not yet evidence the responsibility must move out of `implement-it`** — the
  current scope (per-worker, GitHub-state-driven) handled the multi-worker case correctly this time,
  by using only public state. But per the corrected "Next-work recommendation / ready-work selection"
  entry above, that correctness was contingent on the sibling's claim already being publicly visible —
  it is not a guarantee the rule enforces. Watch, don't narrow: keep current behavior, but treat this
  as a live cross-worker extraction WATCH item rather than a closed question. A future scenario where a
  worker needs a sibling's *private* in-progress state (not yet on GitHub) to recommend correctly would
  be the evidence that resolves it one way or the other; none exists yet.
- **Sequencing/readiness behavior that spans multiple issues.** Current owner: `implement-it/rules/
  sequencing.md`, including its new "Parallel workers" section. Why it made sense historically:
  written for one worker deciding its own branch. New evidence: the "Parallel workers" addition
  already had to state a fact that is true across the whole wave (the milestone branch is the shared
  eventual convergence target) without owning coordination of that wave — and it deliberately does
  not. This is already the narrowest version of the fact this rule needs; no further narrowing is
  indicated, and no widening either (the rule was correctly written to state the fact and stop).
- **Any cross-worker progression logic that might be tempting to add to `implement-it`.** Not observed
  as an actual temptation in either run — no worker's report or the parent's own reasoning added
  progression logic beyond what `sequencing.md` already specifies. Recorded as a thing to keep
  watching for, not a finding.

**Conclusion for this section:** no narrowing is justified now. The clearest future trigger would be a
worker needing knowledge of a sibling's *private, not-yet-public* state to make a correct per-issue
decision — that has not happened in either smoke test.

## Responsibility matrix

| Responsibility | Current owner | Evidence | Cross-worker knowledge required? | Candidate future owner | Confidence | Action now |
|---|---|---|---|---|---|---|
| Dependency/readiness inspection (per issue) | `implement-it/sequencing.md` | ST2, all 3 workers | No | — | High | KEEP |
| Concurrent-safe issue selection | Human/parent judgment, ad hoc | ST1 once; ST2 reused a prior dry-run's selection | Yes | Unresolved | Low | WATCH |
| Worker launch | Native runtime (`Agent`) | ST1 + ST2 | N/A | — | High | RUNTIME — DO NOT REIMPLEMENT |
| Isolated worktree creation | Native runtime | ST1 + ST2 | N/A | — | High | RUNTIME — DO NOT REIMPLEMENT |
| Temporary worker branch | `implement-it/sequencing.md`'s patch | ST2, all 3 workers, unprompted | No (per-worker fact) | — | High | KEEP |
| Worker lifecycle/status visibility | Native runtime (notifications, `ListAgents`) | ST1 + ST2 | N/A | — | High | RUNTIME — DO NOT REIMPLEMENT |
| Implementation | Worker / `implement-it` + companions | ST1 + ST2 | No | — | High | KEEP |
| Targeted + broader verification | `implement-it/verification.md` | ST1 + ST2 | No | — | High | KEEP |
| `review-it` | `review-it` | ST2 all 3; ST1 one of two skipped it (bypass, not gap) | No | — | High | KEEP |
| Implementation-review report + approval | `implement-it/review-gates.md` | ST2 all 3; ST1 bypassed | No | — | High | KEEP |
| Commit planning + approval | `implement-it/review-gates.md`, `commit-boundaries.md` | ST2 all 3; ST1 bypassed | No | — | High | KEEP |
| Commit creation | `implement-it/commit-boundaries.md` | ST2 all 3 | No | — | High | KEEP |
| Human-facing decision presentation (wording) | Parent session (today); not skill-specified | ST2, one run, repeated 3x within it | Not inherently — recurs even single-worker | Possible future orchestrator, unresolved | Low-Medium | WATCH |
| Decision routing to correct worker | Parent session's own reasoning, via native `SendMessage` | ST2, incl. 2 ambiguous cases resolved correctly | Yes | Unresolved | Medium | WATCH |
| Worker-specific resumption | Native runtime (`SendMessage`/`resumedAgentId`) + worker re-validating its own resumed state | ST2 all 3 | Partly (targeting is cross-worker; validity re-check is per-worker) | — | Medium-High | RUNTIME — DO NOT REIMPLEMENT (targeting); KEEP (validity re-check) |
| Interrupted-worker recovery | Native runtime (workspace/branch preservation) + `review-gates.md`'s approval-validity check | ST1 once, pre-gate only; not exercised mid-gate in ST2 | Partly | — | Low (mid-gate case untested) | WATCH |
| Temporary-branch push | Worker, using `push-readiness.md` mechanics | ST2 all 3 | No | — | High | KEEP |
| Convergence policy decision | Human, explicitly, both times needed | ST1 inferred by parent (no ask); ST2 explicit human decision | Yes (deciding for the whole wave) | Human decision, standing | High (should stay human) | KEEP — always ask |
| Convergence execution | Worker, resumed, in its own worktree | ST2 all 3; ST1 was parent-performed instead | No, once policy+current-tip are supplied | — | Medium (one run) | KEEP, watch for recurrence |
| Convergence sequencing/serialization | Parent-session reasoning | ST2 only; not applicable in ST1's single-actor shape | Yes | Unresolved | Medium (one run, no conflict tested) | WATCH |
| Shared-branch state validation before mutation | Worker (fetch fresh, verify, trailer-check) | ST2 all 3 | No | — | High | KEEP |
| Combined (multi-worker) verification | Policy now decided (required full-suite run once, before implementation-review); mechanism unowned | ST1 gap; ST2 gap in a subtler shape — recurs across both runs; post-ST2 research decision recorded above | Yes | Unresolved — see `combined-candidate.md` | Low (policy: High; mechanism: Low) | NEEDS DECISION (mechanism only) |
| Full-suite/skip decision, per issue (serial worker) | `implement-it/verification.md` | ST1 + ST2, though ordering vs. `review-it` deviated 2/3 times in ST2 | No | — | High (rule is sufficient); ordering visibility is the actual gap | CLARIFY (see Skill findings) |
| Full-suite decision, per parallel worker | Removed by research decision — no longer a per-worker choice | Post-ST2 decision (above); not yet exercised in a smoke test | No | — | Medium (decided, unvalidated) | NEEDS VALIDATION in Smoke Test 3 |
| Push readiness | `implement-it/push-readiness.md` | ST2 all 3, unmodified; ST1 bypassed entirely | No | — | High | KEEP |
| Issue closure + validation | `implement-it/issue-closure.md` | ST2 all 3, independently re-verified; ST1 bypassed | No | — | High | KEEP |
| Next-work recommendation / ready-work selection | `implement-it/sequencing.md` (behavior unchanged) | ST2 all 3, converged on identical answer, using only public state | Contingently — correct this run only because a sibling's claim was already public | Unresolved | Medium | KEEP behavior; WATCH as cross-worker candidate |
| Architectural/convention consistency across parallel workers | **Unowned** | ST2 once — real, confirmed drift | Yes, to detect; unclear to prevent without serializing | Unresolved | Low | WATCH |
| Overall human-facing lifecycle presentation | Parent session (today) | ST2 | Not inherently | Possible future orchestrator, unresolved | Low-Medium | WATCH |

## Candidate future boundary

Based only on the evidence above, the smallest conceptual boundary currently justified is narrower than
`vision.md`'s original four-layer hypothesis diagram. What the evidence actually supports:

```text
Human
  ↓ (always decides: concurrent-safe selection, convergence policy, full-suite choices)
Workers (bounded per-issue lifecycle, via existing skills)
  ↓
Runtime execution primitives
```

with one additional thin layer that recurred *only* when more than one worker existed at once, and
only for a small number of specific things — not a general coordination responsibility:

```text
Human
  ↓
[ thin cross-worker layer, positively observed but only once each: ]
  - decision routing (human answer → correct waiting worker)
  - convergence sequencing/serialization
  - (still missing entirely) combined verification
  - (still missing entirely) cross-worker convention reconciliation
  ↓
Workers
  ↓
Skills
  ↓
Runtime
```

**What this layer owns**, stated as scope, not mechanism: enough visibility across all currently-active
workers' states and the shared branch's current tip to (a) get a human's answer to the worker it
actually belongs to, (b) order and inform multiple workers converging onto shared state so they don't
race, and, if a future decision extends it, (c) decide when a combined-state check is needed and (d)
notice when parallel workers made inconsistent decisions.

**What is explicitly not decided here:** whether this layer is a skill, a `.claude/agents/
orchestrator.md` definition, a long-lived agent, a process, a service, a repository, or continues to
be informal parent-session reasoning indefinitely. Two smoke tests is not the recurrence
`orchestration.md`'s own extraction bar asks for before choosing an artifact form.

## Extraction bar

Restated from `orchestration.md`, refined against what ST2 actually added evidence for. A responsibility
is a credible candidate for extraction out of an existing skill or out of ad hoc parent-session
behavior once it:

- is inherently cross-worker rather than per-issue (confirmed, not assumed, by evidence that a worker
  cannot answer it from its own issue-scoped state);
- remains necessary after the relevant skill has already been corrected for the parallel case (ST2
  tests this directly — `sequencing.md`'s patch was live, and the responsibility still required parent
  reasoning);
- recurs across real execution waves, not just within one wave's several instances of the same kind of
  event;
- creates awkward or duplicated ownership if left inside a worker skill (a worker would need knowledge
  it structurally cannot have);
- can be stated independently of Claude Code-specific primitives (named as scope/capability, not as
  `Agent`/`SendMessage` calls).

Applying this bar to every candidate above: **only "combined verification" recurs across both ST1 and
ST2** in the strict sense of the same gap appearing independently in two separate runs under two
different skill-correction states. Every other cross-worker candidate (decision routing, convergence
sequencing, architectural drift) has exactly one wave's worth of evidence — real, but not yet
recurrence in the sense this bar requires. None of the four currently clear the bar for "extract now";
"combined verification" is the closest, and even it is closer to "needs an explicit decision somewhere
in the existing lifecycle" than to "needs a new artifact" on the evidence gathered so far. The *policy*
half of that decision has now been made (see "Combined verification"'s research decision, above); the
remaining open question is narrower and purely mechanical — how to construct the combined candidate
state before commit, investigated separately in `combined-candidate.md` — and still does not clear this
bar for "extract into an orchestrator," since the mechanism may turn out to be ordinary Git/parent
reasoning rather than a new cross-worker artifact.

## What remains unresolved

- **Combined verification's mechanism.** The policy (required full-suite pass against the assembled
  combined candidate, before implementation-review) is now decided; the mechanism for safely
  constructing that pre-commit combined candidate state without violating the existing approval
  invariant is not — investigated in `combined-candidate.md`, unvalidated by any smoke test yet.
- **Combined verification's owner, once a mechanism exists.** Not resolved as to whether running the
  mechanism is a `ship-it` addition, a new explicit parent-session step, or something else.
- **Whether decision routing and convergence sequencing recur identically in a third wave**, especially
  one with a higher worker count, a genuine file overlap/merge conflict, or a human answer arriving
  while a worker is still mid-execution rather than already paused — none of these conditions has been
  tested.
- **Whether architectural/convention drift across parallel workers is a recurring risk or a one-off** —
  one confirmed instance is not enough to classify it as inherent-to-parallelism versus incidental to
  this specific wave's issue shapes.
- **The precise cause of the `review-it`-before-full-suite-decision ordering deviation** (see "Skill
  findings" below) — this document adds skill-text evidence narrowing it, but does not fully resolve
  it without access to each worker's own reasoning at the moment it made the choice.
- **Whether worker-performed convergence (ST2's shape) remains worker-performed at higher worker counts
  or under contention**, or whether some other factor made ST1's parent-performed shape emerge instead
  of this one — both are one data point each; a third wave is needed to see which is the pattern and
  which was the outlier.
- **Artifact form for any eventually-extracted cross-worker responsibility** — deliberately left
  undecided in this document per its own instructions.

## Skill findings

Kept conservative per the audit's own instruction, especially regarding `review-gates.md`,
`verification.md`, `push-readiness.md`, and `issue-closure.md`.

**Existing rules confirmed sufficient by this run (no change indicated):**
- `review-gates.md` — both approvals held across all three ST2 workers with no exception needed for
  how work was launched or delegated.
- `push-readiness.md` — its branch-identification step resolved correctly, unmodified, for all three
  workers, regardless of the temporary-branch detour that preceded it.
- `issue-closure.md` — its "ask first," closing recipe, and validation ran correctly, independently,
  three times, confirmed against live GitHub state by this and the prior audit.
- `sequencing.md`'s two-file parallel-worker patch — performed exactly as designed: made concurrent
  worktrees possible, specified nothing about convergence beyond the fact that it must eventually
  happen, and every worker correctly treated the undefined mechanics as a stop rather than guessing.

**Candidate rule correction with evidence (narrower than a rewrite):**
- The ordering requirement — full-suite decision before `review-it` — is real and explicit, but it
  lives only in `SKILL.md`'s composition text ("invoking `review-it` only after the required
  verification decisions have been completed," and, more explicitly, "the human full-suite run/skip
  decision that must be surfaced and answered before `review-it` or Review implementation," both read
  directly from `SKILL.md` for this document). `rules/verification.md`'s own operative procedure (the
  numbered "Targeted verification before Gate 1" steps, and "Full-suite choice") states the full-suite
  ask as step 4 but does not itself restate that `review-it` must wait for it — a worker following the
  individual rule files it was told to load (`verification.md`, `review-gates.md`) rather than
  `SKILL.md`'s own summary sentence could plausibly miss the ordering constraint. Two of three
  independent ST2 workers deviated in exactly this way. **This narrows `smoke-test-2.md`'s own
  "unresolved, not attributed" finding**: the rule exists and is unambiguous at the `SKILL.md` level,
  but is not restated where a worker actually executes the procedure. A conservative fix, if any is
  made, would restate the ordering inside `verification.md`'s own procedure or `review-gates.md`'s
  "Consuming review-it's result" entry condition — not a semantic change to what either gate requires.
- **This document takes no position on whether that restatement should actually be made** — it reports
  the evidence more precisely than the prior audit could (having read the actual skill text), leaving
  the decision to whoever reviews this analysis.

**Execution mistake / rule not followed:**
- No instance in ST2 where a worker violated an unambiguous rule outside the ordering deviation above.
  ST1's failures (`review-it` skipped, both gates bypassed, push/closure bypassed) are independently
  attributed in `smoke-test-1.md`/`vision.md` to a contradictory delegation prompt, not to worker error
  against a clear rule.

**Cross-worker responsibility — do not put into a worker skill yet:**
- Convergence sequencing/serialization, decision routing, and combined verification — all three remain
  outside any worker's own visibility by construction (a worker has no view of sibling workers' state
  or a converged branch it hasn't seen). None should move into `implement-it`'s per-issue rules.

**UX/presentation finding:**
- Restated from "Human-facing presentation" above: internal gate/rule vocabulary reached the human in
  both worker reports and the parent's relay, without breaking lifecycle correctness. Already captured
  in `vision.md`/`orchestration.md`; this document adds no new occurrence.

## Recommended next step

Answering the audit's six framing questions directly:

1. **Does the validated two-file `implement-it` patch need further change?** Not based on this
   evidence. The one candidate correction found (ordering visibility for the full-suite-before-
   `review-it` requirement) is in `SKILL.md`/`verification.md`, not in the two-file patch itself,
   and is offered as evidence, not a mandated fix.
2. **Is parallel implementation ready for documentation/publication?** Not yet, on this document's own
   evidence standard — the combined-verification *mechanism* (constructing a pre-commit combined
   candidate state) remains unresolved (`combined-candidate.md`), and publishing before validating it
   in a smoke test would document an untested mechanism as if it were proven.
3. **Does combined verification need a methodology decision before publication?** Yes, and the policy
   half of that decision has now been recorded (see "Combined verification," above): per-worker
   verification excludes a per-worker full-suite choice; combined verification is a required, not
   run/skip, full-suite pass against the assembled candidate, before the implementation-review
   checkpoint. What remains is validating the mechanism that assembles that candidate without violating
   the existing approval invariant — see `combined-candidate.md` and point 4 below.
4. **Is another smoke test needed?** Yes, and it should deliberately exercise what both prior runs
   could not by construction: a real file overlap or merge conflict during convergence, a worker
   interruption mid-gate (not merely pre-gate workspace preservation), a worker count beyond three, and
   an explicit test of whatever combined-verification decision gets made in response to point 3.
5. **Is there enough evidence to begin an orchestration design investigation?** No, by this document's
   own extraction bar. Three of the four live cross-worker candidates have exactly one wave of
   evidence each; only combined verification recurs, and even it looks more like a lifecycle-gate
   correction than an orchestrator-shaped responsibility on the evidence gathered so far. A third
   smoke test, specifically targeting the untested conditions in point 4, should precede any
   artifact-form decision.
6. **Which responsibilities should remain WATCH items instead of decisions?** Concurrent-safe issue
   selection, human-facing decision presentation, decision routing, convergence sequencing, worker
   recovery mid-gate, next-work recommendation / ready-work selection, and architectural/convention
   drift — each has real but single-occurrence (or contingently-correct) evidence; none should be
   decided, extracted, or codified from this evidence alone.
