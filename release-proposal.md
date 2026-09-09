# v2.0.2 release preparation

**Status:** candidate patch; measurement-tool corrections approved at `4e7b247` after source review and focused executed checks.
The `document-it` authoring extraction is approved at `8ceb238` after source review and independent character-count verification.
The `implement-it` activation-ordering extraction is approved at `6454751` after source review and independent measurement.
The `ship-it` milestone-guidance split below is **pending Control Room review** — not yet approved.
The release target, final notes, and publication are not approved.

Compared with [v2.0.1](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.1)
through [4e7b247](https://github.com/elieandraos/agentic-engineering/commit/4e7b2477cf2d26d5c411227cb33cf994c2d10ca1),
plus the `document-it` authoring extraction reviewed at [8ceb238](https://github.com/elieandraos/agentic-engineering/commit/8ceb238178d3a5979cea371f6a7aba1d2f97b868),
plus the `implement-it` activation-ordering extraction reviewed at [6454751](https://github.com/elieandraos/agentic-engineering/commit/64547517d081eed15f286e445a031569d4aced8d),
plus the `ship-it` milestone-guidance split described below, pending review.
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

The `document-it` authoring extraction, the `implement-it` activation-ordering extraction, and the
`ship-it` milestone-guidance split below are the only extractions implemented so far. Further
conditional extractions remain candidates only, not implemented or included in this release scope.
Existing deferred ecosystem findings are not resolved by these documentation and measurement
changes.

## document-it authoring extraction (approved at 8ceb238)

Extracted `document-it`'s format-selection, new-guide-writing, and existing-guide-update
procedures out of `SKILL.md` into a new `rules/authoring.md`, per
`docs/skill-authoring-methodology.md`. `SKILL.md` now states only each procedure's triggering
condition and hands off; activation, conditional routing, evidence reuse, ownership, the shared
output non-negotiables, and "Maintaining both formats" stay in `SKILL.md` unchanged. The new-guide
trigger is a user's explicit request for a new guide — an existing guide for the same capability
does not block that request; existing-guide-update identity preservation (same file path, same
`url`/favicon) is unaffected. Reconciled the callers this touches: `rules/maintenance.md`'s and
`rules/review.md`'s cross-references, `rules/doc-style.md`'s responsibility-routing list, the skill
`README.md`'s context-consumption note, and `artifacts/document-it.md`'s format-selection section
and rule-ownership table. Updated `docs/skill-context-workflows.json`: added `rules/authoring.md`
to the three existing new-guide/update workflow rows, and added two new rows — a standalone
single-Markdown-guide review and a standalone paired-guide review — each stating the assumption its
two-file estimate rests on: current evidence and the checklist answer every question without
consulting further guidance. Consulting an owning reference such as `rules/maintenance.md` does not execute its procedure.
Under the whole-file model, however, opening an additional file increases the estimate; the
two-file figure applies only while its stated assumptions hold. Updated `docs/skill-context.md`'s
`document-it` note to match, with no new historical measurement table added to that guide.

Evidence: a line-level diff between the original `SKILL.md` sections and the new
`rules/authoring.md` showed only the two relocated trigger sentences and three cross-references
necessarily repointed (to `SKILL.md`'s "Maintaining both formats," to `SKILL.md`'s "Output-specific
non-negotiables," and an internal same-file "below") — no other wording changed; the extracted
procedures themselves are unchanged by this correction. Both trigger sentences were confirmed to
remain verbatim in `SKILL.md`. All Markdown links in the touched files resolve; `git diff --check`
is clean; `SKILL.md`'s frontmatter `description` is unchanged at 553 characters.
`scripts/measure_skill_context.py` runs clean against the file lists. Measured character counts
(before extraction -> current, recalculated after this correction): `SKILL.md` 13,742 -> 7,923
(-42%); modeled "new Markdown guide" workflow 34,388 -> 36,056 (+4.9%); "new Artifact guide"
55,301 -> 56,969 (+3.0%); "reconcile existing Markdown guide" 50,788 -> 52,580 (+3.5%) — each
increase from the added `rules/authoring.md` load, now slightly larger than the extraction's
original +4.5%/+2.8%/+3.3% because this correction's new-guide-trigger rewording added characters
to `SKILL.md`. The two standalone-review rows' two-file total (`SKILL.md` + `rules/review.md`)
moved 26,743 -> 20,998 (-21.5%) under the stated assumption above. These are modeled workflow totals
per `docs/skill-context.md`'s three-tier framework, not observed session usage. Preservation was
traced statically across seven scenarios — new Markdown, new Artifact, both formats, existing-path
update, inaccessible Artifact, an explicitly single-format update, and standalone Markdown/paired
review — by reading the moved and reconciled text; no live skill invocation was run. This bounded
correction pass specifically re-verified the new-guide-despite-existing-guide request, an ordinary
existing-guide update, and the assumption stated by both review rows.

## implement-it activation-ordering extraction (approved at 6454751)

Moved the activation-ordering procedure from `rules/verification.md` into
`rules/activation-ordering.md`. Callers retain the runtime-activation check and conditionally
route to the procedure. Structural dependency ordering remains universal; `verification.md`
continues to own isolation-verification eligibility. Callers, summaries, the dossier, and workflow
definitions are reconciled.

Control Room confirmed the original 2,067-character section is preserved exactly against
`7ead845`, including existing-test inspection and the unresolved-ordering-conflict stop.
Frontmatter, reproducible-install guidance, pre-implementation-approval verification,
completed-issue reuse, and the isolation/reconstruction/preservation mechanics are unchanged.
Routing was reviewed in source; the measurement script and independent arithmetic reproduced
these equivalent workflow totals:

| Modeled path | Before (7ead845) | After (6454751) | Change |
|---|---:|---:|---:|
| Ordinary work, no activation changes | 119,958 | 119,300 | −658 characters |
| Activation-dependent ordering with required isolation | 126,589 | 128,779 | +2,190 characters |
| Reconstruction, no activation changes | 141,406 | 140,748 | −658 characters |

The ordinary-path reduction is modest. On the activation path, the new file adds 2,848 characters
while the shared files are 658 characters smaller in total, producing the 2,190-character increase.
The overhead therefore comes from the combined extraction and routing changes, not solely the
new file's introductory sections. These are modeled unique-file text totals, not observed session
consumption or evidence of an overall performance improvement. No live skill invocation was run.

## ship-it milestone-guidance split (pending Control Room review)

Moved `rules/milestone-completion.md`'s shared delivery-lifecycle entry map, what counts as a
delivery/phase milestone, the Backlog exemption, the milestone description as scope contract, and
why closure and release don't gate each other into a new `rules/milestone-lifecycle.md`, per
`docs/skill-authoring-methodology.md`. `milestone-completion.md` keeps closure eligibility, the
post-merge-authorization check, the validated closure mutation, interrupted-attempt recovery, and
reporting; its own condition 1 (delivery/phase milestone, not Backlog) now routes to the new file
instead of restating the definition. Every condition and approval boundary is preserved: closure
still requires applicable post-merge authorization plus freshly checked eligibility, and reading the
shared guidance authorizes no mutation. Reconciled the callers this touches: `milestone-pr-readiness.md`'s
and `ci-failure-correction.md`'s cross-references into the moved sections, `release.md`'s two
"Milestone closure and release do not gate each other" citations, the skill `SKILL.md`'s Rules list
(new bullet, `milestone-completion.md`'s bullet narrowed to the closure gate), the `README.md`'s
context-consumption note (five rule files instead of four), and `artifacts/ship-it.md`'s §7
rule-ownership table. `plan-it`'s `rules/issue-conventions.md` and `implement-it`'s
`rules/issue-closure.md`/`rules/sequencing.md` were inspected; their existing references already
name whichever file still owns the cited content and needed no change. Updated
`docs/skill-context-workflows.json`: the PR-readiness "broader estimate" row now adds
`rules/milestone-lifecycle.md` instead of `rules/milestone-completion.md`; the "post-merge closure
only" row now adds `rules/milestone-lifecycle.md` too, since closure's own eligibility check depends
on it; and the "full delivery happy path" row lists both files. The "local files only" PR-readiness
row and the CI-failure-investigation row are unchanged, since neither ever required the shared
guidance unconditionally. Updated `docs/skill-context.md`'s `ship-it` note to match, with no new
historical measurement table added to that guide.

A bounded correction pass fixed several remaining defects and reduced the split's overhead.
Stale references left pointing at their pre-split location were corrected: `release.md`'s and
`milestone-lifecycle.md`'s "Milestone closure and release do not gate each other" citations
(one still said "that rule"/"this rule's closure gate," another still said "below," when the
target moved to a different file), and two "either gate below"/"Both branches below" phrasings
whose "below" no longer resolved anywhere in that file. `milestone-lifecycle.md`'s own "What this
file does not do" was corrected to say `ci-failure-correction.md` secures the human's
authorization for a correction, not that it authorizes one itself — only the human authorizes.
The same pass trimmed both files' added ownership/dependency/non-goal prose (the Principle's
scope statement, Cross-rule dependencies, and What-this-file/rule-does-not-do sections) into
concise owner references, touching none of the moved substantive guidance, the closure gate's
three conditions, the mutation/recovery/validation steps, or reporting.
`docs/skill-context-workflows.json`'s CI-failure-investigation row was reworded from a categorical
"never needs" claim to a stated modeling assumption (no additional lifecycle guidance consulted on
that path), with its minimal file list unchanged.

Evidence: re-reading both files confirms the closure gate's three conditions, the closing
procedure's five steps (including interrupted-attempt recovery and re-fetch validation), and
reporting are unchanged from the prior pass; the Backlog exemption and delivery-milestone
recognition are unchanged text, only referenced by corrected pointers. All Markdown/backtick file
references in the four touched files resolve; `git diff --check` is clean.
`scripts/measure_skill_context.py` runs clean against the updated file lists. Measured
modeled-workflow character counts (source revision `51589b2` -> after this correction):

| Modeled path | Before (51589b2) | After | Change |
|---|---:|---:|---:|
| PR readiness and authorized creation, local files only | 21,241 | 21,583 | +342 characters |
| PR readiness, broader estimate (shared guidance consulted) | 42,064 | 34,002 | −8,062 characters |
| CI-failure investigation and correction handoff | 28,947 | 29,237 | +290 characters |
| Post-merge closure only | 27,670 | 30,827 | +3,157 characters |
| Full delivery happy path | 59,116 | 62,418 | +3,302 characters |

`milestone-completion.md` and `milestone-lifecycle.md` combined are now 23,742 characters (11,323 +
12,419), down from the prior pass's 25,908 and up from the original single file's 20,823. The
post-merge-closure and full-delivery paths still grow, because closure's own eligibility check
(is this a delivery/phase milestone, not Backlog) genuinely depends on `milestone-lifecycle.md`
now — real routing overhead, not padding — but by less than before, since the added prose
carrying that dependency is tighter. The PR-readiness broader-estimate saving is larger than
before, since the file it now loads instead of the old closure-mechanics-laden
`milestone-completion.md` is itself smaller. These are modeled workflow totals per
`docs/skill-context.md`'s three-tier framework, not observed session usage. No live skill
invocation, browser validation, or runtime context-usage benchmark was performed.

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
