# Companion Activation

## Before implementation

Before writing or modifying code, enumerate the available implementation, testing, tooling, and
stack-companion skills that may apply to the requested issue. Do not stop after finding the first
matching skill, and do not assume one general framework or testing skill makes a custom companion
unnecessary.

For each candidate skill, inspect its activation or trigger description and decide whether it applies.
A matching stack companion remains applicable even when a Boost, framework, or testing skill also
applies; one does not substitute for another unless the applicable skill explicitly says so. When a
skill states that it must be loaded alongside another named skill, treat that relationship as part of
its activation condition and satisfy both sides.

An applicable skill is not considered activated merely because its files were read or its guidance was
consulted. Activate it through the consuming agent's skill mechanism (for example, a `Skill` tool
invocation) before implementation begins. Direct file reads are supporting evidence, not a substitute
for activation.

### Activation checkpoint

Before writing code, produce a concise activation checkpoint in the working session that records:

- candidates considered;
- candidates activated through the skill mechanism;
- applicable candidates that were not activated, with the reason;
- any unavailable activation metadata or mechanism.

Do not begin implementation until this checkpoint is complete. If an applicable skill cannot be
activated through the available mechanism, stop and report the limitation rather than silently
continuing with direct file reads or sibling-code precedent.

## Evidence of activation

The activation checkpoint is the evidence of the decision. At Gate 1, report the activated skill set
again in one concise `Activated skills:` line so the pre-implementation decision remains visible at
the implementation boundary.

Do not infer activation from the implementation outcome afterward. When no custom stack companion
applies, continue with the applicable general implementation skills and do not invent a stack-specific
substitute.
