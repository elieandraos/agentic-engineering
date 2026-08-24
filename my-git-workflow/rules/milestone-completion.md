# Milestone Completion

## Principle

> A delivery/phase milestone passes through two distinct milestone-level gates, never automatically:
> PR readiness, once every milestone issue is closed and final manual testing found nothing more —
> and closure, only after the release that milestone represents has actually shipped and been
> validated, the milestone has no open issues right now, and the human explicitly approves closure.

Neither gate is an automatic consequence of issue closure, PR merge, or release publication — each of
those proves something narrower, and none of them individually proves the milestone is ready for the
next step. This rule owns both checks and the closure mutation itself; it does not own deciding what
belongs in the milestone, and it does not create, review, or merge the PR either gate leads toward.

## Where this phase starts

This rule has two distinct start points, for two distinct gates — do not collapse them:

```
all milestone issues closed  →  MILESTONE PR READINESS  →  (human creates/reviews/merges the PR)
                                                                          │
                                                                          ▼
                                                                    PR merged, human confirms it
                                                                          │
                                                                          ▼
                                                        release.md: authorization → discover policy
                                                        → draft → approve → publish → validate
                                                                          │
                                                                          ▼
                                                              MILESTONE CLOSURE GATE  →  closure
```

- **Milestone PR readiness** (below) starts once `rules/sequencing.md`'s dependency-ready
  recompute finds zero open issues left in the milestone. It never starts earlier — issues can close
  one at a time for a long time before this point, and that's expected, not a signal to check
  readiness early.
- **The closure gate** (below) starts only after release publication has been validated —
  `rules/release.md`'s post-publication validation step. It never starts at issue closure, at PR
  merge, or at PR-readiness itself — passing PR readiness is not evidence the release has shipped.

Each arrow above is a distinct event with its own evidence. None of the earlier ones implies the
later ones:

- **Issue closure** (`rules/issue-closure.md`) closes one issue once its committed work is
  approved — intentionally before the milestone's PR merges (see "Issue closure precedes PR merge"
  under "Milestone PR readiness" below). It says nothing about the milestone that issue belongs to —
  other issues in the same milestone may still be open, and more may still be discovered.
- **Milestone PR readiness** confirms the milestone's shared branch is a reasonable PR candidate. It
  doesn't create the PR, and it doesn't mean a release was cut.
- **PR merge** lands code. It doesn't mean a release was cut, or that the merged result has been
  validated yet.
- **Release + release validation** (`rules/release.md`) confirms a specific version actually
  published correctly. It doesn't by itself confirm every issue the milestone needed is closed —
  release validation can pass cleanly while the milestone still has open work (a Backlog issue
  discovered and filed elsewhere, for instance).
- **Milestone completion check** is the first point where release validation and issue state are
  confirmed together — see "The closure gate" below.
- **Milestone closure** is the mutation itself, gated and validated like every other GitHub
  mutation this workflow performs.

Do not let issue closure, PR-readiness, or PR merge auto-trigger milestone closure. None of them is
evidence of it on its own, and none of them is the closure gate's trigger point.

## What counts as a delivery/phase milestone

A delivery/phase milestone is a bounded body of work intended to ship as a release. That
definition is about scope and intent, not naming syntax — a milestone qualifies by what it bounds,
not by what it's called. Whatever naming convention a given project actually uses for its delivery
milestones, apply this rule the same way once that convention is identified — `my-feature-planning`'s
`rules/issue-conventions.md` is where that convention gets defined (see "Cross-rule dependencies"
below).

A persistent Backlog or other catch-all milestone is not a delivery/phase milestone, regardless of
what it's named — see "Backlog is exempt" below. Backlog/hotfix issues never go through either gate
below — no milestone branch, no PR, no PR-readiness check, no closure gate.

## Milestone PR readiness

> A milestone's shared branch becomes a PR candidate only once every one of its issues is closed,
> the human confirms final manual testing has actually been done, and that testing found nothing
> left to do.

This is the first milestone-level gate, and it is deliberately narrower than the closure gate below:
it's a readiness check for a PR, not a check that the milestone is finished. Passing it means "the
branch is worth putting up for review," not "the milestone is done."

### The three conditions

1. **Every issue in the milestone is closed right now.** Re-query fresh — this is the same trigger
   `rules/sequencing.md`'s recompute reports when the ready set comes back empty.
2. **Final manual testing has actually happened.** This isn't something this rule can verify from
   GitHub state — ask the human directly whether it's been done. Don't infer it from "all issues
   closed" or from time having passed.
3. **That testing found nothing further to do.** If it did, this gate does not pass — see "When
   manual testing finds something" below.

All three must hold together, checked fresh, the same discipline the closure gate uses.

### When manual testing finds something

A bug or missing piece found during this final testing pass is a Discovered-work finding in exactly
the sense `my-feature-planning`'s `rules/discovered-work.md` already defines — it goes through that
same intake, not a special case invented here. The result is a **new issue**, explicitly noting it
was discovered during or after the work represented by the original (now-closed) issue, attached to
this still-open milestone. Re-run this gate from scratch once that new issue closes.

**Do not silently reopen the original closed issue as the default behavior.** Closing that issue was
already an explicit, approved decision (`rules/issue-closure.md`); a new finding doesn't retroactively
undo it. This rule takes no position on whether reopening is ever appropriate in some other
circumstance — it just isn't the default path a manual-testing finding takes.

### Issue closure precedes PR merge — intentionally

Every issue in the milestone is closed, per `rules/issue-closure.md`, at the completed-issue boundary
— before the milestone's PR is even opened, let alone merged. This is the confirmed, intentional
shape of this workflow, not an oversight: an issue's closure marks that its implementation and
verification are done, not that its commits have reached the trunk branch yet. The milestone-level
gates in this file are what actually confirm the aggregate state of all that already-closed work
before it moves toward a PR and, later, a release.

### What this gate does not do

- It does not create the PR. PR creation, review, and merge stay human-owned, exactly as
  `rules/release.md` already states for the phase after this one — this rule only reports whether the
  branch looks ready.
- It does not verify PR content. The observed convention is that the milestone PR references the
  milestone once the human opens it — this rule records that as context, not as something it checks
  or enforces.
- It does not decide milestone closure. That's the separate, later gate below.

Report the result compactly: which of the three conditions hold, and — if not all — what's missing
and why. This is a report, not a mutation, so there's nothing to seek approval for beyond confirming
the manual-testing question with the human.

## The milestone stays open through discovered work

A milestone is not complete merely because every issue known about it right now is closed — this
holds at both gates above and below. Implementation, review, manual testing, and any follow-up
discovered along the way can all still be in flight while the milestone stays open — that's the
expected shape of the middle of this lifecycle, not a sign something's wrong.

A small issue discovered during manual testing that genuinely belongs to this milestone's scope may
legitimately be added to the still-open milestone. Attach it there and keep working the milestone —
don't force it into a separate milestone, or into Backlog, just to preserve a "zero open issues"
appearance on this one.

> Do not infer "milestone complete" from open issues = 0 alone. Zero open issues is necessary for
> PR readiness and for closure, never sufficient by itself for either — see the two gates above and
> below. It's also not a permanent signal: a milestone can go from 0 open issues back to more than 0
> the moment manual testing surfaces something real, and that's a legitimate state, not a bug in the
> process.

## The milestone description, when present, is the scope contract

`my-feature-planning`'s optional milestone-description convention doesn't change here. When a
milestone carries a description defining its intent, boundaries, exclusions, or completion
criteria, that description is what "does this belong to this milestone's scope" gets checked
against when deciding whether a manual-testing finding belongs in this still-open milestone or
somewhere else. This rule consumes that description as-is — it does not draft, redraft,
reinterpret, or second-guess it (see "Cross-rule dependencies" below).

## The closure gate

This is the second, later milestone-level gate — distinct from PR readiness above, and starting only
once release validation has actually passed (see "Where this phase starts"). Close the milestone
only when all three conditions hold at once, checked fresh at the moment of the closure decision:

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

A persistent Backlog (or equivalent catch-all) milestone is never subject to this lifecycle, either
gate. It isn't a bounded body of work shipping as a release, so "is it PR-ready" and "did its release
ship" and "does it have zero open issues right now" are all meaningless questions for it. Do not
propose a PR-readiness check or a closure against it, do not run either gate against it, and do not
treat a quiet stretch of zero open issues on it as anything worth acting on.

## Closing the milestone

Closing a milestone is a validated GitHub mutation, held to the same trust model as every other
mutation this workflow performs: do not infer success from the closure command's exit code alone.

1. **Confirm the gate, explicitly, against freshly queried state** — not memory from earlier in the
   conversation. State which of the three conditions is being confirmed and how, e.g.:
   - "Release `{version}` re-fetched and validated per `rules/release.md`."
   - `gh issue list --milestone "{milestone title}" --state open` returns zero.
2. **Ask for explicit human approval before closing.** This is a real, not-trivially-reversible
   GitHub mutation. Passing the gate is not itself approval to close. If the human says no or not
   yet, leave the milestone open and don't ask again unprompted — the gate gets re-checked fresh
   whenever the human next revisits the question, not on a repeated prompt from this rule.
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

**PR readiness**, report compactly:
- Milestone number/title.
- The three PR-readiness conditions and how each was confirmed (including the human's direct answer
  on manual testing).
- If not ready: what's missing, and — if a new issue was filed — its number and what it references.

**Closure**, report the validated result compactly:
- Milestone number/title.
- The three closure-gate conditions and how each was confirmed.
- The verified closed state.

Do not re-print the milestone's issue list or the release notes — the reader can follow the links.

## Cross-rule dependencies

This rule sits downstream of several other contracts and does not redefine any of them:

- **`rules/sequencing.md`** owns recomputing the dependency-ready set and reports when it's empty —
  that report is what triggers this rule's PR-readiness check. This rule doesn't recompute readiness
  itself.
- **`rules/issue-closure.md`** closes each issue, intentionally before the milestone's PR merges.
  PR readiness's first condition consumes that closed state; this rule doesn't re-decide whether an
  issue should be closed.
- **`my-feature-planning`'s `rules/discovered-work.md`** owns the intake for a manual-testing
  finding — this rule hands off to it rather than defining its own investigation process.
- **`rules/release.md`** owns release drafting, publication, and post-publication validation.
  Condition 2 of the closure gate consumes that validation; this rule does not re-validate a
  release beyond confirming it passed.
- **`my-feature-planning`'s `rules/issue-conventions.md`** owns milestone classification, naming,
  descriptions, and issue drafting. This rule consumes that classification and description as
  given; it does not decide what belongs in a milestone, name one, or draft its description.

## What this rule does not do

- It does not decide milestone scope or draft issues.
- It does not create, review, or merge the PR either gate leads toward — PR creation/merge/review
  stays human-owned.
- It does not run PR readiness before the ready set is actually empty, or closure at issue closure
  or at PR merge.
- It does not touch Backlog or any other persistent catch-all milestone.
- It does not decide whether to reopen a closed issue — a manual-testing finding's default path is a
  new issue, not reopening (see "When manual testing finds something" above).

## Do / Don't

**Do**
- Check PR readiness only once the milestone's ready set is actually empty.
- Ask the human directly whether final manual testing has happened, rather than inferring it.
- File a manual-testing finding as a new Discovered-work issue, referencing the original.
- Re-check all three closure-gate conditions, from fresh state, immediately before closure.
- Treat the milestone description as the scope contract when one exists.
- Ask for explicit human approval before running the closure mutation.
- Verify the resulting state by re-fetching the milestone after closing it.

**Don't**
- Infer PR readiness or completion from zero open issues alone.
- Infer manual testing happened because issues are closed or time has passed.
- Silently reopen a closed issue as the default response to a later finding.
- Infer completion from release publication alone.
- Propose or run either gate against Backlog.
- Trust the closure command's exit code as proof of the resulting state.
- Close a milestone automatically right after release validation, without re-checking issue state
  and without human approval.
