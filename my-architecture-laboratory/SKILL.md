---
name: my-architecture-laboratory
description: "Reconstructs and validates how an existing system or capability actually works — from real implementation, tests, and current evidence — before any documentation is written, then hands that understanding off as a published architecture guide or as an approved `plan.md` for `my-feature-planning`. Trigger to investigate or document existing architecture, to resolve unresolved architecture or design decisions with the user, to write or maintain an architecture guide, or to synthesize already-investigated findings and already-approved decisions into `plan.md`. Not for explaining one function, debugging, reviewing a diff, or writing API reference docs."
---

# My Architecture Laboratory

Phases 1 and 2 are the hard part: reconstruct an accurate understanding of the system, then validate
it with the user before writing anything. Phase 3 hands that already-correct understanding off as a
written guide; the guide is the artifact this methodology produces, not the goal it aims at.

Four phases, in order, produce a published architecture guide. Do not skip Explore, do not skip the
Phase 2 pause, and do not force a fixed template onto Phase 3 — the system being explained determines
the document, not the other way around.

This skill owns architecture exploration, evidence-based current-state analysis, surfacing unresolved
decisions, the human decision gate, and architecture-guide/`plan.md` production and maintenance. It
never writes application code, drafts or mutates GitHub issues, classifies or decomposes features,
sequences delivery work, or performs Git workflow.

> The codebase establishes what exists; the user decides what it should become.

Plan Synthesis is a second, parallel output track for when the goal is a canonical `plan.md` handoff
into `my-feature-planning` instead of a teaching guide. It shares Phase 1's investigation discipline
and Phase 2's validate-before-writing discipline but produces a different artifact for a different
reader — see "Plan Synthesis" below.

This skill routes detailed mechanics to its own references, loaded only when the phase needs them:
`references/doc-style.md` (Phase 3 writing grammar), `references/review.md` (critical review, after
Phase 3 and again in Phase 4), `references/maintenance.md` (Phase 4 evolution discipline), and
`references/plan-synthesis.md` (Plan Synthesis methodology). None are optional shortcuts — an
architecture guide is a living asset across all four phases, and a synthesized plan is a load-bearing
handoff document.

## Phase 1 — Explore

Before writing a single word of documentation, inspect every architectural surface the system
actually has. Typical concerns: persistence and data relationships; business rules and lifecycle
behavior; request or interaction boundaries; authorization and security; background or asynchronous
work; external integrations; user-facing surfaces and reusable UI logic; schema and operational
constraints. These are investigation categories, not a fixed checklist — the consuming project
supplies its own framework, directories, and concrete artifacts.

- Read the tests — they establish the real contract and the real boundaries faster than the
  implementation does.
- If asked, check issue and commit history for *why* — but the current codebase is the source of
  truth for *what*. Never document something history says was planned but the code doesn't show.
- Identify the **architectural center of gravity** — the one idea everything else hangs off (a
  polymorphic contract, a queue pipeline, a runtime subsystem boundary, a sync-vs-async split). Form
  a hypothesis now; Phase 3 will need it.

Do not begin writing documentation in this phase — not even a draft.

## Phase 2 — Recap and validate

Write the recap directly as chat output, not a file or an artifact. Its only purpose is to prove you
understood the system before spending effort teaching it.

Cover, with concrete implementation references threaded throughout rather than clustered in a
bibliography: the problem being solved, the core architecture, reusable pieces versus
integration-specific code, runtime behavior, the data model, the integration seam, security, testing,
architectural decisions, and remaining gaps.

Keep it bullet-driven and honest about gaps. **Stop here and wait for the user to confirm before
moving to Phase 3.** A correction here is real signal about what the guide needs to get right — never
present an unresolved architecture choice as settled without it.

## Plan Synthesis — consolidating findings and decisions into `plan.md`

A different destination than Phase 3: Phase 3 teaches a system to a future engineer; Plan Synthesis
consolidates an already-investigated current state and a set of already-approved user decisions into
a canonical `plan.md` — the input `my-feature-planning` needs so it never has to reconstruct
architecture or product decisions from conversation history.

**Only do this when the user asks for it.** Never produce a `plan.md` as an automatic next step after
Phase 2, and never treat a plain "document/explain X" request as implicitly asking for one.

**Preconditions**, both required: a Phase 1-quality current-state investigation (real, concrete
references — not conventions or guesses), and explicit, user-approved decisions about the target
state. If target-state reasoning or explicit decisions don't exist yet, do that work first — Plan
Synthesis never manufactures a decision on the user's behalf.

Every claim in the plan is exactly one of: a **current-state fact**, a **locked decision**, a
**derived constraint**, or an **open implementation detail** — never blur these together. Full
methodology, the canonical section list, and the pre-finalization review checklist live in
`references/plan-synthesis.md` — read it before writing anything.

State explicitly, at the top of the written section, that it is the source of truth for the
subsequent `my-feature-planning` pass — `rules/plan-md-input.md` checks for this statement before
treating a plan as canonical input.

**Skill boundary.** Plan Synthesis stops at an approved `plan.md`. Feature classification, scope
checklists, design reconciliation, canonical issue definitions, sequencing, and GitHub issue creation
belong to `my-feature-planning` — never pull those responsibilities into this skill.

## Phase 3 — Architecture guide

Only after Phase 2 is approved.

1. Decide the document's structure from the center of gravity identified in Phase 1 and confirmed in
   Phase 2. Architecture guides do not use one fixed section inventory: section structure follows the
   system being explained. Reproduce the reasoning and information hierarchy behind a well-structured
   guide, not the surface shape of any prior one. See `references/doc-style.md` for the writing
   grammar and content-block vocabulary.
2. Load the `artifact-design` skill (required before writing any Artifact page).
3. Write the HTML using `references/template.html` as the starting scaffold. Replace content; keep
   the design system unless the system genuinely needs a new block type.
4. Publish with the `Artifact` tool: title `"{Capability} Architecture"`, a one-sentence description,
   and a stable, domain-appropriate favicon (see `references/doc-style.md#choosing-a-favicon`).
5. Explain architecture, not implementation — why it was built this way and how it's extended. Code
   blocks exist only at genuine extension seams, never as a walkthrough of a whole method body.
6. Before considering the guide complete, run `references/review.md`'s checklist against the
   published guide. This reviews architectural communication, not writing quality.

Publishing through the `Artifact` tool is specific to this output track — Explore, Recap, and Plan
Synthesis's `plan.md` output do not depend on it.

## Phase 4 — Maintenance

When the implementation changes after a guide exists, this phase is governed by
`references/maintenance.md` — read it before making any edit. It is not an editing how-to; it is the
methodology for changing what a guide says without changing the architectural story it tells.

Skeleton: locate the existing guide (`Artifact` tool `action: "list"`, or ask the user) rather than
minting a new one; identify which architectural guarantees actually changed; update only the sections
stating those guarantees; remove completed items from Focused Improvements instead of leaving them
stale; redeploy through the `Artifact` tool with the same `url` and `favicon`; run
`references/review.md` against the sections touched. `references/maintenance.md` governs every
judgment call inside this skeleton.

## Non-negotiables (apply in every phase of the guide pipeline)

- Prefer architecture over implementation; explain concepts before code.
- Distinguish reusable infrastructure from integration-specific code explicitly, in its own section
  or table.
- Explain runtime ownership and lifecycle wherever the system has either — don't invent one for a
  capability with no runtime story.
- Ground security and decision claims in concrete enforcement references where a clear source exists;
  never force a misleading one for formatting's sake.
- No API documentation, no endpoint inventories, no line-by-line implementation walkthroughs, no
  duplicated explanations across sections.
- Finish with intentional limitations, not a generic TODO list — a stated reason beats a bare "should
  add Y eventually."
- A guide is never done until it has passed a `references/review.md` pass — writing and reviewing are
  two separate steps.

Plan Synthesis has its own, separate non-negotiables (the locked-vs-open rule above all) — see
`references/plan-synthesis.md`. Don't apply the guide's rules to a plan, or the plan's rules to a
guide; they serve different readers.
