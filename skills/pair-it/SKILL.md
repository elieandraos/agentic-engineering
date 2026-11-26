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
implementation workflow. Pair programming is opt-in; an ordinary implementation
request does not activate this skill.

## Checkpoints

Inspect the current code and agreed task before editing. Propose an ordered sequence
of meaningful implementation checkpoints, each small enough for the human to review
and large enough to avoid stopping for routine edits. Explain dependencies and adjust
the sequence with the human as needed.

For each checkpoint:

1. **Before:** explain the objective, relevant existing code, proposed changes, why
   the approach fits, and material trade-offs. Identify the files or components the
   human should inspect. Ask for explicit approval to implement this checkpoint.
   Stop before editing.
2. **Implement:** make only the approved checkpoint's changes. Stop for a material
   deviation or unresolved decision rather than extending the approval silently.
3. **Walk through and verify:** show the actual changed files and relevant code.
   Explain how the pieces interact, important decisions, safeguards and failure
   paths. Run appropriate targeted verification and report actual results and any
   limitations. If the checkpoint cannot yet be verified independently, explain why
   and what remains to be verified. Do not claim an incomplete state is complete.
4. **Review:** invite questions and human edits. State what is complete, what remains
   and the next proposed checkpoint. Stop and wait for explicit approval before
   implementing the next checkpoint. Reinspect affected code and verification after
   human edits; preserve changes outside your authorized scope.

Use explanations grounded in the actual code and adapt their depth to the human's
experience and questions. Do not turn the walkthrough into a generic tutorial or
repeat explanations already understood. A question or acknowledgment is not
authorization to advance. A review stop and the next checkpoint's proposal may share
one message if both decisions are clear.

## Completion

After the last checkpoint, return to the underlying workflow's final verification,
review and delivery requirements. Checkpoint approval is not final implementation
approval, commit authorization, or permission to publish. Do not bypass those gates.
