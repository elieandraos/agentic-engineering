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
next step. This rule owns both checks, authorized PR creation, and the closure mutation itself; it
does not own deciding what belongs in the milestone, implementing any of it, or approving/merging the
PR — the human retains both.

## Where this phase starts

This rule has two distinct start points, for two distinct gates — do not collapse them:

```
all milestone issues closed  →  MILESTONE PR READINESS  →  MILESTONE PR CREATION
                                                             (this file, below —
                                                              authorized, human-approved)
                                                                          │
                                                                          ▼
                                                        real CI runs against the open PR
                                                                          │
                                                        fails? → see "CI failure on an open
                                                        milestone PR" below → investigate, human
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

- **Milestone PR readiness** (below) starts once the milestone genuinely has zero open issues left —
  the same condition `implement-it/rules/sequencing.md`'s dependency-ready recompute reports, checked
  directly against current GitHub state rather than requiring evidence that a specific `implement-it`
  session produced it. It never starts earlier — issues can close one at a time for a long time
  before this point, and that's expected, not a signal to check readiness early.
- **The closure gate** (below) starts once the human gives the explicit post-merge authorization —
  the same authorization `rules/release.md`'s step 0 asks for, right after a confirmed PR merge. It
  never starts at issue closure, at PR merge, or at PR-readiness itself — none of those is
  authorization. It also does not wait for release publication to complete first: closure and release
  both branch from the same authorization and proceed independently from there — see "Milestone
  closure and release do not gate each other" below.

Each arrow above is a distinct event with its own evidence. None of the earlier ones implies the
later ones:

- **Issue closure** (`implement-it/rules/issue-closure.md`) closes one issue once its committed work is
  approved — intentionally before the milestone's PR merges (see "Issue closure precedes PR merge"
  under "Milestone PR readiness" below). It says nothing about the milestone that issue belongs to —
  other issues in the same milestone may still be open, and more may still be discovered.
- **Milestone PR readiness** confirms the milestone's shared branch is a reasonable PR candidate. It
  is a report, not a mutation — it doesn't create the PR itself, and it doesn't mean a release was
  cut.
- **Milestone PR creation** (below) is the authorized mutation that follows a positive readiness
  report. It says nothing about whether CI passes, and it doesn't mean a release was cut.
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

## Milestone PR readiness

> A milestone's shared branch becomes a PR candidate only once every one of its issues is closed,
> the human confirms final manual testing has actually been done, and that testing found nothing
> left to do.

This is the first milestone-level gate, and it is deliberately narrower than the closure gate below:
it's a readiness check for a PR, not a check that the milestone is finished. Passing it means "the
branch is worth putting up for review," not "the milestone is done."

### The three conditions

1. **Every issue in the milestone is closed right now.** Re-query fresh against current GitHub
   state — this is the same condition `implement-it/rules/sequencing.md`'s recompute reports as zero
   open issues remaining, distinct from an empty dependency-ready set, which can also occur while
   open issues remain, all blocked (that rule's "When the ready set is empty").
2. **Final manual testing has actually happened.** This isn't something this rule can verify from
   GitHub state — ask the human directly whether it's been done. Don't infer it from "all issues
   closed" or from time having passed.
3. **That testing found nothing further to do.** If it did, this gate does not pass — see "When
   manual testing finds something" below.

All three must hold together, checked fresh, the same discipline the closure gate uses.

### When manual testing finds something

A bug or missing piece found during this final testing pass is a Discovered-work finding in exactly
the sense `plan-it`'s `rules/discovered-work.md` already defines — it goes through that
same intake, not a special case invented here. The result is a **new issue**, explicitly noting it
was discovered during or after the work represented by the original (now-closed) issue, attached to
this still-open milestone. Re-run this gate from scratch once that new issue closes.

**Do not silently reopen the original closed issue as the default behavior.** Closing that issue was
already an explicit, approved decision (`implement-it/rules/issue-closure.md`); a new finding doesn't retroactively
undo it. This rule takes no position on whether reopening is ever appropriate in some other
circumstance — it just isn't the default path a manual-testing finding takes.

### Issue closure precedes PR merge — intentionally

Every issue in the milestone is closed, per `implement-it/rules/issue-closure.md`, at the completed-issue boundary
— before the milestone's PR is even opened, let alone merged. This is the confirmed, intentional
shape of this workflow, not an oversight: an issue's closure marks that its implementation and
verification are done, not that its commits have reached the trunk branch yet. The milestone-level
gates in this file are what actually confirm the aggregate state of all that already-closed work
before it moves toward a PR and, later, a release.

### The milestone-PR reference convention

> A PR carrying milestone work is expected to reference the milestone it integrates.

This is a confirmed observed convention of this workflow, not archaeological context from a single
past run. "Milestone PR creation" below is what now produces a PR against that milestone once the
branch is PR-ready — this rule states the convention and is the one that carries it out, subject to
the human approval that section requires; it is no longer merely a contract this rule is aware of
without enforcing.

By contrast, a Backlog/hotfix issue worked directly on the trunk branch produces no PR at all
(`implement-it/rules/sequencing.md`'s "Branch readiness before starting an issue") — the reference convention
applies only to a milestone's PR.

### What this gate does not do

- It does not itself create the PR. Readiness is a report on the branch, not a mutation — creation is
  the separate, later, authorized step in "Milestone PR creation" below.
- It does not decide milestone closure. That's the separate, later gate further below.

Report the result compactly: which of the three conditions hold, and — if not all — what's missing
and why. This is a report, not a mutation, so there's nothing to seek approval for beyond confirming
the manual-testing question with the human.

## Milestone PR creation

> Readiness alone does not authorize creation. Once the three conditions above pass, prepare a
> concrete PR proposal and get explicit human approval of its exact content before creating anything.

The request that led here — asking to check readiness, or asking to create the milestone PR —
already authorizes preparing that proposal; steps 1–3 below need no separate "may I start preparing"
question. What still requires its own explicit approval, before anything is created, is the specific
title, base/head branches, and body actually proposed (step 4) — preparation and creation are
different acts, and only the second is a mutation. This mutation is precedented by, and mirrors,
`rules/release.md`'s own discover → draft → approve → act → validate pattern — a bounded,
already-reviewed shape applied to a new mutation, not a new kind of gate.

1. **Discover the project's PR-target/base-branch convention.** The same discovery order
   `rules/release.md` applies to release mechanism: an explicit repository-stated convention first,
   then a pattern inferred from established history, then ask the human when the evidence is
   ambiguous or conflicting. Do not assume a base branch, head-branch naming, or PR-template
   requirement without evidence.
2. **Check for an existing matching PR before proposing creation.** Query the repository for an open
   PR already carrying this milestone's head branch. Finding one means creation is not this rule's
   next step — report the existing PR instead of proposing a duplicate.
3. **Draft the PR at PR scope.** Title, base and head branches, and a body referencing the milestone
   per "The milestone-PR reference convention" above — describing the integrated change as a whole,
   the same altitude distinction `rules/release.md` draws between a commit, a PR, and a release.
4. **Present the complete proposal — title, base/head branches, and body together — and stop for
   explicit human approval of that exact content before creating anything.** This is the one
   approval this mutation requires — of the specific content about to be created, the same content-
   approval discipline `rules/release.md`'s step 4 applies to a release's exact version/target/
   title/body. Passing readiness, or having been asked to create the PR, is not approval of this
   specific proposal; approval of this proposal is not the PR approval or merge that still belongs to
   the human once the PR exists.
5. **Create the PR through the discovered mechanism once approved**, then re-fetch it and verify the
   actual result — number, base, head, title, and body — instead of trusting the creation command's
   exit code. A mismatch is a failed validation to report and fix, not a cosmetic discrepancy.
6. **PR approval and merge stay entirely human-owned from here.** Creating the PR triggers the
   project's real CI (see "Where this phase starts" above); this rule does not review, approve, or
   merge it.

## CI failure on an open milestone PR

> A milestone's PR looking ready and a milestone's PR actually being green are different facts. Real
> CI failing after the PR opens, before merge, is a distinct moment from either gate above — narrower
> than PR readiness (which only checked local issue/testing state), and earlier than the post-merge
> authorization (which hasn't happened yet because there's no merge to confirm).

This is not a new gate with its own approval — it's this rule naming a moment its existing phase
diagram would otherwise pass over silently: real CI running against an already-open, not-yet-merged
milestone PR can fail, and the milestone stays in this in-between state — PR open, not merged, not
authorized for post-merge progression — until it's resolved.

**This rule investigates, explains, and secures the human's authorization; `implement-it` performs
the authorized correction.** This rule never edits application code itself — steps 1–5 below are
this rule's own job: investigating, determining scope, and either asking for and confirming the
human's explicit authorization for an already-approved-scope correction, or routing genuinely new
scope to `plan-it`'s discovered-work intake. Only step 6, performing the correction, is
`implement-it`'s — and only once the human has actually authorized it. This rule's own determination
that a fix stays in scope is necessary background for that authorization; it is not the authorization
itself, and never substitutes for it.

1. **The PR stays unmerged.** A red CI run on an open PR is never a reason to merge anyway, wait it
   out, or treat local green as sufficient — merge remains blocked until the PR is genuinely green
   again.
2. **Investigate the failure before recommending a remedy.** Root-cause it the same way any other
   unexpected finding gets investigated before a fix is chosen — don't guess at a correction from the
   failure message alone.
3. **Determine whether the correction stays within already-approved milestone scope, or introduces new
   scope or another decision, and explain what correction is needed.** A fix that only corrects what
   the milestone's own issues already approved (a config/workflow file wired up incorrectly, a
   dependency pin that needs adjusting to what was already intended) is different from one that
   touches something no issue in the milestone scoped — determine which this is, per
   `implement-it/rules/review-gates.md`'s "when to stop and ask" (a commit decomposition or scope
   question with no clearly better answer is exactly that kind of stop), and report the finding and
   the correction it calls for.
4. **A correction that stays within already-approved scope, including an already-closed issue's
   scope, requires explicit human authorization before `implement-it` performs it.** The issue that
   scope belongs to may have already gone through its own approved implementation, review, and
   closure (`implement-it/rules/issue-closure.md`) — reopening that work implicitly, without asking,
   would silently bypass the review this workflow already gave it. This does not require reopening
   the closed issue, or creating a new one, to permit the correction. Ask, and only hand the fix to
   `implement-it` once the human explicitly authorizes a direct fix.
5. **Otherwise, route the finding through the existing discovered-work intake.** A failure that reveals
   real, unscoped work — not a correction to something already approved — is a Discovered-work finding
   in exactly the sense `plan-it`'s `rules/discovered-work.md` already defines (the same
   intake this rule's "When manual testing finds something" section, above, also hands off to). Create
   or attach an issue to the still-open milestone when that intake finds the finding
   warrants one — this is not automatic for every CI failure; a narrow, already-scoped correction with
   explicit human authorization (step 4) can be the legitimate direct-fix path instead, without a new
   issue.
6. **`implement-it` performs the authorized correction through its own lifecycle** — Gate 1/Gate 2 as
   applicable, commit construction (`implement-it/rules/commit-boundaries.md`), and verification
   (`implement-it/rules/verification.md`) — then pushes once authorized. This rule resumes once the
   correction is verified and pushed: confirm real CI runs again against the PR.
7. **No merge, milestone closure, or release progression until the PR is genuinely green and the human
   authorizes the next boundary.** A second (or later) real CI failure on the same PR repeats this
   section from step 1 — there is no cap on how many times this can legitimately happen before the PR
   is actually green.

Not every CI failure on an open milestone PR demands a new issue — a narrow, in-scope, explicitly
authorized direct fix (steps 3–4) is a legitimate outcome of this section, not a fallback to avoid.
What this section prevents is the other failure mode: silently patching the milestone branch past a
real CI failure with no authorization, or no investigation, because the milestone already looked
PR-ready. This rule does not implement the fix under this flow, and this route stays available
without requiring an open issue to exist.

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
2. **Run the closure**, using whatever mechanism the installed/project-supported GitHub tooling
   actually offers — discover it rather than assuming a specific command exists. For example:

   ```
   gh api repos/{owner}/{repo}/milestones/{number} -X PATCH -f state=closed
   ```

3. **Re-fetch the milestone afterward** and confirm its state is actually closed:

   ```
   gh api repos/{owner}/{repo}/milestones/{number}
   ```

   A successful exit code from step 2 is not proof; reading the result back is.
4. **Report the result compactly** — see "Reporting" below.

## Reporting

**PR readiness**, report compactly:
- Milestone number/title.
- The three PR-readiness conditions and how each was confirmed (including the human's direct answer
  on manual testing).
- If not ready: what's missing, and — if a new issue was filed — its number and what it references.

**PR creation**, report the validated result compactly:
- The discovered PR-target/base-branch convention and its source.
- The proposed title, base/head branches, and body, and the human's approval of them.
- The created PR's number, base, head, title, and body as re-fetched — not merely the creation
  command's exit code.

**Closure**, report the validated result compactly:
- Milestone number/title.
- The three closure-gate conditions and how each was confirmed.
- The verified closed state.
- If not eligible: which condition is missing — nothing further is asked until the human revisits
  it.

Do not re-print the milestone's issue list or the release notes — the reader can follow the links.

## Cross-rule dependencies

This rule sits downstream of several other contracts and does not redefine any of them:

- **`implement-it/rules/sequencing.md`** owns recomputing the dependency-ready set and reports zero
  open issues remaining, distinct from an empty ready set that can still hold open, blocked issues —
  that condition is what makes this rule's PR-readiness check applicable, checked directly against
  current GitHub state rather than requiring a live report from a specific session. This rule doesn't
  recompute readiness itself.
- **`implement-it/rules/issue-closure.md`** closes each issue, intentionally before the milestone's PR merges.
  PR readiness's first condition consumes that closed state; this rule doesn't re-decide whether an
  issue should be closed.
- **`plan-it`'s `rules/discovered-work.md`** owns the intake for a manual-testing
  finding — this rule hands off to it rather than defining its own investigation process. A CI failure
  on an open milestone PR that reveals unscoped work hands off to the same intake (see "CI failure on
  an open milestone PR" above).
- **`implement-it/rules/review-gates.md`** owns the "when to stop and ask" standard this rule's
  CI-failure section applies to decide whether a correction stays in scope or needs a new decision.
  This rule investigates, explains, and secures the human's explicit authorization for the
  correction; only once that authorization is given does **`implement-it`'s own lifecycle** — that
  same gate, plus `implement-it/rules/commit-boundaries.md` and `implement-it/rules/verification.md`
  — actually perform, commit, and verify it (see "CI failure on an open milestone PR" above). This
  rule does not implement, and its own scope determination is not itself the authorization.
- **`rules/release.md`** owns release drafting, publication, and post-publication validation, and
  its step 0 owns asking the post-merge authorization this rule's condition 2 also consumes. Neither
  rule's completion is a precondition for the other's gate — see "Milestone closure and release do
  not gate each other."
- **`plan-it`'s `rules/issue-conventions.md`** owns milestone classification, naming,
  descriptions, and issue drafting. This rule consumes that classification and description as
  given; it does not decide what belongs in a milestone, name one, or draft its description.

## What this rule does not do

- It does not decide milestone scope or draft issues.
- It does not review or merge the PR it creates — approval and merge stay human-owned. Authorized
  creation itself is this rule's own job ("Milestone PR creation" above).
- It does not implement a delivery correction itself, and its own investigation grants no
  authority — `implement-it` performs the fix only once the human explicitly authorizes it
  ("CI failure on an open milestone PR" above).
- It does not run PR readiness before the milestone actually has zero open issues remaining, or
  closure at issue closure or at PR merge.
- It does not touch Backlog or any other persistent catch-all milestone.
- It does not decide whether to reopen a closed issue — a manual-testing finding's default path is a
  new issue, not reopening (see "When manual testing finds something" above).
- It does not require release publication to have completed before closing the milestone, and
  closing the milestone is not itself a precondition for release publication — the two proceed
  independently once the human gives post-merge authorization (see "Milestone closure and release do
  not gate each other").
- It does not ask for a second, separate human approval before closing. The post-merge authorization
  already covers it; this rule only re-verifies that authorization and eligibility are both actually
  present before acting.
- It does not require every real CI failure on an open milestone PR to produce a new issue — a
  narrow, already-approved-scope correction with explicit human authorization is a legitimate direct
  fix (see "CI failure on an open milestone PR" above).

## Do / Don't

**Do**
- Check PR readiness only once the milestone actually has zero open issues remaining, re-verified
  against current GitHub state.
- Ask the human directly whether final manual testing has happened, rather than inferring it.
- File a manual-testing finding as a new Discovered-work issue, referencing the original.
- Re-check all three closure-gate conditions, from fresh state, immediately before closure.
- Treat the same post-merge authorization that opens `rules/release.md`'s phase as this gate's own
  trigger too — not release validation.
- Treat the milestone description as the scope contract when one exists.
- Confirm post-merge authorization was already given and actually covers closure — don't ask for it
  again — before running the closure mutation.
- Verify the resulting state by re-fetching the milestone after closing it.
- Discover PR conventions, check for an existing matching PR, and present a complete title/branches/
  body proposal for explicit human approval before creating the milestone PR.
- Re-fetch a created PR to verify number, base, head, title, and body instead of trusting the
  creation command's exit code.
- Keep an open milestone PR unmerged through a real CI failure, investigate before recommending a
  remedy, and get explicit human authorization before handing `implement-it` an already-closed
  issue's scope to correct directly on the branch.

**Don't**
- Infer PR readiness or completion from zero open issues alone.
- Infer manual testing happened because issues are closed or time has passed.
- Silently reopen a closed issue as the default response to a later finding.
- Infer completion from release publication alone.
- Require release publication to finish before checking or passing the closure gate, or treat
  milestone closure as something `rules/release.md` must wait for.
- Propose or run either gate against Backlog.
- Trust the closure command's exit code as proof of the resulting state.
- Merge, close the milestone, or start release progression while an open milestone PR's CI is red.
- Create a duplicate milestone PR without first checking for an existing one, or create any milestone
  PR before the human approves the exact proposed title, branches, and body.
- Implement a delivery correction directly, or authorize `implement-it` to patch an already-closed
  issue's scope on the milestone branch without explicit human authorization; force every CI failure
  through a new issue when an authorized direct fix is the legitimate path.
- Close a milestone without re-checking issue state and authorization fresh, immediately before the
  mutation.
- Ask for a second, separate approval to close once post-merge authorization already covers it.
