# lab-it — Architecture Dossier

Status: Current
Scope: `lab-it` as it stands in this repository
Purpose: A compact architecture artifact for the skill — its evidence discipline, its two
workflows and where each asks for human confirmation, the distinct stages a piece of work passes
through, the claim model behind a synthesized plan, rule ownership, cross-skill handoffs, and
current boundaries and confidence.
[`SKILL.md`](../skills/lab-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/lab-it/README.md) is the human-facing orientation. This
document explains the architecture behind both rather than restating either.

## 1. Purpose and result model

`lab-it` investigates a real system and turns that investigation into exactly
one of two results — or, just as legitimately, into no artifact at all when understanding is the
whole point. It is not for explaining a single function, debugging, reviewing a diff, or writing
API reference documentation; those questions don't need an architecture investigation, and this
skill doesn't try to answer them. It is also not for creating, updating, or reviewing an
architecture guide — that capability, and its own architecture, belong entirely to
[`document-it`](../skills/document-it/), a separate, independently callable skill (§7).

The two results are genuinely different artifacts, not two names for the same deliverable, and
each sits behind its own human checkpoint:

| Workflow | Terminal output | What gates that output |
|---|---|---|
| Standalone investigation | A verified answer, given as chat output | Nothing further required — the recap itself is the result |
| Plan feature architecture, no material decision remaining | A verified answer recommending `plan-it` directly | Nothing further required — investigation alone establishes the recommendation |
| Plan feature architecture, Plan Synthesis requested and run | An approved `plan.md`, handed to `plan-it` | Explicit decisions approved, then the document itself approved |

Investigation and a recap of it can be the complete, standalone result of a session. A `plan.md` is
something a request specifically asks for, never an automatic next step after investigation.

## 2. The evidence discipline every workflow shares

Before any workflow diverges, both run the same discipline: inspect the real, current system
and its relevant evidence — never conventions or assumptions, and scaled proportionally to the
request rather than exhaustively by default — then reconcile implementation, configuration, schema,
tests, runtime evidence, and reliable history into an explanation that names its own uncertainty
rather than smoothing it over. Reliable findings and already-approved decisions are reused rather
than re-investigated once established.

Authority isn't collapsed into "the code is truth for everything." Implementation is authoritative
for implementation facts; configuration, schema, runtime observations, and external-system state
are each authoritative for whatever they specifically govern. Tests carry real weight — they often
surface an actual behavioral boundary faster than the implementation alone — but they are not
infallible: a test can be incomplete or stale, so it gets reconciled against the implementation and
other evidence rather than trusted at face value. Reliable history (an issue, a commit) explains
*why* something is the way it is; it never by itself establishes *what currently is*, and something
history says was planned but the evidence doesn't show is never documented as if it were real.

The skill states its own posture as one sentence: **the system establishes what exists; the user
decides what it should become.** Everything that follows is that sentence applied differently
depending on which of the two workflows is running — and this same discipline is what
`document-it` reuses, without duplicating it, when its own available evidence is missing or stale
(§7).

## 3. Two workflows, two different confirmation gates

### Standalone investigation

Investigate the architectural surface a request actually calls for — persistence and data
relationships, business rules and lifecycle, request or interaction boundaries, authorization and
security, background or asynchronous work, external integrations, user-facing surfaces and reusable
UI logic, schema and operational constraints — treated as investigation categories, not a fixed
checklist a system must satisfy in full. The result is a recap threading concrete implementation
references through whichever concerns actually apply, given as chat output. No further human
confirmation is required beyond ordinary conversational follow-up: a standalone investigation's
recap *is* the result, not a draft awaiting a separate approval gate the way a guide or a plan is.

### Plan feature architecture

This workflow exists to prepare a real implementation initiative, not to teach a system, and can
start from a feature idea raised in conversation, an architecture question, an existing
investigation, or decisions already approved elsewhere. It investigates how the current system
supports or constrains the proposed feature, discusses viable target approaches with the user,
distinguishes current fact from proposed choice, obtains explicit decisions for the questions that
are genuinely material, and leaves an implementation detail open wherever every viable option
preserves the approved guarantees.

A feature that closely follows established, already-approved conventions does not automatically earn
a design interview or a `plan.md`: existing instances establish conventions, not automatic approval
of new product behavior, so investigation goes only as far as confirming architectural fit and
surfacing a genuine difference before any decision conversation opens. When a decision conversation
is warranted, it scales to what is actually unresolved — the materiality test governs which
questions get asked at all, questions with dependencies are sequenced so foundational choices settle
first, exchanges stay small and coherent with consequences and a recommendation attached, genuinely
ambiguous terms are explored through concrete scenarios rather than abstract definition, and a choice
discussion alone cannot resolve is named as needing further inspection, an experiment, or a
prototype rather than guessed at or silently implemented.

**Plan Synthesis** is this workflow's final writing step, not the whole workflow, and runs only
when the user actually asks for it — never as an automatic next step after investigation, and never
implied by a plain "document/explain X" request. It has two mandatory preconditions: a real
current-state investigation of the same quality a standalone investigation requires, and
explicit, user-approved decisions about the target state. If either is missing, synthesis stops and
returns to that investigation or decision conversation rather than papering over the gap — Plan
Synthesis never manufactures a decision on the user's behalf. See §4 for the claim model it writes
into, and
[`rules/plan-synthesis.md`](../skills/lab-it/rules/plan-synthesis.md) for the full
contract.

## 4. Four stages that don't automatically cascade into each other

The prompt asks for one output, but the work behind it always passes through some subset of four
conceptually distinct stages, and no stage silently produces the next:

1. **Investigation** establishes current reality. It commits to nothing beyond itself — an
   investigation and its recap can be, and often are, the entire session.
2. **Architectural decision-surfacing** is the "the user decides" half of the skill's own maxim,
   applied when planning a feature: approving a target-state choice before synthesis. It is
   distinct from investigation — a decision is a choice about what should become true, not an
   observation about what already is.
3. **Plan Synthesis** is the terminal writing step of the "prepare a change" branch. It consolidates
   an already-investigated current state and already-approved decisions; it does not investigate or
   decide anything itself, and its own preconditions (§3) enforce that.
4. **Downstream feature planning** — `plan-it`'s classification, scope, design
   reconciliation, issue decomposition, sequencing, review, and GitHub issue creation — is
   `plan-it`'s job regardless of which terminal output it starts from (§6). When Plan Synthesis
   produced a `plan.md`, that downstream planning begins only once the user has given a second,
   separate approval: of the synthesized *document itself*, not merely of the decisions that went
   into it before synthesis. That second approval gates the `plan.md` path specifically — it is not
   a universal prerequisite for entering `plan-it`, which starts just as validly from a verified
   answer recommending it directly, with no document and no additional approval gate. This skill's
   involvement ends at whichever terminal output applies.

Two of these four look similar and are not: a decision the user approved *before* Plan Synthesis
establishes what the plan is allowed to say; the user approving the *synthesized document itself*
afterward is what actually makes it canonical for `plan-it`. The handoff statement Plan
Synthesis writes into the plan marks its intended role — it is not evidence that either approval has
happened.

## 5. The claim model behind a plan.md

Every material claim inside a synthesized plan is exactly one of four things, kept visually and
textually distinguishable throughout — never left to blur together in a paragraph:

| Category | What it is | What changes it |
|---|---|---|
| Current-state fact | Verified present reality, grounded in whatever evidence actually governs it (code, configuration, schema, tests, runtime behavior) | Re-checking that same authoritative source |
| Locked decision | A target-state choice the user explicitly approved | Only another explicit user decision |
| Derived architectural constraint | A necessary consequence of verified current-state facts plus one or more locked decisions, with its premises stated | One of its stated premises turning out stale |
| Open implementation detail | An unresolved choice whose every viable outcome preserves the approved architecture and guarantees | Ordinary implementation judgment later, against real codebase conventions |

Materiality is decided by consequence, never by what kind of choice it superficially looks like. The
test: if changing a choice would alter approved behavior, a guarantee, an operator/user promise, a
security boundary, ownership, lifecycle, or the target architecture, it is material and must be
resolved with the user before synthesis — a column type, which of two classes absorbs a few lines of
logic, a CLI flag name, and a UI treatment can each be material or genuinely open, depending only on
what breaks if it changes, not on which of those categories it belongs to. An open detail is
recorded only when leaving it open materially helps downstream planning, not to manufacture
symmetry with the locked decisions or to pad out an otherwise-settled section.

A material decision can never be quietly written as though it were an open implementation detail —
doing so would hide a real decision inside what looks like implementation freedom. Plan Synthesis
runs its own internal review before ever presenting the plan for approval: every locked decision
worded exactly as approved, no material decision disguised as open, the four categories still
distinguishable, each derived constraint's premises actually holding, and no evidence reference that
fails to resolve against its authoritative source right now.

## 6. Rule ownership and cross-skill handoffs

The one rule file this skill owns answers a question no other file does, and is loaded only when
its workflow actually needs it:

| File | Owns |
|---|---|
| [`rules/plan-synthesis.md`](../skills/lab-it/rules/plan-synthesis.md) | The full Plan Synthesis contract: the materiality test consulted throughout the decision conversation as well as at drafting time, preconditions, the four-category claim model, evidence rules, the internal review, and the approval/handoff gate |

Guide-writing, guide-scaffold, guide-review, and guide-maintenance rules — formerly this skill's
own — now live entirely under `document-it` and are not duplicated here; §7 states the boundary.

Outside this skill, two things ever cross to another skill as a governed artifact handoff: an
approved `plan.md`, handed to `plan-it`, and a guide-shaped request, routed to `document-it` (§7). A
verified answer — from a standalone investigation, or from "Plan feature architecture" finding no
material decision — may recommend the user proceed to `plan-it` directly; that recommendation
carries no locked decisions, no artifact, and no approval gate, unlike the `plan.md` path. Once
approved, `plan-it` treats the plan as canonical: it can still validate a
current-state fact against current evidence when drafting issues, and can flag a derived constraint
whose stated premise no longer holds, but it does not re-open a locked decision or re-derive
architecture from scratch. That consumption is governed by
`skills/plan-it/rules/plan-md-input.md` on the other side of the boundary, which recognizes an
approved plan only when the initiative matches and the user's explicit approval is independently
established — never inferred from a polished draft or the file's mere existence. GitHub itself is
`plan-it`'s substrate for that downstream work, not this skill's — this skill never
mutates GitHub and never performs Git workflow.

## 7. Boundary with `document-it`

`document-it` is a separate, independently callable skill, not a narrowed remnant of this one — it
owns guide creation, guide maintenance, and guide review in both Markdown and Artifact form, along
with the rendering, identity, and review architecture those require. This skill does not own, and
this dossier does not describe, any of that architecture — see
[`document-it`'s own dossier](document-it.md).

**The relationship runs in both directions, not one.** This skill's own routing table
(`SKILL.md`'s "What this skill does") recognizes a guide-shaped request — document, update, or
review an architecture guide — as outside its own scope and routes it to `document-it`: that is a
real handoff this skill performs, not merely `document-it` reaching backward into this one. In the
other direction, `document-it` draws on this skill's evidence discipline (§2) only for its own
narrower missing-or-stale-evidence sub-problem, reusing sufficient verified evidence rather than
repeating a full investigation from scratch; an investigation entered this way ends by handing back
verified findings to `document-it`, never by this skill drafting or publishing a guide itself.
Neither direction produces the other skill's terminal output: this skill never publishes a guide,
and `document-it` never reaches an architecture decision with the user or synthesizes a `plan.md`
on its own. File extension does not decide ownership either way: an approved `plan.md` stays this
skill's even though it's a `.md` file, and a Markdown architecture guide is `document-it`'s even
though it isn't an Artifact.

## 8. Boundaries, non-goals, and current confidence

This skill owns architecture investigation, architectural explanation, surfacing and resolving
material decisions with the user, and synthesis of approved architecture into `plan.md`. It does
not own application implementation, debugging or diff review, API reference documentation, guide
creation/maintenance/review (§7), feature classification, issue decomposition, GitHub issue
mutation, delivery sequencing, or Git workflow — those stay with `document-it`, `plan-it`, and the
consuming project.

This skill's two external handoffs — an approved `plan.md` to `plan-it`, and a guide-shaped request
routed to `document-it` (§7) — do not make this skill tracker- or stack-specific.

**Architectural coherence.** Two workflows produce two genuinely distinct outputs — a verified
answer and a decision handoff — under one shared evidence discipline, with a single owned rule file
and a clearly stated, reciprocal boundary with `document-it`: each skill routes the other's
shaped requests to it, and neither performs the other's terminal output.

**Current, honest limits:**

- The investigation vocabulary, the claim model, and the plan-synthesis method are written without
  framework- or stack-specific vocabulary in the current rule file — that is a property of how the
  file is currently written, not an empirically exercised claim about how well it generalizes to
  every consuming project's stack.
- The Plan Synthesis → `plan-it` handoff depends on both skills agreeing on the same
  materiality test and the same recognition procedure. That agreement holds because both sides read
  from the same owning files named in §6 — it is not independently enforced at runtime by either
  skill.
- This dossier's own narrowing — separating this skill's architecture from `document-it`'s — has
  been checked against both skills' current `SKILL.md`/`README.md` files and the repository's
  cross-references, not against a live consumer exercise of either skill.
