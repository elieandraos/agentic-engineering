# Skill-Authoring Methodology

A practical methodology for authoring and evolving evidence-backed Claude Code skills: how to
decide what belongs in a skill, where a given piece of knowledge should actually live, how a rule
earns its place, and how to keep a skill's supporting files internally consistent as it changes.

**Authority boundary.** This document owns authoring judgment and knowledge disposition — how a
skill is written, generalized, and kept reconciled. It does not own the operational behavior of any
specific skill; each skill's own `SKILL.md`, `README.md`, and rule/reference files remain
authoritative for their own runtime contract. Section 12 states this boundary explicitly against
operational skills and packaging tooling.

**Revision rule.** When authoring work turns up a case that disproves or refines a principle here,
update this document from that evidence. This document is not a changelog: it holds the current,
reusable methodology, not a chronological log of every pass that shaped it. Case-by-case, per-skill
evidence belongs in version control or a temporary authoring record — not in this document, and not
in a skill's architecture dossier, which holds current architecture, rationale, and
evidence-calibrated confidence, not a growing case-by-case history (Section 7).

## 1. What skill authoring means

Skill authoring is more than editing prose. It includes:

- identifying the capability and its activation boundary;
- separating portable methodology from stack and project knowledge;
- deciding which file owns each contract;
- rewriting fused material where selective deletion would destroy the reusable intent;
- routing non-portable knowledge to the correct destination;
- treating instruction-bearing supporting artifacts — templates, examples, tables, and
  checklists — with the same rigor as prose rules (Section 8);
- verifying that a rule's stated conditionality survives every representation of it, not only its
  entrypoint statement — a diagram, table row, checklist item, or example can silently reimpose
  "mandatory" after the owning text already said "optional." A caveat correctly stated once
  elsewhere in the same file does not make an earlier diagram, summary, or example conditional on
  its own; each representation must carry the same authority and optionality independently;
- reconciling callers, summaries, and downstream handoffs;
- validating the result as a cold reader or agent would;
- retaining evidence without making history a runtime prerequisite.

Success is not measured by how much text a rewrite preserves or deletes. A contract can shrink
because reusable substance moved into routed reference files rather than disappearing, or grow
because a real conditional distinction needed stating explicitly for the first time — neither
direction is itself the goal. The criterion is whether the result lets a reader or agent with no
access to the origin project's history make every decision correctly using only what the file
contains.

## 2. Knowledge classification and destination

A passage in a skill or its supporting files may carry one or more of the following knowledge
types — a single passage can fuse portable methodology, a stack-specific answer, a project
convention, and historical framing all at once. Classify by concept, not only by paragraph or
section: identify each concept a passage carries, classify each independently, and split or
rewrite the passage when its fused concepts have different destinations.

**Portable methodology** — decision rules, invariants, gates, evidence standards, ownership
boundaries, and workflows reusable across consuming projects, independent of any one project's
stack or domain. Home: a portable skill.

**Reusable stack/ecosystem knowledge** — framework, runtime, ORM, frontend, testing, tooling, or
platform conventions reusable across projects on the same stack. A concrete artifact type, a
framework lifecycle behavior, or a stack-native command may belong here, but only once evidence
shows it is reusable across projects on that stack rather than one project's local convention.
Home: a stack-specific skill or reference; this document does not create one.

**Project-specific knowledge** — durable project rules, product conventions, domain vocabulary,
repository policies, metadata conventions, or integration expectations shared by everyone working
in that project. Home depends on scale: short, stable, broadly applicable instructions belong in a
stable, team-visible project instruction file (e.g. `CLAUDE.md`); substantial or conditional
project or domain knowledge that should load only for relevant tasks belongs in a project-local
skill or a version-controlled project reference, routed from that instruction file.

**Initiative-specific approved decisions** — architecture, preserved behavior, product decisions,
exclusions, and constraints that belong to one initiative rather than the project globally. Home:
an approved plan document, and the canonical work that results from it — not a portable rule or a
project-wide instruction file.

**Live or discoverable state** — facts whose authoritative value comes from current code,
configuration, a tracker, a provider, or another external system. Home: query the live source when
needed; do not freeze it into static instructions.

**Personal preference or continuity context** — preferences that improve collaboration with one
person but are not canonical project policy. Home: personal memory. Useful for how one person
likes to work; wrong as the sole source of a rule other users, teammates, or cold-start agents also
need — durable project knowledge belongs in a project instruction file, project-local skill, or
reference instead, not only in personal memory.

**Historical evidence** — earlier cases and defects that explain why a current rule exists but are
not required to execute it. Home: version-control history or a temporary authoring record — not a
skill's architecture dossier (Section 7).

**Obsolete material** — incorrect, contradicted, duplicated, superseded, or purely incidental
content. Home: none. It is not relocated merely because it was removed; deleting it and letting
version control retain the record is normally sufficient.

Do not present a historical finding as a current defect without checking the current file first. A
document written during an earlier pass can describe a defect, a missing capability, or a fused
dependency that has since been fixed; treat every historical citation as a claim about the file's
state at the time it was written, not a standing fact, and re-verify it against the file as it
exists now before repeating it.

Two cross-cutting rules apply regardless of type: a fact reliably discoverable from code should
normally remain in code or configuration rather than being duplicated into agent prose, and
sensitive data never belongs in a skill, dossier, project instruction file, or personal-memory
substitute. Which of these homes a specific consuming project actually uses for a specific fact
remains an explicit, project-level choice; this document records the criteria for choosing among
them, not a decision it makes on a project's behalf.

## 3. Knowledge-disposition ledger

Use a disposition ledger during an authoring pass to track, per concept rather than per deleted
sentence, what a removed or rewritten passage carried:

| Field | Meaning |
|---|---|
| Source | Original file the concept came from |
| Removed or rewritten concept | The knowledge carried by the original passage |
| Classification | Portable, stack, project, initiative, live state, personal, historical, or obsolete |
| Surviving lesson | Reusable reasoning preserved from it, if any |
| Destination | Portable skill, stack layer, project guidance, plan document, runtime discovery, dossier, or nowhere |
| Status | Retained, generalized, rewritten, deferred, extracted, or intentionally discarded |
| Evidence | Why this disposition is justified |
| Confidence / open question | Whether another project or authoring pass must validate it before treating it as settled |

The ledger exists to prevent two opposite failures at once: losing reusable stack or project
knowledge during generalization by deleting it outright, and dumping every removed example into a
new project-specific file without proving it deserves preservation. Keep a pass's own ledger
entries in a temporary authoring record, not a skill's architecture dossier (Section 7) — a dossier
holds current architecture and evidence-calibrated conclusions, not case-by-case disposition
history.

## 4. Evidence-to-rule graduation

- Do not create speculative rules for imagined failures.
- Prefer evidence from real use, demonstrated ambiguity, a concrete failure, or a decision existing
  instructions refused to resolve.
- One project-specific fact is not automatically portable methodology.
- Repeated evidence may justify promotion, but repetition alone does not prove policy — repetition
  confined to one project is still one project's evidence, not proof of portability across
  projects.
- A rule must change decisions or materially improve correctness to earn its place.
- A fact an agent can reliably discover from authoritative code or configuration usually does not
  need a duplicated rule.
- Replace an obsolete rule rather than accumulating nearby qualifications and exceptions around it.
- Keep historical evidence outside runtime instructions unless a compact example materially teaches
  the rule.
- When classifying an observed lesson, ask whether it is portable methodology, reusable stack
  knowledge, stable project policy, live state, historical evidence, or obsolete material — not
  whether it is memorable.
- A rule should graduate only into the narrowest layer supported by its evidence. Decline a
  skill-wide restructuring when the evidence only supports a narrower, local fix.

This is not "never create a rule until a failure occurs" — that overstates the principle. The
standard is proportionate evidence, not imagination: a high-risk invariant can justify an explicit
rule before a failure actually occurs, when the risk and the reasoning behind it are concrete
rather than speculative. Withholding a rule for an unencountered edge case is correct only when a
standing escalation path (asking a human, deferring the decision) already covers that case — that
is a deliberate choice to leave the case to that path, not a gap. By contrast, a rule adopted from a
single explicit human decision, rather than repeated observation, is real and authoritative
immediately, but should be marked with a weaker confidence claim — "current and authoritative"
rather than "validated as portable" — until repeated evidence, ideally from more than one consuming
project, supports the stronger claim.

**A second, stricter bar: promoting a rule into shared tooling.** Adopting a principle as a
current, authoritative rule inside one repository is a lower bar than promoting it into shared,
general-purpose skill-authoring tooling or guidance meant to serve skills and projects beyond this
one. Promote a principle to that second tier only once it is:

- supported by repeated real authoring evidence, not a single instance;
- reusable outside the skill or project where it was first observed;
- shown to change a decision or prevent a demonstrated ambiguity, not merely stylistically
  preferred;
- properly a concern of skill authoring itself, not an operational skill's own runtime behavior;
- not a duplicate of a contract already owned elsewhere;
- statable without requiring the reader to know a specific origin project's history;
- validated by a cold read and, separately, by a forward-use check on real authoring work — these
  are two distinct checks with potentially different results, and a principle can pass one without
  yet having been tested by the other;
- placed at the narrowest disclosure layer that actually needs it.

A principle resting on evidence from only one project, or only one authoring pass, has not yet met
the repeated-evidence and reusable-outside-origin criteria on its own — one project or one pass is
not repeated, independent evidence. Mark such a principle as a working conclusion pending
independent evidence, not as settled guidance, until a separate consuming project or a separate
authoring pass tests it. Distinguishing "this is current, authoritative repository policy" from
"this is validated, portable guidance ready for shared tooling" is itself part of the discipline
this section asks for — apply it to this document's own claims as much as to any rule inside a
skill.

## 5. Authoring workflow

1. Establish the current authoritative baseline — resolve it from version control; do not assume a
   commit or state.
2. Read the skill completely, including its callers and downstream consumers.
3. Map ownership before editing prose.
4. Classify the current passages by knowledge type (Section 2).
5. Identify the portable intent beneath project-specific evidence.
6. Decide whether to retain, generalize, rewrite, route, or discard each concept.
7. Rewrite the owning contract.
8. Reconcile `SKILL.md`, `README.md`, cross-references, and downstream summaries.
9. Perform cold-read behavioral checks: can a reader with no origin-project history apply the rule
   correctly using only the file?
10. Record dispositions and authoring observations in a ledger (Section 3), not in the skill's
    architecture dossier (Section 7).
11. Complete a full re-read and scope verification before publication.

This sequence describes responsibilities, not mandatory section headings or a fixed number of
subprocesses. A given pass may fold several steps into one commit, or split one step across
several, depending on how fused the source material is.

Step 9's cold-read check is necessary but not sufficient for executable supporting material — a
template's embedded script, a generated command, or any other runtime logic. Also trace the real
production entry or discovery path — the actual selector, call site, or invocation the runtime
uses — rather than validating only by invoking an internal helper directly with a hand-picked
input; a helper can be provably correct in isolation while the path that actually reaches it in
production silently excludes the exact case it was written to handle.

A consuming project typically holds a copied snapshot of a skill rather than a live reference back
to its canonical source. When a defect surfaces through a consuming project's use, correct the
canonical source first — the corrected file becomes the new source of truth, and any
already-installed copy is stale until it is refreshed from it. Patching an installed copy directly,
without correcting the canonical source, lets the two drift and reintroduces the same defect the
next time a fresh copy is taken.

## 6. Ownership and conceptual-modeling principles

- Classify by product or system responsibility, not by framework or implementation artifact.
- Distinguish adjacent decisions that carry different authority or outcomes, even when they
  resemble a single decision or a single gate.
- Authority overlays — an approval gate, a review requirement — should not be modeled as a peer
  outcome alongside the substantive result they gate.
- Assign one canonical owner to each contract or decision.
- Route to the owning contract rather than duplicating it. A cross-reference stays accurate as the
  owning rule evolves; a restatement drifts out of sync with it silently.
- A composed or blueprint-shaped artifact may describe and route to the rules it draws on without
  restating their canonical matrices, tables, or decision content. Describing what a rule owns is
  not the same act as owning it — a summary may name an owner, but must not silently become a
  second authority for the same decision.
- Explicitly state where an exceptional path converges back into the ordinary workflow, rather than
  leaving the reader to infer it.

Many authoring defects come from collapsing two related but distinct decisions into one outcome
list, one gate, or one overloaded paragraph — for example, treating "has authorization been given"
and "should this proceed now" as two separate approvals when they are really one decision asked
twice, or the reverse: merging two genuinely different questions into a single gate that silently
skips one of them. The fix in both directions is structural — separate what is actually one
decision from what is actually two — not a wording adjustment to either gate.

Duplication is especially dangerous where two files can each believe the other owns a decision, and
so drift independently without either file's own text signaling a problem — for instance, when a
supporting blueprint restates the same ownership rule that a separate, dedicated rule file already
owns. The fix is not to reconcile the wording in both places; it is to delete the duplicate
entirely and leave the dedicated rule as the sole owner, with the blueprint routing to it by
reference.

## 7. Runtime and supporting file ownership

- `SKILL.md` should contain only the vocabulary and mechanics necessary for activation, routing,
  essential invariants, and major handoffs — including stack-specific vocabulary where the skill
  itself is stack-specific and that vocabulary is what activation actually requires. Rule and
  reference files own substantial conditional or mode-specific mechanics instead.
- `README.md` explains the lifecycle and reasoning without becoming an operational duplicate. Add a
  README specifically when a human maintainer needs a conceptual map, rationale, taxonomy, or
  lifecycle explanation that would otherwise burden or duplicate the always-loaded operational
  entrypoint — not by default, and not merely for symmetry with sibling skills that happen to have
  one. The two files must be read together during reconciliation to confirm they stay
  complementary, not restatements of each other — a README repeating a routing table, or a
  `SKILL.md` repeating a README's rationale, is a duplication defect even when both files are
  individually well-written.
- Runtime skill instructions (`SKILL.md` and rule/reference files) hold the current operational
  contract, not a changelog.
- A skill's own architecture dossier preserves current architecture, rationale, ownership,
  boundaries, and evidence-calibrated confidence, kept up to date as the skill changes — not
  case-by-case history, chronological evidence, removed prose, or per-pass disposition ledgers;
  those remain in version control or a temporary authoring record instead.
- Project instruction files supply durable project context.
- Code, configuration, and live systems remain authoritative for discoverable state.

Progressive disclosure:

- keep the always-loaded entrypoint as short as the complete activation contract allows;
- move substantial conditional guidance into routed references;
- do not create extra files or routing layers without a real conditional need;
- do not force every skill into the same folder or heading structure — let each file's own
  structure follow what it explains, not a template shared with sibling skills.

**Semantic classification over historical filename or location.** A resource's type, directory, and
name should follow how it changes agent decisions and how it is consumed — never its original
location, its historical filename, or a desire for structural symmetry with sibling files. A file
that reads as a single, independently applicable convention belongs with rules; a file whose real
content is a multi-component implementation shape — several classes, a wiring point, and tests that
only make sense installed together — belongs with a different category, such as a blueprint,
regardless of which directory it happened to be authored into first. A misleading filename can
persist even after a resource's actual classification was never wrong, so check the name as its own,
separate question. The reusable principle:

> Choose a resource's type, location, and name from how it changes agent decisions and how it is
> consumed — not from its historical filename or a desire for structural symmetry.

This does not impose any one fixed directory taxonomy — rules, blueprints, templates, or
otherwise — as a universal structure every skill must adopt. A given split is one evidence-backed
answer for one skill's actual content; another skill may need fewer categories, or different ones,
depending on what its own content actually is.

## 8. Instruction-bearing supporting artifacts: examples and templates

Supporting artifacts — templates, examples, tables, and checklists — are instruction-bearing and
deserve the same rigor as prose rules, since each can shape agent behavior or generated output even
when it looks like presentation rather than instruction. Two related but distinct artifact kinds
need their own standard: illustrative code examples embedded in prose, and complete copy/adapt
implementation templates.

For illustrative code examples:

- use neutral domain concepts rather than leaking a real consuming project's product vocabulary,
  models, or literals into a portable skill's public-facing examples;
- demonstrate one relevant contract at a time;
- preserve coherence across related snippets — when several examples form one flow, a reader
  following the whole chain should see one consistent example, not fragments from different
  fictional features;
- use one consistent established idiom for the same operation unless a contrast is intentional and
  explained, rather than silently mixing equivalent-but-different constructions for the same
  contract;
- do not present technically invalid or incomplete pseudocode as if it were runnable;
- illustrative snippets may omit irrelevant detail when the omission is clear, the way a concise
  example from high-quality framework documentation would.

Copy/adapt implementation templates are held to a stricter bar than illustrative snippets, because
a reader is meant to install them directly rather than merely read them for understanding:

- a complete, intended implementation — not a partial illustration;
- an explicit target path and prerequisites stated in the file itself;
- reconciliation instructions: inspect the consuming project for an existing equivalent before
  installing, and reconcile rather than overwrite;
- relevant syntax or execution validation before treating the template as ready to copy.

Call an artifact a generator stub only when an actual generator or placeholder-substitution
mechanism consumes it — never merely because it is a complete file meant to be copied. A complete,
syntactically valid source file that a reader copies and adapts by hand is a template, not a
generator stub, regardless of its file extension or format; the criterion is whether a generator
actually consumes the file, not what its extension happens to be.

## 9. Concision

- Avoid artificial minimum word counts.
- A lower bound invites padding and preserves duplication.
- Use a soft ceiling only when it helps constrain drift.
- The correct length is the shortest complete expression of the contract.
- Added text is justified when it resolves a real ambiguity, protects an invariant, or preserves a
  necessary distinction.
- Shorter is not automatically better when deletion collapses distinct decisions.
- Longer is not automatically more complete.
- An instruction such as "open by distinguishing X from Y" is guidance to the author, not
  necessarily literal target prose.
- Never hard-wrap inside an inline code span.
- Replace obsolete policy instead of accumulating qualifications around it.

Different files in the same skill can legitimately move by different amounts, and in different
directions, under this same discipline — the right length is a property of what each file's own
contract requires, not a shared ratio applied uniformly across a skill.

## 10. Controlled technical English

> Write normative skill instructions in controlled technical English. Prefer active voice, direct
> subjects and actions, one stable term for each defined concept, and one operational instruction
> per sentence when practical. Split complex conditions, exceptions, and consequences into
> structured clauses or bullets. Preserve exact identifiers, paths, commands, quotations, and
> externally defined names. Do not sacrifice necessary authority, exceptions, or technical meaning
> merely to shorten a sentence.

- This is controlled technical English informed by Simplified Technical English, not ASD-STE100
  compliance. Strict ASD-STE100 is a formal controlled language with its own approved vocabulary and
  grammar — not a synonym for clear writing — and nothing here claims to satisfy it.
- Do not use synonyms merely for stylistic variety in normative rules.
- Runtime instructions should be controlled and precise.
- READMEs and dossiers may use more natural explanatory prose.
- Do not mechanically ban every contraction.
- Do not force one instruction into one sentence when splitting it would obscure necessary
  conditions or authority.
- Do not force one paragraph onto one physical line.
- Do not force identical structure across unrelated rule files.
- Do not rewrite a correct skill merely to make it appear more STE-like.

Official standard, linked exactly once: [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).

Three distinct categories, not one indivisible standard:

1. **Controlled-language conventions** — the sentence- and term-level discipline above.
2. **Markdown/diff-formatting conventions** — inline-code-span wrapping, table formatting, heading
   structure. Formatting hygiene, unrelated to sentence-level word choice.
3. **Rule-governance philosophy** — how a rule earns its place (Section 4), where it lives
   (Sections 2, 7), and how it stays reconciled with its callers (Section 11). Governance,
   unrelated to prose style.

## 11. Cross-file reconciliation

- Changing an owning rule may make its callers, indexes, READMEs, and downstream summaries stale;
  reconciliation is its own required pass, not an automatic byproduct of rewriting the owning file.
- Correct stale references and summaries in the same coherent pass when scope permits; do not
  duplicate the corrected procedure into every consumer instead.
- Cross-rule cohesion is behavioral consistency, not identical wording. Cold-read scenarios are
  useful specifically for testing whether one decision routes to exactly one owner.
- Validation should test meaningful behavior and invariants, not merely match expected phrases or
  headings.

Scope the search by dependency, not by convenience and not by an unbounded full-repository re-read:
inspect the owning file itself; inspect its known callers, summaries, indexes, and any direct or
indirect consumer actually affected by the changed contract — including consumers entirely outside
the skill being authored, since re-reading only the file just changed is not sufficient. For a move
or rename specifically, run a repository-wide search for the old name or path: an actual Markdown
link (which must resolve from the file that contains it), a path mentioned in code or a code
comment, and a plain-prose filename mention all need checking, since a link checker alone catches
only the first kind — a bare filename reference can otherwise point at the wrong file once more
than one directory could plausibly hold one with that name. This is a bounded, dependency-driven
search, not a mandate to re-audit unrelated parts of the repository for every change.

## 12. Boundaries with operational skills and packaging tooling

This document owns authoring judgment and knowledge disposition: how a skill is written, evolved,
and kept internally consistent. It deliberately does not own, and should not duplicate, any
operational skill's own runtime workflow — for example:

- an architecture-investigation skill's own investigation method and architecture-decision
  workflow: how it investigates a system, what its own deliverables are, and where its own approval
  gates sit;
- a feature-planning skill's own issue-planning workflow: how it classifies, scopes, and drafts
  tracker issues;
- a delivery-lifecycle skill's own workflow: how it sequences commits, review gates, verification,
  and release.

Each of those is an operational skill's own contract, owned entirely by that skill's own `SKILL.md`
and rule files. This document only supplies the discipline used to author and evolve any such skill
in the first place; it never restates what one of them decides at runtime.

It similarly does not own a skill-packaging or validation tool's own responsibilities: capturing
intent, drafting a triggering description, running iteration or evaluation loops, grading against
test prompts, or packaging a finished skill for distribution. The boundary is one of ownership, not
sequence — such tooling may wrap, drive, or participate at any point across an authoring lifecycle,
not only after this document's judgment has already been applied elsewhere. This document owns
knowledge classification and authoring judgment: what a piece of knowledge is, where it belongs,
and how a skill stays internally consistent. Packaging and validation tooling owns its own
triggering, evaluation, iteration, validation, and packaging mechanics. A principle in this document
graduates into such tooling's own guidance only once it meets the stricter bar in Section 4 — it is
not pre-embedded there, and this document does not describe or depend on any particular tool's
internals.

## 13. Pre-publication validation

Before treating an authoring pass as complete, check:

- **structure** — headings, tables, and lists render correctly, and the document's own section
  order matches its actual content rather than a template copied from an unrelated file;
- **links** — every Markdown link resolves from the file that contains it;
- **references** — every path, filename, and cross-reference names a location that currently
  exists, especially after a move or rename (Section 11);
- **examples** — illustrative snippets are technically valid for the standard stated in Section 8,
  not merely plausible-looking pseudocode;
- **templates** — a copy/adapt template still satisfies its stricter bar (Section 8): complete,
  target path and prerequisites stated, reconciliation instructions present, and syntactically or
  executably valid;
- **changed-file scope** — the set of files actually touched matches the intended scope of the
  pass, with no incidental unrelated edits folded in.
