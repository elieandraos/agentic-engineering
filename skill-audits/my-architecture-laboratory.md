# my-architecture-laboratory — Architecture Dossier

Status: Current
Scope: `my-architecture-laboratory` as it stands in this repository
Purpose: A compact architecture artifact for the skill — its evidence discipline, its three
workflows and where each asks for human confirmation, the distinct stages a piece of work passes
through, the claim model behind a synthesized plan, how a published guide is built and reviewed,
rule ownership, cross-skill handoffs, and current boundaries and confidence.
[`SKILL.md`](../my-architecture-laboratory/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../my-architecture-laboratory/README.md) is the human-facing orientation. This
document explains the architecture behind both rather than restating either.

## 1. Purpose and result model

`my-architecture-laboratory` investigates a real system and turns that investigation into exactly
one of three results — or, just as legitimately, into no artifact at all when understanding is the
whole point. It is not for explaining a single function, debugging, reviewing a diff, or writing
API reference documentation; those questions don't need an architecture investigation, and this
skill doesn't try to answer them.

The three results are genuinely different artifacts, not three names for the same deliverable, and
each sits behind its own human checkpoint:

| Workflow | Terminal output | What gates that output |
|---|---|---|
| Document existing architecture | A new Claude Artifact architecture guide | The user confirms the investigation recap |
| Update an existing architecture guide | The same Artifact, redeployed | Only when authority, intent, or a material decision is unclear |
| Plan feature architecture | An approved `plan.md`, handed to `my-feature-planning` | Explicit decisions approved, then the document itself approved |

Investigation and a recap of it can be the complete, standalone result of a session. A guide and a
`plan.md` are outputs someone has to actually ask for — neither gets produced automatically just
because an investigation happened.

## 2. The evidence discipline every workflow shares

Before any workflow diverges, all three run the same discipline: inspect the real, current system
and its relevant evidence — never conventions or assumptions — then reconcile implementation,
configuration, schema, tests, runtime evidence, and reliable history into an explanation that names
its own uncertainty rather than smoothing it over.

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
depending on which of the three workflows is running.

## 3. Three workflows, three different confirmation gates

### Document existing architecture

Investigate every architectural surface the system actually has — persistence and data
relationships, business rules and lifecycle, request or interaction boundaries, authorization and
security, background or asynchronous work, external integrations, user-facing surfaces and reusable
UI logic, schema and operational constraints — treated as investigation categories, not a fixed
checklist a system must satisfy in full. Investigation also produces a working hypothesis for the
system's **architectural center of gravity**: the one idea everything else hangs off (a shared
contract, a pipeline, a runtime boundary, a data-ownership split).

The recap is written as chat output, never as a file or an artifact, threading concrete
implementation references through whichever concerns actually apply — the problem being solved,
the core architecture, reusable pieces versus integration-specific code, runtime behavior, the data
model, security, testing, decisions, and remaining gaps. This is where the workflow stops and waits:
the investigation does not become a published guide until the user confirms the recap. A correction
here is real signal about what the guide needs to get right, caught before any structure or prose
gets written around it.

Only after that confirmation does the workflow write and publish: decide the guide's structure from
the confirmed center of gravity, load `artifact-design` (required before writing any Artifact
page), build the HTML from the template, publish it, and run the guide review before calling it
done (§6).

### Update an existing architecture guide

This is demand-triggered, not an automatic fourth stage that follows guide creation: a stale
architectural claim, a stale evidence reference, changed configuration or runtime behavior, or a
prior documentation defect all trigger it, independent of whether the implementation itself
changed. [`rules/maintenance.md`](../my-architecture-laboratory/rules/maintenance.md) governs every
judgment call inside it.

The human gate here is narrower than the other two workflows, deliberately: the user is asked only
when authority, intent, or a material decision is unclear. Reconciling a guide with an
already-settled reality is not a new product decision, so it doesn't need one. Concretely,
`maintenance.md` classifies what a reconciliation pass finds into one of four outcomes — no
documentation event (leave it alone), a narrow update (correct one fact or reference in place), a
connected architectural change (follow the complete dependent claim graph, not only the section
where the change was first noticed), or unresolved authority/intent/a material decision (stop, and
route it back through this same shared discipline rather than deciding it during maintenance). This
four-way classification is specific to *how a maintenance pass triages what it finds*; it is a
different mechanism from the four-category claim model a synthesized plan uses (§5) — the two
should not be conflated.

Continuity means preserving every unaffected claim, explanation, and presentation choice — not
rewriting nearby prose merely because the file is open, and not restructuring for taste or
conformity with some other guide's shape. Continuity is not the same as freezing the guide's center
of gravity, ownership, or reasoning in place: when verified architecture has actually moved one of
those, the guide moves with it, in proportion to what changed. The guide's identity survives every
maintenance pass unchanged (§6), and the whole updated guide — not only the touched sections — goes
back through the guide review, with emphasis on the changed claims and whatever depends on them.

### Plan feature architecture

This workflow exists to prepare a real implementation initiative, not to teach a system, and can
start from a feature idea raised in conversation, an architecture question, an existing
investigation, or decisions already approved elsewhere. It investigates how the current system
supports or constrains the proposed feature, discusses viable target approaches with the user,
distinguishes current fact from proposed choice, obtains explicit decisions for the questions that
are genuinely material, and leaves an implementation detail open wherever every viable option
preserves the approved guarantees.

**Plan Synthesis** is this workflow's final writing step, not the whole workflow, and runs only
when the user actually asks for it — never as an automatic next step after investigation, and never
implied by a plain "document/explain X" request. It has two mandatory preconditions: a real
current-state investigation of the same quality "Document existing architecture" requires, and
explicit, user-approved decisions about the target state. If either is missing, synthesis stops and
returns to that investigation or decision conversation rather than papering over the gap — Plan
Synthesis never manufactures a decision on the user's behalf. See §5 for the claim model it writes
into, and
[`rules/plan-synthesis.md`](../my-architecture-laboratory/rules/plan-synthesis.md) for the full
contract.

## 4. Five stages that don't automatically cascade into each other

The prompt asks for one output, but the work behind it always passes through some subset of five
conceptually distinct stages, and no stage silently produces the next:

1. **Investigation** establishes current reality. It commits to nothing beyond itself — an
   investigation and its recap can be, and often are, the entire session.
2. **Architectural decision-surfacing** is the "the user decides" half of the skill's own maxim,
   applied at a different moment in each workflow: confirming a recap (document), approving a
   target-state choice before synthesis (plan), or resolving unclear authority (update). It is
   distinct from investigation — a decision is a choice about what should become true, not an
   observation about what already is.
3. **Guide publication** (new or updated) is the terminal output of the "teach a system" branch. A
   new guide never publishes before its recap is confirmed; neither a new nor an updated guide is
   considered finished before it passes the guide review (§6). Publishing or updating a guide never
   automatically hands anything to the planning workflow — it is a complete, standalone result of
   its own.
4. **Plan Synthesis** is the terminal writing step of the "prepare a change" branch. It consolidates
   an already-investigated current state and already-approved decisions; it does not investigate or
   decide anything itself, and its own preconditions (§3) enforce that.
5. **Downstream feature planning** — `my-feature-planning`'s classification, scope, design
   reconciliation, issue decomposition, sequencing, review, and GitHub issue creation — begins only
   once the user has given a second, separate approval: of the synthesized *document itself*, not
   merely of the decisions that went into it before synthesis. This skill's involvement ends at that
   approved `plan.md`; everything from there is `my-feature-planning`'s job (§7).

Two of these five look similar and are not: a decision the user approved *before* Plan Synthesis
establishes what the plan is allowed to say; the user approving the *synthesized document itself*
afterward is what actually makes it canonical for `my-feature-planning`. The handoff statement Plan
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
fails to resolve against its authoritative source right now. This review is specific to Plan
Synthesis — a different check from the guide review in §6, which never applies to a plan.

## 6. The architecture guide as a published artifact

A guide's section list is decided by the confirmed center of gravity, not poured into a fixed
inventory — two guides for two different capabilities legitimately have different section counts,
names, and content. What *is* fixed is the rhythm each section opens with (a numbered head, an
italicized question a reader would actually ask, then one direct-answer paragraph) before choosing
whichever content blocks actually fit — a spec strip of concrete operational facts, an
ownership/flow diagram, a responsibility table, an ordered timeline, a callout, a formula recap, a
variant badge, or a closing sentence. See
[`rules/doc-style.md`](../my-architecture-laboratory/rules/doc-style.md) for the full grammar; this
dossier does not restate its content-block vocabulary.

**Identity.** A guide's title follows `"{Capability} Architecture"`. Its favicon is one or two
domain-appropriate emoji, supplied at first publish and re-supplied unchanged on every redeploy —
a changed favicon reads as a different document, so a maintenance pass discovers or confirms the
guide's current favicon before touching anything rather than silently picking a new one. Maintaining
a guide redeploys through the same `url`; a new guide is never minted to stand in for updating an
existing one.

**Rendering.** [`rules/template.html`](../my-architecture-laboratory/rules/template.html) is a
self-contained scaffold by explicit operational constraint: no `DOCTYPE`/`html`/`head`/`body`
wrapper (the Artifact tool supplies those at publish time), and no external requests or CDN
dependency — every rule and every script is inline. Theming runs on CSS custom properties across
three coexisting paths: a light default on bare `:root`, a `prefers-color-scheme: dark` media
override, and an explicit `data-theme="dark"`/`"light"` attribute override that wins in both
directions over the media query. The layout is a responsive two-column shell — a sticky section nav
beside the main content column — that collapses to one column under an 880px breakpoint. The syntax
highlighter enhances exactly five disclosed `data-lang` values (PHP, TS, Vue, JSON, HTTP) with token
coloring and a tinted label; every other case — an unsupported-but-present `data-lang`, or none at
all — still reaches an HTML-escaped, unhighlighted plain-code fallback rather than being skipped or
left unescaped.

**Accessibility.** The template carries specific, verifiable signals: `:focus-visible` outlines on
interactive elements, one `aria-label="Sections"` on the nav landmark, a
`prefers-reduced-motion: reduce` override that disables smooth scrolling, and a semantic heading
hierarchy (`h1` hero, `h2` per section, `h3`/`h4` for subdivisions). These are signals, not a
certified contract — no formal accessibility audit (measured contrast ratios, for example) is built
into this skill, and none is claimed here.

**Review.** [`rules/review.md`](../my-architecture-laboratory/rules/review.md) is a check on
whether a *finished* guide actually communicates the architecture, run only against a published
Artifact or the exact draft being proposed — never mid-draft, since drafting is `doc-style.md`'s
job, not this one. Its checklist categories (architectural center; responsibility and ownership;
reuse/integration/variation; runtime, lifecycle, and state; architecture versus implementation;
structure and content; consistency; decisions and limitations) are each conditional on the
architecture actually having that concern — an inapplicable category is skipped, not failed. A
known, honestly-stated gap is not itself a finding; an unstated one is. The output is a short list
of findings ordered by consequence, never a rewrite — the review reports, and the guide's author
decides what to act on.

## 7. Rule ownership and cross-skill handoffs

Every file under `rules/` answers a question none of the others do, and is loaded only when its
workflow actually needs it — none is a universal prerequisite. `template.html` is deliberately not
called a rule: it's a scaffold to edit, not a normative statement the way the other four are.

| File | Owns |
|---|---|
| [`rules/doc-style.md`](../my-architecture-laboratory/rules/doc-style.md) | The writing grammar for guides: section rhythm, the content-block vocabulary, tone and evidence discipline, favicon stability |
| [`rules/template.html`](../my-architecture-laboratory/rules/template.html) (scaffold, not a rule) | The Artifact HTML/CSS/JS: the theme tokens, the responsive shell, the content-block CSS classes, the highlighter and its fallback contract |
| [`rules/review.md`](../my-architecture-laboratory/rules/review.md) | Judging whether a finished guide communicates its architecture |
| [`rules/maintenance.md`](../my-architecture-laboratory/rules/maintenance.md) | Reconciling an existing guide with verified current reality without breaking its identity or unaffected meaning |
| [`rules/plan-synthesis.md`](../my-architecture-laboratory/rules/plan-synthesis.md) | The full Plan Synthesis contract: preconditions, the four-category claim model, evidence rules, the internal review, and the approval/handoff gate |

Outside this skill, the only thing that ever crosses a boundary is an approved `plan.md` — a
published or updated guide is a complete result on its own and never implies a downstream handoff.
Once approved, `my-feature-planning` treats the plan as canonical: it can still validate a
current-state fact against current evidence when drafting issues, and can flag a derived constraint
whose stated premise no longer holds, but it does not re-open a locked decision or re-derive
architecture from scratch. That consumption is governed by
`my-feature-planning/rules/plan-md-input.md` on the other side of the boundary, which recognizes an
approved plan only when the initiative matches and the user's explicit approval is independently
established — never inferred from a polished draft or the file's mere existence. GitHub itself is
`my-feature-planning`'s substrate for that downstream work, not this skill's — this skill never
mutates GitHub and never performs Git workflow.

## 8. Boundaries, non-goals, and current confidence

This skill owns architecture investigation, architectural explanation, surfacing and resolving
material decisions with the user, new architecture guides, maintenance of existing guides, and
synthesis of approved architecture into `plan.md`. It does not own application implementation,
debugging or diff review, API reference documentation, feature classification, issue decomposition,
GitHub issue mutation, delivery sequencing, or Git workflow — those stay with `my-feature-planning`
and the consuming project regardless of which of the three workflows ran.

Two dependencies are deliberate, named openly rather than disguised as neutrality: the guide
workflow publishes through the Claude Artifact tool and the `artifact-design` skill; the planning
workflow's only external handoff is an approved `plan.md` to `my-feature-planning`. Neither makes
this skill tracker- or stack-specific.

**Architectural coherence.** Three workflows produce three genuinely distinct outputs — a taught
guide, a maintained guide, a decision handoff — under one shared evidence discipline, with five rule
files each answering a question the others don't, and no file claiming a boundary another one owns.

**Current, honest limits:**

- The Artifact identity, rendering, and accessibility contract described in §6 is stated as an
  explicit operational constraint inside the template and its own inline documentation. Nothing in
  this skill's files independently confirms how a specific renderer actually displays a published
  guide — the guide review checks whether a guide communicates architecture, not whether a rendered
  page meets a measured contrast ratio or a formal accessibility standard.
- The syntax highlighter enhances five named languages with a disclosed, safe fallback for anything
  else — a bounded, honestly-scoped renderer capability, not a hidden assumption, but still a literal
  list: a guide documenting a system in an unlisted language renders that code unhighlighted, not
  mis-rendered.
- The investigation vocabulary, the claim model, and the structure-follows-architecture principle
  are written without framework- or stack-specific vocabulary in any current rule file — that is a
  property of how the files are currently written, not an empirically exercised claim about how well
  they generalize to every consuming project's stack.
- The Plan Synthesis → `my-feature-planning` handoff depends on both skills agreeing on the same
  materiality test and the same recognition procedure. That agreement holds because both sides read
  from the same owning files named in §7 — it is not independently enforced at runtime by either
  skill.
