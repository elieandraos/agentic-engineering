# Documentation style — grammar for technical guides

Choose structure and depth from the document's purpose and audience, not a template.
For architecture, retain the architectural center of gravity; for operations, prioritize
safe execution; for references, prioritize understanding or lookup; for costs, prioritize
assumptions, totals and trade-offs. These are examples, not prescribed document types.

## Section rhythm

Use a clear heading and whatever opening best serves the reader: a direct explanation,
a guiding question, a table, a diagram or an executable command with necessary context.
Questions and introductory paragraphs are useful when they orient the reader, not mandatory.
Keep Artifact section styling compatible with the existing scaffold without forcing every
section to use every element. Use only content blocks that earn their space.

## Content-block vocabulary


| Communicates | Artifact block (CSS) | Markdown equivalent |
|---|---|---|
| Concrete facts or guarantees grounding the reader before prose — a size limit, a retry count, a cascade behavior. Pick facts that reveal scale or guarantees, not vanity metrics. | Spec strip — `.specsheet` (hero only) | A short bulleted list of 3–6 facts near the top of the guide, before the first section |
| Ownership or topology: data relationships and runtime sequences. Keep it readable in one glance. | Ownership/flow diagram — `.ascii` | A Mermaid diagram when supported, or a fenced monospace diagram |
| Responsibility mapping: component catalogs, decision/trade-off tables, security-concern tables, state tables — one row per concern. | Responsibility table — `.table-wrap > table.lc` | A standard Markdown table. End an enforceable row with an inline-code reference — a path, symbol, schema element, config key, protocol, or runtime boundary, whichever actually identifies where the rule lives |
| Chronological sequence: strictly ordered phases. Only for genuinely sequential steps — independent operations read better as separate tables or flows. | Ordered timeline — `.flow-steps` | A numbered list, each item bold-led with sub-bullets |
| Supporting explanation: a status card, a short "why this architecture?" Q&A, or a boundary explanation. Not tied to a particular section or position. | Side card — `.callouts > .callout` | A blockquote |
| Composition, cost, or lifecycle summary, used when a formula reads clearer than prose. May close a section or the guide; not required because a section covers an operation. | Equation recap — `.formula` | An inline or fenced formula line |
| Recurring variants: short inline tags for 2–3 recurring variants. Add a new variant only when a recurring distinction genuinely needs one. | Variant badge — `.pill` (+ a variant class) | Inline code or a short bold tag, used consistently for the same variant everywhere it appears |
| Closing takeaway: one bolded sentence stating a reuse contract — "A caller integrates by composing X. It does not reimplement Y." Useful for a contract worth a concise close; not required by subject, nor by section name. | Clincher sentence — plain `<strong>` | A bolded sentence, identical in role |

Don't force an Artifact CSS class into a Markdown file, or invent Markdown-only formatting inside
an Artifact page — write each format the way it's natively read.

## Section structure

Use exact commands and configuration values when they are the subject of an operational or lookup guide. Explain prerequisites, consequences and verification where material. Keep secrets out. Diagrams must accurately represent the system; validate syntax and rendering when tooling permits, and report what could not be checked.

For connected guides, keep overview-level explanations in primary documents and detailed facts in their authoritative reference. Link rather than repeat.

**Overview documents.** When introducing a larger system or connected documentation set, establish the big picture first. Give each material subject a compact explanation of what it is, why it matters, and how it relates to the whole. Link to its detailed guide for configuration, mechanics, procedures or deeper reasoning. The overview should be independently useful without becoming a duplicate handbook or a directory of links. Use dates or explicit currency notes for volatile facts, estimates and pending validation when useful.

A guide's section list follows what the subject's information actually looks like, not a
copied table of contents. Compact illustrations, not a checklist:

- A sequential lifecycle reads well as an ordered timeline.
- Independent responsibilities (several things true at once, not a sequence) read better as
  separate tables or flows.
- A real, ordered extension process reads well as numbered steps.
- A capability with no runtime behavior of its own shouldn't get a runtime section just because
  other guides have one.

Keep recurring concerns conditional: purpose, security, runtime ownership, decisions, limitations,
and a closing summary appear only when they materially improve understanding of *this*
capability — never because a previous guide included them. Nothing here requires a section
literally named Building Blocks, Integrating, Architectural principles, Focused Improvements,
Runtime, or Summary — a guide may cover those concepts, but the capability decides what each is
called, how many there are, and where they sit. A closing-takeaway block (the clincher sentence,
the formula recap) can still end a guide; it just can't depend on that section being named
"Summary."

## Tone and evidence

Declarative and technical; no marketing language — but declarative isn't the same as certain:

- State verified facts directly; don't hedge what you've confirmed.
- Label uncertainty, inference, and unresolved decisions honestly instead of smoothing them into
  confident-sounding prose.
- For material technical claims (a reuse guarantee, a security boundary, an ownership
  rule), name the mechanism or evidence behind it — a symbol, a schema element, a config key, a
  protocol, a runtime boundary, whichever is appropriate to the system — not a fixed shape like "a
  class and a method" forced onto every claim.
- Avoid unsupported certainty: don't state something as universal ("every X does Y") unless
  you've verified it holds everywhere, and flag known exceptions instead of smoothing over them.

Numbers can appear wherever they communicate best — a spec strip, a table, or plain prose.

## Choosing a favicon (Artifact only)

Pick one or two emoji from the capability's own domain and keep it stable across every redeploy —
the Artifact tool requires a favicon on every publish call, including updates, so re-supply the
same one rather than omitting it. When maintaining a guide you didn't originally publish, discover
or confirm its current favicon first — read the published Artifact, or ask the user if you can't
tell — rather than silently picking a new one; a changed favicon reads as a different document.
Markdown output has no favicon equivalent; a Markdown guide's identity is its file path.

## Responsibility routing

This file covers the grammar to write *with*. It doesn't own what belongs elsewhere:
`rules/template.html` owns the Artifact HTML/CSS scaffold and the classes named above;
`rules/review.md` owns critically evaluating a finished guide — don't mistake self-checking
against this file's block vocabulary for a review, that's a separate pass run once a draft
exists; `rules/maintenance.md` owns changing an existing guide without breaking its narrative;
`rules/authoring.md` owns format selection and the new-guide/existing-guide-update procedures that
call on this grammar; `SKILL.md` owns which workflow you're in, which format(s) apply, and how
these files route together.
