# my-feature-planning — Skill Dossier

Status: Current
Scope: `my-feature-planning` as it stands at `agentic-engineering@main`
Purpose: Supporting analysis of the current skill — architecture, reasoning, boundaries, evidence,
authoring lessons, and open questions — after the completed rule-by-rule authoring pass and the
cross-rule cohesion pass that followed it.

## 1. Purpose and status

This is supporting analysis, not the operational skill. `SKILL.md`, `README.md`, and `rules/*.md`
remain the authoritative source of what the skill does; if anything here disagrees with them, this
document is stale, not the other way around. It describes the skill as it currently stands. History —
the rule-by-rule authoring pass, the cross-rule cohesion pass, and the portability evidence in
`56cddee47e9d84d6b244b41ec4536d24e8d7cff3:phase-discovery.md` — appears only where it explains why a
current contract is shaped the way it is, never as a chronological account of how the skill got here.
This is not another operational rule file, not a `SKILL.md` replacement, not a change log, not a copy
of that historical record, and not an invitation to revise the completed skill again.

## 2. What the skill is

`my-feature-planning` converts a feature ask, an approved `plan.md` section, or a validated
Discovered-work finding into reviewed, approved, developer-ready GitHub issues.

GitHub is intentionally part of the methodology, not an abstraction layer standing in for some other
tracker. Issues, milestones, labels, assignees, `#N` references, and mutation validation are
GitHub-native concepts this skill is built around. Portability, for this skill, means reuse across
GitHub-based projects with different stacks and conventions — never across issue trackers. This is
stated outright, not disguised as tracker neutrality.

Three starting points feed two work origins into one shared pipeline:

```
feature conversation ──┐
                        ├──► Planned work ────┐
approved plan.md ───────┘                     │
                                               ├──► classify → scope → [design reconcile]
Discovered finding ──► validate ──► Discovered work ──┘     → propose metadata → draft → sequence
                                                              → review → approve → create → validate
```

A feature conversation and an approved `plan.md` are both **Planned work** — both start from an
intentional proposed change, not an unexpected finding, regardless of whether every scope detail is
already resolved. A conversation-driven feature ask enters the pipeline at classification and still
requires scope discovery; an approved plan enters by consuming `rules/plan-md-input.md` first, with
its architecture and decisions already canonical. **Discovered work** starts from an unexpected
finding with scope not yet known, and only a validated finding enters the pipeline. Both origins
converge on the identical canonical-issue pipeline and the identical review bar — Discovered work
never gets a lighter-weight issue.

## 3. Pipeline position and ownership

```
my-architecture-laboratory  →  my-feature-planning          →  my-git-workflow
(approved architecture,        (classification, scope,          (Git/GitHub delivery:
 optional plan.md)              drafting, dependencies,          branch readiness, review
                                 review, metadata proposal,       gates, commits, verification,
                                 approval gates, GitHub           closure, release, milestone
                                 creation, post-mutation          completion)
                                 validation)                          +
                                                                consuming-project implementation
                                                                skills (application/framework code)
```

- `my-architecture-laboratory` may supply approved architecture and an approved `plan.md`; this skill
  never re-derives architecture or re-litigates a decision the plan already locked
  (`rules/plan-md-input.md`).
- `my-feature-planning` owns everything from classification through validated GitHub issue creation.
  Its responsibility ends once approved issues are created and validated.
- `my-git-workflow` owns downstream Git/GitHub delivery. It does **not** own application
  implementation — it composes with the consuming project's own implementation skills, neither
  replacing the other.
- Consuming-project implementation skills own the actual application/framework code, picked up once
  an issue is approved.

**The Discovered-work convergence point.** `rules/discovered-work.md` owns a special path — raw-finding
investigation through semantic disposition and drafting readiness — that exists nowhere else in the
skill. Once a finding is validated, it becomes ordinary planning input: classified
(`rules/feature-classification.md`), scoped, drafted, sequenced, and reviewed exactly like Planned
work. Origin never determines classification, decomposition, or review rigor past that convergence
point.

## 4. Rule architecture

| Rule | Owns | Deliberately does not own | Consumed by |
|---|---|---|---|
| `plan-md-input.md` | Recognizing an approved `plan.md` section (initiative match, source-of-truth statement, known approval); preserving the locked/derived/open distinction; checking a derived constraint's premise for staleness against current code. | Producing or amending `plan.md`; re-running Plan Synthesis's own review. | Entry point before classification; authority precedent for `design-reconciliation.md` and `discovered-work.md`. |
| `feature-classification.md` | Choosing among four feature shapes by organizing responsibility. | Answering the shape-specific scope questions. | Routes to `resource-feature-checklist.md` or `capability-checklist.md`. |
| `resource-feature-checklist.md` | The seven-track (A–G) scope-discovery question set for resource-shaped work. | Concrete stack/implementation answers; issue decomposition. | Feeds `design-reconciliation.md` (Track F) and canonical scope for `sequencing.md`. |
| `capability-checklist.md` | The thirteen-question scope set for cross-cutting/architectural work. | Concrete implementation reuse decisions. | Feeds canonical scope for `sequencing.md`. |
| `design-reconciliation.md` | Comparing design artifacts, shipped app, and approved decisions; classifying drift; the separate drafting-readiness gate. | Amending `plan.md` or design files; implementing UI. | Its outcome becomes scope/constraint input to issue drafting. |
| `discovered-work.md` | Raw-finding intake: reproduction, evidence discipline, depth bands, checkpoints, disposition, readiness, stopping condition. | Fixing code; a second, lighter issue-authoring path. | Hands a validated finding to `feature-classification.md`. |
| `issue-conventions.md` | Title/body shape; the four GitHub-reference categories; the metadata proposal-and-approval workflow; verification-checkpoint proportionality and closure-boundary-feasible completion criteria inside a drafted issue (§10, §11). | Decomposition; milestone lifecycle/closure; how `my-git-workflow` actually executes verification. | `review.md` validates its output against `SKILL.md`'s approval gates. |
| `sequencing.md` | Coherent-outcome decomposition; building and validating the real dependency graph; presenting it as dependency-safe waves. | Implementation order; which issue is worked next; branch strategy; commit structure. | `review.md`'s dependency-quality check; `SKILL.md`'s creation step. |
| `review.md` | Five validation surfaces around `SKILL.md`'s two approval gates: semantic, canonical structural (including member-level closed-set coverage — an approved exhaustive set's whole membership reconciled against the canonical issues it's distributed across), rendered-body (the exact subset of that set assigned to one issue, preserved in its rendered body), rendered-manifest (any set/count claim the manifest states, reconciled against actual canonical membership where applicable), post-mutation live-state. | Issue syntax/metadata policy; decomposition; raw-finding investigation; design/product decisions. | `SKILL.md`'s pipeline steps 7–8 directly. |

These are separate conceptual contracts, not arbitrary file boundaries, because each answers a distinct
question no other file answers: *which shape* (classification) is a different question from *which
questions that shape needs answered* (the checklists); *is the scope right* (semantic review) is a
different question from *does the rendered text match the canonical definition* (structural/rendered
integrity); *does a UI choice need reconciling* (design-reconciliation) is a different question from
*is drafting still blocked* (its own separate readiness gate, not folded into the same question).

## 5. Authority and evidence model

Several kinds of authority coexist, and the skill keeps them from collapsing into one undifferentiated
"most recent wins" rule:

- **Approved locked `plan.md` decisions** are the ceiling. They govern the intended target for
  anything they cover and are never re-litigated by planning; only the user can amend one, explicitly.
- **Derived architectural constraints** bind only while the current-state fact they were derived from
  still holds — `rules/plan-md-input.md` checks this staleness against current code before drafting,
  distinct from re-litigating the locked decision underneath.
- **Open implementation details** may stay open for implementation, under an executability test: would
  flipping the choice change what the system guarantees? If yes, it is product-shaped and must be
  resolved (or asked); if every option preserves the same guarantees, the issue can remain executable
  without picking one.
- **Current code** is authoritative for current-state facts and for discovering already-shipped
  conventions elsewhere in the app.
- **Design artifacts** are evidence of intended UI — not automatically the winning or newest source
  merely because they exist.
- **Project-supplied conventions** (milestone naming, label taxonomy, sequencing constraints) shape a
  proposal; they are inputs to the methodology, never the methodology itself.
- **Observed GitHub history and live state** must be queried fresh at each use — never frozen into
  static methodology, since live label palettes, milestone sets, and repository history change.
- **The user** decides where authority or chronology genuinely can't resolve a disagreement.

Distinctions the skill preserves explicitly, and that a maintainer should not accidentally flatten:

- Shipping something does not by itself prove a deliberate, confirmed newer product decision — code
  can ship without anyone having decided it should stay that way.
- A design artifact is not automatically the winning or newest source just because it exists.
- A milestone description, even an approved one, cannot override an approved locked `plan.md`
  decision — a conflict is surfaced, not silently resolved by the description.
- Repetition in repository history is evidence that may shape a metadata proposal; it is never
  automatically project policy.
- Live GitHub metadata state (labels, milestones) must be queried at proposal time, never stored as a
  static snapshot inside the methodology.
- An approved *absence* of a metadata field (no milestone, no label, no assignee) is a real, valid
  approved result — not a gap to fill by default.

**Why authority overlays must not be modeled as peer reconciliation outcomes.**
`design-reconciliation.md`'s five outcomes classify the *relationship between peer evidence sources*
(a design artifact, the shipped app, established precedent). An approved locked decision is not one
more peer in that comparison — it sits above it as a governing overlay. A mismatch against a locked
decision is always recorded as drift against the approved target; it never enters the peer-comparison
outcome set as if it could lose to a design file or shipped behavior. Collapsing the two would let a
stale mockup or an accidental shipped regression silently outrank a decision the user already made.

**Why source classification and drafting readiness are separate decisions.** Classifying *what the
sources say relative to each other* (five outcomes) is a different question from *can drafting proceed
right now*. "No relevant artifact" classifies cleanly and still doesn't block by itself; only an
actually-unresolved material product decision blocks, and only the issue definitions it affects.
Folding readiness into the classification step would make every "no artifact" or "genuinely new UI"
outcome look like a potential blocker when most are not.

## 6. Classification and scope discovery

`rules/feature-classification.md` sorts a feature into one of four shapes by **organizing
responsibility**, not by implementation footprint:

- **A — new resource**, its own persisted identity and lifecycle → `resource-feature-checklist.md`.
- **B — cross-cutting capability**, organizing responsibility spans multiple existing domains →
  `capability-checklist.md`. Owning its own tables does not disqualify it from B — the state supports
  cross-cutting behavior rather than a resource's own CRUD lifecycle.
- **C — extension** of something that already ships → the relevant slice of whichever checklist
  applies, never a full replan of the parent.
- **D — architectural/refactor** milestone, no new user-facing capability → `capability-checklist.md`'s
  applicable questions only.

Checklist questions **discover** scope; they never dictate issue count — that mapping belongs entirely
to `rules/sequencing.md`'s coherent-outcome test. Capability-shaped and architectural work resolve only
the applicable checklist questions; loose work can use a checklist as a set of prompts without forcing
a full feature replan.

**The shared-foundation test** (`capability-checklist.md` question 2, consumed by `sequencing.md`):
foundation work that's independently coherent and provable on its own may become its own issue;
foundation work that can't actually be proven correct without a real consumer exercising it bundles
with the smallest real consumer instead. Unused scaffolding is never created merely to satisfy an
abstract layering preference.

## 7. Design reconciliation

This rule runs whenever planned work carries any frontend/UI scope — not discretionary once that
condition is met, during planning, before canonical issue definitions exist. A missing design artifact
is a valid, ordinary result of running it, not itself a blocker.

**Locating artifacts.** No directory, filename, format, tool, or tracked/untracked status is assumed;
the consuming project's actual sources are discovered from project-supplied documentation,
configuration, or reliable conversation context. The rule asks the user only when the location is
materially necessary and unclear — it never invents an artifact or a project convention for one.

**Five source-relationship outcomes**, applied after comparing an approved decision, the relevant
design artifact(s), and the shipped surface: no material drift; resolved drift (chronology or approved
authority resolves the intended target); genuine unresolved disagreement; genuinely new UI (a new
artifact, no conflicting decision); no relevant artifact.

**Drafting readiness is a separate decision.** Only a genuine unresolved disagreement, or a missing
artifact that leaves a necessary product decision unresolved, blocks — and it blocks only the affected
issue definitions, never the whole planning pass. Issue definitions unaffected by the open decision
continue normally.

This rule is the clearest illustration of two general lessons stated in §5: authority is an overlay
applied around the classification, not folded into it, and classifying evidence is not itself the same
act as deciding whether the workflow can proceed.

## 8. Discovered work

`rules/discovered-work.md`'s job is turning a raw finding into validated planning input before it ever
reaches classification — without reproducing the operational procedure here, the epistemic model is:

- A raw report — a symptom, a log entry, a review concern — is a finding, not yet a confirmed defect.
  Its existence never by itself confirms the underlying behavior.
- Reproduction is conditional, safe, and non-destructive: preferred when practical, never mutating
  live or production state merely to confirm a report.
- Investigation depth is proportional — shallow, focused, or deep bands, deepening only when remaining
  uncertainty materially affects scope, safety, guarantees, or developer readiness.
- Evidence checkpoints give the user a decision-ready view at natural inflection points; they are
  neither an automatic stop nor an automatic command to keep going.
- **Semantic disposition is classified first** (confirmed defect, intended/no gap, intended/adjacent
  gap, drift from an approved target, unresolved material decision, not-yet-classifiable) — **then
  drafting readiness is assessed separately.** A defect, gap, or drift proceeds; an unresolved material
  decision blocks drafting even though it has a clear disposition; a not-yet-classifiable finding
  requires more investigation and never automatically becomes an instrumentation issue by default.
- Root cause is useful but not always required — uncertainty is acceptable only when bounded and the
  issue remains honest, executable, and non-speculative.
- An unresolved mechanism may become one of the issue's own scoped Tasks, but only under the stopping
  condition: investigate until the finding can be scoped honestly, not necessarily until its complete
  root cause is known.
- Insufficient evidence must never silently become an instrumentation issue by default — that
  conversion requires the stopping condition to actually be met, not merely an absence of a clear
  answer.
- New evidence that materially contradicts a confirmed fact or approved decision *after* approval is
  never ignored — it routes through the applicable review, discovered-work, or human decision gate.

**Scope membership vs. dependency-edge creation stay separate** when Discovered work joins existing
planned scope. Surfacing during another issue's implementation doesn't by itself make a finding
dependent on the issue that exposed it; membership follows the same coherent-outcome test as any other
scope decision, and a dependency edge is added only where a real prerequisite actually exists.

## 9. Canonical issue and metadata model

**Canonical-definition contract.** There is one canonical definition per proposed issue. Every
rendered preview, the compact manifest, and every mutation are generated fresh from the current
canonical definition — never reconstructed from an earlier rendered preview. This is what prevents a
large issue set from drifting (duplicated sections, misplaced acceptance criteria) across revision
rounds.

**Issue-body shape**, and why the parts stay distinct: `## Context` (prose — the problem, outcome,
constraints, scope, exclusions, dependencies) explains a decision rather than citing one;
`## Tasks` are literal, mutable Markdown checkboxes tracking delivery progress; optional
`## Acceptance Criteria` are static guarantees, deliberately never checkboxes, so they can't be
mistaken for completable work items; optional `## Tests` names behavior-level proof obligations only
where it adds value beyond what Tasks/Acceptance Criteria already imply.

**Four GitHub-reference categories** (`rules/issue-conventions.md` §3): real GitHub issue/PR references,
canonical planning identifiers, plan decision identifiers, plan section references. Only the first is
ever written `#N` — GitHub linkifies any `#`+digits regardless of intent, so a bare planning-only
number left as `#N` would silently link to whatever issue happens to hold that number in the repo.

**Why plan sections and planning conversations can't be load-bearing.** A created issue must stand
alone even if `plan.md`, the planning conversation, and this skill's own prior output all disappeared —
a `plan.md` pointer is allowed only *in addition to* an already-complete explanation, never as a
substitute for one.

**Metadata model** (`rules/issue-conventions.md` §5) keeps five things distinct at every step: explicit
project convention; observed GitHub state; planning's proposed metadata; final approved metadata *or*
approved absence; post-approval creation. Milestone (title, optional description, lifecycle owned
downstream by `my-git-workflow/rules/milestone-completion.md`), labels (name/color/taxonomy), and
assignee (validity checked before mutation, never a silent default) are kept type-correct and
conceptually separate — none is conflated with another as "the metadata."

## 10. Decomposition, dependencies, and planning waves

`rules/sequencing.md` decomposes canonical scope by **coherent outcome, real dependency, and
independent provability** — never by checklist question, file, layer, or a fixed template such as
backend-before-frontend.

**A real dependency** exists only when one issue's outcome must exist before another can be safely
completed, landed, or verified — never a preferred order, shared subject matter, milestone membership,
or an implementation-layer habit. Every internal edge is validated into a DAG: roots and disconnected
components are valid outcomes, not exceptions to explain away, and a cycle means the boundaries or a
dependency claim are wrong — it is corrected by fixing the claim, never broken with an arbitrary
ordering decision.

**Planning waves** present the graph as a dependency-safe order — issues whose prerequisites all sit in
an earlier wave — exposing possible parallelism and giving a stable order for presentation and
creation. A wave makes **no claim about live implementation readiness or which issue to work next**;
no implementation-layer order is built into the portable methodology itself. That choice belongs
entirely to `my-git-workflow` once issues exist.

Project-supplied delivery constraints are treated as project input: identified as project-supplied,
checked for whether they create a real prerequisite or only a preferred order, and encoded as a
dependency edge only in the former case.

**Planned and Discovered work converge on the same decomposition method** once a finding is validated —
origin never determines issue count or order.

Three layers stay distinct throughout, never conflated: **membership** in canonical scope (does this
belong to the initiative at all), **dependency edges** inside that scope (which issues actually
require which others), and **downstream live readiness** after issues exist (which ready issue to
work next, recomputed by `my-git-workflow` after each closure). A canonical graph may legitimately
contain parallel roots or disconnected components — belonging to an initiative never requires an edge
to every other issue in it.

## 11. Review, approval, and mutation validation

`SKILL.md` owns two approval gates: **content review** of the full issue set, and **final approval** of
the compact manifest plus the proposed metadata. Nothing is created until both are given.

`rules/review.md` owns five distinct validation surfaces around those gates, each checking a different
artifact against a different standard:

1. **Semantic issue/dependency quality** — is the scope and the graph *right*.
2. **Canonical structural integrity** — do the canonical definitions themselves satisfy count,
   uniqueness, and acyclic-graph invariants. This validates the canonical definitions directly, never a
   rendered preview.
3. **Rendered issue-body integrity** — does a freshly rendered body match its canonical source, with no
   planning leakage or unresolved placeholder.
4. **Rendered-manifest integrity** — does the compact manifest match canonical count, order, and
   values, one-way, freshly generated.
5. **Post-mutation live-state validation** — does GitHub's actual live state, independently re-fetched,
   match the exact approved target.

Canonical structure and live GitHub state are **not** "rendered artifacts" — they are validated against
their own criteria (internal structural correctness, and actual mutation outcome respectively), not
checked for fidelity to something else the way a rendered preview or manifest is.

**Member-level closed-set coverage.** When approved scope establishes an exhaustive set — through an
inventory, named members, an exact count, or "all"/"every" wording — three of the five surfaces carry a
matching check rather than accepting a matching headline total on its own: canonical structural
integrity (surface 2) confirms every in-scope member from that source appears exactly once across the
canonical issues, checked against the actual members, with any member the approved scope explicitly
defers or excludes kept outside the canonical set; rendered issue-body integrity (surface 3) confirms
each rendered body preserves the exact subset of that set assigned to its own canonical issue — not the
whole exhaustive set, since scope may legitimately be distributed across multiple issues; rendered-
manifest integrity (surface 4) confirms any set/count the manifest states reconciles with the canonical
issues' actual membership. This validates fidelity to scope the approved source already established — it
does not authorize searching for members beyond that source, or silently expanding approved scope.

**Why a successful mutation is not proof.** A `gh` command's exit code proves only that GitHub accepted
the request, not that the intended state now exists. Every mutation episode is independently re-fetched
and compared against the exact approved target — including an approved absence of a field — with no
exemption for the first creation versus a later edit.

## 12. Empirical evidence

The methodology isn't theoretical; some of its current shape is directly traceable to earlier defects
found and fixed during the authoring passes. This section keeps only the evidence that still teaches
something surviving in a current rule — not a chronological record of what changed.

- **Why raw findings need epistemic discipline.** `discovered-work.md`'s disposition/readiness split
  and its "not-yet-classifiable never automatically becomes an instrumentation issue" rule exist
  because a shallow finding, taken at face value, is exactly how a vague or wrong issue gets drafted —
  the rule's own stated purpose.
- **Why design authority can't be inferred from an artifact's existence or a shipped implementation.**
  An earlier draft of `design-reconciliation.md` had overlapping outcome/blocking logic that could let
  "the artifact exists" or "it shipped" stand in for an actual authority decision; the current rule
  separates source classification from drafting readiness precisely to prevent that (§7, §5).
- **Why fixed implementation-layer batching was replaced by an actual dependency graph.** An earlier
  version of this skill's top-level guidance described sequencing as "backend/TDD work batched before
  frontend/UI work" as the default shape. The current model — coherent-outcome decomposition plus a
  validated dependency DAG, presented as waves — replaced that fixed template because a template can't
  represent a feature whose real dependency structure doesn't match it; a project's actual graph now
  decides split, bundle, and order every time.
- **Why static project metadata and live palette state don't belong in a portable skill.** An earlier
  version of the metadata rule restated a project's live label-palette state as if it were a fixed fact
  of the methodology. The current `rules/issue-conventions.md` §7 states explicitly that it never
  stores a project's live label state as part of its own methodology — that state is queried fresh
  every time, from GitHub and from project-supplied convention, never frozen into the rule.
- **Why milestone lifecycle mechanics must be owned downstream, not duplicated in planning.**
  `rules/issue-conventions.md` §6 stops at classifying and scoping a milestone and explicitly hands PR
  readiness and closure to `my-git-workflow/rules/milestone-completion.md`'s current contract, "always
  consult that rule's current contract directly rather than restating it here" — avoiding a duplicated,
  driftable copy of downstream lifecycle logic inside planning.
- **Why canonical definitions and independent post-mutation validation matter.** `rules/review.md`
  states, in its own text, that its checks re-derive their expected set from whatever the canonical
  definitions currently are, "for any feature and any issue count," rather than hard-coding an expected
  shape — the discipline that makes the five validation surfaces in §11 actually portable instead of
  tied to one feature's specifics.
- **Resolved historical defect — a stack-specific checklist file.** `resource-feature-checklist.md` was
  once the single heaviest concentration of interleaved generic and project-specific content in this
  skill's rule set, braided sentence-by-sentence rather than separable by section. It has since been
  rewritten so every track states only the portable question, with concrete artifacts explicitly
  delegated to "the consuming stack." Direct inspection of the current file confirms no project-specific
  content remains.
- **Resolved historical defect — private-memory dependencies.** Two rules once depended directly on
  named personal-memory entries for a design-file location and a GitHub-issue convention. Direct
  inspection of the current `design-reconciliation.md` and `issue-conventions.md` confirms neither
  references any memory entry; both now discover the equivalent information from project-supplied
  context instead.
- **Resolved historical defect — stack vocabulary in the always-loaded activation file.** `SKILL.md`
  once named specific framework artifact types directly in its top-level Workflow section — the one
  file every invocation loads regardless of which downstream rule applies, unlike the labeled
  illustrations the rule files used elsewhere. The current `SKILL.md` carries no such vocabulary.

**A real consumer exercise — the approved-`plan.md` path (`useOrbit`, 2026-08-28).** `roadmap.md`
Phase B records that `useOrbit` consumed this skill from
`agentic-engineering@5ff489ca60c26ad971da926118701953fa75e41c` and used it, from the natural
instruction to feature-plan an already-approved `plan.md` initiative, to run classification, canonical
issue drafting, metadata approval, GitHub creation, dependency-reference resolution, and post-mutation
validation end to end, producing `useOrbit#300`, `#301`, and `#302` in the milestone `Phase 23 —
Composer & JavaScript Dependency Upgrade`. Those three issues were then carried through the full
downstream `my-git-workflow` delivery lifecycle to a merged PR (`#303`) and a published release
(`v0.17.1`) — see `skill-audits/my-git-workflow.md` §11 for that downstream evidence, not restated
here. The relevant findings for *this* skill are what that later execution revealed about the issue
contracts this skill produced, not about the downstream delivery itself:

- **The three-issue decomposition itself held up.** Nothing in the downstream execution required
  re-splitting, re-merging, or re-sequencing #300, #301, or #302 — the coherent-outcome boundaries
  (CI/baseline, Composer upgrades, npm upgrades) that review corrected the original eight-way
  over-split down to (recorded in `roadmap.md`, Phase B) survived real implementation unchanged.
- **#302's uniform per-group verification wording caused disproportionate repeated verification
  downstream.** Its Tasks named the same full-project regression gate after each of four npm-only
  implementation groups, regardless of which stack a given group actually touched — driving four full
  backend-regression re-runs that no npm-only change in that issue could plausibly have required. This
  is precisely the gap `rules/issue-conventions.md`'s new §10 ("Verification checkpoints inside a
  multi-group issue") now addresses: state what each checkpoint needs to prove and scale it to the
  affected surface, rather than repeating one full-project command after every group by default.
- **#300's own completion criterion could not be satisfied at its own closure boundary.** Its Tests
  section required a real, PR-triggered CI run as a condition of that issue's own completion, but the
  downstream milestone-branch delivery model closes every issue before any PR for that milestone
  exists — making the criterion structurally unsatisfiable at #300's own closure, regardless of
  sequencing choice. This is precisely the gap `rules/issue-conventions.md`'s new §11 ("Completion
  criteria must be satisfiable at their own closure boundary") now addresses: check a completion
  requirement against the issue's own expected closure boundary before finalizing it, and route
  boundary-dependent proof to the milestone/PR boundary it actually belongs to instead.
- **These are issue-contract quality findings, not evidence that this skill's core mechanics failed.**
  Classification, GitHub issue/milestone creation, dependency resolution, and metadata proposal/
  approval/post-mutation validation all worked as designed in this exercise — the two findings above
  are about what the drafted issue *text* asked for, not about whether planning correctly classified,
  sequenced, created, or validated the issues it produced.

**A second real consumer exercise — the approved-`plan.md` path, architectural/refactor classification
(`useOrbit`, 2026-09-01).** The immutable approved `plan.md` at `useOrbit@0f905cf313301a372a00f24cce684e442590a75f`
defines `useOrbit`'s `tests/` restructuring: an exhaustive 74-file set of Unit-to-Feature dispositions
(§1, §4), an exhaustive 7-file set of HTTP tests to trim of duplication with their paired Action test
(§4a, §8), and an exhaustive 7-file set of HTTP tests needing an added persisted-state assertion (F12,
§4a, §8). A natural instruction activated `my-feature-planning` from this approved plan; it classified
the work as an architectural/refactor initiative (`rules/feature-classification.md` shape D — a test
suite reorganization with no new user-facing capability) and proposed four coherent issues in two
dependency waves, rather than one oversized issue spanning all three exhaustive sets:

- `#305`, `#306`, and `#307` are independent roots — the relocation, the HTTP-trim, and the
  persisted-state-addition outcomes are each independently coherent and provable without depending on
  one another.
- `#308` (dropping `'Unit'` from `tests/Pest.php`'s `->in()` chain) has the single real dependency on
  `#305`, since a file still sitting in `Unit` mid-migration would otherwise lose `TestCase`/
  `RefreshDatabase` if the config change landed first.

Existing Testing metadata and project conventions were reused rather than invented: all four issues were
created under the milestone `Phase 24 — Tests Restructuring`, labeled `Testing`, and assigned to
`elieandraos` — the project's own existing label and assignment conventions, not new methodology-side
policy. Post-mutation validation confirmed live state matches this target: `useOrbit#305`, `#306`,
`#307`, and `#308` all carry milestone `Phase 24 — Tests Restructuring`, label `Testing`, and assignee
`elieandraos`, and are open. Direct inspection of the live bodies confirms complete membership: live
`#305`'s Tasks cover all 74 Unit-to-Feature dispositions, including the one `Listeners/` file
(`UpdateLastLoginTimestampTest.php`); live `#306`'s Tasks cover all 7 HTTP-trim files, including
`Carriers/StoreTest.php`; live `#307`'s Tasks cover all 7 persisted-state-addition files; live `#308`
both references and declares a real dependency on `#305` (`"Depends on #305"`, a real GitHub issue
number, not a canonical planning identifier).

This exercise revealed two findings, and preserving the distinction between them is the point of
recording this evidence:

1. **Portable rule gap.** Exhaustive member-level task coverage was not explicit enough in
   `rules/review.md` before this exercise: a draft or render pass could omit individual members from a
   canonical issue's Tasks while still reporting a headline total that matched the approved count,
   because nothing checked actual membership against the approved source. This justified the narrow
   `rules/review.md` correction landed in `9dc5b6d` ("Add exhaustive task coverage validation"),
   clarified in `4a9557c` ("Clarify closed-set validation wording") — see §4, §11, above.
2. **Execution misses already covered by existing rules.** In the course of this same exercise, a
   rendered manifest temporarily omitted a canonical issue, and some validation reports claimed checks
   had passed despite visible mismatches on inspection. Both are failures the existing canonical-
   structural-integrity and rendered-manifest-integrity rules (§5, §7 of `rules/review.md`, already in
   force before this exercise) already prohibited outright — an execution miss against a standing rule,
   not evidence of a gap in the rule itself. They did not justify any duplicate guidance beyond the one
   correction above.

**This exercise's live issues predate the correction — they are not evidence the corrected rule
produced them.** `useOrbit#305`–`#308` were created on 2026-09-01 at 08:29–08:30 UTC; `9dc5b6d` and
`4a9557c` were committed the same day at 08:34 and 08:42 UTC respectively — after issue creation, not
before it. What this exercise shows is that the final live issue bodies are complete against the
approved plan's exhaustive sets (confirmed above by direct inspection), that the rule correction the
exercise motivated was subsequently authored and published upstream, and that `useOrbit` then refreshed
its installed `my-feature-planning` snapshot and provenance record from
`24b288caf62f4d83b74d741a1cb96583cb1877fe` to `4a9557c372bc68d4fba89b37eb4e8f4ce7ad902d`, verified as
exact 11-file parity (sorted file list, per-file SHA-256 manifest, and `diff -rq` all matching the
canonical directory at `4a9557c3...` exactly; `UPSTREAM_PROVENANCE.md`, "Refresh: `my-feature-planning`
— 2026-09-01 (second refresh, same day)").

**No independent forward test has occurred yet.** No genuinely new, fresh-initiative exercise of the
corrected rule has been run since — the only post-correction activity against these four issues was a
read-only recheck confirming already-correct live bodies, which does not itself constitute a forward
test of the corrected rule drafting a new issue set from scratch.

## 13. Authoring observations

Reusable lessons from this authoring pass are consolidated in
`skill-audits/skill-authoring-methodology.md`. This dossier keeps only their skill-specific
manifestations, in the architecture and empirical-evidence sections above; §12 contains the evidence
relevant to `my-feature-planning`.

## 14. Boundaries and open questions

Genuine current boundaries — deliberate scope limits, not defects:

- **GitHub is intentionally required.** This is a stated design choice (§2), not an oversight to
  generalize away.
- **Application-stack implementation knowledge stays outside this skill.** Checklist questions
  discover scope; the consuming project's own stack-specific skills answer with concrete artifacts.
- **Project conventions remain project inputs.** Milestone naming, label taxonomy, and assignment
  rules are discovered per project, never assumed or hard-coded.
- **Design artifacts may be absent.** A missing artifact is a normal, non-blocking outcome unless its
  absence leaves a necessary product decision unresolved.
- **Human decisions remain necessary where product authority is genuinely unresolved** — a genuine
  design disagreement, an unresolved material Discovered-work decision, or an open implementation
  detail that turns out to affect a guarantee all route to the user rather than being silently decided.
- **Issue drafting cannot make an unresolved material decision executable by wording alone.** A
  well-written issue body doesn't substitute for the decision it depends on.
- **This skill cannot guarantee project-specific implementation quality after handoff.** Its
  responsibility ends at approved, validated issue creation; everything after belongs to
  `my-git-workflow` and the consuming project's own implementation skills.

**Open questions.** Direct inspection of the current nine rule files, `SKILL.md`, and `README.md` —
after both the rule-by-rule authoring pass and the cross-rule cohesion pass — found no genuinely
unresolved internal design question within this skill's own architecture. Every cross-file
contract checked for this dossier (classification → checklist routing, checklist → sequencing,
design-reconciliation's authority model, discovered-work's convergence into the ordinary pipeline, the
metadata proposal-and-approval flow, the five review surfaces, the planning/delivery handoff) is
internally consistent and consistently cross-referenced on the current read. It is valid, and accurate
here, to conclude that no important internal design question remains open. The one class of question
that does remain genuinely open sits outside this skill's own boundary: whether and how
project-specific stack knowledge should be extracted into a separate layer is `roadmap.md` Phase C/D's
classification question for the surrounding repository, not a design gap inside `my-feature-planning`
itself.

## 15. Current assessment

**Demonstrably portable.** The four-shape classification taxonomy, both checklists' governing
questions (Tracks A–G and the thirteen capability questions), the issue-format rules and the four
GitHub-reference categories, the canonical-definition contract, the coherent-outcome
decomposition/dependency method, the five review/validation surfaces, and the discovered-work epistemic
model are all stated generically across all nine current rule files, `SKILL.md`, and `README.md`. No
concrete stack-specific content survives in any of them on direct inspection — including
`resource-feature-checklist.md`, previously the heaviest concentration of interleaved generic and
project-specific content in this skill's rule set.

**Intentionally GitHub-specific.** Milestones, labels, `#N` auto-linkification, and the mutation/
re-fetch validation model are GitHub product concepts this methodology is built around, stated
explicitly rather than hidden behind tracker-neutral language.

**Inputs a consuming project must supply.** Application-stack conventions for answering checklist
questions; design-artifact location and access method; milestone naming and label taxonomy; assignment
rules; live GitHub state at proposal and validation time; and, where relevant, an approved `plan.md`
from `my-architecture-laboratory`.

**Material leakage check.** None found. The specific couplings identified for this skill in
`56cddee47e9d84d6b244b41ec4536d24e8d7cff3:phase-discovery.md` — the heavily mixed checklist file, two
private-memory dependencies, and stack vocabulary inside `SKILL.md`'s always-loaded activation surface
— were checked directly against the current files for this dossier and are absent from all of them.

**Whether further authoring changes are presently justified.** The rule-by-rule authoring pass and the
cross-rule cohesion pass resolved every concrete coupling identified for this skill in
`56cddee47e9d84d6b244b41ec4536d24e8d7cff3:phase-discovery.md`; no further authoring was indicated by
that evidence. Two real downstream executions have since
produced three narrow, evidence-backed corrections beyond that baseline, each scoped to what its own
execution actually showed, not a reopening of the broader authoring pass:

- `rules/issue-conventions.md` §10 — proportional verification checkpoints — and §11 — completion
  criteria satisfiable at their own closure boundary — from the first exercise (`useOrbit#300`–`#302`,
  §12 above): disproportionate per-group verification wording, and a completion criterion unsatisfiable
  at its own closure boundary.
- `rules/review.md`'s member-level closed-set coverage validation (§4, §11 above) from the second
  exercise (`useOrbit#305`–`#308`, §12 above): exhaustive member-level task coverage was not explicit
  enough to catch a draft or render pass omitting individual members while still reporting a matching
  headline total.

Both exercises' evidence comes from the same real consumer, `useOrbit` — this is not yet corroborated by
a second consuming project. No independent fresh-initiative forward test of the third correction has
occurred yet (§12 above). No further authoring change is indicated beyond those three.
