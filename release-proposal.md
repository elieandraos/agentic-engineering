# v2.0.2 release preparation

**Status:** candidate patch; measurement-tool corrections and Control Room review are pending.
The release target, final notes, and publication are not approved.

Compared with [v2.0.1](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.1)
through [e98bb1f](https://github.com/elieandraos/agentic-engineering/commit/e98bb1f81b611884bfc95b0d78d7df83300b90ac).
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

## Work still pending review

The measurement script is committed, but its first version is not yet approved:

- Correct actual-file counts, path-identity deduplication, and frontmatter description parsing.
- Make revision-consistency claims match the measured file inventory; unavailable Git status must
  remain unknown rather than being reported clean.
- State loading and README exclusions as model assumptions, remove claims of detecting stale
  committed workflow definitions, and correct the planning-entry routing explanation.
- Re-run the focused fixtures and reconcile the extraction shortlist's callers and conditional
  savings before treating it as an implementation proposal.

Further conditional extractions are candidates only. None is implemented or included in this
release scope yet. Existing deferred ecosystem findings are not resolved by these documentation
and measurement changes.

## Validation to retain

The initial script was executed against f9462dd. All 17 configured workflow totals matched
independent arithmetic, and repeated output was identical. Focused fixtures also reproduced the
accounting, description-parsing, and revision-reporting defects listed above; these checks do not
validate corrections that have not yet landed.

The test-contract catalogue covers all 47 original scenarios plus additional lifecycle and repair
contracts. Its links, identifiers, scenario coverage, and descriptive approval wording were
checked. It is a specification, not an implemented automated suite or a record of passing agent
tests.

No live skill execution, consumer update, browser validation, or runtime context-usage benchmark
was performed by this work. These are evidence limits, not new publication requirements.

## Finalization

After the pending corrections are reviewed, reconcile the final diff against v2.0.1, select the
exact release target, and prepare short technical notes stating what changed and what was verified.
Publication remains a separate explicit decision.
