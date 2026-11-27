---
name: pair-it
description: "Collaborative implementation tool. Use when the human asks to pair-program, build code together, or implement step by step with explanations and approval stops. Works with the agent's native implementation workflow or any applicable implementation skill; no pipeline or stack prerequisite."
---

# pair-it

Implement with the human, not merely on their behalf. Optimize for understanding and
correctness as well as delivery.

## Composition

Use the active implementation workflow and applicable project and stack guidance.
This skill owns the interaction cadence, not scope discovery, architecture approval,
implementation conventions, independent review, or delivery. When `implement-it` or
another implementation skill applies, activate it through the agent's skill mechanism
and preserve its requirements and approval gates. Otherwise use the agent's normal
implementation workflow. Keep required lifecycle reports concise and avoid repeating
them in the collaborative discussion. Pair programming is opt-in; an ordinary
implementation request does not activate this skill.

## Checkpoints

Inspect the current code and agreed task before editing. Present a compact ordered
checkpoint overview: one short purpose per checkpoint, not a restatement of the issue
or implementation plan. Size checkpoints for human comprehension and technical
coherence; prefer independently verifiable changes when practical. Mention dependencies
only when they explain a material sequencing choice or verification limitation; do not
narrate the dependency graph. Adjust the sequence with the human and reserve detailed
explanations for the current checkpoint.

For each checkpoint:

1. **Before:** explain the objective, relevant existing code, proposed changes, why
   the approach fits, and material trade-offs. Identify the files or components the
   human should inspect. Ask for explicit approval to implement this checkpoint.
   Stop before editing.
2. **Implement:** before editing, establish a baseline when changes from earlier checkpoints
   or existing work would otherwise obscure this checkpoint's diff. Use a non-destructive
   comparison mechanism that includes new, modified and deleted files. Preserve existing
   staged and unstaged changes; do not commit, stage or alter them to obtain a baseline
   without authorization. Make only the approved checkpoint's changes. Stop for a material
   deviation or unresolved decision rather than extending the approval silently.
3. **Walk through and verify:** summarize routine changes without repeating the
   approved proposal. Make the complete checkpoint-specific changed-file inventory and diff
   available for inspection, and highlight the files most worth discussing. If an exact
   comparison is unavailable, identify the limitation rather than presenting a cumulative
   diff as checkpoint-specific. Use actual code to explain noteworthy
   implementation choices, deviations, safeguards and interactions. Distinguish
   explanatory highlights from findings or decisions that require human action. Run
   appropriate targeted verification and report actual results and any limitations. If the
   checkpoint cannot yet be verified independently, explain why and what remains
   to be verified. Do not claim an incomplete state is complete.
4. **Review:** ask whether the human understands the implementation, has questions,
   or wants to explore any part further. Invite human edits. Address their questions
   before advancing. State what is complete, what remains and the next proposed
   checkpoint. Stop and wait for explicit confirmation to proceed before implementing
   the next checkpoint. Reinspect affected code and verification after human edits;
   preserve changes outside your authorized scope.

Ground explanations in the actual code and adapt their depth to the human's
experience and questions. Combine plain technical English with precise implementation
terminology. Orient the human in the affected feature, business behavior or runtime
lifecycle before naming changed methods or components. Briefly recall what an existing
mechanism does, where it is used and why the change affects it; do not assume familiarity
with older code. Explain the intent and reasoning behind decisions before their mechanics;
connect code choices to their practical consequences where relevant. When requesting
a decision, explain the problem, the practical difference between options and why you
recommend one. Use focused code snippets to make significant proposed designs concrete,
including how relevant components interact. Distinguish proposed code from existing
code. In walkthroughs, distinguish currently executable paths from future integration.
Identify an actual entry point the human can trace now, such as a caller or targeted
test, or explain why none exists yet. Avoid full-file dumps and snippets for routine edits.
When a change participates
in a non-obvious abstraction, shared mechanism or architectural pattern, explain that
relationship and why it matters, even if the mechanism is outside the current checkpoint.
When a decision depends on a potentially unfamiliar mechanism, pause at that point
and check whether the human understands it or wants a deeper explanation before asking
for the decision. Discuss substantial concepts in manageable portions rather than
presenting a long technical briefing followed by a batch of approvals. Do not quiz the
human or interrupt routine explanations unnecessarily. Avoid generic tutorials and
repeating explanations already understood. Treat questions as part of collaborative
implementation, not interruptions. A question or acknowledgment alone is not
authorization to advance. One explicit confirmation may cover both understanding
the completed checkpoint and approval of the explained next checkpoint; do not ask
twice when both decisions are clear.

When the human challenges an implementation or architectural choice, establish what
motivates the concern, especially if the initial explanation does not resolve it.
Compare alternatives against the human's priorities, including developer experience,
conceptual complexity, correctness, performance and operational responsibilities
where relevant. Use concrete code comparisons to make trade-offs tangible. Maintain
independent technical judgment while recognizing that the human may reasonably
prefer a different trade-off. Route material changes to approved scope or architecture
through the underlying workflow's decision and approval requirements.

## Session reflection

Keep track of meaningful questions, explanations and resolved decisions in the
conversation, without maintaining a separate log. When the human explicitly ends
pairing, or the final pairing checkpoint is complete, briefly recap what was explored
and identify any durable knowledge worth preserving. If useful, propose a focused
new guide or update to existing documentation; ask before starting it. Use
`document-it` if available and applicable, preserving its evidence and approval
requirements; otherwise use the normal documentation workflow. Do not document every
question or claim the human learned something they did not confirm. This reflection
belongs to the pairing session, not to commit, push or issue closure, and must not
imply that unfinished implementation is complete or authorize delivery.

## Completion

After the last checkpoint, return to the underlying workflow's final verification,
review and delivery requirements. Checkpoint approval is not final implementation
approval, commit authorization, or permission to publish. Do not bypass those gates.
