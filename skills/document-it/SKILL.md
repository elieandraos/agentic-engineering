---
name: document-it
description: "Creates, updates, and reviews explanatory architecture guides in Markdown, a Claude Artifact, or both — reusing sufficient, current, verified understanding already available, and routing to lab-it's investigation method only when evidence is missing or stale. Trigger to document existing architecture, update an existing guide, or review a guide's completeness. Not for investigating a system from scratch, debugging, reviewing a diff, resolving architecture decisions for a proposed feature, or synthesizing plan.md — those stay with lab-it."
---

# document-it

## What this skill does

This skill creates, maintains, and reviews explanatory architecture guides — in Markdown, a Claude
Artifact, or both — from already-available, sufficient, and current understanding. It is
independently callable: a documentation request does not require a fresh investigation to begin.

| User intention                                    | Result                                         |
| --------------------------------------------------- | ------------------------------------------------ |
| Document existing architecture                     | A new guide (Markdown, Artifact, or both)        |
| Reconcile a guide with verified changed reality    | An updated existing guide                        |
| Evaluate whether a guide is complete               | A findings report, not a rewrite                 |

## Evidence: reuse first, route to `lab-it` only when needed

Before writing or updating anything, establish whether currently available understanding is
sufficient and current:

- **Sufficient, current evidence already exists** — from this conversation, a recent
  investigation, or evidence directly verifiable against the real system right now. Use it
  directly. Don't repeat a full investigation just because a documentation workflow is starting.
- **Evidence is missing or stale.** Route the relevant investigation through `lab-it`'s canonical
  investigation method (its "Shared investigation and decision discipline") rather than
  duplicating that method here. Once `lab-it` returns verified findings, resume the documentation
  workflow.

This distinction determines the entry point, not the destination: the result is always a guide, or
a review of one — never a `plan.md`. An approved `plan.md` stays `lab-it`'s output regardless of
which skill performed the underlying investigation; file extension does not decide ownership.

## Format selection

For a **new guide**, ask the user whether they want an Artifact, Markdown, or both — unless
they've already specified. Don't infer the format from context.

- **Artifact** output uses `rules/template.html` and requires the `artifact-design` skill and the
  `Artifact` tool. Load `artifact-design` before writing any Artifact page.
- **Markdown** output lives under the consuming repository's own `docs/` directory; create that
  directory if it doesn't already exist. Markdown has no `template.html` equivalent and does not
  need Artifact-specific tooling — it must work without it.
- If the requested format's publishing capability is unavailable (no `Artifact` tool, no write
  access to the target repository), explain that plainly and ask the user how to proceed. Never
  silently substitute the other format and report success as if the original request were
  fulfilled.

## Document existing architecture

Route: establish sufficient current evidence (reuse, or route to `lab-it`) → recap and obtain
confirmation → decide structure from the architectural center of gravity → write in the confirmed
format(s) → publish/save → run `rules/review.md`.

1. **Establish evidence.** Confirm the architectural surfaces the guide will cover are backed by
   concrete, current evidence — implementation, configuration, schema, tests, runtime behavior.
   Reuse what's already sufficient and current; route missing or stale evidence through `lab-it`.
   Identify the **architectural center of gravity** — the one idea everything else hangs off (a
   polymorphic contract, a queue pipeline, a runtime subsystem boundary, a sync-vs-async split) —
   as a hypothesis the writing step will need.

2. **Recap and confirm.** Write the recap directly as chat output, not a file or an artifact.
   Cover, with concrete implementation references threaded throughout, whichever of these actually
   apply to the system: the problem being solved, the core architecture, reusable pieces versus
   integration-specific code, runtime behavior, the data model, the integration seam, security,
   testing, architectural decisions, and remaining gaps. Don't invent a data model, runtime
   lifecycle, security boundary, reuse seam, or integration split the system doesn't have just to
   fill out the list. Keep it bullet-driven and honest about gaps. **Stop here and wait for the
   user to confirm before this investigation becomes a published guide.** A correction here is
   real signal about what the guide needs to get right.

3. **Write and publish/save the guide.** Only after the recap is approved, and only after format
   selection (above):
   - Decide the document's structure from the confirmed center of gravity. Architecture guides do
     not use one fixed section inventory: structure follows the system being explained. See
     `rules/doc-style.md` for the writing grammar and content-block vocabulary — it covers both
     Markdown and Artifact output.
   - **Artifact:** load the `artifact-design` skill (required before writing any Artifact page).
     Write the HTML using `rules/template.html` as the starting scaffold. Replace content; keep
     the design system unless the system genuinely needs a new block type. Publish with the
     `Artifact` tool: title `"{Capability} Architecture"`, a one-sentence description, and a
     stable, domain-appropriate favicon (see `rules/doc-style.md#choosing-a-favicon-artifact-only`).
   - **Markdown:** write the guide under the consuming repository's `docs/` directory (create it
     if needed), applying the same writing grammar and content-block vocabulary in Markdown-native
     form (see `rules/doc-style.md`).
   - **Both:** produce both outputs from the same confirmed recap and center of gravity, and give
     each a minimal, discoverable cross-reference to the other's location (see "Maintaining both
     formats," below).
   - Run `rules/review.md`'s checklist against the finished guide(s) before considering the work
     complete — see "Output-specific non-negotiables" for what the guide itself must do.

## Update an existing guide

Use this workflow when a published guide needs reconciling with verified current reality —
triggered by a stale architectural claim, a stale evidence reference, changed configuration or
runtime behavior, or a prior documentation defect, not only a changed implementation.

**Locate and inspect the actual target before updating it.** Discover it from what's supplied: a
stated file path or Artifact URL, an existing cross-reference from another guide or from project
documentation, or a repository search by capability name. Ask the user when identification remains
ambiguous — don't guess, and don't assume the target's content from memory.

**Distinguish three different situations**, since each needs a different response:

- **Genuinely missing** — no guide exists yet at the expected identity. This is a new-guide
  request, not an update; route to "Document existing architecture" above.
- **Inaccessible** — the target exists (a known file path or Artifact URL) but can't currently be
  reached or read.
- **Publishing capability unavailable** — the target is fine, but the tooling needed to update it
  (e.g., no `Artifact` tool in this session) is missing.

For the second and third situations, explain the limitation concretely and ask the user whether to:
prepare or update a Markdown version instead; create a replacement Artifact where that's possible;
or change which format is the maintained one going forward. State which document would change and
which would remain unchanged or stale — the user doesn't need to understand "draft versus
migration" to make this choice. **Never claim that writing a Markdown update updated the original
Artifact** — those are different documents once an Artifact can't be reached or written.

Once the target is confirmed reachable: compare its architectural claims against verified current
implementation, configuration, runtime evidence, and tests (reuse sufficient current evidence;
route to `lab-it` when it's missing or stale) → follow the complete affected claim graph, not only
the section where the change was first noticed → update to describe how the architecture works
now, not as a changelog → preserve identity (below) → run `rules/review.md` against the whole
updated guide, with emphasis on the changed claims and whatever depends on them.

`rules/maintenance.md` governs every judgment call in this route — read it before making any edit.
It preserves a guide's unaffected architectural meaning without freezing architecture the evidence
shows has genuinely changed: the center of gravity, structure, ownership, or reasoning can move
when verified reality requires it.

**Preserve identity by default:**

- **Markdown** — the same file path. Preserve unaffected front matter, title, and other metadata,
  while allowing the changes the requested update actually requires.
- **Artifact** — the same `url` and the same favicon.

## Maintaining both formats

When a guide is maintained in both Markdown and Artifact:

- **Keep architectural claims synchronized** across both on an update, unless the user explicitly
  requests otherwise for that update.
- **Format-appropriate presentation, not identical rendering.** Use `rules/review.md` for both —
  one shared checklist, with a handful of items that apply to only one medium (favicon/URL checks
  apply to Artifact only; a link-integrity/structure check applies to Markdown only).
- **Keep the association between the two outputs discoverable** through a minimal cross-reference
  each carries to the other's location — not a registry, and nothing beyond that is required.
- **Report precisely which outputs changed**, and name any remaining divergence or publication
  failure, rather than reporting a single "done." A partial failure (e.g., the Markdown update
  succeeds but the Artifact can't be reached) is reported as exactly that — which document
  changed, which stayed stale, and why.

## Review a guide

Run `rules/review.md` against the actual published or saved guide — Artifact, Markdown, or both —
any time you're asked to evaluate whether a guide is complete or still architecturally misleading,
independent of whether you also just wrote or updated it. See `rules/review.md` for the full
checklist and its medium-conditional items.

## Ownership and handoff

This skill owns:

- creating new architecture guides, in Markdown, Artifact, or both;
- maintaining and reconciling existing guides with verified current reality;
- reviewing a guide for architectural completeness.

This skill does not own:

- investigation from scratch when understanding is missing or stale (→ `lab-it`);
- architecture decisions reached with the user, or `plan.md` synthesis (→ `lab-it` — file
  extension does not decide ownership: an approved `plan.md` stays `lab-it`'s even though it is a
  `.md` file);
- application implementation;
- debugging or diff review;
- API reference documentation;
- feature classification and issue decomposition;
- GitHub issue mutation;
- delivery sequencing;
- Git workflow.

## Rule and supporting-file routing

These are loaded only when their workflow needs them — none is a universal prerequisite:

- guide writing (Markdown and Artifact) → `rules/doc-style.md`
- Artifact scaffold → `rules/template.html`
- guide review → `rules/review.md`
- guide maintenance → `rules/maintenance.md`

## Output-specific non-negotiables

- Explain architecture, not implementation: why it exists, why it's shaped that way, and — where
  extension is relevant — how it can be extended. Code blocks exist only at genuine extension
  seams, never a walkthrough of a whole method body.
- When a real line exists between reusable infrastructure and integration-specific code, make it
  explicit in whatever structure the guide already uses — never a mandated section or table.
- Explain runtime ownership and lifecycle wherever the system has either — don't invent one for a
  capability with no runtime story.
- Ground material architectural claims in concrete evidence or enforcement references when an
  identifiable mechanism exists; never force a misleading one.
- No API documentation, no endpoint inventories, no line-by-line implementation walkthroughs, no
  duplicated explanations across sections.
- Not every guide needs a limitations section. When limitations or deferred work materially affect
  understanding, state the reason rather than adding a generic TODO list.
- A guide is never done until it has passed a `rules/review.md` pass — writing and reviewing are
  two separate steps.
