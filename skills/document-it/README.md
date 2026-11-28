# document-it

Create, maintain, and review purpose-driven technical documentation in Markdown — reusing
sufficient, current, verified understanding, and drawing on `lab-it`'s investigation method only
when evidence is missing or stale.

## When to use it

- A technical system, operational process, reference, integration, cost model, approved design or
  product behavior needs documenting.
- An existing document needs reconciling with verified current reality.
- An existing document needs an independent check of whether it still serves its purpose.

Not for debugging or reviewing a diff. Not for investigating a system from scratch, resolving
architecture or product decisions, or synthesizing `plan.md` — those stay with
[`lab-it`](../lab-it/).

## Boring prompts

```shell
"Document the billing architecture."
"Update the architecture guide to match the current implementation."
"Is the authentication guide still accurate?"
"Write a deployment and recovery handbook."
"Document our infrastructure costs and assumptions."
"Document the payment provider integration and its webhooks."
"Document the subscription renewal rules under docs/billing/."
```

## What normally happens

Every request starts by checking whether currently available understanding is sufficient and
current. When it is, this skill writes or updates directly; when it isn't, it routes the relevant
investigation through `lab-it` first, then resumes. From there:

1. A new document under `docs/`, or wherever you or the project say. The evidence recap is
   confirmed first, unless you have already approved its substance and asked for the document.
   Structure follows purpose and audience.
2. An update to an existing document at its existing path, following every claim the change
   affects and leaving the rest alone.
3. A standalone review — a findings report, never a rewrite.

New documents and updates finish with the same review, and their material findings are corrected
before the work is reported complete.

## Ownership

Owns documentation creation, maintenance, and review. Investigation from scratch, architecture and
product decisions reached with the user, and `plan.md` synthesis belong to
[`lab-it`](../lab-it/) — file extension alone doesn't decide ownership; an approved `plan.md` stays
`lab-it`'s even though it's a `.md` file. Planning the resulting work into GitHub issues belongs to
[`plan-it`](../plan-it/).

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill document-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
