# v2.0.2 release preparation

**Status:** candidate patch; measurement-tool corrections approved at `4e7b247` after source review and focused executed checks.
The `document-it` authoring extraction below is **pending Control Room review** — not yet approved.
The release target, final notes, and publication are not approved.

Compared with [v2.0.1](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.1)
through [4e7b247](https://github.com/elieandraos/agentic-engineering/commit/4e7b2477cf2d26d5c411227cb33cf994c2d10ca1),
plus the `document-it` authoring extraction described below, pending review.
This is a short working record. Update it in place as work is reviewed; retain detailed history
in Git rather than appending correction reports.

## Candidate release content

- Simplified the [skill-context guide](docs/skill-context.md), replacing historical measurement
  tables with an explanation of the model and commands for generating current figures.
- Added a [measurement script](scripts/measure_skill_context.py) and
  [explicit workflow definitions](docs/skill-context-workflows.json) for per-skill, per-file,
  and modeled workflow breakdowns.
- Added [test-contracts.md](test-contracts.md): contributor-readable behavior contracts, descriptive
  approval names, concrete examples, and a framework-independent testing strategy alongside
  [scenarios.md](scenarios.md).
- Updated skill README links to the context model and reconciled the roadmap's published baseline.

These are documentation and maintainer-tooling changes. No runtime skill behavior has changed in
the compared range. The proposed v2.0.2 numbering assumes that scope remains a maintenance patch;
reassess if later work changes the release's scope.

## Reviewed measurement work

The script now counts actual files, deduplicates resolved file paths, reads descriptions only
from frontmatter, and decodes its supported quoted-scalar escapes. Unsupported description forms
fail explicitly. Git-ignored files are excluded when their status is known; unavailable ignore
or revision checks are reported honestly.

The guide and workflow config distinguish file measurements from modeled loading and observed
session consumption. The revision check detects uncommitted input changes only; it does not
validate workflow definitions after committed routing changes. Planning origins feed into
classification. Extraction candidates still need their callers and shared requirements checked
before implementation.

Further conditional extractions are candidates only. None is implemented or included in this
release scope yet. Existing deferred ecosystem findings are not resolved by these documentation
and measurement changes.

## document-it authoring extraction (pending Control Room review)

Extracted `document-it`'s format-selection, new-guide-writing, and existing-guide-update
procedures out of `SKILL.md` into a new `rules/authoring.md`, per
`docs/skill-authoring-methodology.md`. `SKILL.md` now states only each procedure's triggering
condition and hands off; activation, conditional routing, evidence reuse, ownership, the shared
output non-negotiables, and "Maintaining both formats" stay in `SKILL.md` unchanged. Reconciled the
callers this touches: `rules/maintenance.md`'s and `rules/review.md`'s cross-references,
`rules/doc-style.md`'s responsibility-routing list, the skill `README.md`'s context-consumption
note, and `artifacts/document-it.md`'s format-selection section and rule-ownership table. Updated
`docs/skill-context-workflows.json`: added `rules/authoring.md` to the three existing
new-guide/update workflow rows, and added two new rows — a standalone single-Markdown-guide review
and a standalone paired-guide review — to demonstrate that review-only workflows never load the
extracted writing procedures. Updated `docs/skill-context.md`'s `document-it` note to match, with
no new historical measurement table added to that guide.

Evidence: a line-level diff between the original `SKILL.md` sections and the new
`rules/authoring.md` showed only the two relocated trigger sentences and three cross-references
necessarily repointed (to `SKILL.md`'s "Maintaining both formats," to `SKILL.md`'s "Output-specific
non-negotiables," and an internal same-file "below") — no other wording changed. Both trigger
sentences were confirmed to remain verbatim in `SKILL.md`. All Markdown links in the seven touched
files resolve; `git diff --check` is clean; `SKILL.md`'s frontmatter `description` is unchanged at
553 characters. `scripts/measure_skill_context.py` runs clean against the new file list. Measured
character counts (before -> after): `SKILL.md` 13,742 -> 7,793 (-43%); modeled "new Markdown guide"
workflow 34,388 -> 35,926; "new Artifact guide" 55,301 -> 56,839; "reconcile existing Markdown
guide" 50,788 -> 52,450 (each +4-8% from the added `rules/authoring.md` load); a standalone-review
workflow's equivalent total (`SKILL.md` + `rules/review.md`) 26,743 -> 20,868 (-22%), since review
workflows never load the new file. These are modeled workflow totals per
`docs/skill-context.md`'s three-tier framework, not observed session usage. Preservation was traced
statically across seven scenarios — new Markdown, new Artifact, both formats, existing-path update,
inaccessible Artifact, an explicitly single-format update, and standalone Markdown/paired review —
by reading the moved and reconciled text; no live skill invocation was run.

## Validation to retain

Control Room executed 23 focused checks against the corrected script at `4e7b247`, using
disposable Git fixtures and a source snapshot. They covered optional README counts, path aliases,
Unicode and escaped descriptions, unsupported forms and body lookalikes, missing/ignored files,
revision reporting, and command output. All passed.

All 17 configured workflow totals matched independent arithmetic; repeated reports were
byte-identical. The unchanged skill snapshot totals 479,415 Unicode characters across 62 files.
These checks establish accounting and reporting behavior, not that every modeled file list
matches an agent's actual loading.

The test-contract catalogue covers all 47 original scenarios plus additional lifecycle and repair
contracts. Its links, identifiers, scenario coverage, and descriptive approval wording were
checked. It is a specification, not an implemented automated suite or a record of passing agent
tests.

No live skill execution, consumer update, browser validation, or runtime context-usage benchmark
was performed by this work. These are evidence limits, not new publication requirements.

## Finalization

After any separately approved extraction work is complete, reconcile the final diff against v2.0.1, select the
exact release target, and prepare short technical notes stating what changed and what was verified.
Publication remains a separate explicit decision.
