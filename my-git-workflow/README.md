# my-git-workflow

## What this skill is

`my-git-workflow` is the **delivery stage** of the Agentic Engineering pipeline:

```
my-architecture-laboratory   → understand and reconstruct reality
my-feature-planning          → turn that understanding into approved work
my-git-workflow              → turn approved work into verified delivery      (this skill)
```

It picks up one already-approved work item at a time, implements only its scope, stops for human
review, turns the finished diff into a small number of coherent commits (also reviewed before
they're written), verifies at the right scope, optionally closes the item, and tells you what's
unblocked next. Separately, once a PR carrying that work has merged, it discovers the project's real
release policy, classifies the release, drafts outcome-level notes, stops for approval, publishes,
and validates the result. Separately again, once that release is validated, it checks whether the
milestone the work belonged to is actually ready to close.

The methodology below is reusable as stated. A project on a different stack — a different language,
issue tracker, or release mechanism — still applies the same review gates, the same commit-boundary
reasoning, the same verification discipline, and the same release/milestone lifecycle, discovering its
own concrete answer at every point this skill says "the project's own." Where this skill names a
concrete mechanism directly — GitHub issues, the `gh` CLI, git tags — that's the platform this version
of the skill happens to be built against, not a requirement the methodology imposes (see "Boundaries,
dependencies, and composition" below).

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

## What it takes as input

An approved work item from the planning stage (`my-feature-planning`) — concretely, in this skill's
own implementation, a GitHub issue that has already been drafted, reviewed, and approved. This is an
intentional pipeline boundary, not incidental project coupling: this skill never decides what work
should exist, and never starts earlier than an already-approved item.

- It doesn't decide what work should exist — that's `my-feature-planning`.
- It doesn't write the application code — that's whichever implementation skills the code demands.
- It doesn't (yet) decide how a PR gets opened or merged — see "Known v0.1 limitations" below.

It owns everything from an approved item through implementation, review, commits, verification, and
optional closure — then, once merged, release — and finally, once that release is validated, milestone
completion and closure.

## What this skill owns

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

What it does *not* own is covered in "Boundaries, dependencies, and composition" below.

## The working lifecycle

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

### Semantic commit boundaries

Not a mechanical split by folder or file extension. A semantic commit is one implementation decision
you could describe in a single sentence of *why*. Each one, read alone at its point in history, should
leave a coherent, non-broken implementation state that doesn't depend on a later commit to become
structurally valid — even an "inert" early commit, which does nothing observable yet but stands
correctly on its own terms. What makes a commit *not* coherent isn't smallness, and it isn't "does
nothing observable yet" either — it's referencing something that doesn't exist until the next commit,
or bundling two unrelated decisions because they happened to touch the diff at the same time.

Tests travel with the step they prove, not split into a separate commit. A commit with nothing yet to
observe (no consumer, a feature flag still off) can legitimately ship with no new tests of its own —
its proof is that the full suite stays exactly as green as it was before it landed.

Review corrections found before anything is committed just land inside whichever commit they belong
to — no separate "fix review comments" commit. If something's already committed and needs correcting
before push, the fix is a safe local history rewrite (`git reset --soft` + rebuild), never a fixup
commit stacked on top. See `rules/commit-boundaries.md` for the full reasoning, and "Origin and
observed evidence" below for the real split it was extracted from.

Every commit that implements a tracked work item carries a `Refs #N` trailer, on its own line after
the body — never `Closes`/`Fixes`, since closing the issue stays a separate, human-approved step (see
"Issue closure" below). A commit with no tracked item behind it carries no trailer; this isn't a
blanket rule for every commit in the repository. See `rules/commit-boundaries.md`.

### Verification, at the right scope

Targeted tests plus formatting while building each commit; one full regression run at the
completed-issue boundary — not after every single commit. When a split needs *real* proof (a rebuild
after the fact, or an order where correctness depends on sequence), there's a stronger technique:
commit, `git stash push -u` everything not yet committed, run the full suite against just what's
landed so far, `git stash pop`, repeat. See `rules/verification.md` for the full technique.

Watch specifically for a feature flag retroactively un-skipping pre-existing runtime-gated tests
before their supporting code has landed — a real failure mode this skill's evidence hit once (see
"Origin and observed evidence" below), and now checks for on every activation-shaped commit.

### Issue closure

Opt-in, never automatic, and always after the commits exist. Ask first. If yes: check off the Tasks
that are actually done, add a closing comment (implementation summary, verification numbers, the real
commit SHAs, anything discovered along the way worth keeping on the record), close it, and then — the
same discipline `my-feature-planning` applies to every GitHub mutation it makes — re-fetch the issue
and confirm the state, the checkboxes, and the comment actually landed. A `gh` command's exit code is
not proof; reading the result back is. See `rules/issue-closure.md`.

### What's next

After a validated closure, recompute the milestone's dependency-ready set before doing anything else
— closing one issue routinely unblocks others, and that's worth reporting without being asked.
Summarize the graph (newly ready, still blocked and on what), recommend one issue when there's a clear
case for it, and offer the ready set as a choice when there genuinely are several comparable options.
The human makes the final call, always — and starting the recommended/chosen issue is its own new pass
through this workflow, not a continuation of the current one. See `rules/sequencing.md`.

## Core principles

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

Treating those as the same unit of work produces bad history either way: one giant commit per issue
loses the actual implementation narrative, and mechanically splitting a diff by file type or directory
produces commits nobody would recognize as a real decision. Nothing about file count, issue size, or
"how many things changed" predicts which shape a given issue's commits should take — only the actual
diff does.

A few standing rules run through every rule file in this skill:

- **Two review gates, not one, on the pre-merge side.** Approving the implementation is never
  approval of a commit structure.
- **Never trust a mutation's exit code.** Every GitHub mutation this skill performs — issue closure,
  release publication, milestone closure — is re-fetched and validated against the source of truth
  afterward.
- **Discover the project's own mechanism before assuming one.** Release policy and publish tooling
  (and, implicitly, formatting/test tooling) are read from what the project actually has, never
  assumed from a template.
- **A stop is a report plus a question, not a wall of options with no recommendation.** Investigate
  enough to have a position, state it, and let the human decide (`rules/review-gates.md`).

## Release and milestone-completion lifecycle

### Publishing a release

A separate phase, not a continuation of the working lifecycle above — it starts once a PR (which may
bundle several issues' worth of committed work) has actually merged, and it runs once per release, not
once per issue.

```
PR merges
  → discover the project's actual release policy (explicit config, else established history)
  → determine the release's primary theme and meaningful outcomes — never from size
  → draft release notes at release-level altitude, grouped by area
  → STOP — human approves the version, tag target, title, and body
  → (approved) publish through the project's own discovered mechanism
  → re-fetch the tag and release, validate every field against what was approved
```

Neither the version scheme nor the release mechanism is baked into this skill's methodology — they're
read from each project's own evidence every time, and a project whose evidence looks different gets a
different answer than the one this skill was built against. See "Origin and observed evidence" below
for that answer, and `rules/release.md` for the full policy-discovery method.

### Milestone completion, after release validation

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

> A delivery/phase milestone represents a bounded body of work intended to ship as a release — that's
> about scope and intent, not naming syntax. Closing it belongs after that release has shipped and
> held up, not the moment the last currently-known issue happens to close.

This is a forward-looking workflow decision — the one deliberate exception to how the rest of this
skill was built (see "Origin and observed evidence" below for what the alternative would have been and
why it wasn't followed). No existing milestone is retroactively closed because this phase exists.

The milestone stays open through implementation, review, and manual testing — a small issue discovered
there that genuinely belongs to the milestone's scope can legitimately be added to it while it's still
open, without that being read as the milestone failing to converge. When a milestone carries a
description (`my-feature-planning`'s optional milestone-description rule), that description is the
contract this skill checks a manual-testing finding's scope against — it doesn't get reinterpreted
here.

Closing the milestone is a validated GitHub mutation like every other one in this skill: explicit
human approval first, then a re-fetch that confirms `state: closed` — never trust the closure
command's exit code alone. See `rules/milestone-completion.md`.

## Boundaries, dependencies, and composition

**Does NOT own:**
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

**Composition.** This skill composes with whatever implementation, testing, and tooling skills match
the consuming project's actual stack, loaded alongside it — it owns the workflow machinery, never the
code, tests, or framework conventions themselves.

**External dependency.** This skill assumes a GitHub-issue-tracked project reachable via the `gh`
CLI, since that's the concrete mechanism its own rules — issue closure, release publishing, milestone
closure — are written against. A project on a different issue tracker or hosting platform still
applies the same review gates, commit-boundary reasoning, and mutation-validation discipline,
translated to that platform's own equivalent commands.

**Relationship to `my-feature-planning`:**

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
closes a milestone itself; its responsibility ends at defining one and its issue set. This skill trusts
`my-feature-planning` never to hand it an issue that hasn't actually been approved, and trusts the
implementation skills to own the code itself — it owns how that finished work moves into history,
through a published release, to the milestone's own eventual closure.

## Origin and observed evidence

The methodology above is reusable as stated and doesn't require any of what follows to be understood.
This section exists for a different reason: it records the real, completed pass through this workflow
the methodology was extracted from, so the *why* behind a rule is traceable for anyone curious, and so
the concrete project history stays on the record rather than getting lost.

### Semantic commit boundaries — the evidence

The implementation-through-closure loop was extracted from four issues in one real milestone (Phase
22 — Authentication & 2FA), all on one branch:

| Issue | What it was | Commits |
|---|---|---|
| #288 | Provision a new organization + first Owner via an Artisan command | 1 |
| #287 | Remove public registration (21 files, one decision) | 1 |
| #120 | 2FA backend — persistence, then HTTP wiring, then activation | 3 |
| #289 | Org-level 2FA requirement — persistence, policy, settings page, enforcement | 4 |

Two of those were one clean commit each, even though #287 touched 21 files across 11 route files
plus app code, a migration, and tests. Two needed several commits, ordered by real dependency and, in
#120's case, by which commit a feature-flag flip could safely follow without retroactively breaking an
earlier one. Nothing about file count, issue size, or "how many things changed" predicted which shape
a given issue would take — only looking at the actual diff did. One additional commit in this same
evidence — a content-backlog update with no tracked issue behind it — confirms the "omit the trailer
when untracked" case actually occurred, not just theorized. See `rules/commit-boundaries.md` for the
full detail, including the exact mechanics used to safely rebuild #120 from one commit into three
after the fact.

### Verification and commit ordering — the evidence

Both the isolation-verification technique (commit, stash the rest, verify in isolation, pop, repeat)
and the feature-flag-ordering rule were proven on real work: #120's after-the-fact rebase split and
#289's from-scratch multi-commit build were both verified commit-by-commit this way before being
reported done. The ordering rule came from a real near-miss while sequencing #120's commits: enabling
Fortify's 2FA feature flag would have retroactively un-skipped three pre-existing tests in
`SecurityTest.php` — a file the issue never touched — whose assertions depended on a
`SecurityController` change that was still a separate, not-yet-landed commit. Caught and fixed by
reordering before it ever landed red. See `rules/verification.md` for the full mechanics, including
this project's specific Pest/Pint/Fortify tooling, kept explicitly separate there from the portable
technique itself.

### Release — the evidence

The release phase was extracted from one real end-to-end run: PR #298, bundling all four issues
above, merged to `main`, then shipped as `v0.17.0 — Authentication & 2FA` — a lightweight tag on the
merge commit plus a published GitHub Release, this project's own discovered mechanism, found by
inspecting 21 prior releases rather than assumed. The draft-versus-approved gap on `v0.17.0` is the
concrete evidence for "release-level altitude": the first pass grouped outcomes correctly but still
led with implementation language (Fortify TOTP, an Artisan command named directly, middleware); the
approved version described the same five areas as what a member or Owner actually experiences, with
three runtime fixes summarized as outcomes under Bug Fixes rather than re-explained as internals. See
`rules/release.md`.

### Milestone completion — the evidence, and the one deliberate exception

Unlike the rest of this skill, the milestone-completion phase was **not** extracted from observed
practice. The evidence available at the time showed the opposite of this rule: every milestone in the
originating project's full history had been left open, including several where every issue inside was
already closed. That's evidence of past behavior under a different, unstated set of assumptions — not
a convention this rule preserves. It was added because the human made an explicit forward-looking
decision that milestones should have a real completion lifecycle, tied to release validation rather
than issue count. Worth keeping distinct from the rest of this skill's history: everything else here
was pulled from what already happened; this phase was decided, not discovered. See
`rules/milestone-completion.md`'s "Forward-looking only."

### Branch evidence

The whole implementation-through-closure loop above ran on a single branch,
`feature/organization-owner-provisioning`, that ended up carrying all four issues' worth of work — one
data point about how that milestone happened to be worked, not a repeatable convention this project
documents anywhere else. See "Known v0.1 limitations" below for what that does and doesn't license
this skill to assume about branching.

## Known v0.1 limitations

Not designed yet, because no real evidence exists to extract from:

- PR creation and description conventions
- merge strategy (merge commit vs. squash vs. rebase-and-merge)
- deployment triggers
- a branch-naming convention beyond the one data point above — don't generalize "one branch per
  issue," "one branch per milestone," or any other scheme from it; ask, or take whatever branch is
  already checked out, until there's real evidence of a repeated convention to extract

The same method that built this skill — watch what actually happens, extract the rule the evidence
actually supports, say so explicitly when the evidence isn't there yet — is how each of those should
get added later, once there's a real PR-creation pattern or a real merge-strategy choice to learn
from. The release mechanism itself should keep growing the same way: what's recorded in
`rules/release.md` is this project's discovered evidence, not baked into the portable methodology — a
project with different evidence gets a different mechanism, discovered the same way.
