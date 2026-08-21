---
name: my-git-workflow
description: "Personal workflow for moving an already-approved GitHub issue through implementation, human review, semantic git commits, verification, and issue closure, then recalculating the milestone's dependency-ready set afterward. Distinct from my-feature-planning, which decides what work should exist and owns issue drafting/creation/milestones — this skill starts only once an issue is already approved and ready to implement, and owns everything from there through the commit history and (optionally) closing the issue. Core principle: issues describe outcomes, commits describe coherent, verified implementation steps — never assume one issue equals one commit (see rules/commit-boundaries.md for the v0.1 evidence: #288 and #287 each landed as one coherent commit despite touching many files, while #120 and #289 each split into several dependency-ordered commits). Covers: implementing one dependency-ready issue's scope at a time, running verification proportional to what's being proven, a hard stop for human review of the implementation before any commit conversation starts, inspecting the finished diff only after that approval and proposing a semantic commit plan as its own separate review gate, building commits with targeted verification (reserving a full regression run for the completed-issue boundary, or for isolation-proving a non-trivial split), ordering commits so intermediate states stay green even when a feature-flag activation would retroactively un-skip pre-existing runtime-gated tests, asking (never assuming) whether to close the committed issue, the exact checked-tasks/closing-comment/close/post-mutation-validation closure recipe, and recalculating + reporting the milestone's dependency-ready set afterward without auto-starting the next issue. Also covers the Release phase that begins once a PR has been successfully merged: discovering the project's actual release/version policy from explicit config or, absent that, from established release history rather than assuming SemVer/GitHub Releases/a tag type without evidence; classifying the release's primary theme and outcomes (never by commit/file/line count); drafting release notes at release-level altitude grouped by meaningful area; a human approval gate on the proposed version, tag target, title, and body before anything is tagged or published; publishing through the project's own discovered mechanism; and post-publication validation that re-fetches the tag and release rather than trusting a publish command's exit code (see rules/release.md, built from PR #298 merging and shipping as v0.17.0 — Authentication & 2FA, plus this repository's prior 21 releases as evidence of the range of release shapes: feature, infrastructure, hardening/polish, upgrade, and multi-area). Also covers post-release milestone completion for a delivery/phase milestone — a forward-looking workflow decision, not an extraction of past repository practice (this project's full milestone history showed every milestone left open even when fully closed-out, which this rule deliberately does not preserve): the milestone stays open through implementation, review, manual testing, and any small follow-up issue discovered there and legitimately added to it, never inferring completion from open-issues-equals-zero alone; the closure gate requires all three at once, freshly checked — delivery/phase milestone (never the persistent Backlog, which this lifecycle never applies to), the shipping release published-and-validated, and zero open issues at that moment; and closing the milestone is itself a validated GitHub mutation — explicit human approval, then re-fetching the milestone afterward to confirm its state is actually closed, never trusting the closure command's exit code alone (see rules/milestone-completion.md). Trigger when the user asks to implement, build, or start work on a specific approved issue ('implement #290', 'let's build #121 next', 'start on the next dependency-ready issue'); asks to commit already-implemented work ('commit this', 'propose the commit plan', 'split this into commits', 'build and verify each commit in isolation'); asks to close an issue ('close #289 using the usual workflow'); asks what's next in a milestone ('what's the next dependency-ready issue', 'recalculate what's unblocked'); asks to release/publish merged work ('release Phase 22', 'let's publish v0.17.0', 'cut a release for this merge', 'what's our release policy'); or asks about a milestone's completion state ('is Phase 22 done', 'can we close this milestone', 'check if the milestone is ready to close', 'close out the milestone now that it's released'). Always load ALONGSIDE this project's implementation skills (my-laravel-patterns, laravel-best-practices, pest-testing, my-phpstorm-conventions, inertia-vue-development, fortify-development, wayfinder-development, etc. as the code demands) — this skill owns the workflow machinery around commits, closure, release, and post-release milestone completion, not the code, tests, or framework conventions themselves. Does not decide what issues should exist, does not draft or create GitHub issues or milestones, and does not define a milestone's scope or description (that's my-feature-planning, which owns milestone definition but never closes one) — but does own the post-release milestone-completion check and the closure mutation itself, and — v0.1 — does not yet cover PR creation, merge strategy, or deployment automation; nor does it invent a branch-naming convention this repository hasn't already documented."
---

# My Git Workflow

Personal workflow for what happens *after* an issue is approved and *before* it's shipped:
implement it, get it reviewed, turn the finished diff into a small number of coherent commits, get
those reviewed too, verify at the right scope, optionally close the issue, and recalculate what's
next. It also covers the Release phase that begins once a PR has merged — discover the project's
real release policy, classify the release, draft outcome-level notes, get explicit approval, publish
through the project's own mechanism, and validate the result. Built by extracting the actual pattern
from implementing Phase 22 — Authentication & 2FA (#288, #287, #120, #289 through commits and
closure; PR #298 merging and shipping as v0.17.0 for the release phase) — not designed up front.
Where the evidence doesn't cover something (PR creation, merge strategy, branch naming, deployment),
this skill says so explicitly rather than inventing it — see "Left for later versions" below.

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

## A minimal human prompt is enough — it invokes the workflow, not a shortcut past it

This skill owns the workflow machinery — picking up an approved issue, running the right scope of
verification, stopping for review at the right two points, inspecting the diff, proposing commit
boundaries, closing issues correctly, recalculating what's unblocked. A prompt like "implement
#290, same workflow" or "commit this" or "close #289" is enough; the human doesn't need to restate
the review gates, the verification scope, or the closure recipe each time.

> Short prompts invoke the workflow; they do not bypass its gates.

- "implement #290, same workflow" still stops at Gate 1 for implementation review — it is not
  authorization to proceed straight to commits.
- "commit this" starts the commit-boundary proposal (`rules/commit-boundaries.md`); it is not
  itself approval of that plan — Gate 2 still requires an explicit yes on the proposed grouping
  before any commit is written.
- "close #290" still runs the full closure recipe (`rules/issue-closure.md`) — check off Tasks,
  closing comment, close, post-mutation validation — not a shortcut straight to `gh issue close`.

The brevity is about not re-explaining the workflow every time, never about removing a gate the
workflow would otherwise stop at.

## Quick Reference

1. Commit boundaries → `rules/commit-boundaries.md` — one issue does not equal one commit; file
   count is not commit count; boundaries follow coherent implementation decisions; see the diff
   before deciding; keep proving tests with their step; review corrections fold into their
   semantic commit, never a fixup commit; messages explain the decision, not the diff, and every
   commit that implements an issue carries a `Refs #N` trailer — never `Closes`/`Fixes`
2. Verification → `rules/verification.md` — targeted verification per commit, plus two distinct
   full-suite moments (Gate 1's, before history is written, and one at the completed-issue
   boundary, after commits exist); the stronger stash-based isolation technique reserved for when
   intermediate commit states are themselves the property being proven, not a default for every
   multi-commit split; ordering commits so a feature-flag activation doesn't retroactively break an
   already-landed commit
3. Review gates → `rules/review-gates.md` — two separate human approvals (implementation, then the
   commit plan), and the explicit conditions that always warrant a stop
4. Issue closure → `rules/issue-closure.md` — ask first; check off Tasks, add a closing comment,
   close, then post-mutation validation exactly like `my-feature-planning` runs on every GitHub
   mutation
5. Sequencing → `rules/sequencing.md` — recompute the milestone's dependency-ready set after every
   closure, report the graph, recommend, and leave the final choice to the human
6. Release → `rules/release.md` — after a PR merges: discover the project's actual release policy
   before assuming one; classify the release's theme and outcomes without using size as a proxy for
   version importance; draft notes at release-level altitude, grouped by area; get explicit human
   approval of the version, tag target, title, and body; publish through the project's own
   discovered mechanism; re-fetch and validate the result field by field
7. Milestone completion → `rules/milestone-completion.md` — after release validation, not at issue
   closure or PR merge: a delivery/phase milestone stays open through manual testing and any
   legitimately-scoped follow-up issue discovered there; close only once the shipping release is
   published-and-validated *and* the milestone has zero open issues at that moment; the persistent
   Backlog milestone is never subject to this; closure itself is a validated mutation like any other

## The working loop

1. **Choose a dependency-ready, approved issue.** If more than one is ready and the choice isn't
   obvious, that's a sequencing stop (`rules/review-gates.md`, `rules/sequencing.md`) — ask, don't
   pick silently.
2. **Implement only that issue's scope.** Follow the project's implementation skills for the actual
   code/tests/conventions — this skill doesn't own that part.
3. **Run verification proportional to what's being proven** (`rules/verification.md`) — targeted
   tests plus formatting, and a full-suite pass before presenting the implementation. This is the
   Gate 1 full suite — it validates the working tree, not yet any commit history.
4. **Stop for human review** (Gate 1, `rules/review-gates.md`). Report what changed and how it was
   verified. Do not think about commit structure yet.
5. **After approval, inspect the completed diff.** `git status` / `git diff --stat` / the actual
   per-file diffs — never a plan formed before the diff existed.
6. **Propose a semantic commit plan** (`rules/commit-boundaries.md`) — grouping, order and why,
   which tests travel with which commit, draft messages (title/body on the decision, a `Refs #N`
   trailer, never `Closes`/`Fixes`).
7. **Get human approval of that plan** (Gate 2, `rules/review-gates.md`) before writing any commit.
8. **Create the commits**, using targeted verification per commit and, when the split itself needs
   proof (a rebuild after the fact, or an order where correctness depends on sequence), the
   stash-based isolation technique (`rules/verification.md`).
9. **Run the full regression suite once**, at the completed-issue boundary, with everything landed.
   This is a distinct full-suite moment from step 3's — it validates the assembled commit history,
   not the working tree (`rules/verification.md`).
10. **Ask whether to close the issue.** Never assume yes.
11. **If approved, run the closure recipe** (`rules/issue-closure.md`): check off completed Tasks,
    add a concise closing comment (implementation summary, verification numbers, commit SHAs),
    close it, then post-mutation validation — re-fetch and confirm state/checkboxes/comment, never
    trust the mutation's exit code alone.
12. **Recalculate the milestone's dependency-ready set** (`rules/sequencing.md`), summarize the
    graph, recommend a next issue with a one-line rationale, and stop — leave the final sequencing
    choice to the human, and don't start implementing anything in the same pass.

## Release: after a PR merges

This is a separate phase from the working loop above, not step 13 of it — it doesn't run per issue,
it runs once a PR (which may bundle several issues' worth of committed work, the way PR #298 bundled
four) has actually merged. Full detail in `rules/release.md`; the shape:

1. **Discover the project's actual release policy.** Prefer an explicit policy/config if one
   exists; otherwise infer the convention from the repository's established release history. Do not
   assume SemVer, GitHub Releases, a tag type, or a hosting platform without evidence. If the
   evidence is ambiguous, stop and ask rather than invent.
2. **Determine the release's primary theme and meaningful outcomes.** A release can be a feature, an
   infrastructure/architecture change, hardening/reliability work, polish, or a mixture spanning
   several areas under one theme. Never derive version importance from commit count, file count, or
   line count — that's the project's release policy's job, not a size heuristic.
3. **Draft release notes at release-level altitude.** Group outcomes by meaningful area, describe
   what shipped rather than how, and include technical/infrastructure changes only when they carry
   real architectural, operational, reliability, or future-capability significance to a reader.
4. **Stop for explicit human approval** of the proposed version, tag target, release title, and full
   body before creating or publishing anything.
5. **Publish through the project's own discovered mechanism** from step 1 — preserve its established
   tag/release semantics, and don't invent deployment, rollback, prerelease, or changelog-automation
   machinery the repository shows no evidence of wanting.
6. **Re-fetch and validate** the tag and release from the source of truth — version/tag name, tag
   target commit, title, body, and publish state — never trusting a publish command's exit code
   alone.

Issue closure is not part of this phase — every issue behind the merged PR was already closed (or
left open on purpose) during its own pass through the working loop, per `rules/issue-closure.md`,
before the PR even existed.

## Milestone completion: after release validation

A further phase, not step 7 of the release phase above and not a consequence of issue closure or PR
merge on their own — it starts once release validation (step 6 above) has actually passed. Full
detail in `rules/milestone-completion.md`; the shape:

1. **Do not infer completion from zero open issues alone.** A delivery/phase milestone can — and
   routinely will — stay open through manual testing and any small, legitimately-scoped follow-up
   issue discovered there, even after every currently-known issue closes and even after the release
   ships. Adding such an issue to the still-open milestone is expected, not a process failure.
2. **Check the closure gate — all three, together, freshly queried:** the milestone is a
   delivery/phase milestone, not the persistent Backlog; the release it was shipping has been
   published and validated; the milestone has no open issues right now.
3. **If any condition fails, do not close.** An open issue blocks closure regardless of release
   state. A release that published successfully but was followed by a newly-discovered issue keeps
   the milestone open until that issue is done and the gate passes again in full.
4. **Backlog (or any persistent catch-all) is never subject to this gate** — don't run it, don't
   propose closing it.
5. **Stop for explicit human approval** before closing — the same posture as every other mutation
   gate in this skill.
6. **Close, then re-fetch and validate** the milestone's state is actually `closed` — never trust
   the closure command's exit code alone — and report the result compactly.

This is a forward-looking workflow decision, not an extraction of past repository practice — see
`rules/milestone-completion.md`'s "Forward-looking only" for what the repository's actual milestone
history showed and why it isn't the rule being followed here. No existing milestone is retroactively
closed because this phase now exists.

## Relationship to the rest of the workflow

```
my-feature-planning        → decides what work should exist; drafts, reviews, creates GitHub issues
                              and the delivery/phase milestone they belong to
  → issue approved
my-git-workflow            → implementation → review → semantic commits → verification → closure
                              (repeats per dependency-ready issue; several issues may share one PR)
  → PR opened, reviewed, merged            (not yet owned by this skill — see "Left for later")
my-git-workflow            → release: discover policy → classify → draft → approve → publish → validate
my-git-workflow            → milestone completion check → milestone closure (delivery/phase only)
  → implementation skills own the actual code, tests, framework conventions along the way
  → the human owns product/architecture decisions, every review/approval gate, and final sequencing
```

`my-feature-planning` never decides commit structure or touches git, and never closes a milestone —
its responsibility ends at defining the milestone and its issue set. This skill never decides what
an issue should say or drafts/creates/reopens issues, or decides what belongs in a milestone — it
moves already-approved work through implementation to a closed (or left-open) issue, then, once a PR
carrying that work has merged, through to a published release, and finally, once that release is
validated and the milestone has no open issues, through to milestone closure.

## What this skill owns

**Owns:** picking up one dependency-ready approved issue at a time; the two pre-merge review gates
(implementation, then commit plan); proposing and building semantic commit boundaries from the
actual diff; verification scope (targeted vs. full-suite, and when isolation-proving a split is
warranted); commit ordering when feature-activation could break an intermediate state; the
issue-closure recipe and its post-mutation validation; recalculating and reporting the milestone's
dependency-ready set; after a PR merges, the release phase — policy discovery, release
classification, outcome-level drafting, the release approval gate, publishing through the project's
own mechanism, and post-publication validation; and, once release validation passes, post-release
milestone completion — the closure gate (delivery/phase milestone, release published-and-validated,
zero open issues, all three re-checked fresh), the exemption for the persistent Backlog milestone,
and the closure mutation itself with its own post-mutation validation.

**Does not own:** deciding what issues should exist, issue drafting, milestone/label creation, or
defining a milestone's scope or description (`my-feature-planning`); the actual application code,
tests, or framework-specific conventions (the implementation skills); product/architecture
decisions, any review/approval gate's outcome, or final sequencing among multiple ready issues (the
human, always); PR creation, merge strategy, or
deployment automation (still not designed — see "Left for later versions").

## Left for later versions

Not designed yet, because no real evidence exists to extract from:

- **PR creation and description conventions.**
- **Merge strategy** (merge commit vs. squash vs. rebase-and-merge).
- **Deployment triggers.**
- **A branch-naming convention.** The branch used throughout the commit/closure evidence was
  `feature/organization-owner-provisioning` — a milestone-scoped branch that ended up carrying four
  issues' worth of work, not a name chosen per-issue. That's one data point, not a pattern, and
  this repository doesn't document a branching convention anywhere else. Do not generalize "one
  branch per issue," "one branch per milestone," or any other scheme from it — ask, or take
  whatever branch is already checked out, until there's real evidence of a repeated convention to
  extract.

Release/changelog generation is no longer on this list — see "Release: after a PR merges" above and
`rules/release.md`, extracted once PR #298 actually merged and shipped as `v0.17.0`. When real
evidence for PR creation, merge strategy, or deployment shows up, extract those the same way: from
what actually happened, not from what seemed reasonable in advance.
