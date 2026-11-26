# pair-it — Architecture Dossier

Status: Initial contract; live validation pending.
Scope: Collaborative execution, independent of stack and delivery methodology.

## Purpose and ownership

Pair programming is an interaction contract, not a replacement implementation
methodology. The human wants to understand and participate in real code changes,
rather than receive only a completed diff. The tool owns checkpoint selection,
explanation, approval to proceed and walkthroughs. Implementation quality, scope,
independent review and delivery remain with the underlying workflow.

## Composition

`pair-it` works with native agent implementation or an applicable implementation
skill. With `implement-it`, its stops supplement rather than replace the existing
review and delivery gates. No dependency on that skill, GitHub issues or a particular
stack is required for standalone use.

## Confidence and boundaries

The initial contract reflects an explicit human decision about collaborative work,
not observed cross-project behavior. Keep it small until live sessions supply
evidence for refinements. Source-level reconciliation is not proof of activation,
checkpoint adherence or usefulness in a real session. The runtime contract lives in
[`SKILL.md`](../skills/pair-it/SKILL.md).
