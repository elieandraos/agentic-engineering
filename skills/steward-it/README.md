# steward-it

Retrospective engineering stewardship for sessions that were unexpectedly slow, difficult, or
repeatedly off course. It reconstructs what happened, checks the intended workflow against observed
behavior, classifies the likely cause, looks for recurrence, and recommends deliberate improvements
without automatically changing canonical guidance.

## When to use it

- A session took substantially longer than expected and you want to know why.
- Agent behavior appeared to ignore or overreach a skill boundary.
- The same workflow problem has appeared more than once and may be systemic.
- You want to compare a skill trace with what actually happened.

It is human-invoked and retrospective. It is not part of the normal `Lab -> Plan -> Implement -> Review -> Ship`
lifecycle and does not silently monitor ordinary sessions.

## Boring prompts

```shell
"Steward this session. I expected this to be much faster."
"What happened here?"
"Steward this failure and tell me where the problem belongs."
"We've seen this twice now. Is there a pattern?"
```

## What normally happens

1. Reconstruct the relevant session from available evidence.
2. Separate observations from inference.
3. Compare intended guidance with observed behavior.
4. Classify the likely cause and check for recurrence.
5. Recommend the smallest justified improvement.
6. Record only a compact durable observation when a project evidence file is maintained.

Skill traces are optional diagnostics, not a requirement of normal skill execution.

## Evidence convention

Keep stewardship evidence small. A durable observation should normally be one or two sentences and
include a commit, PR, issue, or other concrete reference when available. The evidence file is not a
diary; it exists so later stewardship can detect repeated failure modes from real work.

## Context consumption

Activation should remain lightweight. The session being reviewed already contains most of the useful
material; load only supporting rules or evidence needed for the specific retrospective. Do not require
verbose traces or continuous logging for ordinary work.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill steward-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
