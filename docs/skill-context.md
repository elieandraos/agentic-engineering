# Skill Context Consumption

Dated measurements of how much an agent actually loads to use a skill in this repository, and what
it does not load merely because the skill is installed. This document is the single, ongoing home
for these numbers — later passes append a new dated section rather than silently overwriting this
one's figures.

**Authority boundary.** This document measures and estimates context cost; it does not change any
skill's operational rules, gates, or approvals. Where a reduction is proposed below, the proposal is
inert until a separate authoring pass implements it under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md).

## Measurement date and source

Measured 2026-09-09, against this repository at commit `39b82355` on `main`. Skill file sizes
change as skills evolve; treat every number below as true of that commit, not a standing fact —
re-run "Reproducing these numbers" below to refresh them. This supersedes, for directory-wide and
workflow-level figures, the narrower SKILL.md-only table in `scenarios.md`'s "Entry-point size
observations" (2026-09-08); that table's own pinned-commit figures are unchanged and preserved
there as a historical record, not restated here as current.

## Method

**Rough tokens = characters ÷ 4, always.** This is a coarse approximation, not a Claude tokenizer
count and not an observed session's actual token usage — actual tokenization varies with content
(code, prose, punctuation density) and no session-usage figure is claimed anywhere in this
document. Every "rough tokens" figure below is this same division, stated so the arithmetic is
checkable, not a measured or modeled tokenizer output.

Character counts are `wc -c` (raw bytes; this repository's Markdown and HTML are ASCII/UTF-8 with
negligible multi-byte content, so bytes and characters track closely enough for a rough estimate).

## Three loading tiers

Installing a skill does not load its whole directory. What actually enters context happens in three
distinct tiers, at three different times:

1. **Discovery metadata** — each installed skill's frontmatter `description` (and `name`), read by
   the agent to decide which skill, if any, applies to the current request. This is the only part of
   an *inactive* skill that costs anything. It loads for every installed skill, not only the one that
   ends up activating.
2. **Activated `SKILL.md`** — once a skill is selected, its complete `SKILL.md` (frontmatter plus
   body) loads. This is the operational routing entrypoint: activation vocabulary, ownership, and
   the routing table to supporting files — not yet the supporting files themselves.
3. **Supporting files, on demand** — a `rules/`, `blueprints/`, or `templates/` file loads only when
   the activated `SKILL.md`'s own routing sends the current workflow to it. A skill with nine rule
   files (`plan-it`) does not load all nine for every request; it loads the two or three the request's
   own shape requires. Markdown files here are not chunked or partially loaded — once a workflow needs
   a file, that file's complete size is the cost, regardless of how much of it the current path
   actually exercises.

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
given session — two to three orders of magnitude below any single activated workflow below.

## Activated SKILL.md sizes

| Skill | SKILL.md characters | Rough tokens |
| --- | ---: | ---: |
| document-it | 13,844 | 3,461 |
| implement-it | 10,106 | 2,527 |
| lab-it | 7,545 | 1,886 |
| laravel-inertia-stack | 4,176 | 1,044 |
| plan-it | 6,590 | 1,648 |
| review-it | 6,092 | 1,523 |
| ship-it | 5,957 | 1,489 |
| **Total (all seven, if all were activated)** | **54,310** | **13,578** |

review-it's SKILL.md dropped from 6,343 to 6,092 characters in this pass — the frontmatter
description shortened from 1,219 to 966 characters (see "Metadata correction" below); the body is
unchanged.

## Supporting rule, blueprint, and template sizes

Every supporting file under each skill's `rules/`, `blueprints/`, and `templates/` directories,
largest first per skill. `README.md` is listed separately — it is a human-facing orientation file,
never read by the agent as part of executing a workflow (see the exclusions stated under
"Estimated file-loading costs for representative workflows" below).

### document-it

| File | Characters |
| --- | ---: |
| `rules/template.html` | 20,947 |
| `rules/review.md` | 13,087 |
| `rules/maintenance.md` | 8,961 |
| `rules/doc-style.md` | 7,723 |
| `README.md` (not agent-loaded) | 2,123 |

### implement-it

| File | Characters |
| --- | ---: |
| `rules/verification.md` | 35,472 |
| `rules/commit-boundaries.md` | 23,656 |
| `rules/issue-closure.md` | 14,309 |
| `rules/review-gates.md` | 13,101 |
| `rules/sequencing.md` | 8,909 |
| `README.md` (not agent-loaded) | 2,307 |

`rules/verification.md` is the single largest supporting file among the six portable skills, and
`rules/commit-boundaries.md` is second — both are flagged in "Concrete reduction opportunities"
below.

### lab-it

| File | Characters |
| --- | ---: |
| `rules/plan-synthesis.md` | 12,853 |
| `README.md` (not agent-loaded) | 2,044 |

lab-it's only supporting file loads exclusively for the "Plan feature architecture" workflow, never
for a plain investigation-and-answer request.

### laravel-inertia-stack

| File | Characters |
| --- | ---: |
| `blueprints/resource-controller.md` | 9,881 |
| `rules/actions.md` | 8,726 |
| `blueprints/pest-testing.md` | 7,241 |
| `blueprints/filters-and-sorting.md` | 6,779 |
| `rules/test-ownership.md` | 4,394 |
| `rules/factories-and-seeders.md` | 3,994 |
| `rules/authorization.md` | 3,707 |
| `rules/resources.md` | 3,651 |
| `templates/.../TestingServiceProvider.php` | 3,115 |
| `rules/request-normalization.md` | 2,779 |
| `templates/.../QuerySorter.php` | 1,552 |
| `rules/migrations.md` | 1,572 |
| `rules/enum-options.md` | 1,516 |
| `templates/.../QueryFilter.php` | 1,272 |
| `rules/php-conventions.md` | 1,251 |
| `rules/eloquent-attributes.md` | 1,220 |
| `rules/query-conditionals.md` | 1,110 |
| `templates/.../Filterable.php` | 1,003 |
| `templates/.../Sortable.php` | 989 |
| `README.md` (not agent-loaded) | 2,005 |

This skill's own `SKILL.md` carries an explicit routing table naming exactly which of these files a
given task needs — already the model this document recommends other skills move toward (see
"Concrete reduction opportunities").

### plan-it

| File | Characters |
| --- | ---: |
| `rules/issue-conventions.md` | 19,940 |
| `rules/review.md` | 16,871 |
| `rules/discovered-work.md` | 10,833 |
| `rules/sequencing.md` | 10,561 |
| `rules/resource-feature-checklist.md` | 9,862 |
| `rules/design-reconciliation.md` | 6,542 |
| `rules/plan-md-input.md` | 6,540 |
| `rules/capability-checklist.md` | 4,960 |
| `rules/feature-classification.md` | 3,201 |
| `README.md` (not agent-loaded) | 1,851 |

`rules/resource-feature-checklist.md` and `rules/capability-checklist.md` are mutually exclusive per
request (`rules/feature-classification.md` picks one, never both); `rules/plan-md-input.md` and
`rules/discovered-work.md` are alternate entry routes, not both loaded for the same request.

### review-it

| File | Characters |
| --- | ---: |
| `rules/checklist.md` | 9,281 |
| `rules/scope.md` | 9,114 |
| `rules/verification.md` | 8,744 |
| `README.md` (not agent-loaded) | 2,652 |

All three rule files are consulted on essentially every invocation, per `SKILL.md`'s own "Rules"
list (scope first, then checklist, then verification) — review-it has no large conditional file a
typical review skips.

### ship-it

| File | Characters |
| --- | ---: |
| `rules/milestone-completion.md` | 38,807 |
| `rules/release.md` | 17,142 |
| `README.md` (not agent-loaded) | 1,902 |

`rules/milestone-completion.md` is the largest single file in the entire skill set, and covers three
distinct surfaces in one file — PR readiness, CI-failure investigation, and the closure gate (see
"Concrete reduction opportunities").

### Repository-wide total

All 57 files under `skills/`: **466,362 characters, ~116,591 rough tokens.** No real workflow loads
this whole figure at once — it is the sum across all seven skills' entrypoints, rules, blueprints,
templates, and READMEs, useful only as an upper bound against which the workflow estimates below
should be read.

## Estimated file-loading costs for representative workflows

Each estimate below names every file counted, in the order a workflow would actually reach it,
deduplicates a file reused more than once in the same pass (a file already loaded is not paid for
twice), and states its own assumptions. **Excluded from every estimate**, per the task's own scope:
application/project code the workflow reads or writes, prior conversation history, tool-call output
(command results, diffs, search results), and any external companion skill this repository does not
publish (Laravel Boost's `laravel-best-practices`, `testing-best-practices`,
`inertia-vue-development` — real cost when installed, but not measurable from this repository).
`README.md` files are excluded throughout: they are human-facing orientation, never read by the
agent while executing a workflow. `docs/skill-authoring-methodology.md` and
`docs/skill-consumption.md` are also excluded — they serve a skill's author or a project's installer,
not a running pipeline workflow, and are never loaded by `lab-it` → `ship-it` in the course of doing
their own work.

| Workflow | Files counted (in order) | Characters | Rough tokens |
| --- | --- | ---: | ---: |
| **review-it, standalone review** | `SKILL.md` (6,092) → `rules/scope.md` (9,114) → `rules/checklist.md` (9,281) → `rules/verification.md` (8,744) | 33,231 | 8,308 |
| **lab-it, investigation-and-answer only** | `SKILL.md` (7,545) — `rules/plan-synthesis.md` not reached; no `plan.md` was requested | 7,545 | 1,886 |
| **lab-it, plan feature architecture** | `SKILL.md` (7,545) → `rules/plan-synthesis.md` (12,853) | 20,398 | 5,100 |
| **document-it, new Markdown guide from already-sufficient evidence** | `SKILL.md` (13,844) → `rules/doc-style.md` (7,723) → `rules/review.md` (13,087); `lab-it` not routed to (evidence already sufficient) | 34,654 | 8,664 |
| **document-it, new Artifact guide** | same as above, plus `rules/template.html` (20,947) | 55,601 | 13,900 |
| **document-it, update routed through `lab-it` for stale evidence (cross-skill)** | `SKILL.md` (13,844) → `lab-it/SKILL.md` (7,545, cross-skill) → `rules/maintenance.md` (8,961) → `rules/review.md` (13,087) | 43,437 | 10,859 |
| **plan-it, one resource/CRUD feature, UI in scope, no prior `plan.md`** | `SKILL.md` (6,590) → `rules/feature-classification.md` (3,201) → `rules/resource-feature-checklist.md` (9,862) → `rules/design-reconciliation.md` (6,542) → `rules/issue-conventions.md` (19,940) → `rules/sequencing.md` (10,561) → `rules/review.md` (16,871); `rules/capability-checklist.md`, `rules/plan-md-input.md`, and `rules/discovered-work.md` are the unused alternates for this shape | 73,567 | 18,392 |
| **implement-it, one ordinary issue, no stack companion, cross-skill `review-it` call before Gate 1** | `SKILL.md` (10,106) → `rules/sequencing.md` (8,909) → `rules/review-gates.md` (13,101) → `rules/commit-boundaries.md` (23,656) → `rules/verification.md` (35,472) → `rules/issue-closure.md` (14,309) → `review-it/SKILL.md` (6,092, cross-skill) → `review-it/rules/scope.md` (9,114) → `review-it/rules/checklist.md` (9,281) → `review-it/rules/verification.md` (8,744); `sequencing.md` is read once and reused for both the pre-implementation branch check and the post-closure ready-set recompute | 138,784 | 34,696 |
| **implement-it, same issue, `laravel-inertia-stack` composed for one filtered-index task (cross-skill)** | everything in the row above, plus `laravel-inertia-stack/SKILL.md` (4,176, cross-skill), `blueprints/filters-and-sorting.md` (6,779), `rules/request-normalization.md` (2,779), and the four filter/sort templates (1,272 + 1,552 + 1,003 + 989 = 4,816) | 157,334 | 39,334 |
| **ship-it, PR-readiness check only** | `SKILL.md` (5,957) → `rules/milestone-completion.md` (38,807) | 44,764 | 11,191 |
| **ship-it, full PR-readiness → post-merge closure and release** | `SKILL.md` (5,957) → `rules/milestone-completion.md` (38,807, read once, reused for both the readiness check and the later closure gate) → `rules/release.md` (17,142) | 61,906 | 15,477 |

The largest single-workflow figure above (implement-it composed with the Laravel companion for one
task, ~39,334 rough tokens) is still roughly a third of the repository-wide total (~116,591 rough
tokens) — confirming that, even for a cross-skill, stack-composed pass, progressive disclosure keeps
real per-workflow cost well below "everything installed."

## Concrete reduction opportunities (proposals, not applied in this pass)

These are candidates for a future authoring pass under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md). None is applied here — this
task's scope is measurement and the one authorized metadata fix, not restructuring or shortening any
operational rule.

1. **Repair-history narration embedded inside an operational rule file.**
   `skills/implement-it/rules/commit-boundaries.md` carries five inline parentheticals citing
   `scenarios.md` while narrating *why* a step matters (e.g., "reproduced concretely: three separate
   hunks in one file: one unrelated hunk already staged, one unrelated hunk still unstaged, and the
   correction itself unstaged; the prior extraction-by-subtraction folded the unstaged unrelated hunk
   into the 'correction' and round-tripped anyway — see `scenarios.md`" at line 189). Across all five
   occurrences (lines 189, 199, 210, 248, 264) these parentheticals total roughly 600–650 characters
   of defect-history narration inside a file that loads on every commit-boundary consult, ordinary or
   corrective. **What could change:** shorten each to a bare citation (e.g., "(see `scenarios.md` for
   the reproduced failure)") and move the narrative detail entirely into `scenarios.md`, which already
   carries the full reproduction. **What must be preserved:** the operational instruction each
   parenthetical is attached to (the stop conditions, the positive-isolation requirement, the
   round-trip check) is unrelated to this trim and must not change; per
   `docs/skill-authoring-methodology.md` Section 4, "a compact example materially teaches the rule"
   can still justify keeping a short version rather than deleting it outright — the proposal is
   compression, not blanket removal.

2. **A large file bundling a common path with a rare, conditional sub-procedure.**
   `skills/implement-it/rules/commit-boundaries.md` is 23,656 characters; lines 1–148 (~8,418
   characters) cover ordinary commit-boundary derivation, consulted on every issue, while lines
   149–343 (~15,238 characters, roughly 64% of the file) are the history-reconstruction recipe used
   only when a correction must fold into an already-committed, not-yet-pushed commit — a materially
   rarer case than ordinary boundary derivation. **What could change:** route the reconstruction
   procedure to its own file (e.g. `rules/commit-reconstruction.md`), consulted only from
   `commit-boundaries.md`'s "Something already committed, correction needed before push" heading,
   so an ordinary issue's commit-building pass no longer pays for a procedure it never reaches.
   **What must be preserved:** the reconstruction procedure's own steps, its scratch-directory,
   positive-isolation, and classification-stop mechanics, and its cross-references to
   `rules/verification.md`'s stash-identity procedure — none of that changes, only which file owns it.

3. **A large file covering several distinct conditional surfaces.**
   `skills/ship-it/rules/milestone-completion.md` (38,807 characters, the largest file in this skill
   set) covers three surfaces its own `SKILL.md` already names as distinct — PR readiness (~124–192),
   PR creation (~194–252), CI-failure investigation and correction handoff (~253–338), and the
   closure gate (~348–437) — each with its own trigger condition. A ship-it session asked only "is
   this milestone ready for a PR" currently loads the closure-gate and CI-investigation mechanics it
   will not use this pass. Similarly, `skills/implement-it/rules/verification.md` (35,472 characters)
   bundles "Preserving unrelated worktree content during a Git rewrite" (~4,354 characters) and
   "Isolation verification" (~3,102 characters) — together ~21% of the file — into a file consulted on
   every ordinary verification pass, even though both sections are explicitly "a deliberate
   escalation, not the default." **What could change:** split each file along its own
   already-named conditional surfaces into separately routed files, cross-referenced from the owning
   `SKILL.md`'s "Rules" list exactly as it already distinguishes them in prose. **What must be
   preserved:** every gate, condition, and cross-reference currently stated — a split changes which
   file a reader opens, not what the rule says or when it applies.

4. **Duplicated explanation, checked and not found at repository scope.** README.md and SKILL.md
   pairs were compared across all seven skills for restated content (`docs/skill-authoring-
   methodology.md` Section 7 flags this as a known failure mode). No pair currently restates the
   other: each README explains lifecycle and reasoning in plain prose for a human maintainer, while
   each SKILL.md states the operational ownership and routing table an agent needs — the intended,
   complementary split. This is recorded as a checked-and-clear result, not a defect, so a future pass
   does not have to re-derive it.

## Metadata correction

`skills/review-it/SKILL.md`'s frontmatter `description` exceeded the Agent Skills specification's
1,024-character limit by 195 characters (1,219 measured; see `scenarios.md`'s META-01). It is
shortened to 966 characters in this pass — see `scenarios.md`'s append-only metadata-correction
record for the before/after text and the validation method.

All seven entrypoints' frontmatter were validated in this pass: each has exactly `name` and
`description` fields (no extra metadata fields, invocation controls, or dependencies were found or
added), each `name` matches its directory, and only `review-it`'s description exceeded the
1,024-character limit.

| Skill | Description characters | Within 1,024 limit |
| --- | ---: | --- |
| document-it | 553 | Yes |
| implement-it | 839 | Yes |
| lab-it | 641 | Yes |
| laravel-inertia-stack | 373 | Yes |
| plan-it | 716 | Yes |
| review-it | 966 (was 1,219) | Yes (was: No, by 195) |
| ship-it | 923 | Yes |

## Reproducing these numbers

```bash
# Discovery metadata: one skill's description length
python3 -c "
import re
content = open('skills/<name>/SKILL.md').read()
m = re.search(r'description: \"(.*?)\"\n', content, re.DOTALL)
print(len(m.group(1)))
"

# A single file's character count
wc -c skills/<name>/SKILL.md

# Every file under one skill, largest last
find skills/<name> -type f -exec wc -c {} + | sort -n

# Whole repository's skill content
find skills -type f -exec wc -c {} + | tail -1
```

Rough tokens throughout this document are the resulting character count divided by 4, rounded to
the nearest whole number — not a tokenizer run and not an observed session's actual usage.
