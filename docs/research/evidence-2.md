# Parallel Implementation Smoke Test 2 — Evidence

Status: Evidence from useOrbit #341/#342/#343.

This document reconstructs Smoke Test 2 from direct evidence: the parent session's own conversation
record (SubagentHandback reports and task notifications received in real time), direct `git`/`gh`
inspection of `elieandraos/useOrbit` performed after the run, and the two-file candidate patch to
`implement-it` that was live during the run (`sequencing.md`'s "Parallel workers in a delivery/phase
milestone" section, `worktree-preservation.md`'s terminology clarification). Where something is
inferred rather than directly observed, it is labeled `Inference:` explicitly.

## Experiment

Repository: `elieandraos/useOrbit`. Milestone: "Phase 26 — Policies HTTP & Frontend." Milestone
branch: `feat/policies-http-frontend` (confirmed at `cd70cbc` at launch via `git status`/`git log`
before the run).

Issues, all pre-verified dependency-ready (depend only on #322, closed):

- #341 — Wire the Policies tab on the Client show page
- #342 — Wire the Policies tab on the Agent show page
- #343 — Wire the Policies tab on the Carrier show page

The parent launched three `general-purpose` background agents via the `Agent` tool, each with
`isolation: "worktree"`, in a single message (all three `Agent` calls in one turn). Each agent
received a fully self-contained prompt (fresh agents carry no shared context) instructing it to: load
`implement-it` via the `Skill` tool; read `sequencing.md`'s new parallel-worker section; cut its own
temporary issue branch from the milestone branch's confirmed tip, named `issue-<N>-<slug>` per this
repo's own existing convention (verified against real prior branches, e.g. `issue-354-policies-life-
pages`, `issue-355-policies-travel-pages`); run every real `implement-it` gate for itself and stop
there, presenting the exact report and ending its turn rather than fabricating approval; and, on
reaching `push-readiness.md`'s branch-identification step, stop again — explicitly, by name — because
`sequencing.md`'s parallel-worker section states convergence mechanics/timing are undefined, and not
to guess an answer.

This is a direct, evidence-supported difference from Smoke Test 1's delegation, where (per
`evidence.md`) workers were told to "stop once its branch was committed and tests passed" —  a
launch-time instruction identified there as `evidence.md`'s root-cause explanation for ST1's gate
bypass. ST2's delegation did not contain that instruction.

Resulting agent identities (used throughout as evidence anchors):

| Issue | Agent ID | Temp branch |
|---|---|---|
| #341 Client | `a45052861002f76d7` | `issue-341-client-policies-tab` |
| #342 Agent | `af568be37d36d15ee` | `issue-342-agent-policies-tab` |
| #343 Carrier | `ab013dbcd10f9fc5e` | `issue-343-carrier-policies-tab` |

## Worker #341 lifecycle (Client)

1. **Launch.** Background agent `a45052861002f76d7`, worktree isolation.
2. **Branch setup.** The worker found its worktree's default checkout (`a529ff6`) ~70 commits behind
   `feat/policies-http-frontend`'s confirmed tip. It verified local `feat/policies-http-frontend` ==
   `origin/feat/policies-http-frontend` == `cd70cbc` via `git rev-parse`, then cut
   `issue-341-client-policies-tab` from that confirmed tip. It explicitly reasoned this was "a factual
   correction... not a judgment call with multiple defensible answers," so it proceeded without asking.
3. **Skills.** Reported activating `laravel-best-practices`, `laravel-inertia-stack` (+
   `resource-controller.md`, `authorization.md`, `resources.md`, `inertia-pages.md`, `pest-testing.md`,
   `test-ownership.md`), `inertia-vue-development`, `testing-best-practices`, `wayfinder-development`,
   `my-phpstorm-conventions`; considered and rejected `tailwindcss-development`,
   `fortify-development`/`echo-development`/`echo-vue-development`/`infer-conventions` as not
   applicable.
4. **Implementation.** `Client::policies(): HasMany`; new `ClientPoliciesController::index()`;
   `clients.policies.index` route in `routes/policies.php`; `ClientsController::show()` real
   `policiesCount`; `PoliciesController::create()` reading an optional `client_id` and exposing
   `selectedClientId`; `ClientDetailShell.vue` tab fix; `ClientPoliciesCard.vue` "Add policy" enabled;
   new `ClientPolicies/Index.vue`; new tests `PoliciesIndexTest.php`, `CreateTest.php`, plus additions
   to `ShowTest.php`.
5. **Targeted verification (first pass).** `vendor/bin/pint --dirty` clean; `eslint`/`prettier` clean;
   `vue-tsc` clean; `php artisan test --compact` across `tests/Feature/Http/Clients`,
   `tests/Feature/Http/Policies`, `tests/Feature/Models/ClientTest.php`, `tests/Feature/Policies/{Client,
   Policy}PolicyTest.php` → **343 passed, 1722 assertions, 0 failures**.
6. **Full-suite decision — genuine stop.** The worker explicitly reported: "I have **NOT** invoked
   review-it or reported at the Review implementation gate yet," citing `verification.md`'s requirement
   that the human full-suite run/skip choice be answered *before* `review-it` is invoked. It gave a
   recommendation ("lean toward skip") but asked rather than deciding. **This is the only one of the
   three workers that stopped before `review-it` for this reason** (see "Verification" below).
7. **Human decision.** Parent relayed the question; human answered "Skip full suite for both [#341 and
   #343]" in a later turn (after #343 had already reported its own version of the same question — see
   below). Parent sent `a45052861002f76d7`: "skip the full regression suite... proceed to invoke
   review-it and report at the Review implementation gate. Note: Gate 1 itself is NOT yet approved."
8. **Resumption → `review-it` → Review implementation report.** Worker resumed, ran `review-it`
   standalone (worktree vs. `HEAD`, 9 tracked + 4 untracked files, full checklist, **Clean**), then
   reported "Review implementation report (Gate 1)" with the `Activated skills:` line, implementation
   summary, files touched, verification results, `review-it`'s clean result, ending with "Review
   implementation: approve to proceed to Commit plan."
9. **Human decision.** Answered in a later turn: "Approve #341 and skip full suite for #342 too" — the
   parent parsed this as approving **only** #341 (see "Independent human-gated progression" below for
   why #342 was not treated as approved by this same message).
10. **Resumption → Commit plan.** Worker proposed 3 commits (client-scoped endpoint + tab wiring;
    `policiesCount`; enable Add-policy + prefill), including an explicit note about splitting two
    non-adjacent hunks of `Clients/Show.vue` across commits 2 and 3. Ended with "Commit plan: approve
    to create the proposed commit(s)."
11. **Human decision.** "Approve #341's commit plan" (separate later turn).
12. **Commit creation.** Three commits: `2f45229`, `2552f43`, `a24473a`, each individually
    trailer-checked clean (`git interpret-trailers --parse` → no output, exit 1, per commit — not
    concatenated). Post-commit targeted re-verification: 330 passed / 1683 assertions; Pint clean.
13. **Convergence stop.** Worker reported push-readiness's step 1 as ambiguous for the reason
    `sequencing.md` states, cited prior repo history (`Merge issue-354-...`, `Merge issue-355-...`) as
    evidence only, and asked how to converge — holding with 3 verified, unpushed commits.
14. **Human decision (convergence policy).** "Push each temp branch and merge it into
    feat/policies-http-frontend" (applies to all three workers).
15. **Queued, then released.** Parent told this worker to hold because #343 and #342 were converging
    first (to avoid a shared-branch race); worker acknowledged and stood by; parent released it once
    #342 had converged (`6db2167`).
16. **Convergence performed by the worker itself.** Pushed `issue-341-client-policies-tab` to origin;
    fetched fresh (`6db2167`, not the stale `cd70cbc`); created throwaway local branch
    `converge-issue-341` at that tip (explicitly *not* checking out `feat/policies-http-frontend`, which
    was checked out in the main worktree); `git merge --no-ff issue-341-client-policies-tab` (clean, no
    conflicts — zero file overlap with #342/#343); ran targeted verification against the merged tree
    (Wayfinder regen, `npm run build`, then `php artisan test --compact` across
    `tests/Feature/Http/{Clients,Policies,Agents,Carriers}` + `tests/Feature/Models/ClientTest.php` →
    **446 passed, 2273 assertions, 0 failures**); trailer-checked the merge commit and re-ran the check
    individually across the full unpushed range (`e118e5b`, `a24473a`, `2552f43`, `2f45229` — all
    clean); pushed via `git push origin converge-issue-341:feat/policies-http-frontend` (plain,
    non-force; fast-forward, not rejected — landed as `6db2167..e118e5b`); verified post-push
    reachability with `git merge-base --is-ancestor` for all commits plus an empty
    `origin/feat/policies-http-frontend..origin/issue-341-client-policies-tab`; deleted the local
    throwaway branch; switched back to its own temp branch.
17. **Issue-closure "ask first."** Worker reported push-readiness satisfied and asked, "Do you want me
    to close issue #341 now?" — holding.
18. **Human decision.** "Close #341."
19. **Closure and validation.** Worker closed #341; re-fetched and confirmed `state: CLOSED`, `closed:
    true`, 5/5 checkboxes checked, closing comment present. **Directly re-confirmed by this audit** via
    `gh issue view 341 --json state,closed,body,comments`: `CLOSED`/`true`, 5 checked / 0 unchecked, one
    comment (author `elieandraos`, i.e. the closure was posted under the human's own GitHub identity by
    the tool call, not a bot account) naming all four commit SHAs including the merge commit `e118e5b`
    and the "446 passed / 2273 assertions" figure.
20. **Next-issue recommendation.** Recomputed the milestone's open set (#334, #344, #345 — all
    dependency-ready, nothing newly unblocked by #341's closure) and presented all three as options with
    no single recommendation, citing `review-gates.md`'s "multiple valid sequencing choices" stop.
21. **Terminal handback.** Ended its pass; did not chain into another issue.

## Worker #342 lifecycle (Agent)

Same shape as #341, reconstructed from its own handbacks:

1. **Launch/branch.** `af568be37d36d15ee`, cut `issue-342-agent-policies-tab` from
   `feat/policies-http-frontend`'s confirmed tip `cd70cbc`.
2. **Skills.** `laravel-inertia-stack`, `laravel-best-practices`, `inertia-vue-development`,
   `testing-best-practices`, `wayfinder-development`, `my-phpstorm-conventions`,
   `tailwindcss-development`; explicitly listed non-applicable skills (`fortify`/`echo`/`financial-
   metrics`/`document-it`/`infer-conventions`).
3. **Implementation.** `Agent::policies(): HasMany`; new `AgentPoliciesController::index()`;
   `agents.policies.index` route placed directly in `routes/agents.php` (see "Convergence audit" below
   for why this differs from #341's placement); `AgentsController::show()` real `policiesCount` **and**
   a new `renewingPolicies` prop — active policies with `expiry_date` inside a 30-day window
   (inclusive), capped at 5, soonest first. The worker explicitly flagged this window/cap as its own
   judgment call with "no existing product decision or codebase precedent," offering to change it.
4. **Targeted verification.** `php artisan test --compact tests/Feature/Http/Agents
   tests/Feature/Models/AgentTest.php --no-tia` → **53 passed, 297 assertions**; Pint/eslint/
   prettier/vue-tsc clean.
5. **Ordering deviation: `review-it` ran before the full-suite decision.** Unlike #341, this worker
   self-invoked `review-it` (result: **Clean**, one non-blocking maintainability note about the
   per-class route-map now being duplicated in a third place, explicitly called out as a scope note, not
   a finding) and produced a complete "Review implementation" report *before* the full-suite run/skip
   question was answered. It surfaced both in the same message: "Review implementation: approve to
   proceed to Commit plan — once you've also told me whether to run the full suite... or skip it." See
   "Verification" below for the cross-worker comparison.
6. **Human decisions, split across two turns.** First: "Skip full suite for both [#341 and #343]" did
   not answer #342 (that question was for #341 and #343 only, per the parent's own reading at the time);
   parent explicitly told #342 "skip decision noted... Gate 1 itself is NOT yet approved" — a case where
   the parent deliberately did *not* forward a partial answer as full approval. Worker acknowledged and
   held, restating the open renewal-window question. Second turn: "Approve #342 with a 30-day window" —
   parent forwarded this as full Gate‑1 approval including the window value, and the worker proceeded.
7. **Commit plan.** Two commits proposed (wire the tab/endpoint; surface `policiesCount` +
   `renewingPolicies`), the second's draft message explicitly documenting the 30-day/5-cap choice as "read-
   time judgment calls... easy to retune later since nothing is stored."
8. **Human decision.** "Approve #342's commit plan" (separate turn).
9. **Commit creation.** `038f0ab`, `129e430`; trailer-checked clean individually; targeted
   re-verification 53/53 (both narrowest-scope and combined) still passing.
10. **Convergence stop.** Same pattern and same citation of `sequencing.md`'s undefined-convergence
    language, plus the same prior-history evidence (`#354`, `#355`, `#351`, `#352`, `#329`, etc.).
11. **Human decision (applies to all three).** "Push each temp branch and merge it into
    feat/policies-http-frontend." Parent released #342 second (after #343, before #341), explicitly
    warning it that the milestone tip had already moved to `d9bdb39` and pointing it at #343's exact
    throwaway-branch technique to reuse.
12. **Convergence performed by the worker itself.** Pushed its branch; fetched fresh (`d9bdb39`);
    created throwaway branch `merge-issue-342` at that tip; `--no-ff` merge (clean, no conflicts — "11
    files, all mine; nothing overlapping with #343's changes"); regenerated Wayfinder/rebuilt assets;
    targeted re-verification 53/53 on the merged tree; trailer-checked the merge commit; pushed via
    `git push origin merge-issue-342:feat/policies-http-frontend` → fast-forward `d9bdb39..6db2167`, not
    rejected; verified both original commits as ancestors of the new tip; **left the throwaway branch
    `merge-issue-342` in place rather than deleting it**, explicitly citing observed precedent
    (`merge-issue-332`/`merge-issue-333` from earlier, non-parallel milestone work) — this is the one
    concrete divergence in convergence *housekeeping* between #341/#343 (which deleted their throwaway
    branches) and #342 (which kept it). Confirmed directly: `git branch -a` on the main checkout still
    lists a local `merge-issue-342` alongside deleted-and-gone `converge-issue-341`/`tmp-merge-343-into-
    milestone`.
13. **Issue-closure "ask first," human approval, closure, validation.** Same shape as #341. Directly
    confirmed via `gh issue view 342`: `CLOSED`/`true`, 5/5 checked, one closing comment naming commits
    `038f0ab`/`129e430`/`6db2167` and the 30-day/5-item note, and an explicit scope note that the
    Clients tab / `clientsCount` on the Agent page was intentionally left untouched.
14. **Next-issue recommendation.** #334/#344/#345, no preference stated; one observation offered (not a
    decision): #341 already had an active branch, "likely already spoken for."
15. **Terminal handback.**

## Worker #343 lifecycle (Carrier)

1. **Launch/branch.** `ab013dbcd10f9fc5e`, cut `issue-343-carrier-policies-tab` from
   `feat/policies-http-frontend`'s confirmed tip `cd70cbc` (also noting its own worktree default was
   stale, same reasoning as #341).
2. **Skills.** `laravel-inertia-stack`, `laravel-best-practices`, `inertia-vue-development`,
   `wayfinder-development`, `testing-best-practices`, `my-phpstorm-conventions`,
   `tailwindcss-development`; not activated: `fortify-development`, `echo-development`/`echo-vue-
   development`.
3. **Implementation.** `Carrier::policies(): HasMany`; new `CarrierPoliciesController::index()`
   returning both the paginated `PolicyResource` collection *and* a real `policiesCount` (a deliberate
   addition beyond the issue's literal task wording — flagged by the worker itself and later by
   `review-it` as a scope note, not a defect, because `CarrierDetailShell` is reused on the new page and
   needs that prop); `carriers.policies.index` route placed directly in `routes/carriers.php`;
   `CarriersController::show()` real `policiesCount`; `CarrierDetailShell.vue`'s "Coming soon"
   `ref`-based tab converted to a real `href`-based `Tab`; new `CarrierPolicies/Index.vue`; new
   `PoliciesIndexTest.php`, plus a `ShowTest.php` addition.
4. **Ordering deviation: `review-it` ran before the full-suite decision (same pattern as #342).**
   Reported: "**Full-suite choice: not yet made**... please tell me: run the full suite now... or skip
   it" *inside the same message* that already stated "review-it's result: Clean, with two scope notes."
5. **Human decision.** "Skip full suite for both [#341 and #343], approve Gate 1 for #343 and 341" —
   this is the message that answered #343's full-suite question and its Gate‑1 approval together (unlike
   #341, whose Gate‑1 report didn't exist yet at that point, so the "and 341" half of that instruction
   was necessarily deferred by the parent rather than acted on immediately — see "Independent human-
   gated progression").
6. **Commit plan.** Three commits (endpoint+page+test; wire the tab; feed `policiesCount`), with an
   explicit dependency note ("#2 and #3 have no dependency on each other... #1 must land first") and a
   confirmation that no commit touches configuration/feature-flag/runtime-activation surfaces.
7. **Human decision.** "Approve #343's commit plan" (same turn as the Gate‑1 approval, sent together by
   the parent as two separate `SendMessage` calls but resulting from one user instruction).
8. **Commit creation.** `c4d7d37`, `b23ea48`, `3a023db`; trailer-checked clean individually; per-commit
   targeted verification (`PoliciesIndexTest.php` 5/36, `ShowTest.php` 5/23; `vue-tsc`/`eslint` clean for
   the frontend-only commit, explicitly noting "no frontend test framework exists in this project").
9. **Convergence stop — first to reach it.** Same reasoning and same historical citation as the other
   two; #343 was the first of the three to report this stop.
10. **Human decision (applies to all three, and sets the ordering).** "Push each temp branch and merge
    it into feat/policies-http-frontend." Parent released #343 first (it had asked first), explicitly
    telling it to run the procedure "sequentially and carefully, since #342 will be doing the same merge
    shortly after you."
11. **Convergence performed by the worker itself — first mover, and the one that established the
    pattern the other two reused.** Pushed `issue-343-carrier-policies-tab`; fetched fresh (still
    `cd70cbc` — no divergence yet, since it went first); created throwaway branch
    `tmp-merge-343-into-milestone` at that tip specifically because `feat/policies-http-frontend` was
    checked out in the parent's own main worktree and it did not want to touch that shared ref/checkout;
    `--no-ff` merge (clean, `ort` strategy); targeted re-verification on the merged tree
    (`tests/Feature/Http/Carriers` + `AgentTest.php`... actually `CarrierTest.php` → 66 passed, 299
    assertions); trailer-checked the merge commit `d9bdb39`; pushed via `git push origin tmp-merge-343-
    into-milestone:feat/policies-http-frontend` → fast-forward `cd70cbc..d9bdb39`, not rejected;
    verified ancestry for all three original commits; **deleted** the local throwaway branch afterward
    ("safe; its one commit is already reachable via `origin/feat/policies-http-frontend`").
12. **Issue-closure "ask first," approval, closure, validation.** Directly confirmed via `gh issue view
    343`: `CLOSED`/`true`, 4/4 checked (this issue has 4 tasks, not 5), one closing comment naming all
    four commits including merge `d9bdb39`, the "66 passed, 299 assertions" merged-tree figure, and both
    `review-it` scope notes verbatim (the `policiesCount` addition and the route-placement precedent
    concern — see "Convergence audit").
13. **Next-issue recommendation.** #334/#344/#345 (first to report this, before #341/#342 had closed),
    explicit rationale for why it wasn't picking one, and an explicit note that #341/#342 "aren't
    genuinely available for a new pass" since they were the sibling workers.
14. **Terminal handback.**

## Independent human-gated progression

The core hypothesis under test:

```text
Worker A → waiting for implementation review
Worker B → still implementing
Worker C → waiting for commit-plan approval

human approves one worker → only that worker resumes → other workers preserve their own states
```

**Directly observed, with exact evidence:**

- At one point in the run, #343 had already reported its Review implementation (Gate 1) and was
  waiting, while #341 had separately reported a *different*, earlier stop (the full-suite question,
  before even invoking `review-it`), and #342 had not yet reported anything. The human's message at
  that point ("Skip full suite for both, approve Gate 1 for #343 and 341") did not apply uniformly:
  the parent resumed #341 with only the full-suite answer (because #341 had no Gate‑1 report yet to
  approve) and resumed #343 with both the full-suite answer *and* Gate‑1 approval (because #343's report
  already existed). This is direct evidence that the parent tracked each worker's *actual* reported
  state independently rather than broadcasting one answer to all three, and that mismatched
  instructions (a human answer that assumes a state a worker hasn't reached yet) did not cause the
  parent to fabricate a stop the worker hadn't asked for.
- Later, #342 reported Gate 1 with two coupled questions (full-suite, and the 30-day-window Gate‑1
  approval). The human's first relevant answer ("skip full suite for #342 too") answered only one of
  the two. The parent explicitly told #342: "Gate 1 itself is NOT yet approved... Hold here; do not
  proceed to Commit plan yet" — and the worker's own handback confirms it held: "Not proceeding to
  Commit plan or touching any further implementation surface until Gate 1 is explicitly approved." This
  is direct evidence the parent did not over-apply a partial human answer as full gate approval, and
  that the worker itself independently enforced the same boundary rather than assuming continuation.
- When the human approved #341's Gate 1 and #343's Commit plan in the same message at different points
  in the run, only the named worker's `SendMessage` fired each time (confirmed by the `resumedAgentId`
  field in each `SendMessage` tool result matching exactly the intended target and no other agent ID),
  and each worker's subsequent handback shows it resumed from precisely the state it had been left in
  (e.g. #341's next report was a Commit plan, not a repeat of Gate 1; #343's next report was commit
  creation + the convergence stop, not a repeat of Commit plan).
- Across the whole run, at no point did resuming one worker produce a report or state change from a
  *different* worker. Every `SendMessage` result names exactly one `resumedAgentId`.

**What this proves versus what it merely suggests:**

- **Proven, with direct evidence from this run:** three independently-launched `general-purpose`
  background agents, each running its own `implement-it` pass against a different issue, can each stop
  at a genuine human-owned decision point, remain paused indefinitely while the human deals with the
  other two, and resume correctly (and only) when addressed by name — without any custom orchestrator
  agent, Control Room skill, or worker-event protocol. `orchestration.md`'s "Human decision routing"
  and "Gate-specific worker resumption" watch items — both explicitly marked "Not observed" after Smoke
  Test 1 — are now positively observed, on this one run, on this one runtime (Claude Code's native
  `Agent`/`SendMessage`/task-notification mechanism).
- **Not proven, only suggested by one run:** that this pattern holds at higher worker counts, under
  worker contention over the same files, under a human answer that is ambiguous about *which* worker it
  targets (this run had exactly that ambiguity twice — see above — and the parent resolved it correctly
  both times, but by the parent's own judgment/context-tracking, not by any codified routing rule), or
  that it survives session interruption/recovery mid-gate (Smoke Test 1's interrupted-worker recovery
  was pre-gate workspace preservation, not gate-state recovery, and this run never tested an
  interruption at all).
- **Inference:** the parent's correct handling of the two ambiguous-target human answers above appears
  to rely on the parent session's own conversational memory of which worker had reported what, not on
  any mechanism `implement-it`/`sequencing.md` defines. This is exactly the "decision routing" behavior
  `orchestration.md` flagged as "the most orchestrator-shaped hypothesis" with "zero direct supporting
  execution evidence" before this run. It is no longer zero-evidence, but the evidence is that the
  *parent session's own reasoning* did the routing correctly, not that a mechanism exists that
  guarantees it will always be done correctly by any parent.

## Review and human approval

For each worker, in the order `review-it` actually ran relative to the full-suite decision (this is
the important axis — see "Verification" below for the full comparison):

| Worker | `review-it` ran? | Result | Included in the report shown to the human? | Explicit human approval before Commit plan? | Committed before that approval? |
|---|---|---|---|---|---|
| #341 | Yes, but only *after* the full-suite question was separately resolved first | Clean | Yes — full checklist, explicitly cited in the Review implementation report | Yes — "Approve #341" received and forwarded before the Commit plan was even requested | No — worker explicitly stated "3 verified commits" only after the human's Commit-plan approval, and the transcript shows commit creation strictly followed that approval |
| #342 | Yes, but *before* the full-suite question was resolved | Clean (one non-blocking maintainability note) | Yes — result stated in the same Gate‑1 message | Yes — separate, later, explicit "Approve #342 with a 30-day window" | No |
| #343 | Yes, but *before* the full-suite question was resolved | Clean (two non-blocking scope notes) | Yes — result stated in the same Gate‑1 message | Yes — separate, explicit "approve #343's commit plan" after Gate 1 was separately approved | No |

**Direct comparison against Smoke Test 1's failure mode** (`evidence.md`, "Human gates were bypassed"):
in ST1, neither worker surfaced Review implementation or requested approval at all — both proceeded
straight from implementation/verification to committing, and Travel skipped `review-it` entirely. In
ST2, all three workers (a) ran `review-it`, (b) included its result in a report presented to the human,
(c) explicitly stopped and waited for a human decision before deriving or creating any commit, and (d)
did not commit before that decision arrived. This is a direct, evidence-backed reversal of ST1's
specific failure — not an inference.

**UX/presentation finding (not a correctness finding):** every worker's Gate‑1/Gate‑2 report, and every
parent relay of it to the human, used internal methodology vocabulary — "Gate 1," "Gate 2," "Review
implementation," "Commit plan," rule-file names (`review-gates.md`, `push-readiness.md`), and skill
mechanics ("per `commit-boundaries.md`'s mechanical post-commit verification"). This matches the user's
own observation in this run's audit request. The parent's own relayed summaries to the human (e.g. "#343
reached Gate 1," "approve Gate 1 for #343 and 341") **also carried this vocabulary forward** rather than
translating it — this is a finding about the parent's own presentation, not only the workers'. The
preferred phrasing the human described — "Implementation review is ready. review-it found no issues.
Relevant verification passed. Please manually verify the implementation and approve when you're happy to
proceed to the commit plan." — was not what was actually shown in this run, at either the worker or
parent level. Classified as a UX/presentation finding only, per the audit's own instruction, not a skill
defect: `review-gates.md` itself already permits internal identifiers only "when precise rule references
need them," and does not mandate exposing them in the human-facing report.

## Verification

Per-worker breakdown of what actually ran, and when, relative to the full-suite decision:

**#341 (Client).**
- Targeted (pre-Gate-1, first pass): 343 passed / 1722 assertions (`Clients`, `Policies` Http; `Client
  Test`; `Client`/`PolicyPolicyTest`).
- Full-suite decision: explicitly surfaced and answered ("skip") **before** `review-it` was invoked —
  the ordering `verification.md` actually specifies.
- Post-commit, pre-convergence: 330 passed / 1683 assertions.
- Post-convergence (merged-tree, cross-cutting): 446 passed / 2273 assertions, across `Clients`,
  `Policies`, `Agents`, `Carriers` Http tests + `ClientTest.php`.
- Static/frontend: Pint, ESLint, Prettier, `vue-tsc` all clean at every stage. `npm run build` run when
  Wayfinder needed regeneration.
- **No unfiltered full project suite (`--no-tia` full run) was ever executed for #341,** at any point —
  the human decision was to skip it, and nothing later substituted a full run.

**#342 (Agent).**
- Targeted: 53 passed / 297 assertions (`Agents` Http + `AgentTest.php`), stable across every re-run
  (pre-commit, post-commit, post-convergence).
- Full-suite decision: surfaced, but **after** `review-it` had already run and its clean result was
  already part of the Gate‑1 report — the ordering deviation (see below).
- Human answer: skip.
- **No unfiltered full project suite was ever executed for #342.**

**#343 (Carrier).**
- Per-commit targeted: `PoliciesIndexTest.php` 5/36; `ShowTest.php` 5/23.
- Full-suite decision: surfaced **after** `review-it` had already run and reported clean — same
  deviation as #342.
- Human answer: skip.
- Post-convergence (merged-tree): `tests/Feature/Http/Carriers` + `CarrierTest.php` → 66 passed / 299
  assertions.
- **No unfiltered full project suite was ever executed for #343.**

**The ordering inconsistency, verified from the transcripts as quoted above:** #341 stopped for the
full-suite decision *before* invoking `review-it` (matching `verification.md`'s literal requirement that
the choice be "surfaced and answered **before** `review-it` or Review implementation" is reported).
#342 and #343 both invoked `review-it` and built a complete Gate‑1 report *first*, then surfaced the
full-suite question as an appendix to that same report.

**What this indicates, per the audit's own instruction not to propose a fix without clear evidence:**
This is evidence of **ambiguous execution under real conditions**, not a single worker's isolated
mistake — two of three independently-launched workers, with no shared context, converged on the same
deviation from the third. That two-out-of-three pattern is stronger evidence of an ordering ambiguity
somewhere upstream (either in how `verification.md`'s ordering requirement was actually worded/found
by each worker, or in how each worker's own task briefing paraphrased it) than of an isolated execution
error by one worker. This audit does not have direct access to each worker's own reading of
`verification.md`'s exact text at the moment it made this choice (that would require reading the raw
JSONL transcripts, which this audit was instructed not to do), so it cannot fully distinguish "the rule
text itself is ambiguous" from "each worker's paraphrased task briefing described the ordering less
precisely than the rule does." **This is recorded as an open question, not resolved here — see "What
remains unknown."**

## Convergence

All three workers independently reached the identical stop, citing the identical rule language
(`sequencing.md`: "This rule does not define how or when that convergence happens... not a decision this
rule makes on its own") and the identical class of supporting evidence (this repo's own prior
sequential-issue merge pattern — `Merge issue-354-...`, `Merge issue-355-...`, `Merge issue-352-...`, "
`Merge issue-351-...`, etc.) — all three independently found and cited via `git log --all --oneline`,
without prompting from the parent to look for it.

**Who performed convergence — established directly, not inferred:** each **original worker** was
resumed (via `SendMessage` to its existing agent ID — `a45052861002f76d7`, `af568be37d36d15ee`,
`ab013dbcd10f9fc5e`) and performed its own push and merge itself, inside its own existing worktree. No
fresh agent was created for convergence, and the parent session did not perform any merge or push
directly. This is a direct, load-bearing difference from Smoke Test 1, where `evidence.md`'s "Parent-
session branch behavior" and "Parent-session post-worker behavior" sections record the **parent**
inspecting worker branches and running `git merge --no-ff` itself.

**The human's convergence decision, and how the parent applied it:** "Push each temp branch and merge it
into feat/policies-http-frontend." The parent applied this decision to all three workers uniformly, but
serialized the actual execution rather than telling all three to proceed simultaneously — explicitly
reasoning (in its own messages to the workers) that concurrent pushes/merges to the same shared branch
would race. The order used was #343 → #342 → #341, determined by **arrival order** (whichever worker had
already asked the convergence question first was released first), not by issue number or any other
rule. Each subsequent worker was explicitly told the milestone tip had moved and given the SHA it had
moved to, and each was pointed at the immediately-preceding worker's own throwaway-branch technique as a
pattern to reuse.

**Did the parent need to know cross-worker/shared-branch state to do this safely? Yes, directly
evidenced:** the parent's own messages to #342 and #341 explicitly named the exact current tip
(`d9bdb39`, then `6db2167`) *before* that worker had fetched it itself, and explicitly told #341 to hold
"because #343 and #342 are doing this same merge shortly after you." This is parent-session reasoning
that required visibility across all three workers' states simultaneously — no single worker, and no
worker skill, has or needs that visibility for its own issue.

**What each worker verified before mutating shared state:** every worker, before pushing its
merge, (a) fetched `origin/feat/policies-http-frontend` fresh rather than trusting a previously-known
SHA, (b) ran its own targeted test scope against the merged (not just its own) tree, and (c) ran the
mechanical trailer re-check against the merge commit specifically, individually rather than
concatenated. All three pushes landed as fast-forwards (`cd70cbc..d9bdb39`, `d9bdb39..6db2167`,
`6db2167..e118e5b`) — none were rejected, and no merge conflict occurred (directly confirmed: `git log
--all --oneline --graph` on the actual repository, reproduced below, shows a clean, conflict-free
three-way convergence with no repeated/duplicate commits and no orphaned branch tips).

```text
*   e118e5b Merge issue-341-client-policies-tab into feat/policies-http-frontend
|\
| * a24473a Enable the Add-policy action, pre-filling the client on the create page
| * 2552f43 Pass the client's actual policy count to the Client show page
| * 2f45229 Add the client-scoped policies endpoint and wire up the Policies tab
* |   6db2167 Merge issue-342-agent-policies-tab into feat/policies-http-frontend
|\ \
| * | 129e430 Surface real policy counts and renewing-soon policies on the Agent overview
| * | 038f0ab Wire the Agent show page's Policies tab to a real listing endpoint
| |/
* |   d9bdb39 Merge issue-343-carrier-policies-tab into feat/policies-http-frontend
|\ \
| |/
|/|
| * 3a023db Feed the carrier's real policy count into the show page
| * b23ea48 Wire the Carrier show page's Policies tab to the new endpoint
| * c4d7d37 Add an endpoint listing a carrier's policies
|/
*   cd70cbc Merge issue-354-policies-life-pages into feat/policies-http-frontend
```

**Unexpected finding — the main checkout's own local branch was left stale.** Directly confirmed by
this audit: after all three convergences, the *local* `feat/policies-http-frontend` ref in the parent
session's own main working directory (`/Users/elieandraos/Desktop/Code/useOrbit`) was still at `cd70cbc`
— unchanged. Only `origin/feat/policies-http-frontend` (the remote ref) advanced to `e118e5b`. This is a
direct consequence of every worker deliberately avoiding a `git checkout feat/policies-http-frontend` in
its own worktree (to not disturb the branch checked out in the main worktree) and instead pushing
straight to the remote ref via `git push origin <throwaway>:feat/policies-http-frontend`. This worked
correctly for the workers' own purposes, but it means anyone (or anything) operating against the *local*
`feat/policies-http-frontend` branch in the main checkout — without first running `git fetch` — would see
stale, pre-convergence state. No rule or worker flagged this side effect; it was found only by this
audit's own direct `git rev-parse feat/policies-http-frontend` vs. `git rev-parse
origin/feat/policies-http-frontend` comparison.

**A second unexpected finding — real architectural drift from parallel execution with no merged
precedent to check against.** Directly confirmed by inspecting the actual merged route files:
`clients.policies.index` landed in `routes/policies.php` (grouped by the *sub-resource domain*, matching
this repo's own existing `documents.php`/`notes.php` precedent, where e.g. `clients.documents.index`
lives in `routes/documents.php`, not `routes/clients.php`). `agents.policies.index` and
`carriers.policies.index` instead landed directly inside `routes/agents.php` and `routes/carriers.php`
respectively (grouped by the *owning entity*, matching a different existing precedent —
`carriers.branches.*` inside `routes/carriers.php`). Both are individually defensible against real,
pre-existing conventions in this codebase — but the three parallel workers picked two different,
inconsistent conventions from each other, because at the time each one implemented, the other two
issues' route placement wasn't merged yet to check against. #343's own closing comment explicitly
flagged this as worth checking once #341/#342 landed ("Worth checking once #341/#342 land that all three
nested-route placements ended up consistent with each other") — and, verified directly against the final
merged state, they did **not** end up consistent. No worker, and no human decision in this run, actually
performed that follow-up check or correction.

## Post-convergence verification

Exact reconstruction of the "446 tests" figure, per the audit's specific instruction:

- **Command and scope:** `php artisan test --compact` against `tests/Feature/Http/Clients`,
  `tests/Feature/Http/Policies`, `tests/Feature/Http/Agents`, `tests/Feature/Http/Carriers`, and
  `tests/Feature/Models/ClientTest.php` — a targeted, cross-cutting selection chosen by the #341 worker
  itself, not the unfiltered full suite (`--no-tia` full run was never invoked at this point).
- **When:** run by the #341 worker (`a45052861002f76d7`), *during its own convergence step*, after it
  had created its local throwaway branch `converge-issue-341` at the milestone tip and merged its own
  branch into that throwaway branch — i.e., after the merge, before the push.
- **Repository state at that moment:** the milestone tip #341 merged onto was `6db2167` — which already
  contained **both** #343's merge (`d9bdb39`) and #342's merge (`6db2167` itself). So by the time this
  test run happened, #342 and #343 were already fully converged and pushed to `origin/feat/policies-
  http-frontend`; only #341's own changes were still pending, on top, in a local, not-yet-pushed
  throwaway branch.
- **What it therefore verified:** the combined code of all three issues (#341+#342+#343) together,
  content-wise equivalent to the final `e118e5b` state — but via a curated, worker-chosen subset of
  feature tests, not the project's full regression suite, and not yet the actual pushed/final ref (the
  push happened immediately after, and landed as a clean fast-forward with no further changes).

**What #342 and #343 ran after their own convergence, for comparison:** #343 ran `tests/Feature/Http/
Carriers` + `CarrierTest.php` (66/299) against its own merged tree at the moment it converged (tip
`d9bdb39` — at that point containing only #343 on top of the pre-existing milestone state; #341/#342 had
not converged yet). #342 ran `tests/Feature/Http/Agents` + `AgentTest.php` (53/297, unchanged from its
pre-convergence numbers) against its own merged tree at `6db2167` — containing #343 and #342, not yet
#341.

**Direct answer to the key question:** No. **Smoke Test 2 never presented one explicit human full-
suite/skip decision against the truly final combined milestone branch state, after all three workers
had converged.** Each worker's full-suite question was asked and answered separately, per-issue, before
that issue's own commits even existed — not re-asked, and not asked once collectively, after
convergence. The #341 worker's "446 passed" run is the closest thing to combined verification that
occurred in this run — it is real evidence, run against code equivalent to the final state — but it was
a targeted subset a single worker chose unilaterally as part of its own per-issue convergence procedure,
not a combined-verification decision presented to the human, and not the unfiltered full project suite.
This audit does not reinterpret it as either.

## Push and issue closure

For each issue, directly confirmed against live GitHub state via `gh issue view <n> --json state,closed,
body,comments`:

| Issue | Push authorization followed lifecycle? | Issue closure followed lifecycle? | Human explicitly authorized closure? | Task checkboxes updated? | Closing comment produced? | State validated afterward? | Commit reachability verified? |
|---|---|---|---|---|---|---|---|
| #341 | Yes — worker stopped at push-readiness's ambiguity, held for the human's convergence decision, then itself ran the fetch/reachability/trailer-recheck sequence before and after pushing | Yes — "ask first," explicit human "Close #341" received before any mutation | Yes | Yes — 5/5 checked (confirmed) | Yes — confirmed, names all 4 SHAs | Yes — worker re-fetched; this audit independently re-confirmed `CLOSED`/`true` | Yes — `git merge-base --is-ancestor` run for all 4 commits |
| #342 | Yes, same pattern | Yes, same pattern | Yes | Yes — 5/5 checked (confirmed) | Yes — confirmed, names 3 SHAs + the renewal-window note | Yes — independently re-confirmed | Yes |
| #343 | Yes, same pattern | Yes, same pattern | Yes | Yes — 4/4 checked (confirmed; this issue has 4 tasks, not 5) | Yes — confirmed, names 4 SHAs + both `review-it` scope notes | Yes — independently re-confirmed | Yes |

**Direct comparison against Smoke Test 1's specific failure** (`evidence.md`: "the issue task checkboxes
remained unchecked even though the issues were closed"): in ST2, all three issues closed with every
completed task checkbox actually checked, and this audit independently re-verified that against live
GitHub state rather than trusting any worker's or the parent's self-report. This is a direct, confirmed
reversal of ST1's specific regression — not an inference.

**No remaining mismatch found** between the installed `issue-closure.md`/`push-readiness.md` procedures
and what actually happened, for any of the three issues, based on the direct GitHub/git evidence
gathered for this audit.

## Responsibility classification

| Action observed | Classification | Evidence |
|---|---|---|
| Launching 3 parallel background agents in isolated worktrees | Native Claude Code runtime | `Agent` tool calls with `isolation: "worktree"`, one message, three tool uses |
| Each worker's own implement→verify→review-it→gate→commit lifecycle | Worker / `implement-it` | Per-worker handbacks, Parts above |
| Cutting a temporary issue branch from the milestone branch | Existing skill responsibility (as of the two-file patch) | `sequencing.md`'s new "Parallel workers" section, applied identically by all three workers unprompted beyond the task briefing |
| Presenting each worker's stop to the human, tracking which worker asked what | Parent-session reasoning | The two ambiguous-target-answer episodes above — resolved by the parent's own conversational tracking, not a rule |
| Routing a human answer to the correct, specific worker | Parent-session reasoning, executed via native runtime (`SendMessage`) | Every `SendMessage` result's `resumedAgentId` matches the intended target exactly |
| A worker resuming only from its own last-reported state | Native Claude Code runtime (agent resume-from-transcript) + worker/skill (re-validating the resumed state per `review-gates.md`'s "Approval validity") | Each worker's post-resume report picks up exactly where its prior report left off |
| Deciding the convergence policy itself (push+merge into milestone branch) | Human decision (explicitly, not delegated to any skill or the parent) | User's literal instruction |
| Serializing convergence order and telling each worker the milestone tip's current SHA | Parent-session reasoning — required cross-worker/shared-branch visibility no single worker has | Parent's explicit "hold, #343/#342 are converging first" messages, and explicit SHA hand-offs |
| Actually performing each push/merge | Worker / `implement-it`-adjacent procedure, executed in the worker's own worktree (not the parent, not a fresh agent) | `SendMessage` targets were the original agent IDs; each worker's own handback describes running the git commands itself |
| Choosing the throwaway-branch technique to avoid touching the shared checkout | Worker judgment, first established by #343, explicitly reused (by parent instruction) by #342 and #341 | #343's own reasoning in its handback; parent's messages telling #342/#341 to "reuse #343's approach" |
| Combined-state verification after full convergence | **Unowned gap** — partially and incidentally satisfied by #341's own unilaterally-chosen targeted re-run, never as a deliberate human-facing combined decision | "Post-convergence verification" section above |
| Whether the main checkout's local branch needed updating after convergence | **Unowned gap** — not surfaced by any worker, the parent, or any rule | Direct `git rev-parse` comparison in this audit |
| Route-placement consistency across the three parallel surfaces | **Unowned gap** — flagged as a risk by #343's own closing comment, never actually checked or reconciled by anyone | Direct route-file inspection in this audit |
| Issue closure and its validation | Existing skill responsibility (`issue-closure.md`), executed correctly by each worker | Confirmed live-GitHub state per issue |
| Next-issue recommendation | Existing skill responsibility (`sequencing.md`'s recompute) | Each worker's own final report |

## Smoke Test 1 → Smoke Test 2

| Dimension | ST1 (#354/#355) | ST2 (#341/#342/#343) | Classification |
|---|---|---|---|
| Parallel worker launch | ✓ (2 workers) | ✓ (3 workers) | Fixed/validated (repeated, scaled by one) |
| Isolated worktrees | ✓ | ✓ | Fixed/validated |
| Independent worker contexts | ✓ | ✓ | Fixed/validated |
| Human verification (full-suite) decision | ✗ — both workers decided unilaterally, no ask | ✓ — asked and answered per issue, every time | **Fixed** |
| `review-it` invoked | Life: yes; Travel: no | All three: yes | **Fixed**, but see ordering note below |
| Review implementation surfaced + approved | ✗ neither worker | ✓ all three, each with explicit human approval | **Fixed** |
| Commit plan surfaced + approved | ✗ neither worker | ✓ all three, each with explicit human approval | **Fixed** |
| Worker-specific pause/resume, independent of siblings | Not exercised (no worker reached a gate) | ✓ directly observed, including two ambiguous-target cases resolved correctly | **New finding — first positive evidence** |
| Commits created before approval | Both workers committed unilaterally | None did — confirmed strictly post-approval for all three | **Fixed** |
| Convergence mechanics | Parent performed `git merge --no-ff` directly, itself | Each original worker performed its own push+merge, resumed by the parent | **New finding** — convergence moved from parent-performed to worker-performed once workers were told to stop and ask |
| Convergence serialization | Not applicable (parent did it sequentially by construction, as a single actor) | Explicitly serialized by parent instruction to avoid a shared-branch race between three independent workers | **New finding** — this coordination need only exists because convergence is now worker-performed, not parent-performed |
| Post-convergence verification | ✗ "did not verify the final combined branch after both worker branches had been merged" | Partially — #341's own 446-test run covers the true final combined code, but as an unplanned side effect, not a deliberate combined decision | **Repeated finding** — still not a deliberate, human-facing combined verification |
| Push (mechanics/validation) | Parent pushed directly, bypassing `push-readiness.md` | Every worker ran `push-readiness.md`'s reachability/trailer-recheck itself, before and after pushing | **Fixed** |
| Issue closure procedure | Bypassed — parent closed directly outside `implement-it`/`ship-it` | Each worker ran `issue-closure.md`'s "ask first" → closing recipe → validation itself | **Fixed** |
| Issue task checkbox completion | ✗ both issues closed with checkboxes still unchecked | ✓ all three closed with checkboxes correctly checked, independently re-verified | **Fixed** |
| Worker recovery from interruption | ✓ observed once (workspace/branch preservation, pre-gate) | Not exercised at all in ST2 | Not exercised |
| Next-work recommendation | Not reached (issues closed by parent, not through the recompute step) | ✓ all three workers independently recomputed and recommended, converging on the same open set | **New finding** |

## Orchestration evidence

Revisiting `orchestration.md`'s watchlist against this run's actual evidence — no orchestrator design
is proposed here, per the audit's own instruction.

**Human decision routing (human answer → correct waiting worker).**
- ST1 evidence: none — no worker ever reached a gate.
- ST2 evidence: positive, direct, and including two non-trivial ambiguous cases (partial/mismatched
  human answers correctly resolved per-worker by the parent). See "Independent human-gated
  progression."
- Necessary after the parallel-aware skill correction? Yes — nothing in `sequencing.md`'s two-file patch
  addresses this; it is purely a parent-session behavior.
- Inherently cross-worker? Yes — a worker cannot route a human answer to itself or a sibling; only
  something with visibility across all workers' current states can.
- Currently handled adequately by the parent? On this one run, yes, including under ambiguity — but the
  mechanism was the parent's own conversational memory, not a rule or a data structure that guarantees
  correctness at higher worker counts or across a session restart.
- More evidence needed before extraction? **Yes.** One run, two ambiguous cases, both resolved
  correctly by an unaided parent, is meaningfully stronger evidence than ST1's zero, but `orchestration.md`'s
  own extraction bar requires recurrence across waves — this is the second wave, and the first time this
  specific responsibility was exercised at all.

**Convergence sequencing/serialization.**
- ST1 evidence: none directly — ST1's "convergence" was the parent doing both merges itself, sequentially,
  as a single actor; there was no serialization *decision* to make.
- ST2 evidence: positive and explicit — the parent recognized a genuine race risk across three
  independently-acting workers converging onto one shared branch, decided an order (arrival order, not
  issue-number order or any other rule), and explicitly communicated the moving target SHA to each
  subsequent worker.
- Necessary after the skill correction? Yes — `sequencing.md`'s patch deliberately leaves this
  unspecified by design.
- Inherently cross-worker? Yes, directly confirmed — each worker needed to be told the *other* workers'
  progress and the shared branch's current SHA, information no worker skill gives it.
- Currently handled adequately by the parent? Yes, on this run — zero conflicts, zero rejected pushes.
- More evidence needed? Yes — this run's three workers were file-disjoint by construction (per
  `parallel-dry-run.md`'s own selection criteria); a real file-overlap or conflict case was still not
  exercised, exactly as `parallel-dry-run.md` predicted it wouldn't be.

**Combined-state verification.**
- ST1 evidence: gap — never performed at all.
- ST2 evidence: gap, but a subtler one this time — never performed *as a deliberate decision*, but
  incidentally, mostly satisfied by #341's own unilateral choice of test scope during its own
  convergence step.
- Necessary after the skill correction? Yes — the patch explicitly declined to define this (per
  `parallel-dry-run.md`'s review history, a combined-verification clause was drafted into
  `verification.md` and deliberately removed before this run).
- Inherently cross-worker? Yes — by definition, verifying the union of three workers' changes requires
  knowing all three exist and have converged.
- Currently handled adequately by the parent? **No** — the parent never surfaced a "here's what each
  worker already proved, do you want to run/skip the full suite against the combined branch" decision at
  all, in either direction. This is the clearest remaining gap in the whole run.
- More evidence needed? This is now the second run in which this exact gap recurred in the same shape
  (present, unowned, never explicitly decided). `orchestration.md`'s "recurs across waves" extraction
  criterion is arguably now met for *this specific responsibility* more than for any other candidate —
  but whether it should be extracted to a new place, or simply made an explicit step the parent is told
  to always perform (a smaller fix than extraction), is not resolved by this evidence alone.

**Concurrent-safe issue selection.**
- ST1 evidence: observed once (disjoint files, parent judgment).
- ST2 evidence: not exercised by the run itself — the wave (#341/#342/#343) was pre-selected before this
  audit's session began (visible from `parallel-dry-run.md`, which already did this selection work as a
  dry run before the actual run happened), so this run does not add a second independent data point for
  *how* the selection judgment gets made, only confirms the same three issues were in fact file-disjoint
  in practice (zero conflicts occurred).
- Still: not enough recurrence to extract; still a human/parent judgment call each time, per
  `orchestration.md`'s original framing, unchanged by this run.

**Next-work recommendation.**
- Handled entirely by the existing skill (`sequencing.md`'s recompute), independently by all three
  workers, converging on an identical, correct answer (#334/#344/#345) each time. Not a cross-worker
  responsibility at all — each worker only needed live GitHub state, not knowledge of its siblings.
  **Should clearly remain in the worker skill, not be extracted.**

**What should clearly remain in skills, not be extracted, per this run's evidence:** the entire
per-issue `implement-it` lifecycle (implementation, verification, `review-it`, both gates, commit
mechanics, push-readiness mechanics, issue-closure mechanics, next-issue recompute) worked correctly,
unchanged, run three times concurrently, with zero evidence that any of it needs to move up a level.
This matches `orchestration.md`'s own "Existing lifecycle policy" boundary and this run adds no reason to
revisit it.

## Skill findings

**Existing rules confirmed sufficient (no change indicated by this run):**
- `review-gates.md` — both approvals held, across all three workers, with no commit created before
  explicit approval. `parallel-dry-run.md`'s prediction that the ST1 gate bypass was a delegation-prompt
  problem, not a rule gap, is directly confirmed by this run's correct behavior under a corrected
  delegation prompt with the rule text itself unchanged.
- `push-readiness.md` — its branch-identification step, applied by each worker after convergence had
  already happened by whatever means, resolved correctly with no clause needed about the temporary-
  branch detour, exactly as `parallel-dry-run.md` predicted.
- `issue-closure.md` — its "ask first," closing recipe, and validation steps ran correctly, independently,
  three times, with checkbox completion directly confirmed on live GitHub state.
- `sequencing.md`'s recompute step — ran correctly and identically across all three workers.

**Candidate rule correction with evidence:**
- None of the four conservative files (`review-gates.md`, `verification.md`, `push-readiness.md`,
  `issue-closure.md`) show evidence in this run that they need changing. The one file that *was* changed
  before this run (`sequencing.md`'s parallel-worker addition) performed exactly as designed: it made
  concurrent worktrees possible without specifying anything beyond that, and every worker correctly
  treated the undefined convergence mechanics as a stop rather than guessing.

**Execution mistake / rule not followed:**
- The `review-it`-before-full-suite-decision ordering deviation in #342 and #343 (see "Verification").
  This is recorded as a real deviation from `verification.md`'s stated ordering, observed in two of
  three independent workers — but this audit cannot determine from the evidence available to it (the
  conversation record and git/GitHub state, not the raw per-worker transcripts) whether the deviation
  traces to the rule's own text being read ambiguously, or to each worker's task briefing describing the
  ordering imprecisely, or to independent worker error. Recorded as unresolved, not attributed.

**Cross-worker responsibility — do not put into a worker skill yet:**
- Convergence serialization/sequencing, human decision routing, and combined-state verification — all
  three, per "Orchestration evidence" above, are cross-worker by nature and were exercised only by the
  parent session's own judgment in this run. None should be pushed into `implement-it`'s per-issue rules,
  which have no visibility into sibling workers.

**UX/presentation finding:**
- Internal gate/rule vocabulary ("Gate 1," "Gate 2," rule filenames) surfaced in every worker report and
  in the parent's own relayed summaries, rather than the plain-language phrasing the human described as
  preferred. See "Review and human approval" above for the exact comparison.

## UX findings

Consolidated from above, kept separate per the required document structure:

1. Worker reports consistently used internal identifiers (Gate 1/Gate 2, rule filenames like
   `review-gates.md`/`push-readiness.md`, mechanism names like "mechanical trailer re-check") in the
   text actually shown to the human, rather than plain statements of what was checked and what decision
   is needed.
2. The parent's own relayed summaries to the human carried this vocabulary forward rather than
   translating it (e.g., "reached Gate 1," "approve Gate 1 for #343 and 341").
3. When a human answer only partially matched what a worker had actually asked (the two cases in
   "Independent human-gated progression"), the parent correctly avoided over-applying it — but this
   required the parent to notice the mismatch itself; nothing in the worker's own report format flagged
   "this answer doesn't fully cover what I asked" back to the parent or the human.
4. Convergence housekeeping was inconsistent across workers with no human-visible consequence in this
   run but a latent one: #341 and #343 deleted their throwaway merge branches after confirming
   reachability; #342 left `merge-issue-342` in place, citing an observed precedent
   (`merge-issue-332`/`merge-issue-333`) from non-parallel, single-worker milestone history. Neither
   choice was surfaced to the human as a decision; both are currently silent, worker-level judgment
   calls.

## What remains unknown

Carried forward from `parallel-dry-run.md`'s own "Unknowns" list, marked against what this run actually
answered:

- **Who performs convergence and when** — **answered**: the original worker, resumed, performing its
  own push+merge in its own worktree; timing is whenever the human authorizes it, serialized by the
  parent to avoid a race.
- **Whether combined verification is decided at all, and how** — **partially answered, negatively**:
  it was not decided as a deliberate step; it was incidentally, partially satisfied by one worker's own
  unilateral choice.
- **Whether `push-readiness.md`/`issue-closure.md` work unmodified after convergence** —
  **answered, yes**, for all three issues, directly confirmed against live GitHub state.
- **Merge-conflict handling during convergence** — **still unanswered**: zero conflicts occurred in this
  run, by construction (the three issues were selected for file-disjointness before the run).
- **Whether human decision routing is actually difficult or trivial** — **answered, on this run,
  "trivial for the parent, but not mechanism-backed"**: it worked, including under two ambiguous cases,
  entirely through the parent's own conversational tracking rather than any codified routing logic.
- **Whether a resumed worker re-validates its approval per `review-gates.md`'s "Approval validity"
  section** — not directly exercised: no worker in this run resumed into a state where its scope or diff
  had materially changed between report and resumption, so the re-validation logic's actual behavior
  under a genuine staleness case remains unobserved.
- **Whether leaving convergence and combined verification unowned reproduces ST1's ad hoc parent
  improvisation cleanly, or differently** — **answered: differently, and better in one dimension**
  (convergence moved from parent-performed to worker-performed) **but the same in another**
  (combined verification remains genuinely absent as a deliberate decision, in both ST1 and ST2).
- **Whether repeated waves make any of this recur enough to justify codifying** — this is now two waves
  showing the same combined-verification gap in the same shape; still short of the "recurs across
  waves" bar as an absolute matter, but the strongest repeated signal of the run.
- **New unknowns surfaced by this run specifically, not anticipated by `parallel-dry-run.md`:** the
  stale-local-branch side effect of the throwaway-branch convergence technique; the real (not merely
  hypothetical) route-placement inconsistency across the three parallel surfaces; and the ordering
  deviation between `review-it` and the full-suite decision in two of three workers.
- **Not exercised at all in this run:** worker interruption/recovery mid-gate; a genuine file-overlap or
  merge conflict during convergence; a worker count beyond three; a human answer given while a worker
  was mid-execution (all human answers in this run arrived while the targeted worker was already
  paused).

## Conclusion

Answering the twelve questions directly, from the evidence above:

1. **Did the two-file candidate patch enable a correct parallel worker experiment?** Yes. The only
   structural change needed — a per-worker temporary branch, milestone branch as eventual convergence
   target, convergence mechanics left undefined — was sufficient to make three concurrent `implement-it`
   passes runnable at all, with no other rule requiring modification.
2. **Did independent human-gated `implement-it` lifecycles work concurrently?** Yes, for all three
   workers, across both approval gates, with `review-it` run and its result included in every report,
   and no commit created before its matching approval — a direct, confirmed reversal of Smoke Test 1's
   specific gate-bypass failure.
3. **Did worker-specific decision routing/resumption work?** Yes, including under two genuinely
   ambiguous human answers that did not cleanly map to one worker's exact state — both were resolved
   correctly. This is now positive evidence where `orchestration.md` previously had none, but it is
   evidence of the parent session's own reasoning succeeding once, not of a guaranteed mechanism.
4. **Did convergence emerge as genuinely cross-worker behavior?** Yes, and more specifically than
   before: the *performance* of convergence turned out to be worker-owned (each worker merged and pushed
   its own branch), while the *sequencing/serialization* of convergence across workers, and the
   propagation of the shared branch's moving tip, was genuinely parent-only reasoning that no worker
   skill could have supplied.
5. **Was final combined verification correctly handled?** No. This is the clearest unresolved gap:
   no explicit human full-suite/skip decision was ever presented against the truly final, fully-
   converged milestone branch. What exists instead is one worker's own incidental, targeted re-test of
   code equivalent to the final state — real evidence, but not a deliberate combined-verification
   decision.
6. **Did push/issue closure work correctly?** Yes, for all three issues, independently confirmed against
   live GitHub state — commits reachable, checkboxes actually checked, closing comments present and
   accurate, state validated. A direct, confirmed reversal of Smoke Test 1's specific closure failure.
7. **What repeated responsibilities are now credible orchestration candidates?** Combined-state
   verification (recurred, unowned, in both ST1 and ST2, in slightly different shapes) and, newly,
   convergence serialization/human-decision-routing (both positively exercised for the first time in
   this run, but only once). None yet clear the "recurs across multiple waves with the skill corrections
   already in place" bar `orchestration.md` sets — this run adds real evidence, not a second confirmed
   recurrence for most candidates.
8. **What should we change BEFORE another smoke test?** Nothing in the four conservative files
   (`review-gates.md`, `verification.md`, `push-readiness.md`, `issue-closure.md`) — this run is direct
   evidence they work unchanged. If anything is changed, the strongest evidence-backed candidates are:
   (a) resolving the `review-it`-before-full-suite ordering ambiguity that two of three workers hit
   independently, and (b) deciding — deliberately, not by omission — whether combined-state verification
   should become an explicit, always-asked step somewhere in the existing lifecycle (not necessarily a
   new orchestrator), given this is now its second unowned occurrence.
9. **What should we deliberately NOT change yet?** Convergence mechanics beyond what already exists
   (worker-performed push+merge, parent-serialized ordering) — this run's zero-conflict, zero-rejected-
   push result does not yet cover a real overlap case, and codifying a procedure now would be guessing
   ahead of that evidence. Also: do not extract a decision-routing or convergence-serialization
   mechanism into a new orchestrator component yet — one successful run under favorable (file-disjoint,
   no-interruption) conditions is not the recurrence `orchestration.md` requires.
10. **Is there now enough evidence to begin planning an orchestrator/skills responsibility split, or
    should we run another skill-level experiment first?** Based on this evidence, another skill-level/
    parallel-execution experiment first — specifically one that deliberately exercises what this run
    could not by construction: real file overlap or a merge conflict during convergence, a worker
    interruption mid-gate, and an explicit test of whether a deliberate combined-verification step
    (however lightly specified) closes the one gap that has now recurred twice. Extraction planning
    before that would be building on two data points where `orchestration.md`'s own bar asks for
    repeated, stable recurrence.
