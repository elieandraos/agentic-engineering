# Writing technical documentation

This file is the writing guidance used by `rules/authoring.md` and `rules/maintenance.md`. It
guides judgment; it does not prescribe a layout. `rules/review.md` evaluates the finished document.

Choose structure and depth from the document's purpose and audience, not a template. For
architecture, retain the architectural center of gravity; for operations, prioritize safe
execution; for references and integrations, prioritize understanding or lookup; for costs,
prioritize assumptions, totals and trade-offs; for product behavior, prioritize precise rules.
These are examples, not prescribed document types.

## Structure follows the subject

A document's sections follow what the subject's information actually looks like, not a copied
table of contents. Give each section a clear heading and whatever opening best serves the reader:
a direct explanation, a guiding question, a table, a diagram, or an executable command with its
necessary context. A question-led section is useful when it orients the reader; it is not
required.

Keep recurring concerns conditional: purpose, security, runtime ownership, decisions, limitations,
and a closing summary appear only when they materially improve understanding of *this* subject —
never because another document included them. The subject decides what each section is called,
how many there are, and where they sit. A closing takeaway can end a document without depending on
a section named "Summary."

Compact illustrations, not a checklist:

- A sequential lifecycle reads well as an ordered sequence.
- Independent responsibilities (several things true at once, not a sequence) read better as
  separate tables or flows.
- A real, ordered extension process or procedure reads well as numbered steps.
- A subject with no runtime behavior of its own shouldn't get a runtime section just because other
  documents have one.

## Markdown presentation

Use plain, portable Markdown, and choose each element for what it communicates. None is required;
use an element only when it serves the content better than prose.

- **Summary facts.** A short list near the top can ground the reader in a few concrete facts or
  guarantees — a size limit, a retry count, a schedule. Pick facts that reveal scale or
  guarantees, not vanity metrics.
- **Tables** suit responsibilities, guarantees, states, decisions, configuration, costs and
  trade-offs — one row per concern. Don't use a table for prose that reads fine as a paragraph.
  Where a row states an enforceable rule, an inline-code reference can name where it lives.
- **Numbered lists** suit genuinely sequential steps. Independent operations read better as
  separate bullets, tables or flows.
- **Diagrams** show movement, ownership, topology or relationships; a static topology diagram is
  valid on its own. Keep a diagram readable at a glance and accurate to the system. Use Mermaid
  only where the target renderer supports it; otherwise use a fenced plain-text diagram. Validate
  syntax and rendering when tooling permits, and report what could not be checked.
- **Code blocks** carry exact commands, configuration, or contracts, with a language tag when one
  applies. Explain prerequisites, consequences and verification where material. Keep secrets out.
- **Blockquotes** can hold a supporting explanation, such as a short "why this design?" note, that
  would interrupt the main line of reasoning.
- **Emphasis.** A bolded sentence can state a contract worth a concise close: "A caller integrates
  by composing X. It does not reimplement Y." Use the same short label or inline-code tag for the
  same recurring variant or status everywhere it appears.
- **Formulas.** A short inline or fenced formula can summarize a composition, cost or lifecycle
  when it reads clearer than prose.

Numbers can appear wherever they communicate best — a summary list, a table, or plain prose.

## Architecture material

- Establish the concept before showing code. In explanatory architecture material, limit code to
  genuine extension seams — a contract, an interface, a scope — not full method bodies.
- When a real line exists between reusable infrastructure and integration-specific code, make it
  explicit in whatever structure the document already uses — never a mandated section or table.
- Explain runtime ownership and lifecycle wherever the system has either — don't invent one for a
  capability with no runtime story.

## References and integrations

Use exact commands and configuration values when they are the subject of an operational or lookup
document. An integration or technical reference may document interface contracts, endpoints,
payloads, configuration keys and their constraints when the reader needs them to understand or
integrate. Explain how the technology works, why the project uses it, and its implications,
without becoming a generic tutorial. When an authoritative, discoverable specification exists —
generated API documentation, a provider's reference, the source itself — link to it instead of
copying it exhaustively.

## Product behavior and business rules

Documentation of product behavior records rules already decided; it does not decide them.

- Define each term once and use it consistently.
- State each rule with its boundaries — for example, whether a date limit is inclusive.
- Cover the states and transitions, the permissions, and the material exceptions the subject
  actually has.
- Keep examples consistent with the rules they illustrate.
- Mark a decision that is still open as open, and return it to the user rather than resolving it
  in the document.

## Connected and overview documents

Keep overview-level explanations in primary documents and detailed facts in their authoritative
reference. Link rather than repeat.

When introducing a larger system or connected documentation set, establish the big picture first.
Give each material subject a compact explanation of what it is, why it matters, and how it relates
to the whole. Link to its detailed document for configuration, mechanics, procedures or deeper
reasoning. The overview should be independently useful without becoming a duplicate handbook or a
directory of links. Use dates or explicit currency notes for volatile facts, estimates and pending
validation when useful.

## Tone and evidence

Declarative and technical; no marketing language — but declarative isn't the same as certain:

- State verified facts directly; don't hedge what you've confirmed.
- Label uncertainty, inference, and unresolved decisions honestly instead of smoothing them into
  confident-sounding prose.
- For material technical claims (a reuse guarantee, a security boundary, an ownership rule, a
  business rule), name the mechanism or evidence behind it — a symbol, a schema element, a config
  key, a protocol, a runtime boundary, whichever is appropriate to the system — not a fixed shape
  like "a class and a method" forced onto every claim.
- Avoid unsupported certainty: don't state something as universal ("every X does Y") unless
  you've verified it holds everywhere, and flag known exceptions instead of smoothing over them.
