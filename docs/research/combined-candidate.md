# Combined Candidate Verification

Status: Investigation. This is a mechanism/architecture investigation, not an orchestrator design and
not a skill change. It does not modify `implement-it`, `review-it`, or `ship-it`, and it does not
weaken the existing "no durable implementation commit before Review implementation and Commit plan
approval" invariant. Artifact form for any eventually-needed cross-worker step is unresolved and out
of scope here, exactly as in `responsibility-boundaries.md`.

## Problem

Smoke Test 1 and Smoke Test 2 both verified each parallel worker's own change, but neither ever
verified the *final combined* state with one explicit, deliberate decision (`smoke-test-1.md`;
`smoke-test-2.md`, "Post-convergence verification"; `responsibility-boundaries.md`, "Combined
verification"). After Smoke Test 2, the research position changed (recorded in
`responsibility-boundaries.md` and `vision.md`'s updated "Verification model"): a parallel worker no
longer makes its own full-suite run/skip choice; instead, the full project suite runs once, required,
against one assembled combined candidate state, and only after that candidate is green does the
human-facing implementation-review checkpoint get presented.

That policy decision creates a specific, previously unasked mechanism question, which is this
document's actual subject:

> Given multiple isolated workers whose implementations are complete, whose focused verification has
> passed, and whose `review-it` has already run, but whose changes are still **uncommitted** because
> human Review implementation / Commit plan approval has not happened yet, how can we safely construct
> one temporary combined repository state and run the full project suite against it?

Every mechanism considered here is judged first against whether it can even attempt this without
creating a commit that could be mistaken for an approved implementation step — that is the hard
constraint, not a preference to optimize against other goals.

## Evidence from Smoke Tests

- **ST1** (`smoke-test-1.md`): the parent merged both worker branches directly, itself, after each
  worker had already committed — no pre-commit combination was ever attempted, and no combined-state
  verification happened at all.
- **ST2** (`smoke-test-2.md`, "Convergence"): each worker's own convergence (push + merge into
  `feat/policies-http-frontend`) happened only *after* that worker's Commit plan was approved and its
  commits already existed. The closest thing to combined verification — #341's 446-test run during its
  own convergence step — ran against already-committed, already-approved content, for exactly the
  reason `responsibility-boundaries.md` already documents: nothing in either smoke test ever exercised
  combining *uncommitted* work.
- **Current skill text, read directly for this document** (`skills/implement-it/rules/
  commit-boundaries.md`, "How to derive commit boundaries," steps 1–2; `rules/review-gates.md`,
  "Commit plan — second approval"): commit-plan derivation only starts *after* Review implementation
  is approved, and "No commit is created before Commit plan is approved" is explicit and absolute. This
  confirms the mechanism gap is real, not hypothetical — nothing in the current lifecycle produces a
  commit before both approvals, so nothing currently gives combined verification anything committed to
  work with at the point the new policy wants it to run.
- **A relevant existing precedent, read directly** (`rules/worktree-preservation.md`): the skill
  already trusts a qualified, SHA-tracked `git stash` procedure for temporarily setting aside content
  during a Git rewrite, with explicit discipline against acting on the wrong entry. This is evidence
  that a careful, narrowly-scoped Git mechanism is an acceptable category of tool for this methodology
  when the discipline around it is explicit — it is not evidence that stash is the right *specific*
  mechanism for this problem (see "Option analysis," below).

## Invariants

Constraints this investigation treats as fixed, not up for negotiation by any mechanism choice:

- **No durable implementation commit before both human approvals.** Restated from `review-gates.md`:
  Review implementation and Commit plan are both required, and approval at one never implies the
  other. No mechanism below may create a commit — on any branch, in any worktree, pushed or not — that
  could be mistaken for, or later treated as, an approved implementation step. This document does not
  redefine "durable" or "temporary" to route around this; where a candidate mechanism's own objects
  come close to that line, it says so plainly rather than asserting they don't count (see the
  throwaway-commit/cherry-pick options below).
- **Worker state is not damaged by combination.** A worker's own worktree, branch, and diff must
  remain exactly as it was, usable to resume that worker's own lifecycle, regardless of what happens to
  a combined candidate built from a copy of its content.
- **Convergence execution stays worker-performed, once it is needed.** `responsibility-boundaries.md`'s
  "Convergence execution" finding is that ST2's actual push/merge into the shared branch was performed
  by each *original worker*, resumed, not by the parent or a fresh agent. Nothing about combined
  verification should require inventing a different actor to mutate a worker's own branch later; this
  document's mechanism only concerns a *disposable, pre-approval* combination, never the real
  convergence step that already works.
- **Pre-existing, unrelated worktree content is never discarded or misattributed** (`rules/
  verification.md`'s "Preserve pre-existing worktree changes"; `rules/worktree-preservation.md`).
  Any mechanism that reads from a worker's worktree must do so without disturbing content that isn't
  the worker's own reviewed change.

## Desired parallel verification lifecycle

Restated concretely from `vision.md`'s updated "Verification model," as the target this mechanism
serves:

```text
Worker A: implement → targeted + broader verification → review-it → "ready" (uncommitted)
Worker B: implement → targeted + broader verification → review-it → "ready" (uncommitted)
Worker C: implement → targeted + broader verification → review-it → "ready" (uncommitted)
                                    │
                                    ▼
                    assemble combined candidate state (uncommitted)
                                    │
                                    ▼
                      full project suite — once, required
                                    │
                                    ▼
        implementation-review checkpoint, per worker (review-it summary +
        verification evidence + combined-suite result, in plain language)
                                    │
                                    ▼
              human manual review + explicit approval, per worker
                                    │
                                    ▼
                Commit plan(s) → human approval → durable commits
                                    │
                                    ▼
        convergence (worker-performed, as already validated in ST2) → push → close
```

The mechanism this document evaluates is only the box in the middle: "assemble combined candidate
state," and the full-suite run immediately after it.

## Mechanisms considered

| # | Mechanism | One-line description | Verdict |
|---|---|---|---|
| 1 | Diff/patch into a temporary integration worktree | `git diff` each worker's uncommitted change; `git apply` each patch, in sequence, into a fresh `git worktree` at the milestone tip | Viable — baseline |
| 2 | Git stash-based transfer | Each worker `git stash push`es its change; the integration worktree `git stash apply`s each entry by recorded SHA | Viable but strictly worse than #1 |
| 3 | Temporary/throwaway commits or refs, discarded after use | Commit each worker's uncommitted change to a disposable local ref, merge/cherry-pick that into the integration worktree, discard the ref afterward | Rejected |
| 4 | Cherry-picking into an integration workspace | Same as #3's core problem — cherry-pick needs a source commit to exist first | Rejected, same reason as #3 |
| 5 | Filesystem copy/apply of changed files | Copy the specific changed/added paths (from `git status --porcelain`) directly into the integration worktree's filesystem | Viable fallback, weaker than #1 |
| 6 | Diff/apply refined with `--3way --index` | Mechanism #1, using `git apply --3way --index` instead of a plain `git apply` | **Recommended** |

This list is not exhaustive of every Git trick available — it is exhaustive of the plausible
categories the spec asked to consider (patch/diff, stash, temporary commit, cherry-pick, filesystem
copy, "another Git-native option"), with #6 being that last category, arrived at by refining #1 rather
than inventing something unrelated.

## Option analysis

### #1 / #6 — Diff/patch into a temporary integration worktree (baseline and its refinement)

**Mechanics.** `git worktree add <path> <milestone-branch-tip>` creates a fresh, ordinary worktree with
nothing uncommitted in it. For each ready worker, `git -C <worker-worktree> diff HEAD` captures its
full uncommitted change (staged and unstaged) as a patch; `git -C <integration-worktree> apply
--3way --index <patch>` applies it, staging the result. Repeat per worker, in any order the workers
themselves are file-disjoint enough to tolerate. Run the full suite in the integration worktree.

**Approval invariant.** No commit is created anywhere by this mechanism — not in the integration
worktree, not in any worker's own worktree. The integration worktree's index holds staged-but-uncommitted
content, exactly like any ordinary in-progress change. This is the cleanest fit against the invariant
of any option considered: there is no commit object to mistake for an approved step, on any branch, at
any point.

**Worker preservation.** `git diff` is read-only against the worker's worktree — it changes nothing
there. The worker's own worktree, index, and branch are untouched throughout; the worker can keep
working, or be resumed later, exactly as if combination had never happened.

**Verification.** The full suite runs against the real, physical union of every ready worker's changes
— assuming the patches apply cleanly, the integration worktree's content is not a simulation or
estimate, it is the actual combined code. If any project setup (dependency install, generated
artifacts, built assets) is required — as it was for every ST2 worker's own worktree — the integration
worktree needs that same bootstrap once, not once per worker.

**Conflict behavior.** `git apply --3way` detects a true textual conflict (two workers' patches
touching overlapping lines) and fails with a clear error before the suite ever runs; `--3way`'s
fallback merge can sometimes resolve a benign, non-overlapping-in-substance conflict on its own, but
never silently — a real conflict still stops the apply. This is strictly better conflict visibility
than #5 (filesystem copy), which has no equivalent detection at all.

**Recovery.** The integration worktree is entirely disposable: `git worktree remove --force <path>`
(or simply deleting the directory and pruning) destroys nothing that matters, because it was only ever
a copy assembled from worker state that still exists independently. If combined verification fails —
suite red, or an apply conflict — the integration worktree can be discarded and rebuilt deterministically
from the same worker diffs at any time, since nothing about assembling it consumed or altered the
source.

**Portability.** `git worktree`, `git diff`, and `git apply` are core Git, available in any Git-based
environment, with no Claude Code-specific behavior involved at all. The portable methodology
requirement is narrower than the mechanism: "read each ready worker's uncommitted change without
disturbing it, and materialize their union somewhere disposable, before any commit exists." Git's
worktree/diff/apply primitives happen to satisfy that requirement well; a different runtime could
satisfy the same requirement with different primitives (e.g., a VCS with native shelved-changes
support) without this methodology needing to know which.

**Why #6 over plain #1.** `--index` keeps the integration worktree's staged content visible and
inspectable the same way a real in-progress commit would look, which matters if a human wants to look
at the assembled diff directly. `--3way` is a strict improvement in conflict handling with no downside
against plain `git apply`. There is no reason to prefer unrefined #1 once #6 is available; #1 is
presented mainly to establish the baseline pattern before adding the refinement.

### #2 — Git stash-based transfer

**Mechanics.** Each ready worker runs `git stash push -u -m "<description>"` in its own worktree,
records the resulting SHA per `worktree-preservation.md`'s own discipline, and the integration worktree
runs `git stash apply --index <SHA>` for each one in turn.

**Approval invariant.** A stash push does create Git objects (a commit-shaped worktree tree, and a
stash commit tying it to the index tree and parent), but they are never reachable from any branch ref,
never pushed, and this skill already treats them as a distinct category from an implementation commit
(`worktree-preservation.md` uses exactly this object type for a different, already-accepted purpose).
This satisfies the invariant on the same principled basis #1 does — no branch-reachable, pushable
commit is created — though it is a slightly less clean argument than #1's "no relevant Git object
exists at all."

**Worker preservation — the deciding weakness.** Unlike `git diff`, `git stash push` is *destructive*
against the worker's own worktree: it removes the change from the worktree, leaving it clean, until
something pops or applies it back. If a worker needs to keep looking at or reasoning about its own
diff while combined verification runs elsewhere — or if the human wants to inspect a worker's live
worktree during this window — stashing has already taken that content away from where it was. This is
the specific, concrete reason #2 is strictly worse than #1/#6 for this use case, not merely a stylistic
preference.

**Verification, conflict behavior, recovery.** Materially the same as #1 once the stash is applied —
`git stash apply` surfaces a real conflict the same way `git apply` does, and the integration worktree
is equally disposable. The one recovery wrinkle: if a worker's stash entry is dropped or its SHA lost
before combination happens, `worktree-preservation.md`'s own step 7/9 discipline (never guess a
position, resolve by SHA) would need to be followed exactly to avoid acting on the wrong entry — an
extra discipline burden #1 doesn't carry at all, since a fresh `git diff` needs no identity tracking.

**Portability.** Equally portable to #1 in principle (stash is core Git), but the destructive-to-worker
property makes it a worse fit for *this* problem regardless of portability.

### #3 / #4 — Temporary/throwaway commits, or cherry-picking (which requires one first)

**Mechanics.** Commit each ready worker's uncommitted change to a disposable local ref not treated as
the worker's "real" branch, then merge or cherry-pick that ref's commit into the integration worktree,
discarding the disposable ref afterward.

**Approval invariant — rejected here.** This is the one category the investigation explicitly declines
to recommend, on the invariant itself. `git commit` is the exact action `review-gates.md`'s "No commit
is created before Commit plan is approved" is written to prevent, regardless of whether that commit is
later discarded, never pushed, or lives on a branch nobody calls "real." Treating a commit as
non-durable *because* the plan is to delete it afterward is precisely the kind of redefinition the
brief for this document warned against — it requires trusting a discard step to happen reliably every
time, on every path including a failure or interruption mid-process, and it creates a commit object
that a later reader of `git log --all` or `git reflog` could genuinely mistake for an approved
implementation step, which #1/#2 never do. Cherry-picking (#4) inherits the identical problem, since it
needs exactly this kind of source commit to exist before it can run.

**Not fully disqualified, but not recommended.** If a runtime genuinely could not support #1's
diff/apply pattern (a version-control system with no working analogue), a throwaway-commit approach
might be the only option left, and would need its own, much stricter discipline — e.g., a ref namespace
that is mechanically swept and verified empty after every use, never surfaced in any report as if it
were a commit. Nothing in this investigation establishes that Git-based Agentic Engineering ever needs
to fall back to this; #1/#6 fully covers the need here.

### #5 — Filesystem copy/apply of changed files

**Mechanics.** From each ready worker's `git status --porcelain`, copy the changed/added file paths
directly into the integration worktree's filesystem, and explicitly remove any paths a worker deleted.

**Approval invariant, worker preservation, recovery.** Equivalent to #1 — no commit involved, source
worktrees untouched (a plain file copy is as read-only against the source as `git diff` is), and the
integration worktree is just as disposable.

**Verification and conflict behavior — the deciding weakness.** A whole-file copy has no equivalent to
`git apply`'s conflict detection. If two workers happen to touch the same file, the second copy simply
overwrites the first's version of that file with no error and no signal that anything was lost — a
silent, undetected loss of one worker's reviewed change, exactly the failure mode #1/#6 turns into a
loud, pre-suite error instead. This is the specific reason #5 is not recommended over #1/#6, not a
general preference for one tool over another.

**Portability.** Equally portable (no Git needed at all, in fact), but the conflict-blindness makes it
strictly worse for this specific problem.

## Conflict and staleness implications

Applying the recommended mechanism (#6):

- **A true conflict is detected at apply time, before the full suite runs, before any human sees an
  implementation-review report.** This is strictly earlier and cheaper than discovering it after
  convergence, which is where both smoke tests would have discovered it if it had occurred (it did not,
  by construction, in either wave — see `orchestration.md`, "Conflict handling," "not observed").
- **A conflict does not by itself mean either worker's implementation is wrong.** It means two reviewed
  diffs cannot be mechanically combined as-is. Resolving it requires deciding whose content wins, or
  hand-merging — and if that resolution changes the actual content either worker's `review-it` pass
  reviewed, that worker's review-it result is now stale under `review-it/rules/verification.md`'s own
  staleness rule (already established as existing policy, not something this document is proposing) and
  needs a scoped re-review before that worker's implementation-review checkpoint can rely on it again.
- **Who resolves a conflict is not established by this investigation.** Whether the parent, one of the
  two affected workers, or the human resolves it, and how a resulting content change gets communicated
  back to the affected worker for its own re-review, is left as an open question for Smoke Test 3 to
  exercise deliberately — see "Smoke Test 3 proposal," below. This document only establishes that the
  mechanism *detects* the conflict cleanly; it does not resolve the cross-worker questions the detection
  then raises.

## Recovery

- **Combined verification fails (suite red).** The integration worktree is untouched worker state plus
  a disposable overlay; nothing about a red suite damages any worker. The failure needs to be traced to
  which worker's change is responsible (ordinary debugging against the combined worktree, or by
  removing one worker's applied patch at a time), and that worker's own implementation, targeted
  verification, or review-it may need revisiting — but none of that touches the invariant, since nothing
  has been approved or committed yet for anyone.
- **The integration worktree is interrupted, lost, or corrupted.** Fully reconstructible, deterministically,
  from the same worker diffs, because assembling it never consumed or altered the source (true for #1/#6
  and #5; #2's stash variant has the caveat noted above about needing the SHA still to be resolvable).
  There is no unique state inside the integration worktree that doesn't already exist, in a more
  authoritative form, inside the workers' own worktrees.
- **A worker itself is interrupted while "ready" and awaiting combination.** Outside this document's
  scope to solve generally — `evidence.md`/`smoke-test-1.md`'s pre-gate worktree/branch preservation
  already showed Claude Code's native recovery handles an interrupted worker's workspace; nothing about
  combined verification changes that. What is new and untested is recovery of a worker interrupted
  specifically *after* it was included in a combined run but *before* its own implementation-review
  approval — not yet exercised by either smoke test, and worth Smoke Test 3's attention if schedule
  allows (see below).

## Portability

Separating the three layers the spec asks to keep distinct:

- **Portable methodology requirement.** Combine several ready-but-uncommitted workers' changes into one
  disposable state, verify it once with the project's real full-regression mode, without creating
  anything that could be mistaken for an approved commit, and without disturbing any worker's own state
  in the process. Nothing about this requirement names Git.
- **Git mechanism that satisfies it here.** `git worktree add` for a disposable integration workspace;
  `git diff` (read-only) to capture each ready worker's change; `git apply --3way --index` to combine
  them; ordinary full-suite execution inside that worktree; `git worktree remove` (or simple deletion)
  to discard it.
- **Claude-Code-specific convenience, if any.** None of the above needs a Claude Code primitive — no
  background `Agent`, no `isolation:"worktree"`, no `SendMessage`. The only Claude-Code-shaped question
  this raises is *who* runs these Git commands (the parent session, a fresh short-lived agent, or one of
  the ready workers itself) — that is a runtime/orchestration question this document deliberately does
  not answer, consistent with `responsibility-boundaries.md`'s existing "artifact form is unresolved"
  position. Do not design a runtime adapter from this; the mechanism itself needs no adapter.

## Architectural drift

`responsibility-boundaries.md`'s "Architectural/convention drift" already established, as confirmed
fact, that ST2's three workers picked two mutually inconsistent route-placement conventions
(`clients.policies.index` in `routes/policies.php`; `agents.policies.index`/`carriers.policies.index`
in their own entity route files) because none could see the others' choice while implementing.

Assembling a combined candidate state before approval — the mechanism this document recommends —
*technically* creates a moment where that inconsistency becomes visible: once #6 applies all three
workers' patches into one worktree, a `grep` for the new route names, a `php artisan route:list` pass,
or a human/`review-it` skim of the combined codebase would surface the mismatch immediately, in a way no
single worker's own isolated review ever could.

That is a real opportunity the mechanism enables, but it is not the same thing as the mechanism *solving*
architectural drift, and this document does not assign it that responsibility:

- **Combined verification, as decided, is a test-suite pass/fail check — not a convention-consistency
  check.** Nothing about "run the full suite once" inspects for cross-worker naming/placement
  consistency; that would require a distinct, deliberate step (a targeted `review-it` invocation scoped
  to the combined tree, or a specific human/parent check) that no current skill or this document defines.
- **Classification, unchanged from `responsibility-boundaries.md`:** this remains most precisely an
  inherent parallelism risk specific to convention decisions with no established single precedent yet,
  now joined by one additional fact — a mechanism exists that *could* make the drift visible earlier,
  if something is deliberately pointed at it. Whether that something is a `review-it` scope, a human
  check, or a new step is not decided here, and is recorded as unresolved rather than assigned.

## Recommended mechanism

**Recommend #6 — diff/apply into a temporary integration worktree, using `git apply --3way --index`.**

Tradeoffs, explicitly:

- **For:** cleanest fit against the approval invariant of every option considered (no relevant Git
  object exists at all, not merely one that is unreachable or discarded); strictly non-destructive
  against every worker's own state; loud, pre-suite conflict detection; fully and deterministically
  reconstructible; built entirely from ordinary Git primitives already used elsewhere in this skill
  (`git worktree`, and the same disposable-workspace spirit as `worktree-preservation.md`'s stash
  discipline, without inheriting its destructive-to-source property).
- **Against:** requires a fresh, disposable worktree with its own project bootstrap (dependency
  install, build) — the same cost every ST2 worker already independently paid once for its own
  worktree, now paid once more for the integration worktree; a genuine textual conflict still requires
  a human or parent decision to resolve (the mechanism detects, it does not resolve); at higher worker
  counts, sequential patch application means a late conflict could require re-applying earlier patches
  after an earlier one is adjusted, though this is an ordinary Git workflow cost, not a design flaw.
- **No option safely satisfies the invariant more cleanly than this one.** #3/#4 were rejected, not
  merely ranked lower, specifically because they touch the invariant's actual boundary (a real commit
  object, before approval) rather than staying clearly outside it.

## What remains unresolved

- **Who runs the mechanism** — the parent session, a fresh short-lived agent, or one of the ready
  workers itself — is not decided here (see "Portability," above). This is exactly the kind of
  cross-worker-visibility question `responsibility-boundaries.md` already tracks as unresolved, not a
  gap specific to this mechanism.
- **When assembly is triggered** — whether combined verification waits for every currently-launched
  worker to reach "ready," or runs against whichever subset is ready at some fixed checkpoint, and what
  happens to a worker that becomes ready after an initial combined run already passed. Neither smoke
  test's timing (all three ST2 workers happened to progress in a broadly similar rhythm) tested this.
- **Conflict resolution ownership**, per "Conflict and staleness implications" above — who resolves a
  real textual conflict, and how the resulting content change reaches the affected worker for a scoped
  `review-it` re-review, is not established.
- **Environment bootstrap cost at scale** — every ST2 worker independently ran `composer install` /
  `npm install` / asset builds in its own fresh worktree; the integration worktree needs the same
  bootstrap, and whether that cost is acceptable to pay on every combined-verification run (versus some
  reuse strategy) is unexamined here.
- **Whether this mechanism actually works in practice** — this entire document is a pre-smoke-test
  design analysis. Nothing here has been executed against real concurrent implementation work. It is a
  candidate, not a validated procedure.

## Candidate methodology implications

**Research decision only (already recorded, not repeated as new here):** the per-worker vs.
combined-verification policy split in `responsibility-boundaries.md` and `vision.md`'s updated
"Verification model."

**Candidate methodology change, only if Smoke Test 3 validates the mechanism:**
- `rules/verification.md` may eventually need an explicit "combined verification for concurrent
  workers" procedure, parallel to but distinct from its existing per-issue "Full-suite choice" — not
  written now, and not implied to replace the existing serial-worker procedure.
- `rules/sequencing.md`'s "Parallel workers in a delivery/phase milestone" section may eventually need
  a pointer to that new procedure, the way it already points at convergence as a fact without owning
  its mechanics.
- Neither change is proposed as a patch in this document. Both are explicitly conditional on validation
  evidence this document does not yet have.

**Runtime behavior Agentic Engineering should not reimplement:** `git worktree add`/`remove` for a
disposable integration workspace, and `git diff`/`git apply --3way --index` as the combination
primitive. These are already-correct Git capabilities; no wrapper, adapter, or custom tool is
justified by anything found here.

**Orchestration watch item, consistent with existing entries in `orchestration.md`:** deciding *when*
to trigger assembly across workers in different states, and routing a conflict-driven staleness
consequence back to the correct worker — both inherently require visibility across more than one
worker's state, joining the existing "decision routing" and "convergence sequencing" watch items rather
than becoming a new, separate category.

## Smoke Test 3 proposal

A narrow validation of this mechanism, not a retest of everything ST1/ST2 already validated:

- 2–3 isolated workers (matching ST2's scale is sufficient; the mechanism itself does not need a higher
  count to validate — see "What remains unresolved" above regarding scale questions separately).
- Each worker: implementation, targeted verification, the narrowest meaningful broader regression scope,
  `review-it` — and stops there. **No per-worker full-suite decision, and no commit yet.**
- Assemble a temporary combined candidate via the recommended mechanism (`git worktree add` + `git
  diff` + `git apply --3way --index`, one application per ready worker).
- Run the full project suite once against that combined, still-uncommitted worktree.
- Only after that suite is green: present each worker's implementation-review checkpoint to the human —
  substantive `review-it` summary, focused verification evidence, and the combined-suite result, worded
  in plain technical language per the already-recorded UX finding (`vision.md`, "Human-facing
  presentation") — and get explicit per-worker approval.
- Commit plans, per worker, with explicit approval, exactly as ST2 already validated.
- Durable commits only after that.
- Record what happens to the temporary integration worktree once approvals land (discarded, since the
  real content now exists as approved worker commits) and confirm nothing about it was ever mistaken
  for durable state.
- Convergence, push, and issue closure exactly as ST2 already validated (worker-performed convergence,
  serialized by the parent) — this smoke test does not need to re-prove that part, only confirm it still
  holds once combined verification precedes it.

**One additional stress condition: intentional file overlap.** Deliberately choose or shape two of the
workers' issues so their implementations touch at least one shared file with a real (not cosmetic)
textual overlap. This is the single most valuable untested condition identified in this document and in
`responsibility-boundaries.md`'s own "What remains unresolved" — it directly exercises whether the
recommended mechanism's conflict detection actually fires, and, deliberately left open, forces a real
answer to "who resolves it and how does the affected worker's `review-it` staleness get handled" rather
than a hypothetical one. Do not additionally test interruption-mid-gate or semantic/convention drift in
the same wave — per the audit's own instruction, this would overload the test; either is a reasonable
candidate for a later, separate wave.
