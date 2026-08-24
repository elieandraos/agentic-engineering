# my-git-workflow

## What this skill is

This is the delivery stage of the Agentic Engineering pipeline. It starts from approved work
produced by `my-feature-planning` and owns the Git/GitHub workflow from implementation through
verified delivery and the related release/milestone lifecycle.

It picks up one already-approved work item at a time, establishes which branch that work happens on,
implements only its scope, stops for human review, turns the finished diff into a small number of
coherent commits (also reviewed before they're written), verifies at the right scope, optionally
closes the item, and reports what's unblocked next. Separately, once every issue in a milestone is
closed, it checks whether that milestone's shared branch is actually ready for a PR. Separately
again, once a PR carrying that work has merged and the human authorizes proceeding, it discovers the
project's real release policy, classifies the release, drafts outcome-level notes, stops for
approval, publishes, and validates the result. Separately again, once that release is validated, it
checks whether the milestone the work belonged to is actually ready to close.

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

- Picking up one dependency-ready approved issue at a time, and establishing which branch its work
  happens on (a Backlog/hotfix issue's trunk branch, or a milestone's shared branch).
- The implementation review gate and the commit-plan review gate.
- Proposing and building semantic commit boundaries from the actual diff.
- Verification scope (narrowest reliable scope per commit vs. full-suite vs. isolation-proving a
  split), the regression-baseline treatment of pre-existing lint/format/static debt, and commit
  ordering around feature-activation risk.
- The issue-closure recipe and its post-mutation validation — intentionally before the milestone's
  PR merges.
- Recalculating and reporting the milestone's dependency-ready set.
- Once that set is empty: the milestone's PR-readiness gate.
- Once a PR merges and the human authorizes proceeding: release-policy discovery, classification,
  outcome-level drafting, the release approval gate, publishing, and post-publication validation.
- After release validation passes: the milestone-completion gate, the Backlog exemption, and the
  closure mutation itself (see "Release and milestone-completion lifecycle" below for the gate).

What it does *not* own is in "Composition and boundaries" below.

## Working lifecycle

There are two distinct paths, chosen by which kind of milestone the issue belongs to (a persistent
Backlog/catch-all vs. a delivery/phase milestone — `my-feature-planning`'s existing distinction):

```
choose a dependency-ready, approved issue
  → BRANCH READINESS
      Backlog/hotfix issue  → work on whatever's checked out, normally main; no branch decision
      Milestone issue       → inspect current branch; if wrong, recommend a branch derived from the
                               milestone's nature and ask before creating/switching; every issue in
                               that milestone shares this one branch
  → implement only its scope → verify (full-project scope)
  → STOP — human reviews the implementation
  → (approved) inspect the finished diff → propose a semantic commit plan
  → STOP — human reviews the commit plan
  → (approved) build the commits, narrowest-reliable verification per commit
  → full regression suite once, at the completed-issue boundary
  → ask: close the issue?
  → (if yes) check Tasks, closing comment, close, post-mutation validation
      (this closure intentionally precedes the milestone's PR merging — see below)
  → recalculate the milestone's dependency-ready set, report it, recommend — human chooses next
      (unless the set just went to zero — see "Milestone PR readiness" below)
```

A Backlog/hotfix issue normally ends here, with no PR. A milestone issue's commits stay on the shared
branch until the milestone itself is PR-ready.

**Branch readiness** is read from which kind of milestone the issue belongs to — a persistent
Backlog/catch-all or a delivery/phase milestone, `my-feature-planning`'s existing distinction, not
redefined here. Backlog/hotfix work makes no branch decision at all. Milestone work shares one branch
across every issue in that milestone; if the wrong branch is checked out, recommend one derived from
the milestone's actual nature (never a rigid prefix taxonomy) and ask before creating or switching to
it. Full detail: `rules/sequencing.md`.

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
never proof by itself. This closure is intentionally before the milestone's PR merges — closure marks
implementation and verification as done, not that the commits reached the trunk branch. If a later
finding (e.g. milestone manual testing) concerns work an issue already closed, the default is a new
issue referencing the original, not reopening it. Full detail: `rules/issue-closure.md`.

**What's next:** after a validated closure, recompute the milestone's dependency-ready set before
doing anything else, summarize the graph, recommend when there's a clear case, and leave the final
choice to the human. Starting the next issue is its own new pass through this workflow, not a
continuation of the current one. When that recompute finds zero open issues left in the milestone,
report that instead and move to the milestone's PR-readiness gate. Full detail: `rules/sequencing.md`.

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

**Milestone PR readiness**, the first milestone-level gate, starts once `rules/sequencing.md`'s
recompute finds zero open issues left in the milestone — never earlier:

```
milestone's ready set goes to zero
  → confirm, freshly: every issue closed + human confirms final manual testing done
      + that testing found nothing further
  → testing found something → file it as Discovered work (my-feature-planning), attach to this
      still-open milestone, re-run this gate later — never silently reopen the closed issue
  → all three hold → report "PR-ready" (a report, not a mutation — PR creation stays human-owned)
```

Full detail: `rules/milestone-completion.md`.

**Publishing a release** is a separate phase from both the working lifecycle above and PR readiness
— it starts once a PR (which may bundle several issues) has actually merged, and runs once per
release, not once per issue:

```
PR merges → human confirms it merged (this confirmation is the integration gate — no independent
    re-verification of merge state)
  → STOP — authorization to begin the post-merge phase at all
  → (authorized) discover the project's actual release policy (explicit config, else established
      history)
  → determine the release's primary theme and meaningful outcomes — never from size
  → draft release notes at release-level altitude, grouped by area
  → STOP — human approves the version, tag target, title, and body
  → (approved) publish through the project's own discovered mechanism
  → re-fetch the tag and release, validate every field against what was approved
```

A Backlog/hotfix issue has no PR to merge, so this phase's trigger doesn't apply to it — what release
cadence, if any, covers hotfix work directly on the trunk branch isn't designed here; there's no
evidence yet to extract a rule from. Neither the version scheme nor the release mechanism is baked
into this skill — both are read from each project's own evidence every time. Full detail:
`rules/release.md`.

**Milestone completion** — the second, later milestone-level gate, distinct from PR readiness above —
starts once release validation has actually passed:

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
my-git-workflow       → branch readiness (trunk for Backlog/hotfix, shared branch for a milestone)
my-git-workflow       → implement / review / commits / review / verify / close  (per issue)
  → milestone's ready set empty → PR readiness (all closed + manual testing confirmed clean)
  → PR opened, reviewed, merged        (not owned by this skill; Backlog/hotfix has no PR at all)
my-git-workflow       → authorization to proceed, then release: discover policy / classify / draft
  / approve / publish / validate
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
- **A shared milestone branch, confirmed across multiple milestones.** What started as a single data
  point — one branch carrying a whole milestone's work — recurred across enough real milestones
  (naming patterns like `core/multitenancy`, `feat/agents`, `feat/documents`) to confirm as the actual
  convention, not just one milestone's happenstance: `rules/sequencing.md`'s "Branch readiness"
  section. The prefixes themselves are illustrative of "derived from the milestone's nature," not a
  taxonomy to enforce.
- **Backlog hotfixes bypass milestone planning and PR entirely.** A run of Backlog issues worked
  directly on the trunk branch, closed after ordinary implementation/review/verification, with no
  branch decision and no PR — confirming the second, lighter-weight path this skill's two-path
  working lifecycle now models explicitly.
- **Issues close before their milestone's PR merges — by design, not by accident.** Every issue in a
  real milestone closed individually, on the shared branch, well before that branch was ever proposed
  as a PR. A finding from later manual testing on that branch was filed as its own new issue
  referencing the one it was found near, rather than reopening the closed issue — the concrete
  evidence behind `rules/milestone-completion.md`'s "When manual testing finds something."

Where an identifier is needed above, treat it as a placeholder — issue `{xxx}`, PR `{xxx}`, milestone
`{name}`, release `{version}` — the point is the shape of the example, not the specific numbers it
was first observed with.

## Known limitations

Not designed yet, because no real evidence exists to extract from:

- PR creation and description conventions, PR review procedure, and merge strategy (merge commit vs.
  squash vs. rebase-and-merge) — PR creation/review/merge stays entirely human-owned; this skill picks
  up again once the human reports the outcome (a merge) or a manual-testing finding on the branch.
- Deployment triggers.
- What release cadence, if any, applies to Backlog/hotfix work committed directly to the trunk branch
  with no PR — `rules/release.md`'s trigger is the milestone-PR-merge path specifically.
- Whether dependency ordering and activation-safety ordering can actually conflict during commit
  construction — no real work has produced such a case yet, so no precedence rule is defined
  (`rules/verification.md`'s "Relationship to dependency ordering").
- What happens if a milestone's PR is later rejected or materially revised after some of its issues
  already closed — the issues would already be closed per the intentional pre-merge-closure design,
  and neither this skill nor `my-feature-planning` currently owns un-doing that.

The same method that built this skill — watch what actually happens, extract the rule the evidence
actually supports, say so explicitly when the evidence isn't there yet — is how each of those should
get added later. `rules/release.md`'s policy-discovery method should keep growing the same way: a
project with different evidence gets a different mechanism, discovered the same way, not assumed
from this one.
