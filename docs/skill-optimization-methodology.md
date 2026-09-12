# Skill Optimization Methodology

A practical methodology for improving how skills behave in real execution: reducing unnecessary loading and work, preserving correctness and safety, improving decision reliability, and using observed execution evidence to justify structural changes over time.

**Authority boundary.** This document owns optimization judgment: how to identify, evaluate, and prioritize efficiency improvements to skills and their surrounding workflow. It does not own a skill's operational behavior, authoring/disposition rules, or runtime-specific telemetry extraction. Each skill's own `SKILL.md`, rule/reference files, and the skill-authoring methodology remain authoritative for those concerns.

**Relationship to skill authoring.** Optimization does not replace authoring judgment. `docs/skill-authoring-methodology.md` decides where a durable rule or knowledge belongs and whether it should be generalized. This document decides whether observed behavior justifies changing the skill's structure or execution for greater efficiency or reliability. When an optimization implies a new or changed canonical rule, apply the skill-authoring methodology before publication.

## 1. What skill optimization means

Skill optimization is improving the relationship between **correct outcome** and the total cost of producing it. Cost is broader than token count or elapsed time. It can include context consumption, tool execution, human attention, repeated work, recovery cost, and unnecessary verification, provided the optimization does not weaken an independent safety or authorization boundary.

The goal is not to make a skill smaller. A longer rule can be more efficient when it removes repeated ambiguity, prevents recovery work, or makes a failure mechanically detectable. Likewise, a shorter rule can be worse if it pushes decisions back into improvisation.

Evaluate changes against the whole workflow rather than a single metric.

## 2. Optimization dimensions

A session may expose one or several of these dimensions:

**Loading efficiency** - whether the agent loaded the right guidance at the right time. Look for unnecessary rules, repeated loading, missing conditional boundaries, or a large rule being loaded when only a narrow portion is relevant.

**Context and token efficiency** - how much context is consumed by skills and their supporting material. Look for duplicated guidance, repeated restatement across files, historical material that does not help the current decision, excessive routing text, and rules that are routinely loaded without contributing to the current path.

**Execution efficiency** - how much active work is required to reach the correct outcome. Look for redundant tool calls, repeated inspection, unnecessary retries, avoidable backtracking, and procedures that perform the same discovery more than once.

**Human-interaction efficiency** - how much user attention the workflow consumes. Look for redundant approvals, questions caused by missing routing information, waits that could have been avoided safely, and decisions that are surfaced at the wrong boundary. A human stop that provides meaningful authorization is not waste merely because it takes time.

**Decision accuracy** - whether the skill makes the right behavior easier and wrong behavior harder. A mechanical check, explicit precondition, or clearer ownership can improve optimization even when it adds lines or execution time, because it reduces failure probability.

**Failure and recovery cost** - the effort spent recovering from an incorrect path. Look for rework, amended commits, repeated rule loading, repeated verification, recovery procedures, and fixes that could have been prevented by a stronger earlier boundary.

**Verification efficiency** - whether each verification step proves something distinct. Preserve independent checks that cover different failure modes; investigate checks that repeatedly prove the same thing without adding protection.

## 3. Evidence standard

Optimization decisions should follow:

`observed behavior -> evidence -> explicit decision -> targeted change -> real re-use -> re-evaluation`

Do not turn a theoretical efficiency concern into a canonical rule merely because a workflow looks elaborate.

Use the following confidence ladder:

- **Observed** - a concrete execution characteristic or failure was directly seen.
- **Inferred** - a plausible explanation or cost is derived from observed evidence but not yet directly confirmed.
- **Repeated** - the same optimization signal appears across multiple real execution passes.
- **Validated** - a change was applied and a later execution showed the intended improvement without unacceptable regressions.
- **Portable** - evidence indicates the optimization is useful beyond the skill or consuming project where it first appeared.

Repeated observations inside one consuming project strengthen the case for a repository-local optimization but do not, by themselves, establish cross-project portability.

## 4. Optimize total cost, not one metric

No single measure is a sufficient optimization target.

A useful evaluation considers at least these categories when the evidence supports them:

- context/token consumption;
- active execution time;
- human wait and interaction count;
- tool calls and repeated work;
- recovery/rework;
- correctness or failure rate;
- verification coverage.

Do not optimize a proxy at the expense of the outcome it represents. For example, reducing token usage by deleting a safety check is not an optimization if it increases failures or human recovery work.

Similarly, a file split is not automatically an optimization. It becomes one when the split creates a real loading or ownership boundary that avoids unnecessary context or work without creating greater routing complexity.

## 5. Conditional loading and structural optimization

Conditional splitting is one optimization lever, not a goal in itself.

A split is justified when there is evidence of a meaningful difference in:

- trigger;
- consumer;
- decision authority;
- execution phase;
- or required context.

A good split lets a real workflow avoid loading guidance it does not need, or gives an independently useful contract a clear owner. A bad split simply moves adjacent paragraphs into separate files and adds routing overhead.

Before splitting, ask:

1. What exact behavior is being separated?
2. Does it have an independent trigger or consumer?
3. Can one path reasonably proceed without it?
4. Does the extracted rule have a clear owner and useful cold-read boundary?
5. Does the split reduce real work or context, rather than merely improve aesthetics?
6. What new routing and reconciliation cost does the split introduce?

Prefer the smallest structural change supported by evidence. If a local fix removes the demonstrated cost, do not introduce a new rule only because a file is large.

## 6. Content optimization

Efficiency often comes from reducing duplication rather than reducing substance.

Prefer:

- one canonical owner for a contract;
- references instead of repeated matrices or procedures;
- concise routing language in `SKILL.md`;
- supporting rules for conditional detail;
- current rationale instead of case-by-case history;
- explicit boundaries where they prevent repeated rediscovery.

Do not delete durable reasoning simply because it consumes space. First ask whether the reasoning prevents a known failure, resolves an ambiguity, or supports a real decision.

## 7. Execution and verification optimization

When execution evidence shows repeated work, classify the repetition before removing it.

**Redundant work** - the same information is gathered or checked twice with no distinct protection. Candidate for consolidation.

**Layered protection** - multiple checks intentionally cover different failure modes or different lifecycle boundaries. Preserve unless evidence shows the added cost is disproportionate.

**Recovery work** - effort caused by a prior mistake or ambiguous boundary. Prefer fixing the earlier cause rather than optimizing the recovery procedure away.

**Human authorization** - an intentional decision boundary. Do not remove or collapse it merely because it increases elapsed time.

A successful outcome does not prove the workflow is efficient. A fast outcome does not prove it is safe.

## 8. Human attention as a cost

Treat human time and attention as first-class workflow resources.

Measure when evidence allows:

- number of approval/question stops;
- duration of human waits;
- repeated or redundant questions;
- decisions that were deferred unnecessarily;
- decisions that were surfaced too late to be useful.

Do not treat all waiting as waste. Approval, authorization, scope clarification, and other meaningful human decisions are part of the workflow's contract. Optimize the surrounding process so those decisions occur once, at the right boundary, with enough information to decide them confidently.

## 9. Telemetry and evidence quality

Use observed session telemetry when available. Distinguish:

- **Measured** - directly present in the runtime/session evidence.
- **Reconstructed** - derived from measured events or timestamps.
- **Unavailable** - genuinely absent or inaccessible after the applicable discovery path was attempted.

Never treat a missing measurement as evidence of low cost, and never treat an ambient context-window indicator as equivalent to cumulative session consumption.

Per-skill attribution is useful when the runtime provides it, but attribution alone does not prove that a skill caused a cost. Use it to locate candidates for investigation, then inspect what was actually loaded and what work followed.

## 10. From observation to optimization

A credible optimization candidate should answer:

- **What happened?**
- **What evidence shows the cost or inefficiency?**
- **Why is the current behavior unnecessary, inaccurate, or poorly routed?**
- **What is the smallest change likely to improve it?**
- **What safety, authorization, or correctness boundary must remain intact?**
- **How will the next real execution prove or disprove the change?**

Prefer explicit hypotheses such as:

> "A rule is loaded on a path that never consumes its contract."

or:

> "Two verification commands repeatedly establish the same fact without covering independent failure modes."

over vague claims such as:

> "This skill feels too long."

## 11. Optimization loop

Use the following loop for substantive optimization work:

1. **Observe** real execution.
2. **Measure** available cost and outcome evidence.
3. **Classify** the signal: loading, context, execution, human interaction, accuracy, recovery, or verification.
4. **Form a hypothesis** about the smallest change that could improve the signal.
5. **Check ownership** using `docs/skill-authoring-methodology.md` if the change affects canonical guidance, routing, or rule structure.
6. **Change** only the necessary layer.
7. **Smoke test** on real work, not only by reading the changed files.
8. **Steward** the resulting execution and compare it with the baseline evidence.
9. **Retain, refine, revert, or defer** based on the observed result.

A change that has not survived real re-use remains a hypothesis or current repository experiment, not a validated optimization.

## 12. Reporting optimization findings

A compact optimization finding should contain:

**Observed** - the behavior actually measured.

**Cost or risk** - why it matters.

**Cause** - the smallest evidence-backed explanation.

**Change** - what structural or procedural adjustment was proposed or made.

**Verification** - how the next execution will measure whether it helped.

**Confidence** - observed, inferred, repeated, validated, or portable.

Avoid turning every inefficiency into a finding. Report only signals that can change a decision or meaningfully improve the workflow.

## 13. Boundaries with other methodology

`skill-authoring-methodology.md` owns knowledge disposition, portability, ownership, and authoring structure.

`skill-optimization-methodology.md` owns efficiency analysis and optimization judgment.

`steward-it` owns observing and diagnosing real execution according to its operational contract. It is the primary evidence source for optimization work when the runtime exposes suitable telemetry.

Neither optimization nor stewardship silently changes canonical guidance. Changes to skills, rules, artifacts, or methodology remain subject to the repository's normal approval and publication workflow.

## 14. What counts as a successful optimization

A successful optimization is not necessarily a smaller file, fewer tokens, or faster execution.

It is a change that, under comparable real use, produces a better tradeoff among:

`correctness + decision reliability + context + execution + human attention + recovery cost`

while preserving the workflow's deliberate approval and safety boundaries.

When the evidence cannot establish that tradeoff, keep the change as a hypothesis and gather more evidence before promoting it to durable guidance.
