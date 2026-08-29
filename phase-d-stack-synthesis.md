# Phase D — Stack Synthesis

This document converts `phase-d-stack-discovery.md`'s evidence into decisions. It is a synthesis and
decision artifact only: no skill was edited or created, no `.ai/rules` file was created, no runtime
code was installed, no Composer package was created, and no file was renamed to produce this document.
See `roadmap.md` §5 for Phase D's charter, `phase-discovery.md` for the original Phase C classification,
and `phase-d-stack-discovery.md` for the reconciliation this synthesis acts on.

This document does not restate discovery's evidence ledger, source reads, or per-file Boost-overlap
analysis — it cites `phase-d-stack-discovery.md` by section (`§n`) wherever a decision rests on a
specific finding, and states only the decision, the boundary, or the deferral.

---

## 0. Locked direction, restated as constraints on this synthesis

Carried over verbatim from the task, not re-derived:

- The companion targets **Laravel + Vue 3 + InertiaJS specifically**; Laravel Boost remains the
  broader Laravel baseline.
- `my-phpstorm-conventions` stays a **separate** IDE/tooling companion.
- The Laravel/Inertia companion is refined around only what is **genuinely additive** to Boost.
- `.ai/rules` adoption in `useOrbit` is a real, available target for settled, team-visible
  conventions — but is **not created in this pass**.
- **No Composer package yet.** This synthesis recommends the smallest reversible initial
  distribution mechanism and states what would justify packaging later.
- `QueryFilter`/`Filterable` stay a **documented pattern** projects re-implement locally, unless
  stronger evidence or a later human decision promotes them.
- `assertDatabaseHas()` is **not** preserved as a universal override of Boost's `assertModelExists()`
  default — assertion choice follows what the test needs to prove.
- "Do not test framework behavior" is preserved but **narrowed accurately**: no retesting of Laravel,
  Pest, or Inertia internals; do test project-owned configuration, composition, integrations, macros,
  and contracts where failure would affect the application.
- Nothing here silently publishes project rules or installs runtime code — every adoption/bootstrap
  action is explicit and reviewable, performed in a later, dedicated stage (§7).

---

## 1. Target architecture — five boundaries

| Owner | Owns | Must never contain | Delivery mechanism | Portability |
|---|---|---|---|---|
| **Laravel Boost v2.7.0** | The general Laravel ecosystem baseline: validation, Eloquent mechanics, routing/controller-organization philosophy, general Action/business-operation naming philosophy, migrations, security, style, general testing mechanics and assertion decision tables. | Any concrete, project-specific contract for a pattern it only names generally (see `[[phase-d-stack-discovery]]` §7.2). | Vendor package (`vendor/laravel/boost`), Boost's own skills + `CLAUDE.md` injection. | External dependency — never extracted, renamed, or duplicated (roadmap.md §5 constraint). |
| **Laravel/Inertia companion** (name: §6) | The concrete, portable authoring delta specific to a Laravel-backend-serving-Inertia application: this user's Action/Resource/Authorization/Filter/testing-layer contracts, where Boost states no contract or a materially different one. | Restatement of anything Boost already documents at the mechanics level (e.g. `#[Scope]`'s own syntax); runtime code; `useOrbit` product facts. | Task-triggered `SKILL.md` + `rules/*.md`, always loaded alongside the relevant Boost skill(s) (§1.1 of discovery). | Personal, travels across this user's projects by copy/reinstall; invisible to `useOrbit` teammates (gitignored). |
| **`my-phpstorm-conventions`** | IDE/tooling knowledge: PhpStorm static-analysis false positives and PhpStorm-aware coding conventions, plus the `getDiagnostics` prerequisite check. | Laravel/Inertia authoring conventions that aren't about how the IDE parses code; product facts. | Task-triggered `SKILL.md` + `rules/*.md`, loaded alongside the Laravel/Inertia companion and/or Boost skills. | Personal, same portability profile as the companion above — kept as a **separate** skill per locked direction because its axis of variation (IDE behavior) is orthogonal to the axis the companion varies on (stack authoring conventions). |
| **`useOrbit` `.ai/rules`** | Settled decisions, non-obvious traps, and standing constraints whose evidence and value are currently scoped to `useOrbit` — even if plausibly true elsewhere, not yet shown to recur (discovery §2). | Anything that is actually a portable authoring pattern with no `useOrbit`-specific evidentiary limit — that belongs in the companion instead. | `record-rule` MCP tool → `.ai/rules/<area>.md`, loaded via `useOrbit/CLAUDE.md`'s injected "Project Rules" instruction (discovery §1.2). | Team-visible within `useOrbit` only — committed, not gitignored, but has no cross-project publication mechanism at all. |
| **Reusable executable support** | Runtime PHP code an instruction file cannot substitute for. Today, exactly one capability: the five `TestingServiceProvider` Inertia-testing macros. | Anything documentable as prose alone (that's companion workflow knowledge instead); `QueryFilter`/`Filterable` base classes, per locked direction, stay out of this category for now. | Undecided in general (discovery §1.3); this pass recommends a specific initial mechanism for the macros only (§5). | Requires the code itself to travel — mechanism chosen in §5. |
| **`useOrbit`-specific knowledge** | Product/design-system facts with no cross-project generality claim (badge tones, breadcrumb rules, literal issue links, arbitrary literals like `paginate(7)`). | Nothing structural — this category is a sink, not a home to build on. | `useOrbit`'s own `_docs/`, or `.ai/rules` if a decision is settled enough — decided by `useOrbit`'s own maintainers, not `agentic-engineering`. | Out of `agentic-engineering` scope entirely. |

A pattern's **ownership** (which row it belongs to) is separate from its **mechanism** (which row's
"Delivery mechanism" column applies) — a rule can be owned by `.ai/rules` and *also* be worth stating
briefly in the companion once cross-project evidence exists; ownership decides where the durable
version of the fact lives today.

---

## 2. File-by-file disposition

Legend: **keep** (no content change) · **repair** (fix a defect, no scope change) · **narrow**
(reduce to the Boost delta) · **→ `.ai/rules`** (recording is a separate, gated action — see §4) ·
**→ executable support** (see §5) · **project-specific** (belongs to `useOrbit`, not this repo) ·
**remove** (duplicated/obsolete).

### 2.1 `my-laravel-patterns`

| File | Disposition | Reasoning |
|---|---|---|
| `SKILL.md` | **repair** | Names the retired Boost skill `pest-testing` instead of `testing-best-practices` (discovery §8.11, Tier 1 #1). Also gains one addition: the description/quick-reference should name the `TestingServiceProvider` macros as a prerequisite the skill assumes exists (§5), not just cite them as fact. |
| `rules/actions-pattern.md` | **narrow** | Boost's `architecture.md`/`routing.md` now name the general Action pattern (discovery §7.2). Trim the philosophy framing ("why Actions exist at all"); retain the concrete contract Boost doesn't define: `app/Actions/{Domain}/` location, `{Verb}{Model}Action` naming, fixed `handle()` method name, fixed `$attributes` parameter name, the FormRequest-derived `@param array{...}` shape algorithm, and the `DB::transaction()`-pure / `->afterCommit()` discipline. |
| `rules/authorization.md` | **keep** | Zero Boost coverage of the `#[Authorize]` attribute mechanism at all (discovery §8.4) — the strongest single keep in the file set. Keep the portability claim and the 35-controller adoption claim stated as two distinct pieces of evidence, not merged into one "strongest keep" framing (discovery already corrects this; carry the correction into the next authoring pass). |
| `rules/eloquent-attributes.md` | **narrow** | Boost's `eloquent.md` already demonstrates `#[Scope]` with `protected` visibility, the attribute import, and a `Builder`-returning method named after the scope — the base mechanics are Boost-owned by example even though Boost doesn't narrate them as an explicit rule. Reduce this file to the actual delta: the migration framing (why this project moved off `scopeXxx`), the `❌ scopeXxx` counter-example (a project-specific "don't regress" warning, not a Boost topic), and the Laravel version pin (`^13.7`). Drop the parts that just restate `#[Scope]`'s own syntax. |
| `rules/enum-options.md` | **keep, caveated** | No Boost overlap found. Not independently re-audited against live code in this or the discovery pass (discovery §8.2) — carry that caveat forward; this is a "no evidence against" keep, not a freshly confirmed one. |
| `rules/factories-and-seeders.md` | **keep, caveated** | Narrow overlap only (Boost's `test-data.md` endorses `for()` generally; the field-derivation/email/date-chaining content has no Boost equivalent). Not independently re-audited this pass (discovery §8.3) — same caveat as above. |
| `rules/filters-pattern.md` | **repair** | The pattern documentation (FormRequest → `QueryFilter` → `Filterable` wiring) has no Boost overlap and stays companion workflow knowledge. Repair required before this file is fit to travel: scrub the live `useOrbit` issue links (`#76`, `#71`) and the arbitrary `paginate(7)` literal (discovery §8.7) — these are `useOrbit` fingerprints, not part of the pattern. The `QueryFilter`/`Filterable` **base classes themselves stay a documented pattern each project re-implements locally** per locked direction §0 — not promoted to executable support in this pass. |
| `rules/query-conditionals.md` | **repair** | Broken example and a dead `TagAttachment::forTaggableType()` citation (discovery §8.10, Tier 1 #3); the underlying `when()`-over-`if` rule needs no content change. |
| `rules/request-normalization.md` | **keep, caveated** | No Boost overlap (Boost's `validation.md` covers rule syntax, not coercion/defaulting discipline). Checked only for internal consistency with `filters-pattern.md` in discovery, not against live FormRequest code (discovery §8.8) — same "not freshly re-audited" caveat. |
| `rules/resources.md` | **repair** | Its own cited example (`ClientsController.php`) uses `inertia()` throughout; the file's `Inertia::render()` examples are internally inconsistent with it and with `filters-pattern.md` (discovery §6.2, §8.5, Tier 1 #2). Fix is a same-skill/cross-skill consistency correction — `Inertia::render()` is not being declared invalid. The `whenLoaded()`/no-`$with` discipline itself has no Boost overlap and is unchanged. |
| `rules/testing-strategy.md` | **repair + split ownership** | Two things land differently: (1) The layer-ownership mapping (Action/Controller/Policy/Filter) and the no-duplication discipline is companion workflow knowledge — trim the now-Boost-stated general layer-ownership principle (`endpoint-tests.md`), keep the concrete mapping. (2) The five macros this file assumes exist are reusable executable support, not documentable content — state that dependency explicitly as a prerequisite pointing at §5, not as an unexplained fact. (3) **Resolved per locked direction:** the `show`-endpoint row's blanket `assertDatabaseHas('clients', ['slug' => $client->slug])` is removed as a required step — `assertHasResource()` already proves the resource's data (including any field it exposes) reached the response, which subsumes a plain existence/column check on those same fields. Restate the guidance as: default to Boost's `assertModelExists($model)` when only existence needs proving; reach for `assertDatabaseHas()` only when asserting a column value the resource assertion doesn't cover (e.g. a soft-delete flag or an internal field never serialized) — a meaningful persistence distinction, not a blanket per-endpoint step. |

### 2.2 `my-phpstorm-conventions`

| File | Disposition | Reasoning |
|---|---|---|
| `SKILL.md` | **repair** | States the `getDiagnostics` prerequisite with no behavior for its absence (discovery §6.3, §10, Tier 2 #5). Add: "if no `mcp__ide__getDiagnostics` tool is available in this session, state that IDE diagnostics were not run and proceed on the written rules alone" — name the dependency and its fallback, don't assume the tool is present. |
| `rules/eloquent.md` | **keep** | Zero Boost overlap (IDE static-analysis mechanics, not Laravel conventions); zero `useOrbit` product-domain leakage across two independent reads (discovery §10). |
| `rules/inertia.md` | **keep** | This file is the reason `resources.md`'s fix (§2.1) is correct: it already documents `Inertia::render()`'s PhpStorm false positive as the motivation for preferring the `inertia()` helper. No change needed — once `resources.md` is repaired, the two files agree. |
| `rules/pest.md` | **keep** | IDE-mechanics only, no Boost or product overlap. |
| `rules/phpdoc.md` | **keep** | Includes the `_ide_helper_macros.php` stub pattern for resolving macros PhpStorm can't see statically — this is the natural doc anchor for a future IDE-visibility fix to the Inertia-testing macros once distributed (§5), not something to change now. |
| `rules/pivot.md` | **keep** | `useOrbit`-agnostic IDE mechanics. |
| `rules/strings.md` | **keep** | `useOrbit`-agnostic IDE mechanics. |

---

## 3. Companion workflows, activation boundaries, and why a skill is still justified

**Activation model, unchanged from current practice:** both companions remain task-triggered,
always co-loaded with a Boost skill, never standalone — the Laravel/Inertia companion with
`laravel-best-practices` and/or `testing-best-practices`; `my-phpstorm-conventions` with either or
both companions whenever a PHP file is being finalized. Each skill's own `SKILL.md` "How to Apply"
section is the correct place for this — no change to that model.

**Why a task-triggered skill, not `.ai/rules`, for this material:**

1. **Portability.** A companion skill travels with the user across every Laravel+Vue+Inertia project
   by copy/reinstall; `.ai/rules` is bound to one repository with no cross-project publication
   mechanism at all (discovery §1.2). The locked direction is explicit that this companion targets
   the Laravel+Vue+Inertia *combination*, not `useOrbit` specifically — a repo-bound mechanism cannot
   serve that goal.
2. **Content shape.** `.ai/rules` accumulates by simple markdown append per area file, with no
   dedup or editing UI (discovery §1.2) — adequate for a handful of settled facts, not for a
   ten-topic pattern language with worked examples, tables, and cross-file references that gets
   actively reorganized as evidence changes (as this very synthesis just did to three files).
3. **What each mechanism is actually for.** `.ai/rules` is for a settled decision or standing
   constraint discovered once, in one project. The companion's content is closer to a personal house
   style meant to be reproduced *before* a team decision exists on a new project — categorically
   different from "this team decided X."
4. **They compose, not compete.** A fact can start in `.ai/rules` (single-project evidence) and later
   graduate into the companion once cross-project recurrence is shown (§4 does this explicitly for
   the `final`-by-default policy) — the two mechanisms serve adjacent points on the same evidentiary
   timeline, not the same job at different scopes.

None of this replaces the case for using `.ai/rules` where it fits (§4) — it explains why doing so
does not make either companion skill redundant.

---

## 4. Proposed `useOrbit` `.ai/rules` set

**Not created in this pass.** Each row is ready to record via `record-rule` *once* the user approves
adopting `.ai/rules` as a practice for `useOrbit` at all (discovery §15) — a separate go/no-go this
document does not make on the user's behalf. If approved, record rules one at a time and verify
`.ai/rules/index.md` regenerates correctly after each (discovery §1.2).

| Rule | Purpose | Path/glob scope | Source | Boost precedence/tension | Status |
|---|---|---|---|---|---|
| `final`-by-default PHP classes | Every new PHP class (Model, Action, Controller, Middleware, Policy, FormRequest) is declared `final` unless inheritance is required. | `app/**/*.php` | `feedback_final_classes.md` (memory), confirmed against 11/11 current `app/Models/*.php`; absent from all 19 `laravel-best-practices` rule files (discovery §11.3). | None — Boost is silent on a default `final` policy. | **Ready to record.** Whether this *also* becomes companion workflow knowledge is a separate question, gated on evidence from a second project (§8). |
| No dedicated tests for pure framework scaffolding | Narrowed per locked direction §0: don't write a test whose only job is confirming a Laravel/Pest/Inertia internal (an `casts()` enum mapping resolving, `Relation::enforceMorphMap()` resolving, a one-line passthrough relation with no added constraint). Do test project-owned configuration, composition, integrations, macros, and contracts a failure would actually affect — e.g. a relation *with* a constraint, a cast whose *mapping* is project logic, a scope. | `tests/**/*.php` | `feedback_no_tests_for_framework_behavior.md` (memory), incident-backed (issue #107). | **Resolved, not a tension.** Boost's `testing-best-practices/rules/review.md` reads "no test asserts the behavior of the framework... a relation *with a constraint*, a cast, or a scope[,] belongs to this project" — that qualifier ("with a constraint") already narrows to the same boundary this rule states. Discovery §11.4/§15 flagged this as an open conflict under the memory's broader, unqualified phrasing; narrowing the rule's wording resolves it rather than leaving it as a Boost-vs-custom standoff. | **Ready to record**, with the narrowed wording above — not the memory file's original broader phrasing. |
| Migration `->notNull()` does not exist | `->notNull()` is not a method on `ColumnDefinition`; PhpStorm's warning is correct. Columns are `NOT NULL` by default — omit the constraint, don't add a nonexistent one. | `database/migrations/**` | `feedback_migration_notnull.md` (memory), single incident. | None — not covered by Boost's `migrations.md`. | **Ready to record.** Too narrow and too mechanical for a skill rule file an agent reads on every relevant task — the canonical `.ai/rules` shape (a "non-obvious trap"). |

Two items discovery raised alongside these are **not** included as `.ai/rules` candidates, resolved
here rather than left open:

- **`QueryFilter`/`Filterable` base classes** — per locked direction §0, these stay a documented
  pattern (companion skill), not a settled `useOrbit` decision needing `.ai/rules`, and not (yet)
  executable support.
- **Enum `::all()` convention** — discovery §15 grouped this with the base-classes question, but it
  doesn't actually fit either "documented pattern vs. executable support" framing: each enum
  implements its own `all()` method independently (there is no shared base class or trait to
  distribute) — it's a naming/shape convention, structurally incapable of becoming reusable executable
  support. It stays companion workflow knowledge with no open promotion question.

---

## 5. Runtime-support model — the Inertia testing macros

**What code belongs to it.** Exactly the five macro registrations in
`app/Providers/TestingServiceProvider.php`'s `boot()` method: `AssertableInertia::macro('hasResource', ...)`,
`AssertableInertia::macro('hasPaginatedResource', ...)`, `TestResponse::macro('assertHasResource', ...)`,
`TestResponse::macro('assertHasPaginatedResource', ...)`, `TestResponse::macro('assertHasInertiaFlash', ...)`,
plus the `runningUnitTests()` boot guard and the class's own `@method` docblock. Nothing else —
`QueryFilter`/`Filterable` is explicitly excluded from this category (§0, §4).

**Smallest reversible initial distribution mechanism.** A skill-bundled installable file, not a
Composer package and not a bare copy-paste instruction with no canonical source:

- The companion skill directory carries the provider file verbatim (e.g.
  `my-laravel-inertia-patterns/support/TestingServiceProvider.php` — exact location decided at
  authoring time, not here) as the single source of truth for what gets installed.
- When a project needs these macros for the first time, the companion instructs the agent to copy
  that bundled file into the target project's `app/Providers/` and register it in
  `bootstrap/providers.php` — an explicit, reviewable action the agent takes once per project, not an
  automatic install.
- This is chosen over a Composer package because it requires no registry, versioning scheme, or
  publish step, and it is maximally reversible: deleting the copied file and its provider-array entry
  removes the capability cleanly, with no dependency-graph entanglement to unwind. It is chosen over
  an undocumented "copy this snippet" instruction because the bundled file is a single canonical copy
  the skill carries, not prose an agent has to faithfully retype.

**How the companion detects whether it is installed.** A prerequisite check, per §1.1's own stated
responsibility (name the dependency, state what to do in its absence): before writing or editing a
test that calls `assertHasResource`, `assertHasPaginatedResource`, or `assertHasInertiaFlash`, the
agent checks for `app/Providers/TestingServiceProvider.php`'s macro registrations and confirms the
class is listed in `bootstrap/providers.php`. If either is missing, install from the bundled file
first rather than assuming the macros exist or hand-rolling an equivalent assertion inline.

**Provenance/update expectations.** The bundled file inside the companion skill is authoritative;
copying it into a project takes a snapshot, not a live link — a later fix to the bundled macros does
not propagate to a project that already copied them. This is the actual cost of choosing copy over a
package, named plainly rather than glossed over. This pass does not design a drift-detection
mechanism (e.g. a version comment in the file, diffed on each companion load) — that is future work,
triggered by the packaging evidence below if it doesn't arrive first.

**What would justify packaging later:**

- The macros are actually copied into and exercised in a **second** real Laravel/Inertia project —
  crossing the one-consumer ceiling this entire document is bounded by (§8).
- A bugfix or feature addition to the macros needs to reach already-consuming projects without manual
  re-copying — i.e. update propagation becomes a live, recurring cost rather than a hypothetical one.
- The capability's surface grows enough (more Inertia-testing helpers, configuration options) that a
  single copied file stops being trivially auditable and reversible.
- The user separately decides to publish this as a standalone open-source or personal Composer
  package as its own deliberate project — a package name, namespace, and vendor choice are explicitly
  out of scope here, exactly as they were out of scope for discovery (§9, §14.10).

---

## 6. Naming options for the Laravel/Vue/Inertia companion

Not renamed in this pass. Evaluated on retained responsibility — what the skill's files actually
contain after §2's dispositions — not on how broad or marketable a name sounds.

| Option | Assessment |
|---|---|
| `my-laravel-inertia-patterns` (**recommended**) | Matches the file set as it actually stands after §2: every retained rule file is either backend-Laravel content (Actions, Filters, Resources, Eloquent attributes, factories, enums, request normalization, query conditionals) or the server-side Inertia response/testing boundary (`resources.md`'s `inertia()` convention, the Inertia-testing macros). No file in the current set states a Vue-component-level convention. Naming it "Inertia" rather than "Vue" is honest about where the actual delta currently lives, and still signals the Boost-delta narrowing (away from "Laravel" in general) that motivates a rename at all. |
| `my-laravel-vue-inertia-patterns` | Matches the locked target combination exactly, but currently overclaims: it would promise Vue-specific content (component conventions, composables, props typing) that no file in this skill provides today. Worth revisiting if genuine Vue-frontend rules are added later with real evidence — not before. |
| `my-laravel-patterns` (status quo) | The current name overclaims in the other direction — it reads as "Laravel" in general, which is exactly the baseline Boost already owns (discovery §0). Keeping it risks the skill silently drifting back toward restating Boost rather than staying scoped to the delta. |
| `my-inertia-app-patterns` | Drops "Laravel" entirely, which misrepresents the file set — nine of ten retained rule files are Laravel-backend content with only an incidental Inertia touchpoint, not Inertia-first content. |

**Recommendation: `my-laravel-inertia-patterns`.** It is the name that best matches what the skill
will actually contain once §2's narrowing is applied, without promising Vue coverage that doesn't
exist yet or Laravel-general coverage that Boost already owns.

---

## 7. Staged implementation sequence

Each stage is independently coherent; later stages depend on earlier ones, not the reverse.

1. **Correctness and stale-reference fixes** (discovery Tier 1 — no design decision required):
   rename `pest-testing` → `testing-best-practices` in both `SKILL.md` files; reconcile
   `resources.md`'s `Inertia::render()` examples to `inertia()`; fix or replace
   `query-conditionals.md`'s broken example and dead `TagAttachment` citation.
2. **Companion authoring pass** (`my-laravel-patterns`, pending the §6 rename decision): apply §2.1's
   narrow/repair dispositions — trim `actions-pattern.md` and `eloquent-attributes.md` to their Boost
   deltas, scrub `filters-pattern.md`'s `useOrbit` fingerprints, resolve `testing-strategy.md`'s
   `assertDatabaseHas`/`assertModelExists` guidance per §2.1's rewrite, and state the macro dependency
   as an explicit prerequisite pointing at §5 (not yet bootstrapped — that's stage 5).
3. **`my-phpstorm-conventions` authoring pass**: add the `getDiagnostics`-absence fallback to
   `SKILL.md` (§2.2). No other content changes identified.
4. **Explicit `useOrbit` `.ai/rules` adoption** — gated on a separate human approval to start using
   `.ai/rules` at all (§4). If approved, record the three rules in §4 one at a time via `record-rule`,
   verifying `index.md` regenerates correctly after each. This stage can run independently of stages
   2–3; it does not wait on the companion-skill rename or content pass.
5. **Runtime-support bootstrap**: create the bundled `TestingServiceProvider` stub inside the
   companion skill directory (§5), verified byte-for-byte against `useOrbit`'s real implementation;
   author the prerequisite-check instructions that reference it.
6. **Refresh into `useOrbit`**: update `useOrbit`'s own gitignored `.claude/skills/my-*` copies to
   match the newly authored `agentic-engineering` versions — the same consume/refresh mechanism
   already used for the three portable methodology skills, not a new one.
7. **Real consumer exercise**: use the refreshed companion and the bootstrapped runtime support on an
   actual piece of `useOrbit` work (a new controller/action/test) to confirm the rewritten rules and
   the bundled macro file work end-to-end — including confirming the prerequisite check in stage 5
   actually fires if the provider were ever missing.
8. **Dossier, README, and roadmap reconciliation** — only after stage 7's verified progress, matching
   this repository's own established practice of reconciling documentation after real exercise, not
   ahead of it (see the commit history's `f0f4817`/`24b288c` pattern). Not performed in this pass.

---

## 8. Non-goals and confidence limits

**Explicit non-goals of this pass:**

- No skill file, `.ai/rules` file, runtime file, README, roadmap, or dossier was edited or created.
- No Composer package, package name, or namespace was chosen (§5).
- No rename was performed — `my-laravel-inertia-patterns` (§6) is a recommendation, not an action.
- `QueryFilter`/`Filterable` base classes were not promoted to executable support — they remain a
  documented pattern per locked direction, pending future evidence or a later human decision.
- `enum-options.md`, `factories-and-seeders.md`, and `request-normalization.md` were not freshly
  re-audited against live `useOrbit` code in this pass — their dispositions in §2.1 carry forward
  Phase C's evidence with that limit stated, not a new confirmation.
- `useOrbit`'s own removed design-system material (badge tones, breadcrumb rules, etc.) is out of
  `agentic-engineering`'s scope entirely — its rehoming, if any, is `useOrbit`'s own decision.

**Confidence limits, stated plainly:**

- **One-consumer evidence ceiling.** Every classification in this document — including the naming
  recommendation in §6 and the "companion workflow knowledge" label on most of §2's rows — rests on
  Laravel Boost's installed source plus exactly one real project, `useOrbit`. None of it has been
  tested against a second Laravel+Vue+Inertia codebase. This is the single largest source of
  uncertainty in the whole document, not a caveat on one row.
- **The runtime-support recommendation (§5) is chosen for reversibility, not proven distribution.**
  It has not been exercised as a separately distributed capability outside `useOrbit` — the
  packaging-justification list in §5 names exactly the evidence this pass does not yet have.
- **The two `.ai/rules`-vs-Boost tensions discovery flagged are resolved here as instructed**
  (the `assertDatabaseHas` precedence point in §2.1, the framework-behavior wording in §4) — these
  are synthesis decisions made under this pass's locked direction, not independent re-litigation of
  what discovery left open. Recording them into `.ai/rules` at all still waits on the separate
  adoption approval (§4, §7 stage 4).
- **`my-phpstorm-conventions`' content remains unverified against a live PhpStorm instance** in any
  pass to date (discovery §15) — this synthesis did not change that.

---

## Coverage check (self-report)

Every ownership row, disposition row, and open question in `phase-d-stack-discovery.md` §12, §14, and
§15 has a destination or an explicit deferral above:

- [x] All 17 `§12` summary-table rows have a disposition in §2 or §4 above, or an explicit
  "resolved, not applicable" note (enum `::all()`, §4).
- [x] Tier 1 (discovery §14, items 1–3) → §7 stage 1.
- [x] Tier 2 (items 4–5) → §7 stages 2–3, §2.1 `testing-strategy.md`, §2.2 `SKILL.md`.
- [x] Tier 3 (item 6) → §4, gated on adoption approval, sequenced in §7 stage 4.
- [x] Tier 4 (items 7–12) → item 7 resolved in §2.1; item 8 resolved in §4; item 9 resolved in §0/§2.1
  per locked direction; item 10 resolved in §5; item 11 resolved in §0 (locked direction already
  settles "stay separate"); item 12 resolved in §2.1 (`eloquent-attributes.md`, narrow now).
- [x] Tier 5 (items 13–14) → item 13 named as out of scope in §8; item 14 is the one-consumer ceiling
  named directly in §8, not silently assumed away.
- [x] No Boost-owned content is proposed for duplication: every "keep"/"narrow" disposition in §2.1
  and §2.2 states the Boost delta it's scoped to, and `eloquent-attributes.md`'s narrowing explicitly
  removes content Boost's own `eloquent.md` example already covers.
- [x] `my-phpstorm-conventions` kept separate per locked direction, justified structurally in §1's
  boundary table (orthogonal axis of variation), not merely asserted.
- [x] Nothing in this document performs a silent `.ai/rules` write or runtime install — §4 and §5 both
  state the action as a distinct, later, explicitly gated stage.
- [x] `git diff --check` run in `agentic-engineering` — see report below.
- [x] Only `phase-d-stack-synthesis.md` changed in `agentic-engineering`.
- [x] No `useOrbit` file changed — only reads were performed there.
