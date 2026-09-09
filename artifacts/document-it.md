# document-it — Architecture Dossier

Status: Current
Scope: `document-it` as it stands in this repository
Purpose: A compact architecture artifact for the skill — its evidence-reuse-first model and its
two-directional relationship with `lab-it`, the three results it produces and where each asks for
human confirmation, format selection and identity preservation across Markdown and Artifact, the
guide as a published/saved document (rendering, identity, accessibility), the maintenance model,
the review checklist, rule ownership, and current boundaries and confidence.
[`SKILL.md`](../skills/document-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/document-it/README.md) is the human-facing orientation. This document
explains the architecture behind both rather than restating either.

## 1. Purpose and result model

`document-it` creates, maintains, and reviews explanatory architecture guides — in Markdown, a
Claude Artifact, or both — from already-available, sufficient, and current understanding. It is
independently callable: a documentation request does not require a fresh investigation to begin,
and does not require [`lab-it`](../skills/lab-it/) to have run first.

| Workflow | Terminal output | What gates that output |
|---|---|---|
| Document existing architecture | A new guide (Markdown, Artifact, or both) | The user confirms the investigation recap before writing |
| Update an existing guide | The same guide, reconciled and re-saved/redeployed | Only when authority, intent, or a material decision is unclear |
| Review a guide | A findings report, not a rewrite | Nothing — the report itself is the result |

This skill's result is always a guide, or a judgment about one — never a `plan.md`. An approved
`plan.md` stays `lab-it`'s output regardless of which skill performed the underlying investigation;
file extension does not decide ownership.

## 2. Evidence reuse first, and the two-directional relationship with `lab-it`

Before writing or updating anything, this skill establishes whether currently available
understanding is sufficient and current — from the conversation, a recent investigation, or
evidence directly verifiable against the real system right now. When it is, this skill proceeds
directly; it does not repeat a full investigation merely because a documentation workflow is
starting.

**When evidence is missing or stale, this skill routes the relevant investigation through
`lab-it`'s own investigation method** (its "Shared investigation and decision discipline") rather
than duplicating that discipline here. `lab-it` investigates and hands back verified findings; it
does not draft a guide itself, even when the investigation it performed originated from a
documentation request. This skill then resumes the documentation workflow with those findings.

**The relationship runs in both directions, not one.** `lab-it` itself recognizes a guide-shaped
request — "document," "update the guide for," "is this guide still accurate" — as outside its own
scope and routes it here (`lab-it/SKILL.md`'s own routing table lists this as one of the three
results using `lab-it` can produce). This skill, in turn, draws on `lab-it`'s investigation
discipline only for the narrower, missing-evidence sub-problem, and always hands the result back to
its own writing/maintenance/review workflow rather than treating an investigation as a reason to
defer the documentation decision itself. Neither direction implies the other skill performs the
requesting skill's own terminal output: `lab-it` never publishes a guide, and this skill never
produces a `plan.md` or reaches an architecture decision with the user on its own.

This distinction determines the entry point, not the destination: however a documentation request
arrives — directly, or routed here from `lab-it` — the result is always a guide or a review of one.

## 3. Format selection and identity

**A new guide.** Ask the user whether they want an Artifact, Markdown, or both, unless they've
already specified — never infer the format from context. Artifact output requires the
`artifact-design` skill and the `Artifact` tool, loaded before writing any Artifact page. Markdown,
for a new guide, lives under the consuming repository's own `docs/` directory by default — this is
a default for a *new* guide only, not a requirement imposed retroactively on an existing one.
Markdown has no `template.html` equivalent and must work with no Artifact-specific tooling at all.
If the requested format's publishing capability is unavailable, explain that plainly and ask how to
proceed — never silently substitute the other format and report success as if the original request
were fulfilled.

**An existing guide.** Locate and inspect the actual target before touching it — a stated path or
URL, an existing cross-reference, or a repository search by capability name; ask rather than guess
when identification is ambiguous. Three different situations need three different responses:
genuinely missing (route to "new guide" instead), inaccessible (the target is known but can't
currently be reached), or the publishing capability itself unavailable (the target is fine, the
tooling isn't). For the second and third, explain the limitation concretely and ask whether to
prepare a Markdown version instead, create a replacement Artifact, or change which format is the
maintained one — stating which document would change and which would stay stale, never requiring
the user to understand a "draft versus migration" taxonomy to decide. Never claim that writing a
Markdown update updated the original Artifact once the two have diverged.

**Preserve identity by default.** Markdown preserves the same file path — including one outside
`docs/`, since that default only ever applied at creation — and preserves unaffected front matter,
title, and metadata; Markdown metadata is not treated as universally immutable, unlike an
Artifact's identity. Artifact preserves the same `url` and the same favicon, both with equal
weight: neither changes as a side effect of an ordinary content update. Relocating a Markdown
guide's path, or minting a new Artifact to stand in for updating an existing one, both require the
user's explicit authorization.

## 4. The guide as a published or saved document

A guide's section list is decided by its confirmed architectural center of gravity — the one idea
everything else hangs off (a shared contract, a pipeline, a runtime boundary, a data-ownership
split) — never poured into a fixed inventory. Two guides for two different capabilities
legitimately have different section counts, names, and content. What's fixed is the rhythm each
section opens with (a heading, an italicized question a reader would actually ask, then one
direct-answer paragraph) before composing from a shared content-block vocabulary — a spec strip of
concrete facts, an ownership/flow diagram, a responsibility table, an ordered timeline, a callout, a
formula recap, a variant badge, or a closing sentence — chosen per section, never applied
uniformly. See [`rules/doc-style.md`](../skills/document-it/rules/doc-style.md) for the full
grammar and the Markdown/Artifact form each block takes; this dossier does not restate its
vocabulary.

**Artifact identity and rendering.** A guide's title follows `"{Capability} Architecture"`. Its
favicon is one or two domain-appropriate emoji, supplied at first publish and re-supplied unchanged
on every redeploy — a changed favicon reads as a different document, so a maintenance pass
discovers or confirms the guide's current favicon before touching anything.
[`rules/template.html`](../skills/document-it/rules/template.html) is a self-contained scaffold by
explicit operational constraint: no `DOCTYPE`/`html`/`head`/`body` wrapper (the Artifact tool
supplies those at publish time), and no external requests or CDN dependency — every rule and script
is inline. Theming runs on CSS custom properties across three coexisting paths: a light default on
bare `:root`, a `prefers-color-scheme: dark` media override, and an explicit
`data-theme="dark"`/`"light"` attribute override that wins in both directions over the media query.
The layout is a responsive two-column shell — a sticky section nav beside the main content column —
collapsing to one column under an 880px breakpoint. The syntax highlighter enhances exactly five
disclosed `data-lang` values (PHP, TS, Vue, JSON, HTTP) with token coloring and a tinted label;
every other case — an unsupported-but-present `data-lang`, or none at all — still reaches an
HTML-escaped, unhighlighted plain-code fallback rather than being skipped or left unescaped. The
template carries specific, verifiable accessibility signals: `:focus-visible` outlines on
interactive elements, one `aria-label="Sections"` on the nav landmark, a
`prefers-reduced-motion: reduce` override that disables smooth scrolling, and a semantic heading
hierarchy (`h1` hero, `h2` per section, `h3`/`h4` for subdivisions) — signals, not a certified
contract; no formal accessibility audit (measured contrast ratios, for example) is built into this
skill.

**Markdown identity and rendering.** A Markdown guide's identity is its file path — there is no
favicon equivalent. It applies the same writing grammar and content-block vocabulary in
Markdown-native form (a fenced-code diagram instead of the Artifact's `.ascii` block, a standard
Markdown table instead of `.table-wrap`, a blockquote instead of a side card, and so on), and must
communicate the architecture with no Artifact-specific tooling, template, or rendering constraints
at all — it is a first-class output, not a fallback.

**Both formats maintained.** Keep architectural claims synchronized across both on an update,
unless the user explicitly requests otherwise for that update; report precisely which outputs
changed and name any remaining divergence rather than reporting a single "done," distinguishing a
publication failure from a user-authorized single-format update; keep the association between the
two outputs discoverable through a minimal cross-reference each carries to the other's location —
not a registry, and nothing beyond that is required.

## 5. Maintenance model

[`rules/maintenance.md`](../skills/document-it/rules/maintenance.md) governs every judgment call in
reconciling a published guide with verified current reality without breaking the identity and
architectural meaning it already carries. The maintenance unit is the **architectural claim** — a
center of gravity, a responsibility, a boundary, an invariant, a lifecycle, an integration seam, a
decision and its trade-off, a limitation, or a concrete evidence reference — not the section,
table, or paragraph that happens to carry it; the same claim routinely repeats across several of
those, and a maintenance pass follows the complete connected claim graph a change actually touches,
not only the section a triggering issue or PR happened to name.

A reconciliation pass classifies what it finds into exactly one of four outcomes: no documentation
event (not every commit is one — leave the guide alone); a narrow update (one fact or reference is
wrong, correct it in place); a connected architectural change (several claims move together,
follow the graph); or unresolved authority, intent, or a material decision (stop — route to the
user, or to `lab-it` when it requires fresh investigation or an architecture decision, rather than
deciding it during maintenance). This four-way classification is specific to how a maintenance pass
triages what it finds; it is a different mechanism from `lab-it`'s own four-category claim model for
a synthesized `plan.md` (locked decision, current-state fact, derived constraint, open detail) — the
two should not be conflated even though both use a four-way split.

Maintenance fails in two opposite directions this rule exists to prevent: leaving stale
documentation in place for the sake of continuity, and rewriting or restructuring beyond what the
verified change actually requires. Continuity means preserving every unaffected claim, explanation,
and presentation choice — not rewriting nearby prose merely because the file is open, and not
restructuring for taste or conformity with another guide's shape. Continuity is not the same as
freezing the guide's center of gravity, ownership, or reasoning in place: when verified architecture
has genuinely moved one of those, the guide moves with it, in proportion to what changed. The guide
is written as present-tense architecture, never a changelog — a past decision or rejected
alternative is preserved as durable rationale when it materially explains the current shape, but
release-history narration is not.

## 6. Review

[`rules/review.md`](../skills/document-it/rules/review.md) is a check on whether a *finished* guide
actually communicates the architecture, run only against a published Artifact, a saved Markdown
file, or the exact draft being proposed — never mid-draft, since drafting is `doc-style.md`'s job,
not this one. Its checklist categories (architectural center; responsibility and ownership;
reuse/integration/variation; runtime, lifecycle, and state; architecture versus implementation;
structure and content; consistency; decisions and limitations; format-specific checks) are each
conditional on the architecture actually having that concern — an inapplicable category is skipped,
not failed. A known, honestly-stated gap is not itself a finding; an unstated one is. Format-specific
checks apply narrowly: an Artifact's favicon stability and preserved `url`; a Markdown guide's
`docs/`-relative location for a new guide (or its preserved existing path, including outside
`docs/`, for an update) and working internal links; and, when both formats are maintained, whether
their claims stay synchronized or an authorized divergence is honestly reported. The output is a
short list of findings ordered by consequence, never a rewrite — the review reports, and the guide's
author decides what to act on.

## 7. Rule ownership and cross-skill handoffs

Every file under `rules/` answers a question none of the others do, and is loaded only when its
workflow actually needs it — none is a universal prerequisite. `template.html` is deliberately not
called a rule: it's a scaffold to edit, not a normative statement the way the other three are.

| File | Owns |
|---|---|
| [`rules/doc-style.md`](../skills/document-it/rules/doc-style.md) | The writing grammar for guides: section rhythm, the content-block vocabulary in both Markdown and Artifact form, tone and evidence discipline, favicon stability |
| [`rules/template.html`](../skills/document-it/rules/template.html) (scaffold, not a rule) | The Artifact HTML/CSS/JS: theme tokens, the responsive shell, content-block CSS classes, the highlighter and its fallback contract |
| [`rules/review.md`](../skills/document-it/rules/review.md) | Judging whether a finished guide, in either format, communicates its architecture |
| [`rules/maintenance.md`](../skills/document-it/rules/maintenance.md) | Reconciling an existing guide with verified current reality without breaking its identity or unaffected meaning |

**Handoff with `lab-it`**, stated precisely (§2): `lab-it` routes a guide-shaped request here; this
skill routes a missing-or-stale-evidence sub-problem to `lab-it`'s investigation discipline and
receives verified findings back. Neither direction produces the other skill's terminal output.
File extension does not decide ownership either way: an approved `plan.md` stays `lab-it`'s even
though it's a `.md` file, and a Markdown architecture guide is this skill's even though it isn't an
Artifact.

**No other downstream handoff exists.** A published or updated guide, or a review report, is a
complete result on its own — it never implies a handoff to `plan-it` or any other skill. GitHub is
never touched by this skill; issue creation and Git workflow belong entirely elsewhere.

## 8. Boundaries, non-goals, and current confidence

This skill owns creating new architecture guides, maintaining and reconciling existing ones, and
reviewing guides for architectural completeness, in Markdown, Artifact, or both. It does not own
investigation from scratch when evidence is missing or stale, architecture decisions reached with
the user, or `plan.md` synthesis (all `lab-it`'s); application implementation; debugging or diff
review; API reference documentation; feature classification and issue decomposition; GitHub issue
mutation; delivery sequencing; or Git workflow.

Two dependencies are deliberate, named openly rather than disguised as neutrality: Artifact output
depends on the Claude Artifact tool and the `artifact-design` skill; Markdown output has no such
dependency and must work without either. Neither makes this skill tracker- or stack-specific.

**Current, honest limits:**

- The Artifact identity, rendering, and accessibility contract in §4 is stated as an explicit
  operational constraint inside the template and its own inline documentation. Nothing in this
  skill's files independently confirms how a specific renderer actually displays a published guide —
  the guide review checks whether a guide communicates architecture, not whether a rendered page
  meets a measured contrast ratio or a formal accessibility standard.
- The syntax highlighter enhances five named languages with a disclosed, safe fallback for anything
  else — a bounded, honestly-scoped renderer capability, not a hidden assumption, but still a literal
  list: a guide documenting a system in an unlisted language renders that code unhighlighted, not
  mis-rendered. Content preservation through highlighting — comments, strings, and PHP attributes
  surviving intact, and an unsupported or missing `data-lang` reaching the plain-text fallback rather
  than aborting the highlighting pass for every block after it — is confirmed by executing the
  shipped script against a minimal DOM stub in Node (`scenarios.md`'s template follow-up records).
  That is script-execution verification, not a rendered page or a published Artifact; real-browser
  rendering of the highlighted output remains unexercised by this evidence.
- The responsive two-column shell's mobile breakpoint (§4) — the sticky section nav becoming a
  static block at or below 880px — is confirmed by source and cascade inspection only: enumerating
  every rule that can set the relevant properties, confirming their selectors share one specificity,
  and resolving each property to whichever declaration is later in source order and applicable at
  the given width. This is not a browser-rendered or computed-style result; treat it as unverified in
  an actual browser until a connected browser tool or headless runner checks it directly.
- Markdown output was extended from an originally Artifact-only contract (Step 2 of this
  repository's ecosystem migration). Its writing grammar, review checklist, and maintenance
  discipline are written to be format-equal by design, but that equality has not yet been exercised
  by a real Markdown-guide maintenance pass in a consuming project — this dossier does not claim
  otherwise.
- The two-directional `lab-it` handoff (§2) depends on both skills agreeing on the same routing
  language and the same investigation-discipline contract. That agreement holds because both sides
  read from the same owning files — it is not independently enforced at runtime by either skill.
