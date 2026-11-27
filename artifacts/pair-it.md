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
A reported follow-up question about an enum elicited its consumers, architectural
relationships and a proposed improvement. The human then requested a session-end
reflection to identify documentation-worthy knowledge independently of issue delivery.
That reflection is an approved design, not yet observed behavior; documentation remains
owned by the applicable documentation workflow.
Reported use in the same project also supports collaborative exploration of
architectural trade-offs during implementation. The human's priorities can differ
from the agent's initial optimization criteria; the interaction contract should
surface those priorities without transferring scope or architecture approval to
`pair-it`. The revised guidance is approved, but its effect without external
prompt coaching remains unvalidated.
Checkpoint reviewability is independent of commit boundaries. The contract calls for
checkpoint-specific comparisons without requiring a particular version-control mechanism.
Walkthroughs distinguish executable paths from future integration and point to a current
entry point where available. Reported use in one project supports the feasibility of
non-destructive baseline comparisons, including untracked files; the revised runtime
instructions have not been independently exercised.

Full lifecycle behavior, automatic activation and portability remain unvalidated.
Keep further growth proportional to observed evidence. The runtime contract lives in
[`SKILL.md`](../skills/pair-it/SKILL.md).
