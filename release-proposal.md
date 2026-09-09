# v2.0.2 release preparation

**Status:** candidate patch; measurement-tool corrections approved at `4e7b247` after source review and focused executed checks.
The `document-it` authoring extraction is approved at `8ceb238` after source review and independent character-count verification.
The `implement-it` activation-ordering extraction below is **pending Control Room review** — not yet approved.
The release target, final notes, and publication are not approved.

Compared with [v2.0.1](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.1)
through [4e7b247](https://github.com/elieandraos/agentic-engineering/commit/4e7b2477cf2d26d5c411227cb33cf994c2d10ca1),
plus the `document-it` authoring extraction reviewed at [8ceb238](https://github.com/elieandraos/agentic-engineering/commit/8ceb238178d3a5979cea371f6a7aba1d2f97b868),
plus the `implement-it` activation-ordering extraction described below, pending review.
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

The `document-it` authoring extraction and the `implement-it` activation-ordering extraction below
are the only extractions implemented so far. Further conditional extractions remain candidates
only, not implemented or included in this release scope. Existing deferred ecosystem findings are
not resolved by these documentation and measurement changes.

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

## implement-it activation-ordering extraction (pending Control Room review)

Extracted `implement-it`'s "Ordering commits to keep intermediate states valid" section, including
its "Relationship to dependency ordering" subsection, out of `rules/verification.md` into a new
`rules/activation-ordering.md`, per `docs/skill-authoring-methodology.md`. Scope is unchanged:
configuration, feature flags, environment-conditioned behavior, and other runtime activation gates
generally — not only explicit feature flags. `verification.md` keeps the activation-risk trigger
stated in place (what to watch for while building commits) and hands off to the extracted file only
once a commit being built actually activates such a gate; ordinary dependency ordering and
intermediate-state coherence remain required for every commit plan regardless. Testing policy,
approvals, reconstruction, and preservation mechanics are unchanged; the reproducible-install
section was not touched. Reconciled the callers this touches: `rules/commit-boundaries.md`'s step 6
(dependency ordering, with the conditional handoff to the new file), `rules/review-gates.md`'s
Gate 2 plan-description bullet, `SKILL.md`'s Rules list (new bullet, and `verification.md`'s bullet
reworded to describe flagging rather than owning the procedure), `verification.md`'s own "Isolation
verification" trigger example (repointed from an internal "below" to the new file), the skill
`README.md`'s context-consumption note (nine rule files, four conditional escalations, and
activation-ordering's relationship to the isolation escalation), and `artifacts/implement-it.md`'s
§5 commit-architecture summary, §6 verification-model summary, and §11 rule-ownership table.
Updated `docs/skill-context-workflows.json`: renamed and re-scoped the three implement-it workflow
rows to state their activation-change assumption explicitly (ordinary work with no activation
changes; activation-dependent commit ordering with its required isolation verification; and
reconstruction with no activation changes), and added `rules/activation-ordering.md` to the
activation-dependent row only. Updated `docs/skill-context.md`'s `implement-it` note to match, with
no new historical measurement table added to that guide.

Evidence: a line-level diff between the original `verification.md` section and the new
`rules/activation-ordering.md` showed the extracted body (the watch-for paragraph, the four-step
procedure, the underlying-principle quote, the worked example, and the "Relationship to dependency
ordering" subsection) is byte-identical to the source, with only a new "When this applies" section
prepended and a new "Relationship to isolation verification" section appended — no other wording
changed in the moved content. `verification.md`'s own remaining text has three changes: its opening
ownership paragraph now names `rules/activation-ordering.md`, its "Isolation verification" trigger
example is repointed from an internal "below" cross-reference to the extracted file, and the
extracted section is replaced with a short routing stub that keeps the activation-risk trigger and
scope statement visible without restating the procedure. All Markdown/backtick file references in
the nine touched files resolve; `git diff --check` is clean; `SKILL.md`'s frontmatter `description`
is unchanged at 839 characters. `scripts/measure_skill_context.py` runs clean against the updated
file lists. Measured modeled-workflow character counts (before extraction -> after, source revision
`7ead845`): "ordinary issue, no activation changes" 119,958 -> 119,448 (-0.4%, from
`verification.md` shrinking with no new file loaded on this path); "activation-dependent ordering
with its required isolation verification" 126,589 -> 129,344 (+2.2%, `verification.md`'s reduction
offset by the added `rules/activation-ordering.md` load — routing overhead, not duplicated content);
"unpublished-history reconstruction, no activation changes" 141,406 -> 140,896 (-0.4%, same
reduction as the ordinary path, no new file loaded). These are modeled workflow totals per
`docs/skill-context.md`'s three-tier framework, not observed session usage. Behavior was traced
statically across four scenarios by reading the moved and reconciled text, not by a live skill
invocation: ordinary dependency ordering with no activation gate (never reaches the extracted file,
per its own "When this applies" entry condition); activation revealing an unrelated pre-existing
test (the extracted procedure's step 2, preserved verbatim); activation preceding a commit it
depends on (steps 3-4 and the worked example, preserved verbatim); and an unresolved conflict
between dependency ordering and activation ordering (the preserved "Relationship to dependency
ordering" subsection's routing to `rules/review-gates.md`'s "when to stop and ask," itself
unchanged by this extraction).

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
