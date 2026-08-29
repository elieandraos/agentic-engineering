# Phase D — Stack Discovery (Reconciliation Pass)

This is a focused reconciliation pass over the first discovery artifact. It does three things the
first pass did not: (1) records locked human context about the intended shape of the reusable stack,
(2) re-evaluates every candidate pattern against three distinct delivery mechanisms instead of
implicitly assuming a single companion skill, and (3) corrects a set of accuracy issues identified on
review. No skill was edited or created to produce this document. See `roadmap.md` §5 for Phase D's
charter and `phase-discovery.md` for the Phase C classification this document reverifies against
current reality.

---

## 0. Locked human context

Recorded as given, not re-derived from evidence — these are the boundaries this pass reasons inside,
not findings:

- **The reusable stack is specifically Laravel + Vue 3 + InertiaJS**, not "Laravel" in general. Laravel
  Boost owns the broader Laravel ecosystem baseline (validation, Eloquent, routing, testing mechanics,
  security, etc.). The custom layer's job, if one continues to exist, is the delta specific to this
  narrower Laravel+Vue+Inertia combination and to this user's own authoring conventions on top of that
  baseline — not a restatement of the baseline itself.
- **The custom Inertia testing macros in `TestingServiceProvider`** (`hasResource`,
  `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`)
  are intended to be ported to every Laravel/Inertia project this user works on. They are therefore
  **candidate reusable runtime support**, not merely `useOrbit`-specific application code that happens
  to be cited as an example. This changes their classification from Phase C and from the first
  discovery pass, both of which treated them only as an undisclosed dependency of `testing-strategy.md`
  to fix, not as a capability in their own right.
- **The likely result is a Boost companion capability** — but discovery must determine its *shape*
  (or shapes) from evidence, not assume one monolithic stack skill in advance. This pass evaluates
  every candidate pattern against three distinct delivery mechanisms (§1) precisely so that assumption
  isn't made by default.

---

## 1. Three delivery mechanisms

Before classifying any pattern, this section establishes what each mechanism actually is, verified
against Laravel Boost v2.7.0's real implementation and `useOrbit`'s actual current configuration —
not assumed from the mechanism's name or from Boost's own marketing description of it.

### 1.1 A task-triggered companion skill

A `SKILL.md` + `rules/*.md` bundle, loaded by trigger condition the way `my-laravel-patterns` and
`my-phpstorm-conventions` already are. Its natural responsibilities: workflow and composition guidance
("load this alongside that Boost skill"), decision guidance (naming conventions, structural choices,
when to reach for one pattern over another), prerequisite checks (state a dependency explicitly and
what to do when it's absent — e.g. the `getDiagnostics` tool, or the `TestingServiceProvider` macros),
and selective Boost-skill activation (telling the agent which Boost skill(s) a given task needs). This
is pure instruction — markdown an agent reads before acting. It travels with the user across projects
only if the user copies or re-installs the skill directory into each one; nothing about it is
automatically shared with a teammate who clones `useOrbit`, since `useOrbit/.claude/skills/my-*` is
gitignored (confirmed: `useOrbit/.gitignore` — see `UPSTREAM_PROVENANCE.md`'s framing of these as
personal, not project-tracked).

### 1.2 Durable repository conventions via Boost's `.ai/rules`

Verified directly against the installed `laravel/boost` v2.7.0 source
(`vendor/laravel/boost/src/Rules/RuleRepository.php`, `vendor/laravel/boost/src/Mcp/Tools/RecordRule.php`)
and `useOrbit`'s actual configuration, not inferred from Boost's own guideline prose:

- **Created, two ways.** (a) An agent calls the `record-rule` MCP tool with a `glob`, `title`, and
  `note`. `RuleRepository::write()` finds or creates an area file under `.ai/rules/` (named from the
  glob's meaningful path segments, e.g. `app/Http/Controllers/**` → `controllers.md`), adds the glob to
  that file's YAML frontmatter `paths:` list if not already present, and appends a `## Title\nNote`
  entry to the file body. (b) Separately, `boost:install`/`boost:update` can *extract* Boost's own
  path-scoped guideline content into a Boost-managed `.ai/rules/boost/` subdirectory
  (`RuleRepository::syncManaged()`), wiping and rewriting that subdirectory wholesale on every run —
  but only when `config('boost.rules.scoped_guidelines')` is enabled. **In `useOrbit`, this is
  currently disabled** (no `config/boost.php` override is published, and `.env` sets neither
  `BOOST_RULES_ENABLED` nor `BOOST_RULES_SCOPED_GUIDELINES` — both default from `laravel/boost`'s
  vendor config to `enabled: true`, `scoped_guidelines: false`). This means the `record-rule` tool is
  live and callable in `useOrbit` right now — `rules.enabled` defaults true — even though
  `.ai/rules/` does not yet exist, because nobody has called it and Boost's own managed-extraction
  feature is off by default.
- **Loaded.** `useOrbit/CLAUDE.md`'s injected "Project Rules" section instructs: before entering plan
  mode or creating/editing any file, open `.ai/rules/index.md`, read every rule file whose glob covers
  the path in scope, and additionally `grep -rin` the directory for keywords a glob match alone would
  miss.
- **Maintained.** `RuleRepository::writeIndex()` regenerates `.ai/rules/index.md` — a table of
  `glob → rule file` — on every `write()` or `syncManaged()` call. Individual area files accumulate
  entries by simple markdown append; there is no rule-deduplication or editing UI, only creation and
  accumulation.
- **Published.** There is no cross-project publication mechanism at all. `.ai/rules/` is a plain
  directory inside one repository's working tree, **not gitignored** by default (confirmed: no `.ai`
  entry in `useOrbit/.gitignore`) — if it existed, it would be a normal tracked, committed, team-shared
  file, visible to every teammate who clones `useOrbit`, the way `.claude/skills/my-*` currently is
  not. A rule recorded here lives only in this one repository; there is no Boost mechanism to copy a
  `.ai/rules` entry from one project into another. This makes `.ai/rules` structurally the opposite of
  a companion skill on the portability axis: **a companion skill is personal and travels across the
  user's own projects but is invisible to `useOrbit` teammates; `.ai/rules` is team-visible within
  `useOrbit` but does not travel anywhere else.**

### 1.3 Reusable executable runtime support

Actual PHP code whose behavior an instruction file cannot substitute for — a skill can tell an agent
to *write* this code, but the code itself, once written, is what does the work at test-run time. The
`TestingServiceProvider` macros are the clearest current example: `assertHasResource()` etc. exist
because a `ServiceProvider::boot()` method registered them via `Macroable::macro()` — no amount of
`rules/testing-strategy.md` prose makes that macro callable in a project that hasn't also registered
it. Distributing this kind of capability across projects requires the code itself to travel — as a
Composer package, a copy-paste-and-adapt stub, a skill-bundled file an agent is instructed to install,
or some other mechanism. **Which exact mechanism is not decided by this pass** — per the task's
instruction, packaging and installation choice is deferred to the synthesis pass. What this pass does
establish is that this is a materially different kind of thing than §1.1 or §1.2: neither a companion
skill nor `.ai/rules` can *be* the macros; at most either can *point at* or *carry instructions to
install* them.

---

## 2. Five-way ownership classification

Every candidate pattern in this document is classified into exactly one primary ownership category
(a pattern may additionally be *delivered* through more than one mechanism, per §1, without changing
its ownership):

- **Boost-owned** — Laravel Boost v2.7.0 already documents this; no custom material needed.
- **Companion workflow knowledge** — an authoring convention, decision rule, or Boost-composition
  instruction that generalizes across this user's Laravel+Vue+Inertia projects. Natural home: §1.1.
- **Persistent project rule** — a settled decision, non-obvious trap, or standing constraint whose
  evidence and value are currently scoped to `useOrbit` specifically (even if the underlying fact would
  also be true elsewhere, it hasn't been shown to recur). Natural home: §1.2.
- **Reusable executable support** — actual runtime code, not documentable as prose alone. Natural home:
  §1.3.
- **`useOrbit`-specific** — a product/design-system fact with no claimed cross-project generality at
  all (file mirrors, badge tones, literal issue links).

This replaces the first pass's implicit "Retain / Boost-owned / useOrbit-specific" three-way sort with
the five-way model the reconciliation requires, and separates *what owns a pattern* from *where it
lives*.

---

## 3. Executive conclusion (revised)

**A custom layer is still justified, but "custom layer" no longer means "one companion skill." The
evidence sorts into three different homes, not one, and the strongest single new finding of this
reconciliation pass is that `useOrbit`'s own current distribution choice — every custom skill
gitignored, `.ai/rules` unused — means none of this material is currently visible to a teammate who
clones the repository, regardless of what Phase D eventually decides about companion-skill shape.**

- **`my-phpstorm-conventions` remains the cleanest candidate for companion-skill treatment.** Every
  content finding from Phase C's two independent full reads still holds. Its `getDiagnostics`
  dependency is now identified with more precision than the first pass stated: it is Claude Code's
  built-in `mcp__ide__getDiagnostics` capability, but it only functions **when Claude Code is connected
  to an active, supported IDE integration** — this is not a universally available CLI tool, and a
  session without that integration gets no diagnostics at all, silently. This is exactly the kind of
  fact §1.1 calls a "prerequisite check": the skill should name the dependency and state what to do in
  its absence, not assume it.
- **`my-laravel-patterns`' content is genuinely additive over Boost v2.7.0 in most of its ten rule
  files.** The `#[Authorize]` attribute pattern is the strongest example — but "strongest" here rests
  specifically on the *portability* claim (no Boost coverage of the mechanism at all), which is
  independent of and should not be conflated with the *adoption* evidence (35 controller files use it
  in `useOrbit` today). Boost does use and name "Action" classes in its own examples
  (`architecture.md`'s "Extract Focused Business Operations," `routing.md`'s `CreatePostAction`) — Boost
  is not silent on the concept — it simply does not define this project's specific Action contract
  (naming, location, `$attributes` parameter, `afterCommit()` discipline, testing-ownership mapping).
  The correct claim is "Boost names the general pattern; it does not own this project's concrete
  implementation of it," not "Boost doesn't cover Actions."
- **Two of `my-laravel-patterns`' four Phase C defects are unchanged; the framing of a third needed
  correction.** `resources.md`'s `Inertia::render()` examples are **inconsistent with the verified
  current `useOrbit` convention and example** (`ClientsController.php` uses `inertia()` throughout) —
  both APIs are valid Inertia calls; this is an internal-consistency defect against the skill's own
  cited code, not a claim that `Inertia::render()` is invalid. The `assertDatabaseHas`/
  `assertModelExists` difference is a **discretionary testing-style preference where Boost states one
  default and `my-laravel-patterns` uses another**, not a forced binary the project must resolve one
  way — `my-laravel-patterns/SKILL.md:8`'s own precedence rule already gives the custom skill's
  convention priority when there is a difference; what's missing is a written acknowledgment that this
  specific point is where that precedence rule applies, not a resolution of "which one is correct." The
  broken `query-conditionals.md` example and dead `TagAttachment` citation are unchanged.
- **Boost v2.7.0's content is broader than Phase C could see, confirming the user's lead — at a
  principle level, not a content level.** Boost's `endpoint-tests.md` now states a general
  layer-ownership testing principle and `routing.md` now states a CRUD/resource-controller-organization
  philosophy. Neither absorbs this project's own concrete class taxonomy (Action, Filter) or its
  specific conventions.
- **Not every candidate pattern in this ecosystem is companion-skill material.** Re-evaluated against
  §1's three mechanisms: most of `my-laravel-patterns`' content is companion workflow knowledge with no
  runtime component. The `TestingServiceProvider` macros are the one clear case of reusable executable
  support (§0, §7). A `final`-by-default PHP class policy and a "don't test framework mechanics" testing
  preference currently live only in personal Claude memory — which is private and per-user, not a
  durable or team-shared mechanism at all — and are reclassified in §9 by what they actually are
  (companion workflow knowledge or persistent-project-rule candidates), not left as "memory findings."
- **A commit-message-format tension noted in the first pass has been removed from this document.** It
  concerns `my-git-workflow`, not the Laravel/Vue/Inertia stack layer, and does not belong in a
  stack-discovery artifact.
- **No recommendation is made here to combine, split, retire, or extract either custom skill, or to
  choose a skill name, packaging mechanism, or `.ai/rules` adoption decision.** Those remain Phase D
  synthesis decisions. §12 lays out what this evidence supports, tiered by mechanism.

---

## 4. Evidence and provenance ledger (additions and corrections)

This supplements, and where noted corrects, the first pass's ledger. Entries not listed here are
unchanged from the first pass.

| Source | What was checked | Method | Result |
|---|---|---|---|
| `useOrbit/vendor/laravel/boost/src/Rules/RuleRepository.php`, `src/Mcp/Tools/RecordRule.php` | How `.ai/rules` is actually created/loaded/maintained/published | Full source read | Verified mechanics recorded in §1.2 — this corrects the first pass's claim that `.ai/rules` was assessed only from `CLAUDE.md`'s guideline prose. |
| `useOrbit/vendor/laravel/boost/config/boost.php`, `useOrbit/.env` | Whether `.ai/rules` features are enabled | Direct read; `grep` for `BOOST_RULES_*` | No project override of `config/boost.php` exists; `.env` sets neither `BOOST_RULES_ENABLED` nor `BOOST_RULES_SCOPED_GUIDELINES`. Vendor defaults apply: `rules.enabled = true` (the `record-rule` tool is live now), `rules.scoped_guidelines = false` (Boost's own managed path-scoped extraction into `.ai/rules/boost/` is off). |
| `useOrbit/.gitignore` | Whether `.ai/rules` would be tracked if created | `grep -n "\.ai"` | No match — `.ai/` is not gitignored. If created, it would be a normal tracked, committed file, unlike `.claude/skills/my-*`, which is gitignored. |
| `useOrbit/.claude/skills/{laravel-best-practices,testing-best-practices}/rules/` | Boost rule-file counts | `ls \| wc -l` on each `rules/` directory | **Correction:** `laravel-best-practices/rules/` contains **19** files, not 16 as the first pass stated (the file list itself was complete; the stated count was an arithmetic error). `testing-best-practices/rules/` contains **9** files, not 8 (`security.md` was listed but not counted). All counts below and throughout this document use the corrected totals. |
| `~/.claude/projects/-Users-elieandraos-Desktop-Code-useOrbit/memory/` | Exact current memory file count | `ls -1`, `grep -c "^feedback_"` | **Correction:** **15** `feedback_*` files + 1 `project_design_files.md` + 1 `MEMORY.md` index = **17** files total, not "16 feedback + 1 project" as the first pass stated. Phase C recorded 16 feedback files; the current count of 15 is one fewer, alongside five files that postdate Phase C's snapshot — this pass did not investigate which specific pre-Phase-C feedback file(s) are no longer present, and does not assert a cause. |

---

## 5. What changed since Phase C, independent of content findings

Unchanged from the first pass except where corrected above: Boost was upgraded to v2.7.0 the same day
as this discovery (`composer.lock`, commit `b979d94`, 2026-08-29 00:19:44 +0300); the testing skill was
renamed `pest-testing` → `testing-best-practices`, and its content restructured from one `testing.md`
into **9** topic files (corrected from "eight"); `.ai/rules` remains unused in practice, though §1.2
now establishes precisely why it's unused (nobody has called `record-rule`; Boost's own managed
extraction is off by default) rather than simply noting its absence.

---

## 6. Phase C baseline versus current state (corrected framing)

Classification labels (still current / resolved / disproven / etc.) are unchanged from the first pass
except for the two entries corrected below; see the first-pass content for `resource-feature-checklist.md`
(§3.1 originally), the test-macro dependency (§3.2), the broken `query-conditionals.md` example (§3.4),
and the two combine/separate skills questions — none of that analysis changes here.

### 6.1 `assertDatabaseHas()` vs. `assertModelExists()` — reframed as a style preference, not a forced conflict

`testing-strategy.md:97` uses `assertDatabaseHas('clients', ['slug' => $client->slug])` for a `show`
endpoint's happy path. Boost's `testing-best-practices/rules/assertions.md` states its own general
default — `assertModelExists($model)` — as a decision-table row. **This is not a binary the project
must resolve by picking one assertion as universally correct.** Both are valid, working Pest/Laravel
assertions; Boost is stating its own baseline preference, and `my-laravel-patterns/SKILL.md:8`'s
existing precedence clause ("these take precedence over general Laravel best practices when there is a
conflict") already establishes that the custom skill's convention governs when the two differ. What is
actually missing is not a resolution but a written acknowledgment: nothing currently states, in either
file, "yes, this specific point is where the precedence rule applies, and it's deliberate." That
disclosure gap — not a correctness question — is what remains open.

### 6.2 `Inertia::render()` vs. `inertia()` — reframed as inconsistency, not invalidity

`resources.md`'s `Clients/Index`/`Clients/Show` examples use `Inertia::render()`. The controller they
claim to model, `app/Http/Controllers/Clients/ClientsController.php`, uses `inertia()` at every call
site. **Both are valid Inertia server-side calls** — `Inertia::render()` is not broken, deprecated, or
wrong on its own terms; `my-phpstorm-conventions/rules/inertia.md` documents it as triggering a PhpStorm
false-positive, not a functional defect. The finding is narrower and more precise than "the examples are
wrong": `resources.md`'s examples are **inconsistent with the verified current `useOrbit` convention and
the exact example file it cites**, and with `filters-pattern.md` elsewhere in the same skill. Fixing
this is a same-skill and cross-skill consistency correction, not a claim that one Inertia API is
categorically invalid.

### 6.3 `getDiagnostics` — identity confirmed, availability qualified

`useOrbit/.claude/settings.local.json` permission-lists `mcp__ide__getDiagnostics` alongside
`mcp__laravel-boost__*` tools. This confirms it is Claude Code's own built-in IDE-integration MCP
capability, not a JetBrains/PhpStorm-specific plugin tool — Iteration 2's speculation was too narrow in
the other direction. But the corrected claim is **not** "so it's generally available": this capability
is exposed only **when Claude Code is actively connected to a supported IDE integration** in the
current session. A session with no such IDE connected has no `mcp__ide__getDiagnostics` tool at all,
regardless of what editor or IDE is nominally in use on the machine. `my-phpstorm-conventions/SKILL.md:30`
still states no behavior for that case, and `feedback_phpstorm_skill_activation.md` (memory) documents
three prior real occurrences of the step not firing. The disclosure gap — name the dependency, state
what happens without it — is unchanged; only the precision of what's being disclosed is corrected here.

---

## 7. Current Boost capability / ownership map (corrected)

### 7.1 Installed state (corrected counts)

- **Version:** `laravel/boost v2.7.0` (constraint `^2.2`), upgraded from `v2.5.3` earlier the same day
  as this discovery.
- **`laravel-best-practices`** ships **19** files under `rules/`: `advanced-queries.md`,
  `architecture.md`, `blade-views.md`, `caching.md`, `collections.md`, `config.md`, `db-performance.md`,
  `eloquent.md`, `error-handling.md`, `events-notifications.md`, `http-client.md`, `mail.md`,
  `migrations.md`, `queue-jobs.md`, `routing.md`, `scheduling.md`, `security.md`, `style.md`,
  `validation.md`.
- **`testing-best-practices`** (renamed from `pest-testing`) ships **9** files under `rules/`:
  `assertions.md`, `endpoint-tests.md`, `finding-features.md`, `isolation.md`, `naming.md`,
  `performance.md`, `review.md`, `security.md`, `test-data.md`.
- Everything else in the first pass's §4.1 (`.mcp.json`, injected `CLAUDE.md`) is unchanged.

### 7.2 Actions — Boost names the pattern, does not own this project's contract

**Corrected claim.** Boost's `architecture.md` ("Extract Focused Business Operations") and `routing.md`
("Keep Controllers Focused on HTTP Concerns," with a `CreatePostAction` example) both use and name
Action classes. Boost is not silent on the concept, and it should not be described that way. What Boost
does not define: `app/Actions/{Domain}/` as a location convention, `{Verb}{Model}Action` naming,
`handle()` as a fixed method name (Boost's own example uses `execute()`), `$attributes` as a fixed
parameter name, the PHPDoc-shape-derived-from-FormRequest-rules algorithm, or the
`DB::transaction()`-pure/`->afterCommit()` side-effect discipline. This is the accurate boundary: Boost
owns the general pattern's existence and rationale; `my-laravel-patterns` owns this project's specific,
concrete contract for it.

### 7.3 What is confirmed still absent from Boost

Unchanged from the first pass: the `#[Authorize]` attribute mechanism itself (as distinct from
`useOrbit`'s adoption of it — see §8.4), the class-based `QueryFilter`/`Filterable` pattern,
`prepareForValidation()`-owns-normalization as a named discipline, the factory realism conventions, the
enum `::all()` convention, and anything about PhpStorm/IDE static analysis.

---

## 8. Passage-level `my-laravel-patterns` overlap matrix (with delivery mechanism and ownership)

Each entry keeps the first pass's Boost-overlap finding (unchanged unless noted) and adds the ownership
category (§2) and delivery mechanism (§1) this reconciliation determines.

### 8.1 `actions-pattern.md`

- **Boost overlap:** Partial — philosophy-level only (§7.2). Concrete contract (location, naming,
  `handle()`, `$attributes`, `afterCommit()` discipline) has no Boost equivalent.
- **Ownership:** Companion workflow knowledge.
- **Mechanism:** Companion skill (§1.1) — this is authoring guidance an agent needs at the moment it
  writes an Action class, portable across this user's Laravel+Vue+Inertia projects in principle. No
  runtime component; nothing here requires §1.3.
- **useOrbit evidence:** `app/Actions/**` follows this shape (corroborated via the `#[Authorize]`
  controller sample and factory evidence elsewhere in this pass) — single-consumer evidence.
- **Disposition:** No change to the underlying recommendation from the first pass (retain the concrete
  contract; optionally trim the philosophy framing now that Boost states the general case).

### 8.2 `enum-options.md`

- **Boost overlap:** None found.
- **Ownership:** Companion workflow knowledge.
- **Mechanism:** Companion skill.
- **useOrbit evidence:** Phase C's own inspection previously confirmed real usage; **this pass did not
  independently re-audit every enum in the codebase.** Corrected disposition: this is not a fully
  confirmed keep so much as "no evidence found against it, and no fresh check performed" — flagged
  explicitly rather than stated as a settled "retain as-is."

### 8.3 `factories-and-seeders.md`

- **Boost overlap:** Partial, narrow — `testing-best-practices/rules/test-data.md` now endorses `for()`
  generally but states no derived-vs-copied decision criterion; the field-derivation, email-generation,
  and date-chaining content has no Boost equivalent.
- **Ownership:** Companion workflow knowledge.
- **Mechanism:** Companion skill.
- **useOrbit evidence:** Internal consistency with `authorization.md`'s scoping examples was checked;
  **the underlying factory code was not independently re-audited in this pass.** Corrected disposition:
  no evidence found requiring change, but the "retain" conclusion rests on Phase C's earlier check, not
  a fresh one performed here — stated as a limit, not asserted as current proof.

### 8.4 `authorization.md` — portability and adoption evidence separated

- **Boost overlap:** None. `security.md`'s "Authorize Protected Actions" covers `Gate::authorize()` and
  FormRequest `authorize()`; neither documents the `#[Authorize]` routing attribute at all.
- **Ownership:** Companion workflow knowledge.
- **Mechanism:** Companion skill.
- **Two distinct evidentiary claims, kept separate as requested:**
  1. **Portability evidence:** the `#[Authorize]` attribute mechanism, including its documented
     string-vs-array-form resolution subtlety, is a real Laravel capability with zero Boost coverage —
     this claim does not depend on how much `useOrbit` uses it.
  2. **Adoption evidence:** 35 controller files in `useOrbit` use `#[Authorize(...)]`; the base
     `Controller` class does not use `AuthorizesRequests`. This is real, current, and widespread —
     **within this one project.** Per Phase C's own §8.8 caveat (repeated throughout this pass), heavy
     single-project adoption is evidence the pattern is load-bearing here; it is not, by itself,
     cross-project portability evidence. The two claims support the same disposition together, but
     neither substitutes for the other, and the "strongest keep in the ecosystem" framing in the first
     pass conflated them.
- **Disposition:** No change to the underlying recommendation — retain — but justified on the
  portability claim, with the adoption claim named as corroborating, single-consumer evidence rather
  than proof of reusability on its own.

### 8.5 `resources.md`

- **Boost overlap:** No dedicated API-Resources content; `db-performance.md`'s
  `Model::preventLazyLoading()` recommendation is named by `resources.md:75` itself as the condition its
  own rule depends on — confirmed absent from `AppServiceProvider.php`.
- **Ownership:** Companion workflow knowledge (Resource-wrapping/`whenLoaded()` discipline);
  `useOrbit`-specific for the literal `Inertia::render()` examples pending the fix in §6.2.
- **Mechanism:** Companion skill.
- **Disposition:** Fix the Inertia-call examples for internal consistency (§6.2) — not because
  `Inertia::render()` is invalid, but because the file's own cited example no longer matches it. Flag,
  don't act on, the `preventLazyLoading()` dependency.

### 8.6 `testing-strategy.md`

- **Boost overlap:** Partial on the layer-ownership *principle* (Boost's `endpoint-tests.md` states a
  general version); the `assertDatabaseHas`/`assertModelExists` difference is a style preference, not a
  conflict (§6.1).
- **Ownership:** Split — the Action/Controller/Policy/Filter mapping and no-duplication discipline is
  companion workflow knowledge; the five macros it depends on (`hasResource`, `hasPaginatedResource`,
  `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`) are **reusable executable
  support** (§0, §9).
- **Mechanism:** Companion skill for the mapping/discipline; §1.3 (mechanism undecided) for the macros
  themselves, since this rule file's examples are not runnable without that code existing in the
  consuming project.
- **Disposition:** Unchanged from the first pass on substance (trim the now-Boost-stated general
  principle; state the macro dependency as an explicit prerequisite or, per §0's new context, as a
  cross-referenced executable-support capability the companion skill assumes is installed).

### 8.7 `filters-pattern.md`

- **Boost overlap:** None.
- **Ownership:** Companion workflow knowledge for the pattern's documentation; **open question** for
  the `QueryFilter`/`Filterable` base classes themselves — this pass has no evidence, one way or the
  other, that the user intends to port the actual base-class code across projects the way the
  `TestingServiceProvider` macros are intended to be ported (§0). If that intent exists, the base
  classes would also be reusable executable support; if not, each project re-authors its own base
  classes from the documented pattern. Not resolved here — a question for the synthesis pass, not an
  assumption this pass makes either way.
- **Mechanism:** Companion skill (pattern); possibly §1.3 (base classes), pending the open question
  above.
- **useOrbit evidence:** Live, resolvable `useOrbit`-repository issue links (`#76`, `#71`) and an
  arbitrary `paginate(7)` literal remain in the example — `useOrbit`-specific fingerprints that would
  need scrubbing before any cross-project distribution, regardless of which mechanism is chosen.

### 8.8 `request-normalization.md`

- **Boost overlap:** None — Boost's `validation.md` covers validation extraction and rule syntax, not
  coercion/defaulting discipline.
- **Ownership:** Companion workflow knowledge.
- **Mechanism:** Companion skill.
- **useOrbit evidence:** Checked only for internal consistency with `filters-pattern.md`'s wiring
  example; **not independently re-verified against live `useOrbit` FormRequest code in this pass.**
  Corrected disposition: no evidence found against it, but this is a not-yet-re-verified carryover from
  Phase C, not a fresh confirmation — stated as a limit rather than a settled "retain unchanged."

### 8.9 `eloquent-attributes.md`

- **Boost overlap:** Substantial — Boost's `eloquent.md` fully documents `#[Scope]` itself. Unchanged
  from the first pass.
- **Ownership:** Companion workflow knowledge, narrowed to the delta (migration framing, the `❌ scopeXxx`
  counter-example, the Laravel version pin).
- **Mechanism:** Companion skill.
- **Disposition:** Unchanged — reduce to the narrow delta rather than restating Boost's own content.

### 8.10 `query-conditionals.md`

- **Boost overlap:** None.
- **Ownership:** Companion workflow knowledge.
- **Mechanism:** Companion skill.
- **Disposition:** Unchanged — fix or replace the broken example; the underlying rule needs no content
  change.

### 8.11 `SKILL.md` staleness (`pest-testing` → `testing-best-practices`)

Unchanged from the first pass: both `SKILL.md` files still name the old Boost skill. This is a
correctness fix independent of any mechanism or ownership decision.

---

## 9. Reusable executable support — the `TestingServiceProvider` macros

Given §0's locked context, this capability is analyzed on its own rather than folded into
`testing-strategy.md`'s "Boost overlap" framing as the first pass did.

- **What it is.** `app/Providers/TestingServiceProvider.php` registers five macros at test-runtime:
  `AssertableInertia::macro('hasResource', ...)`, `AssertableInertia::macro('hasPaginatedResource', ...)`,
  `TestResponse::macro('assertHasResource', ...)`, `TestResponse::macro('assertHasPaginatedResource', ...)`,
  `TestResponse::macro('assertHasInertiaFlash', ...)`. Confirmed present and functioning exactly as
  `testing-strategy.md` assumes.
- **Ownership:** Reusable executable support — this is code, not a convention a skill file can
  substitute for.
- **Mechanism:** Genuinely undecided (§1.3) — a Composer package, a distributable stub file, a
  skill-bundled installer step, or something else are all structurally possible; none is chosen here,
  per the task's instruction to defer packaging/installation decisions to synthesis.
- **Boost overlap:** None — Boost ships no equivalent Inertia-testing macro set.
- **useOrbit evidence:** Real, current, and exercised by every controller test that calls
  `assertHasResource`/`assertHasPaginatedResource`/`assertHasInertiaFlash` — but this is still evidence
  from **one project's one implementation**. §0's locked context establishes the *intent* to port this
  code elsewhere; it does not yet constitute evidence that the code has been successfully exercised as
  a separately distributed capability outside `useOrbit`. That has not happened yet, and this pass does
  not claim otherwise.
- **Disposition:** Not a "retain unchanged" or "extract" call — this is the one candidate in the entire
  ecosystem that cannot be settled by editing a skill file at all. Whatever Phase D decides about a
  companion skill's shape, this capability's distribution is a separate decision requiring its own
  mechanism choice.

---

## 10. `my-phpstorm-conventions` analysis (mechanism note added)

The content-level analysis is unchanged from the first pass: reusable custom tooling capability, zero
`useOrbit` product-domain leakage across two independent full reads, zero Boost overlap, one shared
defect with `my-laravel-patterns` (the Inertia-call reconciliation, §6.2).

**Mechanism, newly considered:** every finding in this skill is companion workflow knowledge, delivered
through §1.1 — decision guidance ("here's the false-positive and its fix") plus, specifically for
`getDiagnostics`, a prerequisite check (§1.1's own stated responsibility: name a dependency, state the
fallback). Nothing in this skill is reusable executable support (no runtime code is shipped or
implied) and nothing in it is currently a `.ai/rules` candidate on its own terms — its content isn't a
`useOrbit`-specific settled decision so much as a portable IDE-mechanics fact, which is exactly why it
belongs in a companion skill rather than a per-repo rule file.

---

## 11. Recovered material from the three canonical skills, and new evidence — reclassified

This replaces the first pass's §6–§7 with corrected ownership classification. Findings not restated
here (the resolved `resource-feature-checklist.md` rewrite, the resolved memory-dependency removals
from `my-feature-planning`, the `my-architecture-laboratory` syntax-highlighter note) are unchanged
from the first pass.

### 11.1 Removed Wayfinder and verification-command facts — Boost-owned

Unchanged from the first pass: the `wayfinder:generate --with-form` fact is now Boost's own documented
content (`wayfinder-development/SKILL.md`); the exact `php artisan test --compact`/`vendor/bin/pint
--dirty --format agent` commands removed from `my-git-workflow/verification.md` are Boost-owned via
`useOrbit/CLAUDE.md`'s injected foundation rules, not any skill file. No recovery needed; no mechanism
decision required.

### 11.2 Removed `useOrbit` design-system content — `useOrbit`-specific

Unchanged from the first pass: badge tones, breadcrumb rules, header breakpoints, file/class mirrors
removed from `resource-feature-checklist.md` are `useOrbit`'s own product convention, preserved only in
git history and rollback copies. If this needs a durable home at all, it belongs in `useOrbit`'s own
`_docs/` or, now that its mechanics are verified (§1.2), potentially `.ai/rules` — not a companion
skill, since none of it generalizes past this product. Out of `agentic-engineering`'s scope either way.

### 11.3 `feedback_final_classes.md` — reclassified by ownership, not "memory as source"

**Fact, unchanged:** this memory entry states a project-wide `final`-by-default policy for every PHP
class type, verified against 11/11 current `app/Models/*.php` files and confirmed absent from all 19
`laravel-best-practices` rule files.

**Corrected framing.** The first pass treated this as "a real gap living in memory, worth adding to a
skill." That undersells what memory actually is here: personal Claude memory is private to this user's
sessions, not committed to `useOrbit`, not visible to a teammate, and not a mechanism Boost or
`agentic-engineering` treats as durable. It is not a fourth delivery mechanism competing with §1's
three — it's closer to a scratch note that hasn't yet been given a real home. Classified by what it
actually is:

- **If this convention is intended to travel across this user's other Laravel projects** (consistent
  with the general, house-style phrasing the memory itself uses — "the user prefers to start final and
  remove it explicitly only when inheritance is required," stated with no `useOrbit`-specific
  qualifier): **companion workflow knowledge**, delivered via §1.1, once evidence exists beyond this one
  project.
- **Regardless of that broader question, it is already a "settled decision" by Boost's own definition
  of what `record-rule` is for** ("a settled decision... or a standing constraint that must always be
  followed"). It could be recorded into `useOrbit/.ai/rules` **today**, independent of any companion-skill
  decision, giving `useOrbit` teammates visibility into a convention that currently has none — the
  `.ai/rules` route does not require the broader companion-skill question to be resolved first.
- **Not Boost-owned, not `useOrbit`-specific** (it's a house-style choice about PHP, not a product
  fact), **not reusable executable support** (nothing here is runtime code).

### 11.4 `feedback_no_tests_for_framework_behavior.md` vs. Boost's `review.md` — reclassified

**Fact, unchanged:** the memory entry records a user-confirmed, incident-backed preference (issue #107)
against testing bare framework mechanics (an Eloquent `casts()` enum mapping, a morph-map resolution).
Boost's `testing-best-practices/rules/review.md` states, plainly read, that a test of "what this project
configures, such as a relation with a constraint, a cast, or a scope, belongs to this project" — which
on a plain reading includes exactly the category of test the user rejected.

**Corrected framing.** As with §11.3, this is not "memory versus Boost" as if memory were a competing
durable source — it's an unrecorded testing-philosophy decision that happens to currently exist only as
a private note, now found to be in tension with Boost's stated default. Classified:

- **This already meets Boost's own "settled decision" bar for `record-rule`** — it was confirmed once,
  concretely, in a real incident. It is a strong candidate to record into `useOrbit/.ai/rules` now,
  independent of whether it later also becomes companion workflow knowledge.
- **Whether it generalizes to companion workflow knowledge** (a testing-philosophy rule for any
  Laravel/Inertia project this user works on) is unresolved — this pass has only one project's evidence
  for it, the same evidentiary bar every other candidate in this document is held to.
- **The conflict with Boost's `review.md`** is a real, current tension between what this project's
  evidence supports and what Boost's own new guidance states as its plain-reading default. Neither side
  is silently chosen as the winner here — that remains a human decision (§13).

### 11.5 `feedback_migration_notnull.md` — reclassified

**Fact, unchanged:** a narrow, single-incident API correction (`->notNull()` does not exist on
migration column definitions; PhpStorm's warning is correct, not a false positive). Not covered by
Boost's `migrations.md`.

**Corrected framing.** This is precisely the shape Boost's own `record-rule` description calls a
"non-obvious trap" — narrower and more mechanical than a skill-worthy convention, but exactly what
`.ai/rules` exists for. Reclassified from "leave in memory" (first pass) to: **persistent-project-rule
candidate for `.ai/rules`**, not a companion-skill candidate (too narrow to warrant a rule file an agent
reads on every relevant task) and not something that should simply stay in private memory indefinitely
if the goal is for this correction to actually persist and be discoverable by anyone else working in
`useOrbit`.

---

## 12. Summary table — ownership and mechanism

| Pattern | Ownership | Mechanism(s) | Boost overlap | Disposition |
|---|---|---|---|---|
| `#[Authorize]` attribute pattern | Companion workflow knowledge | Companion skill | None (portability); heavy single-project adoption (35 controllers) is separate, corroborating evidence, not proof of portability on its own | Retain; keep the two evidence classes distinct in any future writeup |
| `QueryFilter`/`Filterable` pattern (docs) | Companion workflow knowledge | Companion skill | None | Retain; scrub `useOrbit` issue links/literals before any cross-project use |
| `QueryFilter`/`Filterable` base classes (code) | Open — possibly reusable executable support | Undecided (§1.3), pending human intent | N/A | Not resolved — flagged as an open question, not assumed either way |
| `prepareForValidation()` discipline | Companion workflow knowledge | Companion skill | None | No evidence against retaining; not freshly re-audited this pass |
| Enum `::all()` convention | Companion workflow knowledge | Companion skill | None | No evidence against retaining; not freshly re-audited this pass |
| Factory/seeder realism conventions | Companion workflow knowledge | Companion skill | Narrow (`for()` endorsement) | No evidence against retaining; not freshly re-audited this pass |
| Actions pattern (naming/location/`$attributes`/`afterCommit`) | Companion workflow knowledge | Companion skill | Partial — Boost names Actions generally, not this contract | Retain concrete contract |
| Layer-ownership testing mapping | Companion workflow knowledge | Companion skill | Partial — principle now stated generally by Boost | Trim generic framing; keep concrete mapping |
| Inertia testing macros (`hasResource` et al.) | Reusable executable support | Undecided (§1.3) | None | Distribution mechanism deferred to synthesis; not yet exercised outside `useOrbit` |
| `#[Scope]` documentation | Companion workflow knowledge | Companion skill | Substantial | Reduce to narrow delta |
| `when()` query conditionals | Companion workflow knowledge | Companion skill | None | Retain; fix broken example |
| Resource-wrapping/`whenLoaded()` discipline | Companion workflow knowledge | Companion skill | None (self-flagged dependency on an unadopted Boost practice) | Retain; fix Inertia-call examples for internal consistency, not because either API is invalid |
| PhpStorm/Pest IDE-workaround set | Companion workflow knowledge | Companion skill (decision guidance + prerequisite check) | None | Retain; disclose `getDiagnostics`'s active-IDE-integration dependency and a fallback |
| `final`-by-default PHP class policy | Companion workflow knowledge (if it recurs) and/or persistent project rule (today) | `.ai/rules` now; companion skill pending cross-project evidence | None | Human decision on companion-skill inclusion; `.ai/rules` recording does not require that decision first |
| No-tests-for-framework-behavior preference | Persistent project rule (today); possibly companion workflow knowledge later | `.ai/rules` now | Conflicts with Boost `review.md`'s plain reading | Human decision on the Boost conflict; `.ai/rules` recording does not require it resolved first |
| Migration `->notNull()` trap | Persistent project rule | `.ai/rules` | None | Too narrow for a skill; good `.ai/rules` fit |
| Removed `useOrbit` design-system content | `useOrbit`-specific | `useOrbit`'s own `_docs/` or `.ai/rules` | N/A | Out of `agentic-engineering` scope |

---

## 13. Decomposition options and trade-offs (revised for three mechanisms)

Presented as options, not a recommendation:

1. **Keep the current shape (two companion skills) for workflow knowledge; leave `.ai/rules` unused;
   leave the macros undistributed.** Lowest disruption. Misses the team-visibility benefit `.ai/rules`
   would give `useOrbit` collaborators today, and leaves the macros' cross-project intent (§0)
   unrealized.
2. **Adopt `.ai/rules` for `useOrbit`-durable and settled-decision material now** (§11.3–§11.5),
   independent of any companion-skill restructuring — the mechanism is already live
   (`rules.enabled = true` by default) and requires no Phase D skill decision to start using. This is
   the one option that doesn't wait on any other decision in this document.
3. **Treat the macros as a distinct workstream from the companion skill(s) entirely** — their
   distribution mechanism (§1.3) is orthogonal to whether `my-laravel-patterns`/`my-phpstorm-conventions`
   combine, split, or stay as-is; deciding one does not require deciding the other.
4. **Refine `my-laravel-patterns`'s companion-skill content and `my-phpstorm-conventions` on
   independently-timed tracks**, per the asymmetric defect profile the first pass already established —
   unchanged by this reconciliation.

No adapter-folder structure, package name, `.ai/rules` adoption decision, or macro-distribution
mechanism is chosen by any option above.

---

## 14. Recommended Phase D disposition and implementation order (revised)

**Tier 1 — correctness fixes, no design decision required:**
1. Replace `pest-testing` with `testing-best-practices` in both `SKILL.md` files.
2. Reconcile `resources.md`'s Inertia-call examples with `filters-pattern.md` and the actual
   `ClientsController.php` convention — framed as internal-consistency, not API-validity.
3. Fix or replace `query-conditionals.md`'s broken example and dead citation.

**Tier 2 — disclosure fixes:**
4. State the `TestingServiceProvider` macro dependency explicitly wherever `testing-strategy.md`
   assumes it — and note, per §0, that this dependency is now understood as an executable-support
   capability with its own eventual distribution story, not just an undisclosed local fact.
5. Name `getDiagnostics`'s actual nature (Claude Code's built-in capability, active only with a
   connected supported IDE integration) and state a fallback for a session without it.

**Tier 3 — can start now, independent of any companion-skill decision:**
6. Record `feedback_final_classes.md`'s policy, `feedback_no_tests_for_framework_behavior.md`'s
   testing preference, and `feedback_migration_notnull.md`'s trap into `useOrbit/.ai/rules` via
   `record-rule` — the mechanism is live today and needs no Phase D skill decision first (§13, option 2).

**Tier 4 — human decisions this evidence surfaces but does not resolve (§15):**
7. Whether to write down, rather than silently apply, `my-laravel-patterns`' precedence rule at the
   `assertDatabaseHas`/`assertModelExists` point specifically.
8. Whether `feedback_no_tests_for_framework_behavior.md`'s preference should override, narrow, or
   accept Boost's `review.md` default.
9. Whether the `QueryFilter`/`Filterable` base classes are intended for cross-project runtime reuse
   like the testing macros, or remain a documented pattern each project re-authors.
10. The macros' actual distribution mechanism (package, stub, skill-bundled install step, or other) —
    explicitly deferred to synthesis, not decided here.
11. Whether the two companion skills combine, stay separate, or proceed on independent timelines.
12. Whether `eloquent-attributes.md` is trimmed to its narrow delta now or later.

**Tier 5 — deferred, out of this pass's evidence:**
13. `useOrbit`'s own removed design-system material, re-homing decision.
14. Anything gated on cross-project evidence a single-consumer pass cannot supply.

---

## 15. Unresolved human decisions and evidence limits

**Human decisions, explicitly not made here:**
- Whether the `#[Authorize]`, Filters, normalization, enum, factory, and testing-layer conventions in
  `my-laravel-patterns` become one companion skill, several, or stay as-is (§13, §14.11).
- Whether `.ai/rules` is adopted for `useOrbit` at all — it is technically live, but adopting it as a
  practice is still a human choice, not something this pass decides on the user's behalf (§13, option 2;
  §14.6).
- The `assertDatabaseHas`/`assertModelExists` and no-tests-for-framework-behavior tensions with Boost
  (§6.1, §11.4) — flagged, not resolved.
- Whether the `QueryFilter`/`Filterable` base classes and the enum `::all()` mapping should become
  reusable executable support like the testing macros, or remain documented patterns (§8.7, §14.9).
- The macros' actual distribution mechanism — package, stub, or otherwise (§9, §14.10).
- Whether `eloquent-attributes.md` is trimmed now or later.

**Evidence limits, stated plainly:**
- This remains primarily evidence from Laravel Boost's installed source plus **one real consumer**,
  `useOrbit`. Every "genuinely reusable" or "companion workflow knowledge" classification in §8–§12 is
  bounded by that single-project evidentiary ceiling — repeated here because it applies to nearly every
  row in §12, not just the ones explicitly flagged as "not freshly re-audited."
- The `TestingServiceProvider` macros are intended for cross-project use (§0) but **have not yet been
  exercised as a separately distributed capability outside `useOrbit`.** Their current evidence is
  entirely single-project; the intent to generalize them is a human statement of goal, not evidence the
  generalization has already succeeded.
- `enum-options.md`, `factories-and-seeders.md`, and `request-normalization.md`'s "no evidence against
  retaining" dispositions rest on Phase C's earlier checks, not a fresh line-by-line re-audit performed
  in this pass — stated explicitly in §8 and §12 rather than implied by a flat "retain."
- `my-phpstorm-conventions`' content could not be independently re-verified against live PhpStorm
  behavior; no PhpStorm instance was exercised in this or the prior pass.
- The memory-file count discrepancy noted in §4 (15 current feedback files versus Phase C's recorded 16)
  was not investigated further — this pass does not know which file(s) changed or why, and does not
  guess.

---

## Validation checklist (self-report)

- [x] Locked human context recorded verbatim as given, not re-derived (§0).
- [x] Three delivery mechanisms verified against Boost's actual installed source and `useOrbit`'s actual
  configuration before any claim was made about how `.ai/rules` is created, loaded, published, or
  maintained (§1.2, sourced from `RuleRepository.php`, `RecordRule.php`, `config/boost.php`, `.env`,
  `.gitignore` — not from `CLAUDE.md` prose alone).
- [x] Every candidate retained pattern classified into one of the five ownership categories, with
  mechanism(s) named separately from ownership (§8–§12).
- [x] No Boost material duplicated to make any companion candidate self-contained — every entry in §8
  and §12 states what Boost already owns and confines the companion classification to the delta.
- [x] Boost file counts and totals reconciled: `laravel-best-practices` corrected to 19, `testing-best-practices`
  corrected to 9, throughout (§4, §5, §7.1).
- [x] "Boost does not name Actions" corrected to "Boost names the general pattern, not this project's
  contract" (§3, §7.2).
- [x] `mcp__ide__getDiagnostics` described as dependent on an active, supported IDE integration, not
  universally available (§3, §6.3, §14.5).
- [x] `#[Authorize]` portability evidence (no Boost coverage) and adoption evidence (35 controllers)
  kept as two distinct claims (§8.4, §12).
- [x] `assertDatabaseHas`/`assertModelExists` reframed as a style preference with an existing precedence
  rule, not a forced binary (§6.1).
- [x] `Inertia::render()` described as inconsistent with the verified current convention/example, not
  inherently invalid (§6.2, §8.5).
- [x] `feedback_final_classes.md` and `feedback_no_tests_for_framework_behavior.md` classified by
  ownership (companion workflow knowledge / persistent project rule), not presented as memory being a
  durable source in itself (§11.3, §11.4).
- [x] The `my-git-workflow` commit-message/body tension from the first pass has been removed from this
  artifact — that topic belongs to a different skill's methodology, not the stack layer.
- [x] "Retain" dispositions without a fresh `useOrbit` re-check (`enum-options.md`,
  `factories-and-seeders.md`, `request-normalization.md`) now state that limit explicitly rather than
  asserting a settled keep (§8.2, §8.3, §8.8, §12, §15).
- [x] No final skill name, Composer packaging, or installation mechanism chosen — all deferred to
  synthesis (§9, §14.10, §15).
- [x] Confidence boundaries preserved: evidence is primarily Boost-plus-one-consumer, and the runtime
  macros are explicitly noted as not yet exercised as a separately distributed capability (§15).
- [x] `git diff --check` run in `agentic-engineering` — see report below.
- [x] Only `phase-d-stack-discovery.md` changed in `agentic-engineering`.
- [x] No `useOrbit` file changed — only reads were performed there, including inside `vendor/laravel/boost`.
