---
name: my-architecture-laboratory
description: "Methodology for reconstructing and validating an accurate architectural understanding of a reusable capability in this codebase from its real implementation, then handing that understanding off as a guide in the visual/writing style established by the Documents and Tags architecture artifacts — the written guide is the artifact this methodology produces, not the point of it. Trigger on requests to understand, reverse-engineer, or document a reusable capability's architecture: 'help me understand how X actually works', 'reverse-engineer the architecture of X', 'what's the architecture behind X', 'document the architecture of X', 'write an architecture guide/handoff for X', 'produce an architecture recap for X', or a request to explain/teach a reusable capability (polymorphic model, extension point, pipeline, runtime subsystem, notification infrastructure, multitenancy) to a future engineer. Also trigger when asked to update an existing architecture guide after a capability changed. Also trigger for Plan Synthesis — turning an already-investigated current state plus explicit user/product decisions into a canonical `plan.md` that becomes the source of truth for a later `my-feature-planning` pass: 'turn the approved findings and decisions into plan.md', 'synthesize a plan from this investigation', 'write up the target architecture as a plan', 'consolidate this into plan.md before we plan issues', 'turn this into a plan.md'. Do NOT use for a quick explanation of a single function or class, debugging a specific issue, reviewing a diff, API reference docs, README files, code comments, or one-off implementation summaries that aren't meant to teach the architecture."
---

# My Architecture Laboratory

**What this skill actually does:** the hard part of this methodology is Phases 1 and 2 — reconstructing an accurate architectural understanding of a capability from its real implementation, then validating that understanding with the user before writing a word of documentation. Phase 3 hands that already-correct understanding off as a written guide; the guide is the artifact the methodology produces, not the goal it's aiming at. Read the phases below with that emphasis — Phase 3 isn't the task with Phases 1–2 as prep for it; it's the reverse.

Four phases, in order, produce a published architecture guide. Do not skip Explore, do not skip the Phase 2 pause, and do not force a fixed template onto Phase 3 — the capability determines the document, not the other way around.

There is a second, parallel output track — **Plan Synthesis** — for when the goal isn't a teaching guide but a canonical `plan.md` handoff into `my-feature-planning`. It shares Phase 1's investigation discipline and Phase 2's validate-before-writing discipline, but produces a different artifact for a different audience. See "Plan Synthesis" below, after Phase 2 — it is not Phase 5 of the guide pipeline, it's a fork off of Phase 1/2.

The two existing guides this methodology was reverse-engineered from are published Claude Artifacts, not repo files:
- **Reusable Documents Architecture** — `https://claude.ai/code/artifact/7a9c2f1c-bbb5-4241-95b0-7502c4c2bc0b`
- **Centralized Tagging Architecture** — `https://claude.ai/code/artifact/ab74b104-8e43-4301-b46d-9963c2f35449`

If you haven't internalized why those two documents have *different* section names for what looks like "the same" section, read `references/doc-style.md` before writing anything — that's the whole point of this methodology.

This skill encodes four complementary methodologies, each in its own reference and loaded only
when its phase needs it: `references/doc-style.md` is how to *write* a guide (Phase 3);
`references/review.md` is how to *critically review* one (after Phase 3 produces a draft, and
again during Phase 4); `references/maintenance.md` is how to *evolve* one without breaking its
narrative (Phase 4, required before making any edit); `references/plan-synthesis.md` is how to
*consolidate* an investigation and its locked decisions into a canonical `plan.md` (the Plan
Synthesis track below, not part of the four numbered phases). None of these are optional steps
you skip when short on time — an architecture guide is a living engineering asset across all four
phases, and a synthesized plan is a load-bearing handoff document, neither produced once and
forgotten.

## Phase 1 — Explore

Before writing a single word of documentation:

- Read the backend: models, actions/services, controllers, policies, resources, jobs, migrations for the capability.
- Read the frontend: composables, the components that consume them, the pages that integrate them.
- Read the tests — they tell you the real contract and the real boundaries faster than the implementation does.
- If the user asks for it, check GitHub milestones/issues/PRs/commit history for *why* — but the current codebase is the source of truth for *what*. Never document something history says was planned but the code doesn't show.
- Identify the **architectural center of gravity** — the one idea everything else hangs off (a polymorphic contract, a queue pipeline, a runtime subsystem boundary, a sync-vs-async split). You'll need this in Phase 3; form a hypothesis now.

Do not begin writing documentation in this phase — not even a draft.

## Phase 2 — Implementation recap

Write the recap directly as chat output (not a file, not an artifact — that's Phase 3's job). Its only purpose is to prove you understood the system before you spend effort teaching it.

Cover, with implementation file references (`path/to/File.php:method`) threaded throughout, not clustered in a bibliography at the end:

- problem being solved
- core architecture
- reusable backend pieces
- reusable frontend pieces
- runtime behavior
- data model
- integration seam (what a new adopter must supply vs. gets for free)
- security
- testing
- architectural decisions
- remaining improvements

Keep it bullet-driven and honest about gaps — this is a checkpoint, not a sales pitch. **Stop here and wait for the user to confirm before moving to Phase 3.** If they correct something, that correction is real signal about what the guide needs to get right.

## Plan Synthesis — consolidating findings + decisions into `plan.md`

A different destination than Phase 3. Phase 3 teaches a reusable capability to a future engineer.
Plan Synthesis consolidates an already-investigated current state and a set of already-made user
decisions into a canonical `plan.md` — the input document `my-feature-planning` needs so it never
has to reconstruct architecture or product decisions from conversation history.

**Only do this when the user asks for it** — "turn this into a plan," "synthesize plan.md,"
"consolidate the findings and decisions," or equivalent. Never produce a `plan.md` as an automatic
next step after Phase 2, and never treat a plain "document/explain X" request as implicitly asking
for one. Most Phase 1/2 investigations end at the chat recap or a Phase 3 guide; Plan Synthesis is
for the subset that's headed toward `my-feature-planning` next.

**Preconditions.** Plan Synthesis does not investigate or design — it consolidates what's already
on the table:
- A Phase 1-quality current-state investigation (real file/class references, not conventions or
  guesses).
- Explicit, user-approved decisions about the target state. If target-state reasoning hasn't
  happened yet, or decisions are still implicit/assumed rather than stated by the user, do that
  reasoning (informally — it doesn't need its own numbered phase) and get explicit decisions
  *before* synthesizing. Plan Synthesis must never manufacture a decision on the user's behalf to
  fill a gap.

**How to run it.** Full methodology, the canonical section list, the locked-vs-open decision
rule, and the pre-finalization review checklist all live in `references/plan-synthesis.md` — read
it before writing anything. In brief: gather the current-state facts and the locked decisions
already established in conversation; derive the architectural constraints and open implementation
details that follow from them; choose only the canonical sections that fit this initiative; write
`plan.md` (new file, or a clearly-scoped new section in an existing one — ask if it's unclear
which the user wants); state explicitly at the top of the written section that it is the source of
truth for the subsequent `my-feature-planning` pass; run the review checklist; present the result
and wait for approval before treating it as final.

**Skill boundary.** Plan Synthesis stops at an approved `plan.md`. Feature classification, scope
checklists, design reconciliation, canonical issue definitions, sequencing, and GitHub issue
creation all belong to `my-feature-planning` — never pull those responsibilities into this skill,
and never draft or create issues here even if the user's decisions make the eventual issues seem
obvious.

## Phase 3 — Architecture guide

Only after Phase 2 is approved.

1. Decide the document's structure from the center of gravity you identified in Phase 1, confirmed in Phase 2 — don't copy either reference guide's section list. See `references/doc-style.md` for the section-naming lesson (`references/doc-style.md#section-inventory-is-not-fixed`) and the full grammar of content blocks (ascii diagrams, `table.lc`, `flow-steps`, `callouts`, `formula`, `pill`) you'll compose the sections from.
2. Load the `artifact-design` skill (required before writing any Artifact page).
3. Write the HTML to a file using `references/template.html` as the starting scaffold — it carries the CSS, the nav/hero shell, and the syntax-highlighter script already wired up. Replace content; keep the design system unless the capability genuinely needs a new block type.
4. Publish with the `Artifact` tool: title = `"{Capability} Architecture"`, a one-sentence `description`, and a stable domain-appropriate `favicon` emoji (see `references/doc-style.md#choosing-a-favicon`).
5. Explain architecture, not implementation. Teach why it was built this way and how it's extended. Code blocks exist only at genuine extension seams (an interface, a contract method, a scope) — never as a walkthrough of a whole method body.
6. Before considering the guide complete, switch to `references/review.md` and run its checklist against the published guide. This is a review of architectural communication, not writing quality — keep it lightweight: surface findings, don't rewrite prose to address them unless a finding clearly warrants it.

## Phase 4 — Maintenance

When the underlying implementation changes after a guide exists, this phase is governed by
`references/maintenance.md` — read it before making any edit. It's not an editing how-to; it's
the methodology for changing what a guide says without changing the architectural story it's
telling. The steps below are the mechanics; `references/maintenance.md` is what should be
shaping every judgment call you make while doing them.

1. Find the existing guide first (`Artifact` tool, `action: "list"`, or ask the user for the URL) — never mint a new URL for a guide that already exists.
2. Diff your Phase-1-style understanding of the *current* code against what the guide currently claims. Identify only the architectural guarantees that actually changed — `references/maintenance.md` covers what counts as a guarantee versus what doesn't need a documentation change at all.
3. Update only the affected sections and only the affected guarantees within them (often: the specsheet numbers, one row in the decisions table, the runtime ownership table, the improvements list). Never regenerate the whole document, and never write it as a changelog of what happened — state the system as it works now.
4. Remove completed items from Focused Improvements instead of leaving them stale.
5. Preserve the document's own established narrative and section names — don't retrofit the other reference guide's structure onto it just because you're touching it.
6. Redeploy with `Artifact` passing the same `url`, and keep the same `favicon`.
7. Before considering the maintenance pass complete, run `references/review.md` against the sections you touched (not necessarily the whole document) — confirm the edit didn't quietly separate a decision from its trade-off, orphan a runtime-ownership row, or leave a now-completed item sitting in Focused Improvements.

## Non-negotiables (apply in every phase of the guide pipeline)

- Prefer architecture over implementation; explain concepts before code.
- Distinguish reusable infrastructure from integration-specific code, explicitly, in its own section or table.
- Explain runtime ownership and lifecycle wherever the capability has either — but don't invent a "Runtime" section for a capability with no runtime story (pure config, for instance).
- Every security row should include an `src-ref` pointing at the concrete enforcement location. Decision rows should include implementation references when a clear and useful source exists — but don't force a single-file reference onto a decision that's distributed across multiple components or represented by the design as a whole, and never add a misleading source reference just to satisfy formatting consistency. References exist as navigation aids, not proof by citation.
- No API documentation, no endpoint inventories, no controller walkthroughs, no duplicated explanations across sections.
- Finish with intentional limitations, not a generic TODO list — "deliberately deferred until X" beats "should add Y eventually."
- A guide is never "done" until it has passed a `references/review.md` pass — writing it and reviewing it are two separate steps, not one.

Plan Synthesis has its own, separate non-negotiables (the locked-vs-open decision rule above all) — see `references/plan-synthesis.md`. Don't apply the guide's "no API documentation" or "src-ref on every row" rules to a plan; don't apply the plan's "never resolve an open decision" rule to a guide. They're different documents for different readers.