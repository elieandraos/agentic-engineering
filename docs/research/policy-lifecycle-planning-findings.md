# Policy lifecycle planning findings

> **Status:** candidates for evaluation, captured 2026-11-02 from useOrbit's policy lifecycle
> planning and draft-issue review. Compared with `improve-2.2.3` at
> `e2b1918d8a13fca725427d414917c05e07541feb`. No skill changes are promoted by this record.

## Evidence and limits

The owner supplied the approved plan and the complete six-issue draft set during a review session.
The findings below concern those drafts, before GitHub creation or application implementation.
The session also inspected current useOrbit code, including
[`PolicyValidationRules::policyRules()`](https://github.com/elieandraos/useOrbit/blob/main/app/Concerns/PolicyValidationRules.php).

Evidence is one initiative in one project. The exact installed skill version and execution trace of
the drafting session were not verified. A missed finding does not establish that the current
canonical guidance lacks the rule, or that a new instruction would prevent recurrence. Distinguish
literal draft inconsistencies, a code-backed reuse hazard, and a newly resolved product question.

## Candidate classification

| Finding | Evidence | Likely owner | Current guidance and candidate disposition |
| --- | --- | --- | --- |
| Renewal-tag criteria checked only the outgoing link, although a policy can also have an incoming link | Literal inconsistency in draft issue 3 | `plan-it/rules/review.md` | Semantic correctness and approved-decision fidelity already apply. Evaluate a narrow relationship-state check within that review; do not add a universal chain checklist. |
| Reusing update validation for a new record could exempt the source record from uniqueness | Code-backed hazard in draft issue 4's proposed reuse; not an observed runtime failure | `plan-it` semantic review; framework mechanics remain framework-owned | Current-source authority is established in `rules/plan-md-input.md`. Evaluate checking operation-specific assumptions when an issue relies on reuse. No new Laravel uniqueness convention is justified. |
| An acceptance criterion's “exactly when” eligibility omitted restrictions stated in its own Context | Literal inconsistency in draft issue 4 | `plan-it/rules/review.md` | Existing semantic/body review should catch contradictory guarantees. Treat as an execution miss first; evaluate a small clarification only if it improves detection. |
| Editable dates had field-to-field validation but no stated relationship to the source policy's term | Product question exposed during draft review | `lab-it/rules/plan-synthesis.md` primarily; `plan-it` as a downstream check | Both skills already prohibit hiding material decisions as implementation details. Evaluate prompting for source-relative constraints when a workflow derives a new record from an existing one. The actual date restriction stays project knowledge. |

## 1. Relationship direction and position

Draft issue 3 required a “Renewal of…” tag on a renewal, but also said:

> A policy with no renewal, or whose only renewal is Cancelled, shows no tag.

The latest term has no outgoing renewal, yet still has a predecessor and must show its incoming
tag. A middle term can carry both tags while retaining one displayed status. The correction was to
evaluate the two directions independently and cover the standalone, first, middle and latest terms
where those states affect the behavior.

**Possible refinement:** when an issue's guarantees depend on directional relations, exercise the
material relation combinations against its literal criteria. A missing outgoing relation must not
silently imply the absence of an incoming one. Keep this conditional on the feature; not every issue
needs a relationship matrix.

## 2. Reuse across different operations

Draft issue 4 proposed reusing shared policy validation for a renewal that creates a new row.
The inspected helper obtains `$this->route('policy')` and passes its ID to
`Rule::unique(...)->ignore($policy?->id)`. That exemption is appropriate when editing the existing
row. Blindly carrying it into renewal validation could allow the source policy's number through
validation, despite per-organization uniqueness.

The requested correction was create-style uniqueness with no source-row exemption, plus an
explicit rejection case for submitting the source policy's number. No renewal endpoint had been
implemented, so the evidence does not claim that a failing production or feature test was observed.

**Possible refinement:** when proposed reuse materially supports a new operation, inspect whether
the reused code assumes update versus create, route-bound source versus destination, or retention
of existing values versus eligibility for a new record. Require the operation's intended guarantee;
leave the implementation choice to the consuming stack. Avoid copying Laravel API mechanics into
portable planning guidance.

## 3. Eligibility across sections

Draft issue 4's Context refused renewal for an archived client or carrier. Its first acceptance
criterion nevertheless promised acceptance “exactly when” the status was eligible and no renewal
existed, omitting both party restrictions.

The correction was to include active client and carrier requirements in the acceptance condition,
while preserving the approved blocked explanation and archived-agent behavior.

**Possible refinement:** compare unconditional and exhaustive claims such as “exactly when,”
“always,” and “only” against the restrictions elsewhere in the issue and approved scope.
Member-level closed-set coverage in `review.md` checks source membership; it does not by itself
prove that conditions distributed across sections form a consistent behavioral promise.

## 4. Source-relative values and decision ownership

The modal's dates were editable, and validation only required expiry on or after the submitted
effective date. This left open whether a renewal could overlap, or even precede, its source term.
The owner then accepted a handoff requiring the new effective date to be after the old expiry,
allowing gaps while refusing overlap.

That restriction was a product decision, not a fact derivable from “editable dates” or a portable
insurance rule. The annual-term and leap-year choices likewise remain useOrbit decisions.

**Possible refinement:** during investigation, identify source-relative invariants that ordinary
validation of the new record does not settle. If drafting exposes an unresolved behavior-changing
choice, surface it for approval through the owning plan process; do not silently lock a preferred
answer or re-open decisions already settled.

## Evaluation before promotion

- Compare these candidates with existing semantic review, approved-plan input, and plan-synthesis
  guidance before adding text. Prefer improving execution of an existing instruction over adding
  another checklist.
- Use minimal raw draft/code artifacts with the existing guidance to determine which findings
  are missed. Do not leak the expected diagnosis into the evaluation prompt.
- If a narrow clarification is warranted, compare detection before and after it, including a
  sound draft where no new product decision or extra investigation is needed.
- Preserve the boundary: `lab-it` settles material behavior with the owner; `plan-it` preserves
  approved intent and checks executable, internally consistent issue scope. Neither should turn
  this project's tags, renewal dates, or validation design into universal doctrine.

No active skill, compiled artifact, roadmap commitment, or consumer installation is changed by this
candidate record.
