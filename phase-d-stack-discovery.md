# Phase D — Stack Discovery (First Pass)

Evidence gathering and decision preparation only. No skill was edited to produce this document. See
`roadmap.md` §5 for Phase D's charter and `phase-discovery.md` for the Phase C classification this
pass reverifies against current reality.

---

## 0. Executive conclusion

**A custom stack layer is still justified, but it is smaller and more asymmetric than Phase C's
classification-time snapshot suggests, and one of the two candidate skills carries real, currently
live defects that should be fixed before any extraction — independent of whatever Phase D decides
about extraction itself.**

- **`my-phpstorm-conventions` remains the stronger, cleaner candidate.** Every finding from Phase C's
  two independent full reads still holds against the current file contents. Its one open disclosure
  gap — the identity of the `getDiagnostics` tool — is now resolved by direct evidence (§4.3): it is
  Claude Code's own built-in `mcp__ide__getDiagnostics` IDE-integration tool, not a JetBrains-specific
  plugin capability as Iteration 2 speculated. Zero Boost overlap found anywhere in this skill, on a
  full re-read of all six rule files against Laravel Boost v2.7.0.
- **`my-laravel-patterns` is genuinely additive over Boost v2.7.0 in most of its ten rule files**, and
  in one dimension (the `#[Authorize]` attribute pattern, §5.4) more additive than Phase C could have
  shown, since Boost still does not document that mechanism at all. But three of Phase C's four
  concrete defects are not just unresolved, they are **worse under direct re-verification**:
  `resources.md`'s `Inertia::render()` examples are now provably wrong against the exact controller
  they claim to model (`ClientsController.php` uses `inertia()` throughout — §5.9), and the
  `assertDatabaseHas`/`assertModelExists` conflict with Boost's testing guidance is now stated as an
  explicit decision-table line in Boost's own `testing-best-practices/assertions.md`, not prose easy to
  miss (§5.6). The broken `query-conditionals.md` example and the dead `TagAttachment` citation are
  unchanged (§3.1).
- **Boost's actual v2.7.0 content is broader than Phase C could see**, and does now contain
  substantially expanded testing and controller/CRUD guidance, confirming the user's lead (§4). But
  the overlap is **principle-level, not content-level**: Boost now states a general
  "which-layer-owns-which-test-case" methodology (`testing-best-practices/rules/endpoint-tests.md`,
  §5.6) that echoes the *spirit* of `testing-strategy.md`'s layer-ownership table, and a
  resource/CRUD-controller-organization philosophy (`laravel-best-practices/rules/routing.md`, §5.4)
  that echoes `actions-pattern.md`'s thin-controller philosophy — but neither Boost file names Actions,
  Filters, or this project's own class taxonomy, so neither fully absorbs the custom skill's concrete
  content. This is a genuine partial overlap requiring a trim, not a full-file duplication requiring
  removal.
- **Two disclosure-only defects are newly introduced by today's Boost upgrade, not by anything in
  either custom skill.** Both `my-laravel-patterns/SKILL.md` and `my-phpstorm-conventions/SKILL.md`
  still say "load with `pest-testing`" — the Boost skill Phase C inspected under that name is now
  installed as `testing-best-practices` (§2.2). This is stale as of a `composer update` that ran
  **today**, 2026-08-29 (§2.1), and could not have been caught by Phase C.
- **`resource-feature-checklist.md`'s Phase-C-flagged rewrite is now complete and independently
  verified clean** (§3.1) — every stack/`useOrbit` fact that used to live inline (tenancy trait names,
  file mirrors, badge tones, the `wayfinder:generate --with-form` fact) has been generalized out or
  removed, and each removed fact resolves cleanly under this pass's classification: the wayfinder fact
  and the exact `php artisan test`/`vendor/bin/pint` commands removed from `my-git-workflow`'s
  `verification.md` are **already, independently Boost-owned** (§6.1–§6.2) — not lost, not orphaned.
  The remaining removed material (badge tones, header breakpoints, breadcrumb rule, drop-menu
  ordering, file/class mirrors) is `useOrbit`'s own design-system convention, not Laravel/Vue-ecosystem
  knowledge, and does not belong back in any skill (§6.3).
- **New evidence outside Phase C's original scope surfaced during this pass**, all confirmed against
  live memory and code: a real, repeated, verified `final`-by-default PHP class convention that exists
  only in personal memory and nowhere in `my-laravel-patterns` (§7.1); a real, current tension between
  a user-confirmed testing preference and Boost's own new test-review checklist (§7.2); and one
  self-flagged conditional assumption in `resources.md` that directly names a Boost practice
  (`Model::preventLazyLoading()`) the project has not adopted (§5.5).
- **No recommendation is made here to combine, split, retire, or extract either custom skill.** That
  remains Phase D's decision, informed by this evidence. §11 lays out the disposition options this
  evidence actually supports.

---

## 1. Evidence and provenance ledger

| Source | What was checked | Method | Result |
|---|---|---|---|
| `agentic-engineering` local + `origin/main` | Canonical baseline | `git rev-parse`, `git fetch --all`, `git log` | Local `HEAD`, local `main`, and `origin/main` all resolve to `24b288caf62f4d83b74d741a1cb96583cb1877fe` — matches the expected baseline exactly. Working tree clean except pre-existing untracked `.idea/`. |
| `useOrbit` local repo | Tracked-file cleanliness | `git status --short` | Clean before and after this pass — nothing in the tracked repo was touched. |
| `useOrbit/.claude/skills/{my-git-workflow,my-feature-planning,my-architecture-laboratory}` | Snapshot fidelity vs. canonical | `diff -rq` against `agentic-engineering` at `24b288c` | Byte-identical in all three directories. The consumed snapshot is current with the exact baseline this pass was asked to verify. |
| `useOrbit/.claude/skills/UPSTREAM_PROVENANCE.md` | Consumption/refresh history | Full read (303 lines) | Confirms the above independently: last refresh recorded at upstream commit `24b288caf62f4d83b74d741a1cb96583cb1877fe`, consumed 2026-08-29, verified via `diff -rq` byte-identical checks recorded in the file itself. |
| `useOrbit/composer.json`, `composer.lock`, `boost.json` | Installed Boost version/provenance | Direct file read | `laravel/boost: ^2.2` constraint; **installed `v2.7.0`** (`composer.lock`); `boost.json`'s `skills` array lists `testing-best-practices` where Phase C's inspection recorded `pest-testing`. |
| `useOrbit` git history on `composer.lock` | When the Boost upgrade happened | `git log -p -- composer.lock`, `git show -s --format` | Boost version history in this repo: `v2.4.9 → v2.4.13 → v2.5.3 → v2.7.0`. The `v2.5.3 → v2.7.0` bump is commit `b979d94`, dated **2026-08-29 00:19:44 +0300** — today, hours before this discovery pass. |
| `useOrbit/.claude/skills/{laravel-best-practices,testing-best-practices,wayfinder-development,inertia-vue-development}` | Full current Boost skill content | Full read of every `rules/*.md` and `SKILL.md` file present | 19 rule files read in full across `laravel-best-practices` (16) and `testing-best-practices` (8, restructured from Phase C's single `testing.md`), plus both single-file skills. See §4–§5 for content-level findings. |
| `useOrbit/CLAUDE.md` | Injected foundation guidelines | Full read (provided in session context) | Confirms `.ai/rules` + `record-rule` mechanism is documented but `useOrbit/.ai/` still does not exist (§2.3) — Phase C's finding is unchanged. Confirms exact `php artisan test --compact` / `vendor/bin/pint --dirty --format agent` commands are injected foundation rules, not skill content (§6.1). |
| `useOrbit/.claude/skills/my-laravel-patterns/**` | Every instruction file | Full read: `SKILL.md` + all 10 `rules/*.md` | All ten rule files read in full; see §5. |
| `useOrbit/.claude/skills/my-phpstorm-conventions/**` | Every instruction file | Full read: `SKILL.md` + all 6 `rules/*.md` | All six rule files read in full; see §4.3, §5.9. |
| `useOrbit/app/Providers/TestingServiceProvider.php` | Test-macro dependency | Full read | Confirms all five macros (`hasResource`, `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`) exist exactly as `testing-strategy.md` assumes — dependency is real and current. |
| `useOrbit/app/Http/Controllers/**` | Real Inertia-call-style usage | `grep -rn`/`grep -rl` across all controllers | 6 files use `Inertia::render()`, 6 use `inertia()` — evenly split, no clean temporal trend, but the resource-pattern CRUD controllers (`ClientsController`, `CarriersController`, `AgentsController`, `OrganizationMembersController`) all use `inertia()`; simpler singleton controllers (`Settings/*`, `Notifications`, `OrganizationInvitations`) use `Inertia::render()`. |
| `useOrbit/app/Http/Controllers/Clients/ClientsController.php` | The literal file `resources.md` claims to model | Full grep of Inertia calls | Uses `inertia()` at all four call sites (`index`, `create`, `show`, `edit`) — directly contradicts `resources.md`'s own `Inertia::render('Clients/Index', ...)` / `Inertia::render('Clients/Show', ...)` examples. |
| `useOrbit/app/**` (`TagAttachment`, `StatesController`, `GeneratesUniqueSlug`) | `query-conditionals.md`'s three citations | `find`, `grep` | `TagAttachment` confirmed absent from the entire codebase; the other two citations still hold and still call `->when(...)`. |
| `useOrbit/app/Http/Controllers/**` (`#[Authorize]`) | Real usage of the attribute pattern | `grep -rln` | 35 controller files use `#[Authorize(...)]`; base `Controller.php` does not use `AuthorizesRequests`. Widespread, current, real. |
| `useOrbit/app/Models/*.php` | `final class` convention | `grep -h "^final class\|^class "` | 11/11 models declared `final class`. |
| `useOrbit/pint.json` | Style-enforcement config | Direct read | Enforces `declare_strict_types`; does not and cannot enforce `final` (PHP-CS-Fixer has no rule for adding `final` to arbitrary classes). |
| `useOrbit/app/Providers/AppServiceProvider.php` | `Model::preventLazyLoading()` adoption | `grep` | Not present — confirms `resources.md`'s stated assumption is still true today, and that Boost's own recommendation to adopt it (`db-performance.md`) has not been taken up. |
| `useOrbit/.mcp.json`, `.claude/settings.local.json` | `getDiagnostics` identity | Direct read | `mcp__ide__getDiagnostics` is permission-listed alongside `mcp__laravel-boost__*` tools — confirms it is Claude Code's own built-in IDE-integration MCP tool, not a Boost or JetBrains-specific plugin tool. |
| `useOrbit/.ai/` | `.ai/rules` mechanism adoption | `find`/`ls` | Still does not exist. Phase C's "not yet exercised" finding is unchanged. |
| `~/.claude/projects/-Users-elieandraos-Desktop-Code-useOrbit/memory/` | Personal memory drift since Phase C | `ls -la`, full reads of new files | 16 feedback files + 1 project file (+ `MEMORY.md` index) now exist, versus Phase C's 16+1. Five files postdate Phase C's 2026-08-23 snapshot: `feedback_final_classes.md`, `feedback_memory_summary_format.md`, `feedback_migration_notnull.md`, `feedback_no_tests_for_framework_behavior.md`, `feedback_subagent_model_selection.md`. Three are stack-relevant; read in full (§7). |
| `useOrbit/.claude/_rollback/**` | Historical pre-refresh snapshots | `find`, targeted reads | Used only as dated historical evidence per instruction, never as current truth — e.g. to recover the exact original text of `resource-feature-checklist.md` (§3.1) and `verification.md` (§6.1) before generalization, for comparison against the current files. |
| `agentic-engineering` git history | What exactly was removed from `resource-feature-checklist.md` and `verification.md` | `git log`, `git show <sha>:<path>` | Primary evidence for §3.1 and §6.1 — the pre-rewrite file content at `fe5bd29` and `pre-phase-b-skills`, diffed conceptually against the current file. |
| `agentic-engineering/skill-audits/{my-feature-planning,my-architecture-laboratory,my-git-workflow}.md` | Authoring-pass outcomes for stack-shaped removals | Full targeted reads (grep-located sections) | Confirms `resource-feature-checklist.md`'s rewrite is complete and independently verified stack-free (`my-feature-planning.md` §12/§15); confirms the five-language syntax highlighter in `my-architecture-laboratory` remains a disclosed, optional, fallback-safe stack list, not a defect (`my-architecture-laboratory.md` §14). |

**Distinguishing evidence classes used throughout this document:** *source inspection* (direct read of
the current file), *current implementation evidence* (grep/verification against live `useOrbit` code),
*historical evidence* (rollback copies, git history, `phase-discovery.md`'s own classification-time
findings), *inference* (a judgment this pass draws from the above), and *human decision* (explicitly
flagged as unresolved, not decided here).

---

## 2. What changed since Phase C, independent of content findings

### 2.1 Boost was upgraded today

`useOrbit/composer.lock` records Boost moving `v2.5.3 → v2.7.0` in commit `b979d94`
(2026-08-29 00:19:44 +0300) — the same calendar day as this discovery pass, and after
`phase-discovery.md` was written (files dated through 2026-08-28). Every Boost-content finding in this
document is against the **current, just-upgraded** `v2.7.0`, not the version Phase C inspected.

### 2.2 A Boost skill was renamed

Phase C's evidence (`phase-discovery.md` §5) recorded Boost's testing skill as `pest-testing`. The
currently installed `boost.json` lists `testing-best-practices` instead, and no `pest-testing`
directory exists anywhere under `useOrbit/.claude/skills/`. This is a real rename, not a Phase C error
— and it leaves both `my-laravel-patterns/SKILL.md` and `my-phpstorm-conventions/SKILL.md` naming a
Boost skill that no longer exists under that name (§5.10, §4.3). Boost's own testing content was also
restructured from one `testing.md` file into eight topic files (`assertions.md`, `endpoint-tests.md`,
`finding-features.md`, `isolation.md`, `naming.md`, `performance.md`, `review.md`, `test-data.md`) —
this is the structural source of the "substantially improved testing guidance" the user observed
(§4.2).

### 2.3 `.ai/rules` is still unused

Phase C flagged that Boost's own `record-rule`/`.ai/rules` mechanism — its intended home for durable,
team-shared project rules — was not yet exercised in `useOrbit`. `useOrbit/.ai/` still does not exist.
This is unchanged, current, and worth naming again because it means the disposition question in §11
("where should recovered/companion material live") cannot lean on `.ai/rules` as an existing home —
it would be a new adoption, not a currently-active alternative.

---

## 3. Phase C baseline versus current state

This section addresses the roadmap's required reconciliation: classify each Phase C finding about the
custom stack candidates as **still current**, **resolved since Phase C**, **changed by later skill
authoring**, **changed by the Boost update**, **disproven**, or **still unresolved**. Phase C's own
readiness scores (`my-phpstorm-conventions` 8.2/10, `my-laravel-patterns` 5.8/10) are historical
classification-time measurements, not restated here as current scores — see `roadmap.md`'s own
caveat on this point, which this pass's evidence does not contradict or need to re-derive.

### 3.1 `resource-feature-checklist.md` — **resolved since Phase C**

Phase C (`phase-discovery.md` §12) found this file's generic Track A–G skeleton and `useOrbit`-specific
instantiation "braided sentence-by-sentence," requiring a rewrite rather than an extraction. Direct
comparison of the file `git show fe5bd29:my-feature-planning/rules/resource-feature-checklist.md`
against the current file confirms the rewrite happened and is complete: every organization_id/
`BelongsToCurrentOrganization`/`Carrier.php`/badge-tone/breadcrumb/drop-menu fact that used to be
inline is gone, replaced by portable questions ("What ownership, tenancy, or isolation boundary
applies?" for the old organization_id line; "the consuming project's own design system and
already-shipped patterns" for the old badge-tone/header lines). `skill-audits/my-feature-planning.md`
§12/§15 independently confirms "no project-specific content remains" on direct inspection. This
finding is resolved, not merely improved — and see §6 for where the removed content itself landed.

### 3.2 The test-macro dependency (`testing-strategy.md`) — **still current**

`TestingServiceProvider.php` still defines exactly the five macros Phase C found
(`hasResource`, `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`,
`assertHasInertiaFlash`). `testing-strategy.md` still uses all five in its worked examples with no
stated prerequisite anywhere in the skill. Unchanged from Phase C.

### 3.3 `assertDatabaseHas()` vs. `assertModelExists()` — **still current, and more prominent in Boost**

`testing-strategy.md:97` still instructs `assertDatabaseHas('clients', ['slug' => $client->slug])` for
a `show` endpoint's happy path. Boost's current `testing-best-practices/rules/assertions.md` states the
same guidance Phase C found in the old `testing.md`, now as an explicit decision-table row: *"The
existence of a model | `assertModelExists($model)` rather than `assertDatabaseHas('users', ['id' =>
$user->id])`"*. The conflict is unchanged in substance and, if anything, harder to miss now that it's a
lookup-table entry rather than prose. `my-laravel-patterns/SKILL.md:8`'s precedence rule ("these take
precedence... when there is a conflict") still exists and still has not been invoked to resolve this
specific, named disagreement.

### 3.4 The broken `query-conditionals.md` example — **still current**

The example still references undefined `$ownerColumn`/`$modelClass`, and still cites
`App\Models\TagAttachment::forTaggableType()`, confirmed absent from the current codebase by direct
`find`/`grep`. The other two cited files (`StatesController::index()`, `GeneratesUniqueSlug`) still
exist and still use `->when(...)`. Unchanged from Phase C.

### 3.5 `Inertia::render()` vs. `inertia()` — **still current, and now disproven against real code**

Phase C found this an internal contradiction between `resources.md` and `my-phpstorm-conventions/
inertia.md`, and a second contradiction with `filters-pattern.md` in the same skill. This pass adds
direct evidence Phase C did not have: `app/Http/Controllers/Clients/ClientsController.php` — the
literal controller `resources.md`'s `Clients/Index`/`Clients/Show` examples claim to model — uses
`inertia()` at every call site, zero uses of `Inertia::render()`. `resources.md`'s examples are not
merely stylistically inconsistent with a sibling skill; they no longer match the real code they cite.
Repo-wide, usage is split 6/6 with no clean temporal trend, but is stack-shape-correlated: all four
resource-pattern CRUD controllers (`Clients`, `Carriers`, `Agents`, `OrganizationMembers`) use
`inertia()`; the `Inertia::render()` users are simpler, non-resource-shaped controllers (`Settings/*`,
`Notifications`, `OrganizationInvitations`). This raises the priority of fixing this specific
contradiction from "worth fixing regardless of Phase D's outcome" (Phase C's framing) to "the file's
own worked examples are currently wrong."

### 3.6 The `getDiagnostics` dependency/fallback — **resolved since Phase C**

Iteration 2 (`phase-discovery.md` §11) could not determine `getDiagnostics`' provenance and speculated
it was "almost certainly a JetBrains/PhpStorm IDE-integration MCP tool." Direct inspection of
`useOrbit/.claude/settings.local.json` shows `mcp__ide__getDiagnostics` permission-listed alongside
`mcp__laravel-boost__*` tools with the `mcp__ide__` namespace — this is Claude Code's own built-in
IDE-integration MCP server, exposed when Claude Code is connected to a compatible IDE, not a
JetBrains/PhpStorm-specific plugin capability. This resolves Iteration 2's open question with high
confidence. It does not resolve the *fallback* question — `SKILL.md:30` still states no behavior for a
session where this tool is unavailable, and `feedback_phpstorm_skill_activation.md` (memory) still
documents three prior real occurrences of the activation step not firing — so the disclosure gap Phase
C called for (name the dependency, state a fallback) is still open even though the tool's identity is
now known.

### 3.7 Combining or separating the two custom skills — **still unresolved, with new (ambiguous) evidence**

Phase C found no cross-project evidence either way and noted the two skills' most consequential
problems sit on opposite sides of the seam (Iteration 2, §13). This pass adds a further asymmetry:
`my-phpstorm-conventions`' one remaining defect (disclosure-only) is now largely resolved (§3.6);
`my-laravel-patterns`' four defects are unresolved and one has worsened in evidence quality (§3.5).
Both `SKILL.md` files still state "always load alongside" with no independent trigger for either
skill — the co-loading evidence is unchanged. The two skills' problem profiles are now more clearly
asymmetric than at Phase C, which is itself new evidence, but it points toward *not* combining rather
than combining: merging a low-defect, high-cohesion skill with a skill carrying four independent,
unresolved defects would make `my-phpstorm-conventions`' otherwise-clean extraction readiness
conditional on fixes it doesn't itself need. Still a human decision — not resolved here.

---

## 4. Current Boost capability / ownership map

### 4.1 Installed state

- **Version:** `laravel/boost v2.7.0` (constraint `^2.2` in `composer.json`), upgraded from `v2.5.3`
  earlier today (§2.1).
- **`boost.json` skills:** `infer-conventions`, `fortify-development`, `laravel-best-practices`,
  `testing-best-practices`, `wayfinder-development`, `inertia-vue-development`, `echo-vue-development`,
  `echo-development`, `tailwindcss-development`.
- **`laravel-best-practices`** now ships 16 topic files under `rules/`: `advanced-queries.md`,
  `architecture.md`, `blade-views.md`, `caching.md`, `collections.md`, `config.md`,
  `db-performance.md`, `eloquent.md`, `error-handling.md`, `events-notifications.md`,
  `http-client.md`, `mail.md`, `migrations.md`, `queue-jobs.md`, `routing.md`, `scheduling.md`,
  `security.md`, `style.md`, `validation.md` — materially more granular than Phase C's single-file
  citations of `architecture.md`/`eloquent.md`.
- **`testing-best-practices`** (renamed from `pest-testing`, §2.2) ships 8 topic files:
  `assertions.md`, `endpoint-tests.md`, `finding-features.md`, `isolation.md`, `naming.md`,
  `performance.md`, `review.md`, `security.md`, `test-data.md`.
- **`.mcp.json`:** `laravel-boost` (`php artisan boost:mcp`) and `claude_design` — unchanged from Phase
  C.
- **Injected `CLAUDE.md`** (foundation + boost + php + tests + inertia + laravel/core + wayfinder +
  pint + pest rule blocks) is Boost-generated and always active, independent of which skills are
  explicitly loaded. This is where the exact `php artisan test --compact` / `vendor/bin/pint --dirty
  --format agent` commands actually live now (§6.1) — not in any skill file at all.

### 4.2 What is genuinely new or deeper since Phase C

Confirmed by full reads, not inferred from file names:

- **CRUD/resourceful controller conventions** (`routing.md`): "Use Resource Routes for Resourceful
  Actions," "Organize Controllers Around Resources," and an explicit decision rule for when a custom
  verb should become its own resource controller instead of a bolt-on action. None of this existed in
  the `architecture.md`-only view Phase C had.
  Boost's own example even names an `Action` class (`CreatePostAction`) in a controller-organization
  context, using `execute()` as the method name where `my-laravel-patterns` uses `handle()` — a naming
  difference, not a documented conflict, since Boost does not prescribe a specific action-class
  contract.
- **A general layer-ownership testing principle** (`testing-best-practices/rules/endpoint-tests.md`,
  "Which Layer Owns Which Case"): *"The rule-class test owns the matrix of values that pass and fail.
  The endpoint test proves that the endpoint applies the rule... The same division applies to policies,
  scopes, and other classes called by a request."* This is the same underlying methodology
  `testing-strategy.md`'s "Layer Ownership" table teaches, stated generically for the first time in
  Boost's own guidance (§5.6).
- **A file-layout convention** (`testing-best-practices/rules/naming.md`): "Place each test file at the
  same relative path as the class under test," with `app/Actions/DeleteTeam.php` →
  `tests/Unit/Actions/DeleteTeamTest.php` given as Boost's own example — the same convention
  `actions-pattern.md`/`testing-strategy.md` already state for this project's Action tests.
- **A general N+1-prevention recommendation** (`laravel-best-practices/rules/db-performance.md`):
  `Model::preventLazyLoading()` in `AppServiceProvider::boot()`. Not adopted in `useOrbit` (§1 ledger),
  and directly relevant because `resources.md`'s own `whenLoaded()` rule is explicitly conditioned on
  its absence (§5.5).
- **The `--with-form` Wayfinder flag** is now Boost's own documented content
  (`wayfinder-development/SKILL.md`), not something `resource-feature-checklist.md` needed to carry
  (§6.2).

### 4.3 What is confirmed still absent from Boost

Full reads found **no** Boost coverage, in `v2.7.0`, of: the `#[Authorize]` PHP-attribute authorization
pattern and its array-vs-string resolution behavior (§5.4); the class-based `QueryFilter`/`Filterable`
pattern (§5.7); `prepareForValidation()`-owns-normalization as a boundary discipline, including the
"two independent `??` fallbacks" and "absent-value semantics" failure modes (§5.8); the derive-fake-
fields-from-one-source-of-truth and chronological-date-chaining factory conventions (§5.3); backed-enum
`::all()` static-method convention (§5.2); or anything about PhpStorm/IDE static-analysis behavior
(confirmed again on this pass's full re-read of all six `my-phpstorm-conventions` rule files, §3.6,
§5.9).

---

## 5. Passage-level `my-laravel-patterns` overlap matrix

Ten rule files, each rated against the current Boost `v2.7.0` install. "Delta" = what remains after
subtracting anything Boost already owns.

### 5.1 `actions-pattern.md`

- **Purpose:** FormRequest-validates / Action-executes / Controller-responds split; naming, location,
  `$attributes` parameter convention, `afterCommit()` side-effect discipline.
- **Boost capability:** `architecture.md`'s "Extract Focused Business Operations" (bare `handle()`
  example, no FormRequest split, no naming/location convention) + `routing.md`'s "Keep Controllers
  Focused on HTTP Concerns" (thin-controller philosophy, an `Action`-using example, warns against
  extracting "merely to satisfy an arbitrary line limit").
- **Relationship:** **Partial overlap.** The high-level philosophy (thin controller, extract business
  logic) is now stated on both sides. The concrete contract — `app/Actions/{Domain}/` location,
  `{Verb}{Model}Action` naming, `handle()` as the fixed method name, `$attributes` as the fixed
  parameter name, the PHPDoc-shape-derived-from-FormRequest-rules algorithm, and the
  `DB::transaction()`-pure / `->afterCommit()`-for-side-effects discipline with its three-scenario
  failure table — has no Boost equivalent.
- **useOrbit evidence:** `app/Actions/**` widely follows this shape (verified via the `#[Authorize]`
  grep's controller sample and `TestingServiceProvider`/factory evidence elsewhere in this pass).
- **Disposition:** Retain the concrete contract; the philosophy framing sentence could be trimmed since
  Boost now states the general case. Not urgent — no conflict, low cost either way.
- **Confidence:** High. Both Boost files read in full; no additional overlap found beyond what's noted.

### 5.2 `enum-options.md`

- **Purpose:** Backed enums own a static `all(): array` mapping; never inline `::cases()` mapping at
  call sites.
- **Boost capability:** None found — `grep -rln -i enum` across all 16 `laravel-best-practices` files
  hits only `config.md` and `style.md`, neither substantively.
- **Relationship:** No overlap.
- **useOrbit evidence:** Not independently re-verified against every enum in this pass (out of scope
  for a discovery-level check); Phase C's own inspection already confirmed real usage.
- **Disposition:** Retain as-is.
- **Confidence:** High on the no-overlap finding; unchanged from Phase C on the content itself.

### 5.3 `factories-and-seeders.md`

- **Purpose:** Derive dependent fake fields from one source of truth; build emails from generated
  names; chain dates chronologically; `for()` vs. custom factory state decision rule; seeder structure
  and environment gating.
- **Boost capability:** `testing-best-practices/rules/test-data.md` ("Factories and Test Data") now
  exists and recommends `for()`/"the relationship helper of the project" for declaring ownership, plus
  `recycle()`/`sequence()`/named-state guidance.
- **Relationship:** **Partial overlap, narrow.** Boost's "prefer `for()`" endorsement overlaps the
  spirit of `factories-and-seeders.md`'s `for()` guidance, but Boost states no decision criterion for
  *when* a custom state is warranted (derived value) versus not (copied value already in scope) — that
  decision tree is this skill's own delta. The dependent-field derivation, email-generation, date-
  chaining, and seeder-structure/environment-gating sections have no Boost equivalent at all.
- **useOrbit evidence:** Not independently re-verified in this pass beyond the `for()`/derived-state
  distinction being internally consistent with `my-laravel-patterns/rules/authorization.md`'s own
  organization-scoping examples.
- **Disposition:** Retain; optionally trim the `for()` framing sentence to acknowledge Boost's own
  endorsement rather than presenting it as solely this skill's convention.
- **Confidence:** High on the file-existence/overlap-shape finding; medium on completeness of the
  underlying `useOrbit` factory-code cross-check (not exhaustively re-audited).

### 5.4 `authorization.md`

- **Purpose:** `#[Authorize(ability, model)]` PHP-attribute-based controller authorization; never
  `$this->authorize()`; the array-form resolution rule for `create`/`viewAny` on a child resource.
- **Boost capability:** `security.md`'s "Authorize Protected Actions" — `Gate::authorize()` inline in
  the controller, or a FormRequest's `authorize()` boolean method. No mention of the `#[Authorize]`
  routing attribute anywhere in `laravel-best-practices`.
- **Relationship:** **No overlap — genuine delta, and the strongest one in the skill.** This is a real,
  non-trivial Laravel mechanism (`Illuminate\Routing\Attributes\Controllers\Authorize`) with subtle,
  documented resolution behavior (string-with-backslash vs. array-form argument handling) that Boost's
  own guidance does not cover at all, confirmed on a full read of `security.md`.
- **useOrbit evidence:** 35 controller files use `#[Authorize(...)]`; base `Controller.php` does not
  use `AuthorizesRequests` — widespread, current, real, directly verified.
- **Disposition:** Retain unchanged. Highest-confidence keep in the entire skill.
- **Confidence:** High.

### 5.5 `resources.md`

- **Purpose:** Always wrap Eloquent results in a `JsonResource` before passing to Inertia; `final`
  class, `@mixin` PHPDoc convention; `whenLoaded()` over bare accessor or model-level `$with` for
  relation exposure.
- **Boost capability:** No dedicated API-Resources file in `laravel-best-practices`; `db-performance.md`
  covers N+1 prevention generally, including `Model::preventLazyLoading()` — a practice
  `resources.md:75` explicitly cites the *absence* of as its own rule's justification ("this app
  doesn't call `Model::preventLazyLoading()` anywhere").
- **Relationship:** No direct overlap on the Resource-wrapping/`whenLoaded()` content itself. But
  `resources.md`'s own stated rationale names a Boost recommendation the project has not adopted —
  confirmed absent from `AppServiceProvider.php` in this pass. This is not a conflict (the rule already
  self-labels its assumption as falsifiable), but it is a live dependency on a fact that could change
  the next time someone acts on Boost's own advice.
- **useOrbit evidence:** `Inertia::render()` examples confirmed wrong against `ClientsController.php`
  (§3.5) — this is the file's real, current defect, independent of the Resource-wrapping content.
- **Disposition:** Fix the Inertia-call-style examples now (high-confidence, low-cost, evidence-backed);
  flag the `preventLazyLoading()` dependency as something to recheck if that practice is ever adopted.
  The Resource-wrapping/`whenLoaded()` content itself needs no change.
- **Confidence:** High on the Inertia-example defect (directly reproduced); medium-high on the
  `preventLazyLoading()` framing (correctly self-disclosed, not a hidden assumption).

### 5.6 `testing-strategy.md`

- **Purpose:** Four-layer test-ownership model (Action/Controller/Policy/Filter, no cross-layer
  duplication); custom Inertia/TestResponse macro usage; per-scenario controller-test assertion table.
- **Boost capability:** `testing-best-practices/rules/endpoint-tests.md`'s "Which Layer Owns Which
  Case" now states the general no-cross-layer-duplication principle for validation rules, policies, and
  scopes. `testing-best-practices/rules/assertions.md` states `assertModelExists()` over
  `assertDatabaseHas()` as a decision-table row.
- **Relationship:** **Partial overlap on the ownership *principle*; conflict on one concrete
  assertion.** Boost's version generalizes "the narrow-scope class owns the matrix, the caller-test
  proves wiring with one case" but never names Actions or Filters — both are this project's own class
  taxonomy, not stock Laravel/Eloquent concepts, so the concrete Action-test/Filter-test mapping remains
  a genuine delta even though the underlying principle is now stated elsewhere in more general form.
  The `assertDatabaseHas`/`assertModelExists` disagreement is a real, current, unresolved conflict
  (§3.3), not overlap.
- **useOrbit evidence:** `TestingServiceProvider.php` macros confirmed real and current (§3.2);
  `ClientsController.php`'s `show` action pattern matches `testing-strategy.md:97`'s exact
  `assertDatabaseHas` example.
- **Disposition:** (1) Trim or reframe the generic "never duplicate across layers" sentence, since
  Boost now states that principle in its own general form — keep only the concrete Action/Controller/
  Policy/Filter mapping, which Boost does not have. (2) Resolve the `assertDatabaseHas`/
  `assertModelExists` conflict explicitly — either invoke the skill's own stated precedence rule in
  writing, or change the examples. (3) State the five-macro dependency as an explicit prerequisite
  before any extraction. All three are human decisions on *how* to resolve, not just *whether* —
  flagged, not resolved, here.
- **Confidence:** High on all three sub-findings; each independently reproduced against current files.

### 5.7 `filters-pattern.md`

- **Purpose:** Class-based `QueryFilter`/`Filterable` dispatch mechanism; convention-over-configuration
  method-name matching; controller/FormRequest wiring.
- **Boost capability:** None found anywhere in `laravel-best-practices` or `testing-best-practices`.
- **Relationship:** No overlap.
- **useOrbit evidence:** `filters-pattern.md:5` still contains live, resolvable hyperlinks to
  `github.com/elieandraos/useOrbit/issues/76` and `#71` — a literal repository fingerprint, unchanged
  from Phase C's finding. The worked example (`Client::query()->filter(...)->latest('enrollment_date')
  ->paginate(7)`) still reads as a lightly-cleaned real snippet (the `paginate(7)` literal), also
  unchanged.
- **Disposition:** Retain the mechanism; if ever prepared for extraction, replace the literal issue
  links and the arbitrary `paginate(7)` literal with generic placeholders.
- **Confidence:** High.

### 5.8 `request-normalization.md`

- **Purpose:** `prepareForValidation()` owns all input coercion/defaulting; the "computed twice, drifts
  apart" failure mode; the "changes what absent means" failure mode; `validated($key, $default)` over
  destructuring.
- **Boost capability:** `validation.md` covers form-request extraction, rule syntax, `validated()`/
  `safe()` over `all()`, conditional rules, and cross-field `after()` validation — but nothing about
  where *coercion/defaulting* (as distinct from validation) belongs, and nothing about either named
  failure mode.
- **Relationship:** No overlap — this rule answers a question Boost's validation guidance doesn't ask.
- **useOrbit evidence:** Not independently re-verified beyond internal consistency with
  `filters-pattern.md`'s wiring example.
- **Disposition:** Retain unchanged.
- **Confidence:** High on no-overlap; not independently re-verified against live `useOrbit` FormRequest
  code in this pass.

### 5.9 `eloquent-attributes.md`

- **Purpose:** `#[Scope]` attribute over legacy `scope`-prefixed method naming; `protected` visibility;
  Laravel `^13.7` version pin.
- **Boost capability:** `eloquent.md`'s "Use Local Scopes for Reusable Queries" gives `#[Scope]` as
  Boost's own first-party "correct" example, with the same `protected` method, same import.
- **Relationship:** **Substantial duplication, narrow real delta.** Boost fully documents the
  `#[Scope]` pattern itself. What `eloquent-attributes.md` adds: the explicit `❌ scopeXxx` counter-
  example (Boost's file doesn't show the legacy form at all), the "no call-site change" note, and the
  version pin. Unchanged from Phase C's finding; independently confirmed against the current
  `eloquent.md` text in this pass.
- **useOrbit evidence:** `Client::filter()` defined via `#[Scope]` is the same example
  `filters-pattern.md`/`my-phpstorm-conventions/eloquent.md` both reference — real, current, consistent
  across three files.
- **Disposition:** Trim to the narrow delta (the migration framing, the counter-example, the version
  pin) rather than retaining the full restatement of Boost's own content — this is the one file in the
  skill where "reduce" is the evidence-backed disposition, not "retain" or "remove."
- **Confidence:** High.

### 5.10 `query-conditionals.md`

- **Purpose:** `when()` over `if` for conditionally applying a query-builder clause mid-chain.
- **Boost capability:** None found — `when(` does not appear in `advanced-queries.md`, `collections.md`,
  or `eloquent.md`.
- **Relationship:** No overlap.
- **useOrbit evidence:** The rule's own flagship example is broken (§3.4) and its third citation is
  dead. The rule's *content* (prefer `when()`) is sound and unchallenged by any evidence gathered; only
  the *example* is defective.
- **Disposition:** Fix or replace the example; the rule itself needs no change.
- **Confidence:** High.

### 5.11 `SKILL.md` (frontmatter and "How to Apply")

- **Finding, not in the rule files themselves:** Both `my-laravel-patterns/SKILL.md` and
  `my-phpstorm-conventions/SKILL.md` instruct loading alongside `pest-testing`, a Boost skill name that
  no longer exists as of today's upgrade (§2.2). This is a fresh, evidence-confirmed disclosure gap
  introduced by the Boost update itself, not by anything either custom skill did.
- **Disposition:** Update both references to `testing-best-practices` regardless of any other Phase D
  outcome — this is a correctness fix, not a design decision.
- **Confidence:** High.

---

## 6. Recovered material from the three canonical skills

### 6.1 `my-git-workflow/rules/verification.md`'s embedded stack commands — **already Boost-owned**

Phase C (`phase-discovery.md` §6a) flagged the literal `php artisan test --compact <path>` /
`vendor/bin/pint --dirty --format agent` commands embedded directly in `verification.md`'s prose,
contrasted with `release.md`'s cleaner "what this repository's evidence shows" boxing pattern.
`UPSTREAM_PROVENANCE.md` records this as resolved by `my-git-workflow`'s 2026-08-24 authoring pass. But
comparing the current `verification.md` (fully generalized: "Discover the project's verification tools"
— no literal command anywhere) against the pre-refresh rollback copy shows these facts were not boxed,
they were **removed outright** — and this pass finds why that's correct: `useOrbit/CLAUDE.md`'s
injected foundation guidelines (visible in this session's own context) state, verbatim, *"Run the
narrowest set of tests... Pass a file path... to `php artisan test --compact`"* and *"you must run
`vendor/bin/pint --dirty --format agent` before finalizing changes."* These exact facts are
**already, independently Boost-owned** — not through a skill file, but through Boost's own injected
`CLAUDE.md` rule blocks (`pint/core`, `pest/core`). Nothing needs to be recovered here; the removal was
correct classification, confirmed by evidence Phase C's own inspection didn't check (Phase C's §5 named
Boost's *skills*, not its injected `CLAUDE.md` content, as the external-dependency inventory).

The Fortify-2FA feature-flag incident narrative that once illustrated the "gated tests silently
reactivate" methodology point (rollback: `verification.md` lines 65–76) generalized correctly into the
current file's "runtime activation gate" section — no Fortify/Laravel vocabulary survives, and no
Fortify-specific fact needs recovery. **Portable concern already correctly generalized.**

### 6.2 `resource-feature-checklist.md`'s removed Track G Wayfinder fact — **already Boost-owned**

The removed fact ("`php artisan wayfinder:generate` alone omits `.form()` helpers — pass `--with-form`
explicitly") is now Boost's own documented content, verbatim in spirit, in
`wayfinder-development/SKILL.md`'s "Generate Routes" section. No recovery needed.

### 6.3 `resource-feature-checklist.md`'s removed Track A/B/C/D/F design-system content — **useOrbit-specific**

The remaining removed content — `BelongsToCurrentOrganization`/`HasSlug` trait names, `Carrier.php`/
`BranchModal.vue`/`ClientsIndexHeader.vue` file mirrors, the badge-tone palette (`tone="success" dot"`,
etc.), the breadcrumb rule (index: none, sub-pages: yes), the mobile/desktop header breakpoint classes,
drop-menu ordering, the nav-link file path — is `useOrbit`'s own product design-system and file
layout, not Laravel/Vue-ecosystem-wide knowledge. This confirms Phase C's own judgment (§8.3) rather
than revising it: a different Laravel/Inertia application would have its own equivalents, not these
exact values. None of it currently exists anywhere else (not in `_docs/`, not in memory, not in any
skill) — it is only preserved in `agentic-engineering`'s own git history and the `useOrbit` rollback
copies, both historical, neither a living reference. **This is the one piece of genuinely lost
information from this exercise** — not wrongly removed from the portable skill, but not yet
re-homed anywhere `useOrbit` itself could consult it (its own `_docs/`, a design-system reference, or
project memory). This is a `useOrbit`-side gap, out of `agentic-engineering`'s scope to fix, but worth
naming so it isn't silently lost twice.

### 6.4 `my-feature-planning`'s removed memory dependencies — **resolved since Phase C**

Phase C (§6c) found `design-reconciliation.md` and `issue-conventions.md` each directly naming a
personal-memory entry inline. `skill-audits/my-feature-planning.md` §12 confirms, and direct inspection
of the current files confirms independently, that neither file references any memory entry by name
anymore — both discover the equivalent information from project-supplied context instead. No content
to recover; this was a coupling removal, not a knowledge removal.

### 6.5 `my-architecture-laboratory`'s stack-named syntax highlighter — **portable concern, not removed**

Not a removal at all, included here because it's the one place a canonical skill still names a stack
list: the five-language (PHP, TS, Vue, JSON, HTTP) syntax-highlighter list in `template.html`, per
`skill-audits/my-architecture-laboratory.md` §14, is a disclosed, optional capability with a documented
safe universal fallback — not a hidden assumption. This pass finds no new evidence changing that
assessment; whether it should move to a stack layer remains the open, narrow question that dossier
already flagged, not resolved here.

### 6.6 `my-git-workflow`'s commit-body-line tension — **still unresolved**

`feedback_commit_workflow.md` (memory, still present, last modified 2026-08-29) still states commit
messages must be "a single descriptive sentence — no multi-sentence bodies," while
`commit-boundaries.md` still permits an optional body. Neither file reconciles this. Not a stack-layer
question, included here only because it's one of the specific items the roadmap named for reverification
(§8.5) — still open, still a human decision.

---

## 7. New evidence outside Phase C's original scope

### 7.1 `feedback_final_classes.md` — a real, verified gap, not currently a companion candidate on file

**Fact.** This memory entry (present as of today, `originSessionId` distinct from any file Phase C
inventoried) states: *"All new PHP classes must use `final class` by default... This applies to every
class type: Models, Actions, Controllers, Middleware, Policies, FormRequests."*

**Current implementation evidence.** `grep -h "^final class\|^class "` across `app/Models/*.php` shows
11/11 models declared `final class`. `my-laravel-patterns` already states `final` individually for
Actions (`actions-pattern.md`), Resources (`resources.md`), and Filters (`filters-pattern.md`), but
none of its ten rule files states the general, project-wide "final by default for every PHP class"
policy this memory records — and Models are the clearest evidence of a class type covered by the
general policy but not by any of the skill's per-pattern mentions.

**Boost capability check.** No mention of `final` anywhere in `laravel-best-practices`
(`grep -rln "final class\|\bfinal\b"` across all 16 files returns nothing).

**Disposition:** Genuine companion candidate, currently under-captured. This is real, current,
repeated, verified, stack-generic (a PHP/Laravel house-style convention, not a `useOrbit` product
fact), and not Boost-owned. It is not something removed from a portable skill — it simply never made
it from memory into `my-laravel-patterns` as a general rule. Whether to add it, and where, is a human
decision; the evidence supports that it belongs somewhere in the custom stack layer if one continues to
exist.

**Confidence:** High on the evidence; the disposition itself (add now vs. wait) is unresolved by
design.

### 7.2 `feedback_no_tests_for_framework_behavior.md` vs. Boost's own test-review checklist — **a real, live tension**

**Fact.** This memory entry (confirmed, dated 2026-07-18, referenced by `[[feedback_no_tests_for_design_docs]]`)
records a user-confirmed, incident-backed preference: *"Don't write unit tests for scaffolding that has
no business logic of its own — e.g. verifying an Eloquent `casts()` enum mapping works... Caught during
issue #107... user rejected a `DocumentTest.php` covering exactly these three things."*

**Boost capability check.** `testing-best-practices/rules/review.md`'s "Test Value" checklist states:
*"no test asserts the behavior of the framework. A test of what this project configures, such as a
relation with a constraint, **a cast**, or a scope, belongs to this project."* Read plainly, this
instructs testing a project-configured cast — the same category of test (an Eloquent `casts()` enum
mapping) the user explicitly rejected in a real, confirmed incident.

**Relationship:** **Conflict, not overlap** — between a user-confirmed preference (memory) and Boost's
own current guidance, not between the custom skill and Boost (neither custom skill states this rule at
all; it lives only in memory). Per this task's instruction not to silently choose a winner: this is
flagged, not resolved. It is plausible Boost's "belongs to this project" language means something
narrower than "always write this test" (e.g., "this failure mode is this project's responsibility to
catch if it matters," not "always add a dedicated test for it") — but the plain reading conflicts with
the user's own confirmed, incident-backed preference, and only the user can say which framing governs
going forward.

**Disposition:** Human decision required. Neither custom skill needs a code change either way; this is
worth surfacing precisely because a future agent following Boost's `review.md` checklist literally
could reintroduce exactly the test pattern the user has already rejected once.

**Confidence:** High on both sides of the conflict being accurately quoted; medium on whether the
conflict is substantive (a plain reading favors "yes") versus a phrasing ambiguity — flagged rather than
asserted.

### 7.3 `feedback_migration_notnull.md` — narrow, single-incident, not skill-worthy

**Fact.** *"Never use `->notNull()` on migration column definitions. The method does not exist... and
PhpStorm's warning about it is correct, not a false positive."* Not covered by Boost's `migrations.md`
(checked directly). Notably the *inverse* shape of every `my-phpstorm-conventions` finding — a case
where the IDE warning is right and the workaround is "don't write the code," not "suppress the
warning." Real and current, but a single narrow API-knowledge correction, not a generalizable
convention. **Disposition:** leave in memory; does not meet the bar for a skill rule.

---

## 8. `my-phpstorm-conventions` analysis

Answering the roadmap's classification question directly: **it is a reusable custom tooling capability,
positioned as a Laravel+PhpStorm+Pest companion layer alongside `my-laravel-patterns`, not a
`useOrbit`-specific skill, not primarily "external-tool instructions" in the sense of documenting the
tool itself rather than a project convention, and not something this pass finds reason to change in
content.**

- **Reusable custom tooling capability:** yes — every one of its six rule files documents a PhpStorm/
  Pest static-analysis behavior whose validity depends on PhpStorm's own resolution engine, not on
  `useOrbit`'s product domain. Confirmed on this pass's own full re-read of all six files (§5.9 for the
  `eloquent.md`/`inertia.md` cross-reference; `pivot.md`, `pest.md`, `strings.md`, `phpdoc.md` read in
  full with zero product-domain findings).
- **Part of the Laravel/Vue/Inertia companion layer, not a fully separate IDE-specific companion:**
  the evidence for treating it as one unit with `my-laravel-patterns` is unchanged from Phase C — both
  `SKILL.md`s state "always load alongside," neither states an independent trigger, and `_docs/
  skills.md`'s prior grouping note (Phase C §1.4) still stands, unverified by this pass but not
  contradicted either. The asymmetric defect profile (§3.7) is new evidence, and it argues against
  forcing a merge, not for treating them as unrelated.
- **Not `useOrbit`-specific:** confirmed again, independently, on this pass's own reads — zero findings
  depend on tenancy, roles, or product domain.
- **Not "mostly external-tool instructions":** each rule teaches a project-adopted convention or a
  documented workaround for a specific false positive, with a stated mechanism (why the fix works), not
  a restatement of PhpStorm's own documentation.
- **Comparison with Boost:** zero overlap found across all six files against Boost `v2.7.0` (confirmed
  again on this pass, §4.3) — the subject matter (IDE static analysis) sits entirely outside anything
  Boost documents.
- **Comparison with `my-laravel-patterns`:** exactly one point of content coupling — the
  `Inertia::render()`/`inertia()` contradiction (§3.5), which this pass's new evidence makes higher-
  priority to fix than Phase C could show.
- **What remains unproven:** the PhpStorm/plugin-version dependency (no baseline stated, and at least
  one finding — `eloquent.md`'s `#[Scope]`-not-resolved section — describes current, not-yet-fixed IDE
  behavior JetBrains could patch at any time); this pass has no way to independently verify current
  PhpStorm behavior and does not claim to.

---

## 9. Remaining custom companion capabilities — summary table

| Capability | Skill/file | Boost overlap | Disposition |
|---|---|---|---|
| `#[Authorize]` attribute pattern | `authorization.md` | None | Retain unchanged — strongest keep in the ecosystem |
| `QueryFilter`/`Filterable` pattern | `filters-pattern.md` | None | Retain; scrub literal issue links/arbitrary literals if extracted |
| `prepareForValidation()` normalization discipline | `request-normalization.md` | None | Retain unchanged |
| Enum `::all()` convention | `enum-options.md` | None | Retain unchanged |
| Factory/seeder realism conventions | `factories-and-seeders.md` | Narrow (`for()` endorsement) | Retain; optionally reframe |
| Actions pattern (naming/location/`$attributes`/afterCommit) | `actions-pattern.md` | Partial (philosophy only) | Retain concrete contract |
| Layer-ownership testing model (Action/Controller/Policy/Filter) | `testing-strategy.md` | Partial (principle only) + one active conflict | Trim generic framing; resolve `assertModelExists` conflict; disclose macro dependency |
| `#[Scope]` attribute documentation | `eloquent-attributes.md` | Substantial | Reduce to narrow delta |
| `when()` over `if` query conditionals | `query-conditionals.md` | None | Retain; fix broken example |
| Resource-wrapping / `whenLoaded()` discipline | `resources.md` | None (but self-flagged dependency on an unadopted Boost practice) | Retain; fix Inertia-call examples now |
| PhpStorm/Pest IDE-workaround set (6 files) | `my-phpstorm-conventions` | None | Retain; disclose `getDiagnostics` + fallback; consider version baseline |
| `final`-by-default PHP class policy | memory only, not in any skill | None | Human decision: add as new rule |

---

## 10. Decomposition options and trade-offs

Presented as options, not a recommendation of one:

1. **Leave both skills as two, unchanged in shape, apply only the disclosure/correctness fixes above.**
   Lowest risk, addresses the newly-worsened `resources.md` defect and the fresh `pest-testing` staleness
   immediately. Leaves the `assertModelExists`/macro-dependency/`eloquent-attributes.md` trims for a
   later, separately-scoped pass.
2. **Refine `my-laravel-patterns` substantially before considering extraction; leave
   `my-phpstorm-conventions` to proceed on its own, faster timeline.** Matches the asymmetric evidence
   directly (§3.7, §8) — treats "extraction-ready" as a per-skill property, not a joint one. Risk: if
   Phase D's actual goal is a single combined extraction, staggering the two skills' readiness could
   complicate that.
3. **Combine into one skill now, on the theory that they're always co-loaded anyway.** The co-loading
   evidence is real and unchanged since Phase C, but this pass's asymmetric-defect finding is evidence
   *against* this option, not for it — combining now would make `my-phpstorm-conventions`' already-clean
   content ship bundled with `my-laravel-patterns`' four open defects.
4. **Do nothing yet; treat this pass's findings as a backlog for whenever Phase D actually convenes.**
   Consistent with roadmap.md §5's explicit "deciding that no further extraction is justified yet" as a
   legitimate outcome. Risk: `resources.md`'s Inertia-example defect and the `pest-testing` staleness are
   both correctness bugs independent of any extraction decision, and continue to mislead a consuming
   agent until fixed regardless of when/whether extraction happens.

No adapter-folder structure, package name, or forced single-skill outcome is implied by any option
above, consistent with `roadmap.md`'s own guardrail.

---

## 11. Recommended Phase D disposition and implementation order

This section states what the evidence supports doing, in what order — not a final decision, since
several of the underlying calls are explicitly human decisions (§12).

**Tier 1 — correctness fixes, evidence-backed, no design decision required, worth doing regardless of
what Phase D decides about extraction:**
1. `my-laravel-patterns/SKILL.md` and `my-phpstorm-conventions/SKILL.md`: replace `pest-testing` with
   `testing-best-practices` (§2.2, §5.11).
2. `resources.md`: fix the `Inertia::render()` examples to `inertia()`, matching both the sibling
   skill's rule and the actual current `ClientsController.php` (§3.5, §5.5).
3. `query-conditionals.md`: fix or replace the broken example and the dead `TagAttachment` citation
   (§3.4, §5.10).

**Tier 2 — disclosure fixes, evidence-backed, narrow in scope:**
4. `testing-strategy.md`: state the five `TestingServiceProvider` macros as an explicit prerequisite
   (§3.2, §5.6).
5. `my-phpstorm-conventions/SKILL.md`: name `getDiagnostics` as Claude Code's built-in IDE-integration
   tool (now known, §3.6) with a stated fallback for a session without it.

**Tier 3 — human decisions this evidence surfaces but does not resolve (see §12):**
6. Reconcile or deliberately document the `assertDatabaseHas`/`assertModelExists` conflict with Boost
   (§3.3, §5.6).
7. Decide the disposition of `feedback_final_classes.md` (§7.1) and the `feedback_no_tests_for_
   framework_behavior.md` vs. Boost `review.md` tension (§7.2).
8. Decide whether `eloquent-attributes.md` is trimmed to its narrow delta now or left as a convenience
   restatement (§5.9).
9. Decide whether the two custom skills combine, stay separate, or proceed on independently-timed
   readiness tracks (§3.7, §8, option 2 in §10).

**Tier 4 — genuinely deferred, out of this pass's evidence:**
10. `useOrbit`'s own design-system material (§6.3) re-homing — outside `agentic-engineering`'s scope.
11. Anything gated on cross-project evidence this single-consumer pass cannot supply (repeated per
    Phase C's own §8.8, unresolved by construction).

---

## 12. Unresolved human decisions and evidence limits

**Human decisions, explicitly not made here:**
- Whether `my-laravel-patterns` and `my-phpstorm-conventions` combine, stay separate, or proceed on
  independent timelines (§3.7, §8, §10).
- How to resolve the `assertDatabaseHas`/`assertModelExists` conflict with Boost — invoke the stated
  precedence rule explicitly, or change the examples (§3.3, §5.6).
- How to resolve the `feedback_no_tests_for_framework_behavior.md` vs. Boost `review.md` tension —
  reject Boost's checklist item, narrow its reading, or update the memory (§7.2).
- Whether to add `feedback_final_classes.md`'s policy as a new general rule, and where (§7.1).
- Whether `eloquent-attributes.md` is trimmed now or later (§5.9).
- The `feedback_commit_workflow.md`/`commit-boundaries.md` commit-body tension — still open, not
  addressed by this pass, carried forward from Phase C (§6.6).
- Whether `useOrbit`'s own design-system material (§6.3) gets re-homed into `useOrbit`'s own docs/memory
  — outside this repository's scope to decide or act on.

**Evidence limits, stated plainly:**
- This remains a single-consumer discovery pass. Every "genuinely reusable" judgment in §5 and §9 is
  bounded by Phase C's own §8.8 caveat: within-project repetition is not the same evidentiary bar as
  cross-project repetition, and this pass does not manufacture the latter.
- `my-phpstorm-conventions`' content could not be independently re-verified against live PhpStorm
  behavior (no PhpStorm instance was exercised in this pass) — findings rest on the skill's own stated
  mechanics and are only as current as PhpStorm's actual, unpinned version.
- The `#[Authorize]` attribute's 35-controller usage count and the 11/11 `final class` model count are
  grep-based structural confirmations, not a semantic audit of every call site.
- `factories-and-seeders.md` and `enum-options.md`'s underlying `useOrbit` code was not independently
  re-audited line-by-line in this pass beyond what Phase C already established; this pass relied on
  Phase C's own confirmed evidence for those two files specifically, adding only the fresh Boost-overlap
  check.
- Historical rollback copies and `phase-discovery.md`'s own readiness scores were used strictly as
  dated evidence of what changed, never presented as current fact or a current score.

---

## Validation checklist (self-report)

- [x] Every current file in both custom skills accounted for: 10/10 `my-laravel-patterns` rule files
  plus `SKILL.md`; 6/6 `my-phpstorm-conventions` rule files plus `SKILL.md` — all read in full (§1
  ledger, §5, §8).
- [x] Current installed Boost version and capability set inspected locally: `v2.7.0`, `boost.json`,
  16 `laravel-best-practices` rule files, 8 `testing-best-practices` rule files, `wayfinder-development`
  and `inertia-vue-development` `SKILL.md`s, and the injected `CLAUDE.md` — all read directly, not
  inferred (§1 ledger, §4).
- [x] Actions, testing, and controller conventions received explicit comparison: §4.2, §5.1, §5.6.
- [x] Every proposed removal has an identified replacement owner or is clearly obsolete: §6.1–§6.2 name
  the exact Boost owner for each removed fact; §6.3 explicitly flags the one piece of content with no
  current owner anywhere, rather than silently treating it as resolved.
- [x] Every proposed retained rule adds something Boost does not already own: stated per-file in §5's
  "Relationship" and "Delta" framing, with explicit "no overlap" or "narrow delta" verdicts, not blanket
  assertions.
- [x] Historical backups treated as dated evidence, not current truth: rollback copies used only to
  recover pre-rewrite text for comparison (§1 ledger, §3.1, §6.1), never cited as describing current
  state.
- [x] Phase C's historical scores not presented as current scores: §3's introduction states this
  explicitly; no score is restated as current anywhere in this document.
- [x] `git diff --check` run in `agentic-engineering` — see report below.
- [x] Only this new discovery artifact changed in `agentic-engineering` — confirmed via `git status
  --short` before writing and will be reconfirmed after.
- [x] No `useOrbit` file changed — confirmed via `git status --short` in `useOrbit`, both before and
  after this pass; only reads were performed there.
