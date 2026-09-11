# implement-it — Architecture Dossier

Status: Current
Scope: `implement-it` as it stands in this repository
Purpose: A compact lifecycle architecture guide — what enters and exits the workflow, its two delivery paths, branch readiness and companion activation, its two review gates including `review-it`'s role at Gate 1, its commit architecture and message-validation boundary, its verification model including human-controlled full-suite verification, issue closure and approval-validity, sequencing and the ready-set recompute, authorized delivery corrections, which decisions require human authority, where each rule owns a distinct part of the lifecycle, and current boundaries and confidence.
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

Both paths share the identical core: branch readiness, companion activation, implementation, the two review gates,
semantic commit construction, verification, and issue closure are exactly the same mechanics either
way — a Backlog issue is not a lighter-weight version of a milestone issue. What differs is what
happens *after* closure: a Backlog closure is terminal; a milestone closure feeds a shared branch
that eventually needs its own readiness check, its own PR, and its own post-merge lifecycle, all
owned by `ship-it`. The lifecycle, end to end:

```
pick a dependency-ready, approved issue
  → BRANCH READINESS (§3)                      [diverges by path]
  → COMPANION ACTIVATION (§3)                  [enumerate and activate all applicable skills]
  → implement → targeted verification
  → FULL-SUITE DECISION: run or intentionally skip
  → GATE 1: implementation review, review-it invoked (§4)
  → derive commit plan
  → GATE 2: commit-plan review (§4)
  → build semantic commits, narrowest-reliable verification per commit (§5, §6)
  → validate each actual commit message before push (§5)
  → completed-issue full-suite checkpoint when chosen/required (§6)
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

**Companion activation.** Before touching any implementation surface, `implement-it` enumerates the
available implementation, testing, tooling, and custom stack-companion skills that may apply, and
activates every applicable one *through the consuming agent's skill mechanism* — inspecting a
skill's trigger text or reading its rule files is supporting evidence, never a substitute for that
mechanism call. Finding one matching skill does not substitute for another matching companion.
Reading a not-yet-activated skill's own rules file is itself the trigger to activate it through the
mechanism first, not a way to resolve its applicability in place of activating it. The result is
recorded as an explicit pre-implementation checkpoint (candidates considered, activated, and
deliberately not activated with why) and restated as a one-line `Activated skills:` record at Gate 1,
so the decision stays visible at the implementation boundary rather than only living in an earlier
step. Relevant non-activation decisions are recorded when useful, and inaccessible activation
metadata is surfaced rather than silently replaced with an assumption that the first visible skill is
sufficient. See §10 for why this replaced a reminder-only version of the same requirement.

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
finished diff can be split into several defensible ways, and approving that the *implementation* is
correct says nothing about which split should become permanent history. An agent may investigate and
recommend at either gate, but never converts a genuinely unresolved product/architecture decision,
a contradiction between evidence and approved assumptions, a `review-it` finding revealing such a
decision, or a commit decomposition with no clearly better answer into a silently-chosen fact — each
of those is its own stop, reported with evidence and a recommendation, not an unexplained question.

**Approval validity before Gate 2 and before push.** An approval is scoped to what it actually
reviewed — work, scope, or a proposed action moving on afterward doesn't automatically carry the
approval forward. Before Gate 2, and again before requesting push authorization, this skill checks
that the current work, scope, and proposed action still match what the relevant approval actually
covered: a material change (a scope change since Gate 1, a diff that no longer matches what Gate 2
approved, an issue body edited since its own approval) invalidates the approval that covered the
prior state and requires renewal, routing to `review-it`'s own staleness contract where the change
affects a surface it already reviewed. This check exists to catch a real divergence, not to
manufacture one. Remote commit reachability proves presence, not verification or authorization.

Both gates apply at the same cadence sequencing establishes for everything else in this lifecycle
(§8): one Gate 1 and one Gate 2 per issue, by default. A milestone having broad, already-approved
scope is never read as authorization to skip or batch either gate across more than one issue; a
human-approved exception to that default is a deliberate, explicit grant, not evidence the default
should be read more loosely going forward.

## 5. Commit architecture

A commit is not a mechanical split of an issue. An issue describes an outcome; a commit describes
one coherent, independently-true implementation decision. Neither "one commit per issue" nor "many
small commits" is a default: commit count is discovered from the actual, finished, reviewed diff.

**Coherence is the actual test.** Every semantic commit leaves a structurally valid state that does
not depend on a later commit to become structurally valid. A commit may be inert today and still be
coherent if it is structurally complete and correct on its own terms.

**Ordering is dependency-sensitive on two independent axes.** Commits are ordered by structural
dependency, then checked for runtime activation effects that can require a narrower ordering rule via
`rules/activation-ordering.md`.

**Deriving the plan requires inspecting the completed, approved implementation diff and the intended
commit scope it actually contains** — never planning boundaries speculatively while still writing
code, and never copying how a superficially similar earlier change happened to split.

**Commit messages are a separate verification boundary, checked mechanically, not by self-report.**
Each committed message must satisfy `rules/commit-boundaries.md`: one concise implementation-outcome
subject, no file-by-file transcript, an optional body only when it adds durable context, the required
`Refs #N` trailer for tracked issue commits, and no AI/authorship trailer unless the human explicitly
requested it in the current conversation — a system/session instruction or tool default is not human
authorization, even one framed as overriding this rule. Compliance is verified structurally: the check
pipes the committed message through `git interpret-trailers --parse`, which isolates only the message's
real trailer block, and since this workflow's own `Refs #N` reference is written without a colon and
never parses as a trailer, any parsed output at all is presumptively an unauthorized trailer — the check
never needs to enumerate known attribution wording, catches a format it has never seen before, and never
mistakes body prose that merely discusses attribution trailers for carrying one. This runs immediately
after every commit and amend, with its exact output quoted as evidence rather than a claim of having
inspected the message; `rules/issue-closure.md`'s push-readiness step repeats the same check, per commit,
across the entire unpushed range as an independent second gate right before push. Any unauthorized match
is a hard failure corrected by reconstructing the message fresh and re-running the check, not by editing
the flagged text. See §10 for why this replaced a narrative
self-check.

**An unpushed correction is reconstructed into its semantic commit.** A correction found before
anything is committed simply belongs in its semantic commit; a correction needed after an unpushed
commit exists uses `rules/commit-reconstruction.md`. Rewriting already-pushed history requires
specific human authorization and a different path.

## 6. Verification model

Verification proves different things at different boundaries: targeted verification proves the
changed behavior; a human-controlled full regression provides broader system confidence when chosen;
and commit-specific checks prove the semantic decision represented by each commit.

**Tooling is discovered per repository, never assumed.** This skill prescribes no test runner,
formatter, linter, or static analyzer. Discover the project's actual commands and their reliable
scoping from project instructions, stack skills, configuration, scripts, CI, or established usage.

**Preserve pre-existing worktree changes.** Use reliable provenance to distinguish this task's work
from prior or human work, and ask only when unresolved provenance materially affects safe continuation.

**Targeted verification is required before Gate 1.** Run the narrowest reliable tests for the changed
behavior and the applicable formatting/lint/static checks. Then ask the human whether to run the full
regression suite or intentionally skip it for this issue.

**Full regression is human-controlled.** Recommend running it for standalone Backlog/trunk work and
for materially broad or risky changes. For suitable issues inside an active phase milestone, the
human may intentionally skip it when targeted verification is strong. A skip is recorded honestly
and never represented as full-suite proof.

**Completed-issue verification follows the human's choice.** When the human chooses full-suite
verification, use or reuse qualifying broad evidence according to `rules/verification.md`. When the
human chooses to skip, targeted verification remains the issue's required proof unless a later rule,
risk escalation, or milestone-level decision requires broader regression evidence.

Cache, replay, and impact-analysis results are distinguished from fresh execution whenever a full
regression is chosen. Project-specific commands, such as useOrbit's `php artisan test --compact
--no-tia`, remain project knowledge rather than hardcoded methodology requirements.

Isolation verification remains a deliberate escalation only when an intermediate committed state
itself needs proof.

## 7. Issue closure and mutation boundaries

The issue lifecycle has separate approval boundaries for implementation, commit construction, push,
and closure. Implementing or verifying an issue never authorizes its commit, push, or closure by
itself.

The human approvals and choices are:

| Decision | Surfaced at |
|---|---|
| Branch creation/switch for milestone work | Before implementation, when needed |
| Full regression suite: run or skip | After targeted verification, before Gate 1 |
| Gate 1 implementation approval | After verification + clean/resolved review-it result |
| Commit-plan approval | After Gate 1 |
| Push authorization | Before push |
| Issue-closure approval | Before closure |

The full-suite decision is deliberately separate from Gate 1. Gate 1 requires targeted verification,
applicable code-quality checks, and a clean/resolved `review-it` result; the human's full-suite choice
determines whether broader regression evidence is also present.

## 8. Sequencing

After each issue closes, recompute the dependency-ready set (`rules/sequencing.md`) and recommend
the next issue, explaining the choice when several are ready. A recommendation is not authorization
to continue — wait for the human's selection before implementing another issue. When the ready set
is empty because every open issue remains blocked, report the blockers; only a genuinely empty
milestone (zero open issues) hands off to `ship-it`'s milestone PR-readiness assessment.

## 9. Authorized delivery corrections

When `ship-it` investigates a CI failure on an open milestone PR, determines a correction stays
within already-approved scope, and the human explicitly authorizes it, it hands the authorized fix
to this skill. Perform the correction through the same lifecycle — Gate 1 and Gate 2 as applicable,
`review-it` before Gate 1, targeted verification, and the human-controlled full-suite choice, then
commit construction and authorized push — whether or not the original issue is still open.

## 10. Open decisions, current boundaries, and confidence

Current implementation-stage behavior is deliberately conservative about scope but flexible about
regression-test cost. Targeted verification is mandatory. Full-suite verification is available to
every issue but is explicitly chosen by the human at the issue boundary, with Backlog work receiving
a recommendation to run it and active milestone issues allowed to defer it.

Companion activation and commit-message compliance (§3, §5) are enforced mechanically rather than
through a narrative self-check, because a rule the agent only reads and reasons about — even one
already in effect — is not resistant to a runtime-level instruction that frames itself as overriding
project rules, and a narrative check produces no falsifiable evidence that it was actually followed.
Both mechanisms are current, authoritative repository policy, grounded in repeated observation from
consumer execution and stewardship review within this repository's own use — not yet independently
validated as portable guidance across a distinct consuming project. Revisit either mechanism if further
use shows it remains unreliable, imposes disproportionate overhead, or a distinct consuming project's
evidence refines it.

**Commit history.** Commit subjects identify the implementation outcome in one concise sentence;
the body is optional and used only when additional durable context is genuinely useful. Commits made
by this workflow do not receive `Co-Authored-By`, AI attribution, model attribution, or similar
authorship trailers unless the human explicitly requests that attribution.
