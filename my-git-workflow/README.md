# my-git-workflow

A "turn approved work into a clean, verified history — and, once it merges, a published release"
skill. It picks up one already-approved GitHub issue at a time, implements only its scope, stops for
review, turns the finished diff into a small number of coherent commits (also reviewed before
they're written), verifies at the right scope, optionally closes the issue, and tells you what's
unblocked next. Separately, once a PR carrying that work has merged, it discovers the project's real
release policy, classifies the release, drafts outcome-level notes, stops for approval, publishes,
and validates the result.

It doesn't decide what work should exist — that's `my-feature-planning`. It doesn't write the
application code — that's whichever implementation skills the code demands. It doesn't (yet) decide
how a PR gets opened or merged — see "Is this v0.1, and what's missing on purpose" below. It owns the
machinery in between and after: implementation → review → commits → verification → closure → what's
next, then, after merge: release, and finally, once that release is validated: milestone completion
and closure.

## Why this exists

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

Those are different units of work, and treating them as the same thing produces bad history either
way — one giant commit per issue loses the actual implementation narrative, and mechanically
splitting a diff by file type or directory produces commits nobody would recognize as a real
decision. This skill exists to get the split right, on the evidence of how it actually went for
four issues in Phase 22 — Authentication & 2FA:

| Issue | What it was | Commits |
|---|---|---|
| #288 | Provision a new organization + first Owner via Artisan command | 1 |
| #287 | Remove public registration (21 files, one decision) | 1 |
| #120 | 2FA backend — persistence, then HTTP wiring, then activation | 3 |
| #289 | Org-level 2FA requirement — persistence, policy, settings page, enforcement | 4 |

Two of those were one clean commit each, even though #287 touched 21 files across 11 route files
plus app code, a migration, and tests. Two needed several commits, ordered by real dependency and,
in #120's case, by which commit a feature-flag flip could safely follow without retroactively
breaking an earlier one. Nothing about file count, issue size, or "how many things changed"
predicted which shape a given issue would take — only looking at the actual diff did.

## The working loop

```
choose a dependency-ready, approved issue
  → implement only its scope
  → verify (targeted + one full-suite pass)
  → STOP — human reviews the implementation
  → (approved) inspect the finished diff
  → propose a semantic commit plan
  → STOP — human reviews the commit plan
  → (approved) build the commits, targeted verification per commit
  → full regression suite once, at the completed-issue boundary
  → ask: close the issue?
  → (if yes) check Tasks, closing comment, close, post-mutation validation
  → recalculate the milestone's dependency-ready set, report it, recommend — human chooses next
```

Two review gates, not one. Approving the implementation is not approving a commit structure — the
same diff can be split several defensible ways, and the human sees the proposed split before it
becomes permanent history. See `rules/review-gates.md`.

## What a good commit plan looks like

Not a mechanical split by folder or file extension. A semantic commit is one implementation
decision you could describe in a single sentence of *why*:

- #120's three commits: "add the 2FA data layer" → "wire the Security settings page to read it" →
  "turn the Fortify feature on and prove the whole pipeline end to end."
- #289's four commits: "add the requirement column" → "add the Owner-only policy" → "add the
  toggle page" → "enforce it via middleware."

Each one, read alone at its point in history, should leave a coherent, non-broken implementation
state that doesn't depend on a later commit to become structurally valid — even the "inert" early
ones, which do nothing observable yet but stand correctly on their own terms. What makes a commit
*not* coherent isn't smallness, and it isn't "does nothing observable yet" either — it's
referencing something that doesn't exist until the next commit, or bundling two unrelated decisions
because they happened to touch the diff at the same time.

Tests travel with the step they prove, not split into a separate commit. A commit with nothing yet
to observe (no consumer, a feature flag still off) can legitimately ship with no new tests of its
own — its proof is that the full suite stays exactly as green as it was before it landed.

Review corrections found before anything is committed just land inside whichever commit they
belong to — no separate "fix review comments" commit. If something's already committed and needs
correcting before push, the fix is a safe local history rewrite (`git reset --soft` + rebuild),
never a fixup commit stacked on top. See `rules/commit-boundaries.md` for both, with the exact
mechanics used for #120's rebase.

Every commit that implements a GitHub issue carries a `Refs #N` trailer, on its own line after the
body — never `Closes`/`Fixes`, since closing the issue stays a separate, human-approved step (see
"Closing an issue" below). A commit with no issue behind it — the content-backlog commit in this
skill's own evidence, for instance — carries no trailer; this isn't a blanket rule for every commit
in the repository. See `rules/commit-boundaries.md`.

## Verification, at the right scope

Targeted tests plus formatting while building each commit; one full regression run at the
completed-issue boundary — not after every single commit. When a split needs *real* proof (a
rebuild after the fact, or an order where correctness depends on sequence), there's a stronger
technique: commit, `git stash push -u` everything not yet committed, run the full suite against
just what's landed so far, `git stash pop`, repeat. That's how both #120's rebase and #289's
from-scratch build were verified commit-by-commit before any of it was reported done. See
`rules/verification.md`.

Watch specifically for a feature flag retroactively un-skipping pre-existing runtime-gated tests
before their supporting code has landed — that's a real failure mode this workflow hit once
(#120's `SecurityTest.php`) and now checks for on every activation-shaped commit.

## Closing an issue

Opt-in, never automatic, and always after the commits exist. Ask first. If yes: check off the
Tasks that are actually done, add a closing comment (implementation summary, verification numbers,
the real commit SHAs, anything discovered along the way worth keeping on the record), close it, and
then — the same discipline `my-feature-planning` applies to every GitHub mutation it makes —
re-fetch the issue from GitHub and confirm the state, the checkboxes, and the comment actually
landed. A `gh` command's exit code is not proof; reading the result back is. See
`rules/issue-closure.md`.

## What's next

After a validated closure, recompute the milestone's dependency-ready set before doing anything
else — closing one issue routinely unblocks others, and that's worth reporting without being asked.
Summarize the graph (newly ready, still blocked and on what), recommend one issue when there's a
clear case for it, and offer the ready set as a choice when there genuinely are several comparable
options. The human makes the final call, always — and starting the recommended/chosen issue is its
own new pass through this workflow, not a continuation of the current one. See `rules/sequencing.md`.

## Publishing a release

A separate phase, not a continuation of the loop above — it starts once a PR (which may bundle
several issues' worth of committed work, the way PR #298 bundled four) has actually merged, and it
runs once per release, not once per issue.

```
PR merges
  → discover the project's actual release policy (explicit config, else established history)
  → determine the release's primary theme and meaningful outcomes — never from size
  → draft release notes at release-level altitude, grouped by area
  → STOP — human approves the version, tag target, title, and body
  → (approved) publish through the project's own discovered mechanism
  → re-fetch the tag and release, validate every field against what was approved
```

Extracted from the one real run so far: PR #298 (Phase 22 — Authentication & 2FA) merged, then
`v0.17.0 — Authentication & 2FA` shipped as a lightweight tag on the merge commit plus a published
GitHub Release — this repository's own discovered mechanism, found by inspecting 21 prior releases
rather than assumed. Neither the version scheme nor the release mechanism is baked into this
skill's methodology; they're read from each project's own evidence every time, and a project whose
evidence looks different gets a different answer, not this repository's answer applied elsewhere.

The draft-versus-approved gap on `v0.17.0` is the concrete evidence for "release-level altitude": the
first pass grouped outcomes correctly but still led with implementation language (Fortify TOTP, the
`organizations:provision` command, middleware); the approved version described the same five areas
as what a member or Owner actually experiences — recovery codes, the login-time challenge,
interrupted enrollment staying resumable, visible enforcement feedback — with the three runtime
fixes summarized under Bug Fixes rather than re-explained as internals. See `rules/release.md`.

## Milestone completion, after release validation

A further phase, not a continuation of the release loop above and not triggered by issue closure or
PR merge on their own — it starts once release validation has actually passed.

```
release validation passes
  → milestone still open? check the gate, freshly:
      delivery/phase milestone (never Backlog)
      + shipping release published-and-validated
      + zero open issues right now
  → any condition fails → stay open (an open issue blocks closure regardless of release state;
      a newly-discovered follow-up issue re-opens the question even after a clean release)
  → all three hold → STOP, human approves closing
  → (approved) close, then re-fetch and confirm state is actually `closed`
```

> A delivery/phase milestone represents a bounded body of work intended to ship as a release.
> Closing it belongs after that release has shipped and held up — not the moment the last
> currently-known issue happens to close.

This is a forward-looking workflow decision, not something extracted from how this repository has
actually used milestones so far — its full milestone history shows every milestone ever created was
left open, even ones where every issue was already closed. That's evidence of past behavior under a
different, unstated set of assumptions, not a convention this rule preserves; no existing milestone
gets closed retroactively because this phase now exists. See `rules/milestone-completion.md`.

The milestone stays open through implementation, review, and manual testing — a small issue
discovered there that genuinely belongs to the milestone's scope can legitimately be added to it
while it's still open, without that being read as the milestone failing to converge. When a
milestone carries a description (`my-feature-planning`'s optional milestone-description rule), that
description is the contract this skill checks a manual-testing finding's scope against — it doesn't
get reinterpreted here.

Closing the milestone is a validated GitHub mutation like every other one in this skill: explicit
human approval first, then a re-fetch that confirms `state: closed` — never trust the closure
command's exit code alone.

## What this skill owns

**`my-git-workflow` owns:**
- picking up one dependency-ready approved issue at a time
- the implementation review gate and the commit-plan review gate
- proposing and building semantic commit boundaries from the actual diff
- verification scope (targeted vs. full-suite vs. isolation-proving a split)
- commit ordering around feature-activation risk
- the issue-closure recipe and its post-mutation validation
- recalculating and reporting the milestone's dependency-ready set
- after a PR merges: release-policy discovery, release classification, outcome-level drafting, the
  release approval gate, publishing through the project's own mechanism, and post-publication
  validation
- after release validation passes: the post-release milestone-completion gate (delivery/phase only,
  release published-and-validated, zero open issues, all freshly re-checked), the Backlog exemption,
  and the closure mutation itself with its own post-mutation validation

**It does NOT own:**
- deciding what issues should exist, or drafting/creating them
- milestone and label creation, or defining a milestone's scope or description
- the actual application code, tests, or framework-specific conventions
- product/architecture decisions
- any review/approval gate's outcome (implementation, commit plan, release content, or milestone
  closure)
- final sequencing among multiple ready issues
- how a PR gets created, reviewed, or merged, or any deployment automation

Those belong to `my-feature-planning`, the implementation skills, or the human. `my-feature-planning`
defines a milestone and its issue set; this skill is the only one that ever closes one, and only
after release validation and the closure gate both pass.

## Relationship to my-feature-planning and the implementation skills

```
my-feature-planning     → classify / scope / reconcile / draft / review / create GitHub issues
                           and the delivery/phase milestone they belong to
  → issue approved
my-git-workflow         → implement (scope only) / review / commits / review / verify / close
                           (repeats per dependency-ready issue; several may share one PR)
  → PR opened, reviewed, merged        (not yet owned by this skill)
my-git-workflow         → release: discover policy / classify / draft / approve / publish / validate
my-git-workflow         → milestone completion check / closure (delivery/phase only, never Backlog)
  → implementation skills own the code, tests, and framework conventions along the way
  → the human owns product/architecture calls, every review/approval gate, and final sequencing
```

`my-feature-planning` trusts this skill to take an approved issue the rest of the way — and never
closes a milestone itself; its responsibility ends at defining one and its issue set. This skill
trusts `my-feature-planning` never to hand it an issue that hasn't actually been approved, and
trusts the implementation skills to own the code itself — it owns how that finished work moves into
history, through a published release, to the milestone's own eventual closure.

## Is this v0.1, and what's missing on purpose

The implementation-through-closure loop was extracted from four issues implemented on one branch
(`feature/organization-owner-provisioning`). The release phase was added once that branch's PR (#298)
actually merged and shipped as `v0.17.0`. What's still not designed — not guessed at, not left as a
stub, just not built, because there's no real evidence to extract it from yet:

- PR creation and description conventions
- merge strategy
- deployment triggers
- a branch-naming convention — the one branch used throughout the commit/closure evidence carried
  four issues' worth of work, which is one data point about how *this* milestone happened to be
  worked, not a repeatable convention this repository documents anywhere. Don't generalize "one
  branch per issue" or any other scheme from it.

The same method that built this skill — watch what actually happens, extract the rule the evidence
actually supports, say so explicitly when the evidence isn't there yet — is how each of those should
get added later, once there's a real PR-creation pattern or a real merge-strategy choice to learn
from. The release phase itself should keep growing the same way: this repository's own release
mechanism (git tags + GitHub Releases) is recorded as *this project's* discovered evidence in
`rules/release.md`, not baked into the portable methodology — a project with different evidence gets
a different mechanism, discovered the same way.

Milestone completion (`rules/milestone-completion.md`) is the one deliberate exception to that
method: it wasn't extracted from how this repository has actually used milestones — the evidence
there points the other way, every milestone ever created was simply left open. It was added because
the human made an explicit forward-looking workflow decision that milestones should now have a real
completion lifecycle, tied to release validation rather than issue count. Worth keeping distinct
from the rest of this skill's history: everything else here was pulled from what already happened;
this phase was decided, not discovered.
