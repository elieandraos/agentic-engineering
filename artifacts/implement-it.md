# implement-it — Architecture Dossier

Status: Current
Scope: `implement-it` as it stands in this repository
Purpose: A compact lifecycle architecture guide — what enters and exits the workflow, its two
delivery paths, branch readiness, its two review gates including `review-it`'s role at Gate 1, its
commit architecture, its verification model including the completed-issue reuse rule and worktree-
provenance preservation, issue closure and approval-validity, sequencing and the ready-set recompute,
authorized delivery corrections, which decisions require human authority, where each rule owns a
distinct part of the lifecycle, and current boundaries and confidence.
[`SKILL.md`](../skills/implement-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/implement-it/README.md) is the human-facing walkthrough. This document
explains the lifecycle architecture behind both rather than restating either.

## 1. Purpose and entry boundary

`implement-it` begins from any approved, implementation-ready GitHub issue — whether
[`plan-it`](../skills/plan-it/) drafted it or it already existed some other way — and carries that
single issue's work through verified Git/GitHub implementation, ending at issue closure and the
next-issue recommendation. What matters for entry is that the issue meets `plan-it`'s own quality bar
(`rules/issue-conventions.md` and `rules/review.md`) and carries the human's approval to implement
it — not who drafted it; this skill does not recreate or replan an issue that already meets that bar
merely because `plan-it` didn't produce it.

A second, separate entry route exists with no issue prerequisite at all: an explicitly
human-authorized delivery correction handed to this skill by [`ship-it`](../skills/ship-it/) (§9).

This skill does not discover product scope, decide what work should exist, or make an unresolved
product or architecture decision on its own — every one of those questions belongs upstream, and a
genuine gap in any of them is a reason to stop and ask, not a reason to improvise past it (§10).
GitHub is not incidental tooling this skill happens to use: Git and GitHub are intentional core
substrate for the methodology itself — reference syntax, mutation/re-fetch discipline, and the
shape of a milestone, issue, and release are all load-bearing architecture here, not an abstraction
layer meant to be swapped for another tracker.

## 2. Two delivery paths, one shared core

Every issue this skill picks up belongs to one of two paths, distinguished by which kind of
milestone it belongs to — a persistent catch-all/Backlog milestone, or a bounded delivery/phase
milestone intended to ship as a release (a classification `plan-it` makes, not this skill):

- **Backlog/hotfix path.** Work happens directly on the repository's trunk branch. There is no
  branch decision, no shared branch, and no PR at the end of it — the issue closes and the path
  ends there, entirely inside this skill. It never reaches `ship-it` at all.
- **Milestone path.** Every issue in the milestone shares one working branch. Issues close
  individually on that branch, well before the branch is ever proposed as a PR. Only once every
  issue in the milestone is closed does the path hand off to `ship-it`'s milestone PR readiness.

Both paths share the identical core: branch readiness, implementation, the two review gates,
semantic commit construction, verification, and issue closure are exactly the same mechanics either
way — a Backlog issue is not a lighter-weight version of a milestone issue. What differs is what
happens *after* closure: a Backlog closure is terminal; a milestone closure feeds a shared branch
that eventually needs its own readiness check, its own PR, and its own post-merge lifecycle, all
owned by `ship-it`. The lifecycle, end to end:

```
pick a dependency-ready, approved issue
  → BRANCH READINESS (§3)                      [diverges by path]
  → implement → full-suite verification
  → GATE 1: implementation review, review-it invoked (§4)
  → derive commit plan
  → GATE 2: commit-plan review (§4)
  → build semantic commits, narrowest-reliable verification per commit (§5, §6)
  → full-suite verification at the completed-issue boundary, fresh or reused (§6)
  → confirm commits reachable on the correct remote branch, push with authorization if not (§7)
  → ask: close the issue? → closure procedure + validation (§7)
  → recompute the milestone's dependency-ready set (§8)         [Backlog: path ends here]
      → ready set non-empty → report/recommend, human picks the next issue (new pass)
      → open issues remain, all blocked → report the blockers, no handoff
      → zero open issues remain → hand off to ship-it's milestone PR readiness
```

## 3. Branch readiness

Before implementation starts, this skill determines which branch the work happens on — and for a
Backlog/hotfix issue, determines that no branch decision exists at all.

**Backlog/hotfix.** This work runs directly on the repository's trunk branch — never a newly
created feature branch. Which branch a given repository actually treats as trunk is discovered from
the repository itself, never assumed from a fixed, common name. If the current checkout isn't that
branch when the work begins, the mismatch is surfaced to the human rather than silently proceeding
on whatever happens to be checked out, and the branch is never silently switched on the workflow's
own initiative.

**Milestone work.** Every issue in a delivery/phase milestone shares one branch. The current branch
is inspected first; if it already is the milestone's branch, implementation proceeds directly. If
not, a branch name is recommended — derived from the milestone's actual nature and scope, never a
rigid, enforced prefix taxonomy — and the human is asked before anything is created or switched to.
Only once the correct branch is confirmed active does implementation begin.

Branch choice is evidence-driven throughout, never hard-coded: trunk's actual name, a milestone
branch's actual name, and whether the current checkout matches either are all read from the
repository's real state at the moment work starts, not inferred from a template or a naming
convention assumed in advance. A stale or unexpected branch is always surfaced, never silently
worked around — for Backlog/hotfix by refusing to proceed off-trunk, and for milestone work by
asking before changing anything.

## 4. Two review gates

Two separate human approvals gate everything before commits exist, and neither substitutes for the
other:

- **Gate 1 — implementation review.** Stops once the approved scope is implemented — the approved
  issue, for ordinary work, or the explicitly authorized correction, for a delivery correction
  (§9) — the verification appropriate to it has run (§6), and
  [`review-it`](../skills/review-it/)'s pass against the completed implementation is either clean or
  its findings have been resolved and re-verified. This third bullet is new relative to this skill's
  predecessor: `review-it` is invoked standalone against the completed working tree before Gate 1's
  report, supplied with whichever intended-scope evidence this invocation actually has (the approved
  issue, or the authorized correction's scope and evidence). A `review-it` pass is evidence Gate 1's
  report cites — it does not grant authorization by itself, and Gate 1's own mechanics (the report,
  then explicit human approval) are otherwise unchanged. `review-it`'s own architecture — its
  checklist, its verification and staleness discipline — is not restated here; see its own dossier.
- **Gate 2 — commit-plan review.** Only after Gate 1 is approved: the finished diff is inspected, a
  semantic commit plan is derived and presented — grouping, order and its rationale, which tests
  travel with which commit, draft messages, and the issue-reference trailer — and no commit is
  written until the human approves that plan explicitly. A partial correction to part of the plan is
  never treated as approval of the rest of it.

Gate 2 can never substitute for Gate 1, because they prove genuinely different things: the same
finished diff can be split into commits several defensible ways, and approving that the
*implementation* is correct says nothing about which of those splits should become permanent
history. An agent may investigate and recommend at either gate, but never converts a genuinely
unresolved product/architecture decision, a contradiction between evidence and approved
assumptions, a `review-it` finding revealing such a decision, or a commit decomposition with no
clearly better answer into a silently-chosen fact — each of those is its own stop, reported with
evidence and a recommendation, not an unexplained question.

**Approval validity before Gate 2 and before push.** An approval is scoped to what it actually
reviewed — work, scope, or a proposed action moving on afterward doesn't automatically carry the
approval forward. Before Gate 2, and again before requesting push authorization, this skill checks
that the current work, scope, and proposed action still match what the relevant approval actually
covered: a material change (a scope change since Gate 1, a diff that no longer matches what Gate 2
approved, an issue body edited since its own approval) invalidates the approval that covered the
prior state and requires renewal, routing to `review-it`'s own staleness contract where the change
affects a surface it already reviewed. This check exists to catch a real divergence, not to
manufacture one: ordinary staging and assembling of unchanged, already-approved content into its
already-approved commits must not automatically invalidate Gate 1 merely because `HEAD` moved or the
remaining diff changed shape. Remote commit reachability proves presence, not verification or
authorization — finding a commit already on the remote branch is not evidence Gate 1, Gate 2, or
push authorization ever actually happened for it.

Both gates apply at the same cadence sequencing establishes for everything else in this lifecycle
(§8): one Gate 1 and one Gate 2 per issue, by default. A milestone having broad, already-approved
scope is never read as authorization to skip or batch either gate across more than one issue; a
human-approved exception to that default is a deliberate, explicit grant, not evidence the default
should be read more loosely going forward.

## 5. Commit architecture

A commit is not a mechanical split of an issue. An issue describes an outcome; a commit describes
one coherent, independently-true implementation decision — and nothing forces those two counts to
match. Neither "one commit per issue" nor "many small commits" is a default: commit count is
discovered from the actual, finished, reviewed diff every time, never decided in advance from issue
size, file count, how many directories or file types are touched, or how an earlier change happened
to split. A large diff can be one commit if it's one decision applied consistently everywhere it
reaches; a small diff can be several commits if it genuinely contains several decisions.

**Coherence is the actual test**, and it is narrower than "deployable" or "user-visible": every
semantic commit must leave a structurally valid state that does not depend on a later commit to
become structurally valid. A commit can be inert — dead code today, live once something later
activates it — and still be coherent, as long as it is structurally complete and correct on its own
terms; a commit that references a definition only a later commit introduces is never coherent, no
matter how small it is.

**Ordering is dependency-sensitive on two independent axes.** Commits are first ordered by
structural dependency — the order one decision must exist before another can build on it. A second,
narrower concern layers on top: a commit that flips a runtime activation gate (a feature flag,
environment-conditioned behavior) can retroactively make previously dormant tests and code paths
active the instant it lands, so an activating commit must land only after everything it activates —
including a pre-existing test unrelated to the current issue — is already present in an earlier
commit (`rules/activation-ordering.md`, summarized at §6). These two orderings have not been
observed to conflict; no precedence rule exists for the case where they might (§11).

**Deriving the plan requires inspecting the completed, approved implementation diff and the intended
commit scope it actually contains** — the real diff, file by file, not necessarily an already-staged
scope — never planning boundaries speculatively while still writing code, and never copying how a
superficially similar earlier change happened to split.

**An unpushed commit and already-pushed history are corrected differently.** A review correction
found before anything is committed simply becomes part of whichever semantic commit it belongs to —
there is never a separate "fix review comments" commit. A correction needed after something is
already committed, but before that commit has been pushed, is folded in by rebuilding local history
so the correction lands inside the commit it actually belongs to, rather than bolting a fixup commit
on top — the result reads as if it had been built correctly from the start. The current rules
describe this reconstruction only for commits that haven't been pushed yet; they don't define a
technique for rewriting history that has already been shared, consistent with commit history being
treated as effectively immutable once it leaves the local, unpushed state.

**Reconstruction preserves unrelated content and its staged/unstaged shape, and is bounded to what
it can safely classify.** Every path the correction touches is captured before anything is mutated,
and the correction itself is isolated positively — never derived by subtracting a known piece from
the combined content — so unrelated content sharing the same file is never folded into the
correction or silently lost. This recipe supports a path only when its unrelated content, if any,
resolves cleanly to one of a small number of classifications relative to `HEAD` (none, fully staged,
or fully unstaged); a path where the correction can't be cleanly separated from every other
difference, or where the unrelated content's staged/unstaged shape can't be established that way,
falls outside what this recipe supports.

Two different failure points call for two different responses, not one. A **preflight separation or
classification failure** — the correction can't be cleanly isolated from every other difference, or
the unrelated content's staged/unstaged shape can't be established — is detected before any real
mutation: nothing has yet been cleared, staged, or reset, so the procedure stops and reports the
specific obstacle, leaving the repository exactly as found. A **restoration failure**, by contrast,
can only surface after reconstruction has already happened — once the owning commit has been rewound
and the semantic commits already rebuilt — when reapplying a correction-touched path's set-aside
unrelated content back against its new, reconstructed content fails to merge cleanly. At that point
the real repository already carries the reconstructed commits; the procedure stops and preserves the
captured recovery data (the scratch location's contents) for a retry or a hand-off, rather than
guessing at a resolution or discarding anything — it does not, and cannot, undo the reconstruction
that already happened. `rules/commit-boundaries.md`'s "Review corrections fold into their semantic
commit" classifies which of the two cases applies and hands the reconstruction case to
`rules/commit-reconstruction.md`, which owns the full mechanics; this dossier does not restate
them.

## 6. Verification model

Verification proves different things at different boundaries, and one never substitutes for
another: that the changed behavior is actually correct, and that the specific commit boundary being
built or already built is itself structurally sound. A full-suite run before Gate 1 proves the
complete working tree works, before any commit history exists to split; a check at the
completed-issue boundary, after every commit is assembled, proves the final commit history —
however many commits it became — reconstructs that same correct result. These are not duplicates of
each other even when the same command produces both results, and both checkpoints stay required.

**Tooling is discovered per repository, never assumed.** This skill prescribes no test runner,
formatter, linter, or static analyzer, and no fixed command for any of them — what each tool is,
what it can and can't scope to a narrower subset, and what the project's full regression command
actually is are all read from the repository's own instructions, configuration, and established
usage. The same discovery discipline extends to whether the current checkout's starting state
actually matches what the real delivery boundary (CI, a fresh clone) would start from — a
proportional, risk-based check, not a blanket requirement to reset the environment before every
ordinary change.

**Preserve pre-existing worktree changes.** A starting or resumed session can encounter a worktree
that already carries content this session didn't create. Recency, being uncommitted, or resembling
the approved issue's scope does not by itself prove a change belongs to this session — appearance is
not provenance. This skill uses whatever reliable provenance is actually available — `git reflog`
(which establishes commit/ref history, not authorship of an uncommitted edit), the session's own
recorded start point, or an explicit statement from the human — and asks only when unresolved
provenance would materially affect whether it's safe to continue, never discarding work merely to
obtain a clean checkout.

**Targeted verification is the default while building commits; broad verification is reserved for
specific moments.** While constructing each semantic commit, verification runs at the narrowest
scope that reliably proves that one decision — falling back to a tool's broader mode only where the
project's tooling genuinely can't scope narrower. The full regression suite's own pass/fail signal
never softens regardless of project history; a separate, narrower allowance exists for lint/
format/static-analysis debt specifically — pre-existing, unrelated violations are tolerated, the
standard is that this work introduces no new failures.

**Completed-issue verification: run or reuse.** The full suite runs again by default at the
completed-issue boundary — the only correct choice whenever reuse's applicability can't actually be
established. Reuse of an earlier full-suite result is permitted, from either the pre-Gate-1 run or a
run already executed directly against the final committed state (e.g. isolation verification's last
per-commit run, when nothing remained stashed afterward), only once four conditions all hold:
identifiable evidence of an actual successful, complete run (never merely remembered); the final
committed content matching the tested content (never inferred from a clean worktree, an unchanged
`HEAD`, or a successful commit command alone — established directly, for example by confirming the
assembled commits' combined diff against the pre-Gate-1 starting point matches exactly); equivalent
relevant test inputs and environment, including any commit metadata the project's own checks
consume; and no unresolved limitation undermining that equivalence. A cache hit, a replayed result,
or a subset selected through impact analysis can never by itself satisfy the first condition. Any
relevant change since the reused run — including a post-Gate-1 correction, from a `review-it`
finding or otherwise — requires a fresh run; a narrower per-commit check never substitutes where the
full suite is required. Reuse is reported honestly: which execution actually satisfies the
checkpoint, and why it still applies — never presented as freshly executed.

**Isolation verification proves an intermediate committed state itself, and is a deliberate
escalation, not the default.** Commit, set aside everything not yet committed, run the full
verification against exactly what's landed so far, then restore the rest and repeat for the next
commit. This is reserved for when a commit's standalone correctness genuinely needs proving on its
own — reconstructing history after the fact, or an ordering where a later commit's correctness
depends on an earlier one already being in place — not invoked merely because an issue happened to
split into multiple commits. Its final per-commit run, when nothing remains stashed afterward,
directly satisfies the completed-issue checkpoint under the reuse conditions above.

**Ordering commits around activation risk** is `rules/activation-ordering.md`'s own procedure, not
`verification.md`'s — before treating dependency order as final, `verification.md` requires
checking each commit against runtime activation (configuration, a feature flag,
environment-conditioned behavior) and hands off to the extracted rule only when that check finds an
effect. `rules/commit-boundaries.md`'s dependency ordering and this activation-safety ordering have
not been observed to conflict; no precedence rule exists for if they do (§11). Reaching this
procedure is itself one of the examples that can also trigger isolation verification, above, when
the activation step's own intermediate state needs proving — `verification.md` owns that decision.

## 7. Issue completion and closure

Closure is opt-in and only ever asked once committed, verified work exists — never automatically
inferred from a green build, and never repeated unprompted once the human has said not yet.

**Closure also requires the issue's commits to already be reachable on the correct remote branch** —
the repository's trunk for Backlog/hotfix work, or the milestone's shared branch otherwise, exactly
as branch readiness (§3) selected. If they aren't yet, this rule asks for explicit authorization to
push them — a permission check for a mutating remote action, not a third review gate alongside Gate
1 and Gate 2 (§4) — then pushes normally, never with `--force`, and re-fetches the remote branch to
confirm both that nothing local remains unpushed and that every commit implementing the issue is
specifically an ancestor of it. Either way — commits already remote, or newly pushed — this skill
confirms Gate 1/Gate 2 approval validity (§4) before advancing toward closure; remote presence never
substitutes for that confirmation. This reachability check is not itself a milestone or release
event: it doesn't create, review, or merge a PR, doesn't trigger a release or milestone closure, and
isn't a reason to rerun the completed-issue full-suite verification that already proved those
commits correct.

**A completion criterion must be satisfiable at the point this workflow actually closes the
issue.** Before asking to close, the issue's own stated Acceptance Criteria or Tests are checked
against this workflow's real closure timing — for example, a criterion requiring a real CI run
against a PR, when this issue closes, by this workflow's own design, before any PR for its milestone
exists yet. A contradiction like that is surfaced, not silently closed past; resolving it (closing
anyway with the gap disclosed, deferring the criterion to the boundary where it can actually be
proven, or sending it back for a wording correction) is the human's call, not this rule's.

**The closure procedure runs in a fixed order once approved:** check off only the Tasks that are
genuinely complete, explaining any intentionally deferred or trimmed one instead of silently
checking it off; write a durable closing comment — what was implemented, verification results
(including whether the completed-issue checkpoint was satisfied by reuse, and which earlier run),
the actual commits that implement the issue, and anything discovered during implementation or review
a future reader would otherwise have to reconstruct; persist the updated body and comment, then
close; and only then re-fetch the live result. Validation checks three things independently: the
issue is actually in a closed state, the checked-task count matches what was genuinely completed,
and the closing comment actually exists — a mutation's exit code is never treated as proof of any of
them.

**Closing an issue is a distinct fact from merging a milestone PR.** This closure intentionally
happens before a milestone's PR merges — for a milestone issue, often well before that PR even
exists, though never before its own commits have reached that milestone's branch. Closure marks that
this issue's implementation and verification are done; it says nothing about whether its commits
have reached the trunk branch, and nothing about the aggregate state of the milestone that contains
it. This rule also never reopens a closed issue on its own — a later finding concerning already-
closed work defaults to a new issue referencing the original.

## 8. Sequencing: the ready-set recompute and the no-chaining default

Only after a validated closure does this rule act. It lists the milestone's remaining open issues,
reads each one's actual dependency information exactly as `plan-it`'s established convention records
it, and classifies each as ready (every dependency closed, or none stated at all) or blocked
(waiting on something still open). The result is reported in categories — newly ready because of
this closure, already ready, still blocked and on what — never as a flat list.

**Dependency order is not the same thing as issue numbering, milestone membership, or drafting
order.** Readiness is computed purely from the real dependency graph the issues themselves declare.
A recommendation for which ready issue to pick up next is offered when the evidence genuinely
supports one, and presented as a real choice between comparable options otherwise. A recommendation,
and even an immediate, unambiguous human answer, is never itself authorization to start
implementing.

**The default cadence is one issue at a time, with an explicit stop between each.** Recomputing and
reporting the ready set ends this workflow pass; starting the next issue is always a new pass, with
its own explicit authorization — never a continuation folded into the current one, even when the
human's answer arrives instantly.

**An empty ready set is not automatically a handoff.** For a Backlog/hotfix issue, an empty ready
set means nothing further — there's no milestone graph to exhaust. For a delivery/phase milestone,
recomputing after a closure can find zero dependency-ready issues for two different reasons that
demand different responses: **zero open issues remain** — the milestone genuinely has nothing left,
report the empty set and hand off to `ship-it`'s milestone PR readiness; or **open issues remain, but
every one of them is currently blocked** on something that hasn't closed yet — the milestone is not
done, report the blockers, and do not hand off. Only the first case reaches `ship-it`; this skill
does not check that gate's own conditions (final manual testing, whether it found anything) itself —
it only recognizes the zero-open-issues state and points to where that question gets answered.

## 9. Delivery corrections

This skill accepts a second, distinct entry route: when `ship-it` investigates a CI failure on an
open milestone PR, determines a correction stays within already-approved scope, and the human
explicitly authorizes it, `ship-it` hands the authorized fix to this skill. Acceptance requires the
human's explicit authorization actually accompanying the handoff — `ship-it`'s own determination that
a fix stays in scope is necessary but never sufficient by itself; without that authorization there is
nothing yet for this skill to perform.

Once accepted, the correction proceeds through this skill's ordinary lifecycle — Gate 1 and Gate 2 as
applicable, invoking `review-it` standalone before Gate 1 the same way as ordinary work, verification
(§6), commit construction (§5), and authorized push (§7) — whether or not the original issue is still
open. This route stays available without requiring an open issue to exist; it does not require
reopening a closed issue, and it is distinct from genuinely new scope, which still routes through
`plan-it`'s discovered-work intake instead. Once the correction is verified and pushed, `ship-it`
resumes the delivery workflow — re-running real CI and reporting; a further failure returns to
`ship-it`'s own investigation, repeating from there.

This is the same lifecycle already described in §1-§8, applied to a correction instead of a fresh
issue — not a second procedure. See [`ship-it`'s own dossier](ship-it.md) §4 for the investigation/
authorization half of this split, which this skill does not perform.

## 10. The human-decision model

Certain decisions are always surfaced to the human rather than assumed, each at a specific point in
the lifecycle already described above:

| Decision | Surfaced at |
|---|---|
| Whether the implementation is acceptable | Gate 1 (§4) |
| Whether the proposed commit boundaries and messages are acceptable | Gate 2 (§4) |
| Whether to push already-approved commits to the correct remote branch | Push readiness, before issue closure (§7) |
| Whether to close the issue now | Issue closure (§7) |
| Which ready issue to start next, and whether to start it now | Sequencing (§8) |
| Approving any deviation from the normal per-issue cadence or gate structure | Review gates / sequencing (§4, §8) |
| Authorizing a delivery correction, and confirming its scope stays within what was already approved | Delivery corrections (§9), gated by `ship-it` before the handoff |

A stop is always a report plus a question, never a bare question or an unexplored wall of options:
investigate enough to understand the decision, state the relevant evidence, offer a recommendation
when the evidence supports one, then let the human decide. Ordinary engineering choices that
approved scope, repository convention, and available evidence already resolve are not a reason to
stop — a stop is reserved for a genuinely missing decision, a contradiction between evidence and
approved assumptions, a `review-it` finding revealing such a decision, or a choice the evidence can't
narrow down on its own.

## 11. Rule ownership and cross-skill handoffs

| Rule | Owns |
|---|---|
| [`sequencing.md`](../skills/implement-it/rules/sequencing.md) | Branch readiness before an issue starts, and recomputing/reporting the dependency-ready set after a validated closure |
| [`review-gates.md`](../skills/implement-it/rules/review-gates.md) | The two pre-commit human approval gates, how Gate 1 consumes `review-it`'s result, approval validity before Gate 2 and before push, and the general standard for when a genuine unresolved decision forces a stop |
| [`commit-boundaries.md`](../skills/implement-it/rules/commit-boundaries.md) | Deriving semantic commit boundaries from the reviewed diff, commit-message content, the issue-reference trailer, and classifying where a review correction lands — handing off to `commit-reconstruction.md` for the case that needs history rewritten |
| [`commit-reconstruction.md`](../skills/implement-it/rules/commit-reconstruction.md) | The unpublished-history reconstruction procedure itself — owning-commit identification, positive-attribution capture, round-trip verification, classification stops, and restoration — used only once `commit-boundaries.md` hands off to it |
| [`verification.md`](../skills/implement-it/rules/verification.md) | Verification scope at every lifecycle boundary, tool/starting-state discovery, worktree-provenance preservation, the completed-issue reuse rule, and *when* isolation verification is warranted — handing off to `isolation-verification.md` for the technique itself and to `activation-ordering.md` for the activation-risk ordering procedure |
| [`activation-ordering.md`](../skills/implement-it/rules/activation-ordering.md) | Reordering commits when checking one against runtime activation finds an effect; owns that procedure and its relationship to `commit-boundaries.md`'s dependency ordering — consulted only once the check finds one |
| [`isolation-verification.md`](../skills/implement-it/rules/isolation-verification.md) | The per-commit full-suite escalation technique — commit, isolate, verify, restore — used only once `verification.md`'s trigger criteria apply, or unconditionally for every commit `commit-reconstruction.md` rebuilds |
| [`worktree-preservation.md`](../skills/implement-it/rules/worktree-preservation.md) | The qualified stash-identity procedure for setting aside unrelated worktree content during a Git rewrite — shared, unmodified, by `isolation-verification.md` and `commit-reconstruction.md`; never invoked directly for ordinary work |
| [`issue-closure.md`](../skills/implement-it/rules/issue-closure.md) | Confirming an issue's commits are reachable on the correct remote branch (pushing, with authorization, if not) before asking, whether and how to close it, the closing-comment contract, and post-mutation validation |
| [`review-it`](../skills/review-it/) (separate skill, invoked, not owned) | The implementation-assurance checklist Gate 1 consumes as its third stop condition, and the same capability invoked again before a delivery correction's own Gate 1 |

**Upstream handoff, from `plan-it`.** This skill's ordinary-work input is already-approved work: an
issue already classified, scoped, drafted, reviewed, and created, with its dependency information
already recorded in whatever convention `plan-it` established. This skill reads that convention; it
never redesigns or invents one, and it never decides what belongs in an issue or a milestone.

**Downstream handoff, to `ship-it`.** Once a milestone genuinely has zero open issues remaining
(§8), this skill's involvement ends there for that milestone — `ship-it` owns everything from
milestone PR readiness onward, and this skill's own dossier does not describe that architecture; see
[`ship-it`'s dossier](ship-it.md).

**Stack/project implementation guidance is a separate concern, composed alongside — not sourced
from one place.** Project instructions, established repository conventions, and applicable
implementation/testing/tooling skills all supply guidance this skill performs the work with; an
applicable custom stack companion (such as `laravel-inertia-stack`) is loaded when one is available
and adds technology-specific implementation knowledge on top of that, but it is optional, not a
prerequisite — this skill must function correctly with no custom companion installed, drawing on
project instructions, configuration, and established usage instead (`verification.md`'s "Discover
the project's verification tools" applies the same discovery discipline to test/format/lint/
static-analysis tooling specifically). No technology-specific default is carried inside this
skill's own portable rules; see `SKILL.md`'s "Composition" for the owning statement of this model,
which this dossier does not duplicate.

**A discovered material contradiction routes back through whichever boundary actually owns it, never
resolved silently in place.** An issue's own completion criterion that can't be met at this
workflow's real closure timing routes to the human, not a silent close or a silent rewrite. A missing
product or architecture decision, wherever it surfaces — including one a `review-it` finding
reveals — routes to the human through the same "when to stop and ask" standard, never invented in
place to keep the workflow moving.

## 12. Boundaries and confidence

GitHub specificity is intentional, not a portability gap — this methodology's substrate is Git and
GitHub themselves, and its portability claim is being reusable across GitHub-based projects with
different stacks, not across trackers.

Several things stay outside this skill by design, not by oversight: milestone PR readiness/creation,
PR review and merge, deployment triggers, rollback behavior, and release are entirely `ship-it`'s or
the human's; and what release cadence, if any, applies to Backlog/hotfix work committed directly to
the trunk with no PR is not defined here, because no evidence exists yet to define it from.

Two narrow lifecycle questions remain genuinely unresolved, not merely undocumented: whether
dependency ordering and activation-safety ordering (§5, §6) could ever actually conflict during
commit construction has no precedence rule, because no real case has produced one yet; and what
happens if a milestone's PR is later rejected or materially revised after some of its issues have
already closed is a case neither this skill nor `ship-it` currently owns undoing, given the
intentional design that closes issues before their milestone's PR ever merges.

This architecture — implementation, both review gates including `review-it`'s Gate 1 role,
verification (including isolation verification, worktree-provenance preservation, and the
completed-issue reuse rule), issue closure, and delivery corrections — has been exercised through
repeated real Backlog and milestone delivery under this skill's predecessor, undivided skill, before
`review-it` was extracted and the verification/recovery additions (this repository's Steps 4 and 5)
were made. The `review-it`-integrated Gate 1, the reuse rule, worktree-provenance preservation, and
approval-validity checking are each source-reviewed and static-walkthrough-validated (per their own
implementation steps' records). The history-reconstruction procedure and the stash-identity
preservation technique it shares with isolation verification went through a further, executed
round instead: disposable Git repositories, created and discarded outside this project, ran the
literal commands both the earlier and corrected procedures specify, with results inspected via
`git log`, `git show`, `git diff`, and `git stash list` (`scenarios.md`'s four follow-up records).
That is executed Git-mechanics verification: it confirms the underlying Git commands behave as the
corrected procedures specify, not that this skill's own activation, gates, or reporting have carried
a request through either procedure end to end. This dossier's evidence does not include such a live
run — whether one has happened outside the record this dossier draws on is not something it
establishes either way. Validation beyond one real consuming project also remains unproven.
