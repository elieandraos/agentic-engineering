# Reviewing technical documentation

This file owns evaluating whether a finished document serves its intended purpose, and reporting
the findings. It is not a proofreading pass: a document can be well-written and still fail this
review, and a document with rougher prose can pass it. This file never edits the document.

## When this review runs

- **Standalone review** — the user asks whether a document is complete, accurate, or still fit for
  its purpose. The result is the findings report and nothing else. Don't edit the document; any
  fix needs its own authorized scope, through `rules/maintenance.md`.
- **Review pass inside authoring or maintenance** — `rules/authoring.md` or `rules/maintenance.md`
  runs this review on the document it just wrote or updated. This file still only evaluates and
  reports; the calling workflow owns acting on the findings.

Not while a document is still being drafted — this is a review of a finished document or of the
exact draft being proposed, not a drafting aid.

## Philosophy

- The question is whether the document serves its intended purpose and reader accurately and
  usefully, not whether it matches a preferred writing style.
- A finding is material when it affects whether the intended reader can correctly understand,
  operate, extend, look up or decide what the document is for — how a system is shaped and owned,
  whether a procedure can be run safely, whether a rule can be applied without guessing. If a
  suggested change wouldn't affect that, it is a preference, not a finding. Drop it.
- Don't nitpick style, word choice, or section ordering unless it actually obscures a technical
  claim (an ambiguous pronoun that leaves "who owns this" unclear is a finding; a synonym you'd have
  picked instead is not).
- A document is allowed known gaps. The review's job is to confirm that a gap which materially
  affects the reader is stated somewhere in the document, not silently absent — an unstated gap is
  the finding, not the gap itself.

## How to run it

1. Inspect the actual saved document — or the exact draft being proposed when none is saved yet —
   the way its intended reader would encounter it, not your own memory of drafting it. Working from
   memory lets gaps silently fill themselves in.
2. Establish the document's confirmed purpose and audience. Review against that purpose, not
   against an architecture template.
3. Work through the general questions, then only the purpose dimensions the document actually has.
   A question about a concern the subject doesn't have (reuse, runtime, security, costs,
   decisions, limitations) is inapplicable, not failed — skip it rather than forcing an answer.
4. When a claim's factual accuracy is in question, reconcile it against verified evidence, not the
   document's own wording. This is a truth check on an existing claim, not a fresh investigation —
   investigating the system from scratch is `lab-it`'s method, not this review.
5. Verify diagram semantics as well as syntax, and render when tooling permits. Never execute
   destructive procedures merely to review documentation. Match review effort to consequence and
   intended use.
6. For every question you can't answer "yes" outright, write one finding: what's missing, unclear,
   or contradicted, and where in the document. Then report.

## General questions

- **Accuracy.** Do material claims match verified evidence? Do evidence references resolve?
- **Status honesty.** Are verified behavior, approved design, estimates and pending verification
  distinguishable? Is a proposal or an open decision presented as settled?
- **Structure.** Does each section serve a coherent reader need, with a direct answer, rather than
  covering two unrelated questions at once? Is the structure driven by the subject and purpose,
  not carried over from another document — a section that exists only because another document had
  one is a finding?
- **Presentation.** Do diagrams show movement, ownership, topology or relationships rather than
  decoration? Are tables used for responsibilities, guarantees, states, decisions, configuration,
  costs or trade-offs rather than as formatting for prose?
- **Consistency.**
  - Do counts, labels, and guarantees mean the same thing everywhere they appear — a number in one
    place matching what a table or diagram elsewhere claims?
  - Is a volatile configuration value presented as a durable fact?
  - Does every subject the document treats as core have an identifiable home — some place where
    its ownership or definition is pinned down — rather than being mentioned repeatedly without one?
  - Does any absolute claim ("every mutation uses X") conflict with an exception documented
    elsewhere, or state an intended convention as a universal fact? The document should
    distinguish convention from current behavior from known exception, and note an exception
    wherever the convention itself is taught.
- **Currency.** Does the document describe current reality or an explicitly approved design,
  rather than narrating history or release notes?
- **Connected documents.** Is subject ownership clear? Do cross-links, including links to headings
  within the document, resolve? Do shared claims
  agree, without unnecessary duplication? Check affected neighboring documents, not only the target.
- **Location.** A new document lives under `docs/` or the location the user or project named. An
  updated document keeps its existing path unless the user authorized relocating it — a path
  outside `docs/` is preserved identity, not a defect.

## Purpose dimensions

Apply each dimension only where it is part of the document's purpose. These are examples, not
modes; a document can combine several.

### Architecture

- Is the architectural center of gravity clear early enough to orient the reader, and does every
  major section reinforce it rather than wander into a tangent? Where the document has closing
  material, does it leave the reader with the architectural abstraction itself — a contract, a
  pipeline, a boundary — rather than a list of features?
- Are responsibilities, ownership, and boundaries explicit — could a reader point to where one
  component's responsibility ends and another's begins? Where a material rule, guarantee, or
  boundary has an identifiable enforcement mechanism, is it named, without forcing a class/method
  shape onto a rule enforced some other way?
- Where reusable infrastructure sits alongside integration-specific code, is the line between them
  explicit? Where an extension seam exists, does the document distinguish what a new
  implementation must *provide* from what it inherits? When several implementations of the same
  architecture appear, is one the running example, with the others invoked only for a meaningful
  variation — unless comparing them is itself the point?
- Where the capability has runtime behavior, is runtime ownership explained, and kept distinct from
  lifecycle state? Are state transitions ("the record becomes X") distinguishable in the prose from
  responsibility transitions ("component A hands off to component B")?
- Does explanatory material establish the concept before showing code, with snippets limited to
  genuine extension seams? Has an implementation walkthrough started replacing the design — a
  section regenerable by reading the source top to bottom?
- Would another engineer understand *why* the system was designed this way? If every "why,"
  "because," and trade-off were removed, would anything architectural be lost? Does the document
  leave the reader understanding the impact of a future change and the invariants it must
  preserve?

### Operations

Prerequisites, exact commands or actions, ordering, safeguards, failure consequences, recovery and
verification. Is a proposed procedure distinguished from a tested one?

### References and integrations

Accurate mechanisms, configuration names and values, interface contracts, scope, dependencies,
overrides, security constraints and lookup usability. Does the document link to an authoritative
specification instead of copying it exhaustively?

### Costs and capacity

Arithmetic, units, billing periods, assumptions, exclusions, shared versus incremental costs, and
estimates versus actual charges.

### Approved designs and decisions

Where the document records a decision, does it state the decision, the known rationale, and the
accepted trade-off, plus implementation status and pending verification? Missing rationale is a
finding, not something to invent.

### Product behavior and business rules

- Are terms defined once and used consistently across the document and connected documents?
- Is each rule stated clearly enough to apply without guessing, including its boundaries?
- Are lifecycle states and transitions complete for what the document claims to cover?
- Are permissions stated where they govern behavior?
- Are material exceptions stated where the rule itself is taught?
- Do examples agree with the rules?

A contradictory or missing decision is a finding to report, not a decision for the reviewer to
make.

### Limitations and deferred work — when the document states any

- Is deferred work genuinely still open, with a stated reason? A completed item left in as future
  work is a finding.
- Is each known limitation's real status accurate — intentional, deferred, unresolved, or an
  acknowledged defect — with its consequence stated, rather than a bare "TODO"?
- A known and accurately stated limitation is not itself a finding, unless it contradicts another
  claim, hides a consequence that matters, or is presented misleadingly.

## Review output

- Report only material findings, one sentence each: what's missing, unclear, contradicted, or
  obscured, and where in the document.
- Include the relevant evidence when a finding is a factual mismatch against verified evidence.
- Order by consequence.
- Report checks that could not be performed, such as rendering that tooling did not permit.
- If there are no material findings, say the document passes. Don't invent improvements to avoid
  returning a clean review.

## What this review does not flag

- Word choice, sentence rhythm, or comma placement that doesn't change what's understood.
- A different but equally valid section order or shape, when it serves the purpose equally well.
- A missing presentation element, unless the reader can't follow the content without it.
- A purpose dimension or question that doesn't apply to the subject.
- A stated known gap, unless it contradicts another claim, hides a material consequence, or is
  presented misleadingly.
- A scope-limited update of connected documents that the user authorized, as long as the remaining
  divergence is reported and no document is presented as current when it isn't.
- An existing document's path outside `docs/`, when that path is its preserved identity.
