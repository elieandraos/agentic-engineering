# my-git-workflow — Architecture Dossier

Status: Current
Scope: `my-git-workflow` as it stands in this repository
Purpose: A compact lifecycle architecture guide — what enters and exits the workflow, its two
delivery paths, its state transitions and stopping points, how sequencing, branching, review gates,
commits, verification, closure, PR readiness, milestone completion, and release cooperate, which
decisions require human authority, where each rule owns a distinct part of the lifecycle, and its
current boundaries and confidence. [`SKILL.md`](../my-git-workflow/SKILL.md) remains the operational
routing entrypoint; [`README.md`](../my-git-workflow/README.md) is the human-facing walkthrough. This
document explains the lifecycle architecture behind both rather than restating either.

## 1. Purpose and entry boundary

`my-git-workflow` begins only from already-approved implementation scope — normally one approved
GitHub issue, or an approved set of them inside a milestone, produced by `my-feature-planning`. It
carries that scope through implementation, two pre-merge review gates, semantic commits,
verification, issue closure, and — for milestone work — the PR-readiness, release, and
milestone-completion lifecycle that follows a merge.

It does not discover product scope, perform feature planning, or make an unresolved product or
architecture decision on its own — every one of those questions belongs upstream, and a genuine gap
in any of them is a reason to stop and ask, not a reason to improvise past it (§11). GitHub is not
incidental tooling this skill happens to use: Git and GitHub are intentional core substrate for the
methodology itself — reference syntax, mutation/re-fetch discipline, and the shape of a milestone,
issue, and release are all load-bearing architecture here, not an abstraction layer meant to be
swapped for another tracker.

## 2. Two delivery paths, one shared core

Every issue this skill picks up belongs to one of two paths, distinguished by which kind of
milestone it belongs to — a persistent catch-all/Backlog milestone, or a bounded delivery/phase
milestone intended to ship as a release (a classification `my-feature-planning` makes, not this
skill):

- **Backlog/hotfix path.** Work happens directly on the repository's trunk branch. There is no
  branch decision, no shared branch, and no PR at the end of it — the issue closes and the path
  ends there.
- **Milestone path.** Every issue in the milestone shares one working branch. Issues close
  individually on that branch, well before the branch is ever proposed as a PR. Only once every
  issue in the milestone is closed does the path continue into PR readiness, merge, and the
  post-merge release/completion lifecycle.

Both paths share the identical core: branch readiness, implementation, the two review gates,
semantic commit construction, verification, and issue closure are exactly the same mechanics either
way — a Backlog issue is not a lighter-weight version of a milestone issue. What differs is what
happens *after* closure: a Backlog closure is terminal; a milestone closure feeds a shared branch
that eventually needs its own readiness check, its own PR, and its own post-merge lifecycle. The
lifecycle, end to end:

```
pick a dependency-ready, approved issue
  → BRANCH READINESS (§3)                      [diverges by path]
  → implement → full-suite verification
  → GATE 1: implementation review (§4)
  → derive commit plan
  → GATE 2: commit-plan review (§4)
  → build semantic commits, narrowest-reliable verification per commit (§5, §6)
  → full-suite verification at the completed-issue boundary (§6)
  → ask: close the issue? → closure procedure + validation (§7)
  → recompute the milestone's dependency-ready set (§8)         [Backlog: path ends here]
      → ready set non-empty → report/recommend, human picks the next issue (new pass)
      → ready set empty → MILESTONE PR READINESS (§9)
  → (human creates, reviews, merges the PR)
  → human confirms merge → STOP: post-merge authorization (§10)
      ├─ MILESTONE CLOSURE                 ├─ RELEASE
```

## 3. Branch readiness

Before implementation starts, the skill determines which branch the work happens on — and for a
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

- **Gate 1 — implementation review.** Stops once the approved issue's scope is implemented and the
  verification appropriate to it has run. It proves that the right behavior now exists in the
  working tree. Approval here authorizes moving on to commit planning — nothing more; deriving
  commit structure never begins before it.
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
assumptions, or a commit decomposition with no clearly better answer into a silently-chosen fact —
each of those is its own stop, reported with evidence and a recommendation, not an unexplained
question.

Both gates apply at the same cadence sequencing establishes for everything else in this lifecycle
(§8): one Gate 1 and one Gate 2 per issue, by default. Nothing in the current rules describes a
mechanism for one approval to cover several issues' worth of implementation or commit structure at
once — a milestone having broad, already-approved scope is never read as authorization to skip or
batch either gate across more than one issue. If a human explicitly chose to approve multiple
issues under one combined review, that would be a deliberate, explicit exception granted in the
moment, not a default this workflow infers from the size or shape of the milestone.

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
commit. These two orderings have not been observed to conflict; no precedence rule exists for the
case where they might (§11).

**Deriving the plan requires inspecting the actual staged scope** — the real diff, file by file —
never planning boundaries speculatively while still writing code, and never copying how a
superficially similar earlier change happened to split.

**An unpushed commit and already-pushed history are corrected differently.** A review correction
found before anything is committed simply becomes part of whichever semantic commit it belongs to —
there is never a separate "fix review comments" commit. A correction needed after something is
already committed, but before that commit has been pushed, is folded in by rebuilding local history
so the correction lands inside the commit it actually belongs to, rather than bolting a fixup commit
on top — the result reads as if it had been built correctly from the start. The current rules
describe this reconstruction only for commits that haven't been pushed yet; they don't define a
technique for rewriting history that has already been shared, which is consistent with commit
history being treated as effectively immutable once it leaves the local, unpushed state. Fixup-style
residue is deliberately avoided wherever a clean semantic boundary can still be constructed before
push — the history should read as a sequence of engineering decisions, never a transcript of how the
work conversation actually went.

## 6. Verification model

Verification in this workflow proves two different things at different boundaries, and one never
substitutes for the other: that the changed behavior is actually correct, and that the specific
commit boundary being built or already built is itself structurally sound. A full-suite run before
Gate 1 proves the complete working tree works, before any commit history exists to split; the same
full-suite run at the completed-issue boundary, after every commit is assembled, proves the final
commit history — however many commits it became — reconstructs that same correct result. These are
not duplicates of each other even when the same command produces both results.

**Tooling is discovered per repository, never assumed.** This skill prescribes no test runner,
formatter, linter, or static analyzer, and no fixed command for any of them — what each tool is,
what it can and can't scope to a narrower subset, and what the project's full regression command
actually is are all read from the repository's own instructions, configuration, and established
usage. The same discovery discipline extends to whether the current checkout's starting state
actually matches what the real delivery boundary (CI, a fresh clone) would start from — a
proportional, risk-based check, not a blanket requirement to reset the environment before every
ordinary change.

**Targeted verification is the default while building commits; broad verification is reserved for
two specific moments.** While constructing each semantic commit, verification runs at the narrowest
scope that reliably proves that one decision — falling back to a tool's broader mode only where the
project's tooling genuinely can't scope narrower. The full regression suite runs in full exactly
twice: once before Gate 1, and once at the completed-issue boundary — never reflexively after every
commit merely by habit.

**Automated checks and human-performed manual verification are distinct categories.** Tests,
formatting, linting, and static analysis are all things this workflow can run and interpret itself.
A final round of manual testing — confirmed only by asking the human directly, never inferred from
closed issues or elapsed time — is a separate, milestone-level category this rule doesn't perform
itself (§9).

**Pre-existing debt is tolerated; new regressions are not.** A project's full-project lint,
formatting, or static-analysis output isn't required to already be clean before this workflow can
run — the standard is that this work introduces no new failures beyond whatever baseline already
existed. A regression test suite gets no such allowance: a test passes or fails regardless of the
codebase's history.

**Isolation verification proves an intermediate committed state itself, and is a deliberate
escalation, not the default.** Commit, set aside everything not yet committed, run the full
verification against exactly what's landed so far, then restore the rest and repeat for the next
commit. This is reserved for when a commit's standalone correctness genuinely needs proving on its
own — reconstructing history after the fact, or an ordering where a later commit's correctness
depends on an earlier one already being in place — not invoked merely because an issue happened to
split into multiple commits.

**A passing command is not proof it actually executed freshly.** Caching, result replay, and
test-impact analysis can each produce a complete-looking green result without re-executing
everything it appears to cover. At the two boundaries that specifically require a fresh full-
regression proof — the completed-issue boundary, and each step of isolation verification — the
project's uncached/full mode is used, where one exists, rather than trusting a result that could
have come from cache or replay.

## 7. Issue completion and closure

Closure is opt-in and only ever asked once committed, verified work exists — never automatically
inferred from a green build, and never repeated unprompted once the human has said not yet.

**A completion criterion must be satisfiable at the point this workflow actually closes the
issue.** Before asking to close, the issue's own stated Acceptance Criteria or Tests are checked
against this workflow's real closure timing — for example, a criterion requiring a real CI run
against a PR when this issue closes, by this workflow's own design, before any PR for its milestone
exists yet. A contradiction like that is surfaced, not silently closed past; resolving it (closing
anyway with the gap disclosed, deferring the criterion to the boundary where it can actually be
proven, or sending it back for a wording correction) is the human's call, not this rule's.

**The closure procedure runs in a fixed order once approved:** check off only the Tasks that are
genuinely complete, explaining any intentionally deferred or trimmed one instead of silently
checking it off; write a durable closing comment — what was implemented, verification results, the
actual commits that implement the issue, and anything discovered during implementation or review a
future reader would otherwise have to reconstruct; persist the updated body and comment, then close;
and only then re-fetch the live result. Validation checks three things independently: the issue is
actually in a closed state, the checked-task count matches what was genuinely completed, and the
closing comment actually exists — a mutation's exit code is never treated as proof of any of them.

**Closing an issue is a distinct fact from merging a milestone PR.** This closure intentionally
happens before a milestone's PR merges — for a milestone issue, often well before that PR even
exists. Closure marks that this issue's implementation and verification are done; it says nothing
about whether its commits have reached the trunk branch, and nothing about the aggregate state of
the milestone that contains it. This rule also never reopens a closed issue on its own — a later
finding concerning already-closed work defaults to a new issue referencing the original.

## 8. Sequencing: the ready-set recompute and the no-chaining default

Only after a validated closure does this rule act. It lists the milestone's remaining open issues,
reads each one's actual dependency information exactly as the project's own established convention
records it, and classifies each as ready (every dependency closed, or none stated at all) or blocked
(waiting on something still open). The result is reported in categories — newly ready because of
this closure, already ready, still blocked and on what — never as a flat list.

**Dependency order is not the same thing as issue numbering, milestone membership, or drafting
order.** Readiness is computed purely from the real dependency graph the issues themselves declare;
nothing about which issue was created first, discussed first, or numbered lowest enters into it. A
recommendation for which ready issue to pick up next is offered when the evidence genuinely supports
one — it unblocks the most follow-on work, or continues the same context the recent work was in —
and presented as a real choice between comparable options otherwise. A recommendation, and even an
immediate, unambiguous human answer, is never itself authorization to start implementing.

**The default cadence is one issue at a time, with an explicit stop between each.** Recomputing and
reporting the ready set ends this workflow pass; starting the next issue is always a new pass, with
its own explicit authorization — never a continuation folded into the current one, even when the
human's answer arrives instantly. A milestone having broad, already-approved scope across many
issues never authorizes silently chaining straight from one issue's closure into the next issue's
implementation — that would collapse the per-issue stop this rule exists to preserve. A human can
still explicitly authorize proceeding immediately, issue after issue, in the same conversation — but
that is a deliberate, explicit authorization given fresh each time, not evidence that chaining
becomes the default going forward.

**An empty ready set is not this rule's problem to solve.** For a Backlog/hotfix issue, an empty
ready set means nothing further — there's no milestone graph to exhaust. For a delivery/phase
milestone, recomputing after a closure can find zero open issues remaining; this rule reports that
state and hands off to milestone PR readiness (§9) rather than inventing a next issue or checking
that gate's conditions itself.

## 9. Milestone PR readiness

This gate starts only once the ready-set recompute (§8) reports zero open issues left in the
milestone — never earlier, and never inferred from a quiet stretch with no activity. It is
deliberately narrower than milestone closure (§10): it answers whether the shared branch is worth
proposing as a PR, not whether the milestone is finished.

Three conditions are re-confirmed fresh, together, every time this gate runs:

- **Every issue in the milestone is closed right now** — the same state the ready-set recompute
  already tracks; automated, per-issue verification is already part of what got each of those
  issues to a closed state (§6, §7), so this condition is really "is that already-established,
  per-issue verified state complete across the whole set," not a fresh check of its own.
- **Required manual verification is complete, or explicitly not applicable.** Whether final manual
  testing has actually happened is not something GitHub state can answer — it's asked of the human
  directly, never inferred from all issues being closed or from time having passed.
- **No unresolved implementation finding blocks the milestone.** If that manual testing pass finds
  something, the gate does not pass — the finding becomes a new issue attached to the still-open
  milestone (never a silent reopening of whatever issue it was found near), and the gate is re-run
  from scratch once that new issue closes.

Passing all three produces a report — "the branch looks ready" — not a mutation. PR creation,
review, and merge remain entirely human-owned unless a future rule explicitly says otherwise; this
skill resumes only once the human reports the outcome. Real CI running against an already-open,
not-yet-merged milestone PR occupies its own in-between state — narrower than readiness, earlier
than any post-merge authorization — where a red result keeps the PR unmerged until it's investigated
and either corrected within already-approved scope (with explicit human authorization, since the
affected issue's scope may already be closed) or routed into a new Discovered-work finding when it
reveals real, unscoped work.

## 10. Post-merge lifecycle: milestone closure and release

The human's confirmation that the PR merged is itself the integration gate — this workflow does not
independently re-verify the merge state, since whatever CI, conflict, and diff checks preceded that
confirmation are the human's to have already done. That confirmation is necessary to reach this
phase, but it is not by itself authorization to act: the skill stops and asks for explicit
authorization to begin the post-merge sequence at all, which can cover both branches below in one
question. That single authorization is the human approval both branches consume — neither branch
asks for it a second time, and neither branch waits on the other to finish; they proceed
independently from the same starting point.

**Milestone closure** re-confirms, from fresh state at the moment of the mutation, that the
milestone is genuinely a delivery/phase milestone (never a persistent Backlog-style one, which is
exempt from this entire lifecycle), that the post-merge authorization already given actually covers
closure, and that the milestone has zero open issues right now — re-queried fresh, since discovered
work can have added one since authorization was given. All three must hold together; none of them —
zero open issues alone, the authorization alone, or the release having published — is sufficient by
itself. If a later finding reopens the count above zero, the milestone stays open until it's
resolved and this whole gate is re-run.

**Release** starts from the same authorization and proceeds through its own sequence: discover the
project's actual, real release policy — an explicit stated policy first, only then inferred from the
repository's own established artifacts and history, and never invented when the evidence is
ambiguous — understand the release being made (its actual merged outcomes and theme, never inferred
from diff size or commit count), draft notes at release-level altitude (what shipped and why it
matters, not a replay of commit messages or issue titles), stop for the human's explicit approval of
the exact version, tag target, title, and body together, publish through whatever mechanism was
actually discovered, and re-fetch and validate every one of those fields afterward against the
approved content.

Deployment triggers, rollback machinery, prerelease channels, and changelog automation stay outside
this skill entirely — inventing any of them beyond what the repository's own evidence supports is
exactly the failure this discovery-first approach to release is designed to prevent.

## 11. The human-decision model

Certain decisions are always surfaced to the human rather than assumed, each at a specific point in
the lifecycle already described above:

| Decision | Surfaced at |
|---|---|
| Whether the implementation is acceptable | Gate 1 (§4) |
| Whether the proposed commit boundaries and messages are acceptable | Gate 2 (§4) |
| Whether to close the issue now | Issue closure (§7) |
| Which ready issue to start next, and whether to start it now | Sequencing (§8) |
| Approving any deviation from the normal per-issue cadence or gate structure | Sequencing / review gates (§4, §8) |
| Confirming a PR actually merged, and reporting that outcome | Milestone PR readiness / post-merge (§9, §10) |
| Authorizing the post-merge sequence (milestone closure and/or release) to begin at all | Post-merge lifecycle (§10) |
| Approving the exact release version, tag target, title, and body | Release (§10) |

A stop is always a report plus a question, never a bare question or an unexplored wall of options:
investigate enough to understand the decision, state the relevant evidence, offer a recommendation
when the evidence supports one, then let the human decide. Ordinary engineering choices that
approved scope, repository convention, and available evidence already resolve are not a reason to
stop — a stop is reserved for a genuinely missing decision, a contradiction between evidence and
approved assumptions, or a choice the evidence can't narrow down on its own.

## 12. Rule ownership and cross-skill handoffs

| Rule | Owns |
|---|---|
| [`sequencing.md`](../my-git-workflow/rules/sequencing.md) | Branch readiness before an issue starts, and recomputing/reporting the dependency-ready set after a validated closure |
| [`review-gates.md`](../my-git-workflow/rules/review-gates.md) | The two pre-commit human approval gates, and the general standard for when a genuine unresolved decision forces a stop |
| [`commit-boundaries.md`](../my-git-workflow/rules/commit-boundaries.md) | Deriving semantic commit boundaries from the reviewed diff, commit-message content, the issue-reference trailer, and folding in review corrections |
| [`verification.md`](../my-git-workflow/rules/verification.md) | Verification scope at every lifecycle boundary, tool/starting-state discovery, the regression-baseline model, and isolation verification |
| [`issue-closure.md`](../my-git-workflow/rules/issue-closure.md) | Whether and how to close an issue, the closing-comment contract, and post-mutation validation |
| [`milestone-completion.md`](../my-git-workflow/rules/milestone-completion.md) | Milestone PR readiness, the CI-failure-on-an-open-PR handling, and the milestone closure gate |
| [`release.md`](../my-git-workflow/rules/release.md) | Post-merge authorization's release branch: policy discovery, understanding and drafting a release, approval, publication, and post-publication validation |

**Upstream handoff, from `my-feature-planning`.** This skill's only input is already-approved work:
an issue already classified, scoped, drafted, reviewed, and created, with its dependency information
already recorded in whatever convention that skill established. This skill reads that convention; it
never redesigns or invents one, and it never decides what belongs in an issue or a milestone.

**Stack/project implementation guidance is a separate concern, composed alongside.** Application
code, framework conventions, and the concrete test/format/lint/static-analysis tooling a project uses
all come from whatever implementation and tooling skills the consuming project's stack requires,
loaded alongside this one — never carried inside this skill's own rules.

**A discovered material contradiction routes back through whichever boundary actually owns it, never
resolved silently in place.** An issue's own completion criterion that can't be met at this
workflow's real closure timing routes to the human, not a silent close or a silent rewrite. A CI
failure that reveals real, unscoped work routes to `my-feature-planning`'s Discovered-work intake,
the same path a milestone's manual-testing finding takes. A missing product or architecture decision,
wherever it surfaces, routes to the human through the same "when to stop and ask" standard, never
invented in place to keep the workflow moving.

## 13. Boundaries and confidence

GitHub specificity is intentional, not a portability gap — this methodology's substrate is Git and
GitHub themselves, and its portability claim is being reusable across GitHub-based projects with
different stacks, not across trackers.

Several things stay outside this skill by design, not by oversight: PR creation, review, and merge
strategy remain human- and project-owned; deployment triggers and rollback behavior are entirely
outside its scope; and what release cadence, if any, applies to Backlog/hotfix work committed
directly to the trunk with no PR is not defined here, because no evidence exists yet to define it
from — that gap is honestly left open rather than filled with an invented default.

Two narrow lifecycle questions remain genuinely unresolved in the current rules, not merely
undocumented: whether dependency ordering and activation-safety ordering could ever actually conflict
during commit construction has no precedence rule, because no real case has produced one yet (§5);
and what happens if a milestone's PR is later rejected or materially revised after some of its issues
have already closed is a case neither this skill nor `my-feature-planning` currently owns undoing,
given the intentional design that closes issues before their milestone's PR ever merges.

This architecture has been exercised through repeated real Backlog and milestone delivery —
implementation, both review gates, verification (including isolation verification and pre-existing-
debt handling), issue closure, CI failure handling on an open milestone PR, merge, milestone closure,
and release — not merely authored and left untested. That confidence does not extend to broad
portability: validation beyond one real consuming project remains unproven, and this document does
not claim otherwise.

A human-approved exception to the normal per-issue cadence, or to any gate, is evidence that such an
exception can be explicitly authorized when a human chooses to grant one — it is not evidence that
the default rule requiring a fresh stop and a fresh authorization for each issue should be weakened
or read more loosely going forward.
