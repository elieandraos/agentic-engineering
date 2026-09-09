# v2.0.2 release preparation

**Status:** candidate patch; measurement-tool corrections approved at `4e7b247` after source review and focused executed checks.
The release target, final notes, and publication are not approved.

Compared with [v2.0.1](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.1)
through [4e7b247](https://github.com/elieandraos/agentic-engineering/commit/4e7b2477cf2d26d5c411227cb33cf994c2d10ca1).
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
