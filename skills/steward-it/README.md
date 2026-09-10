# steward-it

Retrospective engineering stewardship for sessions that were unexpectedly slow, difficult, or
repeatedly off course. It reconstructs what happened, checks the intended workflow against observed
behavior, classifies the likely cause, looks for recurrence, and recommends deliberate improvements
without automatically changing canonical guidance.

## When to use it

- A session took substantially longer than expected and you want to know why.
- Agent behavior appeared to ignore or overreach a skill boundary.
- The same workflow problem has appeared more than once and may be systemic.
- You want to compare a skill trace or context report with what actually happened.

It is human-invoked and retrospective. It is not part of the normal `Lab -> Plan -> Implement -> Review -> Ship`
lifecycle and does not silently monitor ordinary sessions.

## What normally happens

1. Reconstruct the relevant session from available evidence.
2. Separate observations from inference.
3. Compare intended guidance with observed behavior.
4. When relevant, compare static context estimates with what the session reports as loaded or consumed.
5. Classify the likely cause and check for recurrence.
6. Recommend the smallest justified improvement.
7. Record only a compact durable observation when a project evidence file is maintained.

Skill traces and context reports are optional diagnostics, not requirements of normal skill execution.

## Evidence convention

Keep stewardship evidence small. A durable observation should normally be one or two sentences and
include a commit, PR, issue, or other concrete reference when available. The evidence file is not a
diary; it exists so later stewardship can detect repeated failure modes or useful cost patterns from
real work.

## Context consumption

Treat context cost as a diagnostic signal, not a quality verdict. Keep static file measurements,
modeled workflow estimates, and observed session consumption separate. Do not promote rough
characters-to-token estimates into measured runtime usage, and do not recommend splitting a rule file
from a single large number alone.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill steward-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
