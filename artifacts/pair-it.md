# pair-it — Architecture Dossier

Status: Initial contract; partial forward-use evidence.
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

The initial contract reflects an explicit human decision about collaborative work.
Two reported pre-edit interactions in one consuming project showed checkpoint planning,
composition with an implementation workflow and approval stops. Human feedback identified
excessive upfront detail and insufficient concrete explanation of proposed code. The
contract now favors compact orientation and focused technical examples at the current
checkpoint. The candidate was read directly, not activated as an installed skill.
A subsequently reported first checkpoint cycle showed implementation, targeted
verification and a human review stop. Human feedback favored the inspection pointers
but found the report somewhat long; the walkthrough now separates the complete file
inventory from discussion-worthy changes and avoids repeating the approved proposal.
Full lifecycle behavior, automatic activation and portability remain unvalidated.
Keep further growth proportional to observed evidence. The runtime contract lives in
[`SKILL.md`](../skills/pair-it/SKILL.md).
