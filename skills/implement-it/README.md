# implement-it

Take an approved GitHub issue from implementation through verified commits and closure.

## When to use it

- Implementing, committing, verifying, or closing an approved issue.
- Checking what's next once a milestone issue closes.
- Performing an authorized delivery correction that `ship-it` has handed back.

The issue can come from [`plan-it`](../plan-it/) or already exist through another valid
route — what matters is that it's approved, not who drafted it.

## Boring prompts

```shell
"Implement issue #42."
"Commit the approved work for issue #42."
"What's next in this milestone?"
```

## What normally happens

1. Establish the correct branch for the work.
2. Implement and verify the issue's scope.
3. Stop for human review — once on the implementation, once on the proposed commit plan.
4. Build coherent commits and push them, once authorized.
5. Close the issue only once its commits are reachable on the remote.
6. Recompute the milestone's dependency-ready set and recommend the next issue — or hand off
   to [`ship-it`](../ship-it/) once the milestone is genuinely empty.

## Ownership

Performs the approved implementation itself. Project context supplies repository and
domain conventions; an applicable stack companion (such as
[`laravel-inertia-stack`](../laravel-inertia-stack/)) supplies technology-specific
implementation knowledge. Deciding what work should exist belongs to
[`plan-it`](../plan-it/); milestone PR readiness, PR creation, and release belong to
[`ship-it`](../ship-it/).

A specific-issue request ends after that issue's own lifecycle — completing one issue is
never by itself authorization to continue into the next, or into milestone delivery.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill implement-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
