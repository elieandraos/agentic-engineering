# Milestone Completion

## Principle

> A delivery/phase milestone is closed only after the release it represents has actually shipped
> and been validated, the milestone has no open issues right now, and the human explicitly approves
> closure.

Milestone completion is a distinct workflow decision. It is never an automatic consequence of issue
closure, PR merge, or release publication — each of those proves something narrower, and none of
them individually proves the milestone is done. This rule owns the check and the closure mutation
itself; it does not own deciding what belongs in the milestone.

## Where this phase starts

This phase begins only after release publication has been validated — `rules/release.md`'s
post-publication validation step. It never starts at issue closure and never at PR merge.

```
issue closure → PR merge → release → release validation → milestone completion check → closure
```

Each arrow is a distinct event with its own evidence. None of the earlier ones implies the later
ones:

- **Issue closure** (`rules/issue-closure.md`) closes one issue once its committed work is
  approved. It says nothing about the milestone that issue belongs to — other issues in the same
  milestone may still be open, and more may still be discovered.
- **PR merge** lands code. It doesn't mean a release was cut, or that the merged result has been
  validated yet.
- **Release + release validation** (`rules/release.md`) confirms a specific version actually
  published correctly. It doesn't by itself confirm every issue the milestone needed is closed —
  release validation can pass cleanly while the milestone still has open work.
- **Milestone completion check** is the first point where release validation and issue state are
  confirmed together — see "The closure gate" below.
- **Milestone closure** is the mutation itself, gated and validated like every other GitHub
  mutation this workflow performs.

Do not let issue closure or PR merge auto-trigger milestone closure. Neither is evidence of it on
its own, and neither is this rule's trigger point.

## What counts as a delivery/phase milestone

A delivery/phase milestone is a bounded body of work intended to ship as a release. That
definition is about scope and intent, not naming syntax — a milestone qualifies by what it bounds,
not by what it's called. Whatever naming convention a given project actually uses for its delivery
milestones, apply this rule the same way once that convention is identified — `my-feature-planning`'s
`rules/issue-conventions.md` is where that convention gets defined (see "Cross-rule dependencies"
below).

A persistent Backlog or other catch-all milestone is not a delivery/phase milestone, regardless of
what it's named — see "Backlog is exempt" below.

## The milestone stays open through discovered work

A milestone is not complete merely because every issue known about it right now is closed.
Implementation, review, manual testing, and any follow-up discovered along the way can all still be
in flight while the milestone stays open — that's the expected shape of the middle of this
lifecycle, not a sign something's wrong.

A small issue discovered during manual testing that genuinely belongs to this milestone's scope may
legitimately be added to the still-open milestone. Attach it there and keep working the milestone —
don't force it into a separate milestone, or into Backlog, just to preserve a "zero open issues"
appearance on this one.

> Do not infer "milestone complete" from open issues = 0 alone. Zero open issues is necessary for
> closure, never sufficient by itself — see the gate below. It's also not a permanent signal: a
> milestone can go from 0 open issues back to more than 0 the moment manual testing surfaces
> something real, and that's a legitimate state, not a bug in the process.

## The milestone description, when present, is the scope contract

`my-feature-planning`'s optional milestone-description convention doesn't change here. When a
milestone carries a description defining its intent, boundaries, exclusions, or completion
criteria, that description is what "does this belong to this milestone's scope" gets checked
against when deciding whether a manual-testing finding belongs in this still-open milestone or
somewhere else. This rule consumes that description as-is — it does not draft, redraft,
reinterpret, or second-guess it (see "Cross-rule dependencies" below).

## The closure gate

Close the milestone only when all three conditions hold at once, checked fresh at the moment of the
closure decision:

1. **It's a delivery/phase milestone, not Backlog** (or an equivalent persistent catch-all).
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

Each condition is necessary on its own, but no single one is sufficient:

> Zero open issues ≠ milestone complete. Release validated ≠ milestone complete. All three
> conditions, checked from current state, are what closure requires.

## Backlog is exempt

A persistent Backlog (or equivalent catch-all) milestone is never subject to this lifecycle. It
isn't a bounded body of work shipping as a release, so "did its release ship" and "does it have
zero open issues right now" are both meaningless questions for it. Do not propose closing it, do
not run the closure gate against it, and do not treat a quiet stretch of zero open issues on it as
anything worth acting on.

## Closing the milestone

Closing a milestone is a validated GitHub mutation, held to the same trust model as every other
mutation this workflow performs: do not infer success from the closure command's exit code alone.

1. **Confirm the gate, explicitly, against freshly queried state** — not memory from earlier in the
   conversation. State which of the three conditions is being confirmed and how, e.g.:
   - "Release `{version}` re-fetched and validated per `rules/release.md`."
   - `gh issue list --milestone "{milestone title}" --state open` returns zero.
2. **Ask for explicit human approval before closing.** This is a real, not-trivially-reversible
   GitHub mutation. Passing the gate is not itself approval to close.
3. **Run the closure**, using whatever mechanism the installed/project-supported GitHub tooling
   actually offers — discover it rather than assuming a specific command exists. For example:

   ```
   gh api repos/{owner}/{repo}/milestones/{number} -X PATCH -f state=closed
   ```

4. **Re-fetch the milestone afterward** and confirm its state is actually closed:

   ```
   gh api repos/{owner}/{repo}/milestones/{number}
   ```

   A successful exit code from step 3 is not proof; reading the result back is.
5. **Report the result compactly** — see "Reporting" below.

## Reporting

Report the validated result compactly:

- Milestone number/title.
- The three gate conditions and how each was confirmed.
- The verified closed state.

Do not re-print the milestone's issue list or the release notes — the reader can follow the links.

## Cross-rule dependencies

This rule sits downstream of two other contracts and does not redefine either:

- **`rules/release.md`** owns release drafting, publication, and post-publication validation.
  Condition 2 of the closure gate consumes that validation; this rule does not re-validate a
  release beyond confirming it passed.
- **`my-feature-planning`'s `rules/issue-conventions.md`** owns milestone classification, naming,
  descriptions, and issue drafting. This rule consumes that classification and description as
  given; it does not decide what belongs in a milestone, name one, or draft its description.

## What this rule does not do

- It does not decide milestone scope or draft issues.
- It does not run at issue closure or at PR merge.
- It does not touch Backlog or any other persistent catch-all milestone.

## Do / Don't

**Do**
- Re-check all three gate conditions, from fresh state, immediately before closure.
- Treat the milestone description as the scope contract when one exists.
- Ask for explicit human approval before running the closure mutation.
- Verify the resulting state by re-fetching the milestone after closing it.

**Don't**
- Infer completion from zero open issues alone.
- Infer completion from release publication alone.
- Propose or run the closure gate against Backlog.
- Trust the closure command's exit code as proof of the resulting state.
- Close a milestone automatically right after release validation, without re-checking issue state
  and without human approval.
