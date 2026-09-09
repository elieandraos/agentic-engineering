# Skill Context Consumption

Dated measurements of how much an agent actually loads to use a skill in this repository, and what
it does not load merely because the skill is installed. This document is the single, ongoing home
for these numbers — later passes append a new dated section rather than silently overwriting this
one's figures.

**Authority boundary.** This document measures and models context cost; it does not change any
skill's operational rules, gates, or approvals. Where a reduction is proposed below, the proposal is
inert until a separate authoring pass implements it under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md).

**Revision note (2026-09-09b).** This revises the first 2026-09-09 version of this same document,
which mixed two different units (byte counts from `wc -c` presented alongside Unicode-character
description limits), listed workflow-file orders that didn't match the owning skill's actual
lifecycle, and stated some conditional dependencies as absolute ("never loaded together," "never
pulls in") without checking every owning rule file first. This version corrects all three; the
numbers below replace, rather than supplement, that first version's tables.

## Measurement date and source

Measured 2026-09-09, against this repository's working tree, built on top of commit `cd2f3f5` on
`main` — this pass's own changes land as ordinary new commits after it, not a rewrite of it. Skill
file sizes change as skills evolve; treat every number below as true of that pinned revision, not a
standing fact — re-run "Reproducing these numbers" below against the current tree to refresh them.
This supersedes, for directory-wide and workflow-level figures, the narrower SKILL.md-only table in
`scenarios.md`'s "Entry-point size observations" (2026-09-08); that table's own pinned-commit
figures are unchanged and preserved there as a historical record, not restated here as current.

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
   routing can require more than the primary table entry alone. Markdown files here are not chunked
   or partially loaded — once a workflow needs a file, that file's complete size is the cost,
   regardless of how much of it the current path actually exercises.

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

Rough tokens: ~1,253. This is the entire cost of having all seven skills installed but unused in a
given session — roughly two orders of magnitude below any single activated workflow below.

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

`rules/verification.md` is the single largest supporting file among the six portable skills, and
`rules/commit-boundaries.md` is second — both are flagged in "Concrete reduction opportunities"
below.

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
tokens: **~116,965**. No real workflow loads this whole figure at once — it is the sum across all
seven skills' entrypoints, rules, blueprints, templates, and READMEs, useful only as an upper bound
against which the workflow estimates below should be read.

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
results), and any external companion skill this repository does not publish (Laravel Boost's
`laravel-best-practices`, `testing-best-practices`, `inertia-vue-development` — real cost when
installed, but not measurable from this repository). `README.md` files are excluded by default: five
of the seven skills' `SKILL.md` files never mention `README.md`, so an executing agent has no stated
reason to open it. The two exceptions — `plan-it` and `laravel-inertia-stack`, whose `SKILL.md` text
each point a reader to `README.md` — are called out in their rows below rather than silently folded
into the totals, since whether an executing agent actually follows a prose pointer like that, versus
a human maintainer reading the same file, is not something this document can assert either way.
`docs/skill-authoring-methodology.md` and `docs/skill-consumption.md` are also excluded — they serve
a skill's author or a project's installer, not a running pipeline workflow, and no `SKILL.md` or rule
file in this repository references either one.

| Workflow | Files counted (in order) | Characters | Rough tokens |
| --- | --- | ---: | ---: |
| **review-it, standalone review** | `SKILL.md` (6,052) → `rules/scope.md` (9,064) → `rules/checklist.md` (9,235) → `rules/verification.md` (8,686) | 33,037 | 8,259 |
| **lab-it, investigation-and-answer only** | `SKILL.md` (7,497) — `rules/plan-synthesis.md` not reached; no `plan.md` was requested | 7,497 | 1,874 |
| **lab-it, plan feature architecture** | `SKILL.md` (7,497) → `rules/plan-synthesis.md` (12,789) | 20,286 | 5,072 |
| **document-it, new Markdown guide from already-sufficient evidence** | `SKILL.md` (13,742) → `rules/doc-style.md` (7,645) → `rules/review.md` (13,001); `lab-it` not routed to (evidence already sufficient) | 34,388 | 8,597 |
| **document-it, new Artifact guide** | same as above, plus `rules/template.html` (20,913) | 55,301 | 13,825 |
| **document-it, update routed through `lab-it` for stale evidence (cross-skill)** | `SKILL.md` (13,742) → `lab-it/SKILL.md` (7,497, cross-skill) → `rules/maintenance.md` (8,903) → `rules/review.md` (13,001) | 43,143 | 10,786 |
| **plan-it, one resource/CRUD feature, UI in scope, no prior `plan.md`, single-shape (no secondary checklist)** | `SKILL.md` (6,542) → `rules/feature-classification.md` (3,171) → `rules/resource-feature-checklist.md` (9,796) → `rules/design-reconciliation.md` (6,514) → `rules/issue-conventions.md` (19,801) → `rules/sequencing.md` (10,509) → `rules/review.md` (16,800); `rules/capability-checklist.md`, `rules/plan-md-input.md`, and `rules/discovered-work.md` are the unused alternates for this shape. A mixed-characteristic feature would add `rules/capability-checklist.md` (4,930) on top, per `rules/feature-classification.md`'s secondary-questions allowance | 73,133 | 18,283 |
| **implement-it, one ordinary issue, no stack companion, cross-skill `review-it` call before Gate 1** | `SKILL.md` (10,042) → `rules/sequencing.md` (8,862) → `rules/verification.md` (35,260) → `review-it/SKILL.md` (6,052, cross-skill) → `review-it/rules/scope.md` (9,064) → `review-it/rules/checklist.md` (9,235) → `review-it/rules/verification.md` (8,686) → `rules/review-gates.md` (13,015) → `rules/commit-boundaries.md` (23,510) → `rules/issue-closure.md` (14,243); `review-it` is invoked before Gate 1's report — well before `commit-boundaries.md` or `issue-closure.md` are reached, not after them — and `sequencing.md`/`verification.md` are each read once and reused later in the same pass (the post-closure ready-set recompute, and the per-commit/completed-issue verification checkpoints) | 137,969 | 34,492 |
| **implement-it, same issue, `laravel-inertia-stack` composed for one filtered-index task (cross-skill, including the blueprint's own testing cross-references)** | everything in the row above, plus `laravel-inertia-stack/SKILL.md` (4,164, cross-skill), `blueprints/filters-and-sorting.md` (6,743), `rules/request-normalization.md` (2,761), the four filter/sort templates (1,270 + 999 + 985 + 1,550 = 4,804), and — per that blueprint's own "Testing" section — `rules/test-ownership.md` (4,364) and `blueprints/pest-testing.md` (7,201) | 168,006 | 42,002 |
| **ship-it, PR-readiness check only** | `SKILL.md` (5,919) → `rules/milestone-completion.md` (38,499) | 44,418 | 11,105 |
| **ship-it, full PR-readiness → post-merge closure and release** | `SKILL.md` (5,919) → `rules/milestone-completion.md` (38,499, read once, reused for both the readiness check and the later closure gate) → `rules/release.md` (17,050) | 61,468 | 15,367 |

The largest single-workflow figure above (implement-it composed with the Laravel companion,
including its internal testing cross-references, for one task, ~42,002 rough tokens) is roughly 36%
of the repository-wide total (~116,965 rough tokens) — still well under "everything installed," even
for the most cross-skill, most-composed representative case this document models.

## Concrete reduction opportunities (proposals, not applied in this pass)

These are candidates for a future authoring pass under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md). None is applied here — this
task's scope is measurement and documentation correction, not restructuring or shortening any
operational rule.

1. **Repair-history narration embedded inside an operational rule file.**
   `skills/implement-it/rules/commit-boundaries.md` carries five inline parentheticals citing
   `scenarios.md` while narrating *why* a step matters (e.g., "reproduced concretely: three separate
   hunks in one file: one unrelated hunk already staged, one unrelated hunk still unstaged, and the
   correction itself unstaged; the prior extraction-by-subtraction folded the unstaged unrelated hunk
   into the 'correction' and round-tripped anyway — see `scenarios.md`" at line 189). Across all five
   occurrences (lines 189, 199, 210, 248, 264) these parentheticals total exactly 655 characters of
   defect-history narration inside a file that loads on every commit-boundary consult, ordinary or
   corrective. **What could change:** shorten each to a bare citation (e.g., "(see `scenarios.md` for
   the reproduced failure)") and move the narrative detail entirely into `scenarios.md`, which already
   carries the full reproduction. **What must be preserved:** the operational instruction each
   parenthetical is attached to (the stop conditions, the positive-isolation requirement, the
   round-trip check) is unrelated to this trim and must not change; per
   `docs/skill-authoring-methodology.md` Section 4, "a compact example materially teaches the rule"
   can still justify keeping a short version rather than deleting it outright — the proposal is
   compression, not blanket removal.

2. **A large file bundling a common path with a rare, conditional sub-procedure.**
   `skills/implement-it/rules/commit-boundaries.md` is 23,510 characters; lines 1–148 (8,366
   characters) cover ordinary commit-boundary derivation, consulted on every issue, while lines
   149–343 (15,144 characters, roughly 64% of the file) are the history-reconstruction recipe used
   only when a correction must fold into an already-committed, not-yet-pushed commit — a materially
   rarer case than ordinary boundary derivation. **What could change:** route the reconstruction
   procedure to its own file (e.g. `rules/commit-reconstruction.md`), consulted only from
   `commit-boundaries.md`'s "Something already committed, correction needed before push" heading, so
   an ordinary issue's commit-building pass no longer pays for a procedure it never reaches. **What
   must be preserved:** the reconstruction procedure's own steps, its scratch-directory,
   positive-isolation, and classification-stop mechanics, and its cross-references to
   `rules/verification.md`'s stash-identity procedure — none of that changes, only which file owns it.

3. **A large file covering several distinct conditional surfaces.**
   `skills/ship-it/rules/milestone-completion.md` (38,499 characters, the largest file in this skill
   set) covers three surfaces its own `SKILL.md` already names as distinct — PR readiness (~lines
   124–192), PR creation (~194–252), CI-failure investigation and correction handoff (~253–338), and
   the closure gate (~348–437) — each with its own trigger condition. A ship-it session asked only
   "is this milestone ready for a PR" currently loads the closure-gate and CI-investigation mechanics
   it will not use this pass. Similarly, `skills/implement-it/rules/verification.md` (35,260
   characters) bundles "Preserving unrelated worktree content during a Git rewrite" (4,326
   characters) and "Isolation verification" (3,080 characters) — together ~21% of the file — into a
   file consulted on every ordinary verification pass, even though both sections are explicitly "a
   deliberate escalation, not the default." **What could change:** split each file along its own
   already-named conditional surfaces into separately routed files, cross-referenced from the owning
   `SKILL.md`'s "Rules" list exactly as it already distinguishes them in prose. **What must be
   preserved:** every gate, condition, and cross-reference currently stated — a split changes which
   file a reader opens, not what the rule says or when it applies.

4. **Duplicated explanation, checked and not found at repository scope.** README.md and SKILL.md
   pairs were compared across all seven skills for restated content (`docs/skill-authoring-
   methodology.md` Section 7 flags this as a known failure mode). No pair currently restates the
   other: each README explains lifecycle and reasoning in plain prose for a human maintainer, while
   each SKILL.md states the operational ownership and routing table an agent needs — the intended,
   complementary split, even for the two skills (`plan-it`, `laravel-inertia-stack`) whose SKILL.md
   points to its README rather than restating it. This is recorded as a checked-and-clear result, not
   a defect, so a future pass does not have to re-derive it.

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
