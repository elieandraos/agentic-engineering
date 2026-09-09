# Skill Context Consumption

How much of a request budget this repository's skills actually spend, and how to measure it
yourself. This document explains the model; it does not carry a manually maintained table of
current figures — those drift every time a rule file changes, so generate them instead of reading
a stale copy here.

**Authority boundary.** This document measures and models context cost; it does not change any
skill's operational rules, gates, or approvals. A reduction it identifies as worth investigating is
inert until a separate authoring pass implements it under
[`docs/skill-authoring-methodology.md`](skill-authoring-methodology.md).

## Three loading tiers (a model, not an observed runtime guarantee)

Nothing here has been confirmed against a real agent session's actual context. What follows is the
working model this document and its script use to reason about cost — installing a skill is
assumed not to load its whole directory, with three distinct tiers assumed to enter context at
three different times:

1. **Discovery metadata** — each installed skill's frontmatter `description` (and `name`), assumed
   read by the agent to decide which skill, if any, applies to the current request. Modeled as the
   only cost an *inactive* skill has, paid for every installed skill, not only the one that ends up
   activating — a per-session tax that scales with how many skills are installed, under this model.
2. **Activated `SKILL.md`** — once a skill is selected, its complete `SKILL.md` (frontmatter plus
   body) is assumed to load as one unit: the operational routing entrypoint stating activation
   vocabulary, ownership, and the routing table to supporting files. This document assumes nothing
   in a `SKILL.md` loads partially, so a large entrypoint is modeled as costing its full size on
   every activation of that skill, regardless of which workflow the request turns out to need —
   that assumption is not independently verified here.
3. **Supporting files, on demand** — a `rules/`, `blueprints/`, or `templates/` file is assumed to
   load only when the activated `SKILL.md`'s own routing, or a supporting file's own further
   routing, sends the current workflow to it. Under this assumption, a skill with many rule files
   does not load all of them for every request; it loads the ones the request's own shape requires.
   That set is not always one file per concern — a mixed-characteristic feature or a blueprint with
   its own internal routing can pull in more than the primary table entry alone, and a followed
   cross-reference into another file's shared guidance is modeled as adding that file's full size,
   not just the cited section.

## How to read the figures

**Unit: Unicode characters, not bytes.** Every count is `len()` on a file's content after UTF-8
decoding — the same unit the Agent Skills specification's 1,024-character `description` limit
uses. This repository's prose uses multi-byte UTF-8 punctuation (em dashes, curly quotes) heavily
enough that a raw byte count (`wc -c`) is consistently larger and not interchangeable with the
character counts this document and its script report.

**Rough tokens = characters ÷ 4, always.** A coarse, checkable approximation, not a Claude
tokenizer count and not an observed session's actual usage — real tokenization varies with content.

**Three different kinds of figure exist. Keep them separate:**

- **A file measurement** — a direct reading of one file's current size. Always current at the
  moment you run the script.
- **A modeled workflow estimate** — a sum of file measurements standing in for a hypothetical
  loading sequence, under an explicit, hand-maintained file list
  ([`docs/skill-context-workflows.json`](skill-context-workflows.json)) and three stated modeling
  assumptions, none of them an observed or guaranteed runtime mechanic: **whole-file reads** (a
  file that gets opened is assumed to contribute its complete size, never a partial section);
  **deduplication** of a file already opened earlier in the same modeled pass; and **README
  exclusion by default** (a `SKILL.md` that doesn't mention `README.md` is assumed to give an agent
  no reason to open it mid-workflow — an assumption about likely behavior, not a proof that no
  session ever opens it). No instrumentation of a real session backs these totals.
- **Observed session consumption** — an actual agent session's measured token usage. This
  repository has none of this: nothing here has been benchmarked against a real run, and neither
  this document nor its script claims otherwise.

**A larger number identifies where to look, not a verdict.** A large supporting file, or a large
modeled-workflow total, tells you which skill or rule file is worth investigating for a possible
split — it is not, by itself, evidence that the skill performs poorly, that an agent struggled with
it, or that the split is worth making once routing overhead and cross-references are accounted for
(see `docs/skill-authoring-methodology.md` Section 4's evidence-to-rule bar, which applies equally
to evidence for *removing* content). Treat these figures as a prioritization signal for where a
future authoring pass should look first, not as a defect report.

## Generating current figures

```bash
python3 scripts/measure_skill_context.py
```

Prints, read-only: the source revision and whether the `skills/` tree or the workflow config has
uncommitted changes since it; discovery-metadata totals; a compact per-skill table separating
entrypoint size from supporting-file size; the repository-wide total; and every modeled workflow
total from `docs/skill-context-workflows.json`.

```bash
python3 scripts/measure_skill_context.py --detail <skill-name>   # full file-by-file breakdown
python3 scripts/measure_skill_context.py --detail all            # every skill's breakdown
python3 scripts/measure_skill_context.py --workflow "<name>"     # one workflow's file list and running total
```

The script fails clearly, with a non-zero exit, if a workflow's configured file list names a path
that doesn't exist. It never writes or modifies a file.

`docs/skill-context-workflows.json` is a hand-maintained, explicit list of representative
workflows, seeded from this document's own prior workflow modeling and checked against each
skill's `SKILL.md` routing at the time it was last edited. It is not derived by recursively
following Markdown links or crawling directories — an actual `SKILL.md` can route conditionally,
compose across skills, or follow a further cross-reference inside a supporting file, none of which
a link crawl would resolve correctly.

**What the script's revision check does and does not establish.** It reports whether the working
tree's `skills/` content and the workflow config differ from `git HEAD` right now — an uncommitted-
change check, nothing more. It does not know when the config file was last reconciled against
routing, and it cannot tell you whether a routing change that was already committed and merged
cleanly has since made a listed workflow stale — a fully committed, clean working tree will still
report "measured inputs match this revision" even if a skill's routing changed three commits ago
and nobody updated the config to match. Detecting that kind of staleness is not something this
script does; it would require tracking which commit last reconciled the config against routing, and
no such mechanism exists here. Update the config file directly whenever you change a skill's
routing, and treat "measured inputs match this revision" as "the working tree is clean," not as "the
workflow definitions are still accurate."

The config also records, per workflow, the assumptions behind it (e.g. which citation is
conditional versus mandatory) and excludes content this repository cannot measure: external
companion skills (Laravel Boost's `laravel-best-practices`, `testing-best-practices`, and
`inertia-vue-development`; the `artifact-design` skill `document-it` requires before writing an
Artifact page), and `docs/skill-authoring-methodology.md`/`docs/skill-consumption.md` themselves,
which no `SKILL.md` or rule file references.

## Per-skill notes

The sections below exist to anchor stable links from each skill's own `README.md`
("Context consumption"). Run the script for current numbers; each note below states only what
isn't already obvious from the size table — a routing detail that changes what a workflow's total
actually includes.

### document-it

`rules/authoring.md` owns format selection and the new-guide/existing-guide-update procedures;
`SKILL.md` states only each workflow's trigger condition and hands off to it. `rules/template.html`
(the Artifact scaffold) is the largest supporting file and loads only for Artifact output, never
for a Markdown guide. `rules/maintenance.md` and `rules/review.md` both route back to
`rules/doc-style.md` for how a change gets written, so a guide update can load more than its own
primary rule file. A standalone review reaches only `rules/review.md` — it never loads
`rules/authoring.md`, since reviewing a guide needs no writing procedure. See the `document-it`
rows in `skill-context-workflows.json`, including the two standalone-review rows.

### implement-it

`rules/verification.md` is the largest single file in the skill set and loads on every ordinary
pass. `rules/isolation-verification.md`, `rules/worktree-preservation.md`, and
`rules/commit-reconstruction.md` are conditional escalations layered on top of it — see the three
`implement-it` workflow variants (ordinary, isolation-triggered, reconstruction) in
`skill-context-workflows.json` for what each actually adds. `implement-it/SKILL.md`'s "Entry
contract" names `plan-it/rules/issue-conventions.md` and `rules/review.md` to describe the quality
bar an approved issue already meets; the ordinary path does not re-open either file, so they are
not counted in the modeled `implement-it` workflows.

### lab-it

The only supporting file, `rules/plan-synthesis.md`, loads exclusively for the "Plan feature
architecture" workflow — a plain investigation-and-answer request never reaches it.

### laravel-inertia-stack

`blueprints/filters-and-sorting.md`'s own "Testing" section routes further to
`rules/test-ownership.md` and `blueprints/pest-testing.md`; its "Naming and location" section
separately cites `rules/php-conventions.md`. A filtered-index task composed with `implement-it`
therefore reaches more files than the routing table's own single row names — see the composed
`implement-it` + `laravel-inertia-stack` workflow in `skill-context-workflows.json`.

### plan-it

`rules/resource-feature-checklist.md` and `rules/capability-checklist.md` are chosen by
`rules/feature-classification.md`'s shape classification, but a mixed-characteristic feature can
load both, per that file's own secondary-questions allowance. `rules/plan-md-input.md` (an approved
`plan.md` origin) and `rules/discovered-work.md` (an unexpected-finding origin) are earlier pipeline
steps that feed into classification, not routes that replace or skip it — per `SKILL.md`'s own
numbered pipeline, both origins still reach `rules/feature-classification.md` and the same
canonical-issue pipeline from there. A request with neither origin (a feature ask stated directly
in conversation) enters straight at classification, which is what the modeled `plan-it` rows in
`skill-context-workflows.json` assume; no workflow row there models the plan-md-input or
discovered-work paths.

### review-it

All three rule files (`scope.md`, `checklist.md`, `verification.md`) are consulted on essentially
every invocation, in the order `SKILL.md`'s own "Rules" list states — this skill has no large
conditional file a typical review skips.

### ship-it

`rules/milestone-completion.md` owns the shared delivery-lifecycle entry map and the closure gate;
`rules/milestone-pr-readiness.md` and `rules/ci-failure-correction.md` own the two earlier,
narrower surfaces and each cite `milestone-completion.md`'s shared guidance conditionally rather
than restating it. `rules/ci-failure-correction.md`'s own step 3 unconditionally directs consulting
`implement-it/rules/review-gates.md`, which the CI-failure-investigation workflow row therefore
counts as mandatory, not merely conditional.

## Frontmatter validation

The Agent Skills specification limits a skill's frontmatter `description` to 1,024 characters. The
script's discovery-metadata totals report each skill's current length; check a new or edited
`description` against that limit before publishing it; this document does not track compliance
separately.
