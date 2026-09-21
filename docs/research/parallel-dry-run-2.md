# Parallel Implementation Smoke Test 3 — Dry Run

Status: Investigation and dry run. No useOrbit code, issues, or branches were touched to produce this
document. No installed skill file was modified — every change below is a proposal only. Smoke Test 3
itself was not started.

This document treats `vision.md`, `smoke-test-1.md`, `smoke-test-2.md`, `orchestration.md`,
`responsibility-boundaries.md`, and `combined-candidate.md` as the current, not-yet-accepted
investigation state — evidence and recorded decisions, not automatically accepted methodology — and
treats the skills actually installed in useOrbit's `.agents/skills/` (`implement-it`, `review-it`,
`ship-it`) as the real methodology being exercised, read directly for this document rather than assumed
from the prior docs' quotations. useOrbit's working tree currently carries Smoke Test 2's two-file
patch (`sequencing.md`'s "Parallel workers" section, `worktree-preservation.md`'s vocabulary note) as an
**uncommitted** local change — confirmed by `git diff` against both files, byte-for-byte identical to
`parallel-dry-run.md`'s proposed diff. This document's own proposal is additive to that uncommitted
state, not a replacement for it.

## Candidate wave

**Selected: #334 ("Add Policies link to top nav"), #344 ("Implement Policies index filters drawer"),
#345 ("Policies show page — Members tab").**

Directly confirmed via `gh issue list --milestone "Phase 26 — Policies HTTP & Frontend" --state all`:
these are the *only* three open issues left in the milestone — #341/#342/#343 (Smoke Test 2's wave) and
everything before them are closed. There is no fourth candidate to choose between; the milestone itself
now has exactly the wave size `combined-candidate.md`'s own Smoke Test 3 proposal asked for ("2–3
isolated workers... matching ST2's scale is sufficient").

**Dependencies, confirmed live:**

- #334 depends on #322 — closed.
- #344 depends on #335, #332 — both closed.
- #345 depends on #336 — closed.

All three are dependency-ready right now. None has an existing branch (`git branch -a | grep -E
"334|344|345"` — empty) and none has any comment (`gh issue view <n> --json comments` — zero for all
three) — genuinely unclaimed, exactly as ST2's wave was before it started.

**File-disjointness, confirmed by direct repository inspection, not assumed from issue text:**

| Issue | Files touched | Backend surface |
|---|---|---|
| #334 | `resources/js/components/shell/navItems.ts` (one line) | None |
| #344 | New `resources/js/pages/Policies/partials/FiltersDrawer.vue` (this repo already has this exact partial name/shape on `Agents`, `Carriers`, and `Clients` — direct precedent, confirmed by `find`); wiring inside `resources/js/pages/Policies/Index.vue`'s query state | None — #332 already built the backend query-param filtering this issue wires a UI to |
| #345 | `resources/js/pages/PolicyMedical/partials/PolicyMedicalDetailShell.vue` | Likely a small read-only prop addition to feed the roster table (a `PolicyInsured`-derived query), the same shape as ST2's `policiesCount`/`renewingPolicies` additions — confirmed only that `PolicyInsured` already exists as a model; not fully scoped, since this document does not plan the issue |

Zero file overlap among the three. This is a materially *cleaner* disjointness than ST2's wave: ST2's
three workers each touched a shared naming pattern (`routes/<entity>.php`, `<Entity>Controller`,
`<Entity>DetailShell.vue`) that later produced the confirmed route-placement drift
(`responsibility-boundaries.md`, "Architectural/convention drift"). Here, the three issues sit in three
structurally unrelated areas — global nav, the Policies index page, and one policy class's show page —
with no shared naming decision for the three workers to diverge on. Per the brief's own instruction to
prefer a clean happy path and not manufacture overlap, this wave is used as found, with no modification.

**Why include #334 despite its triviality.** `parallel-dry-run.md` deliberately set #334 aside from ST2
for gate-mechanics novelty reasons ("too small to exercise the gate lifecycle meaningfully... reach
Review implementation before targeted verification has finished mattering"). That reasoning doesn't
apply to *this* smoke test's actual subject. `combined-candidate.md`'s own "What remains unresolved"
list flags, unanswered by either prior smoke test: "whether combined verification waits for every
currently-launched worker to reach 'ready'... Neither smoke test's timing tested this." #334 finishing
almost immediately while #344/#345 are still implementing is exactly the asynchronous-readiness
condition that question needs. Its triviality is the reason to include it this time, not a reason to
exclude it.

**No deliberate conflict.** Per the brief's explicit instruction, no file overlap was manufactured. The
one stress condition `combined-candidate.md` itself recommended for Smoke Test 3 ("intentional file
overlap... the single most valuable untested condition") is **not** exercised by this wave, and this
document does not recommend reshaping the wave to force it — that recommendation belongs to
`combined-candidate.md`'s own research position and is noted, not adopted, per this dry run's brief.

## Desired lifecycle

Restated concretely against the actual three issues, merging `vision.md`'s updated verification model
with the brief's own execution trace:

```text
Parent: selects #334/#344/#345 as the concurrent-safe wave (file-disjoint, confirmed above);
        launches three isolated background workers, each on its own temporary issue branch cut from
        feat/policies-http-frontend's confirmed tip (sequencing.md's existing "Parallel workers"
        section — already installed, uncommitted).

Worker #334 (nav link):
  implement → targeted verification → review-it → "ready for combined verification" → WAITS
  (no full-suite question; no Review implementation report yet; no commit)

Worker #344 (filters drawer):
  implement → targeted + narrowest meaningful broader verification → review-it →
  "ready for combined verification" → WAITS

Worker #345 (Members tab):
  implement → targeted + narrowest meaningful broader verification → review-it →
  "ready for combined verification" → WAITS

        (#334 reaches "ready" well before #344/#345 — deliberately observed, not smoothed over)

Once all three report "ready":
  Parent (or a fresh short-lived agent — unresolved, see "Runtime/parent responsibilities"):
    → captures each ready worker's uncommitted diff (git diff HEAD, with the untracked-file and
      binary-file corrections this document's Part 6 review found necessary — see below)
    → creates a temporary integration worktree from the milestone branch's confirmed tip
    → applies each worker's patch with git apply --3way --index
    → if a real conflict is detected, stops here and reports it — does not run the suite, does not
      advance any worker toward Review implementation
    → if it applies cleanly, runs the full project suite once against that combined, still-uncommitted
      worktree — required, not a run/skip choice
    → if red, reports which worker's change is implicated and does not advance any worker
    → if green, presents each worker's Review implementation checkpoint to the human: substantive
      review-it summary, focused verification evidence, and the combined-suite result, in plain
      technical language (vision.md's "Human-facing presentation")

Human reviews and approves workers independently, in any order, exactly as ST2 validated:
  → approving #345 resumes #345 only; #334 and #344 preserve whatever state they were left in
  → each approved worker derives and presents its own Commit plan
  → human approves each Commit plan independently
  → durable commits created only then, per worker

After durable commits exist:
  → convergence: each approved worker performs its own push + merge into feat/policies-http-frontend,
    resumed by name, serialized by the parent to avoid a race — exactly as ST2 validated; this smoke
    test does not re-prove this part
  → push-readiness, issue closure, task-checkbox validation — per issue, unmodified
  → recompute: with #334/#344/#345 closed, the milestone has zero open issues; hand off to
    ship-it/rules/milestone-pr-readiness.md
```

Two things this trace deliberately does **not** pre-decide, left to ST3 to observe (see "Unknowns"):
whether combined verification is triggered the moment the *last* worker reaches ready, or on some other
timing; and who actually executes the capture/apply/suite-run sequence.

## Responsibility classification

Per the brief's five-way scheme (A: already correctly specified; B: existing responsibility needing a
small parallel-aware correction; C: native runtime/Git capability; D: cross-worker, parent/future
orchestration; E: unknown, observe in ST3).

| # | Behavior | Class | Notes |
|---|---|---|---|
| 1 | Selecting #334/#344/#345 as the concurrent-safe subset | D | Same as ST1/ST2 — human/parent judgment from file-disjointness; no skill computes this |
| 2 | Launching 3 isolated background workers on temporary branches | C | Native runtime + `sequencing.md`'s already-installed patch |
| 3 | Per-worker implementation | A | Unchanged, per-issue, worker/`implement-it` |
| 4 | Per-worker targeted + narrowest meaningful broader verification | A | Already accommodated by `verification.md`'s existing "narrowest reliable scope that proves the implementation" language — this is worker judgment already, not a separate rule to add (see "Current skill gaps") |
| 5 | Worker does **not** ask its own full-suite question | **B** | Real gap: current `verification.md` step 4 always asks it. This is the one behavioral correction ST3 actually needs |
| 6 | Worker invokes `review-it` standalone | A | Already scope-agnostic, unaffected |
| 7 | Worker reports itself "ready for combined verification" instead of Review implementation | **B** | No current rule describes this stop; needs the same small correction as #5 |
| 8 | Worker holds indefinitely, mid-wave, while siblings are in different states | C (mechanism) + A (worker doesn't need its own rule to just... wait) | ST2 already validated multi-state holding; nothing new here specifically for holding |
| 9 | Capturing each ready worker's uncommitted diff without disturbing it | C | Git-native (`git diff`/`git add -N`/`git reset`); see Part 6 findings below for the corrected procedure |
| 10 | Creating a disposable integration worktree | C | Native Git (`git worktree add`) |
| 11 | Applying each worker's patch (`git apply --3way --index`) | C | Native Git; validated experimentally, see below |
| 12 | Detecting a real conflict during apply | C | Native Git; validated experimentally |
| 13 | Deciding *when* to trigger assembly (wait for all three vs. a checkpoint) | **E** | Explicitly unresolved in `combined-candidate.md`; #334's early finish makes this wave the first real test |
| 14 | *Who* runs the capture/assembly/suite sequence (parent, fresh agent, a worker) | **E** | Explicitly unresolved in `combined-candidate.md`; observe |
| 15 | Running the full suite once against the combined worktree | C (mechanism) + D (deciding it's required, not run/skip) | The requirement itself is a research decision already recorded (`responsibility-boundaries.md`); running the command is mechanical |
| 16 | Reporting the combined result, red or green | D | Cross-worker by construction — no single worker can report on the union |
| 17 | If red, tracing which worker's change is implicated | E | Not exercised by either prior smoke test; genuinely open |
| 18 | Presenting each worker's Review implementation checkpoint in plain language, citing combined-suite evidence | D (presentation) + A (the report's substance, which review-it/verification.md already produce correctly) | `vision.md`'s already-recorded UX finding; not new to ST3 |
| 19 | Worker's Review implementation stop now requires combined-suite evidence, not its own full-suite choice | **B** | Needs the matching correction in `review-gates.md` (see below) |
| 20 | Human approves each worker independently | A (mechanism already validated) | ST2 already proved this works, including under ambiguous partial answers |
| 21 | Commit plan, per worker, after its own approval | A | Unchanged |
| 22 | No commit created before both approvals, for any worker | A | Already unconditional in `review-gates.md`/`commit-boundaries.md`; see "Current skill gaps" for why no change is needed here |
| 23 | Disposing the temporary integration worktree once real commits exist | C | Native Git (`git worktree remove`); validated experimentally |
| 24 | Convergence (push + merge per approved worker), serialized | A/D | Already validated worker-performed mechanism from ST2; serialization remains parent reasoning, unchanged by this smoke test |
| 25 | Push readiness, issue closure, task-checkbox validation | A | Unchanged; confirmed by direct reading of `push-readiness.md`/`issue-closure.md` — neither cares how a worker's pre-commit state was assembled |
| 26 | Recompute → zero open issues → hand off to `ship-it` | A | Unchanged; this would be the first smoke test to actually reach this hand-off, since #341–345 was the milestone's entire remaining open set |

## Current skill gaps

After reading `implement-it/SKILL.md`, `rules/verification.md`, `rules/review-gates.md`,
`rules/sequencing.md`, `rules/commit-boundaries.md`, `rules/push-readiness.md`,
`rules/issue-closure.md`, and `rules/worktree-preservation.md` directly (not from the prior docs'
quotations) against the desired lifecycle above:

**Real gap — the only one that blocks ST3 from being runnable as designed.** `verification.md`'s
"Targeted verification before Gate 1" step 4 is unconditional: "Then ask the human whether to run the
full regression suite for this issue or skip it." Nothing in the file's current text exempts a
concurrent worker from asking this, and `review-gates.md`'s "Review implementation" stop condition
("the verification appropriate to it has been run") is satisfied, on the current text, by exactly the
same steps a serial worker uses — there is no separate concurrent path to route into. Run literally, a
worker in this wave would ask its own full-suite question and then report Review implementation on its
own targeted evidence alone, precisely the per-worker full-suite choice the post-ST2 research decision
(`responsibility-boundaries.md`, "Combined verification") already removed. This is not a hypothetical
reading — it is what the current text, applied literally, produces.

**Not a gap: "narrowest meaningful broader regression scope."** The brief's own framing (from
`vision.md`) names this as a required per-worker tier distinct from targeted verification and the full
suite. Reading the installed `verification.md` directly: there is no separate rule for it. What exists
is step 1's "use the narrowest reliable scope that proves the implementation" — worded broadly enough
that a worker choosing to include a related surface (as every ST1/ST2 worker did unprompted — e.g.
#341's targeted run already spanned `Clients`, `Policies` Http tests, and two model/policy test files)
already fits inside it as worker judgment. Both smoke tests show this working correctly without a
named rule. No change proposed; this is Category A, already correctly specified via existing latitude,
not a gap ST3 needs fixed.

**Not a gap: the commit-boundary/approval invariant.** `combined-candidate.md`'s brief asked whether any
rule needs clarifying so that assembling the temporary combined candidate cannot be interpreted as
permission to commit. Read directly: `commit-boundaries.md`'s commit-plan derivation already starts only
after Review implementation is approved, and `review-gates.md`'s "No commit is created before Commit
plan is approved" is already unconditional and does not reference *how* the pre-commit state came to
exist. Structurally, the combined candidate is assembled *before* any worker's Review implementation is
even reported (per the desired lifecycle above) — no worker's own lifecycle reaches commit derivation
until its individual Review implementation is approved, which itself now requires combined-suite
evidence to exist first. There is no path through the current rules, with or without this document's
proposed correction, where "the combined candidate was assembled" could be read as "commit is
authorized." No change proposed. This matches the pattern `parallel-dry-run.md` and
`responsibility-boundaries.md` both already established for this file family: investigate the candidate
correction, find the existing wording already sufficient, and say so rather than adding anything.

**Not a gap: `sequencing.md`.** Its installed "Parallel workers in a delivery/phase milestone" section
already states the one structural fact ST3 needs (temporary branch, milestone branch as eventual
convergence target, convergence mechanics undefined) and says nothing about verification ordering or
gate timing — the two things this wave's actual new behavior touches. No additional sequencing rule is
needed for this wave; the branch mechanics ST2 already validated are unchanged by anything in this
document.

**Not a gap: push/closure.** `push-readiness.md`'s reachability check and `issue-closure.md`'s "ask
first"/closing/validation procedure both operate strictly after commits exist and are agnostic to how
the pre-commit state was assembled, confirmed by direct reading — neither file's text depends on knowing
whether a combined-candidate step happened. No change proposed.

## Combined-candidate mechanism review

`combined-candidate.md` recommends mechanism #6 — a disposable `git worktree`, `git diff HEAD` per
worker, applied with `git apply --3way --index`. This document tested that mechanism directly, in
scratch state, rather than accepting the recommendation on its own analysis. Setup: a throwaway repo
with two worker worktrees, each carrying a mix of a modified tracked file, a staged new file, a staged
deletion, a staged rename-shaped add, an untracked new file, and a modified binary file — then a fresh
integration worktree and the recommended apply sequence, then a deliberately conflicting third worker to
confirm conflict detection, then disposal.

**Confirmed correct, exactly as `combined-candidate.md` describes:**
- `git diff HEAD` correctly captures staged *and* unstaged changes to already-tracked content in one
  patch — modifications, deletions, and content-based renames (captured as delete+add, which `git
  apply` handles with no issue) all appeared correctly and applied cleanly.
- `git apply --3way --index` applied two workers' disjoint patches into a fresh integration worktree
  cleanly, correctly reproducing both workers' changes together with no manual intervention.
- A genuine textual conflict (two workers editing the same line) was detected loudly: `git apply`
  returned a non-zero exit code, left `<<<<<<< ours` / `>>>>>>> theirs` conflict markers in the file,
  and reported `UU` status — exactly the loud, pre-suite failure `combined-candidate.md` claims, not a
  silent corruption.
- The conflicted integration worktree discarded cleanly with `git worktree remove --force`, and the
  original worker worktrees were confirmed completely untouched throughout (`git status --porcelain`
  identical before and after) — the "worker state is not damaged" invariant held in every case tested.
- No commit object was created anywhere in this sequence, on any branch, at any point — the invariant
  `combined-candidate.md` treats as non-negotiable held throughout.

**A real gap in the mechanism's own description, demonstrated, not hypothesized.** `combined-candidate.md`'s
"Mechanics" section states the capture command as `git -C <worker-worktree> diff HEAD` and claims it
"captures its full uncommitted change (staged and unstaged)." Tested directly: **`git diff HEAD` does
not include untracked files at all**, under any flag combination that doesn't first stage them. A
worker's genuinely new file (exactly the shape of ST2's own new page components and test files) is
silently absent from the patch as written, with the apply step reporting nothing wrong — the omission is
silent, not loud, which is precisely the failure mode `combined-candidate.md` correctly identifies as
disqualifying for option #5 (filesystem copy) but did not identify in its own recommended mechanism's
literal command.

**A second, smaller gap, also demonstrated.** The recommended command as written omits `--binary`.
Tested directly: applying a `git diff HEAD` patch (no `--binary`) that touches a modified binary file
fails outright — `error: cannot apply binary patch to '<file>' without full index line` — not a silent
loss, but a hard failure the mechanism's own description does not anticipate.

**The corrected capture procedure, validated experimentally:**

```text
1. git add -N -- $(git ls-files --others --exclude-standard)   # mark untracked files intent-to-add,
                                                                  in the worker's own worktree
2. git diff HEAD --binary                                       # now includes untracked + binary content
3. git reset -- $(git ls-files --others --exclude-standard)     # undo step 1's staging immediately
```

Step 3 is required to satisfy `combined-candidate.md`'s own "worker state is not damaged" invariant —
tested directly: `git add -N` followed by `git reset` on the same paths restores the worker's worktree
to byte-identical `git status --porcelain` output, with no content change. Steps 1 and 3 briefly touch
the worker's own index; the desired lifecycle above already holds every worker paused at "ready for
combined verification" (not actively mutating its own worktree) by the time capture would run, which is
what makes this safe in practice — a reason to prefer capturing only from workers that have already
reached and reported "ready," never from one still implementing.

**Verdict: the recommended mechanism category (#6) survives this review; its literal command does
not, and needs the three-step correction above.** This is a correction to `combined-candidate.md`'s own
mechanics description, not a reason to prefer a different mechanism from its option list — #2 (stash) is
still destructive to the worker's worktree while running, #5 (filesystem copy) is still silently
conflict-blind, and #3/#4 (throwaway commits/cherry-pick) still touch the approval invariant directly.
Nothing tested here changes `combined-candidate.md`'s own ranking; it changes the exact command the
recommended option actually needs.

**Not tested here, left for ST3 itself:** applying against a real project's dependency-install/build
bootstrap cost; a conflict that requires re-applying an already-applied patch after adjusting an earlier
one at higher worker counts; and staleness propagation back to a worker whose content changes during
conflict resolution (`review-it/rules/verification.md`'s staleness rule would apply, per
`combined-candidate.md`'s own analysis, but no run has exercised it).

## Architectural-drift watch item

Per the brief's own caution against inventing a cross-worker architecture-review subsystem: no change
proposed. This wave is a weaker test of the drift ST2 found than ST2 itself was — #334, #344, and #345
touch three structurally unrelated areas (global nav, one page's filter UI, one policy class's detail
tab) with no shared naming pattern for the three workers to diverge on the way ST2's three
`routes/<entity>.php`/`<Entity>Controller` placements did. There is no comparable convention decision
point visible in these three issues' text.

What is worth recording as an observation, not a rule: assembling the combined candidate (this
document's actual subject) creates, incidentally, the same visibility `combined-candidate.md` already
noted — a human or `review-it` pass looking at the assembled integration worktree would see all three
workers' changes together before any of them commits, which is earlier visibility than either prior
smoke test had. Nothing in this wave's file-disjointness gives that visibility anything to actually
catch this time. Classify as: keep observing: if a future wave's parallel workers touch a shared naming
or convention surface again, note whether anyone looking at the assembled candidate actually notices
before approval — this wave, by its own clean-file-disjointness design, cannot generate that evidence
itself.

## Proposed minimum skill changes

Two files — the same file family, same conservative posture, as `parallel-dry-run.md`'s own two-file
patch for ST2.

### 1. `implement-it/rules/verification.md` — a concurrent worker skips its own full-suite choice

- **Current behavior:** step 4 of "Targeted verification before Gate 1" always asks the full-suite
  run/skip question, with no exception; "Gate 1 evidence" always requires that choice's result.
- **Evidence this is required:** the post-ST2 research decision (`responsibility-boundaries.md`,
  `vision.md`'s updated "Verification model") already removed the per-worker full-suite choice for a
  concurrent worker; nothing in the installed rule text reflects that removal. Applied literally today,
  a Smoke-Test-3 worker would ask a question the current research position says should not be asked.
- **Smallest change:** step 4 gains a one-clause exception routing a concurrent worker (identified by
  `sequencing.md`'s already-installed "Parallel workers" section) to a new short subsection instead of
  asking; that subsection states the worker reports "ready for combined verification" and stops, without
  specifying who assembles the candidate, when, or how — exactly the same restraint
  `sequencing.md`'s own patch already exercised about convergence. "Gate 1 evidence" gains a matching
  either/or clause.
- **Why here, not elsewhere:** this rule already owns exactly this decision point for the serial case;
  the concurrent case is a carve-out of the same decision point, not a new responsibility.
- **Portability:** fully portable — states a stop condition and a substitute evidence source, names no
  runtime.
- **Serial/single-worker behavior:** entirely unchanged — the exception only applies when
  `sequencing.md`'s parallel-worker condition already applies, which requires explicit prior human
  authorization of a concurrent wave.

### 2. `implement-it/rules/review-gates.md` — Review implementation waits for combined evidence

- **Current behavior:** "Review implementation" stops once "the verification appropriate to it has
  been run (`rules/verification.md`)" — a generic reference that, without change 1 above, resolves
  identically for a serial or concurrent worker.
- **Evidence this is required:** ST2 already demonstrated the exact failure shape this would otherwise
  reproduce: two of three workers built a complete Gate‑1 report *before* a required verification
  decision was actually resolved, because the ordering constraint lived only in `SKILL.md`'s summary
  sentence and not in the rule text a worker actually executes
  (`responsibility-boundaries.md`, "Skill findings"). Without an explicit wait-condition here, a
  concurrent worker could satisfy the letter of "the verification appropriate to it has been run" the
  moment its own `review-it` pass completes, before the combined-suite result the new research decision
  requires actually exists — repeating the identical class of ordering deviation on a different pairing
  of steps.
- **Smallest change:** one paragraph stating that for a worker in an authorized concurrent wave, this
  stop is reached only once the wave's combined verification result has been supplied to it, and that
  until then the worker holds in the state `verification.md`'s new subsection describes.
- **Why here, not an orchestrator:** this is an entry-condition timing clarification to an approval this
  rule already owns end-to-end — the approval mechanics, the report shape, and the requirement for
  explicit human approval are all completely unchanged.
- **Portability:** fully portable.
- **Serial/single-worker behavior:** unchanged — the clause is conditioned on the same parallel-worker
  authorization as change 1.

### Considered and rejected as unnecessary

- **A `sequencing.md` addition.** Investigated directly against the desired lifecycle; branch mechanics
  are untouched by anything in this wave. Not proposed.
- **A `commit-boundaries.md` clarification about the combined candidate.** Investigated directly; the
  existing "commit-plan derivation only starts after Review implementation is approved" already makes
  the sequencing question moot, since the combined candidate is fully assembled and disposed of *before*
  any worker's Review implementation is even reported. Not proposed.
- **A `push-readiness.md` or `issue-closure.md` clause.** Both already operate strictly post-commit and
  are agnostic to pre-commit assembly mechanics, confirmed by direct reading. Not proposed.
- **Any rule encoding the `git worktree`/`git diff`/`git apply --3way --index` mechanism itself.** This
  is Category C — native Git capability this document validated experimentally, not methodology. Not
  proposed, consistent with every prior document's "do not reinvent runtime mechanics" stance.
- **Any rule assigning ownership of *who* runs the combined-candidate mechanism.** Explicitly left
  unresolved in `combined-candidate.md`, and this document adds no new evidence resolving it before ST3
  runs. Not proposed.

## Proposed unified diffs

```diff
--- a/implement-it/rules/verification.md
+++ b/implement-it/rules/verification.md
@@
 1. Run the project's targeted verification for the changed behavior. This is mandatory when the project
    provides a meaningful targeted mode; use the narrowest reliable scope that proves the implementation.
 2. Run the applicable formatter/linter/static-analysis checks at their narrowest reliable scope.
 3. Inspect the results for failures, warnings, or limitations that could affect the claim being made.
-4. Then ask the human whether to run the **full regression suite for this issue** or skip it.
+4. Then ask the human whether to run the **full regression suite for this issue** or skip it — unless
+   this is a worker in a human-authorized concurrent wave (`rules/sequencing.md`'s "Parallel workers in
+   a delivery/phase milestone"), in which case skip this step and see "Concurrent workers in a parallel
+   wave" below instead.
 
 The targeted check is the required implementation proof. The full suite is a separate regression choice.
 Do not silently decide that a full suite is required merely because the issue is complete.
@@
 If the human chooses to skip it, report that choice explicitly at Gate 1. Do not describe targeted tests
 as full-regression proof.
 
+### Concurrent workers in a parallel wave
+
+A worker executing as part of a human-authorized concurrent wave does not make the full-suite choice
+above at all — that choice, and the full-suite run it may trigger, belong once to the wave's combined
+candidate state, not per worker. Once targeted verification (steps 1–3 above) and `review-it` are
+complete, report the implementation as ready for combined verification and stop — do not proceed to
+Review implementation yet, and do not ask the full-suite question. Combined verification's result, once
+supplied, supplies the regression evidence this worker's own Review implementation report will cite in
+place of step 4 and "Full-suite choice" above (`rules/review-gates.md`'s "Review implementation — first
+approval (Gate 1)").
+
+This section does not change the full-suite choice for a single worker running alone, and does not
+specify how, by whom, or when the combined candidate state is assembled or verified — that stays
+outside this rule.
+
 ## Gate 1 evidence
 
 Gate 1 requires:
 
 - approved scope implemented;
 - targeted verification complete;
 - applicable code-quality checks complete;
 - `review-it` clean, or findings fixed and re-reviewed;
-- the human's explicit full-suite choice, including the result if run or an explicit skip.
+- the human's explicit full-suite choice, including the result if run or an explicit skip — or, for a
+  concurrent worker, the wave's combined verification result in its place (see "Concurrent workers in a
+  parallel wave" above).
 
 A full-suite result is evidence of regression coverage, not authorization. Gate 1 remains the human's
 approval of the implementation report.
```

```diff
--- a/implement-it/rules/review-gates.md
+++ b/implement-it/rules/review-gates.md
@@
 Stop here once:
 
 - the approved scope has been implemented — the approved issue, for ordinary implementation work,
   or the explicitly authorized correction, for a delivery correction (see "Consuming review-it's
   result," below, for how each supplies `review-it`'s intended scope);
 - the verification appropriate to it has been run (`rules/verification.md`);
 - `review-it`'s pass against the completed implementation is either clean, or its findings have
   been resolved and re-verified.
 
+For a worker in a human-authorized concurrent wave (`rules/sequencing.md`'s "Parallel workers in a
+delivery/phase milestone"), "the verification appropriate to it" is `rules/verification.md`'s
+"Concurrent workers in a parallel wave" path, and this stop is reached only once that wave's combined
+verification result exists and has been supplied to this worker. Until then, hold in the "ready for
+combined verification" state that section describes rather than reporting Review implementation early.
+
 Invoke `review-it` standalone against the completed working tree once the first two bullets hold,
 before reporting at this approval stop — see "Consuming review-it's result," below. A `review-it`
 pass does not grant authorization by itself; it is evidence this report cites, and Review
 implementation's approval mechanics — the report below, then explicit human approval — stay exactly
 as they were.
```

### Self-challenge (per the brief's Part 8)

- **Removed before this draft:** an earlier version of this proposal included a third hunk in
  `commit-boundaries.md` restating the no-commit invariant for the combined-candidate case. Removed
  after re-checking `commit-boundaries.md`'s actual installed text directly — the existing "derivation
  only starts after Review implementation is approved" already makes the restatement redundant; keeping
  it would have been adding a sentence the rule already implies, which the brief's own challenge step
  asks to cut.
- **Removed before this draft:** a clause in `sequencing.md` pointing at the new verification path.
  Removed because nothing in the desired lifecycle requires a worker to consult `sequencing.md` to learn
  about combined verification — it learns that from `verification.md`/`review-gates.md` directly, the
  same two files change 1/2 already touch.
- **Not added:** any statement about *when* assembly triggers or *who* performs it. Both remain
  Category E per the classification table; adding either would be exactly the kind of premature
  ownership assignment `orchestration.md` and `combined-candidate.md` both warn against.
- **Not added:** anything about the `--3way`/untracked-file/binary corrections this document's mechanism
  review found. Those are runtime/Git mechanics (Category C), not methodology, and belong to whoever
  executes the mechanism in ST3 — not to a skill rule.
- **Confirmed unchanged:** re-reading both diffs against the full `verification.md` and `review-gates.md`
  text one more time — the full-suite choice for a serial worker, the two-approval structure, the
  report shapes, and "no commit before Commit plan" are all untouched by either hunk.

## Runtime/parent responsibilities

Everything in this section stays outside any skill file for this smoke test — Category C (native Git)
or Category D/E (parent-session or genuinely unresolved), per the classification table above.

- **Launching three isolated background workers on temporary branches** — native runtime, already
  validated twice (ST1, ST2).
- **Capturing each ready worker's diff, creating the integration worktree, applying patches, running the
  suite once, disposing the worktree** — native Git, validated experimentally in this document's
  "Combined-candidate mechanism review," using the corrected three-step capture procedure. *Who*
  performs this sequence — the parent session itself, a fresh short-lived agent, or something else — is
  not decided here, consistent with `combined-candidate.md`'s own position.
- **Deciding when to trigger assembly**, given #334 will likely reach "ready" well before #344/#345 —
  genuinely untested by either prior smoke test; this wave's own speed mismatch (deliberately kept, see
  "Candidate wave") is what should generate the first real evidence.
- **Presenting the combined result and each worker's Review implementation checkpoint in plain
  technical language** — the parent's own responsibility today, per `vision.md`'s already-recorded UX
  finding; not new to this smoke test.
- **Routing each human approval to the correct waiting worker** — native `SendMessage`/`resumedAgentId`
  plus the parent's own conversational tracking, already validated by ST2 under two ambiguous cases.
- **Serializing convergence once multiple workers are approved** — already validated by ST2; this smoke
  test does not need to re-prove it, only confirm it still holds once combined verification precedes it.
- **Tracing a red combined suite, or a real apply conflict, back to the responsible worker** —
  genuinely unexercised by either prior smoke test; if either occurs in ST3, record what actually
  happens rather than assuming a procedure.

## Unknowns deliberately left for ST3

Carried forward and narrowed from `combined-candidate.md`'s own "What remains unresolved," restated
against this specific wave:

- **Who runs the capture/assembly/suite-run sequence.** Not decided here.
- **When assembly triggers**, specifically now testable because #334 will very likely reach "ready"
  materially before #344 or #345 — does the parent wait for all three, or does something else happen?
  Record what actually happens; do not assume either answer in advance.
- **Whether a real conflict occurs at all.** This wave was deliberately kept file-disjoint per the
  brief's own instruction, so none is expected — but confirm this rather than assume it, and if one
  occurs anyway (e.g. through an unexpected shared import or shell-component edit), record how it was
  detected and who resolved it, since no prior run has exercised this.
- **Whether the corrected three-step capture procedure (intent-to-add, diff --binary, reset) actually
  works cleanly against real, larger diffs** — validated only against a synthetic scratch repository in
  this document, not against useOrbit's actual Vue/PHP change shapes, generated files (Wayfinder
  regeneration, compiled assets), or dependency/build bootstrap cost in the integration worktree.
- **Whether the two-file `verification.md`/`review-gates.md` correction is sufficient**, or whether a
  worker still finds an ambiguity in practice the way two of three ST2 workers did for the
  `review-it`-before-full-suite ordering — this document's correction is modeled directly on that
  failure shape, but has not itself been run.
- **Whether presenting the combined result in plain technical language actually happens correctly**,
  or reproduces ST2's gate/rule-vocabulary leakage — `vision.md`'s UX finding is recorded but unfixed by
  any rule; this smoke test is an opportunity to observe it again, not a guarantee it improved.
- **Whether the final authoritative branch/worktree state gets checked**, so ST2's own "stale local
  checkout" finding (the main worktree's local `feat/policies-http-frontend` ref was left behind after
  convergence, only the remote ref advanced) doesn't silently recur a second time.

## Exact success criteria

Marked M (validates methodology / the two-file skill correction) or R (validates runtime/parent
behavior, not methodology).

- [M] Each of the three workers runs targeted + narrowest meaningful broader verification and
  `review-it`, and none asks its own full-suite run/skip question.
- [M] Each worker reports itself "ready for combined verification" and stops — no worker reaches Review
  implementation before combined verification exists.
- [M] No worker creates a durable implementation commit before its own explicit Review implementation
  *and* Commit plan approvals, in that order, both received.
- [R] The parent (or whatever actually performs it) assembles the three ready workers' uncommitted
  diffs into one temporary combined worktree without creating any commit anywhere.
- [R] Each original worker's own worktree, branch, and diff remain completely unaffected by the
  combined-candidate assembly, confirmed by inspection after the fact.
- [R] The full project suite runs exactly once against the assembled combined worktree, using the
  project's genuine full-regression mode.
- [M] No worker's Review implementation checkpoint is presented to the human before that combined suite
  result is known and green.
- [M] Each worker's Review implementation checkpoint, once presented, cites its own substantive
  `review-it` result and its own targeted/broader verification evidence, plus the shared combined-suite
  result — worded in plain technical language, not internal gate/rule vocabulary.
- [R] The human can approve #334, #344, and #345 independently, in any order, and only the approved
  worker resumes each time — siblings preserve whatever state they were left in.
- [M] Each approved worker derives and presents its own Commit plan only after its own Review
  implementation approval, and creates commits only after its own Commit plan approval.
- [R] Convergence (push + merge per approved worker into `feat/policies-http-frontend`) is
  worker-performed and serialized with no race, as ST2 already validated.
- [M] Push readiness and issue closure run correctly, unmodified, for all three issues once their
  commits exist, including checked task boxes independently re-verified against live GitHub state.
- [R] The temporary integration worktree is disposed of (or reconstructed, if reused mid-run) with
  nothing about it ever mistaken for durable state.
- [R] After convergence, the *local* `feat/policies-http-frontend` ref in the main checkout is
  explicitly checked against `origin/feat/policies-http-frontend`, so ST2's stale-local-branch finding
  is caught rather than silently repeating.
- [M] With all three issues closed, the recompute correctly reports zero open issues remaining and hands
  off to `ship-it/rules/milestone-pr-readiness.md`.

## Recommendation

Apply the two minimal diffs above to `implement-it/rules/verification.md` and
`implement-it/rules/review-gates.md`, on top of the already-installed (currently uncommitted)
`sequencing.md`/`worktree-preservation.md` patch from Smoke Test 2. Then run Smoke Test 3 against #334,
#344, and #345, using the corrected three-step diff-capture procedure this document validated
experimentally (`git add -N` on untracked paths, `git diff HEAD --binary`, immediate `git reset` to
restore worker state) for whatever assembles the combined candidate. Do not pre-decide who performs that
assembly or when it triggers relative to #334's early finish — both are exactly what this smoke test
should observe. Do not manufacture a file conflict; this wave's genuine disjointness is a feature of
this run, not a limitation of it — a conflict-specific wave, if wanted, is better run as its own,
separate, deliberately-shaped smoke test rather than layered onto this one. Update
`combined-candidate.md`'s "Mechanics" section with the corrected capture procedure regardless of how
Smoke Test 3 itself goes, since that correction is independently demonstrated and not contingent on the
smoke test's outcome. Update `smoke-test-2.md`/`responsibility-boundaries.md`/`orchestration.md` with
whatever Smoke Test 3 actually observes about assembly timing and ownership before treating either as
settled enough to extract into anything.
