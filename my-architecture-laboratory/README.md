# my-architecture-laboratory

A "before we code, document, or redesign" skill for understanding important parts of a system and
deciding what should happen next. Read this if you want to understand what the skill is for and why
it works the way it does. For the exact steps it follows, read `SKILL.md` and the files in
`references/` — this document explains the idea, not the operational detail.

## Two main ways to use it

### 1. Understand and document an existing capability

Use this when the goal is to understand how an existing subsystem works — nothing is changing yet,
you just need the real picture.

```
existing capability → investigate → validate understanding with the human → architecture guide
```

**Output:** a published Architecture Artifact that explains how the existing system works, why
it's shaped that way, and how it can be extended.

### 2. Understand and plan a new capability or a major change

Use this when the goal is to change an existing system or build something new, and the
architecture needs to be settled before anyone plans issues or writes code.

```
existing system / new capability → investigate → discuss target architecture
→ make product/architecture decisions → plan.md → my-feature-planning
```

**Output:** a canonical `plan.md` that captures the agreed target state and the constraints the
next planning step has to respect.

The distinction in one line each:

> **Architecture guide** → "How does this system work, and why?"
> **`plan.md`** → "What are we agreeing to build or change, and what must stay true?"

Sometimes both are involved. A capability may already have an architecture guide, and a planned
change to it may still need fresh investigation before a `plan.md` can be written. After the change
ships, the same architecture guide can be updated to reflect the new reality.

## How the investigation works

Both branches start the same way: understand the real system before touching it. The difference
comes after the investigation. Branch 1 turns that understanding into an Architecture Artifact.
Branch 2 uses that understanding as the starting point for target-state discussion, user decisions,
and eventually `plan.md`. Plan Synthesis itself does not investigate or make new decisions; it
consolidates what we have already learned and decided.

```
inspect the real system → understand how it actually works → identify boundaries and existing precedents
→ form a target-state hypothesis → surface decisions for the human → validate before writing the final artifact
```

The guiding principle:

> **The codebase tells us what exists. The human decides what it should become.**

Tests get special weight here. They're not just extra reading — they're evidence of the real
behavioral contract. Code can look like it does one thing while a test proves the actual boundary
is somewhere else; tests win.

This is also why the skill isn't a code generator. It doesn't start by picking an implementation —
writing anything (guide or plan) is the last step, not the first, and it only happens after the
human has validated the understanding it's based on.

## Branch 1 in detail: the architecture guide workflow

Four phases, always in order:

**Phase 1 — Explore**
Read the backend, frontend, tests, database, routes, policies, jobs — whatever is actually part of
this capability. Look for its architectural center of gravity: the one idea everything else in the
system hangs off. Nothing gets written for the human yet — no draft, no outline.

**Phase 2 — Recap and validate**
Tell the human what was found, in plain chat, not a document. This is the important checkpoint.
It's much cheaper to catch a wrong assumption here than after a whole guide has been built around
it. If the human corrects something, that correction is real signal — it means the final artifact
needs to get that part right.

**Phase 3 — Architecture guide**
Only starts after the recap is approved. The result is a **published Artifact** — not just a
Markdown file — built using the visual/document design system in `references/template.html` and
`references/doc-style.md`, following the `artifact-design` workflow before publishing. Once
published, the skill runs an architecture review checklist (`references/review.md`) against it
before calling it done. The exact template and document grammar aren't repeated here — that's what
`SKILL.md` and the reference files are for. The one thing worth knowing at this level: the guide's
structure is shaped around *this capability's* center of gravity, not poured into one fixed,
universal section list.

**Phase 4 — Maintenance**
When the implementation changes later, the skill can update the existing guide instead of writing a
new one. It compares the current code against what the guide currently claims, updates only the
architectural guarantees that actually changed, keeps the guide's existing narrative and its URL,
and re-runs the review checklist on the sections it touched.

## Branch 2 in detail: Plan Synthesis

Plan Synthesis is the planning branch (use case 2 above) — a separate path from the architecture
guide workflow, not a Phase 5 that always happens after Phase 3. It's used when the point of the
architecture work isn't teaching — it's preparing a real implementation initiative.

```
investigation → target-state discussion → user-approved decisions → plan.md → my-feature-planning
```

`plan.md` is the handoff document into `my-feature-planning`. It is:

- The **source of truth** the next planning pass starts from.
- **Implementation-aware** — it names real files and classes, not vague descriptions.
- **Not a literal list of code edits**, and **not a list of GitHub issues.** Those come later.

The part that's easy to get wrong, and matters most: every claim in the plan has to be clearly one
of four kinds, and they must never blur together:

- **current-state fact** — what the code does today
- **locked decision** — something the human explicitly approved
- **derived constraint** — something that necessarily follows from a locked decision, even though
  no one said it in those words
- **open implementation detail** — a real choice nobody has made yet, left for later

Example:

> "Public signup is being removed" — **locked decision**.
> "Something else must now create the first Owner" — **derived constraint** (follows from the
> decision above).
> "Use a boolean column or a timestamp to represent it" — **open implementation detail**, left
> unresolved on purpose.

The plan must never quietly pick an answer to an open implementation detail just to look more
finished. If it's genuinely undecided, it stays listed as open, with the real options named.

## What the skill owns

**my-architecture-laboratory owns:**
- Investigating the real architecture
- Reasoning about the target state
- Surfacing the decisions that need a human
- Recording the decisions once made
- Writing the architecture guide
- Synthesizing `plan.md`

**my-architecture-laboratory does NOT own:**
- Writing application code
- Classifying or scoping a feature
- Drafting or creating GitHub issues
- Managing milestones or labels
- Sequencing a batch of issues

Everything in that second list is `my-feature-planning`'s job. The handoff is simple:

```
my-architecture-laboratory → approved architecture guide OR approved plan.md → my-feature-planning
```

## What a good result looks like

- A good investigation **tells us how the system really works** — not how it's supposed to work,
  not how similar things usually work.
- A good architecture discussion **makes the important choices explicit**, instead of leaving them
  implied.
- A good architecture guide **explains how the system works and why**, so a future engineer can
  extend it correctly without re-deriving the reasoning.
- A good `plan.md` **records the agreed target so the next planning step doesn't have to
  reconstruct the conversation** — no missing decisions, no ambiguity about what's locked vs. open.

## What it should avoid

- Guessing from framework conventions instead of reading the actual code.
- Trusting an old plan, PR description, or ticket over what the code does today.
- Inventing a "cleaner" abstraction because it looks nicer, not because it's actually there.
- Making a product decision on the user's behalf instead of asking.
- Writing the final guide or plan before the system is genuinely understood.
- Turning the architecture guide into an API or endpoint reference.
- Turning `plan.md` into a task checklist.
- Mixing architecture work with GitHub issue planning — that boundary belongs to
  `my-feature-planning`.

## Is this portable?

The way of thinking — understand before you document, validate before you write, keep facts and
decisions and open questions separate, find the center of gravity — isn't specific to this project
and could apply to any codebase.

The skill as it's actually written today is not that generic yet. It assumes things specific to
this project: this project's Laravel/Vue stack, its particular Artifact publishing workflow for
architecture guides, the existence of `plan.md`, and a handoff to `my-feature-planning`.

> The methodology is reusable. The current implementation of the skill is still project-specific.

If portability ever becomes a real goal, that would mean separating the reusable reasoning from
these project-specific pieces — that separation hasn't happened yet.

## Relationship to the other skill

```
my-architecture-laboratory  →  understand / decide / document / synthesize plan
my-feature-planning      →  classify / scope / reconcile / sequence / draft issues / GitHub
```

The two skills stop at different, intentional boundaries. `my-architecture-laboratory` never drafts a
GitHub issue; `my-feature-planning` never re-investigates architecture or re-decides something this
skill already settled. Each one trusts the other to do its part.

---

`my-architecture-laboratory` helps us understand what the system is, decide what it should become, and
capture that decision as either an architecture guide or a planning-ready `plan.md`.
