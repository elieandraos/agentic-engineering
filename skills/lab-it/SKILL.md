---
name: lab-it
description: "Investigates and validates how an existing system or capability actually works, from real implementation, tests, and current evidence — never conventions or guesses — producing a verified answer, an architecture decision reached with the user, or an approved `plan.md` handed to `plan-it`. Trigger to investigate or explain how a system works, resolve architecture or design decisions for a proposed feature, or synthesize approved findings into `plan.md`. Not for explaining one function, debugging, reviewing a diff, writing API reference docs, or creating, updating, or reviewing an architecture guide — route guide work to `document-it`."
---

# lab-it

## What this skill does

This skill investigates a real system and turns the resulting understanding into one of the
following:

| User intention                                    | Result                                                          |
| -------------------------------------------------- | ----------------------------------------------------------------|
| Understand how a system actually works             | A verified answer — investigation and recap, no guide required  |
| Design feature architecture through conversation    | Approved `plan.md` handed to `plan-it`                          |
| Create, update, or review an architecture guide     | Routed to `document-it`                                         |

Investigation comes first in every workflow — whether user confirmation follows, and when, is
conditional; see "Shared investigation and decision discipline" below. Investigation and recap
alone may be the complete result: no `plan.md` gets produced just because an investigation
happened.

## Shared investigation and decision discipline

Every workflow below starts with the same evidence discipline — including an investigation
`document-it` routes here when its own available evidence is missing or stale:

1. Inspect the real current system and relevant evidence — not conventions or assumptions.
2. Reconcile implementation, configuration, schema, tests, runtime evidence, and reliable history.
3. Explain the current architecture and identify uncertainty.

> The system establishes what exists; the user decides what it should become.

Tests are strong evidence — often surfacing real boundaries faster than implementation alone —
but not infallible authority: reconcile them with the implementation and other relevant evidence,
since tests can be incomplete or stale. Implementation is authoritative for implementation facts;
configuration, schema, runtime observations, and external-system state are authoritative for
whatever they each actually govern. If asked, check issue and commit history for *why* — reliable
history explains rationale, it doesn't establish current behavior. Never document something
history says was planned but the evidence doesn't show. Do not begin writing a `plan.md` — or,
when this investigation was routed from `document-it`, a guide — during this step.

What happens next is conditional, not uniform: investigation can end in a verified answer alone,
with no further output required; planning feature architecture requires explicit, user-approved
decisions before writing `plan.md`; an investigation routed here from `document-it` ends by
handing back verified findings rather than drafting a guide itself.

## Plan feature architecture

Use this workflow when the point of the architecture work is to prepare a real implementation
initiative, not to teach a system. It can begin from a feature idea discussed in conversation, an
architecture question, an existing investigation, or already-approved findings and decisions.

The workflow may need to:

- investigate how the current system supports or constrains the proposed feature;
- discuss viable target approaches with the user;
- distinguish current facts from proposed choices;
- obtain explicit decisions for material product/architecture questions;
- leave implementation details open when every viable option preserves the approved guarantees.

Only after the architecture is sufficiently investigated and the material decisions are approved
does this workflow perform its final writing step, **Plan Synthesis** — consolidating an
already-investigated current state and already-approved user decisions into a draft `plan.md`
intended to become canonical, the input `plan-it` needs instead of reconstructing
decisions from conversation history.

**Only perform Plan Synthesis when the user asks for it.** Never produce a `plan.md` as an
automatic next step after investigation, and never treat a plain "document/explain X" request as
implicitly asking for one.

**Preconditions**, both required: an investigation meeting the same evidence discipline as
"Shared investigation and decision discipline" above (concrete references, not conventions or
guesses), and explicit, user-approved decisions about the target state. If either is missing, do
that work first — Plan Synthesis never manufactures a decision on the user's behalf.

Every claim in the plan must fall into exactly one of four categories — see "Output-specific
non-negotiables" for the rule. `rules/plan-synthesis.md` owns the full methodology: the
four-category claim model, the flexible initiative-driven content model, evidence and placement
rules, the internal review pass, and the approval/handoff contract — read it before writing
anything.

State at the top of the written section that it is the source of truth for the subsequent
`plan-it` pass. That statement marks the section's intended handoff role — it does not
by itself prove approval. `plan-it` treats a plan as canonical only once the initiative
matches and the user's explicit approval is established; see
`plan-it/rules/plan-md-input.md` for the full recognition procedure.

**Skill boundary.** This workflow stops at an approved `plan.md` — see "Ownership and handoff" for
what belongs to `plan-it` instead.

## Ownership and handoff

This skill owns:

- architecture investigation;
- architectural explanation;
- surfacing and resolving material decisions with the user;
- synthesis of approved architecture into `plan.md`.

An investigation may end in a verified answer alone — a guide is never a required next step.

This skill does not own:

- creating or updating an architecture guide, or guide review (→ `document-it` — draws on this
  skill's investigation method when its own available evidence is missing or stale, rather than
  duplicating it);
- application implementation;
- debugging or diff review;
- API reference documentation;
- feature classification and issue decomposition;
- GitHub issue mutation;
- delivery sequencing;
- Git workflow.

## Rule and supporting-file routing

- plan writing → `rules/plan-synthesis.md`, loaded only when "Plan feature architecture" needs it.

Guide-writing, guide-scaffold, guide-review, and guide-maintenance rules live under `document-it`
and are not duplicated here.

## Output-specific non-negotiables

Plan rules (apply to "Plan feature architecture"; full contract in
`rules/plan-synthesis.md`):

- Keep current-state facts, locked decisions, derived constraints, and open implementation details
  visually and textually distinct — the locked-vs-open rule above all.
- Never present an unresolved decision as settled without the user's explicit confirmation.

Guide-specific non-negotiables live in `document-it/SKILL.md` and `document-it/rules/review.md` —
not duplicated here.
