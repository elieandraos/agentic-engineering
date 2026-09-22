# Parallel Implementation Smoke Test 3 — Evidence

Status: Evidence from useOrbit #334/#344/#345. This document reconstructs Smoke Test 3 from direct
evidence: the parent session's own conversation record (`SubagentHandback` reports, task notifications,
`SendMessage` results, `AskUserQuestion` answers, received in real time), direct `git`/`gh` inspection of
`elieandraos/useOrbit` performed both during and after the run, selective `grep`/targeted-offset reads of
the three workers' raw JSONL transcripts (never dumped wholesale), and the pre-registered dry run for this
exact wave (`parallel-dry-run-2.md`). Where something is inferred rather than directly observed, it is
labeled `Inference:` explicitly. Quoted worker text is copied verbatim from the parent session's own
conversation record (each worker's `SubagentHandback`), not reconstructed from memory.

## Experiment

Repository: `elieandraos/useOrbit`. Milestone: "Phase 26 — Policies HTTP & Frontend" (milestone #27).
Milestone branch: `feat/policies-http-frontend`, confirmed at `e118e5b` at launch (`git status`/`git log`
before any worker started). This was the milestone's entire remaining open set — `parallel-dry-run-2.md`
confirmed, before the run, that #334/#344/#345 were the *only* three open issues left.

Issues, all pre-verified dependency-ready:

- #334 — Add Policies link to top nav (depends on #322, closed)
- #344 — Implement Policies index filters drawer (depends on #335, #332, both closed)
- #345 — Policies show page — Members tab (depends on #336, closed)

**Starting-state verification.** Before launching any worker, the parent ran `git status --porcelain=v1`
and confirmed the only pre-existing dirty files were the expected local Agentic Engineering candidate-skill
edits: `.agents/skills/implement-it/rules/{review-gates,sequencing,verification,worktree-preservation}.md`
and `skills-lock.json` — all uncommitted, all pre-existing before this session began. These are exactly
`parallel-dry-run-2.md`'s proposed two-file patch (`verification.md`, `review-gates.md`) layered on top of
Smoke Test 2's already-installed two-file patch (`sequencing.md`, `worktree-preservation.md`) — confirmed
directly by diffing the working-tree copies against `git show HEAD:<path>` for each file: every diff hunk
matches `parallel-dry-run-2.md`'s "Proposed unified diffs" section byte-for-byte, and `sequencing.md`'s
diff matches `parallel-dry-run.md`'s (Smoke Test 2's dry run) diff. The parent never modified these files;
it treated them as pre-existing state to preserve, per the user's explicit instruction, and excluded them
from every application commit made during the run.

**File-disjointness analysis**, redone directly by the parent before launch (not merely trusting
`parallel-dry-run-2.md`'s prediction): `find resources/js -iname "*FiltersDrawer*" -o -iname
"*PolicyMedicalDetailShell*" -o -iname "navItems.ts"` confirmed the three issues' expected surfaces
(`resources/js/components/shell/navItems.ts`; four existing `*/partials/FiltersDrawer.vue` siblings with
no `Policies` one yet; `resources/js/pages/PolicyMedical/partials/PolicyMedicalDetailShell.vue`) were
distinct files with no overlap — matching `parallel-dry-run-2.md`'s own pre-run finding of "zero file
overlap among the three."

**The premature convergence question, and the human's deferral.** Before launching any worker, the parent
asked (via `AskUserQuestion`) how the three branches should converge into `feat/policies-http-frontend`
once approved: merge each as soon as approved, or hold all three and merge together later. The human's
actual answer: *"This decision is not needed yet. Start the three authorized workers and let each follow
the installed methodology until it reaches its candidate-ready waiting state. Do not decide permanent
branch convergence yet. Surface that decision when approved durable worker commits actually exist and
convergence is required."* The parent deferred the question and launched the workers. This is a genuine,
explicit human decision made during ST3, not existing methodology — `sequencing.md`'s "Parallel workers"
section already states convergence mechanics are undefined by design; what the human added here is *when*
that undefined-ness should be raised at all (not before launch), which the installed rule text does not
itself say.

**Worker launch.** Three `Agent` calls, `isolation: "worktree"`, sent in one message (parallel). Each
worker received a self-contained prompt (fresh agents carry no shared context) naming its issue's full
body/tasks, the milestone branch, the dependency-closure evidence, an instruction to invoke `implement-it`
via the `Skill` tool and follow `.agents/skills/implement-it/rules/*.md` as binding methodology (not a
research document), an instruction to cut its own branch per `sequencing.md`'s parallel-worker section
(naming convention modeled on the actual prior branches, e.g. `issue-341-...`), and an explicit instruction
not to merge, push, or close its own issue, and to hold at whatever gate the skill reaches pending the
still-deferred convergence decision. Resulting identities:

| Issue | Agent ID | Branch | Worktree |
|---|---|---|---|
| #334 Nav link | `a707d74ada1a37c2c` | `issue-334-policies-nav-link` | `.claude/worktrees/agent-a707d74ada1a37c2c` |
| #344 Filters drawer | `a03d6eb6a63be057c` | `issue-344-policies-filters-drawer` | `.claude/worktrees/agent-a03d6eb6a63be057c` |
| #345 Members tab | `ace396347fa58c93d` | `issue-345-policies-members-tab` | `.claude/worktrees/agent-ace396347fa58c93d` |

All three transcripts' first line timestamp is `2026-09-22T06:30:06.3xxZ` (within 9 milliseconds of each
other) — direct confirmation of genuine concurrent launch, not sequential dispatch. Final timestamps:
`07:18:30` (#334), `07:19:07` (#344), `07:18:41` (#345) — roughly 48–49 minutes of wall-clock time spanning
implementation through final commit, across all three workers plus every parent round-trip.

## Timeline

Chronological reconstruction of the run's major beats (full worker-internal detail is in the
per-worker sections below; this section is the cross-wave sequence):

1. Starting-state verification, file-disjointness check, dependency confirmation (all closed).
2. Premature convergence question asked → human deferral ("not needed yet, launch first").
3. Three workers launched in one message, each on its own temporary branch.
4. Worker bootstrap: all three independently ran `composer install`/`npm install` (or `npm ci`) and
   `php artisan wayfinder:generate` in their fresh worktrees (see "Worker bootstrap cost").
5. Implementation proceeded independently and asynchronously; #334 (a one-line nav change) finished its
   implementation and verification pass fastest, exactly as `parallel-dry-run-2.md` predicted it would
   ("#334 will very likely reach 'ready' materially before #344 or #345").
6. Each worker ran targeted verification, then `review-it`, then attempted to report its stopping point.
   **#334 correctly held itself at "ready for combined verification," citing the wave's parallel-worker
   rule and explicitly declining to present Review implementation.** **#344 and #345 both instead
   presented themselves at Review implementation (Gate 1) and asked the parent to make the per-worker
   full-suite run/skip call** — the exact per-worker choice the installed candidate patch removes for a
   concurrent worker. The parent caught this in both cases and sent each a correction (see "Parent
   supervision" and each worker's section below); both re-checked, agreed, and re-reported themselves
   holding at the same "ready for combined verification" point #334 had already reached.
7. Once all three held at that same point, the parent reported a compact wave-ready summary to the human
   (implementation + verification + `review-it` substance for each, not a bare "clean") and asked how the
   wave's combined full-suite verification should be run.
8. **Combined-verification decision.** The parent presented this as a run/skip choice — "Assemble the
   three diffs together, run full suite" vs. "Skip full suite, rely on each worker's targeted results" —
   and the human chose the former. See "Verification-policy decision" below for why this framing itself
   is evidence worth treating carefully: the pre-registered research position (`responsibility-boundaries.md`)
   had called combined verification "a required step... not a run/skip decision," and the parent's own
   live framing reintroduced a skip option that text had explicitly ruled out.
9. **Temporary combined-candidate assembly**, performed by the parent itself (not a fresh agent, not one
   of the ready workers) directly in the main checkout. See "Combined candidate" below for the exact
   mechanism, which diverged from the validated `combined-candidate.md`/`parallel-dry-run-2.md` procedure
   in specific, identified ways.
10. **Combined verification**, run once against the assembled worktree: full Pest suite fresh/uncached,
    frontend build, `vue-tsc`, ESLint, Prettier, Pint, route table — all confirmed passing. See "Combined
    verification" below for exact reproduction of each figure from the parent's own tool output, not
    merely restated from memory.
11. **Disposal** of the temporary integration worktree and its scratch branch (`git worktree remove
    --force`, `git branch -D`), confirmed complete.
12. The parent relayed the combined-verification result to all three workers and told them they could now
    present Review implementation citing it in place of a per-worker full-suite result.
13. **Formal Review implementation reports**, one per worker, arriving asynchronously in the order #345 →
    #334 → #344. The parent relayed each to the human as it arrived, rather than batching them — see
    "Commit-plan UX" and "Decision-oriented presentation" for why this repetition is itself a finding.
14. **Human implementation approvals**: "Approve all three, proceed to Commit plan" — one message,
    covering all three workers at once.
15. **Commit plans**, one per worker, again arriving asynchronously (#334 → #345 → #344) and relayed
    individually as they arrived.
16. **Human Commit-plan approvals**: "Approve all three, create the commits" — again one message covering
    all three.
17. **Semantic commit creation**: `bbca52b` (#334); `3978d7c` + `a854314` (#344); `aed09ce` (#345). Each
    worker ran its own mechanical trailer check (`git interpret-trailers --parse`) per commit and reported
    a clean result (no output, exit 1) before reporting completion.
18. **Convergence decision**, now genuinely relevant (durable commits exist): the human chose "merge
    sequentially now, one at a time" — matching ST2's validated pattern in *policy*, but see "Convergence
    behavior" for who actually performed it, which diverged from ST2.
19. **Sequential convergence**, performed directly by the parent in the main checkout (not by resuming the
    original workers, as ST2 validated): `git merge --no-ff issue-334-policies-nav-link`, then
    `issue-344-policies-filters-drawer`, then `issue-345-policies-members-tab`, in that order, each a
    clean, conflict-free `ort`-strategy merge — confirmed by `git log --oneline -8` immediately after.
20. **Push authorization**: "Push all three and close the issues" (one combined human instruction covering
    both push and closure). The parent pushed `feat/policies-http-frontend` directly (`git push origin
    feat/policies-http-frontend`, plain fast-forward, `e118e5b..50c6c83`, not rejected).
21. **Issue closure**, performed directly by the parent via `gh issue close -c "<message>"` for each of the
    three issues — **not** via each issue's own `issue-closure.md` "verify and check off completed Tasks"
    step. See "Push and issue closure" below: this is a confirmed, direct regression, not an inference.
22. **Milestone ready-set recomputation**: `gh issue list --milestone 27 --state open` → empty (zero open
    issues), confirmed fresh against live GitHub state, not inferred from the closures alone.
23. **Handoff to milestone PR readiness**: the parent explicitly declined to decide next steps itself and
    named `ship-it`'s milestone-PR-readiness gate as the correct next stop.
24. On a later human request, the parent invoked `ship-it`, ran the three-condition PR-readiness gate
    (zero open issues re-verified fresh; the human's direct confirmation that final manual testing had
    happened and found nothing further), discovered the project's PR-title/base-branch/milestone-field
    convention from real prior merged PRs (not assumed), drafted a complete PR proposal, and — after
    explicit human approval, including a follow-up clarification on the attribution footer — created and
    re-fetched PR #357 (`main` ← `feat/policies-http-frontend`, milestone field set), confirming its actual
    number/base/head/title/milestone matched the approved proposal exactly.
25. **This audit**, run afterward, with the milestone PR left open and unmerged throughout, per the
    human's explicit instruction not to merge it as part of this audit.

## Worker #334

**Branch/worktree.** `issue-334-policies-nav-link`, cut from `feat/policies-http-frontend` at `e118e5b`,
in worktree `.claude/worktrees/agent-a707d74ada1a37c2c`.

**Skills activated, and when.** Directly confirmed from the transcript: the `Skill("implement-it")` call
is the transcript's first tool call (line 13); its own `wayfinder-development` and `laravel-inertia-stack`
companion activations happened next, both *before* any implementation edit. The worker's own report
states `tailwindcss-development` (no styling touched) and `laravel-best-practices`/`testing-best-practices`
(no backend/PHP surface, and — per direct precedent on this exact file — no test surface) were considered
and explicitly not activated, with a reason given for each, rather than silently skipped.

**Implementation scope.** One file: `resources/js/components/shell/navItems.ts` — added a `Policies` nav
entry (Shield icon from `@lucide/vue`, via generated `@/routes/policies`), positioned after Agents,
mirroring the two prior nav-link precedent commits on this exact file (`a4195fa`, `0c61a9f`) in import
shape and array-literal structure.

**Targeted verification.** `npx vue-tsc --noEmit`, `npx eslint`, `npx prettier --check`, `npm run build` —
all clean. No test added, matching both direct precedents on this file (neither added one either).

**Did it incorrectly attempt a per-worker full-suite decision?** No. Its own report stated explicitly:
*"Per this concurrent-wave's rules, this is not yet a Review implementation (Gate 1) stop. As a worker in
the human-authorized parallel wave... full-suite regression evidence for Gate 1 is the wave's combined
candidate state, not a per-worker choice — so I'm holding here rather than presenting Review
implementation."* This is the correct behavior on the first attempt — see "Candidate-ready boundary" and
"Parent supervision" for why this worker, uniquely among the three, got this right immediately.

**`review-it` result.** Clean. No findings — requirements compliance, correctness, architectural fit,
maintainability, and accidental-scope-expansion all checked with nothing to report; security/data-integrity
categories not applicable to a static array addition.

**Candidate-ready state.** Reached correctly, on the first pass, with no parent correction needed.

**Remained uncommitted until approval?** Yes — confirmed by the worker's own repeated statements ("no
commits have been created yet") and by the parent's own `git status` checks at each stage.

**Combined-verification evidence received.** The parent relayed the full combined result (1287/1287 fresh
Pest run, clean build/typecheck/lint/format/pint, 47 routes with no collisions) once it existed.

**Human Review-implementation approval.** Received as part of the single combined human message "Approve
all three, proceed to Commit plan."

**Semantic Commit plan.** One commit, the entire diff — "there's no independent sub-decision to split
out." No tests, matching precedent. Draft message: `Add Policies link to top nav` / `Refs #334`. No Git
trailers — the worker explicitly cited this project's `commit-boundaries.md` trailer policy as the reason,
stating it applies "regardless of any other instruction in scope" (i.e., regardless of this session's own
default attribution reminder).

**Human approval.** Received as part of the combined "Approve all three, create the commits" message.

**Durable commit.** `bbca52b`, one file, 3 insertions/1 deletion. Mechanical trailer check
(`git log -1 --format=%B | git interpret-trailers --parse | grep -q .`) reported no output/exit 1 — clean,
confirmed by the worker itself, not merely asserted.

**Convergence.** Performed by the parent (see "Convergence behavior"), not by this worker itself —
`git merge --no-ff issue-334-policies-nav-link -m "Merge issue-334-policies-nav-link into
feat/policies-http-frontend"` → `288693f`, clean, `ort` strategy, one file changed.

**Push.** Part of the parent's single `git push origin feat/policies-http-frontend` covering all three
merges at once — landed as `e118e5b..50c6c83`, not rejected.

**Issue closure.** Closed directly by the parent (`gh issue close 334 -c "Closed by commit bbca52b (merged
via 288693f into feat/policies-http-frontend, pushed to origin)."`), confirmed live: `state: CLOSED`,
`closedAt: 2026-09-22T07:21:45Z`.

**Task-checkbox validation.** **Not performed.** Directly confirmed by re-fetching the issue body after
closure: its one task line still reads `- [ ] Add a \`Policies\` entry to \`navItems\`...` — unchecked.
See "Push and issue closure" for why this is a confirmed regression, not an inference.

**Terminal handback.** The worker itself never performed convergence, push, or closure — those three steps
were executed directly by the parent, a genuine divergence from how #334's own final handback describes
its own state (it last reported having created its commit and awaiting further instruction).

## Worker #344

**Branch/worktree.** `issue-344-policies-filters-drawer`, cut from `e118e5b`, in worktree
`.claude/worktrees/agent-a03d6eb6a63be057c`. This worktree had no `vendor`/`node_modules`/`.env`/built
assets at all on start — the worker set up `.env`, sqlite, migrations, `composer install`, `npm install`,
`wayfinder:generate`, and `npm run build` before it could run anything (see "Worker bootstrap cost").

**Skills activated, and when — the self-disclosed process gap, reconstructed precisely.** Directly
confirmed from the transcript's own line numbers: the transcript's first `Skill` calls (lines 13, 21) are
both `implement-it` (request + result pair); the worker then proceeded directly to implementation edits
(first `Edit`/`Write` calls to `FiltersDrawer.vue`/`PoliciesController.php`/`Index.vue` at lines 256, 264,
272). Only *after* those edits did it invoke `review-it` for the first time (line 380), and only *after*
that first `review-it` pass did it activate all seven remaining companion skills in sequence
(`inertia-vue-development`, `tailwindcss-development`, `laravel-best-practices`, `testing-best-practices`,
`laravel-inertia-stack`, `my-phpstorm-conventions`, `wayfinder-development`, lines 432–459) — followed by a
*second* `review-it` invocation (line 505). This exactly matches, and refines with hard evidence, the
worker's own self-disclosure: *"the last 5 [companions] were activated retroactively, after the code was
already written, not before — I had followed sibling-file conventions directly instead of invoking the
skill mechanism first, which is exactly the failure mode `companion-activation.md` describes."* The precise
correction to that self-report: it activated companions retroactively not just relative to implementation,
but relative to its *own first `review-it` pass* as well — the retroactive companion check is what
surfaced the fix described below, which then triggered a second `review-it` pass, not a re-run of the
first.

**Implementation scope.** New `resources/js/pages/Policies/partials/FiltersDrawer.vue` (search, status,
type, class multi-select via the codebase's existing "multiple checkboxes" idiom — no shared multi-select
chip component existed to reuse), wiring into `resources/js/pages/Policies/Index.vue` (Filters button +
active-count badge), a `filtered` empty-state variant in `resources/js/pages/Policies/partials/
EmptyState.vue`, and backend prop exposure in `app/Http/Controllers/Policies/PoliciesController.php`
(`statuses`/`types`/`classes`/`sources`/`carriers` option lists plus a `filters` prop mirroring
`IndexPolicyRequest`'s validated params — `IndexPolicyRequest`/`PolicyFilter` from #335/#332 untouched).
4 new tests in `tests/Feature/Http/Policies/IndexTest.php`.

**Focused verification.** `php artisan test --compact tests/Feature/Http/Policies/` → 228/228 passed, 1177
assertions (full Policies-HTTP directory, not just the new tests, specifically to catch a regression in
the shared controller). `vue-tsc`, ESLint, Prettier (2 auto-fixed nits), Pint — all clean.

**Did it incorrectly attempt a per-worker full-suite decision?** **Yes, confirmed directly.** Its first
attempt at a stopping report asked the parent: *"Decision needed from you next: Per `verification.md`,
before `review-it` can be invoked and Gate 1 reported, you need to make the full-suite run/skip decision
for this issue"* — offering "Run full suite" vs. "Skip full suite" as the choice. This is precisely the
per-worker full-suite choice the installed candidate patch (verification.md's "Concurrent workers in a
parallel wave" section) removes. The parent's correction message pointed the worker back to that section
and declined to answer the question, since it wasn't the parent's call either at that point. **The worker's
own explanation for the mistake, given after correction**, attributes it to reading `verification.md` from
a location that lacked the candidate-patch text — see "Candidate-ready boundary" below for the precise,
directly-confirmed root cause, which both narrows and partially corrects that self-explanation.

**`review-it` result.** Clean on both passes. First pass: clean, one non-blocking scope note (the
`EmptyState.vue` `filtered`-state addition goes beyond the issue's literal two checklist items, but is
low-risk and mirrors the established Carriers/Agents `EmptyState.vue` convention) and one informational,
UI-unreachable note about a validation-error key (`class.0` vs `class`) that the drawer's own UI can never
actually trigger. The retroactive `testing-best-practices` check (performed *after* the first `review-it`
pass, per the ordering established above) surfaced a real, independent finding: 4 new option-list
assertions compared against `count(PolicyStatus::cases())` etc. — a near-tautological check, since any
1:1 `array_map` transformation satisfies a bare count regardless of correctness. **Fixed**: replaced with
literal integers (3/2/6/4), independently verified against the actual enum source
(`grep -c "case " app/Enums/*.php`), re-ran the test file (22/22 passed) and Pint (clean). The scoped
re-review (second `review-it` pass) confirmed this fix clean with no new issue introduced.

**Candidate-ready state.** Reached, correctly, after the parent's correction — the worker's own
re-statement: *"Not making the full-suite run/skip call and not presenting Review implementation — per the
corrected rules, that's decided once for the wave's combined candidate state, not per worker."* Wait — this
quoted sentence is #345's; #344's own equivalent re-statement was: *"Holding here, exactly as instructed —
not presenting Gate 1 ('Review implementation'), not making any full-suite call. Ready for combined
verification whenever the wave-level decision is made."*

**Remained uncommitted throughout that hold.** Yes, confirmed by the worker's own repeated statement and
by `git status --short` returning empty only after the eventual approved commits, not before.

**Combined-verification evidence received.** Full combined result relayed by the parent, cited explicitly
in the worker's Review-implementation report in place of a per-worker full-suite result.

**Human Review-implementation approval.** Part of the combined "Approve all three, proceed to Commit plan"
message.

**Semantic Commit plan.** Two commits, in dependency order: (1) `PoliciesController.php` +
`IndexTest.php` — the backend prop exposure and its proving tests, coherent standalone since
`Policies/Index.vue` doesn't yet reference the new props at this intermediate point, and the full Policies
HTTP suite passes on this state alone; (2) new `FiltersDrawer.vue` + `Index.vue` + `EmptyState.vue` — the
frontend half, depending on (1)'s exposed props, intentionally test-free (no Vue test framework exists in
this project, matching every sibling `FiltersDrawer.vue`). Messages: `Expose Policies filter options and
current filters to the index page` / `Refs #344`, then `Add a filters drawer to the Policies index page` /
`Refs #344`. No trailers, same cited policy as #334.

**Human approval.** Part of the combined "Approve all three, create the commits" message.

**Durable commits.** `3978d7c` (2 files, 99 insertions) then `a854314` (3 files, 398/12). Both individually
trailer-checked clean by the worker (`no output, exit 1` on each, run separately — "not concatenated").
Working tree confirmed clean (`git status --short` empty) after both.

**Convergence.** Performed by the parent, not this worker — `git merge --no-ff
issue-344-policies-filters-drawer` → `be990c0`, clean, 5 files, one new file created.

**Push.** Part of the parent's single combined push, `e118e5b..50c6c83`.

**Issue closure.** Closed directly by the parent (`gh issue close 344 -c "Closed by commits 3978d7c and
a854314 (merged via be990c0 into feat/policies-http-frontend, pushed to origin)."`); confirmed live:
`CLOSED`, `closedAt: 2026-09-22T07:21:47Z`.

**Task-checkbox validation.** **Not performed** — directly confirmed: both of #344's two task lines remain
`- [ ]` in the closed issue's body. Same regression as #334; see "Push and issue closure."

## Worker #345

**Branch/worktree.** `issue-345-policies-members-tab`, cut from `e118e5b`, in worktree
`.claude/worktrees/agent-ace396347fa58c93d`.

**Skills activated, and when.** Directly confirmed: all of `implement-it` plus its seven companions
(`inertia-vue-development`, `tailwindcss-development`, `laravel-inertia-stack`, `laravel-best-practices`,
`testing-best-practices`, `my-phpstorm-conventions`, `wayfinder-development`) were activated at transcript
lines 13–85 — every one of them *before* the first implementation edit (first `Edit`/`Write` to
`PolicyMembersController`/`PolicyMembers`/`PolicyMedicalDetailShell` at line 203). This worker did **not**
exhibit #344's retroactive-activation pattern; its only post-implementation `Skill` call (line 360) is
`review-it`, in the correct position.

**Implementation scope.** Computed `age` field on `app/Http/Resources/PolicyInsuredResource.php`; new
`app/Http/Controllers/Policies/PolicyMembersController.php` (`#[Authorize('view', 'policy')]`, guarded on
Medical class and Group type, 404 otherwise); new `routes/members.php` + `routes/web.php` wiring →
`policies.members.index`; new `resources/js/pages/PolicyMembers/Index.vue` (relationship filter chips,
search, read-only roster table — no add/edit/remove control); wired the pre-existing placeholder Members
tab in `PolicyMedicalDetailShell.vue` to the real route (its `type === 'group'` gating was already present,
unchanged); `age: number` added to the `PolicyInsured` TS interface; 7 new tests in
`tests/Feature/Http/Policies/MembersIndexTest.php`.

**Focused verification.** `MembersIndexTest.php` re-run 8× consecutively (to rule out flakiness after the
fix below) — stable 7/7 every time. Broader: `tests/Feature/Http/Policies/` + `PolicyInsuredTest.php` →
236/236 passing. `Pint --dirty`, `vue-tsc`, ESLint, Prettier — clean; `npm run build` succeeds;
`php artisan route:list --path=policies` confirmed `policies.members.index` registers with no collision.

**Did it incorrectly attempt the wrong verification/Review-implementation path?** **Yes, confirmed
directly and in the same shape as #344.** Its first stopping report presented itself explicitly as
"Status: stopped at 'Review implementation' (Gate 1) — needs your decision," reporting a completed Gate-1
package and asking: *"this is a milestone/parallel-wave issue with strong targeted coverage already... I'd
lean toward skipping the true full `php artisan test --compact --no-tia` run for this issue... but this is
your call, not mine to decide silently. Run it now, or skip for this issue?"* alongside a request to
approve Review implementation directly. The parent's correction pointed it at the same
`verification.md`/`review-gates.md` sections cited to #344 and declined to answer either question. The
worker's own explanation after correcting, quoted directly: *"I re-checked `verification.md` in this
worktree (both `~/.claude/skills/implement-it` and the project's `.agents/skills/implement-it` copy are
identical and currently lack the [Concurrent workers] section you referenced), but that's consistent with
the pending uncommitted edits to exactly those 4 rule files that this session's initial git status showed
on the shared checkout — my isolated worktree, cut from a committed point, wouldn't see those uncommitted
edits."* This self-diagnosis is directly confirmed as accurate by this audit's own inspection — see
"Candidate-ready boundary" below.

**`review-it` result.** Clean after one fix. Finding: the `'authenticated user gets 404 for a non-medical
policy'` test built its policy with the base `Policy::factory()`, which selects `class` at random across
all six policy classes — on the roughly 1-in-6 draw where it randomly picked Medical, both controller
guards would pass and the endpoint would return 200 instead of the expected 404, a flaky test. The sibling
`MedicalShowTest`'s equivalent test avoids exactly this with an explicit `->automotive()` factory state.
**Fixed** by switching to `->automotive()`; re-ran the file 8× consecutively afterward — stable every time.
One non-blocking scope note: the controller authorizes via `#[Authorize('view', 'policy')]` rather than the
child-policy `viewAny` form `PolicyDocumentsController`/`PolicyNotesController` use for their own
child-listing endpoints — reasoned as functionally equivalent, since `PolicyInsured` has no independent
authorization semantics and no dedicated policy class exists; confirmed non-blocking by the cross-org-404
test already passing under either form.

**Candidate-ready state.** Reached after the parent's correction: *"Not making the full-suite run/skip call
and not presenting Review implementation — per the corrected rules, that's decided once for the wave's
combined candidate state, not per worker. This sits at the same stopping point as #334 and #344."*

**Remained uncommitted throughout.** Yes, confirmed by the worker's own statement and by `git status`.

**Combined-verification evidence received.** Relayed by the parent; cited in place of a per-worker
full-suite result.

**Human Review-implementation approval.** Part of the combined "Approve all three, proceed to Commit plan"
message.

**Semantic Commit plan.** One commit, all 8 files (4 modified, 4 new) — every changed file serves one
implementation decision (exposing the Medical roster as a read-only tab); the backend endpoint has no
consumer without the Vue page and vice versa, so splitting would leave a non-functional intermediate
state — explicitly citing this milestone's own precedent (the single-commit Agent Policies-tab wiring,
`038f0ab`). Message: `Wire the Medical policy show page's Members tab to a real roster endpoint` / body /
`Refs #345`. No trailers, same cited policy.

**Human approval.** Part of the combined "Approve all three, create the commits" message.

**Durable commit.** `aed09ce`, 8 files, 419 insertions/1 deletion. Trailer-checked clean (no output,
exit 1). `git status --short` confirmed exactly the 8 planned files staged, nothing stray.

**Convergence.** Performed by the parent, not this worker — `git merge --no-ff
issue-345-policies-members-tab` → `50c6c83`, clean, 8 files, 4 new files created.

**Push.** Part of the parent's single combined push.

**Issue closure.** Closed directly by the parent (`gh issue close 345 -c "Closed by commit aed09ce (merged
via 50c6c83 into feat/policies-http-frontend, pushed to origin)."`); confirmed live: `CLOSED`,
`closedAt: 2026-09-22T07:21:50Z`.

**Task-checkbox validation.** **Not performed** — both of #345's task lines remain `- [ ]`, directly
confirmed by re-fetching the closed issue's body. Same regression as #334/#344.

## What differed between #334 and #344/#345 — the precise root cause

The audit's own instruction was not to assume rule ambiguity without evidence. Direct transcript inspection
answers this precisely, and the answer is **not** ambiguous rule text:

**All three workers' `Skill("implement-it")` call reported the identical base directory:**
`/Users/elieandraos/.claude/skills/implement-it` — confirmed by grepping each transcript's first
`Skill`-tool result for `"Base directory for this skill"`. This path is a symlink
(`~/.claude/skills/implement-it -> ../../.agents/skills/implement-it`, resolved relative to `~/.claude/
skills/`, i.e. `~/.agents/skills/implement-it` — a *separate, global, user-home-level* installation of this
skill, physically distinct from the project's own `/Users/elieandraos/Desktop/Code/useOrbit/.agents/
skills/implement-it`). Direct diff confirms this global copy is byte-for-byte identical to useOrbit's last
**committed** `verification.md`/`review-gates.md` — it entirely lacks the ST2+ST3 candidate patch, which
exists *only* as an uncommitted change in the main useOrbit checkout's own working directory.

**Every worker operates inside its own isolated `git worktree`**, a separate checkout of the same repo.
Git worktree isolation means an uncommitted change sitting in the *main* checkout's working directory is
categorically invisible to any other worktree — including one reading the *same relative path*
(`.agents/skills/implement-it/rules/verification.md`) from inside its own, separately-checked-out copy.
This is true regardless of whether a worker reaches that path via the global symlink mirror or via the
project-local path *as it exists inside its own worktree* — both resolve to the last-**committed**,
unpatched content.

**The one path that *does* see the candidate patch: an absolute reference into the main checkout itself.**
Directly confirmed: worker #334's two `Read` calls (transcript lines 101, 103) used the literal absolute
path `/Users/elieandraos/Desktop/Code/useOrbit/.agents/skills/implement-it/rules/{verification,
review-gates}.md` — the **main checkout's own path**, not a path under its own worktree
(`.../​.claude/worktrees/agent-a707d74ada1a37c2c/...`) and not the global mirror. Reading that path returns
whatever bytes are physically on disk in the main checkout at that moment — including the uncommitted
candidate patch sitting there throughout the entire run. #334 happened to read the rule files this way
(most plausibly because the parent's own launch prompt to it named the path
`.agents/skills/implement-it/rules/*.md` without qualifying it as worktree-relative, and #334's own
subsequent `Read` calls used that literal string against the filesystem root, landing on the main
checkout). #344 and #345, when they later wanted to double-check a specific rule file mid-task, instead
followed the *Skill tool's own reported base directory* (transcript lines 330/360 for #344; 354/356 for
#345) — the global, permanently-stale mirror — and only later, after the parent's correction, re-read from
the correct project-scoped offset (`.agents/skills/implement-it/rules/verification.md`, offset 50/limit 75;
`review-gates.md`, offset 27/limit 45 — #345, transcript lines 455/461) to actually see the patch text the
parent's correction message quoted to them.

**Conclusion, stated precisely:** this is not evidence that `verification.md`/`review-gates.md`'s prose is
ambiguous — both files' installed candidate text is unambiguous once read. It is evidence that **an
uncommitted candidate patch living only in a main checkout's working directory is not reliably visible to
concurrently-launched isolated workers at all**, and that whether a given worker happens to see it depends
on an accident of which absolute path it reads a rule file from, not on anything the methodology or the
worker's own judgment controls. #334's correctness was not evidence of superior rule-following; it was
evidence of an accidental main-checkout read. #344/#345's mistake was not evidence of rule ambiguity or of
worse worker judgment; it was the structurally expected outcome for any worker that (reasonably) trusted
the `Skill` tool's own reported location or its own worktree's project-local copy. **This is a runtime/
process-execution finding about candidate-patch propagation into isolated worktrees, not a skill-wording
gap** — see "Skill findings" for why no proposed rule-text change addresses it.

## Candidate-ready boundary

The target lifecycle (parallel worker → implementation → targeted verification → meaningful broader
verification → `review-it` → candidate-ready → NO per-worker full-suite decision → NO Review
implementation approval yet → NO Commit plan → NO durable commit → wait) **eventually held for all three
workers**, but only two of three (#334) reached it without an external correction; #344 and #345 both
initially attempted a per-worker full-suite decision and a premature Review-implementation presentation,
and both required the parent's explicit intervention (quoting the installed rule text back to them) before
correcting.

**Was the installed skill wording sufficient by itself, or was parent supervision necessary?** On this
run's evidence: **parent supervision was necessary**, but not because the wording itself was insufficient
— per "What differed" above, two of three workers were structurally unable to see the correct wording at
the moment they needed it, for reasons outside the wording's own control (candidate-patch propagation into
isolated worktrees). The wording that eventually resolved both deviations was the parent quoting the exact
installed sentences back to each worker from a source the worker could then read correctly. This is
different from Smoke Test 2's "Skill findings," which found the ordering rule "exists and is unambiguous at
the `SKILL.md` level, but is not restated where a worker actually executes the procedure" — this run's
deviation is not that kind of gap; the rule text a worker eventually reads is fine, but not every worker
reliably reads the *current* version of it in the first place.

## Combined candidate

**Who triggered assembly, and when.** The parent, directly, once all three workers had independently
reported (and, for #344/#345, been corrected into) the same "ready for combined verification" state — not
before, and not partially: assembly began only after all three workers' hold-state reports existed in the
parent's own conversation record.

**Authoritative candidate-ready confirmation.** The parent's own record shows the exact sequence: #334's
initial correct hold arrived first; #344's and #345's *corrected* holds arrived afterward, each following a
parent intervention. Assembly began after the third (corrected) hold, not after the first.

**Which context performed assembly.** The parent session itself, directly in the main checkout — **not** a
fresh short-lived agent and **not** one of the three ready workers. This answers one of
`combined-candidate.md`'s and `parallel-dry-run-2.md`'s explicitly-unresolved questions ("who runs the
capture/assembly/suite-run sequence") with this run's one data point: the parent.

**Base commit/branch.** `git worktree add -b wave-verification/334-344-345 .claude/worktrees/wave-
verification feat/policies-http-frontend` — a fresh worktree cut from the milestone branch's confirmed tip
(`e118e5b`), on a disposable scratch branch.

**Exact worker-diff capture procedure used, and how it diverged from the validated procedure.**
`parallel-dry-run-2.md` experimentally validated a specific three-step capture procedure: `git add -N` on
each worker's untracked paths, `git diff HEAD --binary`, then immediate `git reset` on those same paths to
restore worker state. **The parent did not use this procedure.** It instead ran plain `git -C
<worker-worktree> diff HEAD` for tracked changes (correctly capturing staged+unstaged modifications to
already-tracked files) and separately used `git -C <worker-worktree> ls-files --others --exclude-standard`
plus individual `cp` commands to copy each worker's untracked new files directly into the integration
worktree's filesystem — closer to `combined-candidate.md`'s rejected option #5 (filesystem copy) for the
untracked-file portion specifically, not the validated `--3way`-apply procedure for those files. **This
worked in this run** because none of the three workers' new files collided with each other or with anything
already in the integration worktree (confirmed: `git status --porcelain` in the integration worktree after
all three captures showed exactly the expected 9 modified + 5 new files, matching each worker's own
reported file list with no unexplained entries) — but it reintroduces exactly the silent-overwrite risk
`combined-candidate.md` identified as disqualifying for option #5 in general, and it is a **confirmed
divergence** from the specific mechanism `parallel-dry-run-2.md` pre-registered and experimentally
validated for this exact wave.

**A capture failure occurred and was caught, not silently accepted.** The first attempt at copying #345's
four untracked files failed silently in the tool output (a shell quoting/formatting issue, not a Git
failure) — all four files' destination paths were missing after the first pass. The parent did not trust
the tool's stdout alone; it explicitly verified each destination file's presence and content-equality
against the source worker's copy (`diff -q`), found all four missing, and re-copied each individually with
explicit `mkdir -p` per file before re-verifying. This is a real, confirmed near-miss (a documented capture
procedure was not used, and its filesystem-copy substitute did fail on its first attempt) that the parent's
own follow-up verification caught before it could produce false-negative combined-verification evidence.

**How the tracked-diff portion was applied.** `git -C <integration-worktree> apply <patch-file>` (plain
`git apply`, without `--3way` and without `--index`) — again a divergence from the validated `git apply
--3way --index` recommendation. All three tracked-diff applies succeeded cleanly with no conflict, since
the three workers' tracked-file changes were genuinely disjoint (confirmed by inspecting the resulting
`git status` after each apply) — this run's clean disjointness meant the missing `--3way`/`--index`
refinement was never actually exercised or tested; had a real conflict existed, plain `git apply` would
have failed with a less informative error than `--3way` would have produced, and the changes would not
have been staged (`--index`) the way the validated recommendation intends.

**Whether binary-safe diff handling was used.** Not applicable in this run — none of the three workers'
changes touched a binary file, so the `--binary` flag's absence from the tracked-diff capture (`git diff
HEAD`, not `git diff HEAD --binary`) was never exercised either way.

**Whether any conflicts occurred.** None. Zero merge/apply conflicts across all three tracked-diff applies
and all filesystem copies — consistent with the pre-registered file-disjointness analysis and with
`parallel-dry-run-2.md`'s own note that this wave deliberately did not manufacture a conflict.

**Whether original worker worktrees/indexes remained intact.** Confirmed: `git diff HEAD` is read-only
against a worker's own worktree, and the filesystem `cp` operations only read from worker worktrees, never
wrote to them. No worker's own worktree, branch, or diff was touched by assembly.

**Whether any implementation commit was created as part of assembly.** No. The integration worktree's
content was staged/copied but never committed — confirmed by `git status --porcelain` in the integration
worktree showing modified/untracked entries, never a clean tree with a new commit, at any point before
disposal.

**Whether the temporary workspace was fully disposable, and whether it was removed afterward.** Yes, both.
`git worktree remove --force .claude/worktrees/wave-verification` followed by `git branch -D
wave-verification/334-344-345`, confirmed by the branch-deletion output and by the main checkout's own
`git status` afterward showing only the pre-existing candidate-skill diffs, nothing else.

**Comparison against `docs/research/combined-candidate.md`.** That document's recommended mechanism (#6:
`git worktree add` + `git diff HEAD` (with the `parallel-dry-run-2.md` corrections) + `git apply --3way
--index` + full suite + `git worktree remove`) was **followed in spirit but not in exact mechanics**: the
worktree-creation and disposal steps match exactly; the tracked-file capture/apply matches in category
(`git diff`/`git apply`) but omitted `--3way`, `--index`, and `--binary`; the untracked-file capture used
filesystem copy instead of the validated `add -N`/`diff --binary`/`reset` procedure. **This divergence is
recorded as a finding, not corrected retroactively** — the run's actual result was still correct (no
corruption, no silent loss, confirmed by direct post-capture inspection), but it was correct *this time*
without the safety margin the validated procedure specifically provides against a same-file collision or a
binary file, neither of which this wave's clean disjointness happened to test.

## Combined verification

Exact reproduction of what the parent actually ran, from its own tool-call record, against the assembled
integration worktree (after replacing a first, broken symlink-based `vendor`/`node_modules` setup with real
copies — see below):

- `composer dump-autoload -o` — required because the project's `composer.json` sets
  `"optimize-autoloader": true`; a symlinked `vendor` pointing at the main checkout would have corrupted the
  main checkout's own autoloader with paths rooted in the disposable worktree. The parent caught this
  before running it against the shared vendor, replaced the symlinks with real `cp -Rc` (APFS clone) copies
  of `vendor`/`node_modules`, and regenerated the autoloader inside the now-independent copy — "Generated
  optimized autoload files containing 10980 classes."
- `php artisan route:list --path=policies` — 47 routes registered, including `policies.members.index`, with
  no name/path collision; this failed on the very first attempt (`ReflectionException: Class
  "App\Http\Controllers\Policies\PolicyMembersController" does not exist`) precisely because the stale
  symlinked autoloader hadn't yet been regenerated — a real, caught failure, not a hypothetical one.
- `npm run build` — required before the first full-suite attempt too: the first `php artisan test
  --compact --no-tia` run failed 172 of 1287 tests with `Illuminate\Foundation\ViteManifestNotFoundException:
  Vite manifest not found` — an environmental gap (no built assets in the fresh worktree), not a real
  regression. Building assets first, then re-running, is what produced the clean result below.
- `php artisan test --compact --no-tia` (fresh, uncached — required specifically because this project's
  test-impact-analysis is enabled by default, per this project's own `verification.md` guidance) →
  **1287/1287 passed, 4233 assertions**, confirmed directly from the tool's own JSON summary output, not
  restated from a worker's claim.
- `npx vue-tsc --noEmit` — clean, no output.
- `npx eslint resources/js/` — clean, no output.
- `npx prettier --check resources/js/` — clean ("All matched files use Prettier code style!").
- `vendor/bin/pint --test --format agent` — `{"tool":"pint","result":"passed"}`.

**What exact combined repository state those checks covered.** Confirmed directly by `git status
--porcelain` in the integration worktree immediately before running the suite: all 9 tracked modifications
and all 5 new files from all three workers were present together (verified path-by-path against each
worker's own reported file list, with the corrected #345 re-copy described above). This is the union of all
three candidates, not a subset.

**Was this the first ST1/ST2/ST3 run to genuinely verify the union of all parallel candidates before human
implementation approval?** **Yes.** ST1 never verified the combined branch at all
(`smoke-test-1.md`). ST2 never presented a deliberate combined-verification decision; its closest substitute
(#341's own 446-test run) ran *after* commits already existed and had already been approved
(`smoke-test-2.md`, "Post-convergence verification"; `responsibility-boundaries.md`, "Combined
verification"). ST3 is the first run where a full, fresh, uncached regression suite ran against a
still-**uncommitted** union of every worker's changes, *before* any worker's Review implementation was even
presented — exactly the gap both prior smoke tests left open, and exactly the sequencing
`combined-candidate.md`/`vision.md`'s updated verification model called for.

## Verification-policy decision

This requires the careful, exact treatment the audit asked for, because the pre-registered research
position and what actually happened in this live run are not identical.

**Pre-ST3 research position, verbatim** (`responsibility-boundaries.md`, "Combined verification"):
*"Combined verification... is a required step for the parallel wave, not a run/skip decision — unlike the
existing per-issue full-suite choice `verification.md` already defines for a single (serial) worker."*
`vision.md`'s updated "Verification model" states the same: *"a required full-suite run for the parallel
wave, not a run/skip decision."*

**Installed candidate-patch text, verbatim** (`.agents/skills/implement-it/rules/verification.md`,
"Concurrent workers in a parallel wave," confirmed directly from the file): *"A worker executing as part of
a human-authorized concurrent wave does not make the full-suite choice above. Final regression verification
for its candidate implementation belongs to the wave's combined candidate state — decided and run once, for
the wave, not per worker... This does not change the full-suite choice for a single worker running alone,
and does not specify how, when, or by whom the combined candidate state is assembled, verified, or
evaluated — that stays outside this rule."* This text removes the *per-worker* choice explicitly. It does
**not** itself say the wave-level result is mandatory-required rather than a run/skip choice — it is
silent on that specific question, deliberately leaving it "outside this rule."

**What actually happened in this live run.** The parent, once all three workers held at "ready," presented
the human with an explicit two-option choice via `AskUserQuestion`: *"Assemble the three diffs together,
run full suite (Recommended)"* vs. *"Skip full suite, rely on each worker's targeted results."* The human
chose the first option. **This is a real, observed divergence from the pre-registered "required, not a
run/skip decision" research position** — the parent's own live framing reopened a skip option that
document had explicitly closed, and did so on its own initiative, not because any installed rule text
required presenting it as a choice (the installed text is silent, not permissive of a skip).

**Precise attribution, as the audit asked for.** The audit's own framing described this as "an explicit ST3
methodology decision" the human made, phrased as an abstract principle ("Parallel workers should still
never make individual full-suite decisions. Instead... the human should receive ONE combined full-suite
run/skip decision for the wave."). Checked directly against the actual conversation record: **the human did
not independently author that abstraction during the run.** What is directly observed is narrower: the
parent presented a two-option question (one of which was a skip), and the human selected "run." The
abstract principle is this audit request's own retrospective synthesis of that exchange, not something the
human stated in their own words during ST3 itself. This distinction matters for where responsibility for
the divergence sits: it is **parent-session presentation choice**, ratified by a human answer to the
specific question actually asked — not a considered human amendment to the pre-registered "mandatory"
research position that the parent merely executed.

**Analysis against the installed rule text and single-worker behavior.** `verification.md`'s serial-worker
full-suite choice (unaffected by any of this) is explicitly framed as "a human-controlled choice at the
issue boundary" with a real skip option, recommended-vs-reasonable framing for each side
("Run full suite now. Recommended when..."; "Skip full suite for this issue. Reasonable for a low-risk
issue..."). The parent's live combined-verification question used the *identical* two-option, one-
recommended shape — i.e., it modeled the wave-level decision on the *serial* per-issue pattern
`verification.md` already defines, rather than on `responsibility-boundaries.md`'s stricter
"required" framing. Whether that is the right shape going forward is exactly the kind of judgment call the
installed text's silence leaves open — but it should not be recorded as if the installed candidate text, or
an explicit human-authored principle, already settled it. It did not; the parent's presentation settled it,
this one time, and the human ratified that specific framing by answering within it.

**Minimum methodology correction implied.** `review-gates.md`'s installed addition already correctly
requires combined-suite evidence to exist and be successful before Review implementation, regardless of
whether that evidence comes from a mandatory run or a human-chosen skip. If the wave-level choice is to
remain run/skip (as this run treated it), the smallest correction is to state that explicitly in
`verification.md`'s "Concurrent workers in a parallel wave" section, alongside — not instead of — its
current silence on *who* assembles the candidate; if instead the "required, not skip" research position is
to be preserved, `verification.md` needs a sentence saying so, since its current text is genuinely silent,
not permissive of a skip by design. **This document takes no position on which of the two the methodology
should adopt** — it reports, precisely, that the live run diverged from the pre-registered position, and
why, and leaves the choice to whoever reviews this evidence next. No skill file was edited to reflect
either option as part of this audit.

## Human-facing review UX

**Positive evidence, directly confirmed.** Once combined verification passed, the parent's relayed summary
to the human, per worker, was compact and substantive rather than a bare "clean": for #334, one file
changed, no findings, matches direct precedent; for #344, what changed plus the specific `EmptyState.vue`
scope note and the retroactive-skill-activation self-correction, named plainly; for #345, what changed plus
the flaky-test root cause and fix, plus the authorization-pattern scope note. This matches Smoke Test 2's
own recorded preference (`smoke-test-2.md`; `vision.md`, "Human-facing presentation") for reporting
implementation substance rather than a bare pass/fail, and is recorded here as confirmed positive evidence,
not merely a restated goal.

**The repetition problem, confirmed directly.** After combined verification passed and the parent relayed
that result to all three workers at once, each worker still independently produced and returned its own
full, separately-formatted Review-implementation report (arriving asynchronously: #345 first, then #334,
then #344), and the parent relayed each one to the human as three separate messages rather than batching
them into one checkpoint — even though the underlying implementation content for all three had not changed
since the earlier compact summary. The same pattern repeated at Commit-plan stage: #334's plan arrived
first, then #345's, then #344's, each relayed individually, and the parent explicitly told the human at one
point "You now have two commit plans pending... still waiting on #344's" — asking the human to hold multiple
partially-accumulated decisions in their head across separate messages, exactly the pattern the audit
described as the preferred-behavior violation.

**The preferred interaction, per the audit's own Checkpoint A/B framing, evaluated against what actually
happened.** Checkpoint A (wave-ready: compact summaries + one combined run/skip decision) **did occur**,
correctly, once — the parent's pre-combined-verification summary was exactly this shape. Checkpoint B (after
the decision: report the combined result once, do not repeat full worker detail unless a worker materially
changed, ask which implementations are approved to proceed) **did not occur** — the parent instead let each
worker's own subsequent Review-implementation and Commit-plan report re-arrive and re-relay in full,
asynchronously, three separate times each, rather than collecting them into one follow-up checkpoint before
presenting anything further to the human. **Classification, per the audit's own instruction: this is
human-facing presentation/orchestration evidence, not a worker-skill defect** — each worker's own report was
substantively correct and non-redundant from that worker's own perspective; the redundancy was introduced
entirely by the parent choosing to relay each arrival immediately rather than batching arrivals that
belonged to the same human decision boundary.

**Internal methodology jargon.** Directly confirmed present in several of the parent's relayed messages:
"Gate 1," "Review implementation (Gate 1)," explicit rule-file names (`commit-boundaries.md`'s trailer
policy, `verification.md`'s "Concurrent workers" section) surfaced verbatim in text shown to the human, both
in the parent's own summaries and in directly-quoted worker text the parent chose to relay unedited. This
repeats Smoke Test 2's own recorded finding (`smoke-test-2.md`, "UX/presentation finding";
`responsibility-boundaries.md`, "Human-facing presentation") rather than resolving it — the same gap
recurred a third time, under the same "not a correctness defect" classification: lifecycle mechanics were
correct throughout (both gates held for all three workers, nothing committed early), only the vocabulary
carried unnecessary internal detail into the human-facing text.

## Commit-plan UX

Reconstructed directly from the parent's own message order: worker Commit plans arrived asynchronously —
#334's first, then #345's, then #344's — each relayed to the human as a separate message rather than
accumulated first. The parent's own text at the halfway point ("You now have two commit plans pending
(#334, #345) — still waiting on #344's") is direct, first-party evidence of exactly the "human had to
mentally accumulate them" problem the audit described, not an inference about it.

**Verification of the required `Refs #N` line on every actual commit, checked directly against `git log`,
not assumed:**

- `bbca52b` (#334): `Add Policies link to top nav\n\nRefs #334` — confirmed present.
- `3978d7c` (#344, commit 1): `Expose Policies filter options and current filters to the index page\n\n
  Refs #344` — confirmed present.
- `a854314` (#344, commit 2): `Add a filters drawer to the Policies index page\n\nRefs #344` — confirmed
  present. **Both of #344's commits carry the reference**, directly checked, not merely trusted from the
  worker's own report.
- `aed09ce` (#345): body plus `Refs #345` — confirmed present.

All five commits also independently confirmed trailer-free via each worker's own mechanical
`git interpret-trailers --parse` check, reported per-commit rather than concatenated across a range.

**The preferred presentation structure the audit specified** (issue / commit N · message / what it does /
files / tests / `Refs #N`) was **not** what the parent actually relayed to the human in this run — the
parent's relays were prose summaries of each worker's own free-form Commit-plan report, not a normalized,
per-commit structured block. This is recorded as unresolved, not retrofitted after the fact.

## Decision-oriented presentation

The broader pattern the audit asked to evaluate — workers report asynchronously, the parent accumulates
related state, a shared decision boundary becomes ready, the parent presents one coherent checkpoint, the
human decides once, relevant workers resume — **was validated once** (the pre-combined-verification
wave-ready checkpoint) and **was not repeated** at either the post-combined-verification Review-
implementation stage or the Commit-plan stage, where the parent instead relayed each worker's arrival
individually as it happened. Evidence strength, per stage:

- **Candidate-ready/review summaries:** strong positive evidence — the parent explicitly held #334's and
  #344's completed reports before relaying anything, specifically because "combining with 1 out of 3
  doesn't achieve the purpose," and waited until #345's corrected hold arrived before presenting the
  combined-verification question at all.
- **Combined verification:** the decision itself was batched correctly (one question, covering the whole
  wave); the *result* was relayed to all three workers in one round of messages, but the human never saw a
  single follow-up checkpoint after that — only the three subsequent Review-implementation relays,
  individually.
- **Commit plans:** weakest evidence — no batching at all; three separate relays, with the parent's own
  text acknowledging the accumulation problem live, rather than resolving it before presenting anything.
- **Convergence:** the decision was requested and applied once, uniformly, to all three workers together
  ("Merge sequentially now, one at a time") — correctly batched at the decision level, even though its
  *execution* (see "Convergence behavior") diverged from ST2 in a different way.

**Classification.** This pattern — batch related state into one decision checkpoint rather than relaying
each worker's event as it lands — is evidenced here as a real, recurring need, but the evidence is entirely
about *how the parent chose to present already-correct worker output*, not about anything a worker itself
does wrong. Per the audit's own instruction, this is recorded as an orchestration/Control Room-shaped
candidate responsibility (decision-boundary batching across concurrently-reporting workers), not a
worker-skill correction — no artifact is proposed here.

## Convergence timing

The exact skill gap the audit asked about, reconstructed precisely: `sequencing.md`'s "Parallel workers in
a delivery/phase milestone" section states convergence mechanics are undefined "not a decision this rule
makes on its own," but says nothing about *when* that undefined-ness should be surfaced relative to worker
launch. Absent that, the parent's own first instinct — asked before any worker had even started
implementing — was to ask the human to decide convergence policy immediately, before there was anything to
converge. The human's correction (quoted in full under "Timeline," point 2) supplies exactly the missing
fact: an undefined mechanic is not a prerequisite to authorizing the wave that will eventually need it; it
only needs deciding once real, approved, durable commits exist and require it.

**Whether evidence supports adding this clarification to `sequencing.md`.** Yes, on this run's direct
evidence — the parent asked prematurely once, was corrected once, and the correction generalizes cleanly
("surface the decision when durable approved commits exist and convergence is required," not "resolve
every unspecified mechanic before authorizing the wave that will eventually need it"). This document does
not itself add that sentence to any skill file, per the audit's explicit instruction.

## Convergence behavior

**Commits, verified directly from `git log`:** `bbca52b` (#334); `3978d7c`, `a854314` (#344); `aed09ce`
(#345) — matching each worker's own Commit-plan-derived structure exactly, with no additional or missing
commit.

**Human convergence decision:** "Merge sequentially now, one at a time" — presented and chosen after all
three workers' commits already existed and were approved, matching `sequencing.md`'s own framing of when
this decision becomes relevant.

**Merge order and SHAs, verified directly:** `288693f` (`issue-334-...`), `be990c0` (`issue-344-...`),
`50c6c83` (`issue-345-...`), each a clean, conflict-free `ort`-strategy `--no-ff` merge, confirmed by `git
log --oneline --graph -12 feat/policies-http-frontend`'s actual output matching this exact sequence and by
each merge's own reported file-change summary matching that worker's known diff.

**Conflict behavior.** None — zero conflicts across all three merges, consistent with the pre-launch
file-disjointness analysis.

**Shared milestone branch state afterward:** `feat/policies-http-frontend` at `50c6c83`, 7 commits ahead of
its pre-run tip `e118e5b` (4 merge commits + the three workers' underlying commits collapse to: `bbca52b`,
`3978d7c`, `a854314`, `aed09ce`, `288693f`, `be990c0`, `50c6c83` — matching `git status -sb`'s own "ahead 7"
report at push time).

**Who actually performed convergence — the sharpest divergence from Smoke Test 2 in this entire run.** In
ST2, each *original worker* was resumed by name and performed its own push+merge inside its own worktree
(`smoke-test-2.md`, "Convergence" — confirmed by `SendMessage` targets matching the original agent IDs). In
**ST3, the parent performed every merge directly itself**, in the main checkout, with `git merge --no-ff
<branch>` run from the main session's own shell — **none of the three original workers was resumed to
perform its own convergence.** This is a direct reversion to Smoke Test 1's parent-performed shape for this
specific responsibility, not a repetition of Smoke Test 2's validated worker-performed shape, even though
the *policy* decision (human-authorized, sequential, one-at-a-time) matches ST2's policy almost exactly.
**Do not conflate the two**: policy and performer are the two separate axes `responsibility-boundaries.md`
already distinguishes, and ST3 kept ST2's policy shape while reverting the performer to ST1's shape.

**Evaluating whether sequential convergence has now accumulated enough evidence to become default
mechanical behavior.** The *sequencing* itself (one at a time, in a human-chosen order, onto a
confirmed-fresh tip before each subsequent merge) has now succeeded, conflict-free, across three separate
runs (ST1's parent-performed sequential merges; ST2's worker-performed sequential merges; ST3's
parent-performed sequential merges) — this is real, repeated evidence for the *sequencing* pattern
specifically. It has **not** yet accumulated equivalent evidence for *who* performs it: ST1 and ST3 both
used the parent; only ST2 used the original workers; and no run has yet tested convergence under real
file-overlap or a genuine race condition (all three runs' waves were file-disjoint by construction). **Do
not treat "parent-performed convergence" as now-validated default behavior on this evidence** — it worked
because this wave's merges were disjoint and low-risk, not because a comparison of parent-performed versus
worker-performed convergence favored one over the other; ST3 simply did not attempt the worker-performed
shape ST2 validated, for reasons not evidenced in this run's transcripts (no worker was asked to converge
itself, and no worker asked to).

**Distinguishing default-safe mechanics from cases still requiring human judgment.** What all three runs
agree on: sequential ordering onto a confirmed-fresh tip, `--no-ff` merge commits matching this repo's
existing convention, and re-verifying (or, in ST1/ST3's case, at minimum re-checking `git status`) after
each merge before the next — these look like safe, repeatable default mechanics regardless of who performs
them. What still requires human judgment, unresolved by any of the three runs: genuine merge conflict
resolution, unexpected drift in the shared branch's tip between decision and execution, a stale or
partially-invalidated approval discovered mid-convergence, and ambiguity about which branch is actually the
correct convergence target when more than one shared branch could plausibly apply — none of these
conditions has been exercised even once across ST1, ST2, or ST3.

## Verification evidence after commits

**Was the committed content equivalent to the combined candidate that was verified before approval?**
Directly checked: the integration worktree's assembled diff (9 modified + 5 new files, enumerated in
"Combined candidate" above) matches, file-for-file, the union of what each worker's own approved Commit
plan actually produced — `bbca52b` touches exactly `navItems.ts`; `3978d7c`+`a854314` touch exactly the 5
files #344's plan named; `aed09ce` touches exactly the 8 files #345's plan named. No worker altered
implementation content between the combined-verification pass and its own commit construction — each
worker's own post-commit report states its working tree was clean and matched its approved plan exactly,
and this audit's direct `git show --stat` on each resulting commit confirms the same file sets.

**Whether another full suite was run after convergence.** **No** — the parent's own record shows no
`php artisan test` invocation against the fully-converged `feat/policies-http-frontend` (post-`50c6c83`)
at any point before push. Each worker did run its own narrowest-reliable-scope check as part of its own
commit-building step (per `commit-boundaries.md`'s "verify each semantic commit at the narrowest reliable
scope" guidance), but no worker and no parent action re-ran the full 1287-test suite against the final,
fully-merged tip.

**Was another full suite necessary under the existing approval/verification-validity rules?** On the
evidence above (committed content equivalent to the already-verified combined candidate, no worker altering
implementation content during commit construction), `review-gates.md`'s "Approval validity before Commit
plan and before push" section's own standard — "ordinary staging and assembling of unchanged,
already-approved content into its already-approved commits must not automatically invalidate [a prior
verification] merely because HEAD moved or the remaining working-tree diff changed shape" — applies
directly and supports treating the pre-commit combined-suite result as still valid, without requiring a
fresh full run after convergence. **This document does not itself certify that this reasoning was actually
applied by the parent as an explicit check** — no message in the parent's own record explicitly invokes this
approval-validity reasoning before skipping a post-convergence full run; the outcome matches what that rule
would recommend, but the parent's own record does not show it being reasoned through at the time.

## Worker bootstrap cost

Directly confirmed from each worker's own transcript, not inferred:

- **#334** ran `npm ci --prefer-offline --no-audit --no-fund`, `composer install --no-interaction
  --prefer-dist -q`, and `php artisan wayfinder:generate` (twice — once plain, once with `--with-form`
  after discovering the flag mismatch produced ~30 spurious `.form()` type errors across unrelated pages
  in its own environment, resolved by regenerating with the correct flag).
- **#344**'s worktree started with **no** `vendor`/`node_modules`/`.env`/built assets at all — it ran
  `composer install`, set up `.env` + sqlite + migrations, `npm install`, `wayfinder:generate`, and
  `npm run build` before any test could run.
- **#345** ran `php artisan wayfinder:generate` (twice), `composer install --no-interaction --quiet`, and
  `npm install --silent`.

**Why this happened.** Git worktrees do not inherit gitignored state (`vendor/`, `node_modules/`, `.env`,
built assets) from the main checkout or from each other — each is an independent working directory on disk.
This is the third consecutive smoke test (ST1, ST2, ST3) in which every worker independently paid this same
bootstrap cost in its own fresh worktree; `combined-candidate.md`'s own "What remains unresolved" already
flagged "environment bootstrap cost at scale" as unexamined, and this run adds a third data point without
resolving it.

**Classification.** This is a **runtime/provisioning finding**, not a methodology gap — no `implement-it`
rule specifies or should specify how a worktree gets its dependencies installed; the cost is inherent to
how isolated Git worktrees work, independent of Agentic Engineering's own text. It is recorded here,
per the audit's instruction, as an efficiency finding worth investigating before running higher worker
counts, not as a concrete optimization to adopt now.

## Parent supervision

**What allowed the parent to detect #344's and #345's mistakes.** In both cases, the worker's own report
text itself stated the mistaken action plainly (#344: "Decision needed from you next: Per
`verification.md`, before `review-it` can be invoked and Gate 1 reported, you need to make the full-suite
run/skip decision"; #345: "Status: stopped at 'Review implementation' (Gate 1) — needs your decision"),
and the parent recognized the mismatch against the installed `verification.md`/`review-gates.md` text it
had itself already read directly (from the correct, main-checkout path) earlier in the same session, before
any worker launched. Detection did not require inspecting either worker's raw transcript — the mismatch was
visible in each worker's own handback text, compared against methodology the parent already held in its own
context.

**Is parent supervision merely defensive execution assurance, or evidence for an eventual orchestrator
responsibility?** On this run's evidence, it is closer to the former, with one important qualifier: the
parent did not need cross-worker knowledge to catch either mistake — each correction only required
comparing one worker's own report against methodology text, a per-worker check in substance, even though it
happened to be performed by the party coordinating all three. Nothing about the correction itself required
knowing what the *other* workers were doing. This differs from the genuinely cross-worker
responsibilities elsewhere in this document (combined-candidate assembly, convergence sequencing, decision
batching), which do inherently require multi-worker visibility.

**Whether methodology should still be clarified so correct execution does not depend on parent
correction.** Given "What differed between #334 and #344/#345" above, the actual failure mode is not that
the rule text needs clarifying — it is that two of three workers could not reliably see the *current*
version of the rule text at all, for reasons outside the rule text's own control. Clarifying
`verification.md`'s prose further would not have prevented either mistake, since neither worker was reading
that prose's patched version at the moment it mattered. **This document does not normalize the mistake
merely because the parent caught it** — it records plainly that two of three independently-launched
workers, given identical instructions, produced the identical class of deviation, and that catching it
depended on the parent already holding independently-verified knowledge of the correct rule text, not on
any mechanism that guarantees a worker will see that text itself.

## Companion activation ordering

Reconstructed precisely in "Worker #344" above: retroactive activation is real, self-disclosed, and
directly confirmed by transcript line-number ordering (implementation edits at lines 256–272, all seven
companion activations at lines 432–459, after both those edits and a first `review-it` pass at line 380).
**Why this happened**, so far as the evidence shows: no message in #344's own transcript states a reason;
the worker's own self-report attributes it to having "followed sibling-file conventions directly instead of
invoking the skill mechanism first." **How it detected the mistake**: proactively, on its own initiative,
before presenting any gate — not prompted by the parent. **What re-check it performed**: activated each of
the five previously-skipped companions and checked the already-written diff against each one's guidance.
**The actual defect found and fixed**: the near-tautological `count(Enum::cases())` test assertions,
corrected to literal integers, independently verified against the actual enum source, re-tested, and
re-reviewed (full detail in "Worker #344"). **Whether existing companion-activation methodology is already
clear.** Not established either way by this document — the reconstruction above answers *what happened and
how it was caught*, but this audit did not locate or inspect `companion-activation.md`'s own text as part
of this run's evidence-gathering, so no claim is made here about whether that rule's wording is or isn't
sufficient; that would require reading it directly, which this document did not do. **Classification, on
the evidence actually gathered:** this is recorded as an execution-order deviation that the worker itself
caught and fully corrected before any human-facing report relied on the affected content, not as a
demonstrated rule gap — but "not a demonstrated rule gap" here means "not evidenced," not "confirmed
sufficient."

## Push and issue closure

**Per issue, directly confirmed against live GitHub state** (`gh issue view <n> --json state,closed,
closedAt,body,comments`, re-run for this audit, not trusted from the parent's own prior report alone):

| Issue | Commits pushed/reachable | Closed | Closing comment | Task checkboxes checked | Closure procedure followed |
|---|---|---|---|---|---|
| #334 | Yes — `bbca52b` reachable via `50c6c83` on `origin/feat/policies-http-frontend` | Yes, `2026-09-22T07:21:45Z` | Yes — names commit + merge SHA | **No — 0 of 1 checked** | **No** |
| #344 | Yes — `3978d7c`, `a854314` reachable | Yes, `2026-09-22T07:21:47Z` | Yes — names both commits + merge SHA | **No — 0 of 2 checked** | **No** |
| #345 | Yes — `aed09ce` reachable | Yes, `2026-09-22T07:21:50Z` | Yes — names commit + merge SHA | **No — 0 of 2 checked** | **No** |

**This is a confirmed, direct regression, not an inference.** `issue-closure.md`'s own closing recipe,
read directly, states as its first step: *"Verify which Tasks are actually complete, and update the body...
Flip every `- [ ]` that's actually done to `- [x]`"* — via `gh issue edit N --body-file <file>` — **before**
the actual close. None of the three issues had this step performed: their bodies, re-fetched fresh for this
audit, still show every task as `- [ ]`. This exactly reproduces Smoke Test 1's specific, named failure
("the issue task checkboxes remained unchecked even though the issues were closed") — a failure Smoke Test 2
had directly and confirmedly reversed for all three of its issues
(`smoke-test-2.md`, "Push and issue closure": "all three issues closed with every completed task checkbox
actually checked, and this audit independently re-verified that against live GitHub state"). **ST3 reverts
this specific fix.**

**Why.** Directly attributable to the same root cause as the convergence-performer reversion above: in ST2,
each *original worker* was resumed to perform its own push, its own `issue-closure.md` "ask first," and its
own closing recipe (including the checkbox-update step) inside its own context, where that rule's text was
whatever that worker had itself been executing under all along. In **ST3, the parent closed all three
issues directly** with a single `gh issue close -c "<message>"` call per issue — bypassing `issue-closure.md`'s
recipe entirely rather than invoking it. The parent's own closing comments are accurate and reference real,
verifiable commit/merge SHAs, but accuracy of the comment is not the same thing as following the recipe that
also requires updating the body's task state.

**Push-readiness compliance.** Similarly bypassed as a formal procedure: the parent pushed directly (`git
push origin feat/policies-http-frontend`) after checking `git status -sb`'s "ahead 7" and confirming the
branch was tracked, but did not run `push-readiness.md`'s own reachability/trailer-recheck sequence the way
every ST2 worker did formally for its own push. The push itself succeeded (plain fast-forward, not
rejected), so no incorrect result followed from this — but the *procedure*, not merely its outcome, was
bypassed.

## Milestone handoff

**Milestone 27 zero-open-issues, re-verified fresh for this audit:** `gh api
repos/elieandraos/useOrbit/milestones/27` → `{"closed_issues": 35, "open_issues": 0, "state": "open"}` —
confirmed directly, matching the parent's own recompute at the time.

**Did the dependency-ready recomputation correctly recognize milestone exhaustion?** Yes — the parent
explicitly ran `gh issue list --milestone "Phase 26..." --state open` (initially against the milestone
*name*, which under-returned due to a default 30-item pagination limit the parent then caught and corrected
by re-querying with `--limit 100` against the milestone *number*) and reported the correct zero-open-issues
result once the pagination artifact was resolved.

**Did `implement-it` hand off to `ship-it`'s milestone-PR-readiness gate rather than silently shipping?**
Yes — the parent explicitly declined to decide next steps itself, stating the milestone hand-off rather
than proceeding, and only invoked `ship-it` on a later, separate human request ("Check if the milestone PR
is ready to create").

**PR readiness / creation, and whether the PR remains unmerged.** The three-condition gate (zero open
issues, re-verified fresh a second time at that point; the human's direct confirmation that final manual
testing had happened and found nothing further) passed. The PR-target/base-branch/milestone-field
convention was discovered from real prior merged PRs (`#321`, `#309`, `#298` — not assumed), an existing-PR
check found none, a complete proposal was presented and explicitly approved (including a follow-up
clarification removing the default attribution footer), and PR #357 was created and re-fetched to confirm
its actual number/base/head/title/milestone matched the approved proposal exactly. **Directly re-confirmed
for this audit:** `gh pr view 357` → `state: OPEN`, `mergedAt: null`, `baseRefName: main`, `headRefName:
feat/policies-http-frontend` — the PR remains open and unmerged throughout this entire audit, per the
human's explicit instruction not to merge it as part of this exercise.

## Local and remote state

**ST2's specific finding** (`smoke-test-2.md`): after ST2's worker-performed convergence, the *local*
`feat/policies-http-frontend` ref in the main checkout was left stale at the pre-convergence tip, while only
the *remote* ref actually advanced — because every ST2 worker pushed via `git push origin
<throwaway>:feat/policies-http-frontend` without ever checking out that branch locally in the main
worktree.

**Did ST3 avoid this?** **Yes, directly confirmed — and for a structural reason, not a deliberate fix.**
Because ST3's convergence was performed by the *parent itself*, directly in the main checkout, on the
already-checked-out local `feat/policies-http-frontend` branch, every merge commit landed on the local ref
immediately as it was created — there was no separate remote-only push step that could leave local and
remote diverging. Directly verified for this audit: `git rev-parse feat/policies-http-frontend` and `git
rev-parse origin/feat/policies-http-frontend` both return `50c6c8304d603513be43cb9e1931cfeb1f02bf87` —
identical. **This is a side effect of ST3's parent-performed convergence (itself a regression relative to
ST2's worker-performed shape, per "Convergence behavior" above), not evidence that the underlying
local/remote-divergence risk has been methodologically resolved** — the same risk would recur if a future
wave reverted to ST2's worker-performed convergence pattern without also re-checking the main checkout's
local ref afterward.

**No accidental application dirt.** Confirmed at multiple points throughout this run and again for this
audit: `git status --porcelain=v1` in the main checkout shows only the five pre-existing candidate-skill
files (`review-gates.md`, `sequencing.md`, `verification.md`, `worktree-preservation.md`, `skills-lock.json`)
— the same five present before any worker launched, untouched and uncommitted throughout, exactly as the
human's original instruction required.

## ST1 → ST2 → ST3

| Dimension | ST1 | ST2 | ST3 | Classification |
|---|---|---|---|---|
| Parallel worker launch | ✓ (2) | ✓ (3) | ✓ (3) | VALIDATED |
| Isolated worktrees | ✓ | ✓ | ✓ | VALIDATED |
| Temporary branches | Improvised by parent | `sequencing.md` patch, applied unprompted | Same patch, applied unprompted by all 3 | VALIDATED |
| Independent lifecycle progression | Not exercised (no gates reached) | ✓ all 3, both gates | ✓ all 3, both gates | VALIDATED |
| Focused (targeted+broader) verification | ✓ both workers, inconsistent scope | ✓ all 3 | ✓ all 3 | VALIDATED |
| Per-worker full-suite behavior | Both workers decided unilaterally, no ask | Asked and answered per-issue for both workers | **Removed by design** — but 2 of 3 workers still attempted it, both caught and corrected | FIXED SINCE PRIOR TEST, in the sense the rule now says not to ask; STILL UNRESOLVED in the sense 2 of 3 workers weren't reliably shown that rule (see "What differed") |
| `review-it` | 1 of 2 workers | ✓ all 3 | ✓ all 3, correct in every case | VALIDATED |
| Candidate-ready boundary (no Gate 1 yet) | N/A (concept didn't exist) | N/A | Eventually held for all 3; 2 of 3 needed correction | NEW FINDING, partially validated |
| Human implementation approval | Bypassed both times | ✓ all 3, worker-specific | ✓ all 3, batched in one message | VALIDATED |
| Worker-specific resume | Not exercised | ✓ all 3, incl. 2 ambiguous cases resolved correctly | ✓ all 3 correction resumes resolved correctly (no ambiguous case this run) | VALIDATED |
| Semantic Commit plans | Derived internally, not presented | ✓ all 3, presented + approved | ✓ all 3, presented + approved | VALIDATED |
| Durable commits | Both, unauthorized | ✓ all 3, post-approval only | ✓ all 3, post-approval only, trailer-clean | VALIDATED |
| Combined candidate (pre-commit) | Not attempted | Not attempted (concept didn't exist yet) | **First real attempt** — succeeded, with confirmed mechanism divergences from the validated procedure | NEW FINDING |
| Combined verification | Never performed | Gap, partially/incidentally covered post-hoc | **First deliberate full-suite pass against the true pre-commit union** | FIXED SINCE PRIOR TEST, mechanism-validated with caveats |
| Human-facing review presentation | N/A | Gate/rule vocabulary leaked; substance mostly preserved | Same vocabulary leak repeats; substance preserved; new repetition-across-async-arrivals finding | REPEATED, plus NEW FINDING (repetition) |
| Convergence policy | Parent-inferred, not asked | Human-decided, explicit | Human-decided, explicit, deferred correctly until commits existed | VALIDATED (policy) |
| Convergence execution (performer) | Parent-performed | **Worker-performed** | **Parent-performed** | REPEATED FROM ST1, not ST2 — genuine reversion |
| Convergence sequencing | N/A (single actor) | Parent-serialized, race avoided | Parent-serialized (as sole performer), no race | VALIDATED, different shape |
| Push (procedure) | Bypassed | ✓ all 3, formal `push-readiness.md` per worker | **Bypassed** — parent pushed directly, no formal reachability/trailer recheck | REPEATED FROM ST1 |
| Issue closure procedure | Bypassed | ✓ all 3, formal `issue-closure.md` per worker | **Bypassed** — parent closed directly, no checkbox-update step | REPEATED FROM ST1 |
| Task-checkbox completion | ✗ unchecked | ✓ checked, independently re-verified | **✗ unchecked, independently re-verified** | REPEATED FROM ST1 — direct regression |
| Local/remote branch state | Not applicable (parent performed both locally) | Local ref left stale; only remote advanced | Local and remote identical (side effect of parent-performed convergence) | NEW FINDING (avoided this time, for a structural reason, not a fix) |
| Next-work/milestone progression | Not reached | ✓ all 3, converged on same ready set | ✓ milestone exhausted, correctly handed to `ship-it` | VALIDATED, first time reaching this state |
| Worker bootstrap cost | Not recorded in detail | Every worker independently bootstrapped | Every worker independently bootstrapped again | REPEATED — third consecutive occurrence, unresolved |
| Parent supervision correcting workers | Not exercised (no gates reached) | Not needed (no worker deviation observed) | **Needed twice**, both caught and corrected | NEW FINDING |

## Skill findings

Kept conservative, per the audit's own instruction. No skill file was edited as part of this audit.

**Existing rules confirmed sufficient:**
- `commit-boundaries.md`'s trailer policy — applied correctly, unprompted, by all three workers, all five
  commits confirmed trailer-clean by direct `git log` inspection.
- `push-readiness.md`/`issue-closure.md`'s own text — not shown insufficient by this run; they were not
  followed, which is different from being inadequate. No evidence here suggests either file's wording needs
  to change.
- `review-it`'s checklist and staleness discipline — ran correctly all three times, including catching a
  real flaky test and a real near-tautological assertion, neither of which required any parallel-specific
  accommodation.
- The core two-approval structure (`review-gates.md`'s Review implementation / Commit plan split) — held
  for all three workers with no commit created before its matching approval, in every case.

**Candidate clarification/correction with repeated evidence:**
- `sequencing.md`'s convergence-timing gap (see "Convergence timing" above) — one clean instance of the
  parent asking prematurely and being corrected; the clarification is stated but not applied to the file.
- The combined-verification run/skip framing (see "Verification-policy decision" above) — a real,
  attributable divergence between the pre-registered "required" position and what was actually presented
  and decided live. Recorded precisely; no file change proposed or made.

**Explicit methodology decision made during ST3:**
- The human's convergence-timing deferral, quoted in full under "Timeline." This is a genuine explicit
  decision, correctly distinguished (per "Verification-policy decision" above) from the combined-
  verification run/skip framing, which was **not** an explicit human-authored principle in the same sense —
  it was the parent's presentation choice, ratified by a specific answer.

**Execution mistake — existing rule already sufficient:**
- #344's and #345's initial per-worker full-suite/Gate-1 attempts. Per "What differed between #334 and
  #344/#345," the installed rule text itself is not shown ambiguous — the mistake traces to which physical
  copy of that rule text each worker actually read, not to what the text says once read. No rule-wording
  correction is indicated by this finding.
- #344's retroactive companion-skill activation — self-caught, fully corrected, with no claim made here
  about whether `companion-activation.md`'s own wording is sufficient (not inspected as part of this
  evidence-gathering).

**Runtime/provisioning finding:**
- Worker bootstrap cost (third consecutive occurrence, unresolved, classified as runtime/provisioning, not
  methodology).
- **The candidate-patch-propagation gap** (see "What differed" above) — the single most consequential
  finding of this audit. An uncommitted candidate patch living only in a main checkout's working directory
  is not reliably visible to concurrently-launched isolated git worktrees, and whether a given worker
  happens to see it depends on incidental path-resolution choices, not on anything the methodology
  controls. This is a runtime/process-execution concern about how candidate methodology changes propagate
  into isolated workers *before* they are committed — not a wording gap in any rule file, and not
  something a rule-file edit can fix by itself (the content in question is, by definition, not yet
  committed to the repository any worktree checks out).

**Cross-worker / Control Room responsibility candidate:**
- Decision-boundary batching across asynchronously-reporting workers (see "Decision-oriented
  presentation") — real, recurring evidence this run, but about presentation/orchestration, not worker
  methodology.
- Combined-candidate assembly's actor and exact mechanism (who runs it, using which exact procedure) —
  this run supplies one data point (the parent, using a divergent-but-successful procedure) rather than a
  validated, repeatable answer.
- Convergence performer (parent vs. worker) — now two data points favoring parent-performed (ST1, ST3) and
  one favoring worker-performed (ST2), with the ST3 reversion's cause not evidenced in this run's
  transcripts. This is exactly the kind of unresolved recurring question a future Control Room
  investigation should examine directly, rather than this document picking a default from asymmetric
  evidence.

## Control Room / orchestration evidence

Evaluated against `orchestration.md`'s extraction bar (inherently cross-worker; remains necessary after the
relevant skill correction; recurs across real waves; creates awkward ownership inside a worker skill; can be
stated independently of Claude Code's own API) — per-responsibility, across all three smoke tests:

- **Combined-state verification.** Now exercised as a real mechanism for the first time (ST3), after
  recurring as an unowned gap in both ST1 and ST2. Inherently cross-worker (verifying a union requires
  knowing the union exists). Not fitting inside a worker skill (no worker can verify code it hasn't seen
  from a sibling). **This is the strongest Control Room candidate to date** — three consecutive
  waves have now touched this exact responsibility, escalating from "never attempted" (ST1) to "gap,
  incidentally covered" (ST2) to "attempted directly, with confirmed procedural divergence from the
  validated mechanism" (ST3). Still not extracted here — this run adds evidence of *how it goes when
  actually attempted*, not yet a third clean success confirming a stable procedure.
- **Convergence performer.** Two data points for parent-performed (ST1, ST3), one for worker-performed
  (ST2). Inherently cross-worker only in the *sequencing* sense (which worker goes first, avoiding a race)
  — the actual merge/push mechanics are ordinary Git operations either actor can run. Insufficient,
  contradictory evidence to promote this to a settled default either way.
- **Decision-boundary batching / decision-oriented presentation.** Real, recurring evidence across ST2 and
  ST3 (ST2's ambiguous-answer routing; ST3's async Commit-plan/Review-implementation relay repetition).
  Inherently requires knowing multiple workers' current states simultaneously — no single worker skill
  could own this. Growing toward the extraction bar, not yet at it (still evidenced only within single
  runs, not across a clean before/after skill correction the way `sequencing.md`'s branch patch was tested
  against).
- **Candidate-patch propagation into isolated workers.** A genuinely new finding this run, not previously
  identified by ST1/ST2/`orchestration.md`/`responsibility-boundaries.md`. This is arguably **runtime
  mechanics**, not a Control Room responsibility in the cross-worker-coordination sense the other
  candidates represent — it's about how one specific kind of state (an uncommitted methodology change)
  reaches (or fails to reach) an isolated execution context, which is closer to `orchestration.md`'s own
  "runtime mechanics" category (concurrent execution contexts, workspace isolation) than to its
  cross-worker-coordination candidates.
- **Concurrent-safe issue selection, next-work recommendation, architectural drift.** Not meaningfully
  advanced by this run specifically — ST3's wave was pre-selected as the milestone's only remaining open
  issues (no selection judgment was exercised), the recompute correctly found zero open issues (no
  sibling-visibility nuance arose), and the three issues' structurally unrelated surfaces gave no
  opportunity for the kind of convention drift ST2 found. These remain exactly the WATCH items
  `responsibility-boundaries.md` already classified them as.

## What remains unresolved

- Whether combined verification should be a mandatory required step or a human run/skip choice at the wave
  level — genuinely reopened by this run's own live divergence from the pre-registered position, not
  resolved by it.
- Who should perform convergence (parent vs. original worker) — now contradictory evidence across three
  runs, with no data explaining why ST3 diverged from ST2's validated shape.
- Whether the combined-candidate mechanism's specific procedural gaps found here (missing `--3way`,
  `--index`, `--binary`; filesystem-copy substitution for untracked files) would have mattered under a real
  file collision or a binary file — neither was exercised by this wave's clean disjointness.
- How to make an in-flight candidate methodology patch reliably visible to concurrently-launched isolated
  workers before it is committed — the single largest open question this audit surfaced, with no proposed
  fix evaluated here.
- Why `issue-closure.md`'s checkbox-update step and `push-readiness.md`'s formal reachability recheck were
  bypassed this run specifically, when ST2 demonstrated both work correctly when the original worker
  performs its own closure/push — this document records the reversion precisely but does not establish a
  cause beyond "the parent performed these steps directly instead of delegating them back."
- Whether the decision-boundary-batching gap (Commit-plan/Review-implementation relay repetition) is best
  addressed by parent-session discipline alone or eventually needs a structural mechanism.

## Is another smoke test needed?

**Yes, but narrower than a full re-run.** ST1, ST2, and ST3 have already validated, repeatedly, that
isolated concurrent workers can run independent `implement-it` lifecycles correctly through both human
gates, with worker-specific resume, semantic commit planning, and (in ST2 and, partially, ST3) correct
push/closure procedure. **What has not yet been validated, and would require targeted rather than broad
re-testing:**

- A wave with a genuine file overlap or merge conflict, at either the combined-candidate-assembly stage or
  the convergence stage — no run across all three smoke tests has exercised this at all.
- Convergence and issue-closure procedure performed by the **original workers themselves**, after a
  successful combined-verification pass — ST3 skipped this by having the parent perform it directly, so
  this specific composition (ST2's worker-performed convergence *following* ST3's combined-verification
  step, rather than either alone) remains untested.
- Whether an explicit "surface the current, patched rule text directly to each worker in its own launch
  prompt" mitigation (rather than relying on the `Skill` tool's own resolution) would close the
  candidate-patch-propagation gap this audit found — this is a process/runtime question a smoke test could
  answer directly, cheaply, without needing new methodology.

**Which remaining issues are rule/document corrections rather than architecture unknowns:** the
combined-verification run/skip framing question, the convergence-timing clarification for `sequencing.md`,
and the checkbox/push-procedure reversion are all rule-and-process questions — none requires new
architecture to resolve.

**Which unresolved concerns belong to future orchestration/runtime investigation rather than another
implementation smoke test:** the convergence-performer question (parent vs. worker) and the
decision-boundary-batching gap are both cross-worker presentation/coordination questions better suited to a
dedicated Control Room investigation than to another consumer-issue smoke test, since neither depends on
running more real application code — both are about how the parent session behaves once workers have
already reported correctly.

## Recommended next steps

In order, smallest evidence-backed step first:

1. **Decide, explicitly, whether combined verification is a mandatory required step or a wave-level run/skip
   choice** — this run reopened a question the prior research position had already closed, and that
   reopening should be resolved deliberately, not left as an accidental precedent from one run's framing.
2. **Reconcile this document's findings into `combined-candidate.md`, `responsibility-boundaries.md`, and
   `orchestration.md`** — specifically the confirmed mechanism divergence (missing `--3way`/`--index`/
   `--binary`, filesystem-copy substitution), the convergence-performer contradiction across ST1/ST2/ST3,
   and the new candidate-patch-propagation finding, none of which any prior document anticipated.
3. **Investigate the candidate-patch-propagation gap directly** — before running a fourth smoke test that
   depends on any future candidate patch being reliably visible to isolated workers, since this run showed
   two of three workers cannot be assumed to see it without an explicit workaround.
4. **Public README/documentation and any version/release decision remain out of scope until steps 1–3 are
   resolved** — this document's own evidence standard (matching `responsibility-boundaries.md`'s prior
   conclusion) does not support publishing an unresolved mechanism as if it were proven.
5. **The Phase 26 useOrbit PR (#357) manual review and merge is a separate, application-delivery concern**,
   entirely independent of the above — nothing in this audit bears on whether that PR is ready to merge as
   application work; it remains open and unmerged, exactly as instructed, and this document takes no
   position on it beyond confirming its current, live state.
6. **A Control Room/orchestration extraction investigation is better justified now than after ST2**,
   specifically for combined-state verification and decision-boundary batching, but should be scoped as an
   investigation of the two contradictions this run surfaced (convergence performer; combined-verification
   framing) rather than a general architecture design exercise.
7. **Runtime worker-provisioning investigation** (bootstrap cost) remains a valid, lower-priority parallel
   track, unaffected by anything else on this list.

## Conclusion

Smoke Test 3 is the first run to genuinely assemble and verify the union of several still-uncommitted
parallel workers' changes before any of them reached human approval — a real, working first instance of the
one gap both prior smoke tests left open, with a full 1287/1287 fresh regression pass, clean frontend
checks, and a clean route table, all directly confirmed from the parent's own tool output rather than
restated from a worker's claim. Two of three workers initially attempted the exact per-worker full-suite/
Gate-1 mistake the ST2+ST3 candidate patch was written to prevent — but direct transcript evidence traces
this to an uncommitted candidate patch's invisibility inside isolated git worktrees, not to ambiguous rule
prose, a distinction this document establishes with specific file paths and line numbers rather than
inference. Alongside that validated core result, this run also produced two confirmed regressions relative
to Smoke Test 2 — task-checkbox completion and formal push/closure procedure, both bypassed because the
parent performed convergence, push, and closure directly rather than delegating back to the original
workers as ST2 validated — and one genuine, precisely-attributed open question: whether combined
verification should remain a mandatory required step, as the pre-registered research position held, or the
human run/skip choice this run's own live framing introduced and the human ratified. None of these findings
justifies a skill-file edit on its own; each is recorded here as evidence for a deliberate decision still to
be made.
