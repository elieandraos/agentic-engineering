# Milestone Completion

## Principle

> A delivery/phase milestone passes through two distinct milestone-level gates, never automatically:
> PR readiness, once every milestone issue is closed and final manual testing found nothing more —
> and closure, gated on the human's post-merge authorization already covering it and the milestone
> having no open issues right now, both verified fresh immediately before the mutation. That
> authorization is the human approval for closure — this gate does not ask for it a second time.
> Closure also does not wait on the release that milestone represents to have shipped first — see
> "Milestone closure and release do not gate each other" below.

Neither gate is an automatic consequence of issue closure, PR merge, or release publication — each of
those proves something narrower, and none of them individually proves the milestone is ready for the
next step. This rule owns the closure mutation itself and the shared entry map below; PR readiness
and authorized PR creation are `rules/milestone-pr-readiness.md`'s own contract, and the CI-failure
investigation/authorization split in between is `rules/ci-failure-correction.md`'s. None of the three
files owns deciding what belongs in the milestone, implementing any of it, or approving/merging the
PR — the human retains both.

## Where this phase starts

This rule has two distinct start points, for two distinct gates — do not collapse them:

```
all milestone issues closed  →  MILESTONE PR READINESS  →  MILESTONE PR CREATION
                                                             (rules/milestone-pr-readiness.md —
                                                              authorized, human-approved)
                                                                          │
                                                                          ▼
                                                        real CI runs against the open PR
                                                                          │
                                                        fails? → see rules/ci-failure-correction.md
                                                        → investigate, human
                                                        authorizes → implement-it fixes, re-verifies
                                                        → real CI re-runs → repeat until green
                                                                          │
                                                                          ▼
                                                              (human merges once genuinely green)
                                                                          │
                                                                          ▼
                                                                    PR merged, human confirms it
                                                                          │
                                                                          ▼
                                       STOP: explicit human authorization to begin the
                                       post-merge progression (rules/release.md's step 0 —
                                       one ask, both branches below)
                                                    │                              │
                                                    ▼                              ▼
                                    MILESTONE CLOSURE GATE              release.md: discover policy
                                    (this file, below)                   → draft → approve → publish
                                                                                    → validate
```

- **Milestone PR readiness** (`rules/milestone-pr-readiness.md`) starts once the milestone genuinely
  has zero open issues left — the same condition `implement-it/rules/sequencing.md`'s dependency-ready
  recompute reports, checked directly against current GitHub state rather than requiring evidence
  that a specific `implement-it` session produced it. It never starts earlier — issues can close one
  at a time for a long time before this point, and that's expected, not a signal to check readiness
  early.
- **The closure gate** (below) starts once the human gives the explicit post-merge authorization —
  the same authorization `rules/release.md`'s step 0 asks for, right after a confirmed PR merge. It
  never starts at issue closure, at PR merge, or at PR-readiness itself — none of those is
  authorization. It also does not wait for release publication to complete first: closure and release
  both branch from the same authorization and proceed independently from there — see "Milestone
  closure and release do not gate each other" below.

Each arrow above is a distinct event with its own evidence. None of the earlier ones implies the
later ones:

- **Issue closure** (`implement-it/rules/issue-closure.md`) closes one issue once its committed work is
  approved — intentionally before the milestone's PR merges (see `rules/milestone-pr-readiness.md`'s
  "Issue closure precedes PR merge"). It says nothing about the milestone that issue belongs to —
  other issues in the same milestone may still be open, and more may still be discovered.
- **Milestone PR readiness** confirms the milestone's shared branch is a reasonable PR candidate. It
  is a report, not a mutation — it doesn't create the PR itself, and it doesn't mean a release was
  cut.
- **Milestone PR creation** (`rules/milestone-pr-readiness.md`) is the authorized mutation that
  follows a positive readiness report. It says nothing about whether CI passes, and it doesn't mean a
  release was cut.
- **PR merge** lands code. It doesn't mean a release was cut, or that the merged result has been
  validated yet.
- **Post-merge authorization** is the human's explicit go-ahead, right after confirming the PR
  merged, to begin the post-merge progression at all (`rules/release.md`'s step 0). It opens both the
  closure gate below and `rules/release.md`'s drafting/publication — neither branch is implied to wait
  for the other to finish.
- **Release + release validation** (`rules/release.md`) confirms a specific version actually
  published correctly. It doesn't by itself confirm every issue the milestone needed is closed —
  release validation can pass cleanly while the milestone still has open work (a Backlog issue
  discovered and filed elsewhere, for instance) — and it is not a precondition this rule's closure
  gate requires; see "Milestone closure and release do not gate each other" below.
- **Milestone completion check** is the first point where post-merge authorization and current issue
  state are confirmed together — see "The closure gate" below.
- **Milestone closure** is the mutation itself, gated and validated like every other GitHub
  mutation this workflow performs.

Do not let issue closure, PR-readiness, or PR merge auto-trigger milestone closure. None of them is
evidence of it on its own, and none of them is the closure gate's trigger point. Release publication
does not auto-trigger milestone closure either, and milestone closure does not auto-trigger release
publication — each proceeds through its own rule, both starting from the same authorization.

## Milestone closure and release do not gate each other

> Both branches below start from the same event — the human's explicit post-merge authorization —
> and each proceeds entirely through its own rule from there. Neither is a precondition for the
> other.

This rule's closure gate does not wait for `rules/release.md`'s post-publication validation to have
passed, and `rules/release.md` does not wait for this rule's closure to have happened. On the project
this workflow was extracted from, the human has typically closed the milestone first and drafted the
release after — but that is an observed sequencing habit on one project, not a rule either file
enforces. A different project running the two in the opposite order, interleaved, or with real time
between them, is equally valid under this methodology.

## What counts as a delivery/phase milestone

A delivery/phase milestone is a bounded body of work intended to ship as a release. That
definition is about scope and intent, not naming syntax — a milestone qualifies by what it bounds,
not by what it's called. Whatever naming convention a given project actually uses for its delivery
milestones, apply this rule the same way once that convention is identified — `plan-it`'s
`rules/issue-conventions.md` is where that convention gets defined (see "Cross-rule dependencies"
below).

A persistent Backlog or other catch-all milestone is not a delivery/phase milestone, regardless of
what it's named — see "Backlog is exempt" below. Backlog/hotfix issues never go through either gate
below — no milestone branch, no PR, no PR-readiness check, no closure gate.

## The milestone stays open through discovered work

A milestone is not complete merely because every issue known about it right now is closed — this
holds at both milestone-level gates: PR readiness (`rules/milestone-pr-readiness.md`) and closure
(below). Implementation, review, manual testing, and any follow-up discovered along the way can all
still be in flight while the milestone stays open — that's the expected shape of the middle of this
lifecycle, not a sign something's wrong.

A small issue discovered during manual testing that genuinely belongs to this milestone's scope may
legitimately be added to the still-open milestone. Attach it there and keep working the milestone —
don't force it into a separate milestone, or into Backlog, just to preserve a "zero open issues"
appearance on this one.

> Do not infer "milestone complete" from open issues = 0 alone. Zero open issues is necessary for
> PR readiness and for closure, never sufficient by itself for either — see
> `rules/milestone-pr-readiness.md` and the closure gate below. It's also not a permanent signal: a
> milestone can go from 0 open issues back to more than 0 the moment manual testing surfaces
> something real, and that's a legitimate state, not a bug in the process.

## The milestone description, when present, is the scope contract

`plan-it`'s optional milestone-description convention doesn't change here. When a
milestone carries a description defining its intent, boundaries, exclusions, or completion
criteria, that description is what "does this belong to this milestone's scope" gets checked
against when deciding whether a manual-testing finding belongs in this still-open milestone or
somewhere else. This rule consumes that description as-is — it does not draft, redraft,
reinterpret, or second-guess it (see "Cross-rule dependencies" below).

## The closure gate

This is the second, later milestone-level gate — distinct from PR readiness above, and starting once
the human has given the explicit post-merge authorization (see "Where this phase starts"). That
authorization *is* the human approval for this mutation: this gate verifies eligibility against
current fact, it does not request a second, separate approval to close. Close the milestone once all
three conditions hold at once, checked fresh at the moment of the closure decision:

1. **It's a delivery/phase milestone, not Backlog** (or an equivalent persistent catch-all).
2. **The human's post-merge authorization actually covers closure.** This is the same authorization
   `rules/release.md`'s step 0 asks for right after the human confirms the PR merged — confirmed here
   as already given, not re-requested. It is not implied by the release itself having been drafted,
   published, or validated — see "Milestone closure and release do not gate each other."
3. **The milestone has no open issues right now** — re-query it fresh; don't reuse an earlier read
   from before authorization, since discovered work may have added an issue since.

If any one of these doesn't hold, do not close the milestone — report what's missing and stop, the
same discipline `implement-it/rules/issue-closure.md` uses for a declined close: don't ask again unprompted, the
human revisits it when ready.

- **An issue remains open** → do not close, regardless of release state. This holds even if the
  open issue looks trivial — the gate is on issue state, not a judgment call about the issue's
  size.
- **Authorization hasn't been given, or didn't cover closure** → do not close. This gate cannot
  substitute its own approval for that authorization, and it does not wait on the release to have
  published first to become eligible.
- **Manual testing (or anything else) added another issue to the milestone after authorization** →
  the milestone stays open until that issue is completed and the milestone is otherwise closeable
  again. Re-run the whole gate from scratch at that point rather than treating the new issue as the
  only thing left to check.
- **The milestone is Backlog or an equivalent persistent catch-all** → this gate does not apply to
  it at all. Don't run it, don't propose closing it, and don't treat its issue count as evidence of
  anything — see "Backlog is exempt."

Each condition is necessary on its own, but no single one is sufficient:

> Zero open issues ≠ milestone complete. Post-merge authorization alone ≠ milestone complete either.
> All three conditions, checked from current state, are what closure requires — and once they do,
> closing proceeds without asking the human to approve the same closure twice.

## Backlog is exempt

A persistent Backlog (or equivalent catch-all) milestone is never subject to this lifecycle, either
gate. It isn't a bounded body of work shipping as a release, so "is it PR-ready" and "did its release
ship" and "does it have zero open issues right now" are all meaningless questions for it. Do not
propose a PR-readiness check or a closure against it, do not run either gate against it, and do not
treat a quiet stretch of zero open issues on it as anything worth acting on.

## Closing the milestone

Closing a milestone is a validated GitHub mutation, held to the same trust model as every other
mutation this workflow performs: do not infer success from the closure command's exit code alone.

Closure does not get its own, second human approval. The post-merge authorization already granted —
"close the milestone and start the release?" or whatever form it actually took — is the approval for
this mutation. This rule's job is to confirm that authorization is actually present and actually
covers closure, confirm the milestone is actually eligible, and then act — not to ask the human to
approve the same closure a second time.

1. **Confirm the gate, explicitly, against freshly queried state** — not memory from earlier in the
   conversation. State which of the three conditions is being confirmed and how, e.g.:
   - "Post-merge authorization for milestone `{title}` was given by the human on {reference}, and
     covered closure."
   - `gh issue list --milestone "{milestone title}" --state open` returns zero.

   If any condition doesn't hold — including authorization not actually having been given, or given
   but not scoped to closure — stop here and report what's missing instead of closing. Don't ask
   again unprompted; the human revisits it when ready.
2. **Before running the closure mutation, check whether a prior attempt already succeeded.** A lost
   response or a retried request is not evidence the milestone is still open — fetch its current
   state (the same query step 4 below runs) before mutating. If it's already closed, don't run the
   closure mutation again; validate the existing closed state against the gate just confirmed and
   report it as the completed result, rather than re-issuing a mutation that risks erroring or
   masking what actually happened.
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

See `rules/milestone-pr-readiness.md`'s own "Reporting" for PR-readiness and PR-creation reports —
this section covers closure only.

**Closure**, report the validated result compactly:
- Milestone number/title.
- The three closure-gate conditions and how each was confirmed.
- The verified closed state.
- If not eligible: which condition is missing — nothing further is asked until the human revisits
  it.

Do not re-print the milestone's issue list or the release notes — the reader can follow the links.

## Cross-rule dependencies

This rule sits downstream of several other contracts and does not redefine any of them:

- **`implement-it/rules/issue-closure.md`** closes each issue, intentionally before the milestone's PR
  merges — this rule's closure gate re-verifies zero open issues at the moment of closure, but doesn't
  re-decide whether any individual issue should have been closed.
- **`rules/release.md`** owns release drafting, publication, and post-publication validation, and
  its step 0 owns asking the post-merge authorization this rule's condition 2 also consumes. Neither
  rule's completion is a precondition for the other's gate — see "Milestone closure and release do
  not gate each other."
- **`plan-it`'s `rules/issue-conventions.md`** owns milestone classification, naming,
  descriptions, and issue drafting. This rule consumes that classification and description as
  given; it does not decide what belongs in a milestone, name one, or draft its description.
- **`rules/milestone-pr-readiness.md`** owns milestone PR readiness and authorized creation, the
  earlier milestone-level gate this one is deliberately narrower than.
  **`rules/ci-failure-correction.md`** owns the CI-failure investigation/authorization split between
  PR creation and merge. Neither is restated here.

## What this rule does not do

- It does not decide milestone scope or draft issues.
- It does not run closure at issue closure or at PR merge.
- It does not touch Backlog or any other persistent catch-all milestone.
- It does not require release publication to have completed before closing the milestone, and
  closing the milestone is not itself a precondition for release publication — the two proceed
  independently once the human gives post-merge authorization (see "Milestone closure and release do
  not gate each other").
- It does not ask for a second, separate human approval before closing. The post-merge authorization
  already covers it; this rule only re-verifies that authorization and eligibility are both actually
  present before acting.

`rules/milestone-pr-readiness.md` and `rules/ci-failure-correction.md` state their own negatives for
PR readiness/creation and CI-failure correction respectively; not restated here.

## Do / Don't

**Do**
- Re-check all three closure-gate conditions, from fresh state, immediately before closure.
- Treat the same post-merge authorization that opens `rules/release.md`'s phase as this gate's own
  trigger too — not release validation.
- Confirm post-merge authorization was already given and actually covers closure — don't ask for it
  again — before running the closure mutation.
- Verify the resulting state by re-fetching the milestone after closing it.
- Re-query before retrying an interrupted or ambiguous closure mutation — a milestone already closed
  by an earlier attempt — and validate what's found rather than assuming nothing happened.

**Don't**
- Infer completion from zero open issues alone, or from release publication alone.
- Require release publication to finish before checking or passing the closure gate, or treat
  milestone closure as something `rules/release.md` must wait for.
- Propose or run closure against Backlog.
- Trust the closure command's exit code as proof of the resulting state.
- Treat a failed or timed-out query as proof a prior closure mutation didn't happen.
- Re-run the closure mutation against a milestone a prior attempt already closed.
- Close a milestone without re-checking issue state and authorization fresh, immediately before the
  mutation.
- Ask for a second, separate approval to close once post-merge authorization already covers it.

`rules/milestone-pr-readiness.md` and `rules/ci-failure-correction.md` each state their own Do/Don't
for PR readiness/creation and CI-failure correction; not restated here.
