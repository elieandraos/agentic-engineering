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
2. **Implement:** make only the approved checkpoint's changes. Stop for a material
   deviation or unresolved decision rather than extending the approval silently.
3. **Walk through and verify:** summarize routine changes without repeating the
   approved proposal. Make the complete set of changed files available for inspection
   and highlight those most worth discussing. Use actual code to explain noteworthy
   implementation choices, deviations, safeguards and interactions. Run appropriate
   targeted verification and report actual results and any limitations. If the
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
terminology. Explain the intent and reasoning behind decisions before their mechanics;
connect code choices to their practical consequences where relevant. When requesting
a decision, explain the problem, the practical difference between options and why you
recommend one. Use focused code snippets to make significant proposed designs concrete,
including how relevant components interact. Distinguish proposed code from existing
code; avoid full-file dumps and snippets for routine edits. When a change participates
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

## Completion

After the last checkpoint, return to the underlying workflow's final verification,
review and delivery requirements. Checkpoint approval is not final implementation
approval, commit authorization, or permission to publish. Do not bypass those gates.
