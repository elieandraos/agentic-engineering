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

---
---

# Iteration 3 — Deep-Dive Portable Methodology Readiness

**Status:** Phase C discovery pass, third iteration. Still discovery and classification only — no
skill, memory file, or `useOrbit` file was modified to produce it. This iteration does not
supersede §§1–13 above; it opens a scope neither prior iteration covered in depth — the three
*canonical portable* skills (`my-architecture-laboratory`, `my-feature-planning`,
`my-git-workflow`) themselves, rather than the two candidate stack skills iteration 2 deep-dived.
Iteration 1 assessed these three via a full read plus a targeted grep; iteration 2 did not
re-touch them at all. This pass reads every operative file in all three end to end, verifies
concrete claims against `useOrbit`'s actual source, git history, and — new for this pass — the
actual published Claude Artifacts the methodology cites, using the `Artifact` tool's `read` and
`list` actions directly rather than trusting a citation's text.

**Snapshot analyzed:**
- `agentic-engineering` @ `0e7dcd515a996677680bb6f70435fbb115ec334c` (`main`, clean working tree —
  iteration 2's own commit). **Fact, checked directly:** no file inside `my-architecture-laboratory/`,
  `my-feature-planning/`, or `my-git-workflow/` has changed since the single commit that externalized
  them (`fe5bd29`, 2026-08-22) — `git log --all` against every file in all three skills' `rules/`/
  `references/` directories returns only that one commit. This pass and iterations 1–2 are reading
  byte-identical content.
- `useOrbit` @ `e95bf86ad101f56fb32ef8831da1d2af9b63ea67` (clean working tree — unchanged since
  iterations 1–2).
- `useOrbit` project memory directory, re-listed: 15 `feedback_*` files + `project_design_files.md` +
  `MEMORY.md`, vs. iteration 1's count of "16 feedback + 1 project." **Open question, not pursued
  further here** (out of this iteration's scope, which is the three portable skills, not the memory
  ecosystem): whether one feedback memory was removed/merged since iteration 1, or iteration 1's count
  included `MEMORY.md` itself. Noted for completeness, not investigated.
- The user's published Claude Artifacts (`Artifact` tool, `action: "list"`, `scope: "mine"`) — 9
  artifacts total, read directly where `my-architecture-laboratory` cites one.

**Method.** Full-text read of all 23 operative files across the three skills (8 in
`my-architecture-laboratory`, 9 in `my-feature-planning`, 9 in `my-git-workflow`, counting each
`SKILL.md` and `README.md`). Every citation to an external artifact, a `useOrbit` GitHub issue, or a
`useOrbit` memory file was checked against the actual source — not taken on the citing file's word.
Concretely: both Claude Artifact URLs `my-architecture-laboratory/SKILL.md` names as its foundational
worked examples were fetched directly; `useOrbit`'s git history was searched for the polymorphic
`Taggable`/`TagAttachment` architecture doc-style.md's table describes; a `useOrbit` GitHub issue
(`#296`) `discovered-work.md` cites was fetched via `gh issue view` and compared word-for-word against
the rule file's description of it; `template.html`'s embedded syntax-highlighter script was read in
full, not sampled.

---

## 14. `my-architecture-laboratory` — deep-dive

### Evidence

**Fact.** `SKILL.md` (lines 14–16) names two "existing guides this methodology was reverse-engineered
from," both "published Claude Artifacts, not repo files": *Reusable Documents Architecture*
(`claude.ai/code/artifact/7a9c2f1c-bbb5-4241-95b0-7502c4c2bc0b`) and *Centralized Tagging Architecture*
(`claude.ai/code/artifact/ab74b104-8e43-4301-b46d-9963c2f35449`). The file instructs: *"If you haven't
internalized why those two documents have different section names for what looks like 'the same'
section, read `references/doc-style.md` before writing anything — that's the whole point of this
methodology."* `references/doc-style.md` and `references/review.md` both restate that these two guides
are the methodology's entire empirical basis (doc-style.md line 3: *"This file exists because the two
source guides prove structure adapts to the capability"*; review.md line 3: *"the methodology
developed while iterating on the Documents and Tags architecture guides"*).

**Fact, directly verified via `Artifact` `action: "read"`.**
- The Documents URL resolves: owned by the user, private, 67.2 KB, titled "Reusable Documents
  Architecture" — live and consistent with the citation.
- The Tagging URL does **not** resolve: `"artifact not found — it may have been deleted, or it has
  not been shared with you."` This is the exact URL `SKILL.md` names as one of exactly two canonical
  worked examples the entire Phase-3 writing methodology (`doc-style.md`) claims to be built from.

**Fact, via `Artifact` `action: "list"`, `scope: "mine"`.** A *different* artifact titled "Tagging
Architecture" (no "Centralized") exists at a different URL
(`claude.ai/code/artifact/1dd446e6-fee1-4f54-9783-136dec7761f0`), last updated 2026-08-09 — live,
owned by the user, private. Neither `SKILL.md` nor `doc-style.md` nor `review.md` names or links this
URL anywhere. The same listing surfaces a ninth artifact, "CRUD Application Architecture"
(`25f3c842-5343-4168-9cc7-c730c7a436cb`, updated 2026-08-09) — plausibly, but not confirmed by opening
it, the unnamed "CRUD guide" `references/review.md` (line 151: *"exports were the case that surfaced
this in the CRUD guide"*) refers to without ever naming or linking it anywhere in the skill.
**Inference, not confirmed:** the CRUD-guide identification is a title match, not a read-and-compare
verification the way the Documents/Tagging check was — flagged as inference, not fact.

**Fact.** `doc-style.md`'s "Section inventory is not fixed" table (line 53) describes the Tagging
guide's foundation as *"The Taggable contract — a two-method interface... (`ownerColumn(): ?string`)"*
— i.e., a polymorphic tag-attachment architecture.

**Fact, via direct grep of the entire `useOrbit` tracked source tree** (`.php`/`.vue`/`.ts`, excluding
`vendor`/`node_modules`): zero occurrences of `Taggable` or `ownerColumn` anywhere in the current
codebase.

**Fact, via `git log --all`.** A polymorphic `Taggable`/`TagAttachment` architecture did exist:
introduced by `9515a99` ("Add Tag model, polymorphic taggables pivot, and Document wiring (#162)",
2026-07-28), generalized by `1fe9b61` ("Generalize tag filtering from documents to any Taggable
model"), then **removed** by `482e2d8` ("Collapse polymorphic tag attachment into a concrete
`document_tag` pivot (#191)", 2026-07-31) and `126fe31` ("Drop `taggable_type` from Manage Tags UI and
its composables (#192)", same day). This is the identical `TagAttachment::forTaggableType()` removal
iteration 2 §10 already found independently while checking `my-laravel-patterns/rules/
query-conditionals.md` — the same real refactor surfaces a second time here, in a different skill,
through a different citation.

**Fact.** `my-architecture-laboratory/SKILL.md` was committed to `agentic-engineering` (`fe5bd29`) on
2026-08-22 — three weeks after the 2026-07-31 collapse.

**Inference.** The "Centralized Tagging Architecture" guide `SKILL.md` cites by name and URL as half
of its foundational teaching precedent almost certainly documented the pre-collapse polymorphic
`Taggable` architecture (the specific method signature `doc-style.md` quotes, `ownerColumn(): ?string`,
does not exist anywhere in the current source and never will again absent a revert) — and, independent
of that content question, the citation itself is now a dead link for the account that owns it. A
same-titled-but-different guide describing (presumably, per its more recent 2026-08-09 update date)
the current concrete-pivot architecture exists but is referenced from nowhere in the skill.

**Judgment.** This single finding sits in three of this iteration's seven analysis categories at once:
it is a **stale/broken worked example** (category 3 — the cited artifact is unreachable, and the
content it's known to have taught no longer matches the source project); it is **hidden project
coupling** (category 1 — the methodology's entire empirical basis for "how a document's structure
should adapt to its capability" is two specific `useOrbit` capabilities, not synthesized or genericized
examples, disclosed as real guides but not as `useOrbit`-specific in the way `my-feature-planning`'s
rule files consistently self-label their illustrations); and it is a **portability gap** (category 7 —
even a `useOrbit` engineer reading this skill today cannot open the citation to check the lesson
firsthand, and a different project's consumer never could, private-artifact URLs being
non-transferable by construction).

**Fact, via full read of `references/template.html` (438 lines), including its embedded
syntax-highlighter script (lines 356–420).** The `highlight()` function recognizes exactly five
`data-lang` values with dedicated styling: `php`, `ts`, `json`, `vue`, `http`. Keyword highlighting
(`KEYWORDS` map) exists only for `php`, `ts`, and `json`. PHP gets dedicated regex handling for `#[Attribute]`
syntax and `$variable` sigils; Vue gets dedicated tag/attribute regex handling. There is no generic
fallback keyword/type highlighter for any other language — a code block in Python, Go, Ruby, Java, C#,
or Rust would render with string-literal highlighting only, no keyword or type coloring, and no
`--lang-*` CSS variable for its language-badge color (only `--lang-php`, `--lang-ts`, `--lang-vue`,
`--lang-json`, `--lang-http` are defined in the `:root` token, lines 53–57). **Judgment.** This is
concrete, unambiguous stack/tooling coupling (category 2) baked directly into the one shared artifact
scaffold every Phase 3/4 architecture guide is built from, for any capability in any stack — not an
illustrative example that could be swapped, but an implementation gap in the rendering pipeline itself.
`SKILL.md` step 3 instructs using this file "as the starting scaffold... keep the design system unless
the capability genuinely needs a new block type" — nothing in that instruction, or anywhere else in the
skill, flags that the highlighter's language support is PHP/Vue/TS-only.

**Fact, by cross-reference.** `doc-style.md`'s "Content block vocabulary" table names seven CSS
classes (`.specsheet`, `.ascii`, `.table-wrap`/`table.lc`, `.flow-steps`, `.callouts`/`.callout`,
`.formula`, `.pill`); all seven exist in `template.html`, confirmed by direct grep. This is a positive
coherence finding — the one documentation/implementation pairing in this skill that was checked and
found to match exactly, unlike the doc-style.md/Tagging-artifact pairing above.

**Fact.** `README.md`'s "Is this portable?" section (lines 182–195), which iteration 1 §8.6 flagged as
a possibly-stale self-assessment based on a grep-only pass, states the skill *"assumes things specific
to this project: this project's Laravel/Vue stack, its particular Artifact publishing workflow for
architecture guides, the existence of `plan.md`, and a handoff to `my-feature-planning`."*

**Judgment — resolves iteration 1 §8.6.** The literal claim ("assumes... this project's Laravel/Vue
stack") still does not hold on inspection — no operative file in this skill contains Laravel/Vue
keywords, confirmed independently by both iteration 1's grep and this iteration's full read. But this
pass's findings show the self-assessment's *spirit* was right for reasons the text itself doesn't
name: real coupling exists, just not as literal Laravel/Vue references — it's in the PHP/Vue/TS-only
syntax highlighter (a stack-tooling fact, not a stack-vocabulary fact) and in the two-`useOrbit`-guide
teaching precedent (a project-evidence fact, not a stack fact). The self-assessment's other three
claims — the Artifact publishing workflow, `plan.md`'s existence, and the `my-feature-planning` handoff
— are accurate and, per this pass's findings below, correctly classified as external-capability and
internal-methodology dependencies respectively, not defects. **Conclusion: not stale — imprecise about
*why* it's right, but not wrong that real, non-trivial coupling remains.**

**Fact, full read of `references/maintenance.md`, `references/plan-synthesis.md`, and the
Phase-1/2/4 prose in `SKILL.md`.** Zero coupling found — no `useOrbit` reference, no stack reference,
no dead citation, in any of these. `plan-synthesis.md`'s locked/open decision rule, canonical section
list, and review checklist are fully generic and self-contained. This confirms and sharpens iteration
1's "cleanest of the three" verdict for these specific files, while the findings above show the verdict
does not extend to the whole skill uniformly.

**Fact.** `references/review.md`'s checklist itself (the "Architectural center," "Reusable capability,"
"Runtime," "Implementation," "Structure," "Decisions," "Overall" categories) is fully generic — every
question is phrased as a property of "the guide," never of `useOrbit`. The only project-specific
residue in this file is the unnamed "CRUD guide" citation noted above.

### External dependency interaction

**Fact.** Phase 3 (`SKILL.md` steps 2–4) requires the `artifact-design` skill and the `Artifact` tool
by name — both genuinely external, Claude-Code-platform capabilities, not stack-specific. This
dependency is disclosed structurally (named at the point of use) rather than as an upfront "requires"
statement, but it is unambiguous and, on inspection, accurate: Phase 3, Phase 4, and Plan Synthesis's
guide-publishing track cannot function without the `Artifact` tool. **Judgment.** This is a real
environment dependency worth stating explicitly for portability purposes: Phase 1 (Explore) and Phase 2
(Recap) work in any environment with file/code-reading tools; Plan Synthesis's `plan.md` output is a
plain file with no `Artifact` dependency at all; but the architecture-guide half of this skill (Phase
3/4) is unusable in a Claude Code environment without Artifact-publishing access, or in any other
agentic coding tool. This is a reasonable, disclosed-by-use dependency, not a leak — but it is more
consequential to portability than iteration 1 §5 (which covered `claude_design`'s role in
`design-reconciliation.md`, a `my-feature-planning` file) credited to this skill specifically.

### Readiness verdict: **Portable core with targeted refinement needed**

The four-phase discipline, the locked/open Plan Synthesis rule, the maintenance methodology, and most
of the review checklist are genuinely portable and, on a full re-read, hold up better than a
grep-only pass could show. What keeps this skill short of "clean" is concentrated and fixable rather
than structural: (1) the skill's single foundational teaching precedent cites a now-dead artifact URL
whose documented content — per direct source and git-history verification — describes an architecture
`useOrbit` itself no longer has; (2) the shared artifact template's syntax highlighter has PHP/Vue/TS/
JSON-only support with no generic fallback or disclosure; (3) one review-checklist citation ("the CRUD
guide") is never named or linked. None of these require redesigning the phase discipline itself — they
are a broken citation to repair or replace, a template gap to either generalize or disclose, and a
missing link to add.

---

## 15. `my-feature-planning` — deep-dive

### Evidence

**Fact.** `SKILL.md`'s own top-level Workflow section (not a `rules/` file) states at step 18: *"it
names the pieces an issue needs (FormRequest, Action, Policy, API Resource, thin Controller,
factory/seeder, tests)"* — Laravel-specific vocabulary embedded directly in the always-loaded
activation surface, rather than confined to an illustrative `rules/` file the way every other project-
or stack-flavored reference in this skill is. **Judgment.** This is a smaller, more surprising instance
of category-1/2 coupling than anything iteration 1 found in this skill's `rules/` files, precisely
*because* it sits in `SKILL.md` itself — the one file every invocation of this skill loads regardless
of which downstream rule applies.

**Fact, spot-verification via `gh issue view 296`.** `discovered-work.md`'s description of issue #296
(the Inertia background-revisit response-mismatch finding, used as the "Deep" investigation-band
example, lines 38–39 and throughout `issue-conventions.md`'s "Discovered-work issues" section) matches
the live GitHub issue's Context section word-for-word in substance: the same confirmed/unconfirmed
split (HTTP 200 vs. server exception; 2FA-incomplete accounts only; unaffected by #295's fix; the
exact server-side reason left open), the same "Capture the automatic Inertia revisit's actual
request..." task phrasing quoted directly in `issue-conventions.md:165`. All four tasks in the live
issue are checked (`- [x]`), confirming the finding was resolved and the citation reflects a completed,
accurate historical record rather than a stale or aspirational one. **This is a positive finding**:
unlike `my-architecture-laboratory`'s Tagging citation, this skill's most load-bearing concrete
citation is current and accurate on direct verification.

**Fact, re-confirmed on full read.** Every `rules/` file in this skill (`feature-classification.md`,
`capability-checklist.md`, `design-reconciliation.md`, `discovered-work.md`, `issue-conventions.md`,
`plan-md-input.md`, `review.md`, `sequencing.md`) marks its `useOrbit`-derived illustrations with an
explicit, consistent label — "An example from this project," "Examples from this project," "this
project's..." — the same disciplined self-labeling iteration 1 §2/§6 documented. This pass's full read
finds no exception to that discipline anywhere in these eight files; the labeling habit is genuinely
uniform, not selectively applied.

**Fact.** `design-reconciliation.md:11`'s direct, named dependency on the `project-design-files`
memory (*"Per the `project-design-files` memory: design files from Claude Design live at `_design/`..."*)
is present exactly as iteration 1 §6c described — unchanged, unresolved, confirmed on this pass's own
read rather than inherited from iteration 1's citation.

**Fact.** `rules/review.md` (the review/validation file) is, on full read, "generic by construction" in
its own words, twice (lines 80, 126) — the rendered-manifest-integrity and issue-body-content-integrity
checks explicitly state they re-derive their expected set from whatever the canonical definitions
currently are, "for any feature and any issue count," and instruct never hard-coding a specific issue,
title, or phrase into the check itself. This is the single most rigorously self-aware portability
statement found anywhere in the three-skill ecosystem across all three iterations.

**Fact, confirmed unchanged.** `resource-feature-checklist.md` was not re-analyzed line-by-line in this
pass (`git log` confirms it is byte-identical to what iterations 1–2 examined, and iteration 2 §12
already produced a full separability deep-dive on it). This iteration's contribution is corroborating,
not new: the file remains the ecosystem's heaviest concentration of interleaved generic/`useOrbit`-
specific content, and nothing in this pass's reading of the other seven `rules/` files or `SKILL.md`
changes that assessment.

### External dependency interaction

**Fact.** `gh` (GitHub CLI) commands appear throughout `issue-conventions.md`, `review.md`, and
implicitly in the workflow steps of `SKILL.md` — issues, milestones, and labels are GitHub-native
concepts, not just a tool choice. **Judgment.** This is a genuine, undisclosed-but-reasonable platform
dependency distinct from the Laravel/Vue stack-coupling findings: a team using GitLab Issues or Jira
instead of GitHub would need to adapt every `gh`-shaped instruction in this skill, not merely swap a
CLI binary name, because concepts like "milestone," "label," and the `#N` auto-linkification behavior
`issue-conventions.md`'s reference-syntax rules are built around are GitHub-specific product behavior.
Neither this skill nor iteration 1's external-dependency inventory (§5) names "GitHub, specifically" as
a dependency distinct from "Laravel Boost" or "the `Artifact` tool" — worth naming explicitly here as
its own category.

**Fact, confirms iteration 1 §5.** `laravel-best-practices` and `my-laravel-patterns` are named as
implementation-time loads in `SKILL.md`'s frontmatter description and step 18/105 — a correctly
disclosed composition boundary, reconfirmed on full read.

### Readiness verdict: **Portable core with targeted refinement needed**

The classification taxonomy, the checklists' governing questions, the issue-format rules, and the
three-tier review/validation model are genuinely portable, evidence-accurate on spot-check, and
unusually disciplined about labeling illustrative content — this pass found no new instance of
unlabeled project leakage outside what iterations 1–2 already identified. The refinement needed is
concentrated in three places, one newly found here: `resource-feature-checklist.md`'s content split
(iteration 2 §12, unchanged, the heaviest lift), the two named memory dependencies (`design-
reconciliation.md`'s `project-design-files` citation, `issue-conventions.md`'s `feedback_github_issues`
citation), and — new this pass — `SKILL.md` step 18's Laravel vocabulary leaking into the
always-loaded activation file rather than staying confined to an illustrative rule file.

---

## 16. `my-git-workflow` — deep-dive

### Evidence

**Fact, full re-read of `rules/verification.md`, confirms iteration 1 §6a on direct inspection rather
than citation.** The "Default loop" section states, unboxed, directly inside general methodology prose:
*"verify it with the tests actually relevant to that commit's change (`php artisan test --compact
<path>`) plus `vendor/bin/pint --dirty --format agent`"* (lines 18–20), and the isolation-verification
recipe (lines 50–51) repeats `vendor/bin/pint --test --format agent` and `php artisan test --compact`
the same way. **New in this pass:** the same file's "Ordering commits to keep intermediate states
green" section names `skipUnlessFortifyHas()` (line 66) as the concrete mechanism behind its
feature-flag-ordering principle — a second, previously uncited Laravel-Fortify-specific reference in
the same file, also unboxed. Contrast `release.md`, read in full this pass and confirmed to still be
the one file in the entire three-skill ecosystem that consistently separates portable methodology
from project-evidence facts behind an explicit **"What this repository's evidence shows"** heading
(twice — release policy discovery, and the publish-mechanism section) — `verification.md` has no
equivalent heading anywhere, despite carrying comparably concrete repository-specific facts.

**Fact, full read of `rules/commit-boundaries.md`, `rules/issue-closure.md`, `rules/review-gates.md`,
`rules/sequencing.md`, `rules/milestone-completion.md`.** Zero stack or project coupling found in any
of these five files beyond real-evidence citations that are already consistently and explicitly framed
as "the evidence this skill was extracted from" (`#288`, `#287`, `#120`, `#289`, PR `#298`, `v0.17.0`)
— never presented as the rule itself. `review-gates.md`'s one incidental Laravel-specific mention
(`gatherMiddleware()`, line 61) is inside a real-evidence citation illustrating an investigation
method, not a rule statement, and is comparably minor to the `#[Scope]`/`when()` mentions iteration 1
already found acceptable elsewhere in this ecosystem.

**Fact.** `SKILL.md`'s frontmatter explicitly and correctly names the stack-skill composition boundary:
*"Always load ALONGSIDE this project's implementation skills (`my-laravel-patterns`,
`laravel-best-practices`, `pest-testing`, `my-phpstorm-conventions`, `inertia-vue-development`,
`fortify-development`, `wayfinder-development`, etc. as the code demands) — this skill owns the
workflow machinery around commits, closure, release, and post-release milestone completion, not the
code, tests, or framework conventions themselves."* This is the most extensive and explicit
composition-boundary statement found in any of the three skills' frontmatter — a genuine strength,
consistent with iteration 1 §5/§6f's "positive existing boundary" finding, reconfirmed at greater
detail.

**Fact.** `README.md`'s "Is this v0.1, and what's missing on purpose" section explicitly refuses to
invent PR-creation, merge-strategy, deployment-trigger, or branch-naming conventions the repository's
own evidence doesn't support — stated as a deliberate methodological stance ("the same method that
built this skill... is how each of those should get added later... once there's a real... pattern to
learn from"), not an oversight. **Judgment.** This restraint is itself a portable-methodology
principle worth naming explicitly: the skill models "don't extrapolate a rule from one data point" on
itself, in its own gaps, not only in the rules it does state.

### External dependency interaction

**Fact, confirms iteration 1 §5, no revision.** `gh` (issue/milestone/release operations) is used
throughout exactly as in `my-feature-planning`, with the same GitHub-specific-concepts caveat noted in
§15 above applying equally here (milestones, releases, and the `gh api .../milestones` PATCH mechanism
`milestone-completion.md` uses are GitHub product concepts, not just CLI syntax).

### Readiness verdict: **Portable core with targeted refinement needed**

Of the three skills, this one required the smallest correction on a full fresh read: six of its seven
rule files (`commit-boundaries.md`, `issue-closure.md`, `review-gates.md`, `sequencing.md`,
`release.md`, `milestone-completion.md`) are fully portable, evidence-accurate, and — in `release.md`'s
case — the model the rest of the ecosystem should be measured against. The gap is narrow and isolated:
`verification.md`'s "Default loop" and commit-ordering sections carry two Laravel/Pest/Fortify-specific
citations directly inside general methodology prose, unboxed, in the one file of the seven that never
adopts the "what this repository's evidence shows" separation its sibling file uses successfully one
file over. This keeps the skill out of "clean portable core" by a single file's single section, not by
a pervasive or structural problem.

---

## 17. Cross-skill boundary findings

**Fact, reconfirms iteration 1 §6h on a full fresh read of all three skills' README "owns / does not
own" sections side by side.** The architecture → planning → git-workflow lifecycle boundary remains
exceptionally clean: every "owns" list is matched by a corresponding "does NOT own" entry in the
adjacent skill, every cross-reference is directional, and this pass found zero new instance of one
skill silently performing another's job — no issue drafting inside `my-architecture-laboratory`, no
architecture re-derivation inside `my-feature-planning`, no issue creation inside `my-git-workflow`.
This is now confirmed by three independent passes at increasing depth (iteration 1's grep-plus-read,
iteration 2's deep-dive of the adjacent stack skills, and this iteration's full read of all three
portable skills together) — strong, repeated evidence the three-way decomposition itself is sound.

**Fact — a new, genuine handoff-boundary gap.** `my-feature-planning` treats it as an established,
load-bearing fact that `plan.md` sections get deleted once the corresponding work ships — stated
explicitly in `SKILL.md:48` (*"in this project specifically, `plan.md` sections get deleted once the
corresponding work ships (verifiable in its own commit history...)"*) and used to justify the entire
"GitHub issues must stand alone" principle. **Verified true**, independent of the skill's own citation:
`useOrbit`'s git history shows real pruning commits (`4698b7c` "Remove implemented Client Location
Data section from plan.md", `7c1e69b` "Remove completed Clients Export section from plan.md," both
July 2026, predating the skills' formal existence). But `my-architecture-laboratory` — the skill that
now owns `plan.md`'s lifecycle end-to-end, including its Plan Synthesis track — never states this
pruning as something it does. `plan-synthesis.md`'s "Where the plan lives" section (lines 134–140)
only discusses *appending* a new section to an existing `plan.md`, explicitly modeled on how Phase 4
preserves a guide's narrative; nothing anywhere in this skill discusses removing a completed section.
**Judgment.** Neither skill claims ownership of the deletion action. `my-feature-planning` relies on a
practice it doesn't perform and doesn't ask the other skill to perform, having observed it happen
historically under pre-skill, ad hoc practice. This is a real, if narrow, "questionable handoff
boundary" (the deliverable's own language) — not a contradiction, since nothing in either skill
actively conflicts, but an assumption one skill depends on that the other skill never commits to
sustaining now that both are formalized.

**Fact.** Milestone-related rules cross-reference correctly and consistently between the two skills
that touch them: `my-feature-planning/rules/issue-conventions.md`'s Backlog-vs.-delivery-milestone
distinction and its optional-description-as-contract framing are read and respected without
reinterpretation by `my-git-workflow/rules/milestone-completion.md` ("The milestone description, when
present, is still the contract... This skill doesn't redraft, reinterpret, or second-guess that
description — it applies it as written," lines 61–67). No contradiction found on full read of both
files together.

**Fact — a structural strength worth naming explicitly.** All three skills share a consistent,
disciplined self-labeling convention for illustrative `useOrbit` content — "An example from this
project" / "Examples from this project" / "this project's convention" / "the evidence this skill is
built from" — applied uniformly across all 23 files read for this iteration, with the single narrow
exception of `my-architecture-laboratory`'s two-guide teaching precedent (§14 above), which is
disclosed as *real, published, external* material but not disclosed as `useOrbit`-*specific* the way
every other illustrative citation across the ecosystem is. This is evidence the labeling discipline
is a deliberate, cross-skill authored convention — making the one exception more notable, not less.

**Judgment.** Nothing found in this pass argues for changing the three-skill decomposition itself.
Every finding in §§14–16 is containable within its own skill's existing file boundaries (a citation to
fix, a template to generalize, a section to box, a link to add) rather than requiring responsibility to
move between skills — with the single exception of the `plan.md`-pruning gap above, which is a
disclosure gap between two skills' documentation, not evidence either skill is doing the wrong job.

---

## 18. Project/stack leakage — strongest concrete examples, prioritized

1. **`my-architecture-laboratory`'s dead/stale Tagging-guide citation** (§14) — the strongest finding
   of this iteration. Not cosmetic: it is the literal, named empirical foundation of the skill's
   Phase-3 writing methodology, verified unreachable via direct `Artifact` read, and — per independent
   git-history verification — its documented content almost certainly describes an architecture
   `useOrbit` no longer has.
2. **`template.html`'s PHP/Vue/TS/JSON-only syntax highlighter** (§14) — genuine tooling coupling
   baked into the one shared rendering pipeline every architecture guide from any capability, in any
   stack, passes through.
3. **`resource-feature-checklist.md`** (iterations 1–2, reconfirmed unchanged this pass) — remains the
   single heaviest concentration of interleaved generic/`useOrbit`-specific content in the whole
   ecosystem; no new evidence changes iteration 2 §12's "a rewrite, not an extraction" verdict.
4. **`my-git-workflow/rules/verification.md`'s unboxed Laravel/Pest/Fortify commands** (§16) —
   reconfirmed via full read, with one new citation (`skipUnlessFortifyHas()`) iteration 1 didn't
   name; the contrast with `release.md`'s labeled-separation pattern, sitting one file over in the
   same skill, remains the clearest evidence this is a fixable gap, not a structural one.
5. **`my-feature-planning/SKILL.md` step 18's inline Laravel vocabulary** (§15) — smaller in scope
   than the above but notable for *where* it sits: the always-loaded activation file, not an
   illustrative `rules/` file, unlike every other project/stack reference in this skill.

---

## 19. Example/template audit

**Preserve as-is** (portable, evidence-accurate on spot-check, no coupling found on full read):
`my-architecture-laboratory/references/maintenance.md`, `plan-synthesis.md`; `my-feature-planning/
rules/feature-classification.md`, `capability-checklist.md`, `discovered-work.md`, `plan-md-input.md`,
`review.md`, `sequencing.md`; `my-git-workflow/rules/commit-boundaries.md`, `issue-closure.md`,
`review-gates.md`, `sequencing.md`, `release.md`, `milestone-completion.md`. Fourteen of the
twenty-three operative files read this pass fall cleanly into this bucket.

**Needs targeted rewrite/refinement:**
- `my-architecture-laboratory/references/doc-style.md` — the two-guide teaching precedent needs either
  a working, current citation (repoint to the live "Tagging Architecture" artifact once its content is
  confirmed to still teach the intended lesson) or should be generalized into a synthetic/abstract
  description that no longer depends on a private, non-transferable URL at all.
- `my-architecture-laboratory/references/template.html` — the syntax highlighter needs a generic
  keyword/type fallback for unlisted languages, or an explicit note that its language support is
  PHP/TS/Vue/JSON-specific.
- `my-architecture-laboratory/references/review.md` — name and link "the CRUD guide" or remove the
  reference.
- `my-feature-planning/rules/resource-feature-checklist.md` — unchanged conclusion from iteration 2
  §12: needs a genuine content split, not a targeted fix.
- `my-feature-planning/SKILL.md` — step 18's Laravel vocabulary could be reworded to name "this
  project's Actions-pattern layers" generically, or boxed as a labeled example the way every `rules/`
  file in this skill already does.
- `my-git-workflow/rules/verification.md` — needs the same "what this repository's evidence shows"
  boxed treatment `release.md` already models, extended to cover both the Pest/Pint commands and the
  `skipUnlessFortifyHas()` mechanism.

**Stale, specifically (not merely coupled):** `my-architecture-laboratory/SKILL.md`'s
"Centralized Tagging Architecture" citation — both its URL (dead) and, per independent verification,
its known content (a polymorphic architecture the source project collapsed away three weeks before
this skill file was written).

**Verified accurate and current (a positive finding, not previously checked by either prior
iteration):** `my-feature-planning/rules/discovered-work.md`'s `#296` citation, spot-checked directly
against the live GitHub issue and found to match in substance and phrasing, with all tasks resolved.

---

## 20. External capability audit

- **The `Artifact` tool + `artifact-design` skill** (`my-architecture-laboratory`, Phase 3/4 and Plan
  Synthesis's guide track) — correctly used and named at the point of use; genuinely external to the
  portable methodology; not disclosed as an upfront "requires" statement anywhere, but its necessity is
  unambiguous from the phase instructions themselves. A consumer without Artifact-publishing access can
  still use Phase 1/2 (investigation, recap) and Plan Synthesis's `plan.md` output, but not the
  architecture-guide half of the skill.
- **`gh` / GitHub itself** (`my-feature-planning`, `my-git-workflow`) — used extensively and correctly
  as a tool choice, but the dependency runs deeper than tooling: milestones, labels, and issue
  auto-linkification are GitHub product concepts the methodology's vocabulary is built around, not
  swappable for another issue tracker without rewriting `issue-conventions.md`'s reference-syntax rules
  and both skills' `gh`-shaped instructions. Neither skill nor iteration 1's §5 names this as its own
  dependency category, distinct from Laravel Boost or the `Artifact` tool — worth naming explicitly now.
- **Laravel Boost skills + the two custom stack skills** — correctly and explicitly declared as
  "load alongside" dependencies in all three portable skills' frontmatter/`SKILL.md` prose; the
  disclosure quality is highest in `my-git-workflow/SKILL.md`'s frontmatter, which names every specific
  Boost skill it expects alongside it. No revision to iteration 1 §5's finding here — reconfirmed at
  greater detail.
- No new MCP-tool-level dependency was found inside these three skills (`getDiagnostics` belongs to
  `my-phpstorm-conventions`, out of this iteration's scope, per iteration 2 §11).

---

## 21. Readiness conclusion per skill

**`my-architecture-laboratory` — Portable core with targeted refinement needed.**
The four-phase discipline, the maintenance methodology, the Plan Synthesis locked/open rule, and most
of the review checklist are genuinely portable and hold up under a full fresh read better than iteration
1's grep-only pass could show. The skill falls short of "clean" for reasons iteration 1 could not have
found: a foundational teaching citation that is both unreachable and — per independent verification —
describes an architecture the source project no longer has, and a shared artifact template with real,
undisclosed stack-tooling coupling in its rendering pipeline. Both are fixable without touching the
phase discipline itself, but both are more consequential than "cleanest of the three" suggested.

**`my-feature-planning` — Portable core with targeted refinement needed.**
The classification taxonomy, checklist governing questions, issue-format rules, and three-tier
review/validation model are genuinely portable and unusually disciplined about labeling illustrative
`useOrbit` content — confirmed via spot-verification against a live GitHub issue, not just inspection.
The refinement needed is concentrated in `resource-feature-checklist.md` (a genuine rewrite, the
heaviest lift of any single file across all three skills), two named memory dependencies, and — newly
found this pass — `SKILL.md` step 18's Laravel vocabulary sitting in the always-loaded activation file
rather than an illustrative rule file.

**`my-git-workflow` — Portable core with targeted refinement needed.**
The lightest lift of the three, but not zero: six of seven rule files are fully portable and
evidence-accurate, and `release.md` remains the strongest methodology/adapter-fact separation anywhere
in the ecosystem. The one gap — `verification.md`'s two unboxed Laravel/Pest/Fortify citations sitting
in general methodology prose, one file away from a sibling file that solves the identical problem
correctly — is narrow, isolated, and modelable on evidence that already exists inside this same skill.

No skill in this iteration earned "Clean portable core" outright, and none fell to "Mixed; boundary
separation needed" or "Not currently suitable" — every finding in §§14–16 is a targeted content or
disclosure fix contained within existing file boundaries, not a sign the phase/workflow/checklist
*structures* themselves are unsound or need re-drawing.

---

## 22. Phase D implications

Offered as evidence-grounded possibilities, consistent with `roadmap.md`'s "evidence-supported
outcomes" framing — none are recommendations, and Phase D remains free to reach different conclusions
or take no action:

- Evidence supports Phase D **repairing or replacing `my-architecture-laboratory`'s dead "Centralized
  Tagging Architecture" citation** — either repointing to the live "Tagging Architecture" artifact
  (after confirming its current content still teaches the intended structural lesson) or generalizing
  `doc-style.md`'s teaching precedent so it no longer depends on a private, non-transferable URL.
- Evidence supports Phase D **addressing `template.html`'s syntax-highlighter language coverage** —
  either a generic fallback for unlisted languages or an explicit disclosure that its highlighting is
  tuned for PHP/TS/Vue/JSON projects, before the shared artifact template is treated as stack-neutral.
- Evidence supports Phase D **applying `release.md`'s "what this repository's evidence shows" pattern
  to `verification.md`**, now with two citations to box rather than one (the Pest/Pint commands
  iteration 1 found, plus this pass's `skipUnlessFortifyHas()` finding) — unchanged in kind from
  iteration 1's open question §8.4, sharpened with additional evidence.
- Evidence supports Phase D **naming/linking `review.md`'s unnamed "CRUD guide" citation**, or removing
  it if it isn't meant to be a real dependency.
- Evidence supports Phase D **clarifying `plan.md` section-pruning ownership** between
  `my-architecture-laboratory` and `my-feature-planning` — a real, if narrow, disclosure gap between
  two skills rather than a contradiction, newly surfaced by this iteration.
- Evidence continues to support (unchanged from iteration 2 §13) **a genuine content split within
  `resource-feature-checklist.md`** — this iteration's full read of the rest of the ecosystem found
  nothing that reduces the scope of that already-identified lift.
- Evidence does **not** support redesigning the three-skill decomposition — the architecture → planning
  → git-workflow boundary held up under a third, deepest pass with zero new contradictions found, only
  one narrow disclosure gap (plan.md pruning) that doesn't require moving responsibility between skills.
- Evidence does **not** support treating any of the three skills as requiring a ground-up rewrite —
  every finding in this iteration is a targeted, containable fix; none rises to "mixed" or
  "not currently suitable."

---

## 23. What Iteration 3 confirmed, discovered, and leaves unresolved

**Confirmed, with fuller or independently-sourced evidence:**
- The three-skill lifecycle boundary (architecture → planning → git-workflow) remains exceptionally
  clean under a third, full-text pass of all 23 files — no new contradiction found (§17).
- `my-git-workflow/rules/verification.md`'s unboxed stack-command coupling, first found by iteration 1
  via targeted grep, holds up under full read and gains one new supporting citation (§16).
- `resource-feature-checklist.md`'s status as the ecosystem's heaviest-mixed file (iterations 1–2)
  is unchanged and independently reconfirmed by this pass's reading of everything around it (§15, §18).
- `my-feature-planning`'s illustrative-example self-labeling discipline, documented by iteration 1,
  is confirmed uniform across all eight `rules/` files on full read, with one live citation
  (`#296`) spot-verified word-for-word against GitHub (§15).

**Discovered — new to iterations 1–2:**
- `my-architecture-laboratory`'s foundational teaching citation is a dead link, and independently
  verifiable evidence (grep + git history) shows its documented content described an architecture
  `useOrbit` had already refactored away by the time the citation was written into `agentic-engineering`
  — the single most consequential finding of this iteration, in a skill both prior iterations treated
  as the cleanest of the three based on a grep-based pass that could not have found it (§14).
- `template.html`'s syntax highlighter has hardcoded, undisclosed PHP/Vue/TS/JSON-only language support
  baked into the one shared rendering pipeline every architecture guide passes through (§14).
- `my-feature-planning/SKILL.md`'s own top-level Workflow section (not a `rules/` file) carries inline
  Laravel vocabulary, a smaller but more structurally notable instance of coupling than anything found
  in this skill's `rules/` files, because of where it sits (§15).
- A real, if narrow, cross-skill disclosure gap around who is responsible for pruning completed
  `plan.md` sections — relied upon by one skill, never claimed by the skill that owns the artifact (§17).
- `review.md`'s unnamed "CRUD guide" citation, and the existence of a third, unreferenced architecture
  artifact ("CRUD Application Architecture") plausibly matching it (§14).

**Leaves unresolved:**
- Whether "CRUD Application Architecture" is in fact the guide `review.md` calls "the CRUD guide" —
  flagged as inference (title match only), not confirmed by opening the artifact (§14).
- Whether the live "Tagging Architecture" artifact (distinct URL, more recent update date) documents
  the current concrete `document_tag` pivot rather than the polymorphic architecture — not opened past
  its header in this pass; the dead-link finding and the git-history mismatch stand independent of this
  question either way (§14).
- The memory-directory count discrepancy noted in this iteration's snapshot section — out of scope for
  this pass, not investigated (front matter, above).
- Everything iterations 1–2 left open in their own §8 that this iteration's narrower three-skill scope
  did not touch (`content-backlog`'s category, the commit-message body-line soft conflict, `my-laravel-
  patterns`/`my-phpstorm-conventions`'s one-skill-or-two question, etc.) remains exactly as open as
  those iterations left it.

**Net effect on Phase D readiness:** the three canonical portable skills are, on this deepest pass yet,
in materially the same overall state as the two stack candidates iteration 2 examined — genuinely
useful, evidence-grounded methodology with concentrated, fixable gaps rather than structural problems.
No skill in this ecosystem, portable-core or stack-layer, has yet earned an unqualified "clean" verdict
across three increasingly deep passes; each pass has instead found real, previously-invisible issues
proportional to how hard it looked. That pattern is itself evidence worth carrying into Phase D: Phase
A's completion established that the three skills are *consumable*, not that they are *finished*, and
each iteration of this discovery phase has found something the previous one's method could not have
surfaced.

---
---

# Phase C Synthesis — Current Disposition

**Status:** Phase C synthesis pass. Consolidates Iterations 1–3 into a current best evidence-backed
disposition of the mature custom skill ecosystem. Still classification and judgment only — no skill,
`useOrbit` file, `roadmap.md`, or `README.md` was modified to produce this section, and Iterations 1–3
above are preserved byte-for-byte. Per this pass's own instructions, this section does not begin Phase D
and does not prescribe implementation structure beyond what the evidence makes unavoidable.

**Method.** Before writing this section, a fresh reading pass independently re-inspected the underlying
evidence rather than taking Iterations 1–3 on their word: `roadmap.md`'s Phase C/D sections and
`README.md`'s "Current portability status" section were read directly; all five scored skills' directory
structures were confirmed unchanged (`git log` shows `HEAD` is still iteration 3's own commit `fccc9f2`,
identical to the tree iteration 3 analyzed); and a sample of the most load-bearing claims across all
three iterations was independently re-verified against live sources rather than re-derived from the
document text:

- `TestingServiceProvider`'s five macros — confirmed to exist exactly as iteration 2 §10 describes.
- `getDiagnostics` named in `my-phpstorm-conventions/SKILL.md` (lines 3, 30–31) — confirmed exactly as
  iteration 2 §11 describes, including the retry-per-file caveat.
- `verification.md`'s unboxed `php artisan test`/`vendor/bin/pint`/`skipUnlessFortifyHas()` citations —
  confirmed at the exact lines iterations 1 and 3 cite.
- Boost's `laravel-best-practices/rules/eloquent.md:33` and `rules/testing.md:7-13` — confirmed to state
  `#[Scope]` and `assertModelExists()` exactly as iteration 2 §10 describes, and `my-laravel-patterns/
  rules/testing-strategy.md:59,97` confirmed to use the `assertDatabaseCount`/`assertDatabaseHas` pattern
  Boost's own file labels "Incorrect" — the conflict iteration 2 found is real and unchanged.
- `query-conditionals.md`'s `forTaggableType` example — confirmed broken exactly as iteration 2
  describes (`$ownerColumn`/`$modelClass` referenced but never defined or passed), and `git log --all --
  '*TagAttachment*'` independently reproduces the same five-commit lifecycle (introduced `9515a99`,
  generalized `1fe9b61`, collapsed away by `482e2d8`/`126fe31`) iteration 2 first found while checking a
  different skill and iteration 3 found again independently while checking a third.
- `content-backlog`'s skill directory (5 rule files) and `content-backlog.md` (1,432 lines, actively
  tracked) — confirmed to exist as iteration 1 describes.
- **New verification, not performed by any prior iteration:** both Artifact citations central to
  iteration 3's §14 finding were re-fetched directly via the `Artifact` tool, one day after iteration 3's
  own snapshot. The "Centralized Tagging Architecture" URL `my-architecture-laboratory/SKILL.md` cites by
  name **still does not resolve** — "artifact not found." The live, differently-titled "Tagging
  Architecture" artifact iteration 3 found but did not open past its header **was opened and grepped
  directly**: it contains 13 occurrences of `document_tag` and zero of `Taggable`/`ownerColumn`/
  `TagAttachment` — confirming, not merely inferring, that it documents `useOrbit`'s *current* concrete-
  pivot architecture, not the dead polymorphic one the broken citation is known to have taught. This
  resolves iteration 3 §23's second open question: yes, the live guide is current and usable — the
  problem is entirely that `SKILL.md` points at the wrong (dead) URL, not that no good citation exists.
  The "CRUD Application Architecture" artifact was also opened and grepped for `export`: it contains
  extensive `ExportController`/`ExportClientToPdfAction`/`ExportTest` content, corroborating — on content,
  not just title — iteration 3's inference that this is the unnamed "CRUD guide" `references/review.md:151`
  cites. Both of iteration 3's two `content unresolved` open questions are now resolved in the direction
  iteration 3's inference already pointed.
- **New finding, not surfaced by any prior iteration:** `README.md`'s own "Current portability status"
  section (lines 114–116) states, as a Phase A finding, that `my-architecture-laboratory`'s two style
  precedents "resolve from any project context, so no fix was needed there." Direct re-verification shows
  this is no longer true for the Tagging citation specifically — it is a dead link today, independent of
  and prior to this pass's own action (this pass changed nothing). This is recorded here as a *currency*
  gap in `README.md`'s Phase A claim, not a defect in Phase A's process at the time it was written, and
  — per this pass's constraints — `README.md` itself is left unmodified; the gap is Phase D's (or a
  maintenance pass's) to address.

This spot-check covered the ecosystem's most consequential citations across all three iterations and
found every one to hold up exactly as documented, with the two open questions above now resolved and one
new documentation-currency gap surfaced. No claim in Iterations 1–3 was found to be inaccurate on
independent re-inspection.

---

## Readiness rubric

Two rubrics apply, per `roadmap.md` Phase C §"Method"'s own category split — one for the three canonical
portable-methodology skills, one for the two custom stack skills. Both use the same 0–10 scale:

- **8–10:** mature, with only targeted cleanup/refinement needed.
- **6–7.9:** sound foundation, but meaningful refinement remains.
- **4–5.9:** mixed or materially coupled, requiring substantial refinement.
- **0–3.9:** not currently suitable for reusable extraction.

Scores below are this pass's structured judgment applied consistently across both rubrics, not an
objective measurement — a reasonable person could weight some dimensions differently, particularly for
`my-laravel-patterns`, where the score sits closest to a rubric-band boundary (see its own section for
the specific weighing).

### Portable-methodology dimensions

1. **Methodology purity** — does the rule state a principle or process independent of implementation, or
   is the principle fused with concrete stack commands/facts that could be swapped out without losing the
   lesson?
2. **Project independence** — does the rule's *validity* depend only on illustration (a `useOrbit` name
   used as a stand-in), or does it depend on a `useOrbit`-specific fact, macro, field, or live citation
   that a different project would not have?
3. **Stack/tooling independence** — does applying the rule require a specific language, framework,
   editor, or platform to exist, and if so, is that requirement disclosed?
4. **External dependency clarity** — are dependencies on tools/platforms outside the skill itself (the
   `Artifact` tool, GitHub/`gh`, an MCP server) named explicitly, with behavior stated for a consumer
   lacking them, rather than assumed silently?
5. **Example/reference quality** — do the skill's citations and worked examples resolve, remain current
   against the source project, and stay internally consistent?
6. **Internal coherence** — do a skill's own files agree with each other, with no unnoticed
   self-contradiction?
7. **Cross-skill responsibility clarity** — does the skill state what it owns versus what an adjacent
   skill owns, with no silent overlap and no unclaimed handoff?

### Custom-stack dimensions

Stack-specificity is not penalized here — it is the point of this layer. Instead:

1. **Stack relevance and reuse potential** — would a different Laravel/Inertia (or PhpStorm-tooling)
   project genuinely benefit from this rule as stated, beyond this one codebase?
2. **Project independence** — does the rule's validity depend only on the stack, or does it silently
   depend on `useOrbit`-specific code, config, or a live pointer into `useOrbit`'s own issue tracker?
3. **Dependency clarity** — are functional dependencies (custom test macros, IDE-integration tools,
   package versions) disclosed, with a stated fallback for a consumer that lacks them?
4. **Overlap with first-party capabilities** — does the rule duplicate, silently conflict with, or
   cleanly extend what Laravel Boost's own skills already document?
5. **Example/reference quality** — are worked examples runnable, current, and free of citations to
   removed code?
6. **Internal coherence** — do this skill's own files agree with each other and with its always-co-loaded
   sibling skill?
7. **Maintainability** — is version- or time-sensitive knowledge (an IDE build, a framework version)
   pinned or flagged for periodic re-verification, so a future maintainer knows when it might have gone
   stale?

---

## Scoreboard

| Skill | Classification | Readiness score | Category | One-line reason |
|---|---|---|---|---|
| `my-git-workflow` | Portable methodology | **7.3** | Sound foundation, meaningful refinement remains | Six of seven rule files are clean and evidence-accurate; the one gap (`verification.md`'s two unboxed stack citations) is narrow, isolated, and already modeled by a sibling file in the same skill. |
| `my-architecture-laboratory` | Portable methodology | **6.8** | Sound foundation, meaningful refinement remains | The four-phase discipline and Plan Synthesis rule hold up under the deepest read of the three, but its one foundational teaching citation is a dead link whose known content no longer matches the source project, and its shared template has undisclosed PHP/Vue/TS-only tooling coupling. |
| `my-phpstorm-conventions` | Custom stack/ecosystem knowledge | **8.2** | Mature, targeted cleanup only | Zero product-domain leakage found across two full-file reads; every gap is a disclosure gap (`getDiagnostics`' identity, no version baseline), not a content defect. |
| `my-feature-planning` | Portable methodology, mixed at one file | **6.3** | Sound foundation, meaningful refinement remains | Eight of nine files are portable and unusually disciplined about self-labeling; `resource-feature-checklist.md` is the single heaviest concentration of interleaved generic/`useOrbit` content in the whole ecosystem, and `SKILL.md` itself (not just a rule file) carries inline Laravel vocabulary. |
| `my-laravel-patterns` | Custom stack/ecosystem knowledge | **5.8** | Mixed, requires substantial refinement | Genuinely additive authoring philosophy over Boost in most files, but one file has an undisclosed functional dependency on project-local test macros, one actively conflicts with Boost's own guidance, one has a broken worked example, and the skill contradicts its own co-loaded sibling on a concrete convention. |
| `content-backlog` | Category unresolved | — deferred — | Outside current Phase D stack scope | Genuinely owned and mature, but its subject matter (personal-brand/authorial content about the methodology-development process itself) does not confidently fit any of the three defined layers; see its own section below. |

`my-laravel-patterns` sits closest to a band boundary (5.8, just under the 6.0 line into "sound
foundation"). The weighing that keeps it in the lower band rather than the higher one: this pass counts
the *combination* of an undisclosed functional dependency, an active (not merely overlapping) conflict
with Boost's own first-party guidance, a broken example tied to a real deleted-code citation, and a
within-skill self-contradiction as four independent, materially different failure modes concentrated in
one skill — a denser cluster of distinct problem types than any other scored skill carries, even though
most of the skill's individual files are strong.

---

## Skill-by-skill synthesis

### `my-architecture-laboratory`

#### Classification
**Portable methodology.** Confirmed across all three iterations: no operative file contains Laravel/Vue/
PHP-stack vocabulary, and the phase discipline, locked/open Plan Synthesis rule, maintenance methodology,
and review checklist are all stated as properties of "the guide," never of `useOrbit` (Iteration 1 §2;
Iteration 3 §14). The `README.md` self-assessment iteration 1 flagged as possibly stale (§8.6) is resolved
by iteration 3 (§14) and reconfirmed by this pass: its literal claim ("assumes this project's Laravel/Vue
stack") does not hold on inspection, but its *spirit* — real, non-trivial coupling exists — is correct for
reasons the text itself never names (the template's language-specific highlighter, and the two-`useOrbit`
-guide teaching precedent).

#### Strengths
The Explore → Recap → Guide → Maintain discipline, the "codebase tells us what exists, the human decides
what it should become" principle, and the locked/current-state/derived/open-decision Plan Synthesis
taxonomy are fully generic and self-contained (Iteration 1 §2; Iteration 3 §14). `references/maintenance.md`
and `references/plan-synthesis.md` show zero coupling of any kind on full read — the strongest files in
the skill. `references/review.md`'s checklist categories are phrased entirely as properties of "the
guide." The `doc-style.md`/`template.html` content-block vocabulary (seven CSS classes) matches exactly
between documentation and implementation — a positive coherence finding, not just an absence of problems.

#### Problems
One finding dominates: `SKILL.md`'s two named foundational teaching citations are its *entire* stated
empirical basis for the Phase-3 writing methodology, and one of the two — the URL for "Centralized
Tagging Architecture" — is confirmed dead (this pass's own re-fetch, one day after iteration 3's, still
returns "artifact not found"), and its known content (a polymorphic `Taggable` contract with
`ownerColumn()`) describes an architecture `useOrbit` collapsed away three weeks before this skill file
was committed (Iteration 3 §14, independently reproduced by this pass via `git log`). A live,
differently-titled replacement artifact exists and — per this pass's own direct read — documents the
*current* architecture, but nothing in the skill names or links it. Separately, `template.html`'s syntax
highlighter has hardcoded PHP/TS/Vue/JSON-only language support with no generic fallback and no
disclosure (Iteration 3 §14) — real tooling coupling baked into the one rendering pipeline every guide,
in any stack, passes through. A third, smaller gap: `references/review.md`'s "the CRUD guide" citation is
never named or linked — this pass's own verification confirms a real, matching artifact exists
("CRUD Application Architecture," content-matched on its exports discussion), so this is a missing link
to add, not a fabricated reference.

#### Dependencies and overlaps
No `useOrbit` project-memory dependency was found in this skill (contrast `my-feature-planning`, below).
Real external-capability dependency on the `Artifact` tool and the `artifact-design` skill for Phase 3/4
and Plan Synthesis's guide-publishing track — disclosed by use, accurately, though not as an upfront
"requires" statement (Iteration 3 §14). No cross-skill overlap found with `my-feature-planning` or
`my-git-workflow` beyond the correctly-directional Plan Synthesis → issue-drafting handoff (Iteration 3
§17). One genuine, narrow cross-skill disclosure gap: `my-feature-planning` treats `plan.md` section
pruning as an established fact it relies on but does not perform, while `my-architecture-laboratory` —
which now owns `plan.md`'s lifecycle — never states pruning as something it does (Iteration 3 §17).

#### Example/reference quality
Two of the skill's most load-bearing citations were independently re-verified by this pass rather than
taken on the iterations' word: the dead Tagging URL is confirmed dead today, and the live "Tagging
Architecture" and "CRUD Application Architecture" artifacts were opened and grepped directly, confirming
they are current, on-topic, and (for the CRUD one) content-matched to the citation that names it. This
elevates iteration 3's findings from "verified once" to "verified twice, on different days, by different
means" for the artifact-liveness claims specifically.

#### Required refinement
Repoint or regenerate `doc-style.md`'s teaching precedent (repoint to the live "Tagging Architecture"
artifact once its lesson is confirmed to still teach the intended structural point, or generalize the
lesson so it no longer depends on a private, non-transferable URL at all); give `template.html`'s
highlighter a generic fallback or an explicit disclosure of its PHP/TS/Vue/JSON-only scope; name and link
"the CRUD guide." None of these require touching the phase discipline itself.

#### What should remain unchanged
The four-phase structure, the Plan Synthesis locked/open rule, `maintenance.md`, and the review
checklist's generic framing — all confirmed clean under the deepest read applied to any skill in this
ecosystem (Iteration 3's full-text pass plus this pass's independent artifact re-fetch).

#### Current disposition
**Portable core with targeted refinement needed.** The refinement is concentrated and containable — a
citation to repair, a template to generalize or disclose, a link to add — not a sign the phase/workflow
structure itself is unsound.

---

### `my-feature-planning`

#### Classification
**Portable methodology, with one heavily mixed file.** The Planned-vs-Discovered work-origin model, the
investigation-depth/checkpoint framework, the four-shape feature-classification taxonomy, the issue-format
rules, and the three-tier review/validation model are genuinely portable (Iteration 1 §2). One file,
`resource-feature-checklist.md`, braids that portability with dense `useOrbit`-specific content (Iteration
1 §6b; Iteration 2 §12) — see "Mixed material synthesis" below for its own detailed treatment.

#### Strengths
Every `rules/` file marks its `useOrbit`-derived illustrations with an explicit, consistent label ("An
example from this project," etc.) — Iteration 3 §15 confirms this discipline holds with zero exception
across all eight `rules/` files on a full read, not just a sample. `rules/review.md` states twice, in its
own words, that its checks re-derive their expected set "for any feature and any issue count" and warns
against hard-coding — the single most rigorous portability self-statement found anywhere in the ecosystem
across all three iterations (Iteration 3 §15). `discovered-work.md`'s `#296` citation was spot-verified
word-for-word against the live GitHub issue and found accurate, with all tasks resolved — a positive
finding, not just an absence of a negative one (Iteration 3 §15).

#### Problems
`resource-feature-checklist.md` remains the ecosystem's heaviest concentration of interleaved generic and
`useOrbit`-specific content, reconfirmed unchanged across all three iterations, with iteration 2 §12
establishing that separating it is "a rewrite, not an extraction" — the braiding happens within
individual sentences and clauses, not between them. Newly found in iteration 3 (§15): `SKILL.md`'s own
top-level Workflow section — not a `rules/` file, the one file every invocation of this skill loads
regardless of which downstream rule applies — states at step 18 that an issue names "FormRequest, Action,
Policy, API Resource, thin Controller, factory/seeder, tests," Laravel-specific vocabulary sitting outside
the self-labeling discipline the rest of the skill follows. `design-reconciliation.md:11` carries a named,
direct content dependency on the `project-design-files` personal memory entry (Iteration 1 §6c; Iteration
3 §15, unchanged).

#### Dependencies and overlaps
Two named personal-memory dependencies: `design-reconciliation.md` → `project-design-files`, and
`issue-conventions.md` → `feedback_github_issues` (the latter self-acknowledged inline). `issue-
conventions.md` also independently restates the live, evolving `feedback_github_label_colors` "next hue"
state as a static snapshot — the memory is the actual source of truth here, and the skill's restatement
can drift (Iteration 1 §6c/§6d). External dependency on `gh`/GitHub as a product, not just a CLI choice —
milestones, labels, and `#N` auto-linkification are GitHub-specific concepts `issue-conventions.md`'s
reference-syntax rules are built around (Iteration 3 §15, newly named as its own dependency category).
Correctly disclosed composition boundary with `laravel-best-practices`/`my-laravel-patterns` as
implementation-time loads (Iteration 1 §5, reconfirmed Iteration 3 §15).

#### Example/reference quality
Strong outside the one heavily mixed file: the `#296` citation is accurate and current (Iteration 3 §15,
spot-verified). `resource-feature-checklist.md`'s own citations are a mix of genuinely generic pattern
references (the Actions pattern, `wayfinder:generate --with-form`) and literal `useOrbit` file mirrors
(`app/Models/Carrier.php`) fused into the same sentences (Iteration 2 §12).

#### Required refinement
A genuine content split of `resource-feature-checklist.md` (the heaviest lift of any single file across
the whole ecosystem, per iteration 2 §12); rewording or boxing `SKILL.md` step 18's Laravel vocabulary
consistent with the rest of the skill's labeling discipline; a decision on whether the two named memory
dependencies become pointers, generalized patterns, or stay as-is with the dependency simply disclosed
more prominently.

#### What should remain unchanged
The classification taxonomy, the checklist governing questions (outside Track F), the issue-format rules,
the three-tier review model, and the self-labeling discipline itself — all reconfirmed clean under a full
fresh read in iteration 3, with no new exception found.

#### Current disposition
**Mixed; boundary separation needed** for `resource-feature-checklist.md` specifically, sitting inside an
otherwise **portable core with targeted refinement needed** for the skill as a whole. The skill-level
score (6.3) reflects that the mixed file's severity is real but contained to one file plus one
newly-found `SKILL.md` leak, not spread across the skill.

---

### `my-git-workflow`

#### Classification
**Portable methodology.** The lightest lift of the three canonical skills across every iteration that
touched it (Iteration 3 §16, §21).

#### Strengths
"Issues describe outcomes, commits describe decisions"; the full commit-boundary reasoning in `commit-
boundaries.md`; the two-gate model in `review-gates.md`; the ask-first recipe in `issue-closure.md`; the
dependency-ready recalculation in `sequencing.md`; the three-condition closure gate in `milestone-
completion.md` — all confirmed portable, evidence-accurate, and free of stack coupling on a full read
(Iteration 1 §2; Iteration 3 §16, reconfirming with zero new exception across five of the skill's seven
rule files). `release.md` is, across all three iterations, the single clearest methodology/adapter-fact
separation in the entire ecosystem — it boxes concrete repository facts behind an explicit **"What this
repository's evidence shows"** heading, twice, rather than weaving them into general prose (Iteration 1
§2, §6a; Iteration 3 §16). `README.md`'s explicit refusal to invent PR/merge/deployment conventions the
repository's own evidence doesn't yet support is itself a portable-methodology principle worth naming —
the skill models "don't extrapolate from one data point" on itself (Iteration 3 §16).

#### Problems
`rules/verification.md` is the one file that does not follow `release.md`'s labeled-separation pattern —
its "Default loop" and commit-ordering sections state Laravel/Pest/Fortify facts (`php artisan test
--compact`, `vendor/bin/pint --dirty --format agent`, `skipUnlessFortifyHas()`) directly inside general
methodology prose, unboxed (Iteration 1 §6a; Iteration 3 §16 adds the `skipUnlessFortifyHas()` citation
iteration 1 didn't name). This pass's own re-grep confirms both citations sit exactly where documented,
unchanged.

#### Dependencies and overlaps
`gh`/GitHub dependency shared with `my-feature-planning`, same caveat: milestones and releases are GitHub
product concepts (Iteration 3 §16). Correctly and explicitly disclosed composition boundary — `SKILL.md`'s
frontmatter names every specific Boost/custom implementation skill expected alongside it, the most
extensive such statement in any of the three skills (Iteration 1 §5/§6f; Iteration 3 §16). No personal-
memory dependency found, except the soft, unresolved tension between `feedback_commit_workflow.md`'s
"single-sentence, no body" rule and `commit-boundaries.md`'s "concise title and, when useful, a short
body" — independently derived from real commit history, not reconciled by either file (Iteration 1 §6g).

#### Example/reference quality
All real-evidence citations (`#288`, `#287`, `#120`, `#289`, PR `#298`, `v0.17.0`) are consistently framed
as "the evidence this skill was extracted from," never presented as the rule itself (Iteration 3 §16) —
the cleanest citation discipline of any skill in the ecosystem.

#### Required refinement
Apply `release.md`'s own "what this repository's evidence shows" pattern to `verification.md`, now
covering both the Pest/Pint commands and the `skipUnlessFortifyHas()` mechanism.

#### What should remain unchanged
Everything except `verification.md`'s two unboxed sections — `commit-boundaries.md`, `issue-closure.md`,
`review-gates.md`, `sequencing.md`, `release.md`, and `milestone-completion.md` are all confirmed clean
across every pass that read them.

#### Current disposition
**Portable core with targeted refinement needed**, narrowly — this skill is one file's single section
away from "clean portable core," the closest any skill in the ecosystem comes to that top disposition.

---

### `my-laravel-patterns`

#### Classification
**Custom stack/ecosystem knowledge**, genuinely additive over Boost's own `laravel-best-practices` in
most of its ten rule files (Iteration 1 §3; Iteration 2 §10, verified directly against Boost's actual
file contents, not inferred).

#### Strengths
`actions-pattern.md`, `filters-pattern.md`, `request-normalization.md`, `enum-options.md`, `factories-
and-seeders.md` state real architectural decisions with no equivalent in Boost's own coverage — verified
directly, not assumed (Iteration 2 §10). `enum-options.md:41` and `resources.md:75` are models of correct
self-labeling, explicitly framing an arbitrary or conditional choice as exactly that. `SKILL.md:8`'s
explicit precedence rule ("these take precedence... when there is a conflict") is a working composition
model, present and correctly stated (Iteration 1 §3).

#### Problems
Four distinct, independently-verified problems, concentrated in different files: (1) `testing-strategy.md`'s
worked examples are non-functional without `useOrbit`'s five custom Inertia/TestResponse test macros — a
genuine functional dependency, not illustrative naming, undisclosed anywhere in the skill (Iteration 2
§10, this pass's own re-check confirms the macros exist exactly as cited and the rule file names none of
them as a prerequisite); (2) the same file's own examples use the exact assertion pattern
(`assertDatabaseHas`) Boost's own `testing.md` labels "Incorrect," recommending `assertModelExists()`
instead — an active conflict, not mere overlap, unresolved by any stated tie-break despite the skill's own
precedence rule existing to resolve exactly this (Iteration 2 §10, this pass's own re-check confirms both
sides of the conflict verbatim); (3) `query-conditionals.md`'s flagship example references `$ownerColumn`
and `$modelClass`, neither defined nor passed, and cites `App\Models\TagAttachment::forTaggableType()`, a
method this pass's own `git log` confirms was removed by `482e2d8` after the polymorphic tagging feature
it belonged to was collapsed away (Iteration 2 §10, independently reproduced by this pass); (4)
`resources.md`'s `Inertia::render()` examples contradict both `filters-pattern.md` elsewhere in the same
skill and `my-phpstorm-conventions/rules/inertia.md`'s always-co-loaded central rule that `Inertia::render()`
triggers a PhpStorm false positive and the project convention is the `inertia()` helper (Iteration 2 §10,
§11). `eloquent-attributes.md`'s core claim (`#[Scope]` over `scopeXxx`) substantially overlaps Boost's own
first-party `eloquent.md:33` recommendation — real but narrow additive value beyond Boost, not the clean
non-overlap iteration 1 originally credited the skill with (Iteration 2 §10).

#### Dependencies and overlaps
`SKILL.md`'s "load alongside, never replace" boundary with `laravel-best-practices`/`pest-testing` is
structurally clear, but — per problems (2) and (5) above — not actually conflict-free in content on
closer inspection, which iteration 1's file-level read did not surface (Iteration 2 §10). `filters-
pattern.md:5` embeds live, resolvable hyperlinks into `elieandraos/useOrbit`'s own issue tracker — a
stronger identifying fingerprint than a model name (Iteration 2 §10). `authorization.md` and `factories-
and-seeders.md` use `useOrbit`'s actual tenancy field names (`organization_id`, `current_organization_id`)
as the substance of their demonstrations without the "this project's..." separation applied elsewhere in
the same skill (Iteration 2 §10).

#### Example/reference quality
Mixed and the weakest of the two custom-stack skills: `query-conditionals.md`'s example doesn't compile
as shown and cites now-nonexistent code; `filters-pattern.md`/`testing-strategy.md`'s examples read as
lightly-cleaned verbatim snippets from real controllers (arbitrary literals like `paginate(7)`), carrying
real-code idiosyncrasies a portable version would need to deliberately re-author (Iteration 2 §10). By
contrast, `authorization.md`, `resources.md` (aside from its Inertia contradiction), `request-
normalization.md`, and `factories-and-seeders.md` read as intentionally constructed teaching examples.

#### Required refinement
State `testing-strategy.md`'s macro dependency explicitly as a prerequisite, or separate the genuinely
portable layer-ownership methodology from the macro-dependent worked examples; resolve or deliberately
document the `assertDatabaseHas`/`assertModelExists` conflict with Boost; fix or replace `query-
conditionals.md`'s broken example; reconcile the `Inertia::render()`/`inertia()` contradiction with
`resources.md`'s own sibling file and with `my-phpstorm-conventions`; decide whether `eloquent-
attributes.md` is trimmed to its narrow delta over Boost or kept as a convenience restatement.

#### What should remain unchanged
The Actions/FormRequest/Controller split, the `QueryFilter`/`Filterable` mechanism, `prepareForValidation()`
-owns-normalization, and the four-layer test-ownership *model* (as distinct from its macro-dependent
worked examples) — all independently verified as real, additive architectural decisions, not restated
Boost content (Iteration 2 §10).

#### Current disposition
**Promising stack candidate, refinement required.** This is the one scored skill where the disposition
sits closest to a genuine judgment call: the underlying authoring philosophy is sound and substantively
richer than Boost's own coverage, but the density and variety of concrete, independently-confirmed defects
in this pass (an undisclosed functional dependency, an active first-party conflict, a broken citation, and
a self-contradiction with a co-loaded sibling, all distinct in kind) is real enough that this skill should
not be read as "clean modulo cosmetics" the way `my-phpstorm-conventions` can be.

---

### `my-phpstorm-conventions`

#### Classification
**Custom stack/ecosystem knowledge** — genuinely IDE-and-framework knowledge, not project knowledge
wearing project names (Iteration 1 §3; Iteration 2 §11, confirmed on a full re-read specifically checking
for this).

#### Strengths
Every one of the six rule files documents a PhpStorm static-analysis false positive or an IDE-aware
convention whose *findings* — as distinct from their illustrative call sites — depend on nothing about
`useOrbit`'s product domain: `Eloquent::__callStatic` handling, union-typed facade method resolution, the
Pest-plugin's chained-`->and()` inspection, PHP string-interpolation brace grammar (Iteration 2 §11).
`phpdoc.md`'s IDE-helper-file technique explicitly generalizes itself in its own text ("this pattern works
for any runtime-registered methods, not just macros") — one of the few places in the ecosystem where a
file states its own generality rather than leaving it to inference. Example quality is uniformly high:
every file follows a consistent ❌/✅ or Pattern/Warning/Verdict structure, states the exact IDE warning
text, and explains the fix mechanically — no dead citation, no undefined-variable example, no
internally-contradicted example found anywhere in the skill (Iteration 2 §11).

#### Problems
The skill's actual *trigger* mechanism, not its content, is the material finding: `SKILL.md:30` names an
external tool call, `getDiagnostics`, as the enforcement step, and this pass's own re-check confirms the
instruction is exactly as iteration 2 describes, including the "no-argument call returning 'File not
found'" caveat. This tool is not among the MCP dependencies iteration 1's §5 enumerated, and its actual
provenance (JetBrains/PhpStorm-specific, or something more general) is not established by inspecting the
skill files (Iteration 2 §11). `feedback_phpstorm_skill_activation.md` (memory) independently documents
three prior real occurrences of this activation step simply not firing — evidence the mechanism is
fragile in practice, not just in theory. No file states a PhpStorm/plugin/Pest-plugin version baseline,
unlike `my-laravel-patterns/eloquent-attributes.md`'s explicit Laravel version pin, despite at least one
finding (`eloquent.md`'s `#[Scope]`-not-resolved section) describing current, not-yet-fixed IDE behavior
that JetBrains could patch at any time. The one content-level defect, `inertia.md` vs. `my-laravel-
patterns/resources.md`'s contradiction, belongs equally to both files (Iteration 2 §11).

#### Dependencies and overlaps
No overlap found with `laravel-best-practices` or `pest-testing` on a full-file read — the subject matter
(IDE static-analysis behavior) sits entirely outside what either Boost skill documents (Iteration 2 §11).
`getDiagnostics` is a real, previously-unnamed external dependency, distinct in kind from the documented
MCP servers: it is the skill's entire activation mechanism, not a workflow it merely uses.

#### Example/reference quality
Uniformly high, confirmed on a full re-read specifically checking for exactly this — the strongest example
quality of any skill in the ecosystem.

#### Required refinement
Name `getDiagnostics` as an explicit external/environment dependency with a stated fallback for a session
without it (e.g., "read the rule files before finalizing PHP files manually"); either pin a PhpStorm/
plugin-version baseline or explicitly note these findings should be periodically re-verified; fix the
one-line `inertia.md`/`resources.md` contradiction shared with `my-laravel-patterns`.

#### What should remain unchanged
All six rule files' content — zero product-domain leakage found across two independent full reads is the
strongest such finding for any skill in the ecosystem.

#### Current disposition
**Strong stack candidate, ready for Phase D consideration.** The content itself withstood a full re-read
with zero new product-domain findings; what remains is disclosure work (naming a real tool dependency,
considering a version baseline), not content repair.

---

## Mixed material synthesis

### `my-feature-planning/rules/resource-feature-checklist.md`
- **Portable:** the Track A–G skeleton itself (headings + governing questions — core infra, status
  lifecycle, sub-resource, filters/sorting, export, frontend UX consistency, wiring gotchas), and the
  framing sentence that the track *structure* is the generic rule (Iteration 1 §3; Iteration 2 §12). Every
  track name and governing question generalizes to any resource-shaped feature in any CRUD-ish web
  framework, not just Laravel/Vue (Iteration 2 §12).
- **Stack-specific:** some instantiated content genuinely belongs to the Laravel/Inertia ecosystem layer
  — "the Actions pattern," FormRequest normalization, the `wayfinder:generate --with-form` flag fact
  (Iteration 1 §3).
- **Project-specific:** the bulk of the file's actual prose — tenancy column names (`organization_id`),
  audit column names (`created_by`/`updated_by`), literal file mirrors (`app/Models/Carrier.php`,
  `BranchModal.vue`), and — most concentrated in Track F — the badge-tone palette, mobile/desktop header
  breakpoint rules, breadcrumb rule, and drop-menu ordering (Iteration 1 §4, §6b, §6g).
- **External:** none directly; the file's Laravel/Inertia terminology assumes Boost's own vocabulary is in
  scope but does not restate Boost content.
- **Is the separation currently clean?** No — this pass confirms iteration 2 §12's finding stands
  unrevised: the braiding happens *within* individual sentences (a migration line names both "a tenancy
  column" and its literal `useOrbit` name in the same clause), not between separable bullets. Track F has
  no generic sentence to extract from at all — a generic version would need to be authored new, not lifted
  by deletion.
- **Refinement likely required:** a genuine rewrite into (at minimum) a generic Laravel/Inertia answer per
  track plus a separate `useOrbit`-local reference for the mirrors/tones/breakpoints — the heaviest single-
  file lift in the ecosystem, per three iterations' agreement.

### `my-git-workflow/rules/verification.md`
- **Portable:** the entire "targeted-then-full-suite" verification methodology and the isolation-technique
  reasoning.
- **Stack-specific:** `php artisan test --compact <path>`, `vendor/bin/pint --dirty --format agent`, and
  `skipUnlessFortifyHas()` — Laravel/Pest/Fortify facts (Iteration 1 §6a; Iteration 3 §16).
- **Project-specific:** none beyond the stack-specific commands themselves — no `useOrbit` product
  reference found.
- **External:** the commands assume Pest and Pint as installed tooling, disclosed only by use.
- **Is the separation currently clean?** No — this is the one file in `my-git-workflow` that does not
  follow the pattern its own sibling file (`release.md`) already models successfully, one file over in the
  same skill.
- **Refinement likely required:** box the stack-specific commands behind a labeled "what this repository's
  evidence shows" subsection, exactly matching `release.md`'s existing, proven pattern — a template already
  exists inside this same skill.

### Project-memory overlaps inside nominally portable skills
Two named, live dependencies from `my-feature-planning` onto `useOrbit`-local personal memory:
`design-reconciliation.md:11` → `project-design-files` (no `useOrbit`-external fallback stated) and
`issue-conventions.md` → `feedback_github_issues` (self-acknowledged inline) plus a static restatement of
`feedback_github_label_colors`' live "next hue" state that can drift from the memory's actual current value
(Iteration 1 §6c, §6d; Iteration 3 §15, unchanged). Separation is not clean in either case: a GitHub
consumer of this skill without the corresponding memory entries would see the rule silently degrade rather
than fail loudly.

### Other materially mixed content found by the iterations
- `my-architecture-laboratory/SKILL.md`'s two-guide teaching precedent (§14 above) — disclosed as real,
  external, published material, but not disclosed as `useOrbit`-*specific* the way every other illustrative
  citation in the ecosystem is (Iteration 3 §17) — an anomaly in an otherwise uniform cross-skill
  self-labeling convention, not a second instance of the checklist's braiding pattern.
- `my-laravel-patterns/rules/authorization.md` and `factories-and-seeders.md` (§ above) — the *mechanism*
  taught is stack-generic, but `useOrbit`'s tenancy field names are used as the demonstration's substance
  without the "this project's..." framing applied elsewhere in the same skill (Iteration 2 §10).

---

## External capability boundary

Confirmed, unrevised across all three iterations and this pass's own spot-checks:

- **Laravel Boost skills remain externally owned.** `boost.json`'s skill set (`infer-conventions`,
  `fortify-development`, `laravel-best-practices`, `wayfinder-development`, `pest-testing`, `inertia-vue-
  development`, `echo-vue-development`, `echo-development`, `tailwindcss-development`) is upstream-
  maintained and mirrored identically in `.junie/skills/`, confirming it is IDE-agnostic, vendor-
  distributed content, not `useOrbit`- or Claude-Code-authored (Iteration 1 §1.2, §5).
- **Custom skills compose with Boost, correctly, in most places.** Both `my-laravel-patterns` and
  `my-phpstorm-conventions` state "load alongside, never replace" explicitly, and this pass's own
  re-checks confirm no wholesale restatement of Boost content in either skill (Iteration 1 §5; Iteration 2
  §10/§11).
- **Boost content is not extracted or duplicated at the skill-structure level**, but this pass's
  independent re-verification confirms two real exceptions at the *rule* level, not the structural level:
  `eloquent-attributes.md` substantially overlaps Boost's own `#[Scope]` guidance, and `testing-
  strategy.md` actively contradicts Boost's own `assertModelExists()` recommendation (Iteration 2 §10,
  both confirmed verbatim by this pass). Neither is duplication of Boost's *skill*, but both are
  unreconciled disagreement or overlap at the *content* level within a skill that explicitly claims a
  precedence rule for exactly this situation.
- **Conflicts are not yet handled through the stated precedence rule** — `my-laravel-patterns/SKILL.md:8`'s
  "these take precedence... when there is a conflict" rule is stated but was never applied to the
  `assertDatabaseHas`/`assertModelExists` disagreement, because — per iteration 2's own framing — nobody
  had identified the conflict existed to apply the rule to. This is the clearest evidence-backed instance
  in the ecosystem of the "explicit precedence/composition rules rather than silent duplication" principle
  existing on paper but not yet being exercised in practice.

---

## Cross-skill architecture

The three-skill portable lifecycle (`my-architecture-laboratory` → `my-feature-planning` → `my-git-
workflow`) remains, across three independent passes of increasing depth, the single most consistently
reconfirmed finding in this entire discovery phase:

- Iteration 1 (§6h): each skill's README "owns/does not own" sections are matched, cross-references are
  directional, no overlap found on a full read.
- Iteration 2: did not re-touch the boundary directly, but found nothing in its stack-skill deep-dive that
  implicated the three-skill decomposition.
- Iteration 3 (§17): a full fresh read of all three skills' README boundary statements side by side found
  zero new instance of one skill silently performing another's job — no issue drafting inside
  `my-architecture-laboratory`, no architecture re-derivation inside `my-feature-planning`, no issue
  creation inside `my-git-workflow`.

**This synthesis's own assessment: the decomposition remains coherent.** The only evidence-backed boundary
issue found across all three iterations is narrow and disclosure-shaped, not structural: `my-feature-
planning` relies on `plan.md` section pruning as an established practice it observed historically, while
`my-architecture-laboratory` — which now owns `plan.md`'s lifecycle end-to-end — never states pruning as
something it performs (Iteration 3 §17). Neither skill actively contradicts the other; this is an
assumption one skill depends on that the other has not yet formally committed to sustaining. Per this
pass's own constraint, this synthesis does not redesign the three-skill family or prescribe where pruning
responsibility should land — it only records that the gap exists and is real.

---

## `content-backlog`

**Current evidence.** A genuinely owned, mature skill (5 rule files: `formats.md`, `capture.md`,
`backlog-file.md`, `suggestions.md`, `content-strategy.md`), backing a real, actively-used 1,432-line
tracked file (`content-backlog.md`, confirmed by this pass's own `wc -l`, growing from the 96 KB/22-entry
snapshot iteration 1 recorded — evidence of continued real use since Phase C began, not a stale artifact).
It is not `my-`-prefixed, not present in `boost.json`, and `roadmap.md` itself names it as "a possible
Agentic Engineering capability, potentially independent of stack work" (confirmed verbatim by this pass's
own read of `roadmap.md` line 415) — a decision already deferred by the roadmap's own authors, not one
this synthesis is introducing.

**Why it does not yet fit the three-layer classification.** Its content is personal-brand/authorial
material about the user's own public engineering-communication practice, not `useOrbit`'s application
domain (ruling out "`useOrbit`-specific"), not a Laravel/Vue/Inertia/tooling convention (ruling out
"custom stack knowledge"), and not a project-delivery methodology like architecture/planning/git-workflow
(a looser fit for "portable methodology" than the other three skills, even though some individual rules —
e.g. a capture-discipline pattern — might generalize). Several of its own tracked entries are explicitly
*about* the `agentic-engineering` methodology-development process itself (Iteration 1 §1.4) — its
filesystem location inside `useOrbit/.claude/skills/` is an accident of where the user's Claude Code
session happens to run, not evidence the content belongs to `useOrbit` the product.

**What this pass adds.** Nothing that resolves the category question — this pass's own file-existence and
line-count check confirms the skill remains real, mature, and growing, which if anything strengthens the
case that it deserves its own resolved category eventually, not that it fits an existing one now.

**What evidence would be needed to resolve this later.** A close read of the five rule files themselves
(not performed by any of Iterations 1–3, and not performed by this synthesis pass, since Phase C's
existing evidence already establishes the category question as unresolved and this pass's job is to
consolidate, not to open new file-level analysis); a decision on whether "personal-brand content
methodology" is itself a fourth durable category `roadmap.md` should name, or whether specific rules
within it turn out to be a genuinely portable capture/triage discipline separable from its authorial
subject matter; and, if Phase D ever considers it, cross-project evidence this single-consumer discovery
phase cannot supply (the same limitation Iteration 1 §8.8 already named for the stack skills).

**Disposition:** deferred, category unresolved, outside current Phase D stack scope — exactly as
`roadmap.md` itself already frames it. Not extracted, not scored, not assigned to portable core or stack
layer merely to complete the taxonomy.

---

## Phase D entry conditions

This section states conditions, not a plan. Per `roadmap.md` §5, Phase D may result in refinement without
extraction, one reusable stack capability, several cooperating capabilities, combining or splitting
skills, returning project-specific material to `useOrbit`, leaving skills unchanged, or a decision that
extraction is not yet justified — none of these outcomes is assumed or ruled out here.

**Refinements this evidence suggests addressing before or as part of any extraction:**
- `my-architecture-laboratory`: repair or replace the dead Tagging-guide citation (a live, content-verified
  replacement now exists, per this pass's own check); address `template.html`'s language-specific
  highlighter; name the unlinked "CRUD guide" citation (also now content-verified by this pass).
- `my-feature-planning`: the `resource-feature-checklist.md` content split (the heaviest lift identified by
  any iteration); `SKILL.md` step 18's inline Laravel vocabulary; a decision on the two named memory
  dependencies.
- `my-git-workflow`: box `verification.md`'s two stack citations using `release.md`'s own already-proven
  pattern.
- `my-laravel-patterns`: disclose or resolve `testing-strategy.md`'s macro dependency; resolve the
  `assertDatabaseHas`/`assertModelExists` conflict with Boost (a real, standing disagreement, not
  cosmetic); fix `query-conditionals.md`'s broken example; reconcile the `Inertia::render()`/`inertia()`
  contradiction with `my-phpstorm-conventions`.
- `my-phpstorm-conventions`: name `getDiagnostics` as an explicit, environment-specific dependency with a
  stated fallback; consider a version baseline.

**Which skills are mature enough to consider first.** `my-phpstorm-conventions` (8.2) and `my-git-workflow`
(7.3) carry the narrowest, most disclosure-shaped gaps of the five — their content itself is not in
question, only what needs to be stated more explicitly. `my-architecture-laboratory` (6.8) is close behind
but its refinement is more consequential (a foundational citation, not just a disclosure line).
`my-feature-planning` (6.3) and `my-laravel-patterns` (5.8) need more substantial, evidence-dense work
before either is in the same state of readiness — the checklist split and the macro/Boost-conflict
disclosure respectively are not quick edits.

**Mixed rules needing separation.** `resource-feature-checklist.md` above all — evidence-dense, agreed
across three iterations to require a rewrite rather than a mechanical extraction. `verification.md` is a
much smaller, already-modeled version of the same class of problem.

**Dependencies needing disclosure or decoupling.** `testing-strategy.md`'s test macros; `getDiagnostics`'
actual identity and fallback behavior; `gh`/GitHub as a first-class, named dependency distinct from Boost
or the `Artifact` tool (Iteration 3 §15/§16/§20 names this gap but does not close it).

**Evidence gaps that remain.** Whether `my-laravel-patterns` and `my-phpstorm-conventions` should become
one skill or two (Iteration 1 §8.2) — this pass found no new evidence either way, and if anything iteration
2's finding that their two most consequential problems sit on opposite sides of that seam is itself
ambiguous evidence, arguable either way. Whether within-project repetition is sufficient grounds for calling
something "reusable" absent cross-project evidence (Iteration 1 §8.8) — unresolved by a single-consumer
discovery phase by construction. `content-backlog`'s category, as detailed above.

**Where human architectural judgment is still required, not inferable from files alone.** Whether the
`assertDatabaseHas`/`assertModelExists` conflict and the `Inertia::render()`/`inertia()` conflict are
things the user wants reconciled now or only at extraction time (Iteration 2 §13); whether the
`feedback_commit_workflow.md`/`commit-boundaries.md` commit-body-line tension is live or scoped away by
`commit-boundaries.md`'s own pipeline (Iteration 1 §8.5); whether `my-laravel-patterns` +
`my-phpstorm-conventions` combine; whether `content-backlog` ever gets a fourth category.

**What Phase D is not compelled toward by this evidence.** Nothing here requires a `skills/portable-core/`,
`skills/stack-adapters/`, or `skills/project-specific/` directory structure, a single unified adapter, or a
ground-up rewrite of any skill. Every finding across all three iterations and this synthesis is contained
within existing file boundaries — a citation, a template, a section, a link, a disclosure line — except
`resource-feature-checklist.md`, which is the one place the evidence itself (not this pass's preference)
points to something closer to a rewrite.

---

## Phase C conclusion

**1. What did Phase C establish with high confidence?** The five named `my-*` skills plus the
independently-discovered `content-backlog` are the complete set of genuinely owned, mature custom skills.
The three-skill portable lifecycle decomposition is sound, reconfirmed across three passes of increasing
depth with only one narrow, disclosure-shaped boundary gap (`plan.md` pruning ownership). No skill in the
ecosystem has yet earned an unqualified "clean" verdict, and every skill's readiness gaps are, on the
evidence gathered, targeted and containable rather than structural — with `resource-feature-checklist.md`
as the one clear exception requiring a genuine rewrite rather than a targeted fix. This synthesis's own
independent re-verification (the artifact re-fetches, the source-code and git-history spot-checks) found
every load-bearing claim in Iterations 1–3 to hold up, and additionally resolved two of iteration 3's own
open questions (the live Tagging artifact's current content; the CRUD guide's identity) in the direction
those iterations already inferred.

**2. Which skills are currently strongest?** `my-phpstorm-conventions` (8.2) — zero product-domain leakage
across two full reads, only disclosure gaps remain. `my-git-workflow` (7.3) — the lightest lift, with
`release.md` standing as the ecosystem's model file.

**3. Which skills are not ready?** None scores below the "mixed, substantial refinement" band, but
`my-laravel-patterns` (5.8) is the weakest of the five scored skills — not because its underlying
philosophy is unsound, but because it carries the densest, most varied cluster of concrete, independently-
confirmed defects (an undisclosed functional dependency, an active Boost conflict, a broken citation, and
a self-contradiction with a sibling skill) of any skill examined.

**4. What major boundary problems remain?** `resource-feature-checklist.md`'s generic/`useOrbit`-specific
braiding, requiring a rewrite rather than an extraction. Two named personal-memory dependencies inside
`my-feature-planning`. `my-architecture-laboratory`'s dead foundational citation, now resolved in
disposition (a live replacement exists and was independently verified) but not yet repaired in the skill
file itself. The unreconciled `assertDatabaseHas`/`assertModelExists` and `Inertia::render()`/`inertia()`
conflicts between custom skills and Boost, and between two custom skills, respectively.

**5. What should Phase D examine first?** Whichever refinement work the user chooses to prioritize is
their call, not this pass's — but the evidence base is most mature (narrowest remaining unknowns) for
`my-phpstorm-conventions` and `my-git-workflow`, and least mature (most work needed before the picture is
settled) for `resource-feature-checklist.md`'s split and `my-laravel-patterns`' macro/Boost-conflict
disclosure.

**6. What remains genuinely unresolved?** `content-backlog`'s category. Whether `my-laravel-patterns` and
`my-phpstorm-conventions` become one skill or two. Whether the two named content conflicts (Boost/testing,
Inertia-call-style) are live problems the user wants fixed now or only at extraction time. Whether
within-project repetition is sufficient evidence for "reusable" absent cross-project confirmation, for any
of the stack-layer candidates. The `feedback_commit_workflow.md` soft conflict. Every one of these is a
**fact-plus-judgment** pairing this synthesis deliberately leaves open rather than silently resolving: the
facts are established (cited above, several independently re-verified by this pass); the judgment calls
belong to the user or to Phase D, not to a synthesis pass.

---
