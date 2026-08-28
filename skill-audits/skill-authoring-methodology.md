# Skill-Authoring Methodology

## Status and purpose

- **Status:** evidence-backed working methodology. It is not yet universal `skill-creator` policy.
- **Evidence base:** the completed authoring, cohesion, and dossier work for `my-git-workflow` (`skill-audits/my-git-workflow.md`, plus the now-superseded portability audit preserved as historical evidence at `503e638bb926a7f437838cc0eb50f9ffbf59c766:skill-audits/my-git-workflow-portability.md`), `my-feature-planning` (`skill-audits/my-feature-planning.md`), and `my-architecture-laboratory` (`skill-audits/my-architecture-laboratory.md`). All three skills share the same pre-authoring baseline commit, `fe5bd29` ("Externalize Phase A skills: my-feature-planning, my-git-workflow, my-architecture-laboratory"), which introduced every current `SKILL.md`, `README.md`, and `rules/*.md`/`references/*.md` file for all three skills. `my-git-workflow` and `my-feature-planning` were copied verbatim from their origin project at that commit; `my-architecture-laboratory` was externalized with its package-name, frontmatter, and path adaptation (`architecture-laboratory` renamed to `my-architecture-laboratory`, plus a `{{Project}}` placeholder fix) already applied, before its own authoring pass began. `my-git-workflow` and `my-feature-planning`'s authoring passes are the commits between `fe5bd29` and their shared authoring-evidence endpoint, `d8cbaf293c544ce30e3bc042ac43dd6c9e8f13d7`; `my-architecture-laboratory`'s is the twenty-commit pass between `fe5bd29` and its own endpoint, `b3c726ab263a719f7c179e342d150d42c0f457ee` — each skill's last pre-methodology-update authoring correction, not current `main` HEAD. This document was itself committed after each skill's respective endpoint.
- **Third proving pass completed:** `my-architecture-laboratory`'s authoring pass supplied a third distinct real proving pass within this authoring program (Sections 1, 6, 9, 13, and 16 integrate its evidence) — not independent-project validation, since all three passes ran inside this same repository. No further authoring pass is required before reassessing graduation; packaging the surviving principles into `skill-creator` itself remains the separate, later step Section 16 describes.
- **Authority boundary:** the current operational skills and their rule files remain authoritative for their own behavior. This document owns authoring methodology and knowledge disposition, not any operational engineering workflow.
- **Revision rule:** if a later skill-authoring pass disproves or materially refines a principle here, update this working methodology from that evidence.
- **Not a changelog:** this document is not a chronological change log and does not reproduce every historical edit. Per Section 10: Git history and historical audit evidence — including the portability audit that once lived at `skill-audits/my-git-workflow-portability.md` and is now deleted from the current tree, recoverable only at `503e638bb926a7f437838cc0eb50f9ffbf59c766:skill-audits/my-git-workflow-portability.md` — preserve chronology, exact removed prose, and earlier repository states. Current dossiers — `skill-audits/my-git-workflow.md`, `skill-audits/my-feature-planning.md`, and `skill-audits/my-architecture-laboratory.md` — preserve current skill-specific architecture, rationale, and evidence-backed assessment. Runtime skill files hold the current operational contract. This document owns reusable authoring methodology and knowledge disposition.

A worked illustration of the discipline this document asks for: `phase-discovery.md` records that `my-feature-planning/rules/design-reconciliation.md` once depended on a project-local personal-memory entry naming a gitignored `_design/*.jsx` convention. That was true when `phase-discovery.md` was written. It is no longer true — the root `README.md` confirms the rule now discovers a consuming project's design-artifact sources from project-supplied context instead of assuming any directory, filename, or tool, and states explicitly that the memory dependency is "Phase A history for `my-feature-planning`, not a current defect." Every historical finding cited below was checked against the current file before being classified as historical rather than current.

## 1. What skill authoring means

Skill authoring is more than editing prose. It includes:

- identifying the capability and its activation boundary;
- separating portable methodology from stack and project knowledge;
- deciding which file owns each contract;
- rewriting fused material where selective deletion would destroy the reusable intent;
- routing non-portable knowledge to the correct destination;
- classifying and authoring instruction-bearing supporting artifacts — templates, examples, tables, and checklists — with the same rigor as prose rules, since each can shape agent behavior or generated output even when it looks like presentation;
- verifying that a rule's stated conditionality survives every representation of it, not only its entrypoint statement — a content-block definition, table row, checklist item, or example can silently reimpose "mandatory" after the owning text already said "optional";
- reconciling callers, summaries, and downstream handoffs;
- validating the result as a cold reader or agent;
- retaining evidence without making history a runtime prerequisite.

Successful authoring is not measured by how much text was preserved or deleted. `my-git-workflow/SKILL.md` shrank from roughly 3,030 words at baseline to about 722 words today, for two distinct reasons: much reusable operational substance was routed into focused `rules/*.md` files rather than disappearing, and separately, project-specific, duplicated, stale, and incorrect material (Section 14) was deleted outright. `my-git-workflow/README.md` stayed roughly flat (about 2,609 to 2,912 words) across the same pass, because its job — orientation and reasoning, not operational contract — did not shrink. Neither number is the success criterion. The criterion is whether the resulting skill makes correct decisions without hidden project context: whether a reader or agent who has never seen the origin project can apply every rule correctly using only what is in the file.

## 2. Knowledge classification model

A passage in a skill or its supporting files may carry one or more of the following knowledge types — a single passage can fuse portable methodology, stack-specific answers, project convention, and historical evidence at once. Classify by concept, not only by paragraph or section: identify each concept a passage carries, classify each independently, and split or rewrite the passage when its fused concepts have different destinations.

**Portable methodology** — decision rules, invariants, gates, evidence standards, ownership boundaries, and workflows reusable across consuming projects. Example: `my-git-workflow`'s two-gate review model (implementation review, then commit-plan review) and the "never assume one issue equals one commit" invariant.

**Reusable stack/ecosystem knowledge** — framework, runtime, ORM, frontend, testing, tooling, or platform conventions reusable across projects on the same stack. Concrete artifact types, framework lifecycle behavior, or stack-native commands may belong here, but only when evidence shows they are reusable across projects on that stack rather than one project's local convention. A stack skill or reference is a candidate destination for this category; this document does not create one.

**Stable project-specific knowledge** — durable project rules, product conventions, domain vocabulary, repository policies, metadata conventions, or integration expectations shared by the project. Example (historical, now resolved): a project's design-artifact directory convention.

**Initiative-specific approved decisions** — architecture, preserved behavior, product decisions, exclusions, and constraints that belong to one initiative rather than the project globally. These belong in an approved `plan.md`, not in a portable rule or a project-wide instruction file.

**Live or discoverable state** — facts whose authoritative value comes from current code, configuration, GitHub, a provider, or another external system. Example: a repository's label palette, or the state of a specific milestone. These should be queried, not frozen into instructions.

**Personal preference or continuity context** — user-specific preferences that improve collaboration but are not canonical project policy. Useful for how one person likes to work; wrong as the sole source of a rule other users or agents also need.

**Historical evidence** — origin-project cases and earlier defects that explain why a current rule exists but are not required to execute it. Example: the "Phase 22 — Authentication & 2FA" narrative (issues, a PR, a release) that `my-git-workflow`'s methodology was extracted from. That narrative was removed from the runtime skill files; it survives in the dossier and in Git history, not required by the runtime rule.

**Obsolete material** — incorrect, contradicted, duplicated, superseded, or purely incidental content. It is not relocated merely because it was removed. Example: an earlier draft of `my-git-workflow`'s milestone-closure rule required a second, redundant "are you sure" approval after authorization had already been given; the fix replaced the defect in place and needed no new home.

Do not present a historical finding as a current defect without checking the current file first — the design-reconciliation example above is the model case.

## 3. Knowledge destination model

| Knowledge type | Expected home |
|---|---|
| Portable decision methodology | Portable skill |
| Reusable stack convention | Stack skill or stack reference |
| Short, stable, always-applicable project instruction | Version-controlled `CLAUDE.md` or equivalent project instruction file |
| Detailed or conditional project knowledge | Project-local skill or version-controlled project reference routed from the project instruction file |
| Initiative-specific approved decision | Approved `plan.md` and resulting canonical work |
| Fact reliably discoverable from code/configuration | Code, configuration, schema, or tests |
| Changing GitHub/provider state | Query the live source when needed |
| Personal working preference | Personal memory |
| Historical evidence | Audit, dossier, or Git history |
| Obsolete/non-teaching material | No new destination; Git history is sufficient |

Explicit statements this table implies:

- Canonical project knowledge needed by teammates or cold-start agents should not live only in personal memory.
- Personal memory is useful for user preferences and conversational continuity, not as the sole source of project policy.
- `CLAUDE.md` is appropriate for concise, stable, broadly applicable project instructions.
- Substantial or conditional project knowledge should not bloat `CLAUDE.md`; route it to a version-controlled project-local skill or reference.
- Feature-specific approved decisions belong in `plan.md`, not global project instructions.
- Live state should be queried rather than copied into static instructions.
- Facts reliably discoverable from code should normally remain in code/configuration rather than being duplicated into agent prose.
- Sensitive data never belongs in a skill, audit, project instruction, or personal-memory substitute.

This table names candidate homes; it does not resolve which one a specific consuming project should use for a specific fact. Section 15 records the selection criteria without deciding a final architecture.

## 4. Knowledge-disposition ledger

Use this ledger during portability and authoring work. It classifies concepts, not every deleted sentence or identifier.

| Field | Meaning |
|---|---|
| Source | Original file and resolved baseline commit |
| Removed concept | The knowledge carried by the original passage |
| Classification | Portable, stack, project, initiative, live state, personal, historical, or obsolete |
| Surviving lesson | Reusable reasoning preserved from it, if any |
| Destination | Portable skill, stack layer, project guidance, `plan.md`, runtime discovery, audit, or nowhere |
| Status | Retained, generalized, rewritten, deferred, extracted, or intentionally discarded |
| Evidence | Why this disposition is justified |
| Confidence/open question | Whether another project or authoring pass must validate it |

The ledger exists to prevent two opposite failures at once: losing reusable stack or project knowledge during generalization by deleting it outright, and dumping every removed example into a new project-specific file without proving it deserves preservation. Section 14 applies this ledger, grouped by concept, to the first two completed passes (`my-git-workflow` and `my-feature-planning`); `my-architecture-laboratory`'s architecture-specific disposition is retained instead in `skill-audits/my-architecture-laboratory.md`, not added to the register here.

## 5. Evidence-to-rule graduation

- Do not create speculative rules for imagined failures.
- Prefer evidence from real use, demonstrated ambiguity, a concrete failure, or a decision the existing instructions refused to resolve.
- One project-specific fact is not automatically portable methodology.
- Repeated evidence may justify promotion, but repetition alone does not prove policy — repetition confined to one project is still one project's evidence.
- A rule must change decisions or materially improve correctness.
- A fact an agent can reliably discover from authoritative code or configuration usually does not need a duplicated rule.
- Replace an obsolete rule rather than adding nearby qualifications and exceptions.
- Keep historical evidence outside runtime instructions unless a compact example materially teaches the rule.
- Ask whether an observed lesson is portable methodology, reusable stack knowledge, stable project policy, live state, historical evidence, or obsolete material.
- A rule should graduate only into the narrowest layer supported by evidence. `my-git-workflow`'s now-deleted portability audit (historical evidence at `503e638bb926a7f437838cc0eb50f9ffbf59c766:skill-audits/my-git-workflow-portability.md`) declined a skill-wide mechanical restructuring on exactly this basis: "the evidence does not justify a skill-wide mechanical restructuring... Retrofitting headings onto files that don't currently have a boxing problem would add ceremony without fixing anything."

This is not "never create a rule until a failure occurs." That is too strong. The precise principle is proportionate evidence, not imagination: a high-risk invariant may justify explicit instruction before a failure occurs, when the risk and the reasoning behind it are concrete rather than speculative. `my-git-workflow` shows both sides of this line in the same rule set. Its dependency-order-versus-activation-order precedence question has never actually conflicted in observed use, and no precedence rule was invented for that unencountered case — the dossier records this as "an observed non-conflict, not a claim that they never can," with the standing escalation path in `review-gates.md`'s "when to stop and ask" as the deliberate fallback rather than a gap. That is evidence withheld correctly. By contrast, its milestone-completion rule was adopted on a single explicit human decision, not repeated observation, and is still current policy — because the risk of silent, unauthorized closure was concrete enough to warrant a rule immediately, while the dossier still flags that decision as "an intentional design choice that may or may not fit a different project's own constraints," not proven-universal. Distinguish "this rule is current and authoritative" from "this rule is validated as portable" — the two are not the same claim, and a rule adopted on one explicit decision should be marked with the weaker claim until repeated evidence, ideally from more than one consuming project, supports the stronger one.

## 6. Authoring workflow

1. Establish the current authoritative baseline (resolve it from Git history; do not assume a commit).
2. Read the skill completely, including callers and downstream consumers.
3. Map ownership before editing prose.
4. Classify the current passages by knowledge type (Section 2).
5. Identify the portable intent beneath project evidence.
6. Decide whether to retain, generalize, rewrite, route, or discard each concept.
7. Rewrite the owning contract.
8. Reconcile `SKILL.md`, `README.md`, cross-references, and downstream summaries.
9. Perform cold-read behavioral checks — can a reader with no origin-project history apply the rule correctly using only the file?
10. Record dispositions and authoring observations.
11. Commit only after full re-read and scope verification.

This sequence describes responsibilities, not mandatory section headings or a fixed number of subprocesses. A given pass may fold several steps into one commit or split one step across several, depending on how fused the source material is.

Step 9's cold-read check is necessary but not sufficient for executable supporting material — a template's embedded script, a generated command, or any other runtime logic. Also trace the real production entry or discovery path (the actual selector, call site, or invocation the runtime uses) rather than validating only by invoking an internal helper directly with a hand-picked input; a helper can be provably correct in isolation while the path that actually reaches it in production silently excludes the exact case it was written to handle.

## 7. General authoring principles from feature classification

- Classify by product or system responsibility, not framework artifacts.
- Persistence does not automatically determine conceptual shape.
- Work origin does not predict downstream classification.
- Extensions route according to the affected slice without replanning the whole parent.
- Generic examples can teach a taxonomy without requiring project archaeology.

Distinguish the skill-specific rule from the authoring lesson. "Persistence does not automatically make something resource-shaped" is `my-feature-planning/rules/feature-classification.md`'s own classification rule — it governs whether owning database tables puts a feature in shape B (capability) or shape A (resource). The broader authoring lesson, applicable beyond that one skill, is to define categories by their organizing responsibility rather than by incidental implementation artifacts. The same discipline applies to "work origin does not predict downstream classification": inside `my-feature-planning` this is the rule that a feature discovered mid-implementation classifies by what it is, not by how it was found; as an authoring lesson it says a passage's provenance (where in the codebase or process it came from) should not bias how a skill categorizes it.

Two items once tracked as gaps are now resolved, and are recorded here only as historical evidence for why origin and classification must stay independent: `my-feature-planning/rules/capability-checklist.md` now handles capability-shaped (and capability-shaped-extension) work directly, through its own thirteen-question contract; `my-feature-planning/rules/discovered-work.md` no longer carries a "usually C or D" classification bias for discovered work — a direct search of the current file confirms no such language remains. Neither is a current TODO.

## 8. General authoring principles from the resource checklist

- A portable structure can require a full textual rewrite when project answers are fused into every sentence.
- Portable checklists ask consuming projects for their conventions and evidence; they do not contain one project's answers.
- Scope questions should describe outcomes, responsibilities, and invariants rather than framework artifacts.
- Checklist bullets do not imply one issue per bullet.
- Conditional downstream rules become mandatory once their activation condition holds.
- Exact tooling commands belong to stack or project guidance when the portable methodology only needs to identify the integration category.

`my-feature-planning/rules/resource-feature-checklist.md`'s Track F is the concrete case behind the first bullet. `phase-discovery.md` found no generic sentence to extract from its original text — the project-specific content (badge-tone palette, mobile/desktop header rules, drop-menu ordering) was the entire content of most of the track. A generic version had to be authored from the intent behind that evidence ("plan a responsive header breakpoint," "establish a fixed status-tone palette and reuse it"), not lifted from already-reusable prose by deleting the project-specific parts. Track F now reads as outcome-shaped questions under the heading "User-facing surfaces and UX consistency." `capability-checklist.md`'s extension-seam question is the concrete case behind the fifth bullet: seam-checking is skipped unless one of three named trigger conditions holds, and becomes mandatory — not optional — once one does.

Generalize these carefully. `resource-feature-checklist.md` is one example that demonstrates the rewrite-from-intent principle clearly; it is not a prerequisite for understanding the authoring method described elsewhere in this document.

## 9. Conceptual-modeling principles

- Authority overlays should not be modeled as peer outcomes.
- Evidence classification and workflow readiness are separate decisions.
- Semantic disposition and scopeability are separate decisions.
- Canonical-scope membership and dependency-edge creation are separate decisions.
- Planning order and live implementation readiness are separate decisions.
- Material product/architecture decisions and open implementation details are separate decisions. Materiality is a function of architectural consequence — would flipping the choice change approved behavior, a guarantee, a security boundary, ownership, lifecycle, or the target architecture — never a predefined list of choice types; a column type, a class, a CLI flag, or a UI treatment can each be material or not, depending on consequence, not category.
- Canonical structure, rendered artifacts, and live external state require distinct validation.
- Explicitly state where a special path converges back into the ordinary workflow, rather than leaving the reader to infer it.
- Model ownership before designing cross-references.
- Route to the owning contract rather than duplicating it. A cross-reference stays accurate as the owning rule evolves; a restatement drifts. `my-feature-planning/rules/issue-conventions.md` routes milestone lifecycle and closure entirely to `my-git-workflow/rules/milestone-completion.md`'s current contract rather than restating it — a deliberate boundary reconciled across both skills.

Many authoring defects come from collapsing two related but distinct decisions into one outcome list, one gate, or one overloaded paragraph. `my-git-workflow`'s corrected milestone-closure defect is one instance: an earlier draft folded "has authorization been given" and "should the milestone be closed" into two separate approvals asking the same question, when they were really one decision. The fix removed the duplicate rather than adding a qualifier to either gate.

## 10. Runtime files and supporting files

- `SKILL.md` owns activation, core scope, essential invariants, routing, and major handoffs — not downstream mechanics or stack vocabulary, even incidentally.
- Rule/reference files own substantial conditional or mode-specific mechanics.
- `README.md` explains the lifecycle and reasoning without becoming an operational duplicate.
- Runtime skill instructions (`SKILL.md` and rule/reference files) hold the current operational contract, not a changelog.
- Current dossiers preserve current architecture, rationale, and evidence-backed assessment, kept up to date as the skill changes.
- Git history and historical audit evidence preserve chronology, exact removed prose, and earlier repository states — a record of what changed and when, not maintained to stay current.
- Project instruction files supply durable project context.
- Code/configuration/live systems remain authoritative for discoverable state.

Progressive disclosure:

- keep the always-loaded entrypoint as short as the complete activation contract allows;
- move substantial conditional guidance into routed references;
- do not create extra files or routing layers without a real conditional need;
- do not force every skill into the same folder or heading structure — `my-git-workflow`'s seven rule files and `my-feature-planning`'s nine both remained conceptually cohesive by letting each file's structure follow what it explains, not a shared template.

## 11. Concision

- Avoid artificial minimum word counts.
- A lower bound invites padding and preserves duplication.
- Use a soft ceiling only when it helps constrain drift.
- The correct length is the shortest complete expression of the contract.
- Added text is justified when it resolves a real ambiguity, protects an invariant, or preserves a necessary distinction.
- Shorter is not automatically better when deletion collapses distinct decisions.
- Longer is not automatically more complete.
- An instruction such as "open by distinguishing X from Y" is guidance to the author, not necessarily literal target prose.
- Never hard-wrap inside an inline code span.
- Replace obsolete policy instead of accumulating qualifications around it.

`my-git-workflow/SKILL.md`'s drop from roughly 3,030 to about 722 words — routing plus outright deletion, not routing alone (Section 1) — against `README.md`'s roughly flat word count across the same pass, is the concrete evidence against a uniform target: the right length differs by what a file's own contract requires, not by a shared ratio applied to every file in a skill. This document does not impose one-paragraph-per-physical-line as a universal rule.

## 12. Controlled technical English

> Write normative skill instructions in controlled technical English. Prefer active voice, direct subjects and actions, one stable term for each defined concept, and one operational instruction per sentence when practical. Split complex conditions, exceptions, and consequences into structured clauses or bullets. Preserve exact identifiers, paths, commands, quotations, and externally defined names. Do not sacrifice necessary authority, exceptions, or technical meaning merely to shorten a sentence.

- This is controlled technical English informed by Simplified Technical English, not ASD-STE100 compliance. Strict ASD-STE100 is a formal controlled language with its own approved vocabulary and grammar — not a synonym for clear writing — and nothing here or in the underlying dossiers claims to satisfy it.
- Do not use synonyms merely for stylistic variety in normative rules.
- Runtime instructions should be controlled and precise.
- READMEs, audits, and dossiers may use more natural explanatory prose.
- Do not mechanically ban every contraction.
- Do not force one instruction into one sentence when splitting it would obscure necessary conditions or authority.
- Do not force one paragraph onto one physical line.
- Do not force identical structure across unrelated rule files.
- Do not rewrite a correct skill merely to make it appear more STE-like.

Official standard, linked exactly once: [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).

Three distinct categories, not one indivisible standard:

1. **Controlled-language conventions** — the sentence- and term-level discipline above.
2. **Markdown/diff-formatting conventions** — inline-code-span wrapping, table formatting, heading structure. Formatting hygiene, unrelated to sentence-level word choice.
3. **Rule-governance philosophy** — how a rule earns its place (Section 5), where it lives (Sections 3, 10), and how it stays reconciled with its callers (Section 13). Governance, unrelated to prose style.

## 13. Cross-file reconciliation

- Changing an owning rule may make its callers, indexes, READMEs, and downstream summaries stale.
- After changing an owning contract, inspect every direct consumer.
- Correct stale references and summaries in the same coherent pass when scope permits.
- Do not duplicate the corrected procedure into every consumer.
- Cross-rule cohesion is behavioral consistency, not identical wording.
- Cold-read scenarios are useful when they test whether one decision routes to exactly one owner.
- Validation should test meaningful behavior and invariants, not merely match expected phrases or headings.
- A direct consumer of a changed contract can live entirely outside the skill being authored. Check cross-skill consumers explicitly; re-reading only the file just changed is not sufficient.

All three completed passes needed a dedicated reconciliation step, not just per-rule rewrites. `my-feature-planning`'s cross-rule cohesion commit existed because `SKILL.md`, `README.md`, and one rule file still described sequencing, plan-input scope, and the handoff boundary the way they worked before the individual rule rewrites had already changed the underlying contract. `my-git-workflow`'s now-deleted portability audit (historical evidence at `503e638bb926a7f437838cc0eb50f9ffbf59c766:skill-audits/my-git-workflow-portability.md`) found the reverse failure mode: three leaked project-specific terms (a stack formatter name, a fused milestone-naming example, an ambiguous "this project" phrase) survived three prior audit iterations because each pass re-read the skill through the lens of whichever file it had just touched, rather than re-auditing the whole skill fresh. `my-architecture-laboratory`'s pass adds a third failure mode neither predecessor exhibited: its corrected locked-vs-open materiality test lives in `my-architecture-laboratory/rules/plan-synthesis.md`, but a narrower restatement of that same test survived, uncorrected, inside `my-feature-planning/rules/plan-md-input.md` — a rule file in a different skill entirely, found only by reading that consumer directly rather than by re-reading the file that had just been fixed. Together these show reconciliation is its own required pass — not an automatic byproduct of rewriting the owning file, not safe to scope to only the file last touched, and not safe to scope to only the skill being authored.

## 14. Evidence-backed disposition register

Representative removed content from the first two completed passes (`my-git-workflow` and `my-feature-planning`), grouped by concept rather than by identifier. `my-architecture-laboratory`'s architecture-specific disposition is retained instead in `skill-audits/my-architecture-laboratory.md`, not folded into this register.

| Group | Original knowledge type | Portable lesson retained | Destination / non-destination | Stack or project extraction still justified? |
|---|---|---|---|---|
| Framework artifact vocabulary (Laravel/PHP implementation-skill list in `SKILL.md`; "Pint"; `gatherMiddleware()`; Pest commands and `skipUnlessFortifyHas()` in `verification.md`; `useOrbit` design-system vocabulary in Track F) | Stack | Verification and formatting have a scope even when the specific tool is unnamed; a rule can name the integration category without naming the tool | Removed from the current runtime skill files entirely — a direct scan of `my-git-workflow/`'s current Markdown confirms the Laravel/PHP/Pest terms are absent, and a direct scan of `my-feature-planning/`, particularly `rules/resource-feature-checklist.md` Track F, confirms the former `useOrbit` design-system vocabulary is absent as well. Generic portable concepts Track F retains in its place — responsive behavior, design-system consistency, and a status-tone palette category — are not leakage. The removed terms survive only in this repository's audits/dossiers and Git history | Not decided here — a stack skill would need its own evidence that these are reusable across Laravel/Pest projects generally, not incidental to one project's setup |
| Origin-project domain names and issue/phase histories (`#288`/`#287`/`#120`/`#289`, PR `#298`, `v0.17.0`, "Phase 22 — Authentication & 2FA"; `useOrbit` model/column names) | Historical / project | The extraction happened; a worked example can teach message and evidence shape | Removed from the current runtime skill files entirely, including from `commit-boundaries.md` and `release.md`, which now use generic, non-attributed examples instead. Survives only in this repository's audits/dossiers and Git history | No — this is origin-project history, not reusable knowledge |
| Private-memory dependencies (`design-reconciliation.md`'s `project-design-files` memory reference; an earlier `issue-conventions.md` label-palette memory duplicate) | Project (mistakenly treated as portable) | A portable rule must not silently degrade for a reader with no matching memory entry | Rewritten to discover the relevant fact from project-supplied context instead of assuming a memory entry exists | No — the fix was making the rule memory-independent, not relocating the dependency |
| Hard-coded design-file conventions (`_design/*.jsx`, a gitignored directory convention) | Project-specific | A design-artifact source is worth locating; its literal path is not | No runtime home in the portable skill; a project needing this convention documents it in its own project instruction file or reference | Possibly, at the project layer only, if a specific project actually uses that convention |
| Live label-palette state (a Tailwind hue-rotation palette, including "the next hue to assign is rose") | Live/discoverable state | Label color assignment needs a rule; the current palette does not | Query the live source (GitHub) when needed; not copied into static instructions | No — this is state, not knowledge |
| Project milestone naming pattern (a literal `Phase NN — {Feature Name}` syntax), previously fused with assignment defaults into one general definition | Project-specific | A milestone-completion test can be stated generally without requiring a specific naming syntax; the portable skill retains only the rule to classify a milestone's purpose and propose metadata, not an assumed pattern | Not present in current runtime files. If still approved and durable for a given project, it belongs in that project's own instructions; if obsolete, it belongs only in history | No — one project's naming convention, and not a current one |
| Assignment defaults (a self-assignment default, `@me`), previously fused into the same passage | Project- or user-specific metadata, mistakenly treated as portable default behavior | A portable skill must not silently assign anyone; assignment must come from user instruction or explicit metadata approval, unless a durable assignment policy is itself recorded in project-owned instructions | `@me` is not present in current runtime files and is not restored as a current convention; survives only as historical evidence | No — an incorrect generalization of one project's or one user's default, not knowledge to relocate |
| Fixed backend/frontend or TDD batching (an earlier default that sequenced "backend/TDD work batched before frontend/UI work") | Project-specific pattern, mistakenly generalized as default | Real dependency-graph decomposition should decide sequencing, not a fixed batch shape | Replaced outright in `sequencing.md`; the old template survives only as dossier evidence for why it was wrong | No — this was an incorrect generalization, not knowledge to relocate |
| Provider/tool-specific commands (`gh` commands; `php artisan test --compact`; `vendor/bin/pint --dirty --format agent`) | Mixed: `gh` is the mechanism for a GitHub-issue-centric skill; the Laravel commands are stack-specific | `gh` commands are correct to state literally because the skill's whole premise is a GitHub issue, not an example of one mechanism among several; the Laravel commands are not | `gh` commands remain intentionally present where the runtime skill performs GitHub operations, because GitHub is an explicit substrate of `my-git-workflow`. The Laravel commands are absent from the current runtime files entirely and survive only as historical evidence in audits/dossiers and Git history | For the Laravel commands, only at a stack layer with its own supporting evidence |
| Stale cross-rule summaries (pre-cohesion-pass `SKILL.md`/`README.md`/rule descriptions of sequencing and plan-input scope, out of date after the owning rules changed) | Obsolete | Reconciliation must be its own pass, not assumed automatic | Corrected in place during the cohesion pass; no relocation needed | No |
| Inaccurate or contradicted claims (a redundant second milestone-closure approval; an earlier "usually C or D" classification bias in `discovered-work.md`) | Obsolete | The correction itself (remove the duplicate; remove the bias) is the lasting artifact | Fixed in place; Git history is sufficient record | No |

Do not assume every framework term removed from a portable skill belongs automatically in a stack skill — extraction requires its own evidence that the knowledge is a reusable stack convention, not incidental vocabulary from one project's setup. Do not assume every project-specific example belongs in a project instruction file — many are historical evidence or obsolete state and need no runtime home at all.

## 15. Project-specific storage decision criteria

**`CLAUDE.md`** — short, stable, broadly applicable, team-visible instructions that should affect most agent sessions.

**Project-local skill or reference** — substantial, structured, or conditional project/domain knowledge that should load only for relevant tasks.

**`plan.md`** — approved initiative-specific architecture and product decisions.

**Code/configuration/tests** — authoritative discoverable facts and enforceable invariants.

**Runtime query** — changing GitHub/provider/repository state.

**Personal memory** — user-specific preferences and continuity, never the sole canonical source of a project rule needed by other users or agents.

The final project-knowledge storage architecture for any specific consuming project — including this repository's own eventual `useOrbit`-facing decisions — remains an explicit later choice. This document records the criteria for choosing among these homes; it does not choose one.

## 16. Graduation into `skill-creator`

During this authoring pass, a `skill-creator` skill (Anthropic's official plugin) installed locally was inspected read-only, without editing it. No exact version or commit was recorded during that inspection, and none is invented here; every observation below describes only the inspected version, not a timeless fact about `skill-creator`'s current state — its installation and behavior must be rechecked before eventual integration. At that version, it was an eval/iteration-loop tool — capture intent, draft, write test prompts, run with-skill and baseline subagents, grade, benchmark, iterate on the triggering description, package — not an authoring-methodology document. It already used progressive disclosure and already had a `references/` directory, which is the natural extension point below. It had no knowledge-classification model, no disposition ledger, and no controlled-technical-English guidance; its own writing-style guidance favored persuasive, explanatory description text and explicitly warned against heavy-handed all-caps `MUST`/`NEVER` language, targeting triggering descriptions and behavioral nudges rather than normative rule-file prose — so it did not conflict with Section 12, but also did not already embody it.

The complete audit document — this file, and the three skill dossiers — should not be copied into `skill-creator`. Now that a third proving pass exists (see the status block above):

- keep `skill-creator/SKILL.md` concise;
- place substantial methodology in a routed reference such as `references/authoring-methodology.md`;
- promote only principles that materially change authoring decisions;
- exclude historical project evidence from the runtime reference;
- exclude skill-specific classification rules unless generalized and independently supported;
- preserve the knowledge-disposition model;
- preserve controlled technical English as guidance, not a compliance gate;
- use progressive disclosure;
- forward-test the resulting creator guidance on realistic authoring work before treating it as stable.

Graduation criteria — a principle graduates only when it is:

- supported by repeated real authoring evidence;
- reusable outside its origin skill;
- changing decisions or preventing a demonstrated ambiguity;
- properly a concern of skill creation rather than an operational skill;
- not a duplicate of a contract already owned elsewhere;
- statable without origin-project context;
- survived a cold-read or forward-use validation;
- placed at the narrowest appropriate disclosure layer.

Candidate principles, reassessed individually now that a third pass (`my-architecture-laboratory`) exists:

- The two-tier confidence model distinguishing rules grounded in repeated observation from rules grounded in one explicit human decision (Section 5) is not exercised by this pass's evidence. Its status is unchanged — still resting on `my-git-workflow`'s single case — and it still needs its own proving pass before graduation.
- The "separate X from Y" conceptual-modeling checklist (Section 9) is strengthened, not graduated: `my-architecture-laboratory` independently produced its own instance of the pattern — two gates ("decisions approved before synthesis" and "the document approved after synthesis") collapsed into one at a document's point of first mention, found and corrected the same way Section 13's cross-skill example was. It is now supported by two skills' authoring evidence rather than one, but still short of the "more than one consuming project" bar Section 5 sets for the strongest claim, since both instances arose inside the same repository's authoring program.
- The claim that concision has no useful lower bound at all (Section 11) is strengthened: `my-architecture-laboratory`'s `rules/` files moved by different amounts and in different directions under the identical discipline — `doc-style.md` shrank by about 18%, `review.md` grew by about 6%, and `plan-synthesis.md` stayed within 2% of its baseline; its own `README.md`, held to the same discipline, shrank by about 24% — directly against a uniform target. Now supported by three skills' worth of evidence rather than two.

Neither strengthened claim is declared universal by this reassessment; both remain working conclusions pending evidence from an actual, separate consuming project rather than another pass inside this same repository.
