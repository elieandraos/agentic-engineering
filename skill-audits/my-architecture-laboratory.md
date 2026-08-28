# my-architecture-laboratory — Skill Dossier

Status: Current
Scope: `my-architecture-laboratory` as it stands at `agentic-engineering@main`
Purpose: Supporting analysis of the current skill — architecture, evidence and decision model,
ownership, evidence-backed authoring history, and open questions — after the completed authoring
pass and the cross-file cohesion pass that followed it.

## 1. Purpose and status

This is supporting analysis, not the operational skill. `SKILL.md`, `README.md`, and `rules/*` remain
the authoritative source of what the skill does; where anything here disagrees with them, this
document is stale, not the other way around. It describes the skill as it currently stands. The
twenty-commit authoring history between the shared externalization baseline (`fe5bd29`) and the
current endpoint, and the independent portability findings in `phase-discovery.md`, appear only where
they explain why a current contract is shaped the way it is — never as a chronological account of how
the skill got here. This is not an operational rule file, not a `SKILL.md` replacement, not a change
log, and not an invitation to re-open the completed authoring pass.

## 2. What the skill is

`my-architecture-laboratory` investigates a real system and turns the resulting understanding into
exactly one of three results:

| User intention | Result |
|---|---|
| Understand and document existing architecture | A new Claude Artifact architecture guide |
| Reconcile a guide with verified changed reality | An updated existing Artifact |
| Design feature architecture through conversation | An approved `plan.md` handed to `my-feature-planning` |

Investigation and a recap of it are also a valid, complete result on their own — a guide and a
`plan.md` are outputs someone has to ask for, never something an investigation produces
automatically just because it happened. All three workflows share one evidence discipline before
anything is written (§4), and each has its own, different rule for when human confirmation is
required (§4). The skill is deliberately not a fourth thing: it does not classify a feature, decompose
it into issues, mutate GitHub, or write application code — that is `my-feature-planning`'s and the
consuming project's job, picked up only after this skill's boundary (§3).

## 3. Pipeline position and cross-skill boundaries

```
my-architecture-laboratory  →  my-feature-planning  →  my-git-workflow
(investigate, explain,         (classification, scope,   (Git/GitHub delivery)
 guide, maintain, or             drafting, review,
 synthesize plan.md)             GitHub creation)
```

- This skill owns architecture investigation and explanation, surfacing and resolving material
  decisions with the user, new architecture guides, maintenance of existing guides, and synthesis of
  approved architecture into `plan.md`.
- It does not own application implementation, debugging or diff review, API reference documentation,
  feature classification, issue decomposition, GitHub issue mutation, delivery sequencing, or Git
  workflow.
- The guide workflow (new or updated) never automatically hands anything downstream — publishing or
  updating an Artifact is a complete, standalone result.
- Only an approved `plan.md` crosses the boundary into `my-feature-planning`, which then owns
  classification, scope, design reconciliation, canonical issue definitions, review, and GitHub
  creation, and never re-derives architecture or re-litigates a decision the plan already locked
  (`my-feature-planning/rules/plan-md-input.md`, consumed on the other side of this exact boundary).
- Two dependencies are deliberate, not leftover project-specificity, and are named openly rather than
  disguised as tracker- or tool-neutral: the guide workflow publishes to a Claude Artifact using the
  `artifact-design` skill; the planning workflow writes `plan.md` and hands it to
  `my-feature-planning`. Neither makes this skill GitHub-specific — GitHub is `my-feature-planning`'s
  substrate, not this skill's.

## 4. Evidence and human-decision authority

Every workflow starts from the same evidence discipline before any output is written: inspect the
real current system and relevant evidence — not conventions or assumptions; reconcile implementation,
configuration, schema, tests, runtime evidence, and reliable history; explain the current architecture
and identify uncertainty. Authority is not collapsed into "the code is truth for everything":
implementation is authoritative for implementation facts, while configuration, schema, runtime
observations, and external-system state are each authoritative for whatever they actually govern.
Tests are strong evidence — often surfacing a real boundary faster than implementation alone — but not
infallible authority, and get reconciled rather than trusted blindly. Reliable history (issues, commits)
explains rationale; it never by itself establishes current behavior, and something history says was
planned but the evidence doesn't show is never documented as if it were real. The skill's own
pull-quote states the overall posture directly: *the system establishes what exists; the user decides
what it should become.*

What differs, deliberately, per workflow is **when** that second half — the user's decision — is
required:

- **A new guide** needs the user to confirm the investigation's recap before publication. A correction
  at that point is real signal about what the guide needs to get right, not a formality to clear.
- **Planning feature architecture** needs explicit, user-approved decisions for every material
  product/architecture question before `plan.md` is written — Plan Synthesis never manufactures a
  decision on the user's behalf (§11).
- **Updating an existing guide** asks the user only when authority, intent, or a material decision is
  unclear; routine, verified current-state documentation does not require a new product decision.

Plan Synthesis sharpens "material" into an explicit, consequence-based test rather than a fixed list of
choice types (§11): a choice is material, and must be resolved with the user, exactly when changing it
would alter approved behavior, a guarantee, a security boundary, ownership, lifecycle, an operator/user
promise, or the target architecture — never because of what kind of choice it superficially looks like
(a column type, a class, a CLI flag, a UI treatment can each be material or not, depending on
consequence, not category).

## 5. Rule and supporting-file architecture

Everything under `rules/` is loaded only when its workflow needs it — none is a universal
prerequisite. `template.html` is deliberately not called a rule: it is a starting HTML/CSS/JS
scaffold to edit, not a normative statement the way the other four files are.

| File | Owns | Deliberately does not own | Consumed by |
|---|---|---|---|
| `doc-style.md` | The writing grammar for guides: fixed section rhythm (head/prompt/intro), the eight-item content-block vocabulary, tone/evidence discipline, favicon stability. | Critically evaluating a finished guide; changing an existing one; the HTML/CSS scaffold itself. | "Document existing architecture" step 3; `template.html`'s own comments route back to it. |
| `template.html` (supporting file, not a rule) | The Artifact HTML/CSS/JS scaffold: the CSS custom-property theme, the responsive two-column shell, the content-block CSS classes, and the syntax highlighter with its documented fallback contract. | Deciding a guide's section structure or which content blocks to use — that is `doc-style.md`'s job. | The starting point for "Document existing architecture" step 3. |
| `review.md` | The finished-guide review checklist and its philosophy (architecture communicated, not prose polish); the "known gap stated is not a finding" rule. | Drafting a guide; maintaining one; re-investigating facts from scratch. | Both guide workflows, once a draft or update exists. |
| `maintenance.md` | The "Update an existing architecture guide" methodology: the architectural-claim maintenance unit, the reconcile-before-editing classification, the claim-graph rule, continuity-without-freezing, the redeployment/review sequence. | Investigating from scratch (routes to `SKILL.md`'s shared discipline, §4); judging whether a finished guide communicates its architecture (that is `review.md`'s job). | "Update an existing architecture guide." |
| `plan-synthesis.md` | The Plan Synthesis contract: the two mandatory preconditions, the four claim categories, the locked-vs-open materiality test, the flexible content model, evidence-referencing rules, `plan.md` placement rules, the internal review pass, the approval/handoff contract. | Feature classification, issue decomposition, GitHub mutation, implementation planning, or new product/architecture decision-making. | "Plan feature architecture"'s final step; `my-feature-planning/rules/plan-md-input.md` consumes its handoff on the other side of the skill boundary. |

These are five separate contracts because each answers a question the others don't: *how do I write*
is a different question from *how do I judge what's already written* (`doc-style.md` vs. `review.md`),
*how do I change an existing guide without breaking it* is different again from either
(`maintenance.md`), and *how do I hand off a decision instead of teaching a system* is a different
output entirely (`plan-synthesis.md`).

## 6. Architecture center of gravity and the conditional-content model

Investigation is required to surface the **architectural center of gravity** — the one idea everything
else in the system hangs off (a polymorphic contract, a queue pipeline, a runtime subsystem boundary, a
sync-vs-async split) — as a hypothesis during exploration, confirmed during the recap, and used to
decide the guide's actual structure during writing. No guide uses one fixed section inventory; structure
follows the system being explained, not a template.

`doc-style.md` fixes the section *rhythm* (a numbered head, an italic guiding question, a one-paragraph
direct answer) but leaves section count, names, and which of the eight content blocks appear entirely
conditional on what the architecture actually has. Recurring concerns — purpose, security, runtime
ownership, decisions, limitations, a closing summary — appear only when they materially improve
understanding of *this* system, never because a previous guide included them. `review.md` enforces the
same discipline from the reading side: a "when applicable" checklist category that doesn't apply to a
given architecture is inapplicable, not failed, and a missing content block is a finding only when a
real recurring distinction is being described in prose a reader can't actually follow without it.

This conditionality had to be re-verified at every layer that represents a rule, not just stated once
at an entrypoint — §12 records a concrete case where a content-block *definition* silently
reintroduced mandatory phrasing even after the file's own opening text said content blocks are chosen
per section.

## 7. Document existing architecture

Route: investigate the real system → recap and obtain confirmation → decide structure from the
confirmed center of gravity → load the guide-writing and Artifact-design instructions → use the
template → publish the Claude Artifact → run the guide review.

1. **Investigate.** Inspect every architectural surface the system actually has — persistence and data
   relationships, business rules and lifecycle, request/interaction boundaries, authorization and
   security, background/async work, external integrations, user-facing surfaces and reusable UI logic,
   schema and operational constraints — as investigation categories, not a fixed checklist.
2. **Recap and confirm.** Write the recap as chat output, never a file or an artifact, with concrete
   implementation references threaded throughout. Stop and wait for the user to confirm before the
   investigation becomes a published guide — a correction here is real signal, not friction to route
   around.
3. **Write and publish the guide.** Only after the recap is approved: decide structure from the
   confirmed center of gravity (`rules/doc-style.md`); load the `artifact-design` skill (required
   before writing any Artifact page); write the HTML from `rules/template.html`, replacing content and
   keeping the design system unless the architecture genuinely needs a new block type; publish with
   the `Artifact` tool (title, one-sentence description, a stable favicon); run `rules/review.md`
   against the published guide before considering it complete.

Publishing to a Claude Artifact is specific to this workflow and to updating an existing guide;
investigating and recapping don't depend on it, and neither does `plan.md`.

## 8. Claude Artifact identity, rendering, and accessibility contract

**Identity.** A guide's title follows `"{Capability} Architecture"`; its favicon is one or two
domain-appropriate emoji, supplied at first publish and re-supplied unchanged on every redeploy — a
changed favicon reads as a different document, so maintaining a guide discovers or confirms its current
favicon first rather than silently picking a new one. A maintenance update redeploys through the same
`url`; a new guide is never minted to stand in for updating an existing one.

**Rendering.** The scaffold is self-contained by explicit operational constraint: no
`DOCTYPE`/`html`/`head`/`body` wrapper (the Artifact tool supplies them at publish time) and no external
requests or CDN dependencies — every rule and every script is inline. Theming uses CSS custom
properties with three coexisting paths: a light default on bare `:root`, a `prefers-color-scheme: dark`
media override, and an explicit `data-theme="dark"`/`"light"` attribute override that wins in both
directions over the media query. The page layout is a responsive two-column shell (a sticky section
nav plus a main content column) that collapses to one column under an 880px breakpoint. The syntax
highlighter enhances exactly five disclosed `data-lang` values (PHP, TS, Vue, JSON, HTTP) with token
coloring and a tinted label; every other case — an unsupported-but-present `data-lang`, or none at all —
still reaches an HTML-escaped, unhighlighted plain-code fallback rather than being skipped or left
unescaped, with the label itself present only when a `data-lang` attribute exists at all (§12 records a
production-path defect in this exact fallback that was found and fixed during authoring).

**Accessibility.** The template carries specific, verifiable signals rather than a certified contract:
`:focus-visible` outlines on interactive elements, one `aria-label="Sections"` on the nav landmark, a
`prefers-reduced-motion: reduce` override that disables smooth scrolling, and a semantic heading
hierarchy (`h1` hero, `h2` per section, `h3`/`h4` for subdivisions). No formal accessibility audit (for
example, measured WCAG contrast ratios) has been run against this template, and none is claimed here.

**Verification boundary — read honestly.** Everything in this section was confirmed by direct
inspection of `template.html`'s source and its own stated operational constraints during this
authoring pass, not by an actual Claude Artifact publish-and-render cycle. No guide was published
through this template as part of this authoring pass, and the skill has not yet been exercised by a
fresh real consumer (`useOrbit` or otherwise) since this pass completed. A prior discovery pass
(`phase-discovery.md`) did inspect a live precedent Artifact, but that was a different, now-removed
citation (§12, §14) — its outcome is historical evidence about that superseded precedent, not a
verification of the current template. Nothing here should be read as proof that the current scaffold
behaves as described once actually rendered inside a live Claude Artifact.

## 9. Update an existing architecture guide

This is its own workflow, not an automatic stage after creating a new guide, triggered by a stale
architectural claim, a stale evidence reference, changed configuration or runtime behavior, or a prior
documentation defect — not only a changed implementation. `rules/maintenance.md` governs every
judgment call.

The maintenance unit is the **architectural claim** — a center of gravity, a responsibility or
ownership, a boundary, an invariant, a lifecycle or state, an extension seam, a decision and its
trade-off, a limitation, or a concrete evidence reference — not the section or paragraph that happens
to carry it, and not narrowed to only a "guarantee." Reconciling a guide against verified current
evidence classifies what's found into one of four outcomes: no documentation event (a claim and its
evidence are both still accurate — leave it alone); a narrow update (one fact or reference is wrong,
no architectural shift behind it — correct in place); a connected architectural change (several claims
depend on each other and must move together — follow the complete claim graph, not only the section
where the change was first noticed); or unresolved authority/intent/a material decision — stop, and
return it to the user through `SKILL.md`'s shared discipline rather than deciding it during
maintenance.

Continuity means preserving every unaffected claim and presentation choice, never rewriting nearby
prose merely because the file is open — but continuity is not the same as freezing the guide's center
of gravity, structure, ownership, or reasoning in place: if verified architecture actually changed one
of those, the guide changes with it, in proportion to what actually changed. The guide's identity is
preserved (same `url`, same favicon) across every redeploy. After editing, `rules/review.md` runs
against the *whole* updated guide, not only the sections touched, with emphasis on the changed claims
and whatever depends on them.

## 10. Guide review model

`rules/review.md` is a check on whether a finished guide actually communicates the architecture, never
a proofreading pass — a guide can read roughly and still pass; a guide can read beautifully and still
fail. It runs only against a finished artifact (the published Claude Artifact, or the exact draft being
proposed), never during drafting. Every finding must materially affect what a reader understands about
how the system is shaped, owned, constrained, or reasoned about; if a suggested change wouldn't change
that, it's a preference, not a finding, and gets dropped. A guide is allowed known gaps — the review's
job is to confirm a materially relevant gap is stated somewhere, not silently absent; a stated,
accurately-described gap is not itself a finding.

The checklist's eight categories — architectural center; responsibility and ownership; reuse,
integration, and variation (when the architecture has any); runtime, lifecycle, and state (when it has
any); architecture versus implementation; structure and content; consistency; decisions and
limitations (when the guide states any) — are each conditional on the architecture actually having that
concern, and the checklist is explicit that an inapplicable category is skipped, not failed. Output is
a short list of findings, one sentence each, ordered by consequence, never a rewrite; the review
reports and the guide's author decides what to act on. What it deliberately never flags: word choice or
rhythm that doesn't change what's understood, a different but equally valid section order, a missing
content block absent a real distinction that needs one, an inapplicable conditional category, or a
stated known gap that isn't misleading.

## 11. Plan feature architecture and Plan Synthesis

This workflow exists to prepare a real implementation initiative, not to teach a system, and can begin
from a feature idea, an architecture question, an existing investigation, or already-approved findings.
It may need to investigate how the current system supports or constrains a proposed feature, discuss
viable target approaches, distinguish current facts from proposed choices, obtain explicit decisions
for material questions, and leave an implementation detail open when every viable option preserves the
approved guarantees.

**Plan Synthesis** is the workflow's *final writing step*, not the whole workflow, and is performed
only when the user asks for it — never as an automatic next step after investigation, and never
implied by a plain "document/explain X" request. Two preconditions are both mandatory: a real
current-state investigation (concrete evidence — paths, symbols, schema, configuration, tests, runtime
behavior — not conventions or assumptions), and explicit user decisions about the target state,
established in the active conversation or another reliable, identifiable prior context. If either is
missing, synthesis stops and returns to that investigation or decision conversation rather than
papering over the gap.

Every material claim in the resulting plan falls into exactly one of four categories, kept visually
and textually distinct: **current-state fact** (verified present reality, confirmed against the
codebase or other authoritative evidence); **locked decision** (a target-state choice the user
explicitly approved, changeable only through another explicit decision); **derived architectural
constraint** (a necessary consequence of current-state facts plus one or more locked decisions, with
its premises stated so a later stale premise can be detected); **open implementation detail** (an
unresolved choice whose every viable outcome preserves the approved architecture and guarantees). A
material product or architecture decision can never remain classified as an open implementation
detail — the test is whether changing the choice would alter approved behavior, a guarantee, a
security boundary, ownership, lifecycle, an operator/user promise, or the target architecture, never
what kind of choice it superficially is (§4).

The plan's structure follows the initiative, not a fixed template — no exact headings, order, or
one-section-per-concern is required, but the plan must communicate the initiative and problem, the
verified current state, the approved target architecture, the locked decisions, any derived
constraints, what must remain true, the conceptual change boundary, material open details if any, and
the evidence grounding current-state claims; security/failure/recovery, lifecycle/before-after, test
impact, external dependencies, and migration constraints are included only when relevant. It must
never become a file-by-file edit sequence, an implementation checklist, an issue decomposition, or a
delivery plan. Evidence is architecture-neutral (paths, symbols, schema, configuration keys, protocols,
runtime boundaries, tests, authoritative external-system state) rather than tied to one language's or
framework's file shape.

`plan.md` defaults to the repository root unless the project supplies a different convention; before
writing, its existing content (same initiative, a different one, durable project context, stale
material, or an empty placeholder) is inspected rather than assumed, and unrelated content is never
overwritten just because the file exists.

**The handoff statement is not approval.** Near the top of the written section, Plan Synthesis states
that it is the source of truth for the subsequent `my-feature-planning` pass — but that statement only
marks the document's *intended* handoff role; it is not evidence the user has approved the draft. A
Plan-Synthesis-specific internal review (ten checks: every locked decision preserved unsoftened; no
material decision disguised as open; the four categories still distinguishable; each derived
constraint's premises actually hold; no superseded proposal presented as current; evidence resolves at
synthesis time against its authoritative source; no preserved-behavior claim conflicts with a described
change; invariants compatible with the target architecture; the plan is sufficient for
`my-feature-planning` without re-deriving from conversation; and the plan itself performs no
classification, decomposition, sequencing, or GitHub work) runs before the plan is ever presented. Only
after the user's *explicit* approval — of the document itself, distinct from having approved the
decisions inside it before synthesis — does the plan become canonical.

**The other side of the boundary.** `my-feature-planning/rules/plan-md-input.md` recognizes an approved
section only when the initiative matches, the source-of-truth statement is present (necessary but not
sufficient), and explicit approval is independently established — never inferred from a polished draft
or the file's mere existence, and with no persistent approval marker invented to check for instead.
Locked decisions are preserved exactly; derived constraints stay binding only while their premise still
holds, checked against whichever authoritative evidence actually governs the fact (not code alone); an
open detail is resolved during planning only when it materially affects scope, dependencies,
acceptance criteria, or developer readiness, using the identical materiality test named above — never a
narrower one limited to user/operator guarantees.

## 12. Empirical evidence behind the current methodology

The current shape of this skill is directly traceable to concrete defects found and fixed during
authoring, across twenty commits between the shared externalization baseline and the current endpoint.
This section keeps only the evidence that still teaches something surviving in a current rule, not a
chronological record of every edit.

- **Why a mandatory four-phase topology was replaced by three conditional workflows.** The skill once
  treated guide creation and maintenance as one fixed four-stage sequence (Explore → Recap →
  Architecture guide → Maintenance), implying maintenance was a mandatory fourth step of every
  guide-creation run. It is a separate, conditionally-triggered workflow with its own activation
  condition — corrected in `SKILL.md`'s restructuring around what a user can actually ask for (§7, §9),
  with the numbered-phase labels themselves later removed entirely as dead cross-reference weight once
  every reference had its own current name.
- **Why private, unreachable citations don't belong in an activation-time contract.** `SKILL.md` once
  named two specific, account-bound published Claude Artifacts as the guides this whole methodology was
  "reverse-engineered from," plus a "Documents and Tags" visual-style framing tied to them. Neither is
  reachable or verifiable by another agent or a different account, and neither was required to execute
  the methodology, per `doc-style.md`'s own self-contained section-inventory lesson — removed outright,
  not replaced with a new citation.
- **Why fixed section inventories and stack-shaped vocabulary don't belong in a portable writing
  grammar or scaffold.** `doc-style.md` and `template.html` both once carried a fixed
  Purpose→Security→Testing→Decisions→Improvements→Summary section inventory and Laravel/Vue/PHP-shaped
  assumptions (a backend/frontend split, a CRUD-shaped example body, model/action/composable
  vocabulary) — replaced with the conditional content-block model (§6, §10) and a stack-neutral,
  illustrative scaffold.
- **Why conditionality must survive every representation of a rule, not just its entrypoint
  statement.** `doc-style.md`'s Equation-recap and Clincher-sentence content-block *definitions*
  independently used mandatory phrasing ("closes whatever/any section...") even after the file's own
  opening text already said content blocks are chosen per section, not all required every time —
  corrected to state both as optional presentation choices. An entrypoint saying something is optional
  does not make it so if a content-block definition, a table row, or an example elsewhere quietly
  reimposes "always."
- **Why executable supporting material must be exercised through its real discovery path, not just its
  internal helper.** `template.html`'s highlighter selected code blocks to process with
  `document.querySelectorAll('pre[data-lang]')` — a selector that can never match a `<pre>` with no
  `data-lang` attribute at all. `highlight()`'s own fallback branch for a missing language identifier
  was written correctly but was unreachable through the actual production selection path, which skipped
  those elements entirely. Fixed by broadening the selector to `pre`. Reasoning about the internal
  helper in isolation would not have caught this; the defect was only visible by tracing the real
  call path a browser would actually execute.
- **Why "guarantee" was too narrow a maintenance/review unit.** Both `maintenance.md` and `review.md`
  once anchored on a narrower unit (a stated guarantee, or a single content type) for what gets
  reconciled or checked; both were corrected to the broader **architectural claim** (§9, §10), and
  `review.md`'s eight-category checklist was independently corrected across eight separate wording
  defects, each of which silently mandated a structural choice the file's own stated philosophy said
  was conditional (a required diagram, a required "intentional" limitation status, a forced
  reuse/integration split even where none exists).
- **Why an architecture guide isn't assumed to teach a reusable capability.** `plan-synthesis.md` once
  compared itself directly to "Phase 3's architecture guide" and implicitly assumed a guide documents a
  reusable capability. Corrected to state a guide may document any architecture shape — not necessarily
  a reusable one — and to drop every remaining phase-numbered comparison in favor of naming the two
  outputs by what they are.
- **Why a direct consumer outside the skill being authored still needs checking.** The locked-vs-open
  materiality test was corrected inside `plan-synthesis.md` itself, but a separate defect survived one
  layer downstream: `my-feature-planning/rules/plan-md-input.md`'s own restatement of that same test had
  narrowed it to "what the system guarantees to users/operators," silently dropping the
  security-boundary/ownership/lifecycle/target-architecture consequences the corrected owning file now
  names. Found and fixed only by re-reading the consumer file directly, not by re-reading the file that
  had just been changed.
- **Why "canonical" needs two visibly separate gates, not one collapsed one.** `SKILL.md` and
  `README.md` each correctly stated, later in the same document, that a synthesized plan remains a
  draft until the user approves the document itself — but each also still described Plan Synthesis, at
  its very first mention, as writing a "canonical `plan.md`" outright. The two gates (decisions approved
  *before* synthesis; the document approved *after* synthesis) had been collapsed into one at the point
  of first mention, even though the rest of the same file already knew they were distinct.
- **Why a corrected rule's own internal-review checklist needs the same correction applied to it.**
  After the preconditions section was widened to accept approval from "the active conversation or
  another reliable, identifiable context," `plan-synthesis.md`'s own review checklist still asked only
  whether "every locked decision from the conversation" was preserved, and asked only whether evidence
  resolved "against the codebase" — both narrower than the file's own corrected model one section
  earlier. A rule's restatement of itself, inside a checklist meant to verify it, is exactly as capable
  of silently narrowing scope as any other caller.

## 13. Authoring observations

Reusable authoring lessons from this pass are consolidated in
`skill-audits/skill-authoring-methodology.md`, which this pass promoted to a third independent proving
pass alongside `my-git-workflow` and `my-feature-planning`. This dossier retains only the
skill-specific manifestations of those lessons, in §12 above; the methodology document owns the
generalized, cross-skill statement of each one.

## 14. Known boundaries, unproven assumptions, and open questions

Genuine, deliberate scope limits, not defects:

- **Guide publication depends on the Claude Artifact tool and the `artifact-design` skill.** Stated
  openly as a design choice (§3), not tracker-neutral language disguising a real dependency.
- **Plan Synthesis stops at an approved `plan.md`.** Classification, scope, design reconciliation,
  issue drafting, sequencing, review, and GitHub creation are all `my-feature-planning`'s job once the
  boundary is crossed (§3, §11).
- **The skill never writes application code, mutates GitHub, or performs Git workflow.** Every one of
  those is explicitly out of scope regardless of which of the three workflows is active.

Unproven by direct exercise, not by direct inspection — genuinely open until tested:

- **The Artifact identity/rendering/accessibility contract (§8) has been verified only by reading
  source, not by an actual publish-and-render cycle**, and the newly authored canonical skill has not
  yet completed a fresh real-consumer exercise — in `useOrbit` or elsewhere — since this authoring pass
  ended. No temporary fixture or isolated test used anywhere in or around this pass should be read as
  proof of full Artifact publication behavior; none was constructed to stand in for one.
- **No currently-published example guide demonstrates the completed template end-to-end.** The two
  precedent Artifacts this methodology once cited were removed from `SKILL.md` outright (§12) rather
  than replaced with a fresh working citation, so nothing currently published shows the finished
  template rendered for real.
- **The Plan Synthesis → `plan-md-input.md` handoff is internally consistent on direct inspection
  (§11), but has not been exercised end-to-end** with a real approved `plan.md` moving through an
  actual `my-feature-planning` run since the reconciliation pass that corrected it.
- **The five-language syntax-highlighting list (PHP, TS, Vue, JSON, HTTP) is a disclosed, optional
  renderer capability with a safe universal fallback (§8), not a hidden assumption — but it is still a
  literal, named stack list.** Whether that list itself belongs in this portable scaffold at all, or
  should move to a stack layer, is a narrower question this pass didn't need to resolve, since
  disclosure and a safe fallback already remove the misrepresentation a prior discovery pass had
  flagged.
- **Whether the stack-neutral investigation vocabulary fully generalizes to a stack this skill hasn't
  yet been exercised on** remains open until a real consuming project runs a complete workflow against
  the current files.

Outside this skill's own boundary: whether and how project-specific stack knowledge should eventually
be extracted into its own layer is `roadmap.md`'s classification question for the surrounding
repository, not a design gap inside `my-architecture-laboratory` itself.

## 15. Current assessment

**Demonstrably portable, on direct inspection.** The investigation discipline, the per-workflow
confirmation gates, the center-of-gravity/conditional-content model, the four claim categories, and the
locked-vs-open materiality test are stated generically across `SKILL.md`, `README.md`, and all five
`rules/` files. No framework-specific vocabulary, fixed section template, or reusable-capability
assumption survives in any of them after the cross-file reconciliation pass (§12).

**Two dependencies stated openly, not disguised as neutrality.** The Claude Artifact/`artifact-design`
dependency for guides, and the `my-feature-planning` handoff for plans (§3). Neither is hidden and
neither is a GitHub or tracker dependency of this skill's own.

**Architectural coherence.** Strong. Three workflows divide genuinely distinct outputs — a taught
guide, a maintained guide, a decision handoff — under one shared evidence discipline, with five
supporting files each answering a question none of the others do (§5), and no file claiming a boundary
another one owns.

**Authoring quality.** This pass's pattern, repeated across twenty commits (§12), is consistent: remove
private/account-bound or stack-specific evidence, generalize a fixed structure into a conditional one,
then re-verify that the conditionality actually survived into *every* representation of the rule — a
content-block definition, a checklist item, a downstream consumer's own restatement — not only the
owning file's opening statement. Two of the pass's most instructive corrections (§12) were found by
tracing a real execution or consumption path rather than re-reading the file that had just changed.

**Material leakage check.** The couplings a prior discovery pass identified for this skill — two dead
or account-bound precedent citations, and an undisclosed stack-only highlighter assumption — are both
resolved: the citations are gone outright, and the highlighter's five-language list is now explicit,
disclosed, and backed by a universal fallback (§8, §14). The literal five-language list itself remains,
disclosed rather than hidden — see §14 for why that residual question is left open rather than closed
here.

**Whether further authoring is presently justified.** Not for any currently known coupling or
conditionality defect. The substantive gap this assessment cannot close is exercise, not authoring: this
contract has not yet been run against a real consuming project end-to-end (§14). That is validation
work for a future pass, not a known defect in the current one.
