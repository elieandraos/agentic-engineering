# document-it — Architecture Dossier

Status: Current
Scope: `document-it` as it stands in this repository
Purpose: A compact architecture artifact for the skill — its evidence-reuse-first model and its
two-directional relationship with `lab-it`, the three results it produces and where each asks for
human confirmation, purpose-driven Markdown documentation and its identity, the maintenance model,
the review model, rule ownership, and current boundaries and confidence.
[`SKILL.md`](../skills/document-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/document-it/README.md) is the human-facing orientation. This document
explains the architecture behind both rather than restating either.

## 1. Purpose and result model

`document-it` creates, maintains, and reviews purpose-driven technical documentation in Markdown
from already-available, sufficient, and current understanding. It is independently callable: a
documentation request does not require a fresh investigation to begin, and does not require
[`lab-it`](../skills/lab-it/) to have run first.

| Workflow | Terminal output | What gates that output |
|---|---|---|
| Document a technical system or approved design | A new Markdown document | Recap confirmation, unless the user already approved the substance and authorized writing |
| Update an existing document | The same document, reconciled at its existing path | Only when authority, intent, or a material decision is unclear |
| Review a document | A findings report, not a rewrite | Nothing — the report itself is the result |

This skill's result is always a document, or a judgment about one — never a `plan.md`. An approved
`plan.md` stays `lab-it`'s output regardless of which skill performed the underlying investigation;
file extension does not decide ownership.

The skill is runtime-independent: it writes plain Markdown with the consuming agent's ordinary file
tools and depends on no publishing tool, scaffold, or rendering service. Documentation lives in the
repository beside the system it describes, where it is versioned and reviewed with that system.

## 2. Evidence reuse first, and the two-directional relationship with `lab-it`

Before writing or updating anything, this skill establishes whether currently available
understanding is sufficient and current — from the conversation, a recent investigation, evidence
directly verifiable against the real system right now, approved decisions or explicit assumptions.
Approved designs and estimates are distinguished from verified behavior. When understanding is
sufficient, this skill proceeds directly; it does not repeat a full investigation merely because a
documentation workflow is starting.

**When evidence is missing or stale, this skill routes the relevant investigation through
`lab-it`'s own investigation method** (its "Shared investigation and decision discipline") rather
than duplicating that discipline here. `lab-it` investigates and hands back verified findings; it
does not draft documentation itself, even when the investigation originated from a documentation
request. This skill then resumes its workflow with those findings.

**The relationship runs in both directions.** `lab-it` recognizes a documentation request as
outside its own scope and routes it here. This skill draws on `lab-it`'s investigation discipline
only for the narrower missing-evidence sub-problem, and always hands the result back to its own
writing, maintenance, or review workflow. Neither direction performs the other skill's terminal
output: `lab-it` never writes documentation, and this skill never produces a `plan.md` or reaches an
architecture or product decision with the user on its own.

## 3. Purpose-driven Markdown documentation

A document's structure follows its purpose and audience, not a fixed inventory. Architecture
retains a central explanatory idea; operations prioritize safe execution; references and
integrations prioritize understanding and lookup; cost documents disclose assumptions and
trade-offs; product-behavior documents state already-decided rules, states, permissions,
boundaries and exceptions precisely. These are examples, not modes: no purpose has its own
template or mandatory sections, and a document may combine several.

[`rules/doc-style.md`](../skills/document-it/rules/doc-style.md) holds the writing guidance as
judgment, not layout: each Markdown element — summary facts, tables, numbered steps, diagrams, code
blocks, blockquotes, emphasis — is described by what it communicates and when it earns its place.
Diagrams are checked for rendering where the target renderer is known, because Mermaid that a
renderer cannot display fails silently for the reader.

Interface, API, and integration detail is in scope when the reader needs it. The boundary is
duplication, not subject: an exhaustive specification that is authoritative and discoverable
elsewhere is linked rather than copied, and generating API specifications is not this skill's job.

**The new-document recap.** The recap before writing exists because it routinely surfaces
corrections about what the document must get right. Confirmation is required when understanding,
scope, or a material decision is unconfirmed. When the user has already approved the substance and
explicitly authorized writing, that approval is reused rather than requested twice; a material
divergence or a new unresolved decision stops the workflow again.

**Identity.** A document's identity is its file path. A new document defaults to the consuming
repository's `docs/` directory unless the user or project names another location; an existing
document keeps its path, including one outside `docs/`, and unaffected metadata. Relocation
requires explicit authorization.

Connected documentation assigns each subject an authoritative home: overviews stay
self-contained at their level and link to detailed references instead of repeating them.

## 4. Maintenance model

[`rules/maintenance.md`](../skills/document-it/rules/maintenance.md) owns the whole update workflow:
locating the target (missing becomes a new document; unreachable is explained, never reported as
updated), reconciliation, editing, and the final review pass. The maintenance unit is the
**technical claim** — a responsibility, boundary, invariant, lifecycle, procedure step,
configuration value, cost assumption, business rule, decision, limitation, or evidence reference —
not the section that happens to carry it. A pass follows the complete connected claim graph a
change touches, across connected documents when they exist, updating the owning document first.

A reconciliation pass classifies what it finds into one of four outcomes: no documentation event; a
narrow update; a connected technical change; or unresolved authority, intent, or a material
decision (stop and route to the user, or to `lab-it`). This classification is specific to
maintenance triage and is distinct from `lab-it`'s four-category claim model for a `plan.md`.

Maintenance fails in two opposite directions: leaving stale documentation in place for continuity,
and rewriting beyond what the verified change requires. Continuity preserves every unaffected
claim and presentation choice without freezing a center of gravity, ownership, or reasoning that
verified reality has moved. The document describes current reality and explicitly approved design,
never a changelog; durable rationale survives, release history does not.

## 5. Review model

[`rules/review.md`](../skills/document-it/rules/review.md) owns evaluation and findings, and never
edits. It runs in two contexts with one checklist:

- **Standalone review** returns findings only; any fix needs its own authorized maintenance scope.
- **The review pass inside authoring or maintenance** returns findings to the calling workflow,
  which corrects the material defects, verifies the corrections, and stops when a correction needs
  an unresolved decision.

Materiality is judged against the document's purpose and reader: a finding matters when it affects
whether the reader can correctly understand, operate, extend, look up or decide. General questions
— accuracy, status honesty, structure, presentation, consistency, currency, connected documents,
location — apply to every document. Purpose dimensions apply only where the document has that
purpose: architecture (center of gravity, ownership and enforcement, shared versus specific,
runtime versus lifecycle, concept before code, durable "why"), operations, references and
integrations, costs, approved designs, product behavior and business rules, and limitations. An
inapplicable question is skipped, not failed; a known, honestly stated gap is not a finding; an
unstated one is.

## 6. Rule ownership and cross-skill handoffs

Every file under `rules/` answers a question none of the others do, and is loaded only when its
workflow needs it.

| File | Owns |
|---|---|
| [`rules/authoring.md`](../skills/document-it/rules/authoring.md) | New documentation: evidence and purpose, the conditional recap, location, writing, and consuming the review pass |
| [`rules/maintenance.md`](../skills/document-it/rules/maintenance.md) | Updating existing documentation: target discovery, claim-based reconciliation, identity, connected documents, and consuming the review pass |
| [`rules/doc-style.md`](../skills/document-it/rules/doc-style.md) | Writing guidance shared by authoring and maintenance |
| [`rules/review.md`](../skills/document-it/rules/review.md) | Evaluating a finished document against its purpose and reporting findings |

**Handoff with `lab-it`** (§2): `lab-it` routes documentation requests here; this skill routes a
missing-or-stale-evidence sub-problem to `lab-it`'s investigation discipline and receives verified
findings back.

**No other downstream handoff exists.** A written or updated document, or a review report, is a
complete result on its own. GitHub is never touched by this skill; issue creation and Git workflow
belong elsewhere.

This skill documents technical systems. It does not own skill authoring: the repository's
[skill-authoring methodology](../docs/skill-authoring-methodology.md) governs this skill's own
files, not the other way round.

## 7. Boundaries, non-goals, and current confidence

This skill owns creating, maintaining, and reviewing technical documentation in Markdown. It does
not own investigation from scratch, architecture or product decisions reached with the user, or
`plan.md` synthesis (all `lab-it`'s); API specification generation; application implementation;
debugging or diff review; feature classification and issue decomposition; GitHub issue mutation;
delivery sequencing; or Git workflow.

**Current, honest limits:**

- The broadened purpose-driven contract, the conditional recap, the product-behavior review
  dimension, and the Markdown-only output are informed by session transcripts from two consuming
  projects, read retrospectively. Most of that use came from one project. Forward-use validation of
  the revised instructions in a live session, and broader cross-project portability, remain
  unverified.
- Maintenance across connected documents and the conditional reuse of an existing recap approval
  have been checked by source walkthrough against the rule files, not by a live invocation.
- The two-directional `lab-it` handoff depends on both skills agreeing on the same routing
  language and the same investigation-discipline contract. That agreement holds because both sides
  read from the same owning files — it is not independently enforced at runtime by either skill.
