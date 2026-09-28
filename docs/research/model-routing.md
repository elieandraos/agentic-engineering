# Model Routing Research — Claude Code

Status: Investigation. Record runtime capability and observed evidence; do not introduce model routing from this document.

## Question

Can Agentic Engineering describe engineering work in portable capability terms while a runtime-specific layer chooses an appropriate model, reasoning effort, tools, isolation, and execution topology?

This is deliberately different from assigning a model to each skill. One skill invocation can contain both mechanical work and difficult judgment, so routing by whole skill may be too coarse.

## Observed Claude Code runtime

Observed on Claude Code CLI v2.1.281 during normal useOrbit work.

The main session reported:

- Opus 5.5 with a 1M context window;
- medium effort through `CLAUDE_EFFORT`;
- no project/user model or effort override;
- no custom agent definitions;
- no OpenTelemetry configuration.

Observed model controls include:

- main-session model selection through user/runtime controls such as `/model` and CLI configuration;
- a per-call model choice when spawning an Agent;
- a model choice for Workflow `agent()` calls;
- custom agent definitions that can declare model and effort;
- subagents inheriting the parent model when no more-specific choice applies.

The runtime also contains fixed model choices in some built-in behavior. In this investigation, the built-in `claude-code-guide` agent ran on Haiku while its parent ran on Opus.

Do not treat this inventory as a stable portable API. Claude Code model names, aliases, configuration surfaces, and transcript formats are vendor/runtime details and can change.

## Telemetry observed

Claude Code's local transcript/runtime artifacts expose enough information to make later retrospective analysis plausible:

- model;
- effort and per-turn effort;
- input/output/cache/thinking token usage;
- timestamp and request identity;
- subagent identity and spawn depth;
- skill/agent attribution;
- subagent duration and tool-use counts on completion.

Cost is not stored as a simple per-response field in the observed transcripts. Human corrections and retries are also not represented as one explicit outcome field; they would need to be inferred from execution history or captured deliberately.

The internal transcript schema is not documented as a stable interface.

## First routing-quality evidence

The documentation investigation itself produced a useful example.

The built-in `claude-code-guide` agent, running on Haiku, returned two material claims that the Opus parent later found to be wrong when checking the primary Claude Code documentation:

1. it claimed a subagent could not have its own effort level;
2. it claimed Claude Code never routes work to a smaller model.

Both were corrected before the final report.

This is one observation, not evidence that Haiku is unsuitable for documentation research. It does show why routing quality cannot be evaluated from token cost or latency alone.

A useful evaluation lens may need to include:

```text
execution cost
+ verification cost
+ correction/rework
+ human interruption
--------------------
useful correct outcome
```

A cheaper initial worker can be more expensive overall if another context must substantially verify or redo its work.

## Capability routing hypothesis

Do not adopt this as architecture yet.

Current evidence supports investigating a separation resembling:

```text
Methodology skill
  what good engineering work requires
        |
        v
Control Room
  what work is happening and what capability it needs
        |
        v
Runtime adapter
  concrete model + effort + tools + isolation + topology
        |
        v
Execution
        |
        v
steward-it
  retrospective evidence about routing effectiveness
```

The portable unit should likely be a capability requirement rather than a vendor model name.

Examples of capability dimensions worth observing, without defining tiers yet:

- depth of reasoning/judgment;
- exploration versus bounded execution;
- verification sensitivity;
- tool requirements;
- isolation requirements;
- expected context size;
- autonomy/turn budget.

Do not encode mappings such as `lab-it -> Opus` or `search -> Haiku`. A single Lab or Implement invocation can contain work with very different capability needs.

## Boundary hypothesis

### Methodology

Owns the engineering contract: what evidence, verification, review, decisions, and outputs good work requires.

Portable skills should not need to name Claude models or other vendor-specific runtime controls.

### Control Room

Potentially understands the current unit of work and the capability it requires, alongside the lifecycle and coordination responsibilities already under investigation.

### Runtime adapter

Potentially maps a portable capability requirement onto concrete runtime controls. In Claude Code those controls currently include model, effort, tools, isolation, and agent/workflow topology.

Do not conclude yet that this requires predefined agent types. The current inability to set effort in the observed per-call Agent interface is a Claude Code constraint, not a portable architecture decision.

### steward-it

Could later evaluate routing retrospectively if useful outcome evidence can be connected to model/effort/token/duration data.

This extends stewarding beyond raw cost optimization. A routing decision should be judged by engineering outcome, including verification and correction cost.

## Portability

Potentially portable concepts:

- capability-based work classification;
- per-worker model/intelligence selection;
- reasoning/effort selection;
- tool allowlists;
- workspace/isolation needs;
- duration/token telemetry;
- attribution of work to a specialist skill or worker;
- outcome/correction evidence.

Claude Code-specific details include its model aliases, agent frontmatter, environment variables, transcript JSONL schema, built-in agent types, hooks, Workflow/fork mechanics, and usage interfaces.

## What to observe next

Do not change routing for the next useOrbit implementation work merely to test this research. The existing default behavior is useful baseline evidence.

During normal work, retain evidence when it is cheap to do so:

- expensive-model work that was largely mechanical;
- cheaper-model work that required substantial verification or correction;
- difficult work where stronger reasoning prevented rework;
- whether model/effort attribution can be connected reliably to specialist skill, duration, corrections, and final outcome;
- whether useful capability categories recur naturally.

Only after repeated evidence should Agentic Engineering define capability tiers or a runtime-routing policy.
