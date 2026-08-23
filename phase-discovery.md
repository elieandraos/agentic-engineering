# Phase C — Discovery: Classifying the Mature Custom Skill Ecosystem

**Status:** Phase C discovery pass, first iteration. This document is evidence and classification
only — no skill, memory file, or `useOrbit` file was modified to produce it. See `roadmap.md`,
Phase C, for the objective and constraints this pass operates under.

**Snapshot analyzed:**
- `agentic-engineering` @ `c900785272b4a13b844043cae2e55f2cb911055c` (`main`, clean working tree)
- `useOrbit` @ `e95bf86ad101f56fb32ef8831da1d2af9b63ea67` (clean working tree)
- Personal Claude Code project memory for `useOrbit`
  (`~/.claude/projects/-Users-elieandraos-Desktop-Code-useOrbit/memory/`)

**How to read this document.** Every claim below is tagged as one of:
- **Fact** — directly observed in a file, verifiable by re-reading the cited path.
- **Decision** — an explicit choice already recorded in `agentic-engineering/roadmap.md` or
  `README.md`.
- **Inference** — a conclusion drawn from combining facts, not itself directly stated anywhere.
- **Judgment** — a classification call this pass is making, where a reasonable person could place
  the evidence differently.
- **Open question** — a case this pass deliberately does not resolve.

Per Phase C's own rule, this document classifies; it does not restructure, rename, move, or merge
anything.

---

## 1. Inventory

### 1.1 `agentic-engineering` (the canonical portable core)

**Fact.** Three skills exist, each with `SKILL.md` + `README.md` + `rules/` or `references/`:
`my-feature-planning` (9 rule files), `my-git-workflow` (7 rule files), `my-architecture-laboratory`
(4 reference files + `template.html`). All three are byte-identical to the copies consumed into
`useOrbit/.claude/skills/` at upstream commit `12d9c1df75dde5fb1d944b62b0679c1e211137a4`
(verified: `diff -rq` between both trees produced no output; provenance recorded in
`useOrbit/.claude/skills/UPSTREAM_PROVENANCE.md`).

**Fact.** A repo-wide grep for `useOrbit|Orbit` (case-insensitive, `.md`/`.html`) across all three
skills returns zero matches — no literal project reference survives in their operative content.

### 1.2 `useOrbit/.claude/skills/` (the full local ecosystem, 15 skill directories)

**Fact**, cross-referenced against `useOrbit/boost.json`'s `"skills"` array and mirrored in
`useOrbit/.junie/skills/` (JetBrains Junie's copy of the same Boost distribution — corroborating
that these are IDE-agnostic, framework-vendor-distributed skills, not Claude-Code- or
`useOrbit`-authored):

| Skill | Source |
|---|---|
| `infer-conventions`, `fortify-development`, `laravel-best-practices`, `wayfinder-development`, `pest-testing`, `inertia-vue-development`, `echo-vue-development`, `echo-development`, `tailwindcss-development` | **Laravel Boost** (external first-party; listed verbatim in `boost.json`) |
| `my-architecture-laboratory`, `my-feature-planning`, `my-git-workflow` | **Canonical snapshots** from `agentic-engineering` (Phase B consumption) |
| `my-laravel-patterns`, `my-phpstorm-conventions` | **Genuinely owned custom stack skills**, `useOrbit`-local only, no `agentic-engineering` counterpart yet |
| `content-backlog` | **Genuinely owned custom skill**, not `my-`-prefixed, not in `boost.json` — see §1.4 and the open question in §8.1 |

This confirms the task's named five (`my-feature-planning`, `my-git-workflow`,
`my-architecture-laboratory`, `my-laravel-patterns`, `my-phpstorm-conventions`) as the complete
`my-*`-prefixed set, and surfaces **`content-backlog` as a sixth genuinely-owned mature custom
skill** the task instructed this pass to look for but did not name.

**Fact.** `useOrbit/.claude/_rollback/pre-phase-b-skills/` holds the pre-Phase-A,
independently-authored originals (including the pre-rename `architecture-laboratory`) — retired
rollback material, outside active skill discovery, not analyzed further here since Phase B already
diffed them against upstream and found only the documented rename/placeholder edits.

### 1.3 `useOrbit` project memory (personal, not in the `useOrbit` git repo)

**Fact.** 17 memory files exist at
`~/.claude/projects/-Users-elieandraos-Desktop-Code-useOrbit/memory/`: one `type: project`
(`project_design_files.md`), sixteen `type: feedback`. Several are referenced **by name, inline**
from inside nominally-portable `agentic-engineering` skill files (see §6c) — meaning the canonical
skills already carry a live content dependency on `useOrbit`-local personal memory, not just an
illustrative example.

### 1.4 Other durable `useOrbit` evidence

**Fact.**
- `useOrbit/CLAUDE.md` and `useOrbit/AGENTS.md` are byte-identical, Boost-generated
  (`<laravel-boost-guidelines>`), and document the `.ai/rules` + `record-rule` MCP mechanism as the
  intended home for durable, team-shared project rules. **`useOrbit/.ai/` does not exist** — this
  mechanism is not yet in use; today's durable-rule needs are served instead by personal memory
  (§1.3) and the custom `my-*` skills.
- `useOrbit/_docs/Multi-tenancy.md` — durable product/business-domain reference (Organization
  tenancy model, pivot-derived ownership, roles/statuses).
- `useOrbit/_docs/breadcrumbs.md` — repo-specific frontend implementation note, including a
  documented outstanding bug (breadcrumbs prop wired but not rendered).
- `useOrbit/_docs/skills.md` — an informal, `useOrbit`-local note (not referenced anywhere in
  `agentic-engineering`) describing a prior intent to publish `my-laravel-patterns` and
  `my-phpstorm-conventions` together via `skills.sh` under one `"Laravel"` grouping. **Evidence of
  prior user intent, not a locked decision** — relevant to §7.
- `useOrbit/_design/*.jsx` — 20+ gitignored Claude Design mockup files, referenced by
  `my-feature-planning/rules/design-reconciliation.md`.
- `useOrbit/plan.md` — exists at repo root, **currently empty (0 bytes)**. No active Plan Synthesis
  output exists at the time of this pass.
- `useOrbit/content-backlog.md` — a real, tracked, ~96 KB file with 22 indexed entries, actively
  used (not a stub). Several entries are explicitly *about* the `agentic-engineering`
  methodology-development process itself (e.g. entry 9: "I wrote the plan to make my own skills
  public — and the first decision was 'not yet'"; entry 1 references the pre-rename
  `architecture-laboratory`, a stale name).
- `useOrbit/.mcp.json` — `laravel-boost` (`php artisan boost:mcp`) and `claude_design` MCP servers;
  the latter backs `my-architecture-laboratory`'s Artifact-publishing workflow and is an external
  Anthropic capability, not Laravel-specific.

---

## 2. Portable methodology

**Fact**, based on a full read of every `SKILL.md`/`rules/`/`references/` file in all three
canonical skills, cross-checked with a repo-wide grep for `Laravel|Vue|PHP|Inertia|Eloquent|Pest`:

### `my-architecture-laboratory` — the cleanest of the three
Every operative file (`SKILL.md`, `doc-style.md`, `maintenance.md`, `plan-synthesis.md`,
`review.md`) is stack- and project-agnostic: the four-phase Explore → Recap → Guide → Maintain
discipline, the "codebase tells us what exists, the human decides what it should become"
principle, the locked/current-state/derived/open-decision taxonomy in Plan Synthesis, and the
review checklist's "does this explain the architecture" philosophy contain no Laravel/Vue/PHP
content and no `useOrbit` product reference. The one `Laravel|Vue|PHP` grep hit inside this skill's
own operative files is `references/plan-synthesis.md:128`'s generic `path/to/File.php:method`
placeholder syntax, not stack-specific guidance.

**Open question (see §8.6):** `my-architecture-laboratory/README.md` (lines ~182–195) contains a
self-assessment — *"The skill as it's actually written today is not that generic yet. It assumes
things specific to this project: this project's Laravel/Vue stack..."* — that appears **stale**
against this pass's own finding of zero such content in the operative files. Recorded as an
inconsistency, not resolved here.

### `my-feature-planning` — portable workflow skeleton, mixed at the checklist layer
Portable: the Planned-vs-Discovered work-origin model (`SKILL.md`); the entire
`discovered-work.md` investigation-depth/checkpoint/stopping-condition framework (Shallow/Focused/
Deep bands, the falsification-and-checkpoint mechanism); the four-shape feature-classification
taxonomy (`feature-classification.md`); the "GitHub issues must stand alone" principle and its
reference-syntax rules (`issue-conventions.md`); the Context-before-Tasks issue-body shape; the
three-tier validation model — canonical structural integrity / rendered manifest integrity /
issue-body content integrity (`review.md`); the propose-then-approve GitHub-metadata workflow
shape (as distinct from its `useOrbit`-specific instantiation, see §4). All worked examples in
these files cite real `useOrbit` issue numbers, but each file explicitly labels them as
illustration ("they illustrate the rules, they don't define them" — `SKILL.md:8`).

**Judgment.** `resource-feature-checklist.md`'s Track A–G *skeleton* (core infra, status lifecycle,
sub-resource, filters/sorting, export, frontend UX consistency, wiring gotchas) is portable — the
file states this explicitly ("every resource-shaped feature in any codebase needs some answer to
each of these," line 5) — but the file interleaves that skeleton with non-portable content; see §6b.

### `my-git-workflow` — portable by design, one embedding gap
Portable: the "issues describe outcomes, commits describe decisions" principle; the entire
commit-boundary reasoning in `commit-boundaries.md` (one-issue-≠-one-commit, file-count-≠-commit-
count, the "coherent, non-broken state" bar, no-fixup-commits discipline); the two-gate model in
`review-gates.md`; the ask-first + four-step recipe + post-mutation-validation pattern in
`issue-closure.md`; the dependency-ready recalculation in `sequencing.md`; the entire
policy-discovery-before-assumption methodology in `release.md` (which explicitly separates
*methodology* from a boxed **"What this repository's evidence shows"** subsection — the cleanest
methodology/adapter-fact separation anywhere in the ecosystem); the three-condition closure gate in
`milestone-completion.md`.

**Judgment (see §6a).** `verification.md` is the one file in this skill that does *not* follow
`release.md`'s labeled-separation pattern — its Laravel/Pest/Pint commands are woven directly into
general methodology prose rather than boxed as a discovered adapter fact.

---

## 3. Custom stack/ecosystem knowledge

**Fact**, based on a full read of both skills' `SKILL.md` and every `rules/` file:

### `my-laravel-patterns` — genuinely reusable Laravel/Inertia authoring philosophy
Every rule file (`actions-pattern.md`, `authorization.md`, `eloquent-attributes.md`,
`filters-pattern.md`, `enum-options.md`, `request-normalization.md`, `factories-and-seeders.md`,
`query-conditionals.md`, `resources.md`, `testing-strategy.md`) states a Laravel/Eloquent/Inertia
convention generically, using `useOrbit` model names (`Client`, `Carrier`, `Organization`) only as
illustration — not as the substance of the rule. Concretely: FormRequest+Action+thin-Controller
split, `#[Authorize]` attribute usage (never `$this->authorize()`), `#[Scope]` over
`scope`-prefixed methods, the `QueryFilter`/`Filterable` class-based filter pattern, backed-enum
`::all()` static-method convention, `prepareForValidation()`-owns-normalization discipline,
correlated/chronological factory-data realism, `when()` over `if` for query-builder chains, and a
four-layer test-ownership model (Action/Controller/Policy/Filter, no cross-layer duplication) — none
of these depend on `useOrbit`'s tenancy model, domain entities, or design system.

**Fact.** `SKILL.md:8` states an explicit, already-correct composition boundary with the Boost
skill it overlaps with: *"These take precedence over general Laravel best practices when there is a
conflict"* — paired with *"Always load ALONGSIDE... Never load as a replacement for"*
`laravel-best-practices`/`pest-testing`. No content duplication with `laravel-best-practices` was
found on inspection.

### `my-phpstorm-conventions` — genuinely reusable Laravel+PhpStorm+Pest tooling knowledge
Every rule file (`eloquent.md`, `pivot.md`, `phpdoc.md`, `pest.md`, `strings.md`, `inertia.md`)
documents a PhpStorm static-analysis false positive and its workaround, or a PhpStorm-aware coding
convention — Eloquent static-call/polymorphic-call narrowing, the IDE-helper-stub technique for
runtime-registered macros, `@throws`/`@property`/array-shape PHPDoc, `BelongsToMany` pivot typing,
Pest's chained-`->and()`/`@noinspection` suppression patterns, string-interpolation brace rules,
`inertia()` helper vs. `Route::inertia()`/`Inertia::render()`. **This is the single cleanest custom
skill in the entire ecosystem with respect to product-domain leakage** — every example uses
`useOrbit` model names purely as illustration of a generally-applicable IDE workaround; none of the
findings' validity depends on anything about `useOrbit`'s product.

### Partial: the generic portion of `resource-feature-checklist.md`
**Judgment.** The Track A–G skeleton itself (§2) and some of its instantiated content — e.g. "the
Actions pattern," "FormRequest normalization," the `wayfinder:generate --with-form` flag fact — are
genuinely reusable Laravel/Inertia-ecosystem knowledge, not `useOrbit`-specific. Other instantiated
content in the same tracks is not (§4, §6b).

### Corroborating evidence for a stack-layer pairing
**Fact.** `useOrbit/_docs/skills.md` (§1.4) is a prior, informal note proposing exactly
`my-laravel-patterns` + `my-phpstorm-conventions` as one `"Laravel"` `skills.sh` grouping — evidence
the user has already been thinking of these two as a coherent pair, independent of
`agentic-engineering`'s current three-skill roadmap. Not a locked decision (§7, §8.2).

---

## 4. `useOrbit`-specific knowledge

**Fact.**
- `_docs/Multi-tenancy.md` — the canonical Organization/tenancy/ownership/role-and-status model.
  Currently and correctly kept **outside** every skill.
- `_docs/breadcrumbs.md` — page-level breadcrumb data shape plus a documented, currently-unfixed
  bug. Repo implementation state, not methodology.
- Personal memory entries with no stack-generality, currently living only in memory, not in any
  skill: `feedback_github_issues.md` (no bracket-prefix titles, self-assign, ask for
  milestone/label), `feedback_github_label_colors.md` (the live Tailwind-hue rotation table with a
  "next hue to assign" pointer — genuinely stateful, unlike anything in a skill file),
  `project_design_files.md` (the `_design/` gitignore convention plus the `curl | tar` refresh
  command), `feedback_commit_workflow.md` (no `Co-Authored-By`, single-line commit messages, `refs
  #N` reference), `feedback_index_page_conventions.md` (no breadcrumbs on index pages, bordered
  header), `feedback_vue_page_structure.md` (show-page card-partial decomposition vs. single-level
  forms), `feedback_inertia_form_pattern.md` (`<Form>` over `useForm()`, hidden-input serialization
  pattern for custom components), `feedback_design_doc_snippets.md`, `feedback_no_tests_for_design_docs.md`,
  `feedback_no_browser_testing.md`.
- The `useOrbit`-instance content interleaved into `resource-feature-checklist.md`'s tracks: mirrors
  to specific files (`app/Models/Carrier.php`, `app/Policies/CarrierPolicy.php`,
  `BranchModal.vue`/`BranchesCard.vue`), the `organization_id`/Owner-role tenancy-gating convention,
  the badge-tone palette (`tone="success" dot"`, etc.), the mobile-vs-desktop index/show header
  layout rules, the breadcrumb rule (index: none, sub-pages: yes), and drop-menu ordering
  conventions. **Judgment:** these read as this product's own design-system/UI conventions, not
  Laravel/Vue-ecosystem-wide knowledge — a different Laravel/Inertia app would have its own
  equivalents, not these exact values (see the open question in §8.3 on where the boundary
  precisely falls).
- `design-reconciliation.md`'s four worked examples (Carrier `onboarded_date` drift, Notifications
  modal, Global Search plan.md-vs-mockup) — already correctly held as "examples from this project,"
  not the rule itself.
- `content-backlog.md`'s actual entries and the `content-backlog` skill's "Agentic in Public"
  positioning — personal-brand/authorial content tied to the user, not to `useOrbit`'s application
  domain, and not general engineering methodology either. See the open question in §8.1: this may
  not fit the three-layer model at all.

---

## 5. External dependencies

**Fact.**
- **Laravel Boost skill set** (`boost.json`'s `"skills"` array, confirmed installed and mirrored in
  `.junie/skills/`): `infer-conventions`, `fortify-development`, `laravel-best-practices`,
  `wayfinder-development`, `pest-testing`, `inertia-vue-development`, `echo-vue-development`,
  `echo-development`, `tailwindcss-development`. Upstream-maintained, refreshed by Boost tooling —
  not extraction material, per `roadmap.md` §4 and this pass's own observation.
- **Laravel Boost MCP server** (`.mcp.json` → `php artisan boost:mcp`) supplies `search-docs`,
  `database-query`, `database-schema`, `browser-logs`, `record-rule`, `get-absolute-url` — governed
  entirely by Boost's own injected `CLAUDE.md`/`AGENTS.md` guidelines, not by any custom skill.
- **`record-rule` / `.ai/rules`** — Boost's own intended mechanism for durable, team-shared project
  rules, documented in `CLAUDE.md` but **not yet exercised** in `useOrbit` (§1.4). This is a gap
  worth naming: today, durable rule-recording happens through personal memory and the custom `my-*`
  skills instead of through the mechanism Boost itself provides for exactly this purpose.
- **`claude_design` MCP server** — backs `my-architecture-laboratory`'s Artifact publishing and the
  `_design/*.jsx` pipeline. An external Anthropic capability, not Laravel-specific; already
  correctly treated as a tool dependency, not owned content.
- **Composition boundary already correctly stated** in both custom stack skills: `my-laravel-patterns`
  and `my-phpstorm-conventions` both explicitly instruct loading alongside `laravel-best-practices`
  and/or `pest-testing`, and neither restates or duplicates Boost content on inspection (§3).
- **`my-feature-planning`/`my-git-workflow`** both explicitly name Boost skills
  (`laravel-best-practices`, `pest-testing`) as implementation-time loads, distinct from the custom
  stack skills (`my-laravel-patterns`, `my-phpstorm-conventions`) — this distinction is already
  correctly drawn inline in both `SKILL.md` files and in `agentic-engineering/README.md`'s "Current
  portability status" section.

---

## 6. Mixed / misplaced / duplicated material

### (a) Portable methodology mixed with stack assumptions

**Fact.** `my-git-workflow/rules/verification.md`'s "Default loop" section states the targeted-
verification methodology using literal, unboxed commands: *"verify it with the tests actually
relevant to that commit's change (`php artisan test --compact <path>`) plus `vendor/bin/pint
--dirty --format agent`"* (lines 18–20), and again at lines 50–51 for the isolation technique.
Contrast with `rules/release.md`, which draws the same kind of stack/repo fact into an explicitly
labeled **"What this repository's evidence shows"** subsection (release.md lines 30–38, 107–119),
separated from the surrounding stack-agnostic methodology. `verification.md` has no equivalent
separation — the Laravel/Pest/Pint commands sit directly inside the general "targeted-then-full-
suite" methodology prose.

**Fact.** `my-feature-planning/rules/resource-feature-checklist.md` Track A embeds a `useOrbit`
routing fact inline with the generic track item: *"Routes file, `require`d from `web.php` inside
the standard `['auth', 'verified', 'organization']` group"* (line 20) — the middleware-group shape
is a `useOrbit` fact, stated as if it were part of the universal Track A recipe.

### (b) Stack knowledge mixed with `useOrbit` convention (heaviest concentration)

**Judgment.** `resource-feature-checklist.md` is the single most heavily mixed file in the
ecosystem. It braids three distinct kinds of content within the same tracks:
1. generic Laravel/Inertia recipe (Actions pattern, FormRequests, API Resources, `QueryFilter`/
   `Sortable`);
2. `useOrbit`'s actual file/class names as "mirrors" (`app/Models/Carrier.php`,
   `app/Policies/CarrierPolicy.php`, `BranchModal.vue`+`BranchesCard.vue`,
   `ClientsIndexHeader.vue`);
3. `useOrbit` product-design conventions that are arguably neither Laravel nor Vue/Inertia
   ecosystem knowledge at all (badge-tone palette, mobile/desktop header layout rules, breadcrumb
   rule, drop-menu ordering — see §4).

By contrast, `my-laravel-patterns` (§3) almost never does this: its rules state the pattern
generically and use `Client`/`Carrier` only as illustrative variable names, not as the rule's
substance. This is a meaningful, evidence-backed distinction between two files that both mention
the same model names.

### (c) Project-specific knowledge leaking into portable skills

**Fact.** `my-feature-planning/rules/issue-conventions.md`'s "Milestone rules" and "Label rules"
sections state `useOrbit`'s concrete conventions *as inline content*, not as a pointer: the
`Phase NN — {Feature Name}` milestone-naming convention (line 127) and the full Tailwind
vivid-hue-at-200-shade label-color rotation, including "the next hue to assign is `rose`" (lines
127, 158) — this is the same live-state fact independently held in memory's
`feedback_github_label_colors.md` (§6d). The file does self-label these with inline
*"This project's..."* call-outs (a good instinct), but the content itself is embedded rather than
referenced.

**Fact.** `my-feature-planning/rules/design-reconciliation.md:11` states: *"Per the
`project-design-files` memory: design files from Claude Design live at `_design/`..."* — a direct,
named content dependency from a nominally-portable skill onto a `useOrbit`-local personal-memory
entry. A different consumer of this skill from GitHub would have no such memory entry, and the rule
would silently degrade to "ask the user" only after failing to find `_design/`.

### (d) Duplicated knowledge between custom skills and project memory

**Fact.**
- `feedback_github_issues.md` (memory: no bracket prefixes, self-assign, ask for milestone/label)
  vs. `issue-conventions.md`'s "Assignee" and "No bracket prefixes" sections — the same two rules
  independently stated in both places. `issue-conventions.md:3` explicitly names the memory ("See
  also the `feedback_github_issues` memory... this file covers the feature-planning-specific format
  on top of it") — an acknowledged overlap, not eliminated.
- `feedback_github_label_colors.md` (memory — the live, evolving "next hue" pointer) vs.
  `issue-conventions.md`'s static restatement of the same scheme (§6c) — the memory is the actually
  up-to-date source of truth (it tracks state that changes with each new label); the skill's
  restatement has no live-state mechanism and can drift.
- `feedback_phpstorm_skill_activation.md` (memory — three documented recurrence incidents of the
  same missed-activation failure) vs. `my-phpstorm-conventions/SKILL.md`'s "How to Apply" section,
  which already encodes the fix (`getDiagnostics` before presenting any PHP file as finished). This
  is a **resolved, intentional convergence**, not a live problem: the memory itself states *"Recall
  of this memory alone has not been sufficient across three occurrences — treat the skill-file's own
  explicit step as the actual enforcement mechanism, not memory recall."*

### (e) Duplicated knowledge between custom skills

**Fact.** `my-laravel-patterns/rules/eloquent-attributes.md` documents the `#[Scope]` convention;
`my-phpstorm-conventions/rules/eloquent.md`'s "Attribute-Based Scope Not Resolved on Builder"
section restates the same underlying fact (the project uses `#[Scope]`, not `scopeXxx`) as context
for a different point (a PhpStorm false positive). **On inspection this is a linked, not blind,
duplication** — `eloquent.md:104` explicitly cites `my-laravel-patterns`' `rules/eloquent-
attributes.md` by name. Recorded as a duplication that is already correctly cross-referenced, not a
finding requiring action.

### (f) External-dependency composition — a positive existing boundary

Already covered in §5; recorded here per the task's checklist as a *clean* boundary, not a problem:
both custom stack skills explicitly state "load alongside, never replace," and no Boost content is
restated inside either.

### (g) Rules that may belong at a different layer

**Judgment.** `resource-feature-checklist.md` Track F's badge-tone/mobile-desktop-header rules
arguably belong closer to a `useOrbit` design-system reference (or `_docs/`) than inside a skill
whose other tracks are genuinely stack-generic (§4, §8.3).

**Fact — a soft, unresolved conflict.** `feedback_commit_workflow.md` (memory) states commit
messages must be *"a single descriptive sentence — no multi-sentence bodies, no lengthy
explanations."* `my-git-workflow/rules/commit-boundaries.md` (lines 59–63), independently derived
from real commit history (#288/#287/#120/#289), states *"Prefer a concise title and, when useful, a
short body describing the outcome and important guarantees or boundaries"* — permitting an optional
body the memory rule forbids. Not reconciled by either file; not resolved here (§8.5).

### (h) Implicit boundaries that already exist and appear coherent

Recorded so Phase D does not need to re-derive these:
- The three-skill family's own boundary (architecture → planning → git-workflow) is exceptionally
  clean: each skill's `SKILL.md`/`README.md` states what it does *not* own, and cross-references
  are directional with no overlap found on a full read of all three (§2).
- `my-laravel-patterns`'s explicit precedence-over-`laravel-best-practices` rule (§3) is a working
  composition model with no actual conflicting content found on inspection.
- `my-phpstorm-conventions` is the cleanest custom skill with respect to product-domain leakage —
  zero `useOrbit`-dependent findings (§3).
- `release.md`'s methodology/adapter-fact separation (§2, §6a) is the model the rest of the
  ecosystem can be evaluated against.

### (i) Possible over-fragmentation or over-coupling

**Fact.** `my-laravel-patterns` and `my-phpstorm-conventions` are, per both `SKILL.md` files' own
"How to Apply" sections, **always** loaded together with a Boost base skill — no trigger condition
in either file calls for one without the other. This mirrors `_docs/skills.md`'s own prior instinct
to group them (§1.4, §3).

**Fact, contrasting case.** `my-architecture-laboratory`, `my-feature-planning`, and
`my-git-workflow` are, by contrast, never co-loaded — each fires at a distinct lifecycle stage
(architecture/planning → issue drafting → implementation/release). This is evidence the three-way
split is well-founded, not over-fragmented.

---

## 7. Candidate stack capabilities

**Judgment**, offered as candidates for Phase D to weigh, not a recommendation to build any of
them:

1. **A Laravel-authoring-conventions capability**, drawn from `my-laravel-patterns` close to as-is:
   Actions/FormRequest/Controller split, `#[Authorize]`/`#[Scope]` attribute conventions, the
   Filters pattern, the four-layer testing-ownership model, enum-options, request-normalization,
   factory/seeder realism. §3 found this content already free of `useOrbit` product-domain
   leakage.
2. **A PhpStorm/Laravel/Pest IDE-conventions capability**, drawn from `my-phpstorm-conventions`
   close to as-is — same evidence quality as (1), arguably the strongest candidate in the whole
   ecosystem given zero leakage found.
3. **Whether (1) and (2) become one capability or two** is not settled by Phase C evidence — they
   are always co-loaded (§6i) and a prior `useOrbit`-local note already grouped them (§1.4), but
   they cover distinct concerns (authoring convention vs. IDE-warning workaround) and no
   cross-project evidence exists either way (§8.2).
4. **The generic Track A–G resource-feature-shape skeleton** in `resource-feature-checklist.md`
   (§2, §3) — weaker evidence than (1)/(2), since it is a single file's internal skeleton rather
   than an entire skill already built around the generic/specific distinction, and its generic and
   specific content are more thoroughly interleaved (§6b).
5. **`content-backlog`** is explicitly named in `roadmap.md`'s own "Future directions" as *"a
   possible Agentic Engineering capability, potentially independent of stack work."* This pass
   confirms it is genuinely owned, mature (5 rule files, a real 22-entry tracked backlog, real
   usage evidence spanning months), and structurally shaped like the other custom skills. It is
   **not** offered as a stack capability, though — its subject matter doesn't fit the stack-layer
   definition at all (§8.1).

---

## 8. Open questions

1. **Is `content-backlog` stack knowledge, `useOrbit`-specific knowledge, portable methodology, or
   a genuinely distinct category?** Its filesystem location (`useOrbit/.claude/skills/`) is an
   accident of where the user's Claude Code session happens to run, not evidence its content
   belongs to `useOrbit` the product. Several of its own tracked entries are *about* the
   `agentic-engineering` methodology-development process itself. Not resolved by this pass.
2. **Should `my-laravel-patterns` and `my-phpstorm-conventions` become one skill, stay two, or
   split along a different seam** (e.g. coding conventions vs. IDE conventions vs. testing
   conventions)? §6i's co-loading evidence and §1.4's prior grouping note both point toward
   combination, but neither is cross-project repeated evidence — only one project's worth exists
   for either skill.
3. **Where exactly does Track F's badge-tone/header/breadcrumb content belong** — custom Vue/
   Inertia-ecosystem convention, or `useOrbit` product design-system knowledge? §4 classifies it as
   leaning `useOrbit`-specific because the visual system it describes is this product's own design
   language, not a Vue/Inertia-ecosystem-wide convention, but this is a judgment call — the
   underlying responsive mobile/desktop header *pattern* (as opposed to its exact tone names) could
   reasonably sit on the stack side.
4. **Should `verification.md`'s embedded `php artisan test`/`vendor/bin/pint` commands be pulled
   into a labeled "what this repository's evidence shows" subsection**, matching `release.md`'s
   pattern (§6a)? Or is inline embedding acceptable here because it's a shorter, more mechanical
   fact than a release policy? Not resolved — flagged as a seam only.
5. **Is the `feedback_commit_workflow.md` vs. `commit-boundaries.md` body-line difference (§6g) an
   actual conflict**, or does the memory rule apply only to commits outside `my-git-workflow`'s own
   pipeline (which `commit-boundaries.md` scopes itself to)? Not resolved here.
6. **Is `my-architecture-laboratory/README.md`'s "not portable yet" self-assessment simply stale**
   (predating or not accounting for Phase A's `useOrbit`-reference cleanup), or does it know
   something this grep-based pass didn't find? Flagged, not resolved.
7. **Should `_design/*.jsx` location knowledge live in one place instead of two** — it currently
   exists both inline in `design-reconciliation.md` and in the separate `project_design_files`
   memory entry it cites (§6c)? Not resolved here.
8. **Is within-project repetition (e.g. Carriers/Clients/Agents all following the same Track A–G
   shape) sufficient evidence to call something "genuinely reusable Laravel/Vue ecosystem
   knowledge,"** per the categories `roadmap.md` itself defines — or does the "extract rules from
   evidence, not imagination" principle, applied strictly, require cross-project evidence Phase C
   cannot supply from a single consumer? This pass classifies within the roadmap's stated
   categories as instructed, but flags that Phase D's actual extraction/publication bar may
   reasonably be higher than this pass's classification bar.

---

## 9. Phase D implications

Offered as evidence-grounded possibilities, per `roadmap.md`'s "evidence-supported outcomes" list —
none of these are recommendations, and Phase D is free to reach a different conclusion or take no
action:

- Evidence supports Phase D **examining `my-laravel-patterns` and `my-phpstorm-conventions` as
  extraction candidates** (individually or paired) — both are free of `useOrbit` product-domain
  leakage and are the ecosystem's most consistently co-loaded, evidence-dense custom skills (§3,
  §6i, §7).
- Evidence supports Phase D **considering a targeted split within
  `resource-feature-checklist.md`** to separate its generic Track A–G skeleton from `useOrbit`'s
  specific instantiations — file/class mirrors, tone/badge/header conventions (§6b) — without this
  pass prescribing where each piece should land (§8.3).
- Evidence supports Phase D **reviewing whether `issue-conventions.md`'s inline milestone-naming/
  label-color content should become a pointer** to `useOrbit`'s own memory/docs, or a generalized
  pattern ("propose a numbered-phase convention," "rotate a fixed palette") rather than `useOrbit`'s
  literal values (§6c, §6d).
- Evidence supports Phase D **reconciling the commit-message-format soft conflict** between
  `feedback_commit_workflow.md` and `commit-boundaries.md`, if the user considers it live (§6g,
  §8.5).
- Evidence does **not** yet support extracting `content-backlog` into `agentic-engineering` — its
  subject matter doesn't match any of the three defined non-portable layers, and `roadmap.md`
  already treats it as a separate, later, non-committed question. Phase D should treat it as out of
  scope unless §8.1 is resolved first.
- Evidence supports **leaving `my-architecture-laboratory`, `my-feature-planning`'s core workflow
  (outside `resource-feature-checklist.md`), and all of `my-git-workflow` unchanged** — no
  misplaced project- or stack-specific content of consequence was found beyond what's already
  correctly self-labeled as "this project's convention."
- Evidence does **not** support creating `skills/portable-core/`, `skills/stack-adapters/
  laravel-vue-inertia/`, or `skills/project-specific/useOrbit/` yet, per `roadmap.md`'s own
  guardrail — no finding in this pass required a directory structure to express it.
- Whether `my-laravel-patterns` + `my-phpstorm-conventions` become one skill or two (§8.2) is
  genuinely open and should be decided on its own merits, not pre-judged by this discovery pass.

---
---

# Iteration 2 — Deep-Dive Readiness Pass

**Status:** Phase C discovery pass, second iteration. Still discovery and classification only — no
skill, memory file, or `useOrbit` file was modified to produce it. This iteration does not
supersede §§1–9 above; it goes one level deeper on the two strongest candidates and the most mixed
file, per iteration 1's own §7/§9 pointers, and records where it **confirms**, **sharpens**, or
**revises** iteration 1's judgments. Where the two disagree, this iteration's finding is more
specific (it is grounded in reading full rule-file bodies and cross-checking them against actual
`useOrbit` source and Boost skill content, not just skimming for `useOrbit`/stack-name grep hits),
but iteration 1's original text is left untouched above as the record of what that pass concluded
and why.

**Snapshot analyzed:**
- `agentic-engineering` @ `3f4ed76661ba1caa8dd0ebf0eaec14bad2c323cd` (`main`, clean working tree —
  this is iteration 1's own commit, recording its report)
- `useOrbit` @ `e95bf86ad101f56fb32ef8831da1d2af9b63ea67` (clean working tree — **unchanged** since
  iteration 1; both passes analyze the identical `useOrbit` state)
- The same personal `useOrbit` project memory directory, re-read for currency (file list unchanged
  from iteration 1's inventory)

**Method.** Full-text read of every operative file in `my-laravel-patterns` and
`my-phpstorm-conventions` (`SKILL.md` + all `rules/*.md`), of `resource-feature-checklist.md`, and
of the Laravel Boost skill files most likely to overlap with them
(`laravel-best-practices/rules/architecture.md`, `eloquent.md`, `advanced-queries.md`,
`validation.md`, `testing.md`; `pest-testing/SKILL.md`). Every concrete claim a rule file makes
about `useOrbit`'s own code — a class name, a trait, a GitHub issue number, a cited "established
precedent" file — was checked against the actual `useOrbit` source tree and its git history, not
taken on the rule file's word. This is the deeper method §8.8 of iteration 1 anticipated might be
needed.

---

## 10. `my-laravel-patterns` — readiness deep-dive

### Evidence
Full read of `SKILL.md` and all ten `rules/*.md` files, cross-checked against `useOrbit` source:
- `app/Providers/TestingServiceProvider.php` confirmed to actually define `AssertableInertia::macro('hasResource', ...)`,
  `AssertableInertia::macro('hasPaginatedResource', ...)`, `TestResponse::macro('assertHasResource', ...)`,
  `TestResponse::macro('assertHasPaginatedResource', ...)`, `TestResponse::macro('assertHasInertiaFlash', ...)` —
  exactly the five macros `testing-strategy.md` treats as available assertions.
- `app/Models/Concerns/BelongsToCurrentOrganization.php` confirmed to exist — the tenancy trait
  named (in passing) in `filters-pattern.md` and `resource-feature-checklist.md`.
- The GitHub issue links in `filters-pattern.md:5` (`https://github.com/elieandraos/useOrbit/issues/76`
  and `#71`) are literal, resolvable URLs into `useOrbit`'s own (non-`agentic-engineering`) GitHub
  repository — not a placeholder or a generic reference.
- `query-conditionals.md`'s three cited "established precedent" files were checked individually:
  `App\Http\Controllers\World\StatesController::index()` and `App\Concerns\GeneratesUniqueSlug` both
  still exist and both still call `->when(...)` (confirmed by direct grep) — these two citations
  hold up. The third, `App\Models\TagAttachment::forTaggableType()`, **does not exist anywhere in
  the current codebase**; `git log --all -- '*TagAttachment*'` shows it was introduced
  (`f146187`, "Add `TagAttachment::forDocumentableType` scope"), generalized ("Generalize tag
  filtering from documents to any Taggable model"), and then removed when commit `482e2d8`
  ("Collapse polymorphic tag attachment into a concrete `document_tag` pivot (#191)") refactored the
  polymorphic tags feature away entirely.
- `laravel-best-practices/rules/eloquent.md:33` (Boost's own first-party skill) already documents
  `#[Scope]` as its **own** "Correct" example for local scopes — the same attribute
  `my-laravel-patterns/rules/eloquent-attributes.md` presents as this project's convention
  "replacing legacy naming-convention methods."
- `laravel-best-practices/rules/testing.md:7-13` (Boost) states "Use Model Assertions Over Raw
  Database Assertions," giving `assertDatabaseHas('users', ['id' => $user->id])` as its own
  "Incorrect" example and `assertModelExists($user)` as "Correct." `testing-strategy.md`'s own
  worked examples use exactly the discouraged shape: `assertDatabaseCount('clients', 2)` and
  `assertDatabaseHas('clients', ['slug' => $client->slug])` (lines 59, 97) — the second of which is
  a direct instance of Boost's "Incorrect" pattern (asserting a specific record's attribute exists
  via raw DB query, with the model instance already in scope and `assertModelExists($client)`
  available as the alternative).
- `resources.md`'s Controller examples (lines 50, 58) call `Inertia::render('Clients/Index', [...])`.
  `my-phpstorm-conventions/rules/inertia.md` — the always-co-loaded sibling skill (§6i) — states as
  its central rule that `Inertia::render()` triggers a PhpStorm "Required parameter '$' missing"
  false positive and that the project's actual convention is the global `inertia()` helper
  (`rules/inertia.md:7-19`). `filters-pattern.md:116`, elsewhere in the *same* skill, correctly uses
  `return inertia('Clients/Index', [...])`. So `my-laravel-patterns` contradicts itself
  internally (`resources.md` vs. `filters-pattern.md`) and, in the `resources.md` direction,
  contradicts its own required co-loaded skill.

### Strengths (confirms iteration 1)
- `actions-pattern.md`, `filters-pattern.md`, `request-normalization.md`, `enum-options.md`,
  `factories-and-seeders.md` state real architectural decisions — the Actions/FormRequest split, the
  class-based `QueryFilter` dispatch mechanism, `prepareForValidation()`-owns-normalization,
  enum-owns-its-options-mapping, derived-not-independently-randomized fake data — that go
  meaningfully beyond anything Boost's `laravel-best-practices` ships (verified directly: Boost's
  `architecture.md` "Single-Purpose Action Classes" section is a bare `handle()`-method example with
  no FormRequest split, no naming convention, no `$attributes` parameter convention, no
  transaction/`afterCommit()` guidance — `my-laravel-patterns` is substantively additive here, not
  restating Boost in different words).
- `enum-options.md:41`'s explicit "kept consistent across enums for this project" is a model of
  correct self-labeling — an arbitrary naming choice presented as exactly that, not as a Laravel
  universal.
- `resources.md:75`'s framing of the `whenLoaded()` N+1 risk explicitly as conditional on "this app
  doesn't call `Model::preventLazyLoading()` anywhere" is another correctly-scoped, falsifiable
  assumption statement rather than an unstated one.

### Hidden coupling (new — not surfaced in iteration 1)
- **`testing-strategy.md`'s worked examples are not runnable in a project that lacks
  `TestingServiceProvider`'s five macros**, and nothing in `SKILL.md`, `testing-strategy.md`, or
  the skill's stated dependencies (`pest-testing`, `laravel-best-practices`) names this. A consumer
  in another Laravel/Inertia project would follow the rule file's examples verbatim, call
  `assertHasResource(...)`, and get a runtime "method does not exist" error with no explanation
  anywhere in the skill of why. This is a materially stronger form of coupling than the
  illustrative-variable-naming iteration 1 found elsewhere in this skill — it's a functional
  dependency on unexported project code, not a naming choice.
- `authorization.md:64`'s worked policy body (`$carrier->organization_id === $user->current_organization_id`)
  and `factories-and-seeders.md:53-73`'s `organization_id`/`current_organization_id`
  relationship-scoping examples both use `useOrbit`'s actual tenancy field names as the substance of
  a "how do you decide custom-state vs. built-in `for()`" or "how does an attribute-based child
  policy read the parent" demonstration. The *mechanism* each rule teaches (Laravel's `Authorize`
  attribute array-form resolution; `for()` vs. custom factory state) is genuinely stack-generic, but
  neither rule visibly separates "the mechanism" from "this project's tenancy shape" the way
  `resources.md:75` or `enum-options.md:41` do elsewhere in the same skill — a different project
  would need to mentally substitute its own scoping field before the example teaches anything.
- `filters-pattern.md:5`'s live hyperlinks into `elieandraos/useOrbit`'s issue tracker are a literal,
  resolvable identifying reference to the source repository embedded in what iteration 1 classified
  as portable stack knowledge — a stronger form of "project fingerprint" than a model name, since it
  names the actual GitHub repository.

### Redundancy / overlap (new — revises iteration 1's "no duplication found")
- Iteration 1 (§3) states "No content duplication with `laravel-best-practices` was found on
  inspection" for `my-laravel-patterns` as a whole. That holds for nine of the ten rule files on
  this closer read, but **`eloquent-attributes.md` is a partial exception**: its core claim — use
  `#[Scope]`, not `scopeXxx` — is already Boost's own first-party recommended convention
  (`laravel-best-practices/eloquent.md:33`), not something `my-laravel-patterns` originates. What
  `eloquent-attributes.md` adds beyond Boost's version is real but narrow (explicit `protected`
  visibility, the "no call-site change" note, framing it as "replacing legacy... methods" — i.e.
  migration guidance rather than greenfield guidance) — not nothing, but not the clean
  non-overlap iteration 1 recorded for the skill's other nine files.
- `testing-strategy.md` vs. `laravel-best-practices/testing.md`: **an actual disagreement, not just
  overlap** (see Evidence above) — Boost recommends `assertModelExists()` over
  `assertDatabaseHas()`; `my-laravel-patterns`' own worked examples use the pattern Boost's own
  first-party skill labels "Incorrect." Since `SKILL.md` instructs loading both skills together for
  any backend work, an agent following both simultaneously receives contradictory guidance on this
  specific point with no tie-breaking rule stated (contrast `my-laravel-patterns/SKILL.md:8`'s
  otherwise-clear "these take precedence... when there is a conflict" — that precedence rule would
  resolve this cleanly if anyone had noticed the conflict existed to apply it to).

### Example quality
- `query-conditionals.md`'s flagship example is broken as written: the method signature is
  `forTaggableType(Builder $query, string $taggableType, ?string $ownerType = null)`, but the body
  references `$ownerColumn` and `$modelClass`, neither a parameter nor assigned anywhere in the
  shown snippet — an elided resolution step, not obvious to a reader unfamiliar with the (now
  nonexistent) original method. Combined with the dead `TagAttachment` citation above, this is the
  single lowest-quality example in either candidate skill: illustrative-looking code that doesn't
  actually compile as shown, backed by a real-world citation to code that no longer exists.
- `filters-pattern.md`'s `Client::query()->filter(...)->latest('enrollment_date')->paginate(7)` and
  `testing-strategy.md`'s analogous examples read as verbatim (or near-verbatim) snippets lifted from
  real `useOrbit` controllers rather than cleaned teaching examples — the specific, slightly odd
  `paginate(7)` literal is the kind of detail a hand-written generic example wouldn't include. This
  isn't wrong, but it means the skill's examples carry real-code idiosyncrasies (arbitrary literals,
  a live issue-tracker citation, a dead-class citation) that a portable version would need to
  deliberately re-author, not just rename.
- By contrast, `authorization.md`, `resources.md`, `request-normalization.md`, and
  `factories-and-seeders.md`'s examples (aside from the tenancy-field-naming point above) read as
  intentionally constructed to teach the point, are internally consistent, and are not contradicted
  by any other evidence found.

### External dependency interaction
- Confirms iteration 1 (§5): the "load alongside, never replace" boundary with
  `laravel-best-practices`/`pest-testing` is explicit in `SKILL.md`.
- **Revises iteration 1's implicit assumption that this boundary is also conflict-free.** It is
  structurally clear (which skill takes precedence is stated) but not, on this closer read,
  actually conflict-free in content — see the `assertDatabaseHas`/`assertModelExists` and
  `#[Scope]` findings above. The precedence *rule* is fine; nobody has yet applied it to reconcile
  these two specific points.

### Portability risk
Moderate-to-high for `testing-strategy.md` specifically (a consuming project without the same five
custom macros gets non-functional examples with no warning); low-to-moderate for the rest of the
skill (illustrative field names and one dead citation, not structural). A different Laravel/Vue/
Inertia project could adopt `actions-pattern.md`, `filters-pattern.md`, `request-normalization.md`,
`enum-options.md`, `factories-and-seeders.md`, and `query-conditionals.md` (once its example is
fixed or replaced) largely as-is. It could **not** adopt `testing-strategy.md` as written without
either also importing `useOrbit`'s three custom macros or having the rule file explicitly say "these
examples assume the following project-local test macros exist; here's what they do, and here's the
plain-Pest fallback if they don't."

### Unresolved questions (new)
1. Should `testing-strategy.md`'s dependency on `TestingServiceProvider`'s macros be stated
   explicitly as a prerequisite, or should the layer-ownership *methodology* (the genuinely portable
   part — Action/Controller/Policy/Filter, no cross-layer duplication) be separated from the
   macro-dependent worked examples before this file is considered for extraction? Not resolved here.
2. Is the `assertDatabaseHas`/`assertModelExists` conflict with Boost's own `testing.md` a real,
   currently-live disagreement the user would want to reconcile, or does `my-laravel-patterns`'
   stated precedence-on-conflict rule already implicitly resolve it in `my-laravel-patterns`' favor
   (i.e., is this working as designed, just undocumented as a deliberate override)? Not resolved
   here — this is a question for the user, not something inferable from the files alone.
3. Should `eloquent-attributes.md` be trimmed to only the narrow delta over Boost's own `#[Scope]`
   documentation, or retained in full as a project-local restatement for convenience? Not resolved
   here.

### Readiness verdict: **promising but needs refinement first**
The authoring philosophy across most of the skill is genuinely reusable and, per iteration 1, richer
than Boost's equivalent coverage. But this pass found one file (`testing-strategy.md`) with an
undeclared functional dependency on project-local test macros, one file
(`eloquent-attributes.md`) with real (if partial) overlap with Boost's own first-party guidance, one
file (`query-conditionals.md`) with a broken/outdated worked example, and one cross-file internal
contradiction (`resources.md` vs. `my-phpstorm-conventions/rules/inertia.md`) — none of which
iteration 1's file-level read surfaced. These are fixable, scoped issues, not evidence the skill's
underlying philosophy is unsound, but they are concrete work Phase D (or a pre-Phase-D cleanup) would
need to do before this skill could be handed to a different project without also handing over
`useOrbit`'s undisclosed assumptions.

---

## 11. `my-phpstorm-conventions` — readiness deep-dive

### Evidence
Full read of `SKILL.md` and all six `rules/*.md` files.
- Every one of the six files documents a PhpStorm/Laravel-plugin/Pest-plugin static-analysis
  behavior (a false positive and its workaround, or an IDE-accuracy-improving convention). All
  worked examples use `useOrbit` model names (`Client`, `Organization`, `Carrier`, `Country`, `User`,
  `OrganizationMember`) purely as call-site illustration — none of the six files' *findings* depend
  on what those models mean in `useOrbit`'s domain, confirming iteration 1's "cleanest custom skill
  with respect to product-domain leakage" (§3) on a full re-read, not just a grep-based one.
- `SKILL.md:30` names a concrete external tool call, `getDiagnostics`, as the trigger mechanism for
  applying this skill's fixes ("run `getDiagnostics` on that file... a no-argument call returning
  'File not found' means the argument was missing, not that no IDE is connected").
- No file in the skill states which PhpStorm build, Laravel/PhpStorm plugin version, or Pest plugin
  version the documented false positives were observed against — contrast
  `my-laravel-patterns/rules/eloquent-attributes.md:3`'s explicit `laravel/framework ^13.7` pin.
- `rules/inertia.md` and `my-laravel-patterns/rules/resources.md` disagree on which Inertia call
  style is correct (see §10 above) — the contradiction is symmetric and belongs to both files, not
  just one.

### Strengths (confirms iteration 1)
- Zero findings in this file's six rule files depend on `useOrbit`'s tenancy model, design system, or
  product domain — every fix is about PhpStorm's own static-analysis engine (its `__callStatic`
  handling, its handling of union-typed facade methods, its Pest-plugin inspection for chained
  expectations, its handling of PHP string-interpolation grammar). This is genuinely
  IDE-and-framework knowledge, not project knowledge wearing project names.
- `pivot.md`, `strings.md`, and the `first()`/`static-call`/`polymorphic-call` sections of
  `eloquent.md` are self-contained, falsifiable, and independently verifiable by anyone with
  PhpStorm and a Laravel model open — the strongest form of portable evidence available at
  single-project scale.
- `phpdoc.md`'s "IDE Helper File" technique (re-declaring a class in its own namespace with
  `@method` docblocks to satisfy PhpStorm's macro resolution) is a genuinely general PhpStorm
  technique, explicitly generalized in the file itself ("this pattern works for any runtime-
  registered methods, not just macros") — one of the few places in either candidate skill where the
  file states its own generality rather than leaving it to be inferred.

### Hidden coupling (new)
- The skill's actual trigger mechanism (`SKILL.md:30`) is not "read this rule file," it's "call an
  external tool named `getDiagnostics`." That tool is not `search-docs`, not any Boost MCP tool
  listed in iteration 1's §5 external-dependency inventory, and not named anywhere in iteration 1's
  classification. It is almost certainly a JetBrains/PhpStorm IDE-integration MCP tool (the kind
  Junie or a PhpStorm MCP plugin would expose) — meaning **this skill assumes an IDE-integration
  tool most Claude Code sessions will not have**, silently, with no fallback stated for a session
  where `getDiagnostics` doesn't exist. This is a real external dependency this skill has that
  iteration 1's §5 (which covered Boost's MCP server and the `claude_design` MCP server) did not
  enumerate.
- `feedback_phpstorm_skill_activation.md` (memory, cited by iteration 1 §6d) already documents three
  prior occurrences of this skill's fix simply not firing reliably — independent evidence that the
  activation mechanism this skill depends on is itself fragile in practice, not just in theory.

### Redundancy / overlap
- No overlap found with `laravel-best-practices` or `pest-testing` content on this closer read — the
  subject matter (IDE static-analysis behavior) is outside what either Boost skill documents at all.
  This confirms iteration 1's finding with a fuller-file read rather than revising it.
- The one cross-*custom*-skill conflict (`inertia.md` vs. `my-laravel-patterns/resources.md`, see
  §10) belongs equally to this file.

### Example quality
Uniformly high. Every example follows a consistent ❌/✅ (or "Pattern/Warning/Verdict" table)
structure, states the exact PhpStorm warning text, and explains *why* the fix works in terms of
PhpStorm's own resolution mechanics (e.g. `eloquent.md`'s explanation of why `::query()` produces a
typed `Builder<Model>` PhpStorm can resolve, or `pest.md`'s explanation of why `@noinspection`
placed before an arrow-function expression doesn't reach inside the closure body). No dead
citations, no undefined-variable examples, no example found to contradict another file within this
skill.

### External dependency interaction
- `getDiagnostics` (see Hidden coupling above) is the material finding here — an undeclared,
  environment-specific tool dependency, distinct in kind from the MCP servers iteration 1's §5
  covered (those back specific skills' documented workflows; this one is the entire skill's
  triggering mechanism, stated in `SKILL.md` itself but not flagged as an external dependency by
  either pass until now).

### Portability risk
Low for the *content* (confirmed, again, on full read — zero product-domain leakage). Moderate for
the *mechanism*: a project using an editor/IDE other than PhpStorm (or PhpStorm without whatever MCP
integration exposes `getDiagnostics`) gets a skill whose actual enforcement step cannot fire, with no
stated fallback ("if `getDiagnostics` isn't available, read the rule files before finalizing PHP
files manually" or similar). The rule *content* travels; the *activation mechanism* may not.

### Unresolved questions (new)
1. What tool or MCP server actually provides `getDiagnostics` in this environment, and is it
   JetBrains-specific (PhpStorm/Junie) or something more general? Not established by this pass —
   worth the user confirming directly, since it changes how portable the activation mechanism is.
2. Should the skill state a PhpStorm/plugin version baseline (the way `eloquent-attributes.md` pins
   a Laravel version), given JetBrains actively fixes false positives over time and at least one
   finding here (`eloquent.md`'s `#[Scope]`-not-resolved section) explicitly describes current,
   not-yet-fixed IDE behavior ("does **not** (yet)")? Not resolved here.
3. Should `inertia.md` and `my-laravel-patterns/resources.md` be reconciled now, independent of
   Phase D, since they are both custom skills already meant to compose? Not resolved here — flagged
   as the one concrete internal defect worth fixing regardless of Phase D's outcome.

### Readiness verdict: **ready for Phase D consideration**
This remains the strongest custom-skill candidate in the ecosystem — the content itself withstood a
full re-read with zero new product-domain findings. What this pass adds is not a content problem but
two disclosure gaps a Phase D extraction should close as part of the work, not as a precondition to
starting it: name `getDiagnostics` as an explicit external/environment dependency (with a stated
fallback for sessions without it), and either pin a PhpStorm/plugin version baseline or explicitly
note that these findings should be periodically re-verified against current PhpStorm behavior. The
`inertia.md` vs. `resources.md` contradiction is real but is a one-line fix, not a readiness blocker.

---

## 12. `resource-feature-checklist.md` — separability deep-dive

**Question posed:** can the generic Track A–G skeleton be cleanly separated from `useOrbit`-specific
implementation and design-system material?

**Finding: structurally yes, textually no — the separation is a rewrite, not an extraction.**

Iteration 1 (§6b) already identified that this file braids three kinds of content in the same
tracks. This pass went further and checked whether that braiding happens *between* bullets (so a
generic/specific split could be done by moving whole lines) or *within* bullets (so splitting
requires rewriting individual sentences). It is overwhelmingly the latter. Representative instances,
read in full:

- Track A, line 13: `"Migration(s): table with organization_id, slug (if user-facing routing needs
  one), status/lifecycle column, created_by/updated_by, soft deletes, indexes on organization_id
  and [organization_id, status]"` — the generic fact ("a resource typically needs a migration with a
  tenancy/ownership column, an optional slug, a status column, audit columns, soft deletes, and
  indexes matching your query patterns") and the specific fact (`useOrbit` calls its tenancy column
  `organization_id` and its audit columns `created_by`/`updated_by`) are fused into one clause with
  no seam to cut along.
- Track A, line 14: `"Model: BelongsToCurrentOrganization, HasSlug, HasFactory, SoftDeletes — mirrors
  app/Models/Carrier.php"` — same pattern: the generic idea (a model composes traits for its
  cross-cutting concerns) is stated *as* the literal trait names, with a real file path appended as
  the citation.
- Track F, lines 61–66 (badge tones, mobile/desktop header breakpoints, drop-menu ordering) — these
  are not interleaved with anything generic at all; iteration 1 already flagged (§6g, §8.3) that this
  content may not belong to the Laravel/Vue ecosystem layer in the first place. This pass confirms:
  reading these lines in full, there is no generic Track-F "sentence" to extract *from* — the
  specific-to-`useOrbit` content **is** the entire content of most of Track F. A generic version
  would have to be authored new ("plan a responsive header breakpoint," "establish a fixed status-
  tone palette and reuse it"), not lifted by deletion from the current text.
- By contrast, line 5's own framing sentence ("The generic rule is the track structure itself...")
  and line 7 (naming which skills own implementation detail) are already cleanly generic, standalone
  sentences — these two lines, plus the seven track *headings* themselves (A–G) and their one-line
  "ask" framings (e.g. Track B's "does this resource get archived... as distinct from deleted";
  Track E's "which of these apply — they're separate issues"), are the genuinely portable skeleton,
  and they are the minority of the file's actual text.

**Portability of the underlying track *shape*, independent of this file's wording:** every track
name and its governing question (core infra / status lifecycle / sub-resource / filters+sorting /
export / frontend consistency / wiring gotchas) is a question any resource-shaped feature in any
CRUD-ish web framework has to answer, not something specific to Laravel or Vue. The *questions*
generalize further than the *file* currently does.

**Verdict:** the Track A–G shape (headings + governing questions) is a clean, high-confidence
extraction candidate on its own — closer in evidence quality to iteration 1's stronger candidates
than to the file it currently lives inside. The file's actual prose, though, would need to be
rewritten sentence-by-sentence into two versions (a generic Laravel/Vue/Inertia answer to each track,
and a separate `useOrbit`-local reference carrying the mirrors/tones/breakpoints), not mechanically
split. This is a heavier lift than either candidate skill in §10–§11, which need targeted fixes to
existing prose rather than a rewrite of most of it.

---

## 13. What this pass changes, confirms, and leaves unresolved

**Confirms, with fuller evidence:**
- `my-phpstorm-conventions` remains the ecosystem's cleanest custom skill re: product-domain
  leakage — this held up under a full re-read, not just the grep iteration 1 used (§2 of this
  iteration's method).
- `my-laravel-patterns`' authoring philosophy is genuinely additive over Boost's `laravel-best-
  practices`, verified directly against Boost's own file contents rather than inferred (§10,
  Strengths).
- `resource-feature-checklist.md` remains the most heavily mixed file in the ecosystem, and its
  Track F design-system content remains the weakest-fit material for the Laravel/Vue stack layer
  (iteration 1 §6g/§8.3; this pass's §12 independently arrives at the same place from a different
  angle — content density rather than category-fit).

**Revises or sharpens:**
- Iteration 1's "no content duplication with `laravel-best-practices` was found" (§3) is now
  qualified: `eloquent-attributes.md`'s `#[Scope]` guidance substantially overlaps Boost's own
  `eloquent.md`, and `testing-strategy.md` actively *conflicts* (not just overlaps) with Boost's
  `testing.md` on `assertDatabaseHas()` vs. `assertModelExists()` (§10).
- Iteration 1 classified `my-laravel-patterns` as depending only on `useOrbit` model names for
  illustration, with no deeper coupling (§3). This pass found one file
  (`testing-strategy.md`) with a genuine *functional* dependency on project-local test macros — a
  qualitatively different, stronger form of coupling than illustrative naming, and the single most
  consequential finding of this iteration.
- Iteration 1's external-dependency inventory (§5) is incomplete: `my-phpstorm-conventions`'
  `getDiagnostics` tool call is a real external dependency neither pass had previously named as one.
- A concrete, previously-unfound internal defect: `my-laravel-patterns/rules/resources.md` and
  `my-phpstorm-conventions/rules/inertia.md` — two always-co-loaded skills — give contradictory
  guidance on `Inertia::render()` vs. the `inertia()` helper. `my-laravel-patterns/rules/filters-
  pattern.md`, elsewhere in the same skill, follows the correct convention — so this is also a
  within-skill inconsistency, not only a cross-skill one.
- One outdated/broken worked example is now documented with its full provenance:
  `query-conditionals.md`'s `TagAttachment::forTaggableType()` citation refers to code removed by a
  real, identified commit (`482e2d8`), and the surrounding snippet references undefined variables.

**Leaves unresolved (unchanged from iteration 1, or newly opened but not answered here):**
- Whether `my-laravel-patterns` + `my-phpstorm-conventions` become one skill or two (iteration 1
  §8.2) — this pass adds no new evidence either way; if anything, the fact that this pass's two most
  consequential findings sit on opposite sides of that seam (a testing/macro-dependency issue in
  `my-laravel-patterns`, an IDE-tool-dependency issue in `my-phpstorm-conventions`) is itself a data
  point that the two skills carry genuinely distinct kinds of risk, which could argue either for
  keeping them separately addressable or for a combined skill with clearly labeled sub-sections —
  not decided here.
- Whether the `assertDatabaseHas`/`assertModelExists` conflict and the `Inertia::render()`/
  `inertia()` conflict are things the user wants reconciled now (independent of Phase D) or only if
  and when extraction happens — genuinely the user's call, not inferable from the files.
- The `getDiagnostics` tool's actual identity/provenance (§11, unresolved question 1) — not
  established by inspecting skill files alone.
- Everything iteration 1 left open in its own §8 that this iteration's narrower scope did not touch
  (`content-backlog`'s category, the commit-message body-line soft conflict, the milestone/label
  inline-vs-pointer question, etc.) remains exactly as open as iteration 1 left it.

**Net effect on Phase D readiness:** neither candidate is disqualified, but neither is a clean "take
it as-is" either. `my-phpstorm-conventions` is closer to extraction-ready — its gaps are disclosure
gaps (name the tool dependency, consider a version baseline) rather than content defects.
`my-laravel-patterns` needs one file's dependency made explicit or its examples reworked
(`testing-strategy.md`), one file's example fixed or replaced (`query-conditionals.md`), one file's
overlap with Boost acknowledged or trimmed (`eloquent-attributes.md`), and the cross-skill Inertia
contradiction resolved, before it is in the same state of readiness `my-phpstorm-conventions` is
already in. `resource-feature-checklist.md` needs substantially more — a genuine content split
rather than targeted fixes — and this pass's finding (§12) is that the *shape* of that split is now
well-evidenced even though the split itself is out of scope for a discovery pass to perform.
