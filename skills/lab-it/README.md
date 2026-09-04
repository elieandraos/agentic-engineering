# lab-it

Investigate how a system actually works, answer architecture questions, and—when
useful—turn the evidence into an architecture guide or an approved change plan.

## When to use it

- You need an answer about how something in the codebase actually works, backed by real
  implementation, tests, and current evidence — not conventions or guesses.
- A published architecture guide needs checking against current behavior.
- A feature idea needs its architecture decisions settled before planning or
  implementation starts.

Not for explaining one function, debugging, reviewing a diff, or writing API reference
docs.

## Boring prompts

```shell
"How does authentication work across the application?"
"Document the billing architecture."
"Update the architecture guide to match the current implementation."
"Plan how invoice exports should fit into the system."
```

## What normally happens

Every request starts with the same investigation: inspect the real system, reconcile
implementation, config, schema, tests, and history, and explain what's there — including
what's still uncertain. From there, one of four outcomes follows:

1. Investigation and a direct answer.
2. A new architecture guide, extracted from implemented behavior across every layer that
   matters.
3. An update to an existing architecture guide, reconciled with verified current reality.
4. An approved `plan.md`, handed off as canonical input for planning.

Investigation and an answer can be the complete result on their own — a guide or a
`plan.md` is something a request specifically asks for, never an automatic next step.

## Ownership

Owns architecture investigation, architectural explanation, and turning approved
decisions into guides or a `plan.md`. Planning the resulting work into GitHub issues
belongs to [`plan-it`](../plan-it/); implementing it belongs to [`ship-it`](../ship-it/).

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill lab-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
