# Documentation style — grammar and precedent

This file is the deep reference for Phase 3. It exists because the two source guides prove
structure adapts to the capability — this file explains *how* to read that adaptation so you
reproduce the reasoning, not the surface shape.

## The rhythm every section follows

Regardless of what a section is about, it opens the same way:

1. `section-head` — a two-digit stage number in a circle, then an `<h2>` naming the section.
2. `section-prompt` — one italicized, first-person-omitted guiding question. Always a real
   question the reader would actually ask, never a restatement of the heading:
   - "What problem does this capability solve, and what architecture solves it?"
   - "How can one document system support many different owner types?"
   - "Who owns responsibility while a document moves through the running system?"
   - "How does the architecture stay correct and secure as new taggable models are added?"
3. `section-intro` — one muted paragraph that directly answers the prompt before any detail
   follows. The reader should be able to stop after this paragraph and still have the right
   mental model, just not the depth.

Everything after that is composed from the content blocks below, chosen per section, not all of
them every time.

## Content block vocabulary

| Block | CSS | Use for |
|---|---|---|
| Spec strip | `.specsheet` (in the hero only) | 3–6 concrete operational facts grounding the reader before any prose — file size limits, retry counts, cascade behavior, "models implementing this today: 1". Pick facts that reveal scale or guarantees, not vanity metrics. |
| Ownership/flow diagram | `.ascii` | Monospace box-and-arrow diagrams (`─│▼├└`) for both data relationships ("owner → Document") and runtime sequences. Keep it simple enough to read in one glance — this is not the place for exhaustive detail. |
| Responsibility table | `.table-wrap > table.lc` | Component catalogs (name / type / responsibility), decision/trade-off tables, security-concern tables, state tables. One row per concern. End rows that map to a specific enforcement point with an `<span class="src-ref">Namespace\Class</span>`. |
| Ordered timeline | `.flow-steps` | A sequence that happens in strict order over time, with named phases (bold, e.g. **Stage**, **Finalize**, **Process**) each carrying sub-bullets. Use only when steps are genuinely sequential — not for a bag of independent operations (see Tags' catalog/attachment tables instead). |
| Side card | `.callouts > .callout` | A single-topic aside: the "Current reference implementation" status card in section 01, a "Why this architecture?" micro Q&A table, a boundary explanation ("Persistence boundary"), or the "Architectural principles" bullet list that sits between Decisions and Improvements in both reference guides. |
| Equation recap | `.formula` | A monospace composition or cost formula — `A + B + C ─── = outcome`, or a chained count (`N files → N requests → 1 job → 1 notification`). Closes a lifecycle/operations section and reappears in the Summary as the capstone. |
| Variant badge | `.pill` (+ a variant class, e.g. `.two-hop` / `.one-hop`) | Short inline tags distinguishing 2–3 recurring variants discussed across a section — reuses the `--tag-current-*` / `--tag-illustrative-*` CSS custom properties already defined in the template. Define new pill variant classes per capability only when you actually need to visually distinguish recurring cases; don't add pills for their own sake. |
| Clincher sentence | plain `<strong>` | One bolded sentence closing Building Blocks and Integrating: states the reuse contract in a single line — "A page integrates X by composing Y. It does not reimplement Z." This is the sentence a skimming reader should walk away with. |

## Section inventory is not fixed

Both reference guides return to the same recurring conceptual anchors — a purpose statement,
security and integrity, architectural decisions paired with an "Architectural principles"
callout, and a closing summary. A runtime-ownership table shows up in both, but only because both
capabilities happen to have a meaningful runtime story; a capability without one shouldn't get a
runtime anchor forced onto it. None of this fixes the numbering, placement, naming, or exact
sequence of these anchors — the two reference guides put them at different section numbers, and a
third guide is free to put them somewhere else again. The capability's architectural center of
gravity decides where each anchor belongs and what it's called; the anchor list below is a set of
recurring concerns, not a table of contents to reuse. Everything else was named and shaped for the
capability:

| # | Documents (pipeline-oriented) | Tags (extension-oriented, two sub-capabilities) |
|---|---|---|
| 02 | **Reusable document model** — the polymorphic schema story (`documentable_type`/`documentable_id`), because the foundation *is* a data-model decision | **The Taggable contract** — a two-method interface, because the foundation is an interface decision (`ownerColumn(): ?string`), not a schema |
| 03 | Building blocks — one backend table, one frontend section | Building blocks — explicitly **two** tables (catalog vs. attachment), because the capability genuinely is two independent things sharing one data model |
| 04 | Integrating a page — narrative walkthrough of the one seam (`Documentable`) | Integrating a model — a **numbered 3-step checklist**, because integration here really is three discrete, ordered acts (implement contract → register morph alias → bind composable) |
| 05 | **Upload lifecycle** — one `.flow-steps` sequence (Stage → Finalize → Process → Notify → Reconcile), because the capability *is* a pipeline | **Tag operations** — two independent `.table-wrap` tables (catalog ops, attachment ops) plus one `.flow-steps` for the single genuinely-sequential case (create-then-attach), because most operations are NOT sequential |
| 06 | One runtime `.ascii` flow + one Document state-machine diagram | **Two** runtime `.ascii` flows (catalog management, attachment), because there are two independent runtime paths |
| 08 | Testing organized around HTTP integration boundaries versus independently testable shared infrastructure | Testing — explicitly split **shared capability** vs. **integration-specific**, plus a named-and-justified untested branch |
| 11 | One `.formula` (composition) + one `.formula` (request-count chain) | Two intro paragraphs (whole capability, then the two-sub-capability split) + two `.formula` blocks (composition, per-operation cost) |

The lesson isn't "copy whichever row looks closest." It's: **name each section after what the
capability actually does at that stage**, and let the number and shape of tables/diagrams follow
from whether the capability is genuinely one linear thing or genuinely several independent
things. A future notification-infrastructure guide might need a "Delivery channels" section that
neither reference guide has at all — that's correct, not a deviation to correct.

## Tone

Declarative, technical, no hedging, no marketing language. State the mechanism, not just the
claim: never "this is reusable" without naming the interface/class/method that makes it so right
next to the claim. Prefer "X exists because Y" and "Not Z, because —" over softer framings.
Numbers belong in the specsheet and in tables, not buried in prose.

## Choosing a favicon

Pick one or two emoji from the capability's domain (📄 documents, 🏷️ tags) and keep it stable
across every redeploy of that guide — the Artifact tool requires a favicon on every publish call,
including updates, so re-supply the same one each time rather than omitting it. If you're
resuming a guide you didn't originally publish and don't know which emoji was used, ask the user
rather than guessing a new one — a changed favicon reads to them as a different document.

## Reviewing what you wrote

This file covers the grammar to write *with* — it is not the methodology for critically
evaluating what came out the other end. Once a guide is drafted (or after a maintenance edit),
switch to `references/review.md` and run its checklist against the actual document. Don't
self-check against this file's block vocabulary and call that a review — reviewing architectural
communication is a separate pass with its own philosophy, and it's deliberately not loaded during
Phase 1 or while you're still drafting.