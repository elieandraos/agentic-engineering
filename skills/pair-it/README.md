# pair-it

Pair-program with an agent through human-approved implementation checkpoints,
architectural discussions and code walkthroughs.

The goal is collaborative engineering with shared understanding and deliberate
human ownership of technical decisions.

## When to use it

Use it when you want to participate in implementation and understand the code as it
is built. It works with the agent's normal implementation workflow or alongside an
applicable implementation skill.

## Boring prompts

```text
"Pair-program with me on this feature."
"Implement issue #42 and pair-program with me."
```

## Checkpoints are not commits

A checkpoint is a unit of collaboration; a commit is a unit of coherent implementation.
Checkpoints are chosen for human comprehension and technical coherence. Semantic commit
boundaries are derived from the completed, reviewed implementation when using
[`implement-it`](../implement-it/).

Some checkpoints may naturally become individual commits. Others won't. A checkpoint
approval authorizes implementation of that checkpoint, not a commit, push or issue closure.

This separation lets us optimize the learning experience without compromising the
quality of Git history. `implement-it` remains responsible for the lifecycle;
`pair-it` shapes the collaborative experience without duplicating it.

## When pairing ends

Reflect on the meaningful questions and decisions from the session, and consider
whether any durable knowledge is worth documenting. Pairing can end before the
implementation or delivery lifecycle does.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill pair-it
```

See [`SKILL.md`](SKILL.md) for the operational contract.
