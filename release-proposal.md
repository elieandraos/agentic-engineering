# Agentic Engineering v2.0.1 — Release Proposal

**Status: proposal only. Not approved. No tag, draft release, published release, PR, or deployment
has been created for it.** This document exists for Control Room review; publication is a separate,
later, explicitly authorized action.

## Proposed tag and title

Tag `v2.0.1`; release title **"Agentic Engineering v2.0.1."**

## Release candidate — exact target SHA

**`0b74e5c3ce57abb555f800f0a9e7edac26c36abe`**, resolved and confirmed as `origin/main`'s tip before
this proposal was written (`git fetch` then `git rev-parse HEAD` / `git rev-parse origin/main`, both
matching). This is the last commit that has passed Control Room review in this release's scope.

**This proposal document's own commit is deliberately not the release candidate.** Committing and
pushing `release-proposal.md` lands as a new commit after `0b74e5c`; the tag target named above stays
`0b74e5c` regardless — the proposal describes a release of the reviewed code that precedes it, not of
itself. Before publication, whoever runs `ship-it/rules/release.md`'s sequence must independently
re-fetch and confirm both this exact SHA and this exact release-note text against the human's
explicit approval, the same discipline `v2.0.0`'s own finalized proposal used.

## Why this remains a patch, not a minor or major release

No skill was added or removed — the same seven skills published at `v2.0.0`
(`document-it`, `implement-it`, `lab-it`, `laravel-inertia-stack`, `plan-it`, `review-it`, `ship-it`)
are the only seven skills in this release too. No skill's activation triggers, ownership boundaries
(`SKILL.md`'s "What it owns" / "What it does not own"), or entry contracts changed in substance —
only routing lists were updated to reflect where content now lives. Five new files were added
(`skills/implement-it/rules/{commit-reconstruction,isolation-verification,worktree-preservation}.md`;
`skills/ship-it/rules/{milestone-pr-readiness,ci-failure-correction}.md`), but each is a supporting
rule file inside an already-existing skill's own directory, not a new skill or a new consumer-facing
capability — every procedure they contain (unpublished-history reconstruction, isolation
verification, worktree preservation, PR readiness/creation, CI-failure investigation) already existed
in `v2.0.0`, bundled into larger files. A project that refreshes its already-installed skills gets the
same skill names with corrected behavior and the new supporting files loading automatically per each
skill's own routing — no explicit "add these additional skill names" step, unlike `v2.0.0`, which
*was* a major release specifically because responsibility moved *between* skills
(`lab-it → document-it`, `ship-it → implement-it`) and required exactly that step.

## Complete proposed release-note text

> ## Agentic Engineering v2.0.1
>
> A patch release: Git-mechanics correctness fixes in `implement-it`, an Artifact-template rendering
> fix in `document-it`, a frontmatter fix in `review-it`, internal reorganization of two skills'
> largest files into focused, single-purpose supporting files, and expanded documentation. No skill
> was added, removed, or renamed; no skill's activation, ownership, or entry contract changed.
>
> ### Fixed
>
> - **`implement-it`: unpublished-commit history reconstruction and worktree preservation.**
>   Reconstructing a commit's history to fold in a review correction could previously pull unrelated
>   staged work into the wrong commit, drop or overwrite an unrelated older Git stash, or fail to
>   reach the commit a correction actually belonged to when more than one commit separated it from
>   `HEAD`. The isolation-verification technique's own preservation step could similarly collapse a
>   file's staged/unstaged split during restoration. The reconstruction procedure now captures every
>   touched path's committed/staged/working content before mutating anything, isolates a correction
>   positively (never by subtracting a known piece from the combined content), verifies a split by
>   round-trip before trusting it, and stops — leaving the repository untouched — on any capture-time
>   or restoration-time ambiguity it can't safely resolve. Worktree preservation now tracks a stash
>   entry by its commit SHA rather than its position or message, so an older, unrelated stash is never
>   mistaken for the one this procedure created.
> - **`document-it`: Artifact-template syntax highlighting and mobile navigation.** The template's
>   syntax highlighter could corrupt rendered code containing a `//`-style URL (PHP/TypeScript) by
>   stranding internal placeholder characters in the output, and a data-lang value naming an inherited
>   JavaScript object property (e.g. `constructor`) would throw and abort highlighting for every
>   subsequent code block on the page. A PHP `#[...]` attribute inside a comment or string had the
>   same class of defect. All are fixed: comments, strings, and PHP attributes are now matched in one
>   pass so whichever construct starts first consumes to its own end, and an unsupported or malformed
>   language value now falls back to safe, escaped plain text instead of aborting. The mobile-width
>   navigation CSS cascade bug (a desktop rule silently overriding the intended mobile layout) is also
>   fixed.
> - **`review-it`: frontmatter description length.** Shortened from 1,219 to 966 characters, within
>   the Agent Skills specification's 1,024-character limit, with its purpose, discovery triggers, and
>   ownership boundary preserved.
>
> ### Changed (internal reorganization, same behavior)
>
> - `implement-it/rules/verification.md`'s isolation-verification technique and shared
>   worktree-preservation procedure, and `implement-it/rules/commit-boundaries.md`'s
>   unpublished-history reconstruction recipe, are now their own files
>   (`rules/isolation-verification.md`, `rules/worktree-preservation.md`,
>   `rules/commit-reconstruction.md`). Each still loads only when its own trigger condition actually
>   applies; the condition itself stays visible in the caller that hands off to it.
> - `ship-it/rules/milestone-completion.md`'s three conditional surfaces — PR readiness and
>   authorized creation, CI-failure investigation and correction handoff, and the closure gate — are
>   now split into `rules/milestone-pr-readiness.md`, `rules/ci-failure-correction.md`, and a narrowed
>   `rules/milestone-completion.md` that keeps closure and the shared delivery-lifecycle map.
>
> ### Added
>
> - `docs/skill-context.md`: dated, reproducible file-size measurements and modeled (not measured)
>   representative-workflow loading estimates for every skill, linked from each skill's own README.
> - Several principles added to `docs/skill-authoring-methodology.md`, distilled from this release's
>   own corrections: keeping a conditional procedure's trigger visible in its caller when extracting
>   the procedure's own mechanics elsewhere; distinguishing a file's freely consultable guidance from
>   its own gated mutation; validating a multi-step procedure as a complete sequence and its combined/
>   failure cases, not only each step in isolation; calibrating a confidence claim to the specific
>   evidence that actually backs it; checking a runtime reference against what an installed skill
>   actually ships, not only the source repository's own working tree; and validating frontmatter
>   constraints and labeling a size/context figure as measured, modeled, or observed.
>
> ### Install / update
>
> ```shell
> npx skills update <your already-installed skill names> -p -y
> ```
>
> No new skill names are introduced in this release, so a plain refresh of whatever skills your
> project already has installed is sufficient — unlike `v2.0.0`, this release needs no "add these
> additional names" step. A GitHub-source update tracks this repository's default branch at the
> moment the update command runs, not a pinned tag — running it well after this release publishes,
> once `main` has advanced further, will pick up whatever is on `main` at that later moment, not
> necessarily `v2.0.1` specifically. After updating, confirm your installed `implement-it` and
> `ship-it` copies actually include the new supporting files this release adds
> (`rules/commit-reconstruction.md`, `rules/isolation-verification.md`, `rules/worktree-preservation.md`
> under `implement-it`; `rules/milestone-pr-readiness.md`, `rules/ci-failure-correction.md` under
> `ship-it`) — a successful update command is not proof every new file actually landed; read the
> installed directory back to confirm it.
>
> ### Validation
>
> Source and routing review: full re-reads, repository-wide reference searches, `git diff --check`,
> and Markdown-link resolution across every changed file. Executed, disposable Git-repository
> experiments exercised the corrected reconstruction and worktree-preservation mechanics directly —
> real commands, real repositories created and discarded outside this project, results inspected via
> `git log`/`git show`/`git diff`/`git stash list`. The `document-it` template fixes were validated by
> executing the shipped highlighter script against a minimal DOM stub in Node and by source/cascade
> inspection for the mobile-navigation CSS fix. **No skill was invoked end to end as a live session,
> and no consuming project's installation, refresh, or pipeline run was performed.** Real-browser
> rendering of the Artifact template was not exercised — the highlighter fixes are confirmed by script
> execution, not a rendered page.
>
> ### Known deferred items (not in this release)
>
> - `laravel-inertia-stack` defects the original audit identified — customer-ID casting defeating
>   validation, accepted-ascending sort silently falling back to descending, incorrect nullable/
>   required field guidance, a factory/model naming mismatch, and a dynamic-handler/infrastructure-
>   method name collision — remain unfixed.
> - Consumption-tooling concerns the original audit identified — a selective install can omit a
>   required sibling skill; the lock file's integrity guarantee was overstated relative to what it
>   actually proves; `docs/skill-consumption.md`'s blanket "default branch, not a pinned ref" claim is
>   too broad for a source URL that already carries an explicit ref, which the installer actually
>   honors; and the same document's "always relative, portable symlinks" claim holds on POSIX but not
>   on Windows, where the installer uses absolute-target junctions instead — remain unaddressed;
>   `docs/skill-consumption.md` itself is unchanged in this release.
> - Two open gaps remain, both already known: no stated entry route for a standalone `review-it`
>   finding with no issue and no `ship-it` delivery-correction context; and `ship-it`'s release
>   recovery has no explicit missing-evidence branch when a historical release proposal can't be
>   recovered, unlike the equivalent PR-recovery path.
> - The `laravel-inertia-stack`/Laravel Boost precedence question and canonical issue-definition
>   durable storage remain deferred from `v2.0.0`, unchanged.

## Update guidance, verified against `docs/skill-consumption.md`

- §3/§13: installing or updating from a GitHub source needs no release, tag, or package publication
  to exist first — a consumer can already reach every fix in this proposal via a plain
  `npx skills add`/`update` against this repository's current default branch, independent of whether
  `v2.0.1` is ever tagged.
- §7: "a GitHub source tracks the source repository's default branch at install/update time, not a
  pinned ref" — this is the basis for the release-note text's own distinction above between running
  an update *now* (while `main`'s tip equals the proposed target SHA) versus running it *later* (once
  `main` has advanced past `v2.0.1`). This guidance uses only the ordinary, unqualified
  `owner/repo` source `docs/skill-consumption.md` itself documents, for which that statement holds;
  `scenarios.md`'s CONS-03 finding flags the statement as too broad for a source URL that already
  carries an explicit ref (which the installer actually honors), but that capability isn't documented
  in `docs/skill-consumption.md` and isn't asserted here — see "Known deferred items" above. A
  consumer who needs the exact tagged `v2.0.1` correspondence and wants to rely only on what this
  repository's own documentation currently states should confirm `main`'s tip against the `v2.0.1`
  tag's SHA before updating, rather than assuming the update command provides that guarantee.
- §9: "diff the update before committing it, and validate only the skills whose files actually
  changed" — for this release, that's `document-it`, `implement-it`, `plan-it` (reference-only),
  `review-it`, and `ship-it`; `lab-it` and `laravel-inertia-stack` have no behavioral change in this
  range (only a documentation-only "Context consumption" README addition, already covered by an
  earlier, already-approved pass — see "Reconciliation" below).
- §14: stack companions install selectively and independently of the portable-methodology skills;
  this release doesn't change that, and doesn't touch `laravel-inertia-stack`'s own rule content.
- The five new supporting files (see "Install / update" above) are not a new install target — they
  live inside `implement-it`'s and `ship-it`'s own directories and refresh automatically with those
  skills. Confirming they actually landed after an update is the same "verify by reading state back"
  discipline this document's own §9 already asks for, applied to file presence rather than content
  correctness.

## Reconciliation against v2.0.0 → this target's full diff and commit history

31 commits, 33 files changed (3,489 insertions, 2,452 deletions) since `v2.0.0`
(`366bda106a8d51699483768e15fe1dcff4e6a80e`). Grouped by what actually changed, matching the release
note above:

0. **Housekeeping, no functional change** (`581cd6e`, `e6e6c5d`, `86107d1`, `3cb1a0a`, `07bb5bf`) —
   `roadmap.md` next-step and future-direction updates, and removal of the completed `v2.0.0`
   migration plan (`plan.md`, 2,067 lines) from the active repository once it shipped, with the one
   surviving reference to it repointed to the plan preserved at the `v2.0.0` tag on GitHub. Accounts
   for the largest deletion in the diff stat; no skill file changed.
1. **The audit that grounds this release** (`5372afa`) — recorded `scenarios.md`'s original 47-record
   audit (27 aligned, 18 defect, 2 gaps) against the post-`v2.0.0` state, the evidence base every fix
   below traces back to.
2. **`implement-it` reconstruction/preservation repairs** (pre-session-start commits `d6220f0`,
   `caad9d3`, `8ff0bd8`, `a0a5d2b`, `0087a07`, all reviewed and approved before this proposal's
   preparation began) — the fixes summarized in the release note's "Fixed" section, recorded in full
   in `scenarios.md`'s four IMP-05–08 follow-up sections (2026-09-09 through 2026-09-09d).
3. **`document-it` template repairs** (`23ea271`, `39b8235`) — the highlighter/mobile-nav fixes,
   recorded in `scenarios.md`'s two template follow-up sections (2026-09-09e, 2026-09-09f).
4. **`review-it` metadata correction** (`7da2b33`, `cd2f3f5`) — the description-length fix and its
   `scenarios.md` evidence record (2026-09-09g).
5. **Metadata/dossier/context pass** (`43e465c`, `746619b`, `c15f8ec`, `b92fa5c`, `667fab1`,
   `3269c8f`) — created `docs/skill-context.md`; reconciled `implement-it`'s and `document-it`'s
   dossiers against the approved fixes above; corrected the context document's own units, arithmetic,
   and claims across several review rounds, with `scenarios.md`'s 2026-09-09h record covering the
   first of those correction rounds.
6. **`implement-it` conditional-procedure extractions** (`9b77d00`, `a85c956`, `eb64ec9`, `27486d8`,
   `7b0dcea`) — `rules/commit-reconstruction.md`, then `rules/isolation-verification.md` and
   `rules/worktree-preservation.md`, extracted from `rules/commit-boundaries.md` and
   `rules/verification.md` respectively, with behavior preserved and verified by line-by-line diff
   against the pre-extraction source.
7. **`ship-it` conditional-procedure extraction** (`a432509`, `f2c5054`, `8075375`) —
   `rules/milestone-pr-readiness.md` and `rules/ci-failure-correction.md` extracted from
   `rules/milestone-completion.md`, same behavior-preservation standard, plus a correction pass
   fixing two routing/measurement overclaims the extraction's own documentation had introduced.
8. **Authoring-lessons retention and final wording passes** (`094db53`, `0b74e5c`) — the
   `docs/skill-authoring-methodology.md` additions and `docs/skill-context.md`/README wording
   corrections listed in the release note's "Added" section.

Every commit in this range individually passed Control Room review before the next began — this
proposal introduces no new, unreviewed runtime change of its own.

## Validation performed for this proposal (accurate, not end-to-end)

Full re-read of the complete `v2.0.0..HEAD` diff and commit log; cross-checked every "Fixed"/
"Changed"/"Added" claim above against `scenarios.md`'s own follow-up records and the current file
content, not against memory of an earlier pass. Confirmed via direct git-history inspection that
`v2.0.0` is a clean ancestor of the proposed target SHA (`git merge-base --is-ancestor`) and that this
repository has never merged a pull request (`gh pr list --state all` against
`elieandraos/agentic-engineering` returns none, in any state) — the same established direct-to-`main`
publication precedent `v2.0.0` and `v1.0.0` both used. **No skill was invoked end to end, and no
consuming project's installation, refresh, or pipeline run was performed as part of preparing this
proposal.**

## Concrete gap found while checking summaries against these notes (reported, not silently repaired)

`artifacts/ship-it.md` §8's confidence section states "no skill in this ecosystem has been invoked
end to end since `implement-it` and `review-it` were extracted from what this skill used to be" —
correct as a general claim, but it names only that earlier, pre-`v2.0.0` split. It does not
explicitly name the newer `milestone-completion.md` three-way split this release also makes (§7's
rule-ownership table was updated for that split; §8's confidence prose was not). The underlying fact
this sentence states — no live consumer run has exercised any of this skill's file splits — still
covers the newer split correctly by implication, so this is not a contradiction with the release note
above, which already states the same "no live skill execution" limitation independent of which split
it applies to. It is a completeness gap in that dossier's own wording, left for a future documentation
pass rather than fixed here, since this task's scope is the release proposal and a minimal roadmap
note, not further dossier edits.

No other contradiction was found between this proposal's claims and the current dossier/`scenarios.md`
text.

---

**This proposal does not authorize publication.** Tagging, drafting or publishing a GitHub Release,
opening a PR, deploying, or mutating any consuming project remain separate, later, explicitly
authorized actions.
