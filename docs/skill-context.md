# Skill Context Consumption

Dated file-size measurements for this repository's skills, and modeled estimates — built from those
measurements, under explicit assumptions stated where they're used — of what a representative
workflow would load and what it does not load merely because a skill is installed. The file sizes
are direct measurements; the workflow-level figures are arithmetic over named files, not an observed
session's actual consumption. This document is the single, ongoing home for these numbers — later
passes append a new dated section rather than silently overwriting this one's figures.

**Authority boundary.** This document measures and models context cost; it does not change any
skill's operational rules, gates, or approvals. Where a reduction is proposed below, the proposal is
inert until a separate authoring pass implements it under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md).

**Revision note (2026-09-09b).** This revised the first 2026-09-09 version of this same document,
which mixed two different units (byte counts from `wc -c` presented alongside Unicode-character
description limits), listed workflow-file orders that didn't match the owning skill's actual
lifecycle, and stated some conditional dependencies as absolute ("never loaded together," "never
pulls in") without checking every owning rule file first.

**Revision note (2026-09-09c).** This further corrects the 2026-09-09b version: it pins measurement
to a single explicit commit (`667fab15`, not the prior version's ambiguous "built on top of
`cd2f3f5`" framing); removes an internal contradiction where `implement-it`'s own table claimed
`rules/verification.md` was "the single largest supporting file among the six portable skills" while
`ship-it`'s table separately, and correctly, named `rules/milestone-completion.md` as the largest
file overall; removes an unsupported "two orders of magnitude below any workflow" claim (the
smallest modeled workflow is well under one order of magnitude above discovery metadata) and an
unsupported "no real workflow loads this whole figure" guarantee; corrects the reconstruction-recipe
character range in "Concrete reduction opportunities" (it previously included the file's general
Do/Don't summary and excluded the common no-reconstruction "nothing committed yet" case); qualifies
the README/SKILL.md duplication finding and the reduction proposals' savings language as estimates,
not established facts or measured benefits; and adds the `plan-it` secondary-checklist,
`laravel-inertia-stack` testing/`php-conventions.md`, `artifact-design`, and `implement-it`
entry-contract details the workflow estimates previously omitted. Each version's numbers replace,
rather than supplement, the version before it.

## Measurement date and source

Measured 2026-09-09, against the `skills/` tree at commit
[`667fab1555d33fec8031a27aa85296f7103d4159`](https://github.com/elieandraos/agentic-engineering/commit/667fab1555d33fec8031a27aa85296f7103d4159)
on `main`. Every figure below describes that pinned revision specifically, not a later working tree —
this correction pass's own edits to this file land as an ordinary new commit after it, and do not
themselves change any file the figures describe. Skill file sizes change as skills evolve; treat
every number below as true of `667fab15` and nothing later — re-run "Reproducing these numbers"
below against whatever revision you actually want to describe to refresh them. This supersedes, for
directory-wide and workflow-level figures, the narrower SKILL.md-only table in `scenarios.md`'s
"Entry-point size observations" (2026-09-08); that table's own pinned-commit figures are unchanged
and preserved there as a historical record, not restated here as current.

## Method

**Unit: Unicode characters, not bytes.** Every count in this document is the number of Unicode
characters in a file — `len()` on the file's content after UTF-8 decoding — the same unit the Agent
Skills specification's 1,024-character `description` limit uses. This repository's prose makes heavy
use of multi-byte UTF-8 punctuation (em dashes "—", curly quotes and apostrophes), so a raw byte
count (`wc -c`) measures something different and consistently larger: for example,
`skills/document-it/SKILL.md` is 13,742 characters but 13,844 bytes, a 102-byte difference from
multi-byte punctuation alone, and every file in this repository shows the same pattern to varying
degrees. **Do not mix the two figures in one comparison.** Where "Reproducing these numbers" below
shows a `wc -c` command for convenience, its output is bytes, not the character count this document
otherwise reports, and is only safe to use as a rough proxy once you've confirmed the file's
non-ASCII density is similar.

**Rough tokens = characters ÷ 4, always.** This is a coarse approximation, not a Claude tokenizer
count and not an observed session's actual token usage — actual tokenization varies with content
(code, prose, punctuation density) and no session-usage figure is claimed anywhere in this document.
Every "rough tokens" figure below is this same division of the character count, rounded to the
nearest whole number, stated so the arithmetic is checkable, not a measured or modeled tokenizer
output.

## Three loading tiers

Installing a skill does not load its whole directory. What actually enters context happens in three
distinct tiers, at three different times:

1. **Discovery metadata** — each installed skill's frontmatter `description` (and `name`), read by
   the agent to decide which skill, if any, applies to the current request. This is the only part of
   an *inactive* skill that costs anything. It loads for every installed skill, not only the one that
   ends up activating.
2. **Activated `SKILL.md`** — once a skill is selected, its complete `SKILL.md` (frontmatter plus
   body) loads. This is the operational routing entrypoint: activation vocabulary, ownership, and
   the routing table to supporting files. Two of the seven `SKILL.md` files — `plan-it` and
   `laravel-inertia-stack` — additionally point a reader to that skill's own `README.md` in their
   opening text ("See `README.md` for the plain-English walkthrough and reasoning," and similarly for
   `laravel-inertia-stack`); whether an executing agent actually follows that pointer in a given
   session is session-dependent and is not asserted as a fixed cost anywhere below.
3. **Supporting files, on demand** — a `rules/`, `blueprints/`, or `templates/` file loads only when
   the activated `SKILL.md`'s own routing, or a supporting file's own further routing, sends the
   current workflow to it. A skill with nine rule files (`plan-it`) does not load all nine for every
   request; it loads the ones the request's own shape requires — though, as "Estimated file-loading
   costs" below details, "the ones a shape requires" is not always a single file per concern: a
   mixed-characteristic `plan-it` feature or a `laravel-inertia-stack` blueprint with its own internal
   routing can require more than the primary table entry alone. This document assumes whole-file
   reads throughout: once a workflow needs a file, its complete size is counted as the cost,
   regardless of how much of it the current path actually exercises. A tool capable of a partial or
   offset-limited read could load less than that in a real session; this document does not model
   that possibility, and states it as an explicit assumption rather than a guaranteed mechanism.

## Discovery metadata

Sum of all seven `SKILL.md` frontmatter `description` fields — the cost paid once per session,
before any of these skills has actually activated, regardless of which one (if any) ends up
running:

| Skill | Description characters |
| --- | ---: |
| document-it | 553 |
| implement-it | 839 |
| lab-it | 641 |
| laravel-inertia-stack | 373 |
| plan-it | 716 |
| review-it | 966 |
| ship-it | 923 |
| **Total** | **5,011** |

Rough tokens: ~1,253. This is the combined length of the seven `description` fields alone, measured
the same way as every other figure in this document — it is not a full accounting of installation or
session overhead, since a harness may add its own formatting, wrapper text, or additional metadata
around each description that this document does not measure.

## Activated SKILL.md sizes

| Skill | SKILL.md characters | Rough tokens |
| --- | ---: | ---: |
| document-it | 13,742 | 3,436 |
| implement-it | 10,042 | 2,511 |
| lab-it | 7,497 | 1,874 |
| laravel-inertia-stack | 4,164 | 1,041 |
| plan-it | 6,542 | 1,636 |
| review-it | 6,052 | 1,513 |
| ship-it | 5,919 | 1,480 |
| **Total (all seven, if all were activated)** | **53,958** | **13,490** |

review-it's SKILL.md carries 966 characters of frontmatter description (shortened from 1,219 in a
prior pass; see "Metadata correction" below) — its body is otherwise unchanged from the other six
skills' typical shape.

## Supporting rule, blueprint, and template sizes

Every supporting file under each skill's `rules/`, `blueprints/`, and `templates/` directories,
largest first per skill. `README.md` is listed separately with a note on whether that skill's own
`SKILL.md` references it (see "Three loading tiers" above); a skill whose `SKILL.md` does not
mention `README.md` treats it as pure human-facing orientation the agent has no stated reason to open
mid-workflow.

### document-it

| File | Characters |
| --- | ---: |
| `rules/template.html` | 20,913 |
| `rules/review.md` | 13,001 |
| `rules/maintenance.md` | 8,903 |
| `rules/doc-style.md` | 7,645 |
| `README.md` (not referenced from `SKILL.md`) | 2,785 |

### implement-it

| File | Characters |
| --- | ---: |
| `rules/verification.md` | 35,260 |
| `rules/commit-boundaries.md` | 23,510 |
| `rules/issue-closure.md` | 14,243 |
| `rules/review-gates.md` | 13,015 |
| `rules/sequencing.md` | 8,862 |
| `README.md` (not referenced from `SKILL.md`) | 3,156 |

`rules/verification.md` and `rules/commit-boundaries.md` are the two largest supporting files within
`implement-it` itself — both are flagged in "Concrete reduction opportunities" below. Neither is the
largest file in the repository overall: `ship-it/rules/milestone-completion.md` (38,499 characters,
see below) is larger than both.

### lab-it

| File | Characters |
| --- | ---: |
| `rules/plan-synthesis.md` | 12,789 |
| `README.md` (not referenced from `SKILL.md`) | 2,407 |

lab-it's only supporting file loads exclusively for the "Plan feature architecture" workflow, per
`SKILL.md`'s own routing statement ("loaded only when 'Plan feature architecture' needs it") — a
plain investigation-and-answer request does not reach it.

### laravel-inertia-stack

| File | Characters |
| --- | ---: |
| `blueprints/resource-controller.md` | 9,819 |
| `rules/actions.md` | 8,676 |
| `blueprints/pest-testing.md` | 7,201 |
| `blueprints/filters-and-sorting.md` | 6,743 |
| `rules/test-ownership.md` | 4,364 |
| `rules/factories-and-seeders.md` | 3,960 |
| `rules/authorization.md` | 3,681 |
| `rules/resources.md` | 3,617 |
| `templates/.../TestingServiceProvider.php` | 3,113 |
| `rules/request-normalization.md` | 2,761 |
| `templates/.../QuerySorter.php` | 1,550 |
| `rules/migrations.md` | 1,556 |
| `rules/enum-options.md` | 1,508 |
| `templates/.../QueryFilter.php` | 1,270 |
| `rules/php-conventions.md` | 1,239 |
| `rules/eloquent-attributes.md` | 1,210 |
| `rules/query-conditionals.md` | 1,100 |
| `templates/.../Filterable.php` | 999 |
| `templates/.../Sortable.php` | 985 |
| `README.md` (referenced from `SKILL.md`'s routing note) | 2,646 |

This skill's own `SKILL.md` carries an explicit routing table naming the primary file(s) a task
needs, but that table is not the end of the routing: `blueprints/filters-and-sorting.md`'s own
"Testing" section additionally routes to `rules/test-ownership.md` and `blueprints/pest-testing.md`
for how filter/sorter classes are tested — a task landing on that blueprint reaches more than the
table's own row names (see the composed workflow row below).

### plan-it

| File | Characters |
| --- | ---: |
| `rules/issue-conventions.md` | 19,801 |
| `rules/review.md` | 16,800 |
| `rules/discovered-work.md` | 10,783 |
| `rules/sequencing.md` | 10,509 |
| `rules/resource-feature-checklist.md` | 9,796 |
| `rules/design-reconciliation.md` | 6,514 |
| `rules/plan-md-input.md` | 6,504 |
| `rules/capability-checklist.md` | 4,930 |
| `rules/feature-classification.md` | 3,171 |
| `README.md` (referenced from `SKILL.md`'s opening text) | 2,607 |

`rules/resource-feature-checklist.md` and `rules/capability-checklist.md` are chosen primarily by
`rules/feature-classification.md`'s shape classification, but that same file states that "for mixed
characteristics, classify by the primary organizing responsibility and apply secondary checklist
questions only where the actual scope warrants it" — so a mixed-shape feature can load both
checklists, not only the primary one. `rules/plan-md-input.md` and `rules/discovered-work.md` remain
alternate entry routes for the same request, depending on the work's origin.

### review-it

| File | Characters |
| --- | ---: |
| `rules/checklist.md` | 9,235 |
| `rules/scope.md` | 9,064 |
| `rules/verification.md` | 8,686 |
| `README.md` (not referenced from `SKILL.md`) | 3,081 |

All three rule files are consulted on essentially every invocation, in the order `SKILL.md`'s own
"Rules" list states — `scope.md` first ("consult first, at the start of every invocation"), then
`checklist.md`, then `verification.md` — review-it has no large conditional file a typical review
skips.

### ship-it

| File | Characters |
| --- | ---: |
| `rules/milestone-completion.md` | 38,499 |
| `rules/release.md` | 17,050 |
| `README.md` (not referenced from `SKILL.md`) | 2,386 |

`rules/milestone-completion.md` is the largest single file in the entire skill set, and covers three
distinct surfaces in one file — PR readiness, CI-failure investigation, and the closure gate (see
"Concrete reduction opportunities" below). `milestone-completion.md` and `release.md` cross-reference
each other extensively around their shared post-merge authorization trigger, but each still governs
its own phase — a pre-merge PR-readiness check does not need `release.md` at all.

### Repository-wide total

All 57 files under `skills/`: **467,861 characters** (470,648 bytes — the 2,787-byte gap is the same
multi-byte-punctuation effect described in "Method" above, accumulated across every file). Rough
tokens: **~116,965**. This is the sum across all seven skills' entrypoints, rules, blueprints,
templates, and READMEs — every file this document measures, whether or not any single workflow
would ever open all of them together. It is presented as an upper-bound reference point for scale,
not a claim about what any specific workflow actually loads; every modeled workflow estimate below
is a small fraction of it, but this document does not assert that no session ever approaches the
full figure.

## Estimated file-loading costs for representative workflows

**These are modeled unique-file text-volume estimates, not measured session consumption.** Each row
sums the character counts of the files a workflow of that shape would need to open, in the order it
would first reach them, under three explicit assumptions this document makes rather than something
any runtime guarantees: **whole-file reads** (a file that gets opened contributes its complete size,
never a partial section); **deduplication within one pass** (a file already opened earlier in the
same pass is not counted again if the workflow returns to it); and **README exclusion by default**
(justified below). No instrumentation of an actual agent session backs these numbers — they are
arithmetic over the files named, not an observed token count from a real run, and an actual session
could differ (a model re-reading a file, a human interrupting mid-workflow, a path this document
didn't model).

**Excluded from every estimate**, per this task's own scope: application/project code the workflow
reads or writes, prior conversation history, tool-call output (command results, diffs, search
results), and any external companion skill this repository does not publish — Laravel Boost's
`laravel-best-practices`, `testing-best-practices`, and `inertia-vue-development` (real cost when
installed, but not measurable from this repository), and the `artifact-design` skill that
`document-it/SKILL.md` requires loading before writing any Artifact page (same caveat: real cost,
external to this repository, not measured here). `README.md` files are excluded by default: five
of the seven skills' `SKILL.md` files never mention `README.md`, so an executing agent has no stated
reason to open it. The two exceptions — `plan-it` and `laravel-inertia-stack`, whose `SKILL.md` text
each point a reader to `README.md` — are called out in their rows below rather than silently folded
into the totals, since whether an executing agent actually follows a prose pointer like that, versus
a human maintainer reading the same file, is not something this document can assert either way.
`docs/skill-authoring-methodology.md` and `docs/skill-consumption.md` are also excluded — they serve
a skill's author or a project's installer, not a running pipeline workflow, and no `SKILL.md` or rule
file in this repository references either one.

**A separate assumption for `implement-it`'s two rows below:** `implement-it/SKILL.md`'s "Entry
contract" names `plan-it/rules/issue-conventions.md` and `plan-it/rules/review.md` by name, to
describe the quality bar an issue must already meet before `implement-it` accepts it. Nothing in
that text instructs `implement-it` to re-open those files itself — the ordinary path trusts that an
already-approved issue meets the bar, rather than re-verifying it against `plan-it`'s own rules each
time. This document assumes that ordinary path and does not count either `plan-it` file in the
`implement-it` rows below; a session that did re-open them for some other reason (an explicit
re-verification, a dispute about whether an issue actually qualifies) would add
`plan-it/rules/issue-conventions.md` (19,801 characters) and/or `rules/review.md` (16,800
characters) on top of the totals shown.

| Workflow | Files counted (in order) | Characters | Rough tokens |
| --- | --- | ---: | ---: |
| **review-it, standalone review** | `SKILL.md` (6,052) → `rules/scope.md` (9,064) → `rules/checklist.md` (9,235) → `rules/verification.md` (8,686) | 33,037 | 8,259 |
| **lab-it, investigation-and-answer only** | `SKILL.md` (7,497) — `rules/plan-synthesis.md` not reached; no `plan.md` was requested | 7,497 | 1,874 |
| **lab-it, plan feature architecture** | `SKILL.md` (7,497) → `rules/plan-synthesis.md` (12,789) | 20,286 | 5,072 |
| **document-it, new Markdown guide from already-sufficient evidence** | `SKILL.md` (13,742) → `rules/doc-style.md` (7,645) → `rules/review.md` (13,001); `lab-it` not routed to (evidence already sufficient) | 34,388 | 8,597 |
| **document-it, new Artifact guide** | same as above, plus `rules/template.html` (20,913); the external `artifact-design` skill this requires is not counted (excluded above) | 55,301 | 13,825 |
| **document-it, reconcile an existing Markdown guide for a connected architectural change, evidence routed through `lab-it` for staleness (cross-skill)** | `SKILL.md` (13,742) → `lab-it/SKILL.md` (7,497, cross-skill) → `rules/maintenance.md` (8,903) → `rules/doc-style.md` (7,645, since `rules/maintenance.md` routes there for how a connected change gets written) → `rules/review.md` (13,001); `rules/template.html` is not reached because this is a Markdown, not an Artifact, guide | 50,788 | 12,697 |
| **plan-it, one resource/CRUD feature, UI in scope, no prior `plan.md`, single-shape (no secondary checklist)** | `SKILL.md` (6,542) → `rules/feature-classification.md` (3,171) → `rules/resource-feature-checklist.md` (9,796) → `rules/design-reconciliation.md` (6,514) → `rules/issue-conventions.md` (19,801) → `rules/sequencing.md` (10,509) → `rules/review.md` (16,800); `rules/capability-checklist.md`, `rules/plan-md-input.md`, and `rules/discovered-work.md` are the unused alternates for this shape. A mixed-characteristic feature would add `rules/capability-checklist.md` (4,930) on top, per `rules/feature-classification.md`'s secondary-questions allowance | 73,133 | 18,283 |
| **implement-it, one ordinary issue, no stack companion, cross-skill `review-it` call before Gate 1** | `SKILL.md` (10,042) → `rules/sequencing.md` (8,862) → `rules/verification.md` (35,260) → `review-it/SKILL.md` (6,052, cross-skill) → `review-it/rules/scope.md` (9,064) → `review-it/rules/checklist.md` (9,235) → `review-it/rules/verification.md` (8,686) → `rules/review-gates.md` (13,015) → `rules/commit-boundaries.md` (23,510) → `rules/issue-closure.md` (14,243); `review-it` is invoked before Gate 1's report — well before `commit-boundaries.md` or `issue-closure.md` are reached, not after them — and `sequencing.md`/`verification.md` are each read once and reused later in the same pass (the post-closure ready-set recompute, and the per-commit/completed-issue verification checkpoints) | 137,969 | 34,492 |
| **implement-it, same issue, `laravel-inertia-stack` composed for one filtered-index task (cross-skill, including the blueprint's own further cross-references)** | everything in the row above, plus `laravel-inertia-stack/SKILL.md` (4,164, cross-skill), `blueprints/filters-and-sorting.md` (6,743), `rules/request-normalization.md` (2,761), the four filter/sort templates (1,270 + 999 + 985 + 1,550 = 4,804), `rules/test-ownership.md` (4,364) and `blueprints/pest-testing.md` (7,201) per that blueprint's own "Testing" section, and `rules/php-conventions.md` (1,239) per the same blueprint's own "Naming and location" section, which cites it for the abstract base-class-vs-`final`-subclass convention the new concrete `{Model}Filter`/`{Model}Sort` classes this task authors must follow | 169,245 | 42,311 |
| **ship-it, PR-readiness check only** | `SKILL.md` (5,919) → `rules/milestone-completion.md` (38,499) | 44,418 | 11,105 |
| **ship-it, full PR-readiness → post-merge closure and release** | `SKILL.md` (5,919) → `rules/milestone-completion.md` (38,499, read once, reused for both the readiness check and the later closure gate) → `rules/release.md` (17,050) | 61,468 | 15,367 |

The largest single-workflow figure above (implement-it composed with the Laravel companion,
including that blueprint's own further cross-references, for one task, ~42,311 rough tokens) is
roughly 36% of the repository-wide total (~116,965 rough tokens) — a comparison of two figures this
document itself defines, not a claim about a real session's measured usage; it illustrates that even
the most cross-skill, most-composed representative case this document models stays well short of the
repository-wide sum.

## Concrete reduction opportunities (proposals, not applied in this pass)

These are candidates for a future authoring pass under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md). None is applied here — this
task's scope is measurement and documentation correction, not restructuring or shortening any
operational rule. Every character figure below (a section's current size, a proposed split's
resulting file sizes) is a measurement of what exists today; any character reduction implied by a
proposal is a conditional estimate of what a future split could remove from a given workflow's
load, not a measured runtime benefit — no split, merge, or rewording proposed here has actually been
implemented or benchmarked.

1. **Repair-history narration mixed with necessary behavioral teaching, in a file that must also
   work when installed standalone.** `skills/implement-it/rules/commit-boundaries.md` carries five
   inline parentheticals citing `scenarios.md` (lines 189, 199, 210, 248, 264; 655 characters
   combined). They are not uniform. Two of them — line 210 ("reproduced concretely; see
   `scenarios.md`") and line 264 ("verified in practice; see `scenarios.md`") — add no concrete
   detail beyond the citation itself; the sentence each is attached to already states the behavioral
   fact in full without it, so these two are pure repair-history narration. The other three — line
   189's three-hunk example, line 199's tooling-refuses-on-identical-adjacent-text example, and line
   248's both-staged-together example — each carry a compact, concrete illustration of a non-obvious
   stop condition, closer to `docs/skill-authoring-methodology.md` Section 4's "a compact example
   materially teaches the rule" exception than to removable history. **Any change here must also
   account for how this skill is actually consumed:** per `docs/skill-consumption.md`, an installed
   copy carries only `skills/<name>/` — `scenarios.md` is never installed alongside it, so "(see
   `scenarios.md`)" is already a dangling reference for every consuming project, not a convenient
   shorthand. **What could change:** remove the citation and the narration wrapper from the two
   citation-only parentheticals (lines 210, 264) entirely, since the owning sentence already states
   the fact on its own; for the three example-bearing parentheticals (lines 189, 199, 248), rephrase
   each as a self-contained example inside the rule itself, with no `scenarios.md` reference, rather
   than compressing it into a citation that would mean nothing outside this source repository. **What
   must be preserved:** the operational instruction each parenthetical is attached to (the stop
   conditions, the positive-isolation requirement, the round-trip check) is unrelated to this change;
   this is a proposal to make the file's own examples self-sufficient, not to remove the teaching
   content the three compact examples currently carry.

2. **A large file bundling a common path with a rare, conditional sub-procedure.** *Applied in
   commit `9b77d00`, after the `667fab15` snapshot this section otherwise describes — see "Update:
   commit-reconstruction extraction" below for the measured before/after.*
   `skills/implement-it/rules/commit-boundaries.md` was 23,510 characters, in three parts. Lines
   1–157 (8,798 characters) cover ordinary commit-boundary derivation plus the common "nothing
   committed yet" review-correction case — both consulted on every issue. Lines 158–326 (14,144
   characters, roughly 60% of the file) are the history-reconstruction recipe itself ("Something
   already committed, correction needed before push"), used only when a correction must fold into an
   already-committed, not-yet-pushed commit — a materially rarer case than ordinary boundary
   derivation. Lines 328–342 (567 characters) are a general "Do / Don't summary" covering the whole
   file's guidance, not reconstruction-specific, and would stay with the ordinary-guidance portion
   regardless of any split. **What could change:** route only the reconstruction recipe (lines
   158–326) to its own file (e.g. `rules/commit-reconstruction.md`), consulted only from
   `commit-boundaries.md`'s "Something already committed, correction needed before push" heading, so
   an ordinary issue's commit-building pass — including the common no-reconstruction-needed case —
   no longer pays for a procedure it never reaches. **What must be preserved:** the reconstruction
   procedure's own steps, its scratch-directory, positive-isolation, and classification-stop
   mechanics, its cross-references to `rules/verification.md`'s stash-identity procedure, and the
   general Do/Don't summary's place in the remaining file — none of that changes, only which file
   owns the reconstruction recipe specifically.

3. **A large file covering several distinct conditional surfaces.** *Both halves of this proposal are
   now applied. The `implement-it/verification.md` half was applied in commit `eb64ec9` — see
   "Update: isolation-verification and worktree-preservation extraction" above for the measured
   before/after. The `ship-it/milestone-completion.md` half was applied in commit `a432509` — see
   "Update: ship-it milestone-completion.md split" below. The text immediately below describes both
   exactly as originally proposed, against the `667fab15` snapshot; it is not restated as current.*
   `skills/ship-it/rules/milestone-completion.md` was 38,499 characters, the largest file in this
   skill set, covering three surfaces its own `SKILL.md` already named as distinct — PR readiness
   (~lines 124–192), PR creation (~194–252), CI-failure investigation and correction handoff
   (~253–338), and the closure gate (~348–437) — each with its own trigger condition. A ship-it
   session asked only "is this milestone ready for a PR" loaded the closure-gate and CI-investigation
   mechanics it would not use that pass. Similarly, `skills/implement-it/rules/verification.md` was
   35,260 characters, bundling "Preserving unrelated worktree content during a Git rewrite" (4,326
   characters) and "Isolation verification" (3,080 characters) — together ~21% of the file — into a
   file consulted on every ordinary verification pass, even though both sections were explicitly "a
   deliberate escalation, not the default." **What changed (ship-it):** split `milestone-completion.md`
   along its own already-named conditional surfaces into separately routed
   files, cross-referenced from the owning `SKILL.md`'s "Rules" list exactly as it already
   distinguishes them in prose. **What must be preserved:** every gate, condition, and cross-reference
   currently stated — a split changes which file a reader opens, not what the rule says or when it
   applies.

4. **Duplicated explanation: checked in one reading pass, none found — not a claim that none
   exists.** README.md and SKILL.md pairs were compared across all seven skills for restated content
   (`docs/skill-authoring-methodology.md` Section 7 flags this as a known failure mode). This reading
   found no pair that clearly restates the other: each README explains lifecycle and reasoning in
   plain prose for a human maintainer, while each SKILL.md states the operational ownership and
   routing table an agent needs — the intended, complementary split, even for the two skills
   (`plan-it`, `laravel-inertia-stack`) whose SKILL.md points to its README rather than restating it.
   This is a manual comparison by one reader, not an exhaustive or automated content-similarity
   check, so it establishes "no restatement found in this pass," not "no overlap exists anywhere in
   these fourteen files" — a future pass with different scrutiny, or a change to either file, could
   still find something this one missed. Recorded so a future pass starts from what was actually
   checked, not to foreclose checking again.

## Update: commit-reconstruction extraction (2026-09-09i)

Pinned to commit
[`9b77d00`](https://github.com/elieandraos/agentic-engineering/commit/9b77d0003d463fece6f96a301640becedd36ca36)
on `main`, two commits after the `667fab15` snapshot the rest of this document describes (via
`3269c8f`, the documentation-correction commit that landed between them). This records the effect
of applying reduction proposal 2 above — routing the unpublished-history
reconstruction recipe out of `commit-boundaries.md` into its own file — on the file sizes and
workflow estimates that proposal named. It does not re-measure anything else in this document; every
figure outside this section still describes `667fab15`, per this document's own "later passes append
a new dated section rather than silently overwriting this one's figures." Same Unicode-character
method as the rest of this document (Python `len()` on UTF-8-decoded content).

**Changed file sizes:**

| File | `667fab15` | `9b77d00` | Change |
| --- | ---: | ---: | ---: |
| `rules/commit-boundaries.md` | 23,510 | 10,239 | −13,271 |
| `rules/commit-reconstruction.md` (new) | — | 14,766 | +14,766 |
| `rules/verification.md` | 35,260 | 35,230 | −30 |
| `SKILL.md` | 10,042 | 10,384 | +342 |
| `README.md` | 3,156 | 3,417 | +261 |

`commit-boundaries.md` and `commit-reconstruction.md` combined now total 25,005 characters, 1,495
more than the single 23,510-character file they replace — the entry-condition statement the new
file needed to work when loaded on its own, the three citation examples rewritten to stand alone
without `scenarios.md`, and `commit-boundaries.md`'s own shortened handoff paragraph together add
slightly more than they removed from the five citation-wrapper trims. `verification.md`'s two
cross-references were repointed at the new file (−30 characters net). `SKILL.md` gained one routing
entry for the conditional file (+342); `README.md`'s "Context consumption" section was expanded to
distinguish the five ordinary rule files from the one conditional one (+261). These four routing/
shared-dependency changes are not optional overhead an ordinary pass can skip — `SKILL.md` and (when
referenced) `README.md` always load, and `verification.md` loads on every ordinary pass regardless
of which path a correction takes.

**Workflow estimates, ordinary vs. reconstruction path — same "implement-it, one ordinary issue"
shape this document already models, recomputed:**

| Path | Files counted (delta from the file-size table) | Characters | Rough tokens |
| --- | --- | ---: | ---: |
| **Ordinary** (no reconstruction needed) | `SKILL.md` (10,384) + `sequencing.md` (8,862, unchanged) + `verification.md` (35,230) + `review-it`'s four files (33,037, unchanged) + `review-gates.md` (13,015, unchanged) + `commit-boundaries.md` (10,239) + `issue-closure.md` (14,243, unchanged); `commit-reconstruction.md` **not loaded** | 125,010 | 31,252 |
| **Reconstruction** (a correction folds into an already-committed, unpublished commit) | everything in the row above, plus `commit-reconstruction.md` (14,766) | 139,776 | 34,944 |

Against the `667fab15` snapshot's single "implement-it, one ordinary issue" row (137,969 characters,
34,492 tokens, which bundled the reconstruction recipe into every pass regardless of whether it was
needed): the now-more-common **ordinary** path drops to 125,010 characters (31,252 tokens) — a
modeled reduction of 12,959 characters (3,240 tokens, ~9.4%) for the path that doesn't need
reconstruction. The **reconstruction** path itself, which always needed this content, now costs
139,776 characters (34,944 tokens) — 1,807 characters (452 tokens) *more* than the old bundled
figure, the routing/self-sufficiency overhead described above landing on the rarer path instead of
every pass. The Laravel-composed row (`implement-it` + `laravel-inertia-stack` for one filtered-index
task) moves the same way on its ordinary path: 169,245 → 156,286 characters (42,311 → 39,072 tokens,
the same 12,959-character/3,239-token reduction, since the Laravel-specific additions are unchanged).

**These are the same kind of modeled text-volume estimates the rest of this document uses, not a
measured runtime benefit.** No agent session was run to confirm an ordinary implement-it pass
actually avoids opening `commit-reconstruction.md`, or that ordinary and reconstruction requests
occur in any particular proportion in real use — the "more common" framing above is the proposal's
own stated rationale (a review correction needing history reconstruction is rarer than one that
isn't), not a frequency this document measured. The repository-wide `skills/` total moves from
467,861 to 469,929 characters (58 files, up from 57) at `9b77d00` — a net increase, since routing
overhead was added across five files while only one recipe was relocated, not shortened.

**Behavior preservation.** Comparing the extracted procedure against its `667fab15` source
line-by-line: every Git command block (three `git merge-file` invocations) is byte-identical; the
only prose changes are the five `scenarios.md` citation edits (two pure citations removed, three
rewritten as self-contained examples) and one necessary cross-reference fix (the "What makes a
commit coherent" pointer, now naming `commit-boundaries.md` explicitly since that section lives in a
different file than the sentence citing it). No gate, stop condition, classification rule, or
verification requirement changed. See this pass's own commit message and the Control Room report for
the full comparison; this document reports only the resulting sizes.

## Update: isolation-verification and worktree-preservation extraction (2026-09-09j)

Pinned to commit
[`eb64ec9`](https://github.com/elieandraos/agentic-engineering/commit/eb64ec9fd156407b14119fa39db5902ae2346308)
on `main`, two commits after the `9b77d00` snapshot the previous update section describes (via
`a85c956`, that section's own measurement-update commit), and four commits after the `667fab15`
snapshot the rest of this document describes (`667fab15` → `3269c8f` → `9b77d00` → `a85c956` →
`eb64ec9`). This records the effect of applying the `implement-it/verification.md` half of
reduction proposal 3 above — routing `verification.md`'s "Preserving unrelated worktree content
during a Git rewrite" and "Isolation verification" technique out into their own files,
`rules/worktree-preservation.md` and
`rules/isolation-verification.md`, while keeping the decision for *when* isolation verification is
warranted visible in `verification.md` itself. It does not re-measure anything else in this
document; every figure outside this section and the previous "Update" section still describes
`667fab15`, per this document's own "later passes append a new dated section rather than silently
overwriting this one's figures." Same Unicode-character method as the rest of this document.

**Correction to the previous update section's own history claim:** that section stated `9b77d00` was
"one commit after the `667fab15` snapshot." It is two commits after (`667fab15` → `3269c8f` →
`9b77d00`) — corrected in place above, not restated as a new finding here, since it describes that
section's own pinned commit, not this one's.

**Changed file sizes (relative to `9b77d00`, the previous pinned revision):**

| File | `9b77d00` | `eb64ec9` | Change |
| --- | ---: | ---: | ---: |
| `rules/verification.md` | 35,230 | 29,387 | −5,843 |
| `rules/isolation-verification.md` (new) | — | 2,358 | +2,358 |
| `rules/worktree-preservation.md` (new) | — | 4,273 | +4,273 |
| `rules/commit-reconstruction.md` | 14,766 | 14,817 | +51 |
| `SKILL.md` | 10,384 | 11,096 | +712 |
| `README.md` | 3,417 | 3,755 | +338 |

`verification.md` shrank by 5,843 characters — the two extracted sections' full content, minus the
short routing pointer and ownership-statement text that replaced them. `commit-reconstruction.md`
grew by 51 characters (its two cross-references to the moved preservation procedure and isolation
technique, repointed to their new files). `SKILL.md` gained two routing entries (+712); `README.md`'s
"Context consumption" section was rewritten to describe three conditional files instead of one
(+338). As in the previous update, these routing/shared-dependency changes are not skippable
overhead — `SKILL.md` and `verification.md` load on every ordinary pass regardless of which
escalation, if any, a given issue needs.

**Workflow estimates, counting shared dependencies once — three paths this document now
distinguishes for `implement-it`, where the previous update distinguished only two:**

| Path | Files counted (delta from the ordinary "implement-it, one ordinary issue" row) | Characters | Rough tokens |
| --- | --- | ---: | ---: |
| **Ordinary** (no isolation, no reconstruction) | `SKILL.md` (11,096) + `sequencing.md` (8,862, unchanged) + `verification.md` (29,387) + `review-it`'s four files (33,037, unchanged) + `review-gates.md` (13,015, unchanged) + `commit-boundaries.md` (10,239, unchanged) + `issue-closure.md` (14,243, unchanged); `isolation-verification.md`, `worktree-preservation.md`, and `commit-reconstruction.md` **not loaded** | 119,879 | 29,970 |
| **Isolation-triggered** (an intermediate commit's correctness needs proving, no reconstruction) | everything in the row above, plus `isolation-verification.md` (2,358) and `worktree-preservation.md` (4,273); `commit-reconstruction.md` still not loaded | 126,510 | 31,628 |
| **Reconstruction** (a correction folds into an already-committed, unpublished commit — mandates isolation verification for every rebuilt commit, per `commit-reconstruction.md` step 11) | the ordinary row, plus `commit-reconstruction.md` (14,817), `isolation-verification.md` (2,358), and `worktree-preservation.md` (4,273) | 141,327 | 35,332 |

**Incremental change (this pass, against the `9b77d00` snapshot the previous update measured):**

- Ordinary path: 125,010 → 119,879 characters (31,252 → 29,970 tokens) — a further modeled
  reduction of 5,131 characters (1,282 tokens), on top of the previous pass's own reduction.
- Reconstruction path: 139,776 → 141,327 characters (34,944 → 35,332 tokens) — a modeled increase of
  1,551 characters (388 tokens): the reconstruction path now separately pays for
  `isolation-verification.md` and `worktree-preservation.md`, which were previously folded into the
  single `verification.md` it already loaded. This is the same direction the first pass moved this
  path in, not an offsetting saving: extracting `commit-reconstruction.md` in the first pass also
  increased the reconstruction path's total (137,969 → 139,776, +1,807 characters) rather than saving
  anything on it — see the previous update section's own figures. Both extractions have added to this
  path's modeled cost so far; neither has reduced it.

**Cumulative change (both passes combined, against the original `667fab15` snapshot before either
extraction):**

- Ordinary path: 137,969 → 119,879 characters (34,492 → 29,970 tokens) — a modeled reduction of
  18,090 characters (4,522 tokens, ~13.1%) for the path that needs neither escalation.
- Reconstruction path: 137,969 → 141,327 characters (34,492 → 35,332 tokens) — a modeled increase of
  3,358 characters (840 tokens, ~2.4%) for the path that needs both conditional procedures in full,
  accumulated across both passes (+1,807 in the first pass, +1,551 in this one). Routing/entry-
  condition text is not confined to this path — `SKILL.md`, which loads on every pass regardless of
  which path it takes, grew in both passes too (+342, then +712; see the file-size tables above). The
  ordinary path's net reduction comes from excluding the conditional procedure bodies themselves — a
  far larger removal from `commit-boundaries.md` and `verification.md`, files the ordinary path
  already loaded in full — not from routing overhead landing exclusively on the reconstruction path;
  the reconstruction path pays that same shared `SKILL.md` growth on top of loading the full
  conditional content the ordinary path now skips.
- The Laravel-composed ordinary row (`implement-it` + `laravel-inertia-stack` for one filtered-index
  task) moves the same way as the base ordinary row: 169,245 → 151,155 characters (42,311 → 37,789
  tokens), the same 18,090-character/4,522-token cumulative reduction, since the Laravel-specific
  additions are unchanged by either extraction.

**These remain the same kind of modeled text-volume estimates this document uses throughout, not a
measured runtime benefit.** No agent session was run to confirm an ordinary or isolation-triggered
pass actually avoids opening `commit-reconstruction.md`, or that the three paths occur in any
particular real-world proportion — this document has no data on how often implement-it work needs
isolation verification without full reconstruction, isolation verification is a stated design
observation from `rules/verification.md` itself ("a deliberate escalation, not the default"), not a
frequency this document measured. The repository-wide `skills/` total moves from 469,929 to 471,818
characters (60 files, up from 58) at `eb64ec9` — a net increase, consistent with both passes: routing
overhead is added across several files each time, while the extracted content itself is relocated,
not shortened.

**Behavior preservation.** Comparing both extracted files against their `9b77d00` source
line-by-line: in `worktree-preservation.md`, all nine numbered steps are untouched — the only
difference is the heading conversion and one cross-file reference fix (`the isolation technique
below` → `` `rules/isolation-verification.md`'s technique ``). In `isolation-verification.md`, the
technique's six numbered steps are untouched except for three necessary cross-file reference fixes
(pointing at `rules/worktree-preservation.md` and two named sections of `rules/verification.md`
instead of same-file `above`/`below` references that no longer resolve once split across files); the
trigger blockquote, the "reach for this when" criteria, and the escalation-cost rationale paragraph
were deliberately *not* moved — they remain byte-identical in `verification.md`, confirmed by exact
substring match against the pinned source, satisfying this task's requirement that the decision for
when isolation is required stay visible in the file an agent needs it to discover. No gate, command,
stop condition, reuse condition, or stash-identity/restoration mechanic changed. See this pass's own
commit message and the Control Room report for the full comparison; this document reports only the
resulting sizes.

## Update: ship-it milestone-completion.md split (2026-09-09k)

Pinned to commit
[`a432509`](https://github.com/elieandraos/agentic-engineering/commit/a4325097aeb1daff619ec37a4993ad23144235c3)
on `main`. This records the effect of applying the `ship-it/milestone-completion.md` half of
reduction proposal 3 above — splitting that file's three conditional surfaces (PR readiness and
creation, CI-failure investigation and correction handoff, and the closure gate) into
`rules/milestone-pr-readiness.md`, `rules/ci-failure-correction.md`, and a narrowed
`rules/milestone-completion.md` that now owns closure and the shared delivery-lifecycle entry map. It
does not re-measure anything else in this document; every figure outside this section and the two
"Update" sections above it still describes `667fab15`. Same Unicode-character method as the rest of
this document.

**Changed file sizes:**

| File | Before | After | Change |
| --- | ---: | ---: | ---: |
| `rules/milestone-completion.md` | 38,499 | 20,823 | −17,676 |
| `rules/milestone-pr-readiness.md` (new) | — | 14,394 | +14,394 |
| `rules/ci-failure-correction.md` (new) | — | 8,937 | +8,937 |
| `rules/release.md` | 17,050 | 17,052 | +2 |
| `SKILL.md` | 5,919 | 6,391 | +472 |
| `README.md` | 2,386 | 2,540 | +154 |

`milestone-completion.md` shrank by 17,676 characters — the two extracted surfaces' full content,
minus the shared entry map, closure gate, and the short routing text that replaced them.
`release.md` gained 2 characters (one cross-reference repointed from `milestone-completion.md` to
`milestone-pr-readiness.md`, net of wording adjustment). `SKILL.md` gained two routing entries
(+472); `README.md`'s "Context consumption" section now names four conditional files instead of two
(+154).

**Workflow estimates.** Each row's *local-file subtotal* is `SKILL.md` plus only the rule file(s)
that surface's own procedure lives in. Where that procedure's own text carries an explicit
instruction to consult another file's content (not merely an orientation citation), a separate
*broader estimate* adds that file's full size too, under this document's whole-file loading model (a
followed reference loads the complete file, not only the cited section). Whether the broader estimate
applies is stated per row, and not every case is optional: some are conditional on what the pass
actually encounters (a manual-testing finding needing scope interpretation), but at least one below
is a mandatory step in the row's own numbered procedure, not an edge case — there, the local-file
subtotal alone understates the path's real minimum cost, not merely its ceiling.

| Path | Local-file subtotal | Broader estimate |
| --- | --- | --- |
| **PR readiness and authorized creation** | `SKILL.md` (6,391) + `rules/milestone-pr-readiness.md` (14,394) = 20,785 chars, 5,196 tokens | *Conditional.* + `rules/milestone-completion.md` (20,823) = 41,608 chars, 10,402 tokens — only when the pass actually follows `milestone-pr-readiness.md`'s own citation into `milestone-completion.md`'s shared guidance (scoping a manual-testing finding against the milestone description, or confirming Backlog eligibility); an ordinary pass that needs neither stays at the local-file subtotal |
| **CI-failure investigation and correction handoff** | `SKILL.md` (6,391) + `rules/ci-failure-correction.md` (8,937) = 15,328 chars, 3,832 tokens | *Mandatory, not merely conditional.* + `implement-it/rules/review-gates.md` (13,016, cross-skill) = 28,344 chars, 7,086 tokens. Step 3 of this procedure unconditionally directs consulting that file's "when to stop and ask" standard to determine whether a correction stays in scope — every real investigation reaches it, not only some. The local-file subtotal alone therefore does not establish this path's complete workflow cost; 28,344/7,086 is closer to the actual minimum. (This file's own citations of `rules/milestone-completion.md` remain orientation only, confirmed unchanged from the prior pass — naming what it is and where it starts, not an instruction to consult its content.) Step 6's handoff to `implement-it`'s own lifecycle once authorized — Gate 1/Gate 2, `commit-boundaries.md`, `verification.md` — is a separate skill invocation, modeled as `implement-it`'s own workflow cost elsewhere in this document, not folded into this row |
| **Post-merge closure only** | `SKILL.md` (6,391) + `rules/milestone-completion.md` (20,823) = 27,214 chars, 6,804 tokens | Not applicable — closure is self-contained in this file |
| **Full delivery, happy path** (readiness → creation → closure → release, no CI failure) | `SKILL.md` (6,391) + `rules/milestone-pr-readiness.md` (14,394) + `rules/milestone-completion.md` (20,823) + `rules/release.md` (17,052) = 58,660 chars, 14,665 tokens | Already includes `milestone-completion.md`, so the PR-readiness row's own broader-estimate distinction does not add anything further here |

A full-delivery pass that also hits a CI failure reaches the CI-failure row's own mandatory
dependency too (step 3's `implement-it/rules/review-gates.md` consultation): add
`rules/ci-failure-correction.md` (8,937) plus `implement-it/rules/review-gates.md` (13,016) to the
happy-path total — 58,660 + 21,953 = 80,613 characters, 20,153 tokens — not merely
`ci-failure-correction.md`'s own 8,937 characters in isolation.

**Change against the `667fab15` snapshot the rest of this document describes:**

- The old, single "ship-it, PR-readiness check only" row (`SKILL.md` + the whole
  `milestone-completion.md`) was 44,418 characters (11,105 tokens). Compared against the **local-file
  subtotal** (20,785 characters, 5,196 tokens), that is a modeled reduction of 23,633 characters
  (5,909 tokens, ~53%) — but this is the reduction for the minimal case only, when the pass never
  needs `milestone-completion.md`'s shared guidance, not a general PR-readiness saving. Compared
  against the **broader estimate** (41,608 characters, 10,402 tokens, when that guidance actually is
  needed), the reduction is only 2,810 characters (703 tokens, ~6%) — most of the old file's content
  is still reached, just through a followed cross-reference rather than a single bundled file.
- The old "ship-it, full PR-readiness → post-merge closure and release" row was 61,468 characters
  (15,367 tokens). The new happy-path equivalent is 58,660 characters (14,665 tokens) — a modeled
  reduction of 2,808 characters (702 tokens, ~5%). This saving is not from moving PR-readiness/
  creation content into a separate file — this path loads both `milestone-pr-readiness.md` and
  `milestone-completion.md` regardless of which file holds that content, so relocating it saves
  nothing here. The saving instead comes from excluding `rules/ci-failure-correction.md`'s content
  (5,375 characters, the exact size of the old file's former CI-failure section, measured the same
  Unicode-character way as every other figure in this document), which the old single file bundled
  into every load unconditionally, even for a pass with no CI failure. That exclusion is partially
  offset by routing/structural overhead added across the split — 2,093 characters split between
  `milestone-pr-readiness.md` and `milestone-completion.md` (each file's own entry-condition text and
  duplicated Cross-rule-dependencies/Reporting/Do-Don't sections), plus `SKILL.md`'s +472 and
  `release.md`'s +2 — reconciling exactly: 5,375 − 2,093 − 472 − 2 = 2,808.
- CI-failure investigation has no prior comparable row in this document — the earlier snapshot never
  modeled it as distinguishable from the bundled `milestone-completion.md` load.

**These are the same kind of modeled text-volume estimates this document uses throughout, not a
measured runtime benefit.** No agent session was run to confirm a real PR-readiness check actually
avoids opening `rules/ci-failure-correction.md`, or that these four paths occur in any particular
real-world proportion. The repository-wide `skills/` total moves from 472,276 to 478,686 characters
(62 files, up from 60 — two new files added) at `a432509`. 472,276 is the immediate `7b0dcea`
predecessor's own total, not the earlier `eb64ec9` figure (471,818) the previous update section
reports — two intervening commits (`27486d8`, `7b0dcea`) made small unrelated wording corrections
between those two snapshots, so `eb64ec9`'s own 471,818 remains that commit's correct total, but is
not the right baseline for measuring this pass's own change. The 6,410-character difference here is
consistent with the pattern the two `implement-it` updates above already established: routing
overhead is added across several always-loaded files each time, while the extracted content itself
is relocated, not shortened.

**Behavior preservation.** Every substantive line moved from `milestone-completion.md` into the two
new files was compared against the pinned source with a line-by-line diff; every difference found is
one of the identified necessary cross-file reference fixes (a same-file `above`/`below` pointer,
inline diagram annotation, or named-section citation that no longer resolved once split across
files) — no Git command, numbered step, gate, approval requirement, or condition was reworded or
reordered. `rules/release.md` required exactly one such fix (its "milestone-PR reference convention"
citation, now pointing at `rules/milestone-pr-readiness.md`). A repository-wide search found seven
caller files outside `ship-it` citing the moved sections by name (`implement-it`'s `SKILL.md`,
`sequencing.md`, `review-gates.md`, `issue-closure.md`; `plan-it`'s `issue-conventions.md`;
`review-it`'s `SKILL.md`; and `artifacts/ship-it.md`); each was repointed to whichever of the three
files now owns the section it actually cited, and two prose references that genuinely spanned both
the PR-readiness and closure surfaces were reworded to name both files rather than one. See this
pass's own commit message and the Control Room report for the full comparison; this document reports
only the resulting sizes.

## Metadata correction

`skills/review-it/SKILL.md`'s frontmatter `description` exceeded the Agent Skills specification's
1,024-character limit by 195 characters (1,219 measured; see `scenarios.md`'s META-01). It was
shortened to 966 characters in an earlier pass — see `scenarios.md`'s append-only metadata-correction
records for the before/after text and validation method. This pass leaves that fix unchanged and
re-validates it below alongside the other six entrypoints' frontmatter.

| Skill | Description characters | Within 1,024 limit |
| --- | ---: | --- |
| document-it | 553 | Yes |
| implement-it | 839 | Yes |
| lab-it | 641 | Yes |
| laravel-inertia-stack | 373 | Yes |
| plan-it | 716 | Yes |
| review-it | 966 (was 1,219) | Yes (was: No, by 195) |
| ship-it | 923 | Yes |

Each entrypoint has exactly `name` and `description` fields (no extra metadata fields, invocation
controls, or dependencies), and each `name` matches its directory.

## Reproducing these numbers

```bash
# Discovery metadata: one skill's description length, in Unicode characters
python3 -c "
import re
content = open('skills/<name>/SKILL.md', encoding='utf-8').read()
m = re.search(r'description: \"(.*?)\"\n', content, re.DOTALL)
print(len(m.group(1)))
"

# A single file's Unicode character count (the unit this document uses throughout)
python3 -c "print(len(open('skills/<name>/SKILL.md', encoding='utf-8').read()))"

# The same file's byte count, for comparison only — this will be larger whenever the
# file uses em dashes, curly quotes, or other multi-byte UTF-8 characters; do not use
# this figure interchangeably with the character counts above
wc -c skills/<name>/SKILL.md

# Every file under one skill, character counts, largest last
python3 -c "
import glob, os
files = sorted(glob.glob('skills/<name>/**/*', recursive=True))
sized = [(len(open(f, encoding='utf-8').read()), f) for f in files if os.path.isfile(f)]
for c, f in sorted(sized):
    print(c, f)
"

# Whole repository's skill content, character count
python3 -c "
import glob, os
files = [f for f in glob.glob('skills/**/*', recursive=True) if os.path.isfile(f)]
print(sum(len(open(f, encoding='utf-8').read()) for f in files), 'characters across', len(files), 'files')
"
```

Rough tokens throughout this document are the resulting character count divided by 4, rounded to
the nearest whole number — not a tokenizer run and not an observed session's actual usage.
