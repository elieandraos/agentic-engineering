# Milestone Completion

This phase starts after release publication has been validated — `rules/release.md`'s step 6 —
never at issue closure and never at PR merge. It is a new, explicit workflow decision, not an
extraction of past repository practice (see "Forward-looking only" below).

> A delivery/phase milestone represents a bounded body of work intended to ship as a release.
> Closing it belongs after that release has actually shipped and held up — not the moment the last
> currently-known issue happens to close.

## The lifecycle

```
implementation → issue closure → PR → merge → release → release validation
  → milestone completion check → milestone closure
```

Each arrow is a distinct event with its own evidence. None of the earlier ones implies the later
ones:

- **Issue closure** (`rules/issue-closure.md`) closes one issue once its committed work is
  approved. It says nothing about whether the milestone that issue belongs to is done — other
  issues in the same milestone may still be open, and more may still be discovered.
- **PR merge** lands code. It doesn't mean a release was cut, or that manual testing of the merged
  result has happened yet.
- **Release + release validation** (`rules/release.md`) confirms a specific version actually
  published correctly. It doesn't by itself confirm every issue the milestone was going to need is
  closed — the release can validate cleanly while the milestone still has open work.
- **Milestone completion check** is the first point where both of the above are confirmed together
  — see "The closure gate" below.
- **Milestone closure** is the mutation itself, gated and validated like every other GitHub mutation
  this skill performs.

Do not let issue closure or PR merge auto-trigger milestone closure. Neither is evidence of it on
its own.

## What counts as a delivery/phase milestone

A delivery/phase milestone represents a bounded body of work intended to ship as a release — this
project's `Phase NN — {Feature Name}` convention (`my-feature-planning`'s
`rules/issue-conventions.md`). The persistent Backlog milestone (or any similarly persistent
catch-all) is not one — see "Backlog is exempt" below.

## The milestone stays open through discovered work

A milestone is not complete merely because every issue known about it right now is closed.
Implementation, review, manual testing, and any follow-up discovered along the way can all still be
in flight while the milestone stays open — that's the expected shape of the middle of this
lifecycle, not a sign something's wrong.

A small issue discovered during manual testing that genuinely belongs to this milestone's scope may
legitimately be added to the still-open milestone. Attach it there and keep working the milestone —
don't force it into a separate milestone, or into the Backlog, just to preserve a "zero open issues"
appearance on this one.

> Do not infer "milestone complete" from open issues = 0 alone. Zero open issues is necessary for
> closure, never sufficient by itself — see the gate below. It's also not a permanent signal: a
> milestone can go from 0 open issues back to more than 0 the moment manual testing surfaces
> something real, and that's a legitimate state, not a bug in the process.

## The milestone description, when present, is still the contract

`my-feature-planning`'s optional milestone-description rule doesn't change here. When a milestone
carries a description defining its intent, boundaries, exclusions, or completion criteria, that
description is what "does this belong to this milestone's scope" gets checked against when deciding
whether a manual-testing finding belongs in this still-open milestone or somewhere else. This skill
doesn't redraft, reinterpret, or second-guess that description — it applies it as written.

## The closure gate

Close the milestone only when all three hold at once, checked at the moment of the closure
decision:

1. **It's a delivery/phase milestone, not the persistent Backlog** (or equivalent catch-all).
2. **The intended release has been successfully published and validated** —
   `rules/release.md`'s post-publication validation actually passed for the release this milestone
   was shipping.
3. **The milestone has no open issues right now** — re-query it fresh; don't reuse an earlier read
   from before release validation, since discovered work may have added an issue since.

If any one of these doesn't hold, do not close the milestone:

- **An issue remains open** → do not close, regardless of release state. This holds even if the
  open issue looks trivial — the gate is on issue state, not a judgment call about the issue's
  size.
- **Release publication succeeded, but manual testing (or anything else) added another issue to the
  milestone afterward** → the milestone stays open until that issue is completed and the milestone
  is otherwise releasable again. Re-run the whole gate from scratch at that point rather than
  treating the new issue as the only thing left to check — release validation itself doesn't need
  redoing unless the new issue required its own release, but issue-openness and "is this really the
  full set now" both do.
- **The milestone is Backlog or an equivalent persistent catch-all** → this gate does not apply to
  it at all. Don't run it, don't propose closing it, and don't treat its issue count as evidence of
  anything — see "Backlog is exempt."

## Backlog is exempt

The persistent Backlog milestone (`my-feature-planning`'s `rules/issue-conventions.md`, "Backlog vs.
delivery/phase milestones") is never subject to this lifecycle. It isn't a bounded body of work
shipping as a release, so "did its release ship" and "does it have zero open issues right now" are
both meaningless questions for it. Do not propose closing Backlog, do not run the closure gate
against it, and do not treat a quiet stretch of zero open Backlog issues as anything worth acting
on.

## Closing the milestone is a validated mutation

Same trust model as every other GitHub mutation this skill performs
(`rules/issue-closure.md`'s post-mutation validation, `rules/release.md`'s post-publication
validation): do not infer success from the closure command's exit code alone.

1. **Confirm the gate**, explicitly, against freshly queried state — not memory from earlier in the
   conversation. State which of the three conditions is being confirmed and how (e.g. "release
   `v0.18.0` re-fetched and validated per `rules/release.md`; `gh issue list --milestone "Phase 23"
   --state open` returns zero").
2. **Ask for explicit human approval before closing.** This is a real, not-trivially-reversible
   GitHub mutation — the same posture as every other approval gate in this skill (Gate 1, Gate 2,
   the release-content approval). Passing the gate is not itself approval to close.
3. **Run the closure**, e.g. `gh api repos/{owner}/{repo}/milestones/{number} -X PATCH -f
   state=closed` (or whatever mechanism the installed `gh` version actually offers — discover it
   rather than assuming a specific command exists).
4. **Re-fetch the milestone afterward** — `gh api repos/{owner}/{repo}/milestones/{number}` — and
   confirm `state` is actually `closed`. A successful exit code from step 3 is not proof; reading
   the result back is.
5. **Report the result compactly**: milestone number/title, the three gate conditions and how each
   was confirmed, and the verified closed state. Not a re-print of the milestone's issue list or
   release notes.

## Forward-looking only

This is a new, explicit workflow decision — not an extraction of existing repository practice. This
project's full milestone history (checked before this rule existed) showed every milestone ever
created left open, including several where every issue inside was already closed. That was evidence
about how things happened to be left under a different, unstated set of assumptions; it is not the
rule this file follows, and no existing milestone gets retroactively closed because this lifecycle
now exists. This rule governs delivery/phase milestones reaching this point in the workflow from now
on.

## What this phase does not do

It does not decide what belongs in the milestone or draft its issues — that's `my-feature-planning`
(`rules/issue-conventions.md`'s "Milestone descriptions" and "Backlog vs. delivery/phase
milestones"). It does not run at issue-closure time (`rules/issue-closure.md`) or at PR-merge time —
see "The lifecycle" above; both of those are necessary precursors, neither is sufficient on its own.
It does not touch Backlog or any other persistent catch-all milestone.
