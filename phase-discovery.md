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
