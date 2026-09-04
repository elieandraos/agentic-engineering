# plan-it — Architecture Dossier

Status: Current
Scope: `plan-it` as it stands in this repository
Purpose: A compact architecture guide to the skill — what it transforms and produces, its two work
origins and how they converge, where authority actually lives, its classification/scope/design/
decomposition/review/mutation model, how its rules divide ownership, why GitHub is a deliberate
substrate rather than incidental tooling, and its current boundaries and confidence.
[`SKILL.md`](../skills/plan-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/plan-it/README.md) is the human-facing walkthrough. This document
explains the architecture behind both rather than restating either.

## 1. Purpose and result boundary

`plan-it` turns three kinds of input — an intentional feature ask raised in
conversation, an approved `plan.md` initiative section, or a validated Discovered-work finding —
into an approved, reviewed set of GitHub issues (with whatever milestone/label/assignee metadata
the work actually needs). It owns planning and GitHub issue creation. It does not own architecture
decisions: for an approved `plan.md` section, those are already settled upstream before this skill
starts (§3); a direct feature conversation carries no such guarantee, and scope discovery can still
surface a material product or architecture question that must be routed to the user before the
affected drafting proceeds. It does not own application implementation, which begins only after an
issue this skill created has been approved and picked up downstream.

GitHub is not an interchangeable stand-in for "some tracker." The skill's methodology — classify,
scope, reconcile design, draft, review, sequence, create — is portable across GitHub-based projects
with different stacks and conventions; it is not written to be tracker-agnostic. Reference syntax,
milestone/label semantics, and the mutation/validation model are all shaped around what GitHub
specifically provides, and are covered on their own terms throughout this dossier rather than
treated as an implementation detail to abstract away.

## 2. Two work origins, one pipeline

Every planning session starts from one of two origins, and both converge on the identical
downstream pipeline — classification, scope discovery, drafting, sequencing, review, and creation —
with no lighter-weight path for either:

| Origin | What it starts from | Entry point into the shared pipeline |
|---|---|---|
| **Planned work** — feature conversation | An intentional proposed change with scope not yet worked out | Classification |
| **Planned work** — approved `plan.md` | An initiative-specific section [`lab-it`](../skills/lab-it/) has already investigated and the user has already approved, with architecture and decisions canonical | Classification, with architecture and locked decisions already resolved (see [`rules/plan-md-input.md`](../skills/plan-it/rules/plan-md-input.md)) |
| **Discovered work** | An unexpected finding — surfaced during implementation, review, testing, operations, or another workflow — with scope not yet known | [`rules/discovered-work.md`](../skills/plan-it/rules/discovered-work.md)'s investigation; only a *validated* finding reaches classification |

An approved `plan.md` section changes *what already has answers* by the time classification runs —
its architecture and locked decisions are canonical input, not a shortcut around any later step or
gate. A raw Discovered finding changes *what has to happen before classification is safe to run at
all* — running classification or a scope checklist on an unconfirmed symptom is how a vague or
wrong issue gets drafted. Neither difference reaches past its own entry point: origin never
determines a feature's shape, its checklist, its decomposition, its issue count, or its review bar.
A validated Discovered finding can turn out to be any of the four feature shapes (§4), decomposes by
the identical dependency method as planned work (§8), and passes through the identical five review
surfaces before creation (§9).

## 3. Authority and evidence

Three kinds of authority coexist, and the skill's job is to keep them from silently overriding one
another:

- **Approved product and architecture decisions** — a locked decision from an approved `plan.md`
  section, or an explicit decision the user made in the current planning conversation. These are
  authoritative for what they cover and change only through another explicit user decision; nothing
  downstream (a stale design mockup, code that has since drifted, a "cleaner" alternative someone
  notices while drafting) overrides one silently.
- **Verified current implementation evidence** — the codebase, configuration, schema, tests, and
  runtime behavior are authoritative for current-state facts and for whether a `plan.md` claim
  derived from an earlier state still holds. A derived architectural constraint from `plan.md` is
  binding only as long as the fact it was derived from remains true; if current evidence shows that
  fact has moved, the discrepancy is flagged to the user before drafting the affected issues, not
  silently preserved or silently reinterpreted.
- **Design artifacts** — evidence of intended UI, not an automatic authority merely for existing.
  A design artifact never overrides an approved locked decision, and shipped code is not by itself
  proof that a design deviation was a deliberate, confirmed product decision (§6).

**The `plan.md` boundary.** `lab-it` owns investigation, target-architecture
design, and locking decisions with the user — that authority is settled before this skill starts.
`plan-it` verifies relevant current evidence against what an approved plan claims; it
does not reopen approved architecture on its own judgment, and it never reopens a locked decision
itself — a locked decision is preserved exactly regardless of what current evidence shows. What
current evidence *can* do is invalidate the premise a *derived* constraint was built on; when that
happens, or when evidence materially contradicts a locked decision outright, the decision is
preserved as written and the discrepancy is surfaced to the user rather than silently resolved
either way. An unresolved material
product or architecture question — whether raised by a stale `plan.md` premise, a genuine design
disagreement, or an ambiguous Discovered finding — routes to the user through whichever rule
surfaced it; issue wording is never used to manufacture an approval, a certainty, or a resolved
decision that doesn't actually exist. See [`rules/plan-md-input.md`](../skills/plan-it/rules/plan-md-input.md)
for the full consumption contract, including how it distinguishes a locked decision (preserved
exactly), a derived constraint (binding only while its premise holds), and an open implementation
detail (resolvable here only when the choice materially affects scope, dependencies, acceptance
criteria, or developer readiness — otherwise left for implementation).

## 4. Classification and scope architecture

Before any scope question gets asked, the feature is classified into one of four shapes, because
applying single-resource assumptions to cross-cutting work over-scopes it, and skipping
shared-infrastructure thinking under-scopes a capability:

- **A — New resource / first-class domain entity.** A brand-new entity with its own persisted
  identity and lifecycle, where operations and authorization center on that entity.
- **B — Cross-cutting application capability.** Behavior or infrastructure whose organizing
  responsibility spans multiple existing domains rather than one new entity's lifecycle — it may
  still own its own state or tables and remain B, because the state supports cross-cutting behavior
  rather than a resource users manage through its own CRUD lifecycle.
- **C — Extension of an existing capability.** New behavior added to something that already ships.
  Only the affected slice is routed through the relevant tracks or questions of A's or B's checklist
  — the whole existing parent is never replanned for one changed slice.
- **D — Architectural/refactor milestone.** No new user-facing capability; the outcome is
  structural or corrective. Routed loosely through B's outcome/boundaries/preserved-behavior/
  exclusions/dependencies questions, since D has no product shape of its own to interrogate further.

Classification routes to exactly one scope-discovery contract, never a fixed artifact inventory or
an implementation template:

- Shape A, or the resource-shaped slice of C, loads
  [`rules/resource-feature-checklist.md`](../skills/plan-it/rules/resource-feature-checklist.md) —
  seven tracks (core contract, lifecycle/state, child resources, filtering/sorting, export/output,
  user-facing surfaces, integration/tooling completeness) that every resource-shaped feature answers
  in some form, on any stack. Every track must be explicitly resolved for a full shape A — marked
  not-applicable outright rather than silently skipped; a resource-shaped C walks only the tracks
  its changed slice actually affects.
- Shape B, capability-shaped C, or D loads
  [`rules/capability-checklist.md`](../skills/plan-it/rules/capability-checklist.md) — thirteen
  questions (the problem, shared-foundation split, affected domains, runtime paths, security/tenancy
  boundaries, integration points, reusable system- and user-facing patterns, user-visible surfacing,
  collateral changes, exclusions, a conditionally-asked extension-seam question, and proof
  obligations) resolved explicitly for full B, and only for the changed slice for capability-shaped C
  or loosely for D.

Both checklists are scope-*discovery* contracts: they ask which of the consuming project's concrete
artifacts (storage engine, authorization mechanism, interface layer, UI components, tooling) satisfy
each answer — they never answer that on the project's behalf, and they never prescribe an issue
count or a fixed decomposition. That belongs entirely to decomposition and sequencing (§8), decided
independently of which checklist question surfaced the scope. When the resolved scope has any
frontend/UI surface, resource-feature-checklist Track F requires running design reconciliation (§6)
— not discretionary once that condition is met.

## 5. The Discovered-work model

A raw finding — a report, an observed symptom, a log entry, a code-review concern — is not yet
developer-ready scope: its affected behavior, blast radius, and cause may all still be unconfirmed,
and a first symptom alone never justifies a vague issue.
[`rules/discovered-work.md`](../skills/plan-it/rules/discovered-work.md) governs the transition
from a raw finding to exactly one of: validated planning input, no actionable gap, or a
blocked/unresolved finding.

**Evidence intake** works through, proportionally to how quickly a finding actually clarifies: what
was reported and under what conditions; separating confirmed fact from inference and assumption;
reproduction or corroboration where practical; whether the first symptom is the actual problem or
one manifestation of it; enough blast radius to bound the outcome honestly; whether the behavior is
defective, intended, drift from an approved target, or still ambiguous; applicable approved
decisions; and any material decision still requiring the user.

**Safe reproduction** is attempted only when practical, authorized, and non-destructive — existing
evidence, a safe environment, existing tests, and reversible diagnostics are all preferred over
anything that mutates state, and production or live data is never mutated merely to confirm a
report. A reproduction or access limitation is stated honestly; lacking reproduction doesn't
invalidate a finding by itself, but it constrains what the eventual issue can honestly claim.

**Investigation-depth bands** scale to what the planning question actually needs, not to a fixed
depth: *shallow* (an obvious, deterministic symptom and cause — verify completeness and blast radius,
then stop), *focused* (multiple plausible causes, or a symptom crossing feature boundaries —
reproduce, isolate variables, falsify wrong hypotheses one at a time), and *deep* (destructive,
security-, or data-integrity-relevant behavior; cross-layer interaction; contradictory evidence; a
symptom that may hide a materially different defect underneath — trace across whatever boundaries
are necessary and prove the claims that matter). Depth only increases when remaining uncertainty
materially affects scope, safety, guarantees, or developer readiness.

**Evidence checkpoints** are a visibility and decision mechanism, not a time or token budget: surface
one when a major hypothesis is falsified, investigation must cross into a new system or ownership
boundary, remaining evidence would require unavailable access or invasive instrumentation, or a
natural point is reached where coherent scope may already be possible. Each checkpoint reports what's
confirmed, what's ruled out and how, what remains unknown, the next useful step, and whether the
finding is already scopeable.

**Disposition and readiness** are two separate judgments. Disposition classifies the evidence:
confirmed current defect, intended behavior with no actionable gap, intended behavior with an
adjacent gap, drift from an approved target, an unresolved material decision, or not-yet-classifiable.
Readiness then asks whether drafting can proceed at all: a defect, adjacent gap, or drift proceeds
into the normal pipeline; no actionable gap produces no issue; an unresolved material decision blocks
drafting and routes to the owning decision gate; a not-yet-classifiable finding needs more
investigation or stays blocked — it never automatically becomes an instrumentation issue by default.

**The stopping condition** is the discipline that holds the whole model together: *investigate until
the finding can be scoped honestly, not necessarily until its complete root cause or fix is known.*
Stopping short of a complete explanation is legitimate when further work is disproportionate to its
planning value, necessary access is unavailable, or confirming the mechanism would require invasive
instrumentation or implementation work — but only when the remaining unknown doesn't prevent a
reliable outcome, boundary, or proof obligation. An unresolved mechanism may become one of the
eventual issue's own Tasks (§7) only once this condition is genuinely met, never as a shortcut around
investigating.

## 6. Design reconciliation

Design artifacts drift from what actually ships — real product decisions get made mid-implementation
and never get folded back into the design source. [`rules/design-reconciliation.md`](../skills/plan-it/rules/design-reconciliation.md)'s
job is to surface that drift before it silently repeats, not to resolve it in either direction on
its own.

**Activation.** The pass runs whenever planned work has any frontend/UI scope — during planning,
before canonical issue definitions exist. Backend- or infrastructure-only work skips it entirely.
Discovering that no relevant design artifact exists is a valid, ordinary outcome of running the pass,
not a reason to skip running it.

**Authority sources, in order of what's already settled versus what must be surfaced:** an approved
`plan.md` locked decision governs the intended target for anything it covers, and neither a design
artifact nor current implementation can silently override it. Current code is authoritative for
current-state facts and for discovering shipped conventions elsewhere in the app. A design artifact
is evidence of intended UI — not automatically the newest or winning source merely for existing, and
shipping something is never by itself proof that anyone deliberately decided it should stay that way.

**Classifying a disagreement.** After comparing an approved decision (if any), the available design
artifacts, and the shipped surface, the result falls into one of five outcomes: no material drift
(sources align, or their difference doesn't change behavior or scope — proceed); resolved drift
(sources differ, but an approved decision or established chronology resolves the intended target —
record the drift against the resolved target); genuine unresolved disagreement (sources express
different product choices and no approved authority or chronology resolves which governs); genuinely
new UI (an artifact describes a new surface with no shipped counterpart or conflicting decision —
follow it); or no relevant artifact (continue from approved decisions and established conventions,
never inventing layout or interaction requirements to fill the gap).

A genuine unresolved disagreement blocks only the affected issue definitions, presented to the user
as what each source indicates, why neither clearly supersedes the other, the specific decision
required, and an optional recommendation — never silently resolved by picking a side. A missing
artifact blocks drafting only when its absence leaves a necessary product decision unresolved, not
by itself. Design artifacts inform planning; they never automatically override an approved product or
architecture decision, and an approved decision is the one authority this reconciliation never
re-litigates.

## 7. The canonical issue model

The **canonical issue definition** — not any rendered preview, the compact manifest, or a prior
draft — is the single authoritative representation of a proposed issue before it ever touches
GitHub. Every rendered body, every manifest row, and every final `gh issue create` call is generated
fresh from the current canonical definition; nothing downstream is ever reconstructed from an
earlier render. This is what keeps a large issue set from drifting (duplicated sections, misplaced
acceptance criteria) across several rounds of revision.

**Titles** take one form regardless of layer, shape, or origin: `<Area/Capability>: <action or
outcome>` — describing the change or observable outcome, never an implementation-layer batching
choice, with no bracket prefixes and a surface/location qualifier only where it materially improves
clarity.

**A body must stand alone** — understandable even if `plan.md`, the planning conversation, and this
skill's own prior output all disappeared. It is structured around:

- **Context** — why the issue exists: the problem, the intended outcome, the constraints that
  matter, what's in and out of scope, and relevant dependencies, in prose. Context explains a
  decision; it never merely cites one.
- **Tasks** — the actual delivery work, as literal Markdown checkboxes GitHub can render as
  progress.
- **Acceptance Criteria** (optional) — guarantees and observable outcomes that must remain true,
  distinct from a restated Task, added only where an issue's complexity actually earns them.
- **Tests** (optional) — named behaviors or guarantees needing proof, only when that adds real value
  beyond what Tasks and Acceptance Criteria already imply, and always at the level of what needs
  proving rather than an assertion-by-assertion recipe.

**Reference categories stay strictly separate**, because GitHub linkifies any `#` followed by digits
whether intended or not: a **real GitHub reference** (`#<N>`, an actual issue or PR), a **canonical
planning identifier** (this pass's own pre-GitHub sequence number, e.g. "canonical issue 5"), a
**plan decision identifier** (e.g. "decision 7"), and a **plan section reference** (e.g. "`plan.md`
§2.5"). Only the first is ever written as `#<N>`; the other three use hash-free natural wording.
Before an issue is created, every planning-only number in its body must already be resolved to
either a real `#<N>` dependency or rewritten as plain wording. A dependency is expressed as `Depends
on #<N>` once the prerequisite has a real number; a `plan.md` citation may supplement an
already-complete explanation but never substitutes for one, since neither `plan.md` nor the planning
conversation is load-bearing once the issue exists.

**Completion requirements must be feasible at the issue's own closure boundary.** A per-issue
Acceptance Criterion or Test is invalid if it depends on evidence that structurally cannot exist
until a later milestone/PR boundary under the consuming project's delivery workflow — for example,
requiring a PR-triggered CI run as proof for an issue that closes on a shared branch before any PR
for that milestone exists. Disclosing that gap honestly in the issue body is not a substitute for
not creating it; the fix is routing that proof to the boundary where it can actually be produced
(the milestone/PR boundary itself), not softening the wording or caveating an internally
inconsistent requirement.

**Member-level closed-set coverage** applies whenever approved scope defines an exhaustive set —
through an inventory, named members, an exact count, or "all/every" wording. Two distinct things get
validated: whole-set coverage, checked once across the *entire* canonical issue set, confirms every
in-scope member from that approved source appears exactly once somewhere in the set, and that any
member the approved scope explicitly defers or excludes stays outside it; and the narrower,
per-issue check, run against one issue's own rendered body or the manifest's row for it, confirms
that issue's *specific assigned subset* of the members is exactly what it claims — no missing,
duplicated, or extra member for that one issue. Passing the per-issue check for every issue doesn't
substitute for the whole-set check, and neither check searches for members beyond what the approved
scope already defined — that would be scope expansion, not fidelity validation.

## 8. Decomposition and sequencing

[`rules/sequencing.md`](../skills/plan-it/rules/sequencing.md) owns two connected decisions
after checklist scope exists: splitting it into coherent issues, and ordering those issues by real
prerequisites. It does not decide implementation order, which ready issue gets worked next, branch
strategy, or commit structure — all of that is `ship-it`'s.

**Decomposition** is identical across every classification shape: split by coherent outcome, real
dependency, and independent provability — never by checklist question or track, file, class, route,
component, layer, system-side-versus-user-facing split, or a fixed count. A checklist's questions
supply scope; no question number maps mechanically to an issue. Split when parts produce
independently meaningful outcomes, have materially different prerequisite chains, or can be verified
apart from each other; bundle when pieces have no provable outcome apart from each other, when a
foundation can't be trusted without a real consumer exercising it, or when splitting would leave
unused scaffolding. Issue count is never predetermined by input size, checklist length, or file
count — it falls out of what's actually independently provable.

**A real dependency** exists only when one issue's outcome must exist before another can be safely
completed, landed, or verified — never a preferred order, shared subject matter, milestone
membership, or drafting convenience. **Scope membership and dependency-edge creation are separate
decisions**: a validated Discovered finding, or any other piece of scope, belongs to a canonical
issue set based on its actual scope alone, never merely because of when or where it surfaced —
surfacing during another issue's implementation doesn't by itself create a dependency on that issue.
An external prerequisite the issue set doesn't own may be recorded as an external constraint, never
fabricated as an internal issue; an unresolved material product/architecture decision is never
treated as an external constraint — it routes through its owning decision gate instead.

**The dependency graph** treats each canonical issue as a node and each real prerequisite as a
directed edge. It must be acyclic, with every internal dependency resolving to another canonical
issue and unambiguous direction. A cycle means a boundary or a dependency claim is wrong — resolved
by combining inseparable work or correcting the false edge, never by an arbitrary tie-breaking order.

**Waves** present the graph's partial order for creation and review: roots have no internal
prerequisites, and a later wave's issues have all their prerequisites in an earlier wave. A wave
exposes possible parallelism — it says nothing about live implementation readiness or which issue to
work next, both of which belong to `ship-it` once issues exist.

## 9. Review, approval, and mutation

Five review surfaces each validate a different artifact, and none substitutes for another:

| Surface | Validates | Runs |
|---|---|---|
| Semantic issue/dependency review | Whether an issue and its dependencies are *right* — coherent outcome, complete Context, preserved decisions, no hidden material gap, proportional Acceptance Criteria/Tests, closure-boundary-feasible completion requirements, real dependency edges | After drafting, and after every revision |
| Canonical structural integrity | The canonical definitions themselves — unique identifiers/titles, exactly one body per issue, no misplaced content, acyclic and dependency-safe order, whole-set member coverage when scope is an exhaustive set | After drafting, and after every revision |
| Issue-body content integrity | One freshly rendered body — reference-category discipline, no planning leakage, self-contained Context, literal Task checkboxes, per-issue member-subset accuracy | Before content review, and again immediately before any create/edit mutation |
| Rendered-manifest integrity | The compact manifest as a one-way render — row count, identifiers, titles, order, and metadata all matching canonical state | Immediately before the final approval presentation |
| Post-mutation live-state validation | Live GitHub state after a mutation episode, independently re-fetched and compared against the exact approved target | After every related mutation episode, at creation and on any later change |

**Two approval moments gate GitHub**, and nothing — no milestone, label, or issue — is created until
both pass: a **content review** of the full issue set, where scope, Context, Tasks, and Acceptance
Criteria get fixed, and a **final approval** of the compact manifest plus the proposed metadata
(milestone, labels, assignee, including the approved absence of any of them). Metadata itself is
proposed early — queried against current GitHub state, informed by discovered project conventions,
drafted explicitly — but created only at that same final gate; nothing is created speculatively while
issue content is still being drafted.

Reaching the content-review gate is proof-gated, not narration-gated: every review surface applicable
to the current canonical set must actually have run against the exact literal bodies being presented,
captured in a compact review-execution record (kept internal by default, surfaced on request) that
names each surface as applied or genuinely not applicable — a general claim that review was applied
does not satisfy this. A correction invalidates the affected issue's prior record entry; its complete
body is re-rendered fresh and every applicable surface reruns before it is re-presented.

**Validating before mutation is a different act from validating after it.** A `gh` command
succeeding proves only that GitHub accepted the request, not that the intended state now exists.
Immediately before any issue body touches GitHub, it is re-rendered from the current approved
canonical definition and re-checked; after the mutation, live state is independently re-fetched and
compared against the exact approved target — by mutation type (issue creation, a body edit, a
metadata change, milestone or label creation), and identically for a later mutation as for the
original one. A failed validation is reported as GitHub currently being inconsistent with the
approved target — never silently hidden or normalized.

## 10. Rule ownership and handoffs

Every rule under `rules/` answers a distinct question in the pipeline; none restates another's
territory:

| Rule | Owns |
|---|---|
| [`plan-md-input.md`](../skills/plan-it/rules/plan-md-input.md) | Recognizing and consuming an approved `plan.md` section as canonical input; preserving its locked/derived/open distinctions |
| [`discovered-work.md`](../skills/plan-it/rules/discovered-work.md) | Turning a raw finding into validated planning input, no actionable gap, or a blocked finding |
| [`feature-classification.md`](../skills/plan-it/rules/feature-classification.md) | Which of the four shapes a feature is, and which checklist it routes to |
| [`resource-feature-checklist.md`](../skills/plan-it/rules/resource-feature-checklist.md) | Shape-A/resource-shaped-C scope discovery across its seven tracks |
| [`capability-checklist.md`](../skills/plan-it/rules/capability-checklist.md) | Shape-B/capability-shaped-C/D scope discovery across its thirteen questions |
| [`design-reconciliation.md`](../skills/plan-it/rules/design-reconciliation.md) | Comparing design-artifact, shipped, and approved-decision authority when UI is in scope |
| [`issue-conventions.md`](../skills/plan-it/rules/issue-conventions.md) | Title/body format, reference-category discipline, and the metadata proposal-and-approval workflow |
| [`sequencing.md`](../skills/plan-it/rules/sequencing.md) | Decomposition into coherent issues and building the dependency graph/waves |
| [`review.md`](../skills/plan-it/rules/review.md) | All five review surfaces and their validation timing |

`SKILL.md` owns the two approval gates and the overall pipeline order; no rule file reproduces that
gate structure itself.

**Handoff from `lab-it`.** The only thing that ever crosses into this skill from
architecture work is an approved `plan.md` section — a published or updated architecture guide never
implies a downstream handoff by itself. `plan-md-input.md` treats that section as canonical only once
initiative match, the source-of-truth statement, and the user's independently established approval
are all present; a polished draft or the file's mere existence is never enough on its own.

**Handoff to `ship-it`.** This skill's responsibility ends once approved GitHub metadata and
issues are created and validated. From there, `ship-it` owns branch readiness, review gates,
commits, verification, issue closure, and release/milestone progression — including live dependency
readiness as issues actually close, and which ready issue to implement next, neither of which this
skill decides. A wave (§8) is a dependency-safe presentation and creation order, not a live
readiness signal.

**Handoff to consuming stack/project guidance.** Every checklist, this dossier's canonical-issue
model, and the review surfaces stop at *what* must be true and *what* must be proven — never *how* to
implement it. The concrete artifacts that satisfy a checklist question (storage engine, authorization
mechanism, interface components, tooling commands), the project's metadata conventions (milestone
naming, label palette, assignment rules), and any framework-specific implementation detail all come
from the consuming project's own stack-specific skills and established conventions, discovered per
project, never assumed or carried inside this skill's portable rules.

## 11. Boundaries and confidence

GitHub specificity is intentional, not a portability gap to close — this skill's portability claim is
being reusable across GitHub-based projects with different stacks, not across issue trackers.
Application-stack implementation knowledge, milestone-naming patterns, and label palettes are inputs
the consuming project supplies into the methodology; they are not, and should never become, part of
the portable rules themselves. Project metadata conventions must be discovered or supplied per
repository — this skill invents none of them and presents no invented value as an established
convention.

This skill cannot guarantee downstream implementation quality: it owns planning and issue creation,
not the code that later satisfies an issue, and a well-formed, self-contained, review-passed issue
is not a claim about how well it will be implemented.

Its architecture — the classification/checklist model, the canonical-issue and reference-category
discipline, the dependency-graph decomposition, the five review surfaces, and the pre/post-mutation
validation model — has been exercised through real issue planning and real GitHub mutation, not
merely authored and left untested. That confidence does not extend to broad portability across many
consuming projects: validation beyond one real consuming project remains unproven, and this document
does not claim otherwise.

Member-level closed-set coverage (§7, §9) is part of the current review contract as written into the
rule set, but its fresh forward validation remains outstanding — it has not yet received an
independent exercise on a new initiative since its introduction, so this document does not claim to
have watched it catch a real coverage gap on a new feature, only that the contract exists.

Where two rules touch the same concern (a derived constraint's staleness check between
`plan-md-input.md` and `design-reconciliation.md`, or issue-quality review between
`issue-conventions.md` and `review.md`), each explicitly names the other as the owner rather than
restating its logic.
