# Parallel Implementation Smoke Test 2 — Dry Run

Status: Investigation and dry run. Consumer evidence gathered against `elieandraos/useOrbit`,
Phase 26 — Policies HTTP & Frontend milestone. No useOrbit code, issues, or branches were touched to
produce this document, and no installed skill file was modified — every change below is a proposal
only.

This document treats `vision.md`, `evidence.md`, and `orchestration.md` as the current, not-yet-accepted
investigation state, and treats the skills installed in useOrbit's `.agents/skills/` (`implement-it`,
`review-it`, `ship-it`, `plan-it`) as the actual methodology being exercised — not the canonical
GitHub copies.

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
launch it.

## Desired execution trace

Walking the 20 transitions from the brief, with explicit actor ownership. "Worker" means one
background agent instance bound to one issue.

1. **Worker launch** — Parent Claude session selects #341/#342/#343 as the concurrent-safe subset,
   citing the file-disjointness evidence above (proposed `sequencing.md` addition, below). Native
   Claude Code runtime creates three background agents, each in its own isolated worktree, each
   checked out on its own temporary issue branch cut from the milestone branch
   (`feat/policies-http-frontend`) — proposed `sequencing.md` "Parallel workers" addition, below. The
   delegation prompt for each worker instructs it to run `implement-it` to completion **including both
   approval stops** — it does not tell the worker to stop once committed. This is the direct fix for
   `evidence.md`'s root cause.
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
   `Activated skills:` line and `review-it`'s result, and states the exact decision requested. Under
   the proposed `review-gates.md` addition, the worker does this regardless of how its delegation
   prompt was worded — delegation is never itself the approval.
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
13. **Convergence onto the shared milestone branch** — Parent session, per the proposed
    `sequencing.md`/`push-readiness.md` additions: once a worker's commits are approved and pushed to
    its own temporary issue branch, merge that branch into the milestone branch
    (`git merge --no-ff`, the same mechanism the parent improvised in Smoke Test 1). A worker converges
    as soon as *its own* approvals are done — it does not wait for siblings still mid-lifecycle.
14. **Combined verification evidence summary** — Parent session, per the proposed `verification.md`
    addition: restates each already-converged worker's targeted + broader results; does not re-derive
    them.
15. **Full-suite/skip decision** — Human, presented with that summary, answering the same
    human-controlled choice `verification.md` already owns — applied once, to the combined post-
    convergence branch state, instead of separately per worker.
16. **Combined verification** — Parent session runs the chosen full/skip check against the milestone
    branch post-convergence, using useOrbit's actual full-regression command
    (`php artisan test --compact --no-tia`) — project-specific, not portable methodology.
17. **Push readiness** — `push-readiness.md`, unchanged procedure, now checking reachability of the
    converged commits on the milestone branch itself (fed by step 13's output, per the proposed
    addition to step 1's branch identification).
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
| 3 | Concurrent-safe candidate evidence (file/surface overlap) | B | `sequencing.md` gains a small reporting addition; human still decides |
| 4 | Selecting *which* ready issues to run concurrently | D→(human) | The evidence is a skill responsibility now; the actual go/no-go decision stays the human's, as it already is for ordinary sequencing choices |
| 5 | One shared working branch per milestone (current rule) | B | Needs the temporary-issue-branch/convergence correction for the parallel case only; single-worker default unchanged |
| 6 | Isolated worktree/temporary branch creation mechanics | C | Native `Agent(isolation:"worktree")`-equivalent; not encoded into methodology |
| 7 | Worker cannot treat delegation as gate approval | B | One-paragraph correction to `review-gates.md`; directly fixes ST1's root cause |
| 8 | `review-it` working against a single worker's worktree | A | Already scope-agnostic; no change |
| 9 | Human switching into a specific worker session | C | Already demonstrated, ST1 |
| 10 | Resuming exactly the approved worker without affecting siblings | E | Not yet exercised — no worker in ST1 ever reached a gate |
| 11 | Decision routing (human answer → correct worker) as explicit machinery | E | Zero direct evidence either way; `orchestration.md` already flags this as the most orchestrator-shaped, least-evidenced hypothesis |
| 12 | Per-worker targeted + broader verification | A | Already correctly specified and already observed working in ST1 |
| 13 | Per-worker `review-it` before Review implementation | A | Already correctly specified; ST1's Travel worker skipping it was a bypass, not a gap |
| 14 | Convergence of approved worker branches onto the milestone branch | B | Needs a small, explicit rule; currently only the parent's ad hoc `git merge --no-ff` |
| 15 | Convergence waiting for the whole wave vs. per-worker | B (resolved as: per-worker, no wait) | Small enough to state directly; not a scheduler |
| 16 | Combined-state verification evidence summary + full/skip decision | B | Extends `verification.md`'s existing per-issue full-suite choice; does not belong to `ship-it` (too early — pre-push, pre-PR-readiness) |
| 17 | Push-readiness reachability check | A | Already correct; only needs to know convergence happened first (small addition to step 1's branch identification) |
| 18 | Issue closure, including task-checkbox validation | A | Already required; ST1's unchecked boxes were a bypass of an existing rule, not a missing one |
| 19 | Milestone PR readiness / release | A/C | Re-queries fresh GitHub state; not session-bound; nothing here assumes one worker |
| 20 | Merge-conflict handling during convergence | E | Not observed (#354/#355 were non-overlapping); mark as a stop-for-human default, not a resolution policy |
| 21 | Worker interruption/recovery mechanics | C (mechanics) + A (approval-validity check) | `review-gates.md`'s existing "Approval validity" section already covers re-confirming an approval before relying on it again; recovery itself is runtime |
| 22 | "Worktree" vocabulary meaning two different things across the skill family | B | One clarifying sentence, not a behavior change |

## Current installed-skill gaps

Concretely, three real gaps exist in the installed skills for the parallel case, plus one
terminology risk:

1. **`implement-it/rules/sequencing.md`, "Delivery/phase milestone issue"** (the section stating "All
   issues in that milestone share one working branch — implementation does not get a fresh branch per
   issue") has no provision for more than one worker implementing different issues in the same
   milestone at once. Git cannot check the same branch out in two worktrees simultaneously, so this
   rule, taken literally, makes concurrent workers in one milestone impossible without parent
   improvisation — which is exactly what happened in ST1 (`evidence.md`, "Parent-session branch
   behavior").
2. **`implement-it/rules/review-gates.md`** correctly defines both approvals but never states that a
   background/delegated execution context's *instructions* cannot themselves satisfy either approval.
   `evidence.md` traces both workers' gate bypass to a delegation prompt that told them to stop once
   committed — a contradiction the skill has no explicit language to resist.
3. **`implement-it/rules/verification.md`** defines the full-suite choice at a single issue's boundary
   only. It has no notion of a combined branch state produced by more than one worker's converged
   commits, so nothing currently tells the human that a combined decision exists to make, separate from
   each worker's own already-answered choice — the gap `evidence.md`'s "Verification inconsistency"
   section observed directly (Life skipped the full suite; Travel ran it; nobody reconciled the two).
4. **Terminology risk, not a behavior gap**: `implement-it/rules/worktree-preservation.md`,
   `rules/verification.md`, and `review-it`'s rules all use "worktree" to mean the single active
   checkout's working tree/index (uncommitted content, `git status --porcelain`). The parallel-worker
   design in `vision.md`/`evidence.md` uses "worktree" for Claude Code's isolated `git worktree`
   checkouts. Both senses now live in the same skill family. This was flagged in the prior audit
   referenced by the brief; it remains unresolved in the installed files.

`implement-it/rules/push-readiness.md` and `rules/issue-closure.md` are correct as written but assume
`rules/sequencing.md`'s branch selection resolves to one branch already reachable — once (2) is
corrected, `push-readiness.md`'s step 1 needs one clause acknowledging that a parallel worker's commits
reach the milestone branch via convergence, not directly.

## Existing rules already sufficient

No change proposed for these, with the evidence for why:

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
  `implement-it`/`ship-it` entirely (`evidence.md`, "Parent-session post-worker behavior" — "The parent
  did not invoke `ship-it` or the relevant `implement-it` push/issue-closure procedures"), not evidence
  the rule is missing anything.
- **`ship-it/rules/milestone-pr-readiness.md`**. Already re-queries GitHub state fresh rather than
  trusting a specific session's memory ("re-verified against current GitHub state," "Re-query fresh
  against current GitHub state"), and its three conditions (zero open issues, manual testing done,
  manual testing found nothing) are agnostic to how many workers produced the closed issues.
- **`push-readiness.md`'s mechanical trailer re-check and non-force-push discipline**. Already
  independent of how many branches or workers are in play; applies identically per push.

## Proposed minimum skill changes

Five files. Each change is stated with: exact rule, current behavior, evidence of insufficiency, the
smallest correction, why it belongs in that skill (not a future orchestrator), and portability.

### 1. `implement-it/rules/review-gates.md` — delegation is never approval

- **Current behavior**: defines both approvals correctly but says nothing about what a
  background/delegated worker's own launch instructions can or cannot satisfy.
- **Evidence**: `evidence.md`, "Delegation instructions" and "Human gates were bypassed" — both #354
  and #355 proceeded straight to commit because their delegation prompt made committing the framed
  terminal action.
- **Smallest change**: one paragraph stating that delegation, launch instructions, or an instruction to
  "finish" never substitute for the human's actual approval at either stop.
- **Why here, not an orchestrator**: this is a worker-owned obligation about how the worker itself
  behaves at a gate it already owns — not a cross-worker coordination question.
- **Portability**: fully portable; names no runtime.

### 2. `implement-it/rules/sequencing.md` — concurrent-safe evidence + parallel branch model

- **Current behavior**: recommends exactly one next issue, or presents genuinely comparable ready
  issues as options — never states whether two ready issues could safely run at once. Separately,
  assumes one shared working branch for an entire milestone with no provision for more than one worker.
- **Evidence**: `orchestration.md`, "Concurrent-safe issue selection" ("current skills can determine
  readiness and recommend one next issue, but do not define selection of a concurrent-safe subset");
  `evidence.md`, "Parent-session branch behavior" (the parent improvised topic branches + `git merge
  --no-ff` because the shared-branch rule made real parallel worktrees impossible).
- **Smallest change**: (a) when reporting the ready set, additionally state each candidate's expected
  file/surface overlap with the others, as evidence only; (b) when the human has explicitly authorized
  concurrent execution of a milestone wave, each worker gets a temporary issue branch off the milestone
  branch instead of the branch directly, converging back onto it once approved.
- **Why here, not an orchestrator**: both are extensions of a decision this rule already makes
  (readiness evidence, branch selection) for the single-worker case; no new cross-worker judgment is
  introduced beyond what a human already has to decide for ordinary sequencing.
- **Portability**: (a) fully portable — file-overlap reasoning names no runtime. (b) portable as
  stated — "temporary branch, then converge" — deliberately avoids naming Claude Code's
  `Agent(isolation:"worktree")` API.

### 3. `implement-it/rules/push-readiness.md` — branch identification for a converged worker

- **Current behavior**: step 1 resolves "the correct remote branch" from `sequencing.md`'s branch
  selection, assuming that selection already names the one branch the worker committed on.
- **Evidence**: direct consequence of change 2(b) — once a worker's own commits live on a temporary
  branch, "the correct remote branch" for push-readiness purposes is the milestone branch only *after*
  convergence, not the temporary branch itself.
- **Smallest change**: one added clause in step 1 naming the post-convergence milestone branch as the
  target for a parallel worker, per `sequencing.md`'s new subsection.
- **Why here, not an orchestrator**: this file already owns "identify the correct remote branch" for
  every other case (Backlog/hotfix, milestone, delivery correction); adding the parallel case is the
  same responsibility, not a new one.
- **Portability**: fully portable.

### 4. `implement-it/rules/verification.md` — combined verification after convergence

- **Current behavior**: the full-suite choice is defined once, at a single issue's boundary.
- **Evidence**: `evidence.md`, "Verification inconsistency" — Life and Travel made different,
  unreconciled full-suite decisions, and the combined branch was never re-verified after both merged.
- **Smallest change**: a short subsection stating that when more than one worker's approved commits
  converge in one wave, the existing full-suite choice applies once to the combined state, citing each
  worker's already-completed verification as evidence rather than re-deriving it.
- **Why here, not `ship-it`**: this decision happens before push-readiness and issue closure — the same
  lifecycle position the existing per-issue full-suite choice already occupies — not at
  `ship-it`'s milestone-PR-readiness gate, which is about the whole milestone's aggregate state, much
  later and much broader.
- **Portability**: fully portable; the actual command (`php artisan test --compact --no-tia`) stays
  project-specific, unchanged from the existing rule's own treatment of that distinction.

### 5. `implement-it/rules/worktree-preservation.md` — vocabulary disambiguation

- **Current behavior**: "worktree" means the single active checkout's working tree/index throughout
  this file (and `rules/verification.md`, and `review-it`'s rules).
- **Evidence**: the brief's own flagged prior audit finding, confirmed by grep — every existing use of
  "worktree" across `implement-it`/`review-it` means the single-checkout sense; `vision.md`/`evidence.md`
  use "worktree" for Claude Code's isolated `git worktree` checkouts. Both meanings now coexist in the
  same skill family once change 2 lands.
- **Smallest change**: one clarifying sentence at the top of this file naming both senses explicitly.
- **Why here, not an orchestrator**: pure terminology hygiene inside a file that already owns this
  vocabulary; no behavior changes.
- **Portability**: fully portable.

### Self-review (Part 6 challenge)

Applying the review pass the brief asked for, before finalizing:

- **Did I put cross-worker orchestration into `implement-it` unnecessarily?** No — convergence and the
  combined-verification decision are stated as small extensions of rules `implement-it` already owns
  (branch selection, the full-suite choice), not as new coordination logic. Decision routing itself —
  the genuinely orchestrator-shaped candidate — is deliberately left unspecified (see "Unknowns,"
  below).
- **Did I encode Claude Code-specific runtime behavior into portable methodology?** No — "temporary
  branch, then converge" is stated without naming `Agent(isolation:"worktree")`, background-agent
  launch syntax, or task-notification mechanics.
- **Did I duplicate a rule another skill already owns?** No — the combined-verification addition was
  checked against `ship-it/rules/milestone-pr-readiness.md` specifically and placed earlier in the
  lifecycle deliberately, to avoid overlapping that later, broader gate.
- **Did I change something Smoke Test 1 merely bypassed rather than exposed as missing?** Checked
  directly against issue-closure and push-readiness — both already correct, both left unchanged.
- **Did I prematurely answer something Smoke Test 2 should observe?** Decision routing, gate-specific
  resumption, and conflict handling were all considered for a rule and rejected in favor of "Unknowns"
  below, per `orchestration.md`'s own conservative stance on exactly these three.
- **Could any hunk be deleted while still letting Smoke Test 2 run correctly?** Change 5 (vocabulary)
  is the one genuinely optional hunk — Smoke Test 2 would still run without it. Kept anyway because
  change 2 introduces the collision risk directly, and the cost of the one-sentence fix is lower than
  the cost of a future skill correction conflating the two senses. Everything else is load-bearing: 1
  is the direct fix for the observed root cause; 2 is required for parallel worktrees to be possible at
  all under this milestone model; 3 is a direct, mechanical consequence of 2; 4 is required to avoid
  repeating the unreconciled-verification failure.

Ideas considered and cut entirely (not included above):

- A new `rules/convergence.md` file — cut; folded into `sequencing.md`/`push-readiness.md` instead,
  per the brief's "do not create a new lifecycle stage."
- An explicit worker decision-routing protocol — cut; zero supporting evidence, `orchestration.md`
  already flags it as unobserved, left as a watch item.
- Mandating a full suite always after convergence — cut; would remove the human's existing skip option
  and isn't supported by evidence that convergence changes the risk calculus by itself.
- Changing Commit plan to require multi-worker awareness — cut; no evidence a worker's Commit plan ever
  needs to reason about another worker's diff.

## Proposed unified diffs

Proposals only. Not applied to any installed file.

```diff
--- a/implement-it/rules/review-gates.md
+++ b/implement-it/rules/review-gates.md
@@
 `rules/push-readiness.md`'s push-authorization request — asking whether to push already-approved
 commits to the correct remote branch, before `rules/issue-closure.md` asks whether to close the
 issue — is a similar separate boundary, not a third review gate. It approves nothing about the
 implementation or the commit structure; Review implementation and Commit plan remain the only two
 approvals of either.
 
+## Delegation is never approval
+
+Neither approval below is satisfied by how this work was assigned, launched, or delegated — including
+a background or otherwise delegated execution context whose own instructions describe committing, or
+finishing, as the expected outcome. Being told to implement an issue, including under time pressure or
+with an instruction to stop once done, never by itself authorizes proceeding past either approval stop.
+A worker operating under such instructions still owns reaching Review implementation and Commit plan,
+reporting the complete decision this file defines at each, and waiting for that exact human decision
+before proceeding — identically to any other execution of this skill, regardless of what launched it.
+
 ## Review implementation — first approval (Gate 1)
```

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
+in this milestone (see "Concurrent-safe candidate evidence" below for what supports that decision),
+each worker gets its own temporary issue branch, cut from the confirmed milestone branch, instead of
+implementing directly on the shared branch. The milestone branch remains what `rules/push-readiness.md`
+and `rules/issue-closure.md` ultimately require a worker's commits to be reachable on — not the
+temporary branch.
+
+Once a worker's commits are verified and both approvals (`rules/review-gates.md`) are complete, merge
+that worker's temporary branch into the milestone branch (`git merge --no-ff`) before treating its
+commits as reachable for push-readiness purposes. A worker converges as soon as its own commits are
+approved — it does not wait for other workers in the same wave. A merge conflict during convergence is
+a stop for human resolution, not something to resolve automatically.
+
 Do not turn observed branch-name patterns into a rigid taxonomy. A name derived from what the
 milestone actually is — its area, or the kind of change it bundles — is the goal; illustrative shapes
@@
 ## Report the graph, recommend, let the human choose
 
 Summarize compactly, in categories — never a flat ready list:
 
 - which issues just became newly ready because of this closure;
 - which were already ready;
 - which are still blocked, and on what.
 
 For example: issue {A} closes, issues {B} and {C} become ready, and issue {D} remains blocked on
 {E}.
 
 Recommend one ready issue, with a concise rationale, when the evidence gives a reasonable basis —
 e.g. it unblocks the most follow-on work, or it continues the same implementation layer/context the
 recent work was in. When several ready issues are genuinely comparable and the choice is a real
 judgment call, present them as options instead of silently picking one — this is a sequencing
 choice, and `rules/review-gates.md`'s "multiple valid sequencing choices" stop applies here
 directly.
 
 Recommendation is not authorization: investigate enough to recommend when possible, but never
 convert a genuine sequencing judgment into an automatic choice. The human always makes the final
 sequencing decision.
 
+### Concurrent-safe candidate evidence
+
+When more than one issue is ready at once, additionally state what's known about each candidate's
+expected implementation surface — files, routes, models — the same investigation already used to
+recommend a next issue. Disjoint expected surfaces are supporting evidence that running them
+concurrently is likely safe; overlapping or unclear surfaces are evidence against it, or reason to say
+the overlap is uncertain rather than silently assuming either answer. This is evidence for the human's
+decision whether to run issues concurrently — never itself a scheduling decision, the same discipline
+this rule already applies to recommending a single next issue.
+
 ## When the ready set is empty
```

```diff
--- a/implement-it/rules/push-readiness.md
+++ b/implement-it/rules/push-readiness.md
@@
 1. **Identify the correct remote branch.** For ordinary issue implementation,
    `rules/sequencing.md`'s "Branch readiness" already selected it — the repository's trunk branch for
    Backlog/hotfix work, or the milestone's shared branch for milestone work; this step reads that
    selection, it does not re-derive or override it. For an authorized delivery correction, the branch
    is the milestone's already-open PR branch the correction is being applied against.
+   For a worker executing under `rules/sequencing.md`'s "Parallel workers in a delivery/phase
+   milestone," the target is the milestone's shared branch once that worker's temporary issue branch
+   has converged onto it — reachability is checked against the milestone branch, never the temporary
+   branch the worker's own commits were made on.
 2. **Check whether the commits are already there.**
```

```diff
--- a/implement-it/rules/verification.md
+++ b/implement-it/rules/verification.md
@@
 If the human originally chose to skip the full suite, the completed issue can be reported with that skip
 unless a later decision, project rule, or risk escalation requires broader regression evidence. Never
 silently convert a skip into a run.
 
+## Combined verification after parallel convergence
+
+When more than one worker's approved commits converge onto the same milestone branch in one wave
+(`rules/sequencing.md`'s "Parallel workers in a delivery/phase milestone"), this file's full-suite
+choice applies once, to the combined branch state, rather than separately to each worker's own change.
+Summarize each already-converged worker's targeted and broader verification results as evidence — do
+not re-derive them — then ask the human the same run-or-skip question this file already asks at a
+single issue's boundary, now against the branch as it stands after convergence. Run the choice using
+the project's genuine full-regression mode, the same as any other full-suite run this file governs. A
+worker whose commits have not yet converged is not part of this combined state and is not covered by
+this decision.
+
 ## Cache, replay, and impact-analysis results are not fresh-execution proof
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

Carried forward from `orchestration.md`, re-checked against this wave — none earn a skill change yet:

- **WATCH ITEM — DO NOT IMPLEMENT: explicit decision-routing machinery** (human answer → the correct
  waiting worker). Zero direct evidence either way; may turn out to be trivial given how the runtime
  already supports addressing a specific worker session. Observe directly in Smoke Test 2.
- **WATCH ITEM — DO NOT IMPLEMENT: gate-specific worker resumption after interruption.** ST1 only
  demonstrated workspace/branch preservation before any gate was reached — not resumption from a
  paused Review implementation or Commit plan. Do not assume the two are equivalent.
- **WATCH ITEM — DO NOT IMPLEMENT: merge-conflict resolution policy during convergence.** #341/#342/#343
  are expected to be file-disjoint; if Smoke Test 2 nonetheless produces a conflict, treat it as a stop
  for human resolution (already implied by the proposed `sequencing.md` addition) and observe what
  actually happens before writing a resolution procedure.
- **WATCH ITEM — DO NOT IMPLEMENT: a scheduler for the concurrent-safe subset.** The proposed change
  only requires *reporting* file/surface-overlap evidence; picking and launching a wave stays a human
  decision every time, with no automatic threshold.
- **WATCH ITEM — DO NOT IMPLEMENT: any orchestrator, Control Room skill/agent, custom worker-agent
  definition, Herdr dependency, formal worker-event protocol, or runtime adapter.** No evidence from
  either ST1 or this dry run crosses the extraction bar `orchestration.md` sets (inherently
  cross-worker, survives the skill corrections above, recurs across waves, awkward to place in a
  worker skill, statable independently of Claude Code).

## Unknowns deliberately left for the smoke test

- Whether human decision routing to the correct waiting worker is actually difficult, or trivial once
  the runtime lets the human address a specific session directly.
- Whether a worker resumed from a Review implementation or Commit plan stop correctly re-validates its
  approval per `review-gates.md`'s "Approval validity" section, or needs something more.
- What convergence actually looks like when two workers *do* share a file — not exercised by
  #341/#342/#343's disjoint surfaces; a future wave with real overlap is needed to observe this.
- Whether three concurrent workers behave qualitatively differently from ST1's two — e.g. whether
  decision routing gets harder, or convergence ordering matters, once there are three temporary
  branches instead of one.
- Whether the proposed "concurrent-safe candidate evidence" reporting is actually useful to the human's
  decision in practice, or too thin/too noisy at this size.
- Whether combined verification's placement in `verification.md` (rather than `ship-it`) holds up once
  observed against a real combined-state failure, not just a clean pass.
- Whether repeated waves make any of the "Unknowns" above recur often enough to justify eventually
  extracting them — one wave remains evidence, not a rule.

## Exact Smoke Test 2 success criteria

Mapped directly to `evidence.md`'s "Not preserved or not validated" table — every line below is
expected to flip from ✗ to ✓ if the proposed changes hold:

- Every worker (#341, #342, #343) invokes `review-it` before its Review implementation report — no
  worker skips it the way the Travel worker did.
- Every worker surfaces a complete Review implementation report (activated skills, verification
  results, `review-it`'s result, the exact decision requested) and genuinely stops — observed as an
  actual pause, not inferred from the transcript.
- Every worker surfaces a complete Commit plan and genuinely stops before creating any commit.
- The human can approve one worker's Review implementation while the other two remain in their own,
  different states (e.g. #A waiting at Commit plan, #B still implementing, #C waiting at Review
  implementation) — and only the approved worker resumes.
- No worker creates a commit without an explicit, immediately preceding human approval of that exact
  Commit plan.
- A worker's approved commits converge onto the milestone branch without waiting for sibling workers
  still mid-lifecycle.
- After convergence, the human is shown a combined-verification evidence summary and asked a single
  run/skip decision against the combined state — not left to notice on their own that the workers made
  different individual choices.
- `push-readiness.md`'s mechanical trailer re-check and reachability check both run against the
  milestone branch post-convergence, for each issue, before that issue is asked about for closure.
- Each of #341/#342/#343 closes with its actual completed task checkboxes checked, verified by
  `issue-closure.md`'s existing re-fetch-and-validate step — not left unchecked the way #354/#355 were.
- `sequencing.md`'s recompute runs and correctly reports what remains open (#334, #344, #345, and
  anything newly unblocked) after all three closures.
- None of the above required a new orchestrator, Control Room skill/agent, custom worker-agent
  definition, or event protocol to achieve.

## Recommendation

Apply the five minimal diffs above to the installed `implement-it` skill only — no other skill needs a
change for this wave. Then run Smoke Test 2 against #341, #342, #343 with a corrected delegation prompt
that removes the "stop once committed" instruction ST1 used. Watch the five watch items and the seven
unknowns directly rather than pre-deciding them. Update `evidence.md` (and `vision.md`/`orchestration.md`
where warranted) with what's actually observed before considering any further methodology change,
including anything resembling extraction toward an orchestrator — one more wave is evidence, not yet a
second data point toward that decision.
