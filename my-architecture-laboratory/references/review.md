# Reviewing an architecture guide

This is the methodology developed while iterating on the Documents and Tags architecture guides
— not a proofreading pass, a check on whether the document actually communicates the
architecture. A guide can be well-written and still fail this review; a guide with rougher prose
can pass it. Wording is not the subject.

## When to consult this file

- After Phase 3 produces a new guide, before considering it complete.
- After a Phase 4 maintenance edit, before considering the maintenance pass complete.
- Any time you're asked to refine an existing guide.
- Any time you're asked whether a guide is finished.

**Not** during Phase 1 Explore, and not while a guide is still being drafted — this is a review
of a finished artifact, not a drafting aid. Drafting uses `references/doc-style.md`; this file
is what you switch to once there's a document to hold up to the light.

## Philosophy

- The question is always "does this explain the architecture," never "does this read well."
- Every recommendation that comes out of a review must strengthen the reader's understanding of
  *how the system is built and why* — if a suggested change wouldn't change what a reader
  understands about the architecture, it isn't a finding, it's a preference. Drop it.
- Don't nitpick style, word choice, or section ordering unless the issue actually obscures an
  architectural claim (an ambiguous pronoun that leaves "who owns this" unclear is a finding; a
  synonym you'd have picked instead is not).
- A guide is allowed to have known gaps. The review's job is to make sure those gaps are stated
  (in Focused Improvements) rather than silently absent — an unstated gap is the finding, not the
  gap itself.
- The output of a review is a short list of findings, not a rewrite. Identify weaknesses; let the
  guide's author (you, in Phase 3/4, or the user) decide what to act on. Don't rewrite prose
  inline as part of a review pass.

## How to run it

1. Read the guide fresh — ideally by fetching the actual published Artifact URL, the way a new
   engineer would actually encounter it, rather than reviewing your own working draft from
   memory. Working from memory lets you silently fill in gaps that aren't actually on the page.
2. Work through the checklist below, category by category.
3. For every question you can't answer "yes" outright, write one finding: what's missing or
   unclear, and which section it's in. One sentence each — this stays lightweight by design.
4. Stop there. Don't fix findings inline. Report them, or act on only the ones that clearly
   matter, and leave stylistic judgment calls alone.

## Checklist

### Architectural center

- Is the architectural center immediately obvious — within the first section, not inferred by
  the end of the document?
- Does every major section reinforce that central idea, or does at least one section wander into
  a tangent that doesn't serve it?
- Does the summary leave the reader remembering the architectural abstraction itself (a contract,
  a pipeline, a boundary) rather than a list of features?

### Reusable capability

- Is reusable infrastructure clearly separated from integration-specific code — could a reader
  point to the exact line where "shared" ends and "per-integration" begins?
- Does the integration section show only what a new implementation must *provide*, not what it
  inherits for free? (Both guides make this an explicit, short list — three steps for Tags, one
  interface for Documents. If the integration section reads like a tutorial covering the whole
  feature, it's failing this question.)
- Are shared capabilities clearly distinguished from model-specific behavior, including in
  testing (does the guide separate "tests of the shared capability" from "tests of one
  integration," the way Tags does)?
- When the guide covers several concrete implementations of the same architecture (e.g. three
  resources built on one CRUD recipe), is one of them clearly established as the running example
  that carries the explanation, with the others invoked only where they demonstrate an intentional
  variation, exception, or pressure point in the shared pattern? Flag a guide that teaches several
  implementations in parallel to the point that the shared architecture is harder to follow than
  the examples themselves — ask whether one implementation is clearly the running example, whether
  the others are used only where they reveal a meaningful architectural variation, and whether
  feature-specific detail has started competing with the guide's actual subject. This isn't a
  rigid rule: multiple equal examples are legitimate when the architecture genuinely has no
  representative path, or when comparing the implementations is itself the architectural point.

### Runtime

- Is runtime ownership explained wherever the capability actually has runtime behavior — and
  conspicuously absent, not forced, where it doesn't?
- Is lifecycle kept separate from runtime ownership? A state machine (pending → processing →
  completed) and a responsibility handoff (page → composable → action → queue → notification)
  are different diagrams even when they describe the same feature — collapsing them into one
  diagram is a finding.
- Are state transitions distinct from responsibility transitions in the prose, not just the
  diagrams? ("The document becomes `failed`" is a state transition; "the queue hands off to the
  notification system" is a responsibility transition — a guide that uses one sentence shape for
  both is blurring them.)

### Implementation

- Does the guide explain the concept before showing code, every time, or does any section lead
  with a code block?
- Are code snippets limited to important contracts and extension points — an interface, a
  contract method, a scope — or has a full method body snuck in for narrative color?
- Has API documentation or an implementation walkthrough started replacing architecture anywhere?
  (A tell: a section that could be regenerated by reading the controller top to bottom instead of
  by understanding the design.)

### Structure

- Does each section answer exactly one architectural question — the one stated in its
  `section-prompt`? A section that tries to answer two questions usually means the document's
  structure hasn't actually been decided yet.
- Is the document's structure driven by the capability, or has it been forced into the previous
  guide's section list? (See `references/doc-style.md#section-inventory-is-not-fixed` — a
  finding here is a section that exists only because the last guide had one, not because this
  capability needs it.)
- Are diagrams used for movement and ownership — not decoration? An `.ascii` block that doesn't
  show something moving or something being owned is a candidate for deletion, not a finding to
  soften.
- Are tables used for responsibilities, guarantees, or trade-offs — not as a formatting choice
  for prose that would read fine as a paragraph?
- Do structural counts and labels mean the same thing everywhere they appear — "nine layers" vs.
  "nine files," a hero metric labeled "shared engines" that actually only counts backend engines,
  a spec-strip number that quietly drifts from what a table further down claims? Flag volatile
  configuration values (a pagination page size, a UI constant) presented as if they were durable
  architectural facts, and flag a section inventory that never gives a home to a feature the guide
  otherwise treats as core to the capability (named in the purpose, or repeated across sections,
  but never landing in a layer, table, or diagram of its own).

### Decisions

- Are architecture decisions cleanly separated from implementation detail in the decisions table
  — does every row state a *decision*, with a *reason*, and an accepted *trade-off*, rather than
  just describing what the code does?
- Are the items in Focused Improvements genuinely future work — deferred, with a stated reason —
  rather than something that's already been built? (A completed improvement left in the list is
  a finding; remove it during a maintenance pass, don't just leave it stale.)
- Are known limitations clearly identified as intentional, with the reasoning stated, rather than
  read as oversights? ("Deferred until a real one-hop model ships" is identified; a bare "TODO:
  handle this better" is not.)
- Does any absolute claim in the guide ("every mutation uses an Action," "every model carries the
  global scope," "every integration follows the same path") conflict with an exception documented
  elsewhere — or is an intended convention being stated as a universal implementation fact? The
  goal isn't zero exceptions; it's that the guide clearly distinguishes the intended convention
  from the current implementation from any known exception, and that a current exception is
  acknowledged wherever the convention itself is taught, not only in the one section (usually
  Focused Improvements) that lists it.

### Overall

- Could a new engineer extend the capability after reading this guide — implement a second
  integration — without reading the shared infrastructure's source first?
- Would another engineer understand *why* the system was designed this way, not just what it
  does? If you removed every "why," "because," and trade-off column from the document, would
  anything actually be lost? If not, the guide hasn't cleared this bar yet.
- For every feature the guide treats as a core part of the capability (exports were the case that
  surfaced this in the CRUD guide — the same question applies to notifications, search, reporting,
  imports, or background processing in a future one), can a reader locate its architectural layer
  or responsibility owner, its runtime path, its authorization and tenant-isolation guarantees, its
  testing boundary, and — where relevant — its own trade-offs or limitations? A feature mentioned
  repeatedly across sections without its ownership or lifecycle ever being pinned down anywhere is
  a finding, even if each individual mention is accurate on its own.

## What this review does not flag

- Word choice, sentence rhythm, or comma placement that doesn't change what's understood.
- A different but equally valid section order, when both orders communicate the architecture
  equally well.
- A missing content block (a `.pill`, an extra `.callout`) unless a real recurring distinction is
  currently being described in prose that a reader can't actually follow without it.
- Anything already listed, with a reason, in Focused Improvements — a stated known gap is not a
  finding.