# ship-it — Architecture Dossier

Status: Current
Scope: `ship-it` as it stands in this repository
Purpose: A compact lifecycle architecture guide — where this skill's narrower delivery scope begins
and ends relative to `implement-it`, its three independent entry points, PR readiness and creation,
the CI-failure/delivery-correction ownership split with `implement-it`, the post-merge closure and
release lifecycle, which decisions require human authority, where each remaining rule owns a
distinct part of the lifecycle, and its current boundaries and confidence.
[`SKILL.md`](../skills/ship-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/ship-it/README.md) is the human-facing walkthrough. This document explains
the lifecycle architecture behind both rather than restating either.

## 1. Purpose and entry boundary

`ship-it` is the narrower, milestone-delivery half of what a single skill of this name used to own.
Everything from branch readiness through implementation, both pre-commit review gates, semantic
commits, verification, and issue closure belongs to
[`implement-it`](../skills/implement-it/) — a separate, independently callable skill this dossier
does not describe (§2). `ship-it` never implements code and never requires proof that a particular
`implement-it` session produced the state it acts on; it checks a milestone's or PR's actual current
GitHub state instead.

This skill has three independent entry points, each with its own prerequisite, not one linear
pipeline stage that always starts the same way:

- **Milestone PR readiness and creation** — starts once a delivery/phase milestone genuinely has
  zero open issues remaining, re-checked fresh every time this gate runs (§3).
- **Investigation and continuation on an already-open milestone PR** — starts from the PR's own
  current state; it does not re-require zero open issues, since a follow-up finding can reopen the
  milestone's issue count while an existing PR still needs attention (§4).
- **Post-merge closure and release** — starts from the human's confirmation that the PR merged and
  explicit authorization to proceed, independent of any `implement-it` session history in the
  current conversation (§5).

It does not discover product scope, perform feature planning, implement code, or make an unresolved
product or architecture decision on its own — every one of those questions belongs upstream or to
`implement-it`, and a genuine gap in any of them is a reason to stop and ask, not a reason to
improvise past it (§6). GitHub is not incidental tooling this skill happens to use: Git and GitHub
are intentional core substrate for the methodology itself — reference syntax, mutation/re-fetch
discipline, and the shape of a milestone, issue, and release are all load-bearing architecture here,
not an abstraction layer meant to be swapped for another tracker.

## 2. Boundary with `implement-it`

A Backlog/hotfix issue — work with no delivery/phase milestone behind it — never reaches this skill
at all: it runs directly on the repository's trunk branch, closes on its own, and the path ends
entirely inside `implement-it`. Only milestone work, where every issue in a delivery/phase milestone
shares one working branch, ever continues into this skill, and only once that milestone's own
dependency-ready-set recompute (owned by `implement-it/rules/sequencing.md`) reports zero open
issues remaining.

This skill's upstream input is `implement-it`'s own completed, verified, closed work — issue
implementation, both review gates (including the standalone `review-it` invocation before Gate 1),
semantic commit construction, verification, and issue closure are entirely `implement-it`'s
architecture, not restated here. What this skill needs from that upstream state is narrow and
factual: which issues are closed, whether the milestone's shared branch exists and is current, and —
during a delivery correction (§4) — that any authorized fix actually lands through `implement-it`'s
own lifecycle rather than being performed by this skill directly.

## 3. Milestone PR readiness

This gate starts only once a delivery/phase milestone's dependency-ready-set recompute (owned by
`implement-it`) reports zero open issues left — never earlier, and never inferred from a quiet
stretch with no activity. It answers whether the shared branch is worth proposing as a PR, not
whether the milestone is finished (§5 owns that broader question).

Three conditions are re-confirmed fresh, together, every time this gate runs:

- **Every issue in the milestone is closed right now** — the same state the ready-set recompute
  already tracks; automated, per-issue verification is already part of what got each of those
  issues to a closed state inside `implement-it`, so this condition is really "is that
  already-established, per-issue verified state complete across the whole set," not a fresh check
  of its own.
- **Required manual verification is complete, or explicitly not applicable.** Whether final manual
  testing has actually happened is not something GitHub state can answer — it's asked of the human
  directly, never inferred from all issues being closed or from time having passed.
- **No unresolved implementation finding blocks the milestone.** If that manual testing pass finds
  something, the gate does not pass — the finding becomes a new issue attached to the still-open
  milestone (never a silent reopening of whatever issue it was found near), and the gate is re-run
  from scratch once that new issue closes.

Passing all three produces a report — "the branch looks ready" — not a mutation. Once ready, this
skill discovers the project's PR conventions, checks for an existing matching PR before proposing
creation, prepares the title/base-head branches/body referencing the milestone, obtains explicit
approval of that exact proposal, creates through the discovered mechanism, then re-fetches and
validates the actual result. PR review and merge remain entirely human-owned; this skill resumes
only once the human reports the outcome.

## 4. CI failure on an open milestone PR — the delivery-correction split

Real CI running against an already-open, not-yet-merged milestone PR occupies its own in-between
state — narrower than readiness (§3), earlier than any post-merge authorization (§5). A red result
keeps the PR unmerged until it's resolved, and resolving it is split between two skills by
authority, not by convenience:

- **This skill investigates, explains, and gates authorization.** It determines whether the failure
  is correctable within already-approved scope or reveals genuinely new, unscoped work; explains the
  correction needed; and asks the human for explicit authorization before anything is fixed. New
  scope routes to `plan-it`'s Discovered-work intake instead of being corrected in place. This skill
  never implements the fix itself, whether or not the affected issue is already closed, and this
  route stays available without requiring an open issue to exist — an authorized, narrowly-scoped
  direct fix needs no new issue and does not require reopening a closed one.
- **`implement-it` performs any authorized correction**, using the same lifecycle it already owns
  for ordinary issue work: it invokes `review-it` and Gate 1/Gate 2 as applicable, constructs the
  commit(s), verifies, and pushes once authorized.
- **This skill resumes** — re-running real CI and reporting — once the correction lands and CI is
  green.

Only the *who performs the fix* changed from an earlier design; the underlying policy (narrow
authorized direct fix versus discovered-work intake) is unchanged. This is the same authorization
boundary the two-gate model (owned by `implement-it`) already enforces elsewhere: an investigation
or scope determination is never by itself sufficient authorization to implement anything — only an
explicit human authorization is.

## 5. Post-merge lifecycle: milestone closure and release

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

## 6. The human-decision model

Certain decisions are always surfaced to the human rather than assumed, each at a specific point in
this skill's own lifecycle — the decisions gating `implement-it`'s implementation, gates, and commit
plan (Gate 1, Gate 2, push, closure) belong to that skill's own dossier-equivalent contract, not
here:

| Decision | Surfaced at |
|---|---|
| Approving the exact milestone PR proposal (title, base/head, body) before creation | Milestone PR readiness (§3) |
| Confirming a PR actually merged, and reporting that outcome | Milestone PR readiness / post-merge (§3, §5) |
| Authorizing a correction to a CI failure on an open milestone PR, and whether it's in-scope or new work | CI failure on an open PR (§4) |
| Authorizing the post-merge sequence (milestone closure and/or release) to begin at all | Post-merge lifecycle (§5) |
| Approving the exact release version, tag target, title, and body | Release (§5) |

A stop is always a report plus a question, never a bare question or an unexplored wall of options:
investigate enough to understand the decision, state the relevant evidence, offer a recommendation
when the evidence supports one, then let the human decide. Ordinary engineering choices that
approved scope, repository convention, and available evidence already resolve are not a reason to
stop — a stop is reserved for a genuinely missing decision, a contradiction between evidence and
approved assumptions, or a choice the evidence can't narrow down on its own.

## 7. Rule ownership and cross-skill handoffs

| Rule | Owns |
|---|---|
| [`milestone-completion.md`](../skills/ship-it/rules/milestone-completion.md) | Milestone PR readiness and creation, the CI-failure-on-an-open-PR investigation/authorization split (§4), and the milestone closure gate |
| [`release.md`](../skills/ship-it/rules/release.md) | Post-merge authorization's release branch: policy discovery, understanding and drafting a release, approval, publication, and post-publication validation |

**Upstream handoff, from `implement-it`.** This skill's only input is already-closed, already-verified
work on a milestone's shared branch — sequencing, branch readiness, both review gates,
`review-it`-backed implementation assurance, commit construction, verification, and issue closure
are entirely `implement-it`'s architecture, referenced here only as the fact this skill's gates
depend on, never restated.

**Stack/project implementation guidance never reaches this skill.** Application code, framework
conventions, and implementation tooling belong to `implement-it` and whatever stack companion a
consuming project loads alongside it — this skill has no implementation concern of its own to
compose them with.

**A discovered material contradiction routes back through whichever boundary actually owns it,
never resolved silently in place.** A CI failure that reveals real, unscoped work routes to
`plan-it`'s Discovered-work intake, the same path a milestone's manual-testing finding takes. A
missing product or architecture decision, wherever it surfaces, routes to the human through the same
"when to stop and ask" standard, never invented in place to keep the workflow moving.

## 8. Boundaries and confidence

GitHub specificity is intentional, not a portability gap — this methodology's substrate is Git and
GitHub themselves, and its portability claim is being reusable across GitHub-based projects with
different stacks, not across trackers.

Several things stay outside this skill by design, not by oversight: PR creation is this skill's own
job once readiness passes, but PR review and merge strategy remain human- and project-owned;
deployment triggers and rollback behavior are entirely outside its scope; and what release cadence,
if any, applies to Backlog/hotfix work committed directly to the trunk with no PR is not defined
here, because no evidence exists yet to define it from — that gap is honestly left open rather than
filled with an invented default, and because that work never reaches this skill in the first place
(§2).

What happens if a milestone's PR is later rejected or materially revised after some of its issues
have already closed is a case neither this skill nor `implement-it` currently owns undoing, given
the intentional design that closes issues before their milestone's PR ever merges — a narrow,
genuinely unresolved question, not merely undocumented.

This architecture has been exercised through repeated real Backlog and milestone delivery under its
predecessor, undivided skill — implementation, both review gates, verification, issue closure, CI
failure handling on an open milestone PR, merge, milestone closure, and release — not merely
authored and left untested. The split described in this dossier is itself unexercised by a live
consumer run: no skill in this ecosystem has been invoked end to end since `implement-it` and
`review-it` were extracted from what this skill used to be, and this document does not claim
otherwise. Validation beyond one real consuming project also remains unproven.

A human-approved exception to the normal per-issue cadence, or to any gate, is `implement-it`'s own
architecture to describe; this dossier does not restate it. Nothing here should be read as claiming
authority over a decision that skill's own rules actually own.
