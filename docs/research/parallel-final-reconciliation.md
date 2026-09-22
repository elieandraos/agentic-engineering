# Parallel Implementation — Final Reconciliation

Status: Decision input for publication. This document reconciles Smoke Tests 1–3
(`smoke-test-1.md`, `smoke-test-2.md`, `smoke-test-3.md`), the mechanism investigation
(`combined-candidate.md`, `parallel-dry-run.md`, `parallel-dry-run-2.md`), and the responsibility
analysis (`responsibility-boundaries.md`, `orchestration.md`, `vision.md`) into one final position,
against ten explicit decisions the human made after Smoke Test 3. It proposes an exact, unapplied
skill diff and states what remains before publication. No skill file, useOrbit file, or GitHub state
was changed to produce this document. The smoke-test evidence documents are unchanged.

## Purpose

Three real parallel-implementation waves have now run. The question this document answers is not
"what should we try next" but "what does the accumulated evidence actually settle, what does it leave
open, and what is the smallest resulting change to canonical methodology" — so that publication work
(README, version, release) has a single, coherent input to work from instead of five documents in
different states of supersession.

## Evidence base

Read in full for this reconciliation: `vision.md`, `smoke-test-1.md`, `smoke-test-2.md`,
`smoke-test-3.md`, `parallel-dry-run.md`, `parallel-dry-run-2.md`, `combined-candidate.md`,
`responsibility-boundaries.md`, `orchestration.md`, and the canonical skill text on this branch
(`skills/implement-it/rules/{sequencing,verification,review-gates,worktree-preservation,
issue-closure,push-readiness,commit-boundaries}.md`, `skills/implement-it/rules/
companion-activation.md`).

**A load-bearing fact this reconciliation depends on, confirmed directly before writing anything
else:** the canonical `implement-it` skill on this branch *already contains* the full ST2+ST3
candidate patch as committed text — `sequencing.md`'s "Parallel workers in a delivery/phase
milestone" section, `worktree-preservation.md`'s worktree-vocabulary note, `verification.md`'s
"Concurrent workers in a parallel wave" section, and `review-gates.md`'s matching concurrent-wave
paragraph in "Review implementation" all exist as real commits (`git log`: `ac7e401` and earlier).
This is *not* the uncommitted, worktree-invisible state Smoke Test 3 exercised in useOrbit — that was
specific to useOrbit's own working tree at the time. On this branch, the propagation problem
Smoke Test 3 found does not apply to the baseline this document proposes further changes against.

Where the three smoke tests conflict with an earlier hypothesis, the smoke tests are treated as
stronger evidence, per the request. Where a smoke test conflicts with another smoke test (the
convergence-performer question), the conflict is recorded as unresolved, not silently resolved by
picking a majority.

## Final decisions

The ten decisions in the request are treated as settled inputs, not re-litigated. Restated compactly,
with the reconciliation each one drives:

1. **Parallel worker verification** — no per-worker full-suite ask, no Review implementation, no
   Commit plan, no commit; serial path unchanged. Already the canonical text. No change needed.
2. **Wave-ready checkpoint** — parent presents compact, substantive worker/`review-it` evidence once
   all workers are candidate-ready. Presentation/orchestration; not encoded in `implement-it`.
3. **One combined full-suite run/skip decision** — supersedes the prior "mandatory, not a run/skip
   choice" research position. The human makes one wave-level run/skip decision, not per worker;
   RUN requires success before Review implementation; explicit SKIP satisfies the same prerequisite.
   **Drives a real skill hunk** (see below) — the canonical text currently reads as if only a
   successful run satisfies the concurrent-worker Gate 1 prerequisite.
4. **Combined candidate stays disposable** — already the invariant `combined-candidate.md`
   establishes; no skill file encodes mechanism, so nothing to change there.
5. **Exact Git mechanism is not portable methodology** — confirms no skill change; drives a
   `combined-candidate.md` update (the mechanism's own description needs the corrected capture
   procedure, and the fact that ST3 succeeded with a looser mechanism only under file-disjoint
   conditions needs recording as evidence, not as validation of the looser mechanism).
6. **Convergence timing is not a launch prerequisite** — becomes relevant only once durable approved
   commits exist. **Drives a real skill hunk** in `sequencing.md`.
7. **Sequential convergence is normal mechanical progression** once durable commits exist, stopping
   only for a genuine unsafe/ambiguous condition. **Drives the same `sequencing.md` hunk as #6.**
8. **Worker lifecycle ownership after convergence** — the parent coordinates, it does not impersonate;
   convergence/push/closure stay worker-executed procedures. `issue-closure.md` itself needs no
   change (confirmed below); **the performer fact belongs in the same `sequencing.md` hunk as #6/#7**,
   since that is the file that already owns "who does what" for a parallel worker's convergence.
9. **Closing comments in parallel execution** — provenance is additive, not a replacement for the
   normal record. Already correctly specified; the repaired #334/#344/#345 records are the evidence
   this already works when the procedure is actually followed. No skill change.
10. **Human-facing presentation** — decision-oriented, not event-oriented; internal vocabulary hidden
    from the human. Explicitly Control Room/parent territory; not encoded in worker skills.

Two further decisions in the request are runtime/process findings, not methodology, and drive no
skill change: **worker bootstrap cost** (11) and **candidate-skill propagation** (12) — both are
recorded in `orchestration.md`/`combined-candidate.md` as findings, and the request is explicit that
"paste rule text into worker prompts" must not become permanent methodology to compensate for an
experimental uncommitted installation. Since this branch's canonical skill is already committed
(see above), decision 12's actual trigger condition does not even apply here going forward — it
matters only while a *candidate* patch is still uncommitted in a consuming project's own working tree,
which is a one-time installation-window risk, not a standing property of the methodology.

## Final parallel lifecycle

The complete lifecycle after this reconciliation, in plain technical English:

```text
Human authorizes N dependency-ready issues to run concurrently in one milestone.
        │
        ▼
Each issue becomes an isolated worker (isolated worktree, temporary branch cut from
the milestone branch) — no convergence decision is asked yet; it isn't needed yet.
        │
        ▼
Each worker, independently and at its own pace:
  implement → targeted verification → narrowest meaningful broader verification →
  applicable quality/static checks → review-it → holds, uncommitted
  (no full-suite question of its own; no Review implementation yet; no Commit plan; no commit)
        │
        ▼
Once every worker in the wave is holding at that point, the parent presents one compact,
substantive checkpoint: what each worker implemented, its verification evidence, and any
review-it findings/scope notes/fixes worth knowing — in plain language, not internal
gate/rule vocabulary.
        │
        ▼
The human makes ONE decision for the whole wave: run the combined full-suite verification,
or explicitly skip it.
   ├─ RUN → assemble the combined candidate (disposable, never committed) → run the
   │        project's real full regression against the union of every worker's change →
   │        must succeed before any worker proceeds
   └─ SKIP → recorded explicitly; satisfies the same prerequisite for every worker in the wave
        │
        ▼
Each worker's Review implementation is now presentable, citing the wave's combined
result (run-and-green, or the recorded skip) in place of its own full-suite choice.
The human approves each worker's Review implementation independently.
        │
        ▼
Each approved worker derives its own Commit plan; the human approves each Commit plan
independently; only then does that worker create its durable commit(s).
        │
        ▼
Once one or more workers have durable, approved commits that need to reach the shared
milestone branch, converging them there — sequentially, one at a time — is normal
mechanical progression, not a fresh permission question each time. Convergence is
performed by resuming the original worker whose commits are converging, using its own
unchanged push-readiness and issue-closure procedures — not by the coordinating session
acting in the worker's place. The human is asked again only if convergence itself surfaces
a real conflict, unexpected drift in the milestone branch's tip, a stale/invalidated
approval, or ambiguity about the correct target branch.
        │
        ▼
Push readiness, issue closure (including checked task boxes and a durable closing
comment — parallel-wave provenance is additive context, not a replacement for it),
and next-work recomputation proceed exactly as the serial lifecycle already defines them,
per issue, per worker.
        │
        ▼
Once the milestone has zero open issues, hand off to ship-it's milestone-PR-readiness gate,
unchanged.
```

Nothing above is new engineering lifecycle. It is one lifecycle (`Lab → Plan → Implement → Review →
Ship`) executing as several bounded, per-issue instances, with exactly one new cross-cutting
checkpoint (the wave-level combined-verification decision) and one clarified timing/performer fact
(convergence). Everything else — Review implementation, Commit plan, push readiness, issue closure —
is the existing serial contract, unweakened.

## Research reconciliation

Targeted updates made to design documents (not to the smoke-test evidence records, which are
unchanged):

- **`vision.md`.** "Verification model" updated: the prior "required full-suite run... not a run/skip
  decision" language is superseded by the final wave-level run/skip decision (#3 above), with a
  pointer to `smoke-test-3.md` for why the prior position didn't survive contact with a live run.
  "Branch and worktree direction" gets a one-line pointer to the convergence-timing/performer
  clarification instead of leaving convergence framed as fully open. "Next smoke-test goals" gets a
  status note that the goals it listed have been exercised across ST2/ST3, with the residue now
  tracked in this document's "What remains unresolved," not as a still-open goal list of its own.
- **`combined-candidate.md`.** "Mechanics" section updated with the corrected three-step capture
  procedure `parallel-dry-run-2.md` validated experimentally (intent-to-add untracked paths, `git diff
  HEAD --binary`, immediate reset) in place of the original under-specified `git diff HEAD` claim. A
  new subsection records that Smoke Test 3 used a *different*, looser mechanism (plain `git apply`
  without `--3way`/`--index`, filesystem copy for untracked files) and succeeded only because that
  wave was file-disjoint by construction — this is evidence the looser mechanism is not safe in
  general, not evidence the recommended mechanism was wrong. "Smoke Test 3 proposal" is marked
  executed, with a pointer to `smoke-test-3.md` rather than restating it as a future plan.
- **`responsibility-boundaries.md`.** "Combined verification" section's research decision is updated
  to the final wave-level run/skip framing (#3), explicitly marked as superseding the prior
  "mandatory" text. "Convergence policy decision" and "Convergence execution" entries, and the
  matrix rows for both, are updated to record the final decision (#7/#8: sequential convergence is
  normal mechanical progression once durable commits exist, performed by the original worker) as the
  settled position going forward, while preserving the historical fact that ST1 and ST3 both actually
  used parent-performed convergence and only ST2 used worker-performed convergence — the decision
  settles what *should* happen next, not what happened in the three runs already recorded elsewhere.
- **`orchestration.md`.** "Combined-state verification" watch item updated: now attempted for real
  once (ST3), with confirmed mechanism divergence — still the strongest recurring candidate, still
  not promoted past "watch," since a working mechanism has not yet been observed twice. "Convergence
  sequencing" updated to reflect that *sequencing itself* is no longer an open judgment call requiring
  parent reasoning each time (decision #7 makes it default mechanical progression); the genuinely open
  part narrows to conflict/drift/staleness/ambiguous-target handling. A new entry records the
  candidate-patch-propagation finding explicitly as **runtime mechanics** (how an uncommitted
  methodology change reaches an isolated worktree), not a cross-worker coordination candidate — it does
  not belong in the same category as decision routing or combined verification.
- **`parallel-dry-run-2.md`.** A short status note added pointing to `smoke-test-3.md` as the executed
  result, naming where execution diverged from this document's own predictions (the mechanism
  divergence; two of three workers initially taking the wrong verification path, traced to candidate-
  patch propagation rather than the ordering correction this document proposed). The document's own
  predictive content and validated capture-procedure experiment are left intact as the historical
  record of what was planned and pre-validated.

`smoke-test-1.md`, `smoke-test-2.md`, and `smoke-test-3.md` are unchanged — they are evidence, not
design documents, and nothing above rewrites what actually happened in any of the three runs.

## Final skill findings

Kept conservative, per the request's own instruction, and cross-checked against
`smoke-test-3.md`'s own "Skill findings" section rather than re-deriving from scratch.

**Existing rules confirmed sufficient, no change:**
- `issue-closure.md` — directly re-confirmed. Smoke Test 3's task-checkbox/closing-comment regression
  was the parent bypassing this procedure by acting directly instead of resuming the original worker,
  not a defect in the procedure itself. The subsequent repair of #334/#344/#345 (outside this
  reconciliation's own scope, performed as a separate correction) used exactly this file's own recipe
  and is the positive evidence it works when actually followed.
- `push-readiness.md` — same reasoning; bypassed as a procedure in ST3, not shown deficient.
- `commit-boundaries.md` — its trailer policy and commit-plan-derivation timing were applied
  correctly, unprompted, by every worker across all three smoke tests.
- `worktree-preservation.md` — its vocabulary note continues to do exactly the narrow disambiguation
  job it was written for; nothing about the final decisions touches the stash-preserving procedure it
  actually governs.
- `review-it`, `ship-it`, `plan-it` — no direct evidence from any of the three smoke tests requires a
  change to any of these; `ship-it`'s milestone-PR-readiness gate was reached and exercised correctly
  for the first time in ST3, unmodified.

**Candidate correction with repeated/direct evidence — proposed below:**
- `verification.md` — the concurrent-wave section and Gate 1 evidence bullet currently read as if
  only a successful combined run satisfies the concurrent-worker prerequisite; decision #3 requires an
  explicit skip to satisfy it too.
- `review-gates.md` — the matching Review implementation paragraph has the identical gap for the same
  reason.
- `sequencing.md` — the "Parallel workers" section is silent on *when* convergence should be raised
  relative to launch and *who* performs it once needed; decisions #6/#7/#8 settle both.

**Execution mistake, not a rule gap — no change:**
- Two of three ST3 workers' initial per-worker full-suite/Gate-1 attempts, and the convergence/
  push/closure bypass — both traced in `smoke-test-3.md` to specific, non-rule-text causes (candidate-
  patch invisibility across isolated worktrees; the parent acting directly instead of resuming a
  worker), not to ambiguity in what the rules say.

**Runtime/provisioning finding, not methodology — no change:**
- Worker bootstrap cost (third consecutive occurrence).
- Candidate-patch propagation into isolated worktrees (new in ST3, and inapplicable to this branch's
  own canonical, already-committed skill text — see "Evidence base" above).

## Proposed final skill diff

Not applied. Three files, each REDUCE-then-KEEP against the already-installed candidate text — nothing
new is invented, each hunk closes a specific gap named above.

### 1. `implement-it/rules/verification.md`

**Evidence requiring it:** decision #3 supersedes the "mandatory, not run/skip" prior position; the
installed text's Gate 1 evidence bullet ("the wave's combined verification result in its place") reads
as run-only. **Final behavior:** the wave gets one run-or-skip decision, made once, after every
participating worker holds ready — not per worker, and not automatically mandatory. **Why it belongs
here:** this file already owns exactly this decision point for the serial case; the concurrent case is
the same decision point, scoped to the wave instead of the issue. **Why serial behavior is unchanged:**
the existing per-issue "Full-suite choice" section is untouched; this only touches the already-present
concurrent-worker carve-out. **What stays outside this rule:** how, when, or by whom the combined
candidate is assembled — still explicitly not this rule's job.

```diff
--- a/implement-it/rules/verification.md
+++ b/implement-it/rules/verification.md
@@
 A worker executing as part of a human-authorized concurrent wave does not make the full-suite choice
 above. Final regression verification for its candidate implementation belongs to the wave's combined
 candidate state — decided and run once, for the wave, not per worker (`rules/review-gates.md`'s "Review
 implementation — first approval (Gate 1)" states what this worker still needs before presenting that
 approval).
 
+Like the per-issue choice above, the wave-level decision is itself a human-controlled run-or-skip
+choice — made once for the whole wave, after every participating worker has reached this point, never
+asked separately of each worker. A successful combined run and an explicit wave-level skip both satisfy
+it; neither this rule nor `review-gates.md` requires the combined suite to always be run.
+
 This does not change the full-suite choice for a single worker running alone, and does not specify
 how, when, or by whom the combined candidate state is assembled, verified, or evaluated — that stays
 outside this rule.
@@
 - `review-it` clean, or findings fixed and re-reviewed;
-- the human's explicit full-suite choice, including the result if run or an explicit skip — or, for a
-  concurrent worker, the wave's combined verification result in its place (see "Concurrent workers in a
-  parallel wave" above).
+- the human's explicit full-suite choice, including the result if run or an explicit skip — or, for a
+  concurrent worker, the wave's combined-verification decision in its place: a successful combined-suite
+  result if run, or the wave's recorded explicit skip (see "Concurrent workers in a parallel wave"
+  above).
```

### 2. `implement-it/rules/review-gates.md`

**Evidence requiring it:** the same gap as above, in the file that actually owns the Review
implementation stop condition — its current wording ("until successful full-suite evidence... is
available") does not itself account for a valid wave-level skip. **Final behavior:** a concurrent
worker's Review implementation stop resolves once the wave's combined-verification decision is
resolved, whichever way. **Why it belongs here:** this file owns the stop condition end to end for the
serial case; this is the same stop's entry condition, narrowed for the concurrent case. **Serial
behavior unchanged:** untouched for a worker not part of an authorized concurrent wave.

```diff
--- a/implement-it/rules/review-gates.md
+++ b/implement-it/rules/review-gates.md
@@
 A worker in a human-authorized concurrent wave (`rules/sequencing.md`'s "Parallel workers in a
 delivery/phase milestone") may complete the bullets above and `review-it`, but this stop is not reached
-yet: report the implementation as ready for combined verification and hold, rather than presenting
-Review implementation, until successful full-suite evidence covering this worker's candidate
-implementation — from the wave's combined candidate state — is available. Once that evidence exists,
-cite it below in place of a per-worker full-suite result.
+yet: report the implementation as ready for combined verification and hold, rather than presenting
+Review implementation, until the wave's combined-verification decision is resolved — either successful
+full-suite evidence covering this worker's candidate implementation from the wave's combined candidate
+state, or the human's explicit, recorded decision to skip the combined run for the wave. Once that
+decision is resolved, cite it below in place of a per-worker full-suite result.
```

### 3. `implement-it/rules/sequencing.md`

**Evidence requiring it:** decision #6 (ST3's premature convergence question, corrected live by the
human) and decisions #7/#8 (sequential convergence as normal mechanical progression, performed by the
original worker, not the parent — closing the exact regression `smoke-test-3.md` records). **Final
behavior:** convergence mechanics remaining undefined is not a reason to delay authorizing or launching
a wave; once durable, approved commits exist, sequential convergence onto the milestone branch is
ordinary progression, executed by resuming the original worker, using its own unchanged procedures —
not a new decision to ask about each time, and not something the coordinating session performs in the
worker's place. **Why it belongs here:** this section already owns the one structural fact about
parallel convergence the milestone rule needs; this adds the timing and performer facts the same
section was previously silent on. **What stays outside this rule:** how a real conflict, drift, or stale
approval gets resolved once one occurs — those remain human judgment calls, not mechanical defaults.

```diff
--- a/implement-it/rules/sequencing.md
+++ b/implement-it/rules/sequencing.md
@@
 Once the human has explicitly authorized concurrent execution of more than one dependency-ready issue
 in this milestone, each worker gets its own temporary issue branch, cut from the confirmed milestone
 branch, instead of implementing directly on the shared branch. The milestone branch remains the
 eventual convergence target for every worker's approved commits.
 
 This rule does not define how or when that convergence happens. That is an open question pending
 evidence from real parallel execution, not a decision this rule makes on its own.
 
+Convergence mechanics being unresolved is not a reason to delay authorizing or launching this wave, and
+is not a decision to ask the human to make before any worker starts — it only becomes relevant once one
+or more workers have durable, approved commits that need to reach the milestone branch.
+
+Once that point is reached, converging each approved worker's commits onto the milestone branch,
+sequentially, is normal mechanical progression — not a fresh permission question on every occurrence.
+Convergence is performed by resuming the original worker whose commits are converging, using its own
+unchanged push-readiness and issue-closure procedures; the coordinating session does not perform
+convergence, push, or closure in that worker's place. Stop and ask only when convergence itself surfaces
+a genuine unsafe or ambiguous condition: a real merge conflict, unexpected drift in the milestone
+branch's tip, a stale or partially-invalidated approval, or ambiguity about which branch is actually the
+correct convergence target.
+
 Do not turn observed branch-name patterns into a rigid taxonomy. A name derived from what the
 milestone actually is — its area, or the kind of change it bundles — is the goal; illustrative shapes
```

### Every hunk from earlier candidate drafts, challenged and rejected

Per the request's Part 3, classified explicitly rather than silently dropped:

| Candidate hunk | Verdict | Why |
|---|---|---|
| Presentation template for the wave-ready checkpoint | **REMOVE** | Parent/Control Room territory (decision #2/#10); a worker skill has no business specifying how its own report gets worded to a human alongside siblings' reports. |
| Event-aggregation / decision-batching logic | **REMOVE** | Requires knowing multiple workers' states at once; inherently cross-worker, not one worker's engineering concern. |
| Git worktree/vendor/node_modules bootstrap steps | **REMOVE** | Runtime/provisioning (worker bootstrap cost); no `implement-it` rule should specify how a worktree gets its dependencies. |
| `git apply --3way --index`, intent-to-add capture steps, `git worktree add/remove` | **REMOVE** | Exactly the Git mechanics decision #5 says stay out of methodology; belongs in `combined-candidate.md`'s mechanism investigation, not in a skill rule. |
| "Paste patched rule text into each worker's launch prompt" as a standing instruction | **REMOVE** | Explicitly rejected by decision #12 — a workaround for an experimental, uncommitted installation state, not permanent methodology; also inapplicable once the patch is actually committed, as it already is on this branch. |
| A conflict-detection/resolution-routing subsystem | **REMOVE** | No smoke test has exercised a real conflict yet (`smoke-test-3.md`, "What remains unresolved"); speculative ahead of evidence, and explicitly out of scope per the request. |
| Convergence-performer statement (worker, not parent) | **KEEP** | Folded into the `sequencing.md` hunk above — this is decision #8 itself, not a speculative addition. |
| Wave-level run/skip clarification | **KEEP** | Folded into the `verification.md`/`review-gates.md` hunks above — this is decision #3 itself. |
| Convergence-timing clarification | **KEEP** | Folded into the `sequencing.md` hunk above — this is decisions #6/#7 themselves. |

## Responsibility boundary

Restated at the final-decision level, condensing `smoke-test-3.md`'s own "Control Room / orchestration
evidence" and `responsibility-boundaries.md`'s matrix rather than re-deriving it:

**Worker / engineering skills (unchanged in shape, one new wait-condition added):** implement one
issue; targeted + narrowest meaningful broader verification; `review-it`; hold candidate-ready (now
additionally waiting on the wave's one combined-verification decision when part of an authorized
wave); Review implementation; Commit plan; durable commits; push readiness; issue closure with a
durable closing record; next-work recomputation, where current methodology already owns it.

**Runtime (unchanged, still not reimplemented):** concurrent execution contexts; isolated worktrees;
worker identity/status; pause/resume via addressable messaging; preserved workspace state across
interruption. The candidate-patch-propagation finding belongs here, not to Control Room — it is about
how one specific kind of state (an uncommitted methodology change) reaches an isolated execution
context, the same category as workspace isolation itself.

**Parent / Control Room candidate (evaluated, not extracted):**
- Wave-state tracking and candidate-ready synchronization — real, recurring, still informally handled.
- Collecting worker evidence into one decision-oriented checkpoint — validated once (ST3's pre-
  combined-verification summary), not repeated at the Review-implementation/Commit-plan stages in the
  same run; the strongest concrete presentation gap on record.
- The wave-level combined-verification decision itself — now methodology (see skill diff above); *who
  presents it and how* remains parent territory.
- Combined-candidate coordination (assembly actor and exact procedure) — one data point (the parent,
  using a divergent mechanism), not yet a validated default.
- Routing human decisions to the correct worker — validated across ST2 and ST3, including ambiguous
  cases; native runtime plus parent conversational tracking, not a new construct.
- Commit-plan aggregation — real, recurring gap (ST3's async relay-by-arrival pattern); not resolved.
- Convergence serialization (ordering, not performance) — validated across ST1–ST3 as a parent
  responsibility; convergence *performance* is now settled as worker-owned by decision #8, which
  narrows, but does not eliminate, this candidate's remaining scope to sequencing/serialization itself.

No artifact form is decided here. Per the request, next-work recommendation stays a WATCH item —
ST3's wave was pre-selected as the milestone's entire remaining open set, so it added no new evidence
either way.

## Control Room findings

Ranked by how close each candidate is to `orchestration.md`'s own extraction bar, using all three
smoke tests' combined evidence:

1. **Combined-state verification.** The strongest candidate across all three waves — escalated from
   "never attempted" (ST1) to "gap, incidentally covered" (ST2) to "attempted for real, with confirmed
   procedural divergence" (ST3). Still short of the bar: one real attempt with a divergent mechanism is
   evidence of *how it goes when tried*, not a second clean success confirming a stable procedure.
2. **Decision-boundary batching / decision-oriented presentation.** Real, recurring evidence (ST2's
   ambiguous-answer routing; ST3's async relay repetition at both Review-implementation and Commit-plan
   stages). Growing toward the bar, not at it — still evidenced only within single runs, not against a
   clean before/after skill correction the way `sequencing.md`'s branch patch was tested.
3. **Convergence performer.** Now two data points for parent-performed (ST1, ST3) against one for
   worker-performed (ST2) — but decision #8 settles the *policy* going forward regardless of that
   asymmetric evidence; what's still missing is a clean run that actually follows the now-settled policy,
   to confirm it holds under real parallel conditions rather than only in the one run (ST2) that
   happened to do it before the policy was explicit.
4. **Candidate-patch propagation.** Real and consequential, but reclassified here (per decision #12 and
   the "Evidence base" section above) as runtime mechanics, not cross-worker coordination — it does not
   compete for the same extraction bar as the other three.

None of the four clears the bar for "extract into an artifact now." This matches `smoke-test-3.md`'s
own conclusion and does not need re-deriving further.

## What remains unresolved

- Whether the newly-settled convergence-performer policy (#8) actually holds under real parallel
  conditions when applied deliberately, as opposed to the one run (ST2) that happened to do it before
  the policy existed.
- Whether a real file overlap or merge conflict — at combined-candidate assembly or at convergence —
  behaves the way `combined-candidate.md`'s analysis predicts; no run across ST1–ST3 has exercised one.
- Whether the corrected combined-candidate capture procedure (intent-to-add, `--binary`, `--3way`,
  `--index`) actually matters in practice, or whether a project's own risk tolerance makes the looser
  ST3-style mechanism an acceptable default for file-disjoint waves specifically — this reconciliation
  does not decide that trade-off, only records that it exists.
- Decision-boundary batching at the Review-implementation/Commit-plan stages — real, unresolved, and
  explicitly parent/Control Room territory rather than a worker-skill fix.
- Worker bootstrap cost at higher worker counts — unexamined by any of the three waves so far, all of
  which used two or three workers.

## Is another smoke test needed?

**No broad re-run.** ST1–ST3 already validate, repeatedly, that isolated concurrent workers run
independent `implement-it` lifecycles correctly through both human gates, with worker-specific resume
and semantic commit planning, and that the methodology composes cleanly with milestone/`ship-it`
hand-off once a wave empties a milestone. Nothing in this reconciliation surfaces a genuinely
unresolved *architecture* problem — every open item above is a validation, clarification, or
presentation question, not an unknown about how the pieces fit together.

**Challenging that conclusion directly, as asked, rather than merely asserting it:** the strongest
case *for* a further test is the file-overlap/conflict condition — genuinely untested across three
waves, and the one condition `combined-candidate.md` itself flagged as most valuable. But a dedicated
fourth smoke test is not the only way to get that evidence: it can be observed the next time real,
overlapping parallel work occurs naturally, without manufacturing an artificial conflict for its own
sake. The same is true for validating the convergence-performer policy under real conditions. Neither
is evidence of an architecture unknown — both are "does the settled policy hold when exercised again,"
which is confirmatory testing, not investigation.

**Rule/document corrections, not architecture unknowns:** the three-file skill diff above, and the
research-document reconciliation already applied.

**Belongs to future orchestration/runtime investigation, not another implementation smoke test:**
decision-boundary batching, combined-candidate mechanism ownership at scale, and worker bootstrap
cost — none of these needs more application code exercised to advance; they need either a dedicated
Control Room investigation or a runtime-provisioning investigation, not a fourth consumer-issue wave.

## Publication readiness

Assuming the skill diff above is reviewed and applied on its own, separate track, what remains before
publication, listed without performing any of it:

1. Apply the three-file skill diff above (a separate, explicit change from this reconciliation).
2. Review the applied diff against this document and the smoke-test evidence once more, post-apply.
3. Reconcile public README/documentation with the final lifecycle described here.
4. Make the version/release decision this document explicitly does not make.
5. PR, merge, and release the methodology change through whatever process this repository's own
   release discipline requires.
6. Refresh any consuming project (starting with useOrbit, where the candidate patch has existed only
   as an uncommitted working-tree change throughout ST2 and ST3) onto the released version.

None of the above is performed by this document. The useOrbit Phase 26 PR (#357) is a separate,
application-delivery concern, untouched by anything here, and remains open and unmerged.

## Conclusion

Three parallel-implementation smoke tests now agree on far more than they disagree on: isolated
workers running the existing `implement-it` lifecycle, independently, through both human gates, with
worker-specific resume and semantic commit planning, is validated, repeated, and correct. What
changed at ST3 is narrower than it first appeared — not a new lifecycle stage, but one wave-level
verification decision (settled here as a run-or-skip choice, correcting an earlier "mandatory" research
position that a live run did not actually honor) and one timing/performer clarification for convergence
(settled here as "not before launch, and performed by the worker, not the parent, once it matters").
Both are now a three-file, additive skill diff — proposed, not applied — against text that, on this
branch, is already committed rather than the uncommitted candidate state ST3 actually exercised in
useOrbit. No genuinely unresolved architecture problem surfaced. The remaining open items are
validation and presentation questions, better answered by the next real parallel wave or a dedicated
Control Room/runtime investigation than by a fourth smoke test run for its own sake.
