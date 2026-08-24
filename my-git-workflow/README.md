# my-git-workflow

## What this skill is

This is the delivery stage of the Agentic Engineering pipeline. It starts from approved work
produced by `my-feature-planning` and owns the Git/GitHub workflow from implementation through
verified delivery and the related release/milestone lifecycle.

It picks up one already-approved work item at a time, implements only its scope, stops for human
review, turns the finished diff into a small number of coherent commits (also reviewed before
they're written), verifies at the right scope, optionally closes the item, and reports what's
unblocked next. Separately, once a PR carrying that work has merged, it discovers the project's real
release policy, classifies the release, drafts outcome-level notes, stops for approval, publishes,
and validates the result. Separately again, once that release is validated, it checks whether the
milestone the work belonged to is actually ready to close.

## Pipeline role

```
my-architecture-laboratory   → understand and reconstruct reality
my-feature-planning          → turn that understanding into approved work
my-git-workflow              → turn approved work into verified delivery      (this skill)
```

**Input:** one already-approved GitHub issue that `my-feature-planning` has drafted, reviewed, and
created. This skill never decides what work should exist and never starts earlier than an
already-approved item.

## What it owns

- Picking up one dependency-ready approved issue at a time.
- The implementation review gate and the commit-plan review gate.
- Proposing and building semantic commit boundaries from the actual diff.
- Verification scope (narrowest reliable scope per commit vs. full-suite vs. isolation-proving a
  split) and commit ordering around feature-activation risk.
- The issue-closure recipe and its post-mutation validation.
- Recalculating and reporting the milestone's dependency-ready set.
- After a PR merges: release-policy discovery, classification, outcome-level drafting, the release
  approval gate, publishing, and post-publication validation.
- After release validation passes: the milestone-completion gate, the Backlog exemption, and the
  closure mutation itself (see "Release and milestone-completion lifecycle" below for the gate).

What it does *not* own is in "Composition and boundaries" below.

## Working lifecycle

```
choose a dependency-ready, approved issue
  → implement only its scope → verify (full-project scope)
  → STOP — human reviews the implementation
  → (approved) inspect the finished diff → propose a semantic commit plan
  → STOP — human reviews the commit plan
  → (approved) build the commits, narrowest-reliable verification per commit
  → full regression suite once, at the completed-issue boundary
  → ask: close the issue?
  → (if yes) check Tasks, closing comment, close, post-mutation validation
  → recalculate the milestone's dependency-ready set, report it, recommend — human chooses next
```

Two review gates, not one — approving the implementation is not approving a commit structure; the
same diff can be split several defensible ways, and the human sees the split before it becomes
permanent history. Full detail: `rules/review-gates.md`.

**Semantic commit boundaries** are not a mechanical split by file or folder — a semantic commit is
one implementation decision describable in a single sentence of *why*, leaving a coherent,
non-broken state on its own. Tests travel with the step they prove. Review corrections found before
anything is committed land inside the commit they belong to, never a separate fixup commit. Every
commit implementing a tracked item carries a `Refs #N` trailer — never `Closes`/`Fixes`, since
closing stays a separate, human-approved step. Full detail: `rules/commit-boundaries.md`.

**Verification** uses the narrowest reliable scope per commit — across tests, formatting, linting,
and static analysis — plus one full regression run at the completed-issue boundary — not after every
commit. When a split needs real proof, there's a stronger technique:
commit, stash the rest, verify what's landed in isolation, pop, repeat. Watch for a feature-flag
activation retroactively un-skipping tests whose supporting code hasn't landed yet — reorder before
it lands red, not after. Full detail: `rules/verification.md`.

**Issue closure** is opt-in and always after the commits exist — ask first. If yes: check off
completed Tasks, add a closing comment (summary, verification numbers, commit SHAs), close it, then
re-fetch and confirm state, checkboxes, and comment actually landed — a `gh` command's exit code is
never proof by itself. Full detail: `rules/issue-closure.md`.

**What's next:** after a validated closure, recompute the milestone's dependency-ready set before
doing anything else, summarize the graph, recommend when there's a clear case, and leave the final
choice to the human. Starting the next issue is its own new pass through this workflow, not a
continuation of the current one. Full detail: `rules/sequencing.md`.

## Core principles

- **Issues describe outcomes; commits describe coherent, verified implementation steps.** Neither
  file count, issue size, nor "how many things changed" predicts a commit split — only the actual
  diff does.
- **Two review gates, not one, on the pre-merge side.** Approving the implementation is never
  approval of a commit structure.
- **Never trust a mutation's exit code.** Every GitHub mutation this skill performs — issue closure,
  release publication, milestone closure — is re-fetched and validated afterward.
- **Discover the project's own mechanism before assuming one.** Release policy and publish tooling
  are read from what the project actually has, never assumed from a template.
- **A stop is a report plus a question**, not a wall of options with no recommendation — investigate
  enough to have a position, state it, and let the human decide.

## Release and milestone-completion lifecycle

**Publishing a release** is a separate phase from the working lifecycle above — it starts once a PR
(which may bundle several issues) has actually merged, and runs once per release, not once per
issue:

```
PR merges
  → discover the project's actual release policy (explicit config, else established history)
  → determine the release's primary theme and meaningful outcomes — never from size
  → draft release notes at release-level altitude, grouped by area
  → STOP — human approves the version, tag target, title, and body
  → (approved) publish through the project's own discovered mechanism
  → re-fetch the tag and release, validate every field against what was approved
```

Neither the version scheme nor the release mechanism is baked into this skill — both are read from
each project's own evidence every time. Full detail: `rules/release.md`.

**Milestone completion**, a further phase, starts once release validation above has actually passed:

```
release validation passes
  → check the gate, freshly: delivery/phase milestone (never Backlog)
      + shipping release published-and-validated + zero open issues right now
  → any condition fails → stay open (an open issue blocks closure regardless of release state;
      a newly-discovered follow-up issue re-opens the question even after a clean release)
  → all three hold → STOP, human approves closing
  → (approved) close, then re-fetch and confirm state is actually `closed`
```

A delivery/phase milestone represents a bounded body of work intended to ship as a release — that's
about scope and intent, not naming syntax. It stays open through manual testing and any small,
legitimately-scoped follow-up issue discovered there; that's expected, not a process failure. This
is a forward-looking workflow decision rather than an extraction of past practice — see "Real
example of usage" below. Full detail: `rules/milestone-completion.md`.

## Composition and boundaries

**Does NOT own:**
- Deciding what issues should exist, or drafting/creating them; milestone/label creation or scoping.
- The application code, tests, or framework-specific conventions.
- Product/architecture decisions, any review/approval gate's outcome, or final sequencing among
  ready issues.
- How a PR gets created, reviewed, or merged, or any deployment automation.

Those belong to `my-feature-planning`, the stack-specific implementation skills, or the human.

**Composes with:**
- Git and GitHub as intentional core substrate for this methodology — not an abstraction to be
  swapped out.
- Whatever implementation, testing, and tooling skills match the consuming project's actual stack,
  loaded alongside it.
- The workflow machinery is what this skill owns — never the code, tests, or framework conventions.

**Relationship to `my-feature-planning`:** it defines, scopes, drafts, and creates approved work;
`my-git-workflow` implements, reviews, commits, verifies, closes, releases, and completes the
milestone.

```
my-feature-planning   → classify / scope / reconcile / draft / review / create issues + milestone
  → issue approved
my-git-workflow       → implement / review / commits / review / verify / close  (per issue)
  → PR opened, reviewed, merged        (not yet owned by this skill)
my-git-workflow       → release: discover policy / classify / draft / approve / publish / validate
my-git-workflow       → milestone completion check / closure (delivery/phase only, never Backlog)
```

## Real example of usage

The methodology above is reusable as stated and doesn't require any of what follows to be
understood. This section exists to show it isn't theoretical — it was extracted from a real,
completed pass through this workflow in the project where it was first built, generalized here so no
prior knowledge of that project is needed.

- **One issue, one commit, even at scale.** An issue that touched 21 files across a dozen route
  files, application code, a migration, and tests was still one coherent decision — and shipped as
  one commit. File count didn't predict the split; the diff did.
- **One issue, several dependency-ordered commits.** Another issue split cleanly into
  persistence → wiring → activation, each commit a real implementation decision building on the
  last.
- **Activation-ordering caught a near-miss.** While sequencing a multi-commit build, enabling a
  feature flag in the planned commit order would have retroactively un-skipped pre-existing tests
  whose assertions depended on a change still sitting in a later, not-yet-landed commit. Caught and
  fixed by reordering before it ever landed red — this is the concrete case behind
  `rules/verification.md`'s ordering rule.
- **Release mechanism, discovered, not assumed.** The release phase was extracted from one real
  merge-and-release run: a PR bundling several issues merged to the main branch, then shipped as
  release `{version}` — the project's own established mechanism (a tag plus a published release),
  found by inspecting its prior release history rather than assumed. The first draft of the notes
  led with implementation detail; the approved version described the same work at outcome altitude
  instead — the concrete evidence behind "release-level altitude."
- **Milestone completion is a deliberate, forward-looking exception.** Every milestone in that
  project's history had actually been left open, including ones where every issue inside was already
  closed — evidence of past practice, not a convention worth preserving. The completion lifecycle
  above (`rules/milestone-completion.md`) was added as an explicit forward-looking decision instead,
  tied to release validation rather than issue count. No existing milestone was retroactively closed
  because of it.
- **One branch carried a whole milestone's work.** That's one data point about how that milestone
  happened to be worked, not a repeatable convention — see "Known limitations" below.

Where an identifier is needed above, treat it as a placeholder — issue `{xxx}`, PR `{xxx}`, milestone
`{name}`, release `{version}` — the point is the shape of the example, not the specific numbers it
was first observed with.

## Known limitations

Not designed yet, because no real evidence exists to extract from:

- PR creation and description conventions.
- Merge strategy (merge commit vs. squash vs. rebase-and-merge).
- Deployment triggers.
- A branch-naming convention beyond the single data point above — don't generalize "one branch per
  issue," "one branch per milestone," or any other scheme from it; ask, or take whatever branch is
  already checked out, until there's real evidence of a repeated convention to extract.

The same method that built this skill — watch what actually happens, extract the rule the evidence
actually supports, say so explicitly when the evidence isn't there yet — is how each of those should
get added later. `rules/release.md`'s policy-discovery method should keep growing the same way: a
project with different evidence gets a different mechanism, discovered the same way, not assumed
from this one.
