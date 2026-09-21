# Parallel Implementation Smoke Test 2 — Dry Run

Status: Investigation and dry run. Consumer evidence gathered against `elieandraos/useOrbit`,
Phase 26 — Policies HTTP & Frontend milestone. No useOrbit code, issues, or branches were touched to
produce this document, and no installed skill file was modified — every change below is a proposal
only.

This document treats `vision.md`, `smoke-test-1.md`, and `orchestration.md` as the current, not-yet-accepted
investigation state, and treats the skills installed in useOrbit's `.agents/skills/` (`implement-it`,
`review-it`, `ship-it`, `plan-it`) as the actual methodology being exercised — not the canonical
GitHub copies.

The proposed patch below went through three review passes before being accepted here: an initial
five-file draft, a first reduction that cut two files and trimmed two more, and a final pass that
cut the remaining convergence mechanics and the combined-verification rule entirely. What survives is
two files. The rest of this document explains what was cut and why, and is explicit about what
Smoke Test 2 is now expected to observe with no rule backing it, rather than execute against a
codified procedure.

## Candidate wave

**Selected: #341 (Client), #342 (Agent), #343 (Carrier) — "Wire the Policies tab on the `<entity>`
show page."**

All three:

- are dependency-ready right now — each depends only on #322 ("Policies: list all policies"), which
  is closed; `gh issue list --milestone "Phase 26 — Policies HTTP & Frontend" --state open` shows six
  open issues, and all six issues' stated dependencies (#322, #332, #335, #336) are closed;
- are explicitly the same shape as each other in their own issue text — each says "Same shape again"
  or "Same shape as the Client tab-wiring issue" and follows an identical task template: add a
  `HasMany` relation, add a per-entity `*PoliciesController::index()` + named route, feed a real
  `policiesCount`, convert a dead/placeholder tab to a real `href`;
- touch verifiably disjoint files. `routes/` already has one file per entity —
  `routes/clients.php`, `routes/agents.php`, `routes/carriers.php` — confirmed by directory listing,
  so the three new named routes (`clients.policies.index`, `agents.policies.index`,
  `carriers.policies.index`) land in three separate files, not one shared routes file. Each issue also
  touches its own model (`Client`, `Agent`, `Carrier`), its own controller
  (`ClientsController`/`AgentsController`/`CarriersController`), and its own detail-shell Vue component
  (`ClientDetailShell.vue`/`AgentDetailShell.vue`/`CarrierDetailShell.vue`). The one class both sides
  read — `PolicyResource` — is pre-existing and read-only for all three; none of the three issues
  modifies it;
- are close in size (4–5 tasks each), with one deliberate size difference: #342 (Agent) has an extra
  task wiring `PoliciesRenewalCard.vue` to real data, which #341/#343 don't have an equivalent of. This
  gives the wave a plausible reason to diverge in completion speed — useful for observing the
  "workers in different lifecycle states" scenario `vision.md` and `orchestration.md` both flag as
  unobserved.

This is structurally the closest available analog to the #354/#355 experiment: three
policy/entity-scoped issues in the same milestone, file-disjoint by construction, continuing the same
kind of "wire the tab" work the milestone has already been doing.

**Considered and set aside:**

- **#334** ("Add Policies link to top nav") — dependency-ready, touches one file
  (`resources/js/components/shell/navItems.ts`), zero overlap with the other three. Genuinely safe to
  add as a fourth worker, but too small to exercise the gate lifecycle meaningfully — it would likely
  reach Review implementation before targeted verification has finished mattering. Left out to keep the
  wave at three comparably-weighted workers rather than diluting it with a trivial one; note this as a
  candidate for a future *speed-mismatch-specific* smoke test if #341/#342/#343 turn out too similar in
  pace to exercise that scenario.
- **#344** ("Policies index filters drawer") — dependency-ready, but scoped to the shared Policies
  index page area rather than a new entity surface; lower novelty relative to #354/#355, and shares
  conceptual (not file) territory with #345.
- **#345** ("Policies show page — Members tab") — dependency-ready, but single-file-scoped
  (`PolicyMedicalDetailShell.vue`) and carries more UX/roster-design nuance than gate-mechanics
  novelty. A weaker choice for testing lifecycle/gate correctness specifically.

Not started. This selection is a recommendation for the next authorized wave, not authorization to
launch it. It was produced by ordinary ad hoc investigation of the milestone and the repository — no
skill rule was needed to produce it (see "Current installed-skill gaps" below).

## Desired execution trace

Walking the 20 transitions from the brief, with explicit actor ownership. "Worker" means one
background agent instance bound to one issue. Steps 13–16 are marked explicitly where no skill rule
governs them — those are what this smoke test is actually for.

1. **Worker launch** — Parent Claude session selects #341/#342/#343 as the concurrent-safe subset,
   based on the file-disjointness investigation above — this is parent-session judgment, not a
   codified rule (see "Current installed-skill gaps"). Native Claude Code runtime creates three
   background agents, each in its own isolated worktree, each checked out on its own temporary issue
   branch cut from the milestone branch (`feat/policies-http-frontend`) — the one structural carve-out
   proposed below, in `sequencing.md`. The delegation prompt for each worker instructs it to run
   `implement-it` to completion **including both approval stops** — it does not tell the worker to
   stop once committed. This is the actual fix for `smoke-test-1.md`'s root cause; it is a change to how
   the wave is launched, not to any skill file (see "Existing rules already sufficient").
2. **Implementation** — Each worker, running `implement-it`, with `companion-activation.md`'s
   checkpoint completed first (`inertia-vue-development`, `laravel-inertia-stack`,
   `wayfinder-development`, `testing-best-practices`, and any applicable stack companion, per each
   worker's own activation decision — no change from single-worker behavior).
3. **Targeted verification** — Each worker, `verification.md`, narrowest reliable scope for its own
   entity (e.g. Client-policies tests for #341).
4. **Broader regression verification** — Each worker, `verification.md`'s existing human full-suite
   choice, answered by whoever is watching that specific worker session — likely the same "Policies"
   regression scope #354/#355 used, but that is a useOrbit convention, not methodology.
5. **`review-it`** — Each worker invokes it standalone against its own worktree
   (`review-it/rules/scope.md` already handles "a worktree" as a first-class target with no
   parallel-specific change needed).
6. **Review implementation report** — Each worker reports per `review-gates.md`, including the
   `Activated skills:` line and `review-it`'s result, and states the exact decision requested. No
   skill change is proposed for this step — `review-gates.md`'s existing "No commit is created before
   Commit plan is approved" is already unconditional; nothing in it exempts a delegated or
   background-launched worker. What matters is that this run's delegation prompt (step 1) doesn't ask
   the worker to do anything the rule already forbids.
7. **Human manual review + approval** — Human, using the runtime's existing ability to switch into a
   specific worker's session (already validated in Smoke Test 1) to read that worker's Review
   implementation report and decide.
8. **Resuming only the approved worker** — Human addresses that specific worker session; native Claude
   Code runtime resumes it. No skill-level "resume" logic is proposed — this is Category C, and is the
   most orchestrator-shaped hypothesis still unproven (see "Unknowns," below).
9. **Commit plan** — The resumed worker only, per `review-gates.md` Gate 2 and `commit-boundaries.md`,
   scoped to its own diff. No cross-worker content.
10. **Human Commit plan approval** — Human, per worker, independently of the other two workers' states.
11. **Commit** — Worker, per `commit-boundaries.md`'s mechanics and the mandatory post-commit trailer
    check.
12. **Worker completion / handback** — Native Claude Code runtime (task notification, live roster);
    worker reports completion to the parent session.
13. **Convergence onto the shared milestone branch — NOT GOVERNED BY ANY RULE.** Parent session,
    presumably by merging each worker's temporary branch into the milestone branch once that worker's
    commits are approved (the `git merge --no-ff` pattern the parent improvised in Smoke Test 1), but
    neither who performs this nor when it happens relative to sibling workers is specified anywhere.
    `sequencing.md`'s proposed addition only establishes that the milestone branch is the *eventual*
    convergence target — it deliberately says nothing about the mechanics or timing. Observe what the
    parent session actually does.
14. **Combined verification evidence summary — NOT GOVERNED BY ANY RULE.** Whether or how the parent
    session restates each converged worker's targeted + broader results as evidence for one combined
    decision is unspecified. `vision.md`'s diagram describes this as desirable; no installed rule
    requires or shapes it. Observe whether it happens, and whether it happens correctly.
15. **Full-suite/skip decision — NOT GOVERNED BY ANY RULE at the combined-state level.**
    `verification.md`'s existing full-suite choice is scoped to a single issue's boundary; it is not
    extended to a converged multi-worker branch. Whether the human is asked this once for the combined
    state, or the question doesn't arise cleanly at all, is exactly what this smoke test should reveal.
16. **Combined verification** — If the human chooses to run one, the parent session runs the check
    against the milestone branch post-convergence, using useOrbit's actual full-regression command
    (`php artisan test --compact --no-tia`) — project-specific, not portable methodology, and not
    mandated by any rule at this scope.
17. **Push readiness** — `push-readiness.md`, entirely unchanged. By the time this runs (after whatever
    happened in steps 13–16), the relevant commits should already be on the milestone branch, and this
    rule's existing "the milestone's shared branch for milestone work" resolves correctly without
    needing to know anything about the temporary-branch detour that preceded it — the rule only checks
    whether commits are reachable now, not how they arrived.
18. **Issue closure** — `issue-closure.md`, run independently per issue — #341, #342, #343 each closed
    separately, each going through its own task-checkbox verification and post-mutation validation.
19. **Issue task completion / validation** — Already required by `issue-closure.md`'s existing step 1
    and "Validation" section; this smoke test is a direct regression check against #354/#355's failure
    to actually check any boxes.
20. **Recomputation of remaining ready work** — `sequencing.md`'s existing recompute, run once all
    three closures are validated; reports what #341/#342/#343 closing newly unblocks (if anything) and
    restates #334/#344/#345 as still open.

## Responsibility classification

| # | Behavior | Class | Notes |
|---|---|---|---|
| 1 | Launch parallel background agents in isolated worktrees | C | Already demonstrated, Smoke Test 1 |
| 2 | Per-worker `implement-it` lifecycle (implement → verify → review-it → gates → commit) | A | Already correctly specified; failure in ST1 was bypass, not a gap |
| 3 | Concurrent-safe candidate evidence (file/surface overlap) | D | Genuinely cross-worker per `orchestration.md`'s own framing; observed once, not yet corrected — left to parent-session judgment for this wave, not codified |
| 4 | Selecting *which* ready issues to run concurrently | (human) | Always the human's call; no skill computes or authorizes this |
| 5 | One shared working branch per milestone (current rule) | B | Needs the temporary-issue-branch carve-out for the parallel case only; single-worker default unchanged. This is the one surviving correction |
| 6 | Isolated worktree/temporary branch creation mechanics | C | Native `Agent(isolation:"worktree")`-equivalent; not encoded into methodology |
| 7 | Worker cannot treat delegation as gate approval | A | Already correctly specified — "No commit before Commit plan approved" is already unconditional. ST1's failure was a contradictory delegation prompt (a launch-time/process problem), not a skill gap; `vision.md` itself says not to rewrite gate semantics because the experiment failed to honor them |
| 8 | `review-it` working against a single worker's worktree | A | Already scope-agnostic; no change |
| 9 | Human switching into a specific worker session | C | Already demonstrated, ST1 |
| 10 | Resuming exactly the approved worker without affecting siblings | E | Not yet exercised — no worker in ST1 ever reached a gate |
| 11 | Decision routing (human answer → correct worker) as explicit machinery | E | Zero direct evidence either way; `orchestration.md` already flags this as the most orchestrator-shaped, least-evidenced hypothesis |
| 12 | Per-worker targeted + broader verification | A | Already correctly specified and already observed working in ST1 |
| 13 | Per-worker `review-it` before Review implementation | A | Already correctly specified; ST1's Travel worker skipping it was a bypass, not a gap |
| 14 | Temporary branch instead of the shared branch (structural carve-out) | B | The one part of "convergence" that's actually corrected — otherwise concurrent worktrees are mechanically impossible |
| 15 | Who performs the merge into the milestone branch, and when | E | Deliberately unowned; `orchestration.md`'s own watch item; observe |
| 16 | Convergence waiting for the whole wave vs. per-worker | E | Deliberately left open — not resolved by rule, not pre-answered |
| 17 | Combined-state verification evidence summary + full/skip decision | E | Ownership explicitly unresolved per `orchestration.md` ("do not assign ownership prematurely"); no rule added; observe whether the parent session does this correctly on its own |
| 18 | Push-readiness reachability check | A | Entirely unchanged; already branch-agnostic to how commits arrived, only checks whether they're reachable now |
| 19 | Issue closure, including task-checkbox validation | A | Already required; ST1's unchecked boxes were a bypass of an existing rule, not a missing one |
| 20 | Milestone PR readiness / release | A/C | Re-queries fresh GitHub state; not session-bound; nothing here assumes one worker |
| 21 | Merge-conflict handling during convergence | E | Not observed (#354/#355 were non-overlapping); no resolution policy in any rule — watch what happens if it occurs |
| 22 | Worker interruption/recovery mechanics | C (mechanics) + A (approval-validity check) | `review-gates.md`'s existing "Approval validity" section already covers re-confirming an approval before relying on it again; recovery itself is runtime |
| 23 | "Worktree" vocabulary meaning two different things across the skill family | B | One clarifying sentence, not a behavior change |

## Current installed-skill gaps

After three review passes, exactly one real behavioral gap survives, plus one terminology risk:

1. **`implement-it/rules/sequencing.md`, "Delivery/phase milestone issue"** (the section stating "All
   issues in that milestone share one working branch — implementation does not get a fresh branch per
   issue") has no provision for more than one worker implementing different issues in the same
   milestone at once. Git cannot check the same branch out in two worktrees simultaneously, so this
   rule, taken literally, makes concurrent workers in one milestone impossible without parent
   improvisation — which is exactly what happened in ST1 (`smoke-test-1.md`, "Parent-session branch
   behavior"). This is the one gap that actually blocks Smoke Test 2 from being runnable at all under
   the current text, and the only behavioral change proposed below.
2. **Terminology risk, not a behavior gap**: `implement-it/rules/worktree-preservation.md`,
   `rules/verification.md`, and `review-it`'s rules all use "worktree" to mean the single active
   checkout's working tree/index (uncommitted content, `git status --porcelain`). The parallel-worker
   design in `vision.md`/`smoke-test-1.md` uses "worktree" for Claude Code's isolated `git worktree`
   checkouts. Both senses now live in the same skill family the moment (1) lands. This was flagged in
   the prior audit referenced by the brief; it remains unresolved in the installed files.

Three earlier candidate gaps were investigated and rejected after review — kept here for record, not
as pending work:

- **A gate-delegation clause in `review-gates.md`.** Investigated, drafted, then removed: the existing
  rule is already unconditional, and `vision.md` explicitly warns against rewriting gate semantics
  because Smoke Test 1 failed to honor them. See "Existing rules already sufficient."
- **A "concurrent-safe candidate evidence" reporting rule in `sequencing.md`.** Investigated, drafted,
  then removed: `orchestration.md` itself calls this relational/cross-worker and says to "watch for
  recurrence before extracting it" — one wave is not recurrence, and the wave above was selected
  without needing any such rule.
- **A convergence-mechanics clause in `sequencing.md`, a matching branch-resolution clause in
  `push-readiness.md`, and a combined-verification subsection in `verification.md`.** All three were
  investigated, drafted, reduced, and finally removed across this review — see "Proposed minimum
  skill changes" for the full trace of why.

## Existing rules already sufficient

No change proposed for these, with the evidence for why:

- **`implement-it/rules/review-gates.md`, both approvals.** "No commit is created before Commit plan
  is approved" already carries no exception for how the work was launched or delegated. ST1's gate
  bypass traces to the parent's delegation prompt telling both workers to stop once committed — a
  contradiction between the launch instructions and this already-correct rule, not a gap in the rule
  itself. `vision.md`'s own conclusion: "the gate semantics themselves should not be rewritten merely
  because the experiment failed to honor them." The actual fix for Smoke Test 2 lives in the delegation
  prompt (step 1 of the desired trace above), not in this file.
- **`implement-it/rules/verification.md`'s per-issue full-suite choice.** Unchanged. It already governs
  each worker's own targeted + broader verification correctly and completely; extending it to a
  combined multi-worker decision was investigated and removed (see below) because ownership of that
  later decision is explicitly unresolved research, not because the per-issue rule itself has a gap.
- **`implement-it/rules/push-readiness.md`.** Unchanged. Its branch-identification step already
  resolves to "the milestone's shared branch for milestone work" regardless of how a worker's commits
  got there; a clause naming the temporary-branch detour was drafted and removed because the rule
  doesn't actually need to know about it — it only checks reachability at the point it's invoked, which
  is after convergence in the desired trace.
- **`review-it` end to end** (`SKILL.md`, `rules/scope.md`, `rules/checklist.md`, `rules/verification.md`).
  Already an independently callable, worktree/branch/PR-agnostic reviewer with no session-continuity
  assumption; it establishes its own identity fresh every invocation
  (`rules/verification.md`, "Staleness and review identity"). Nothing about running three of these
  concurrently against three different worktrees requires any change.
- **`implement-it/rules/companion-activation.md`**. Purely per-worker, session-scoped decision-making.
  Unaffected by how many other workers exist.
- **`implement-it/rules/commit-boundaries.md`** and **Commit plan** in `review-gates.md`. Already
  scoped strictly to one worker's own diff; nothing in the desired parallel model asks a worker to
  reason about another worker's commits.
- **`implement-it/rules/issue-closure.md`**. Already requires checking off only genuinely completed
  tasks and validating the checked-task count against GitHub post-mutation
  (`## Closure procedure` step 1, `## Validation`). #354 and #355 closing with every checkbox still
  unmarked is direct evidence this *existing* rule was bypassed by the parent acting outside
  `implement-it`/`ship-it` entirely (`smoke-test-1.md`, "Parent-session post-worker behavior" — "The parent
  did not invoke `ship-it` or the relevant `implement-it` push/issue-closure procedures"), not evidence
  the rule is missing anything.
- **`ship-it/rules/milestone-pr-readiness.md`**. Already re-queries GitHub state fresh rather than
  trusting a specific session's memory ("re-verified against current GitHub state," "Re-query fresh
  against current GitHub state"), and its three conditions (zero open issues, manual testing done,
  manual testing found nothing) are agnostic to how many workers produced the closed issues.
- **`push-readiness.md`'s mechanical trailer re-check and non-force-push discipline**. Already
  independent of how many branches or workers are in play; applies identically per push.

## Proposed minimum skill changes

Two files.

### 1. `implement-it/rules/sequencing.md` — temporary branch, milestone branch as convergence target

- **Current behavior**: "All issues in that milestone share one working branch — implementation does
  not get a fresh branch per issue," with no exception.
- **Evidence**: Git cannot check the same branch out for two concurrent worktrees. `smoke-test-1.md`,
  "Parent-session branch behavior," shows the parent improvising a topic-branch-then-merge pattern
  specifically because this rule, taken literally, made real parallel worktrees impossible.
- **Smallest change**: state that a human-authorized concurrent wave uses a temporary issue branch per
  worker instead of the shared branch directly, and that the milestone branch remains the *eventual*
  convergence target — and stop there. Do not specify who performs convergence, when, or how conflicts
  are handled.
- **Why here, not an orchestrator**: this is the minimum fact needed for the branch-readiness decision
  this rule already owns to remain coherent once more than one worker exists — not a new
  responsibility. What's deliberately *not* added (merge mechanics, timing, conflict policy) is exactly
  the part that would have made this a coordination rule instead of a structural fact.
- **Portability**: fully portable — "temporary branch, then eventually converge" names no runtime.

### 2. `implement-it/rules/worktree-preservation.md` — vocabulary disambiguation

- **Current behavior**: "worktree" means the single active checkout's working tree/index throughout
  this file (and `rules/verification.md`, and `review-it`'s rules).
- **Evidence**: the brief's own flagged prior audit finding, confirmed by grep — every existing use of
  "worktree" across `implement-it`/`review-it` means the single-checkout sense; `vision.md`/`smoke-test-1.md`
  use "worktree" for Claude Code's isolated `git worktree` checkouts. Both meanings now coexist in the
  same skill family once change 1 lands.
- **Smallest change**: one clarifying sentence at the top of this file naming both senses explicitly.
- **Why here, not an orchestrator**: pure terminology hygiene inside a file that already owns this
  vocabulary; no behavior changes.
- **Portability**: fully portable.

### Review history (why five files became two)

This patch went through three passes:

1. **Draft (five files).** `review-gates.md` gained a delegation-is-never-approval clause;
   `sequencing.md` gained both a concurrent-safe-evidence reporting rule and a full convergence
   procedure (merge timing, no-wait-for-wave, conflict-is-a-stop); `push-readiness.md` gained a
   matching branch-resolution clause; `verification.md` gained a combined-verification subsection
   that synthesized all workers' evidence into one decision; `worktree-preservation.md` gained the
   vocabulary note.
2. **First reduction (four files, trimmed).** `review-gates.md` was challenged directly against
   `vision.md`'s own "don't rewrite gate semantics" conclusion and removed. `sequencing.md`'s
   concurrent-safe-evidence half was removed as premature per `orchestration.md`'s "watch for
   recurrence" stance. The convergence procedure was trimmed to cut the no-wait-for-wave and
   conflict-is-a-stop clauses, both of which pre-answered questions the research docs explicitly asked
   Smoke Test 2 to observe instead. `verification.md`'s subsection was trimmed to a single sentence
   tying convergence to the existing "relevant environment changed" trigger.
3. **Final reduction (two files).** Re-examined against "does this make `implement-it` responsible for
   coordinating a fleet of workers": the trimmed `sequencing.md` convergence procedure still specified
   *who* merges and *when* relative to push-readiness — removed entirely, leaving only the structural
   fact that temporary branches exist and the milestone branch is the eventual target.
   `push-readiness.md`'s clause depended on that removed procedure and was checked against the desired
   execution order — push-readiness only runs after convergence has already happened, by whatever means,
   so its existing unmodified text already resolves correctly; removed. The trimmed
   `verification.md` sentence was checked against the actual desired experiment ("one combined decision
   after convergence," not per-worker re-asks) and found to work against that goal — applied once per
   converging worker, it produces repeated re-asks instead of one combined decision. Since ownership of
   combined verification is explicitly unresolved in the research docs, removed entirely rather than
   codifying a guess.

What's left is the minimum required for Smoke Test 2 to be *runnable*: workers need branches that
don't collide. Everything about what happens after that — who converges, when, how combined
verification is decided, how a conflict is handled — is left to actual behavior, observed and recorded,
not specified in advance.

## Proposed unified diffs

Proposals only. Not applied to any installed file.

```diff
--- a/implement-it/rules/sequencing.md
+++ b/implement-it/rules/sequencing.md
@@
 **Delivery/phase milestone issue.** All issues in that milestone share one working branch —
 implementation does not get a fresh branch per issue.
 
+This is the default, single-worker path. When the human has explicitly authorized running more than
+one dependency-ready issue in this milestone concurrently, see "Parallel workers in a delivery/phase
+milestone" below instead — Git cannot check the same branch out for two concurrent workers at once, so
+this default path does not apply to that case.
+
 1. Inspect the currently checked-out branch.
 2. If it already is that milestone's working branch, proceed directly to implementation.
 3. If not, recommend a branch name derived from the milestone's actual nature and scope, and ask the
    human before creating or switching to it. Do not silently create or check out a branch.
 4. Only once the correct branch is confirmed active does implementation begin — the rest of the
    working lifecycle (`rules/review-gates.md` onward) is unchanged.
 
+### Parallel workers in a delivery/phase milestone
+
+Once the human has explicitly authorized concurrent execution of more than one dependency-ready issue
+in this milestone, each worker gets its own temporary issue branch, cut from the confirmed milestone
+branch, instead of implementing directly on the shared branch. The milestone branch remains the
+eventual convergence target for every worker's approved commits.
+
+This rule does not define how or when that convergence happens. That is an open question pending
+evidence from real parallel execution, not a decision this rule makes on its own.
+
 Do not turn observed branch-name patterns into a rigid taxonomy. A name derived from what the
 milestone actually is — its area, or the kind of change it bundles — is the goal; illustrative shapes
```

```diff
--- a/implement-it/rules/worktree-preservation.md
+++ b/implement-it/rules/worktree-preservation.md
@@
 # Worktree Preservation
 
+> "Worktree" throughout this file means the single active checkout's working tree and index — the
+> uncommitted, staged, and stashed content an ordinary `git status` describes — never an isolated
+> `git worktree` checkout used to run a separate concurrent worker. `rules/sequencing.md`'s parallel-
+> worker branch model uses the latter sense; this file's procedure operates entirely within one
+> worker's own single checkout and never touches another worker's.
+
 Any procedure in this skill that needs to temporarily clear the working tree or index around content
```

## Native runtime behavior we rely on

Unchanged from `vision.md`'s list, re-confirmed against the installed skills — none of these are
proposed as methodology:

- parallel background agents;
- isolated worktrees (the Claude Code sense) and per-worker branch checkout;
- independent worker contexts;
- live worker progress and roster;
- switching into a specific worker's session;
- worker completion handback and task notifications;
- preservation of an interrupted worker's worktree and branch;
- enough runtime identity for the parent session to inspect and, if needed, restart work in a preserved
  workspace.

## Orchestration watch items — DO NOT IMPLEMENT

Carried forward from `orchestration.md`, re-checked against this wave and the final two-file patch —
none earn a skill change yet:

- **WATCH ITEM — DO NOT IMPLEMENT: who performs convergence, and when.** Deliberately left out of
  `sequencing.md`'s final proposal. Whether the parent session merges each worker's branch as soon as
  it's approved, or waits for the whole wave, is exactly what Smoke Test 2 should surface.
- **WATCH ITEM — DO NOT IMPLEMENT: combined-verification evidence synthesis and the combined full-suite
  decision.** Removed from `verification.md` entirely in the final pass. `orchestration.md` says
  plainly not to assign this ownership prematurely; observe whether the parent session does it
  correctly with no rule at all before deciding it needs one.
- **WATCH ITEM — DO NOT IMPLEMENT: explicit decision-routing machinery** (human answer → the correct
  waiting worker). Zero direct evidence either way; may turn out to be trivial given how the runtime
  already supports addressing a specific worker session. Observe directly in Smoke Test 2.
- **WATCH ITEM — DO NOT IMPLEMENT: gate-specific worker resumption after interruption.** ST1 only
  demonstrated workspace/branch preservation before any gate was reached — not resumption from a
  paused Review implementation or Commit plan. Do not assume the two are equivalent.
- **WATCH ITEM — DO NOT IMPLEMENT: merge-conflict resolution policy during convergence.** #341/#342/#343
  are expected to be file-disjoint. No rule states what happens on a conflict, deliberately — observe
  what the parent session does if one occurs before writing anything.
- **WATCH ITEM — DO NOT IMPLEMENT: a scheduler for the concurrent-safe subset.** No skill computes or
  authorizes which ready issues run together; picking and launching a wave stays a human decision every
  time, informed by ordinary investigation, not a rule-driven process.
- **WATCH ITEM — DO NOT IMPLEMENT: any orchestrator, Control Room skill/agent, custom worker-agent
  definition, Herdr dependency, formal worker-event protocol, or runtime adapter.** No evidence from
  either ST1 or this dry run crosses the extraction bar `orchestration.md` sets (inherently
  cross-worker, survives the skill corrections above, recurs across waves, awkward to place in a
  worker skill, statable independently of Claude Code).

## Unknowns deliberately left for the smoke test

What Smoke Test 2 will leave entirely to parent-session behavior, to be observed and recorded rather
than assumed:

- **Who performs convergence and when.** No rule assigns this. Watch whether the parent session merges
  each worker's temporary branch as soon as it's individually approved, or waits for the wave, and
  whether that choice causes any problem.
- **Whether combined verification is decided at all, and how.** With no rule requiring it, observe
  whether the parent session naturally restates each worker's already-completed evidence and asks one
  combined run/skip question the way `vision.md`'s diagram describes — or whether this step gets
  skipped, duplicated per-worker, or improvised differently than ST1's pattern.
- **Whether `push-readiness.md` and `issue-closure.md`, run completely unmodified after convergence,
  actually work without incident** — confirming or refuting the assumption that no clause was needed
  there.
- **Merge-conflict handling during convergence**, if #341/#342/#343 turn out not to be as disjoint in
  practice as the file-level analysis above suggests.
- **Whether human decision routing to the correct waiting worker is actually difficult, or trivial**
  once the runtime lets the human address a specific session directly.
- **Whether a worker resumed from a Review implementation or Commit plan stop correctly re-validates
  its approval** per `review-gates.md`'s existing "Approval validity" section, or needs something more.
- **Whether leaving convergence and combined verification completely unowned reproduces ST1's ad hoc
  parent improvisation cleanly and consistently, or produces a different, worse, or inconsistent
  pattern** — the actual evidence needed to decide whether either eventually needs a codified rule.
- **Whether repeated waves make any of the above recur often enough to justify eventually codifying
  it** — one wave remains evidence, not a rule, no matter how it goes.

## Exact Smoke Test 2 success criteria

Two groups: what the reduced patch should guarantee mechanically, and what is now explicitly an
observation target with no rule behind it.

**Guaranteed by the surviving rules (already-correct behavior, or the one structural carve-out):**

- Each worker's own worktree checks out its own temporary issue branch, not the shared milestone
  branch directly — the one thing `sequencing.md`'s change actually makes possible.
- Every worker (#341, #342, #343) invokes `review-it` before its Review implementation report — no
  worker skips it the way the Travel worker did.
- Every worker surfaces a complete Review implementation report and genuinely stops, and a complete
  Commit plan and genuinely stops before creating any commit — both already required by the existing,
  unmodified `review-gates.md`.
- No worker creates a commit without an explicit, immediately preceding human approval of that exact
  Commit plan.
- The human can approve one worker's Review implementation while the other two remain in their own,
  different states (e.g. #A waiting at Commit plan, #B still implementing, #C waiting at Review
  implementation) — and only the approved worker resumes.
- `push-readiness.md`'s mechanical trailer re-check and reachability check both run, unmodified, before
  each issue is asked about for closure.
- Each of #341/#342/#343 closes with its actual completed task checkboxes checked, verified by
  `issue-closure.md`'s existing re-fetch-and-validate step — not left unchecked the way #354/#355 were.
- `sequencing.md`'s recompute runs and correctly reports what remains open (#334, #344, #345, and
  anything newly unblocked) after all three closures.
- None of the above required a new orchestrator, Control Room skill/agent, custom worker-agent
  definition, or event protocol to achieve.

**Observation targets (no rule guarantees these — record what actually happens):**

- Whether and how convergence onto the milestone branch actually occurs, and whether it happens
  per-worker or wave-wide.
- Whether a combined-verification decision is presented to the human at all, and if so, whether it's
  one decision citing all three workers' evidence or something else.
- Whether the unmodified push-readiness/issue-closure procedures run cleanly against the
  post-convergence milestone branch with no incident.
- Whether a merge conflict occurs, and if so, what the parent session does about it with no rule to
  follow.

## Recommendation

Apply the two minimal diffs above to `implement-it` — `sequencing.md`'s temporary-branch carve-out and
`worktree-preservation.md`'s vocabulary note. Nothing else in the installed skills changes. Then run
Smoke Test 2 against #341, #342, #343 with a delegation prompt that runs each worker's `implement-it`
to completion, including both approval stops, and does not tell any worker to stop once committed.
Treat everything in "Unknowns" as data to collect, not behavior to assume — in particular, do not have
the parent session privately decide a convergence or combined-verification procedure and then report it
as if a rule required it; report what actually happened, including any improvisation, the same way
`smoke-test-1.md` reported Smoke Test 1's. Update `smoke-test-1.md` (and `vision.md`/`orchestration.md` where
warranted) with what's actually observed before considering any further methodology change, including
anything resembling extraction toward an orchestrator — a second wave is a second data point, not yet
grounds for a rule.
