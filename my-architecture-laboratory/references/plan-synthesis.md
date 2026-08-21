# Synthesizing a plan.md

This is the methodology for the Plan Synthesis track referenced from `SKILL.md`. It turns an
already-investigated current state plus a set of already-approved user decisions into a canonical
`plan.md` — a handoff document, not a teaching document. Nothing here is specific to any one
initiative; the same procedure applies whether the subject is a cross-cutting capability, an
existing subsystem redesign, a major refactor, a new architectural initiative, an integration, or
a security/auth-shaped piece of work.

## What this is for, and what it is not for

A `plan.md` produced here exists to let `my-feature-planning` start from settled architecture and
settled product decisions instead of reconstructing them from conversation history. It is:

- A **consolidation** of what's already been investigated and decided — not a place to do new
  investigation or make new decisions.
- **Implementation-aware** — it names real files, classes, and conventions the eventual issues
  will touch — but **not an implementation checklist**. It states what must be true, not the
  literal sequence of edits.
- The **source of truth** for the subsequent feature-planning pass. Once approved, `my-feature-planning`
  should not need to re-derive architecture or re-litigate decisions from this conversation.

It is not:
- A replacement for Phase 3's architecture guide. A guide teaches a reusable capability to a
  future engineer, independent of any particular change. A plan exists to unblock one specific
  initiative's move into issue planning, and has no reason to outlive that initiative.
- A place to classify the feature, scope it, reconcile it against design files, draft issues, or
  touch GitHub. All of that is `my-feature-planning`'s job, done *after* the plan is approved.

## Preconditions

Don't start writing until both of these are actually true — don't paper over a gap in either:

1. **A real current-state investigation exists.** Concrete file/class/route/test references, not
   conventions or assumptions. If this hasn't happened, that's Phase 1 work, not Plan Synthesis.
2. **The user has made explicit decisions about the target state.** Not implied by the
   investigation, not inferred from "what would make sense" — stated by the user, in this
   conversation or a prior one you can point to. If target-state reasoning hasn't happened yet,
   do that reasoning first (informally — it doesn't need a named phase of its own) and surface the
   decisions that actually need the user's input before synthesizing anything.

If the user asks for a plan before either precondition is met, say so and do the missing work
first rather than synthesizing around the gap.

## The locked-vs-open decision rule

This is the single most important discipline in Plan Synthesis, and the one most likely to be
violated by accident under time pressure. Every claim in the plan falls into exactly one of four
buckets, and the plan must keep them visually and textually distinguishable — never let a
paragraph blur two of them together:

- **Current-state fact** — what the code does today. Falsifiable by reading the repo right now.
- **Locked decision** — something the user explicitly approved as a constraint on the target
  state. Falsifiable only by asking the user again.
- **Derived architectural constraint** — something that necessarily follows from a locked decision
  plus the current-state facts, even though the user never stated it in those exact words (e.g. a
  decision to remove a code path implies a consumer of that path now needs a new source of the
  same data). Mark these as derived, not as if the user had stated them directly.
- **Open implementation detail** — a genuine implementation choice the user has *not* made, that
  doesn't change the target architecture regardless of which way it's resolved. Left for
  feature-planning or implementation to resolve against actual codebase conventions at build time.

A rough test for locked vs. open: if flipping the choice would change what the system *guarantees*
or *promises* to its users/operators, it's a product decision — surface it as locked-or-still-open,
don't quietly decide it yourself. If flipping the choice only changes *how* that guarantee is
implemented (a column type, which of two existing classes absorbs a few lines of logic, a CLI flag
name, which of several equally-valid UI treatments a recommendation gets), it's an open
implementation detail — record it as open, with the real options on the table, and stop there.

**Never silently convert an open implementation choice into a locked product decision** by writing
it as though the user had approved one specific solution. If a section needs to reference an
undecided detail to stay coherent, name the open question and the candidate options inline, and
point to the "Open Implementation Decisions" section rather than picking one.

**Never invent an unresolved requirement merely to make the plan look complete.** A short "Open
Implementation Decisions" list beats a padded one. If everything about a section really is
settled, say so plainly and move on — don't manufacture a question for symmetry.

## Canonical plan structure

Use only the sections that carry real content for this initiative. A plan with three sections
because the initiative is narrow is correct; forcing all of these into a small change just because
the list exists is the failure mode to avoid — the same "don't force a fixed template" discipline
Phase 3 applies to guides applies here to plans.

```
# <Initiative>

## Context / Problem
What exists today and what problem or goal motivates the change.

## Current State
Relevant existing behavior, architecture, constraints, and coupling discovered in the investigation.

## Approved Target Architecture
The agreed future-state design.

## Locked Decisions
Explicit product/architecture decisions made by the user.

## Preserved Behavior / Existing Pieces
What must remain unchanged or be reused.

## Changes
What needs to be introduced, removed, moved, or rewired conceptually.

## Invariants / Boundaries
Security, tenancy, state-model, authorization, lifecycle, or architectural rules implementation
must preserve.

## Open Implementation Decisions
Implementation details deliberately left unresolved for feature-planning/implementation to
resolve against codebase conventions.

## Security / Failure / Recovery
Only when relevant.

## Tests / Behavioral Impact
What existing behavior must remain valid and what new behavior needs proof.

## Before → After
A concise lifecycle/system comparison when useful.

## Source References
Concrete files/classes/routes/tests used as evidence.
```

Thread concrete references (`path/to/File.php:method`, route names, test names) through the
sections where they're actually relevant, the same way Phase 2 threads them through a recap —
don't cluster everything into "Source References" and leave the rest of the document abstract.
`Source References` exists for material that doesn't have one natural home in the sections above,
not as the only place citations are allowed to live.

## Where the plan lives

Default to a `plan.md` at the repository root. If one already exists for the project (general
context, other initiatives), append a clearly-scoped new top-level section rather than overwriting
or restructuring what's there — preserve existing content exactly as Phase 4 preserves a guide's
established narrative when maintaining it. If it's unclear whether the user wants a new file, a
new section in the existing file, or something else, ask rather than guessing.

State explicitly, at the top of whatever section you write, that it is the source of truth for the
subsequent `my-feature-planning` pass, and that implementation details still need verifying
against the codebase when individual issues are actually built (the codebase will have moved on by
then; the plan captures decisions, not a frozen snapshot of every line number).

## Review pass — required before presenting the plan

Do not write the plan and immediately consider it finished. Before presenting it for approval, run
this checklist against your own draft:

- **Locked decisions preserved** — does every locked decision from the conversation appear in the
  plan, worded so it still matches what the user actually approved (not softened, not expanded)?
- **No open decision accidentally resolved** — for every item that should be open, does the plan
  actually leave it open, with real options named, rather than picking one and moving on?
- **No current-state fact presented as future-state design** — could a reader mistake "what the
  code does today" for "what we've decided it should do"? These need to read differently, not just
  live in different sections.
- **No superseded architecture described as current** — if target-state reasoning went through
  more than one iteration in conversation, does the plan reflect only the final approved shape, not
  an earlier draft that was later corrected?
- **References resolve** — do the file/class/route/test references actually exist, at the paths
  named, in the current codebase? Don't carry forward a reference from memory without checking it
  against what you actually read during the investigation.
- **Internal consistency** — does any section contradict another (a "Preserved Behavior" item that
  a "Changes" item quietly removes; an "Invariant" that a described change would violate)?
- **Fit for feature-planning** — could `my-feature-planning` start from this plan without needing
  to ask the user (or re-derive from conversation) what was decided versus what's still open?

Report findings from this pass the same way Phase 3's review does — a short list, not a rewrite —
then fix what the findings surface before presenting the plan. If the user later asks for
corrections, apply them precisely and re-run the parts of this checklist the correction could have
affected (see the pattern of a targeted consistency pass, not a full re-review, for a small fix).

## Approval gate

Present the synthesized plan (or the specific sections changed, for a revision) and wait for the
user's explicit approval before treating `plan.md` as finalized. A plan that hasn't been approved
is a draft, not a source of truth — don't hand it to `my-feature-planning` and don't imply it's
settled in any other way until the user has actually signed off.
