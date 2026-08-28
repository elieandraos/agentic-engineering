---
name: my-architecture-laboratory
description: "Investigates and validates how an existing system or capability actually works, from real implementation, tests, and current evidence — never conventions or guesses — then produces one of three results: a new Claude Artifact architecture guide documenting existing architecture, an updated existing architecture guide reconciled with the current implementation, or an approved `plan.md`, handed to `my-feature-planning`, capturing feature-architecture decisions reached with the user. Trigger to document existing architecture, update an existing architecture guide, resolve architecture or design decisions for a proposed feature, or synthesize approved findings into `plan.md`. Not for explaining one function, debugging, reviewing a diff, or writing API reference docs."
---

# My Architecture Laboratory

## What this skill does

This skill investigates a real system and turns the resulting understanding into one of three
results:

| User intention                                   | Result                                             |
| ------------------------------------------------ | --------------------------------------------------- |
| Understand and document existing architecture    | New Claude Artifact architecture guide             |
| Reconcile a guide with changed implementation    | Updated existing Artifact                          |
| Design feature architecture through conversation | Approved `plan.md` handed to `my-feature-planning` |

Investigation and user validation come first in every workflow, and sometimes that's the whole
job: when the user only wants to understand a system, the skill stops after investigating and
recapping — no guide and no `plan.md` gets produced just because an investigation happened.

## Shared investigation and decision discipline

Every workflow below starts with the same evidence discipline:

1. Inspect the real current system and relevant evidence.
2. Reconcile implementation, tests, runtime evidence, and reliable history.
3. Explain the current architecture and identify uncertainty.

> The codebase establishes what exists; the user decides what it should become.

Tests are strong evidence — often surfacing real boundaries faster than implementation alone —
but not infallible authority: reconcile them with the implementation and relevant runtime
evidence, since tests can be incomplete or stale. If asked, check issue and commit history for
*why* — but the current codebase is the source of truth for *what*. Never document something
history says was planned but the code doesn't show. Do not begin drafting a guide or a `plan.md`
during this step.

What happens next is conditional, not uniform, per workflow: creating a new guide requires recap
confirmation before publication; planning feature architecture requires explicit, user-approved
decisions before writing `plan.md`; updating an existing guide asks the user only when authority,
intent, or a material decision is unclear — routine, verified current-state documentation does not
require a new product decision.

## Document existing architecture

Route: investigate the real system → recap and obtain confirmation → decide structure from the
center of gravity → load the guide-writing and Artifact-design instructions → use the template →
publish the Claude Artifact → run the architecture-guide review.

1. **Investigate** (formerly Phase 1 — Explore). Inspect every architectural surface the system
   actually has before writing anything. Typical concerns: persistence and data relationships;
   business rules and lifecycle behavior; request or interaction boundaries; authorization and
   security; background or asynchronous work; external integrations; user-facing surfaces and
   reusable UI logic; schema and operational constraints. These are investigation categories, not
   a fixed checklist — the consuming project supplies its own framework, directories, and concrete
   artifacts. Identify the **architectural center of gravity** — the one idea everything else
   hangs off (a polymorphic contract, a queue pipeline, a runtime subsystem boundary, a
   sync-vs-async split) — as a hypothesis the guide-writing step will need.

2. **Recap and confirm** (formerly Phase 2 — Recap and validate). Write the recap directly as chat
   output, not a file or an artifact. Cover, with concrete implementation references threaded
   throughout, whichever of these actually apply to the system: the problem being solved, the core
   architecture, reusable pieces versus integration-specific code, runtime behavior, the data
   model, the integration seam, security, testing, architectural decisions, and remaining gaps.
   Don't invent a data model, runtime lifecycle, security boundary, reuse seam, or integration
   split the system doesn't have just to fill out the list. Keep it bullet-driven and honest about
   gaps. **Stop here and wait for the user to confirm before this investigation becomes a
   published guide.** A correction here is real signal about what the guide needs to get right.

3. **Write and publish the guide** (formerly Phase 3 — Architecture guide). Only after the recap
   is approved:
   - Decide the document's structure from the confirmed center of gravity. Architecture guides do
     not use one fixed section inventory: structure follows the system being explained. See
     `references/doc-style.md` for the writing grammar and content-block vocabulary.
   - Load the `artifact-design` skill (required before writing any Artifact page).
   - Write the HTML using `references/template.html` as the starting scaffold. Replace content;
     keep the design system unless the system genuinely needs a new block type.
   - Publish with the `Artifact` tool: title `"{Capability} Architecture"`, a one-sentence
     description, and a stable, domain-appropriate favicon (see
     `references/doc-style.md#choosing-a-favicon`).
   - Run `references/review.md`'s checklist against the published guide before considering it
     complete — see "Output-specific non-negotiables" for what the guide itself must do.

Publishing to a Claude Artifact is specific to this workflow (and to updating an existing guide,
below) — investigating and recapping don't depend on it, and neither does the `plan.md` output of
planning feature architecture.

## Update an existing architecture guide

Use this workflow when a guide already exists and its underlying implementation has changed — not
as an automatic fourth stage after creating a new guide.

Route (formerly Phase 4 — Maintenance): locate the existing Claude Artifact, rather than minting a
new one → compare its claims with verified current implementation → identify changed architectural
guarantees → update the existing guide's affected sections as current-state fact, not as a
changelog of what happened → preserve its identity and stable presentation metadata (same `url`,
same favicon) → run `references/review.md` against the sections touched.

`references/maintenance.md` governs every judgment call in this route — read it before making any
edit. It is not an editing how-to; it is the methodology for changing what a guide says without
changing the architectural story it tells.

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
already-investigated current state and already-approved user decisions into a canonical
`plan.md`, the input `my-feature-planning` needs instead of reconstructing decisions from
conversation history.

**Only perform Plan Synthesis when the user asks for it.** Never produce a `plan.md` as an
automatic next step after investigation, and never treat a plain "document/explain X" request as
implicitly asking for one.

**Preconditions**, both required: an investigation of the same quality "Document existing
architecture" requires (concrete references, not conventions or guesses), and explicit,
user-approved decisions about the target state. If either is missing, do that work first — Plan
Synthesis never manufactures a decision on the user's behalf.

Every claim in the plan must fall into exactly one of four categories — see "Output-specific
non-negotiables" for the rule. Full methodology, the canonical section list, and the
pre-finalization review checklist live in `references/plan-synthesis.md` — read it before writing
anything.

State at the top of the written section that it is the source of truth for the subsequent
`my-feature-planning` pass — `my-feature-planning/rules/plan-md-input.md` checks for this
statement before treating a plan as canonical input.

**Skill boundary.** This workflow stops at an approved `plan.md` — see "Ownership and handoff" for
what belongs to `my-feature-planning` instead.

## Ownership and handoff

This skill owns:

- architecture investigation;
- architectural explanation;
- surfacing and resolving material decisions with the user;
- new architecture guides;
- maintenance of existing guides;
- synthesis of approved architecture into `plan.md`.

This skill does not own:

- application implementation;
- debugging or diff review;
- API reference documentation;
- feature classification and issue decomposition;
- GitHub issue mutation;
- delivery sequencing;
- Git workflow.

## Reference routing

References are loaded only when their workflow needs them — none is a universal prerequisite:

- guide writing → `references/doc-style.md`
- guide scaffold → `references/template.html`
- guide review → `references/review.md`
- guide maintenance → `references/maintenance.md`
- plan writing → `references/plan-synthesis.md`

## Output-specific non-negotiables

Guide rules (apply to "Document existing architecture" and "Update an existing architecture
guide"):

- Explain architecture, not implementation: why it exists, why it's shaped that way, and — where
  extension is relevant — how it can be extended. Code blocks exist only at genuine extension
  seams, never a walkthrough of a whole method body.
- When a real line exists between reusable infrastructure and integration-specific code, make it
  explicit in whatever structure the guide already uses — never a mandated section or table.
- Explain runtime ownership and lifecycle wherever the system has either — don't invent one for a
  capability with no runtime story.
- Ground security and decision claims in concrete enforcement references where one clearly exists;
  never force a misleading one.
- No API documentation, no endpoint inventories, no line-by-line implementation walkthroughs, no
  duplicated explanations across sections.
- Not every guide needs a limitations section. When limitations or deferred work materially affect
  understanding, state the reason rather than adding a generic TODO list.
- A guide is never done until it has passed a `references/review.md` pass — writing and reviewing
  are two separate steps.

Plan rules (apply to "Plan feature architecture"; full contract in
`references/plan-synthesis.md`):

- Keep current-state facts, locked decisions, derived constraints, and open implementation details
  visually and textually distinct — the locked-vs-open rule above all.
- Never present an unresolved decision as settled without the user's explicit confirmation.

Don't apply the guide rules to a `plan.md`, or the plan rules to a guide.
