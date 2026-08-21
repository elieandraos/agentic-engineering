# Resource / CRUD Feature Checklist

Load this when `rules/feature-classification.md` says **A (new resource)**, or for the CRUD-shaped slice of **C (extension)**. Every track below must be explicitly resolved (yes/no + what) for a new resource — never silently assumed. An example from this project: Phase 17 (Carriers) only planned the first track upfront; every other track got retrofitted as new issues after the fact, discovered ad hoc rather than planned. This file exists so that doesn't happen again.

The generic rule is the track structure itself (A–G: core infra, status lifecycle, sub-resources, filters/sorting, export, frontend UX consistency, wiring gotchas) — every resource-shaped feature in any codebase needs some answer to each of these. The specific classes, file names, and UI conventions cited under each track are this project's Laravel/Vue answer to that track, not the universal rule; another project would walk the same tracks against its own stack's equivalents.

The pieces named below (Actions pattern, FormRequest normalization, API Resources, filters, factories/seeders) have their implementation conventions maintained in `my-laravel-patterns` and `laravel-best-practices` — load those when implementation starts. This checklist only needs to name the pieces well enough to scope issues correctly; it doesn't require those skills to be loaded during planning.

## Track A — Core resource infra

Always applies. One issue per item below is the Phase 17 precedent, but they can be combined into fewer issues if the feature is small.

- Migration(s): table with `organization_id`, `slug` (if user-facing routing needs one), status/lifecycle column, `created_by`/`updated_by`, soft deletes, indexes on `organization_id` and `[organization_id, status]`
- Model: `BelongsToCurrentOrganization`, `HasSlug` (if applicable), `HasFactory`, `SoftDeletes` — mirrors `app/Models/Carrier.php`
- Factory (+ any named states like `archived()`) and a dev seeder
- Policy: `viewAny`/`view`/`create`/`update`/`delete`, gated to Owner where the action is destructive/irreversible — mirrors `app/Policies/CarrierPolicy.php`
- FormRequests (`Store{X}Request`, `Update{X}Request`)
- API Resource (`{X}Resource`)
- Thin controller, Actions pattern
- Routes file, `require`d from `web.php` inside the standard `['auth', 'verified', 'organization']` group
- **Nav link** — its own one-line issue (`resources/js/components/shell/navItems.ts`), easy to forget since it's trivial
- Index/create/show/edit Vue pages, **index empty state** as its own concern (mirrors Carriers #206)

## Track B — Status lifecycle (archive/unarchive)

Ask: does this resource get archived (soft-hidden but recoverable) as distinct from deleted (permanent, Owner-only, soft-deleted in DB)?

If yes:
- `Archive{X}Action` / `Unarchive{X}Action`, invokable controllers, Owner-gated policy abilities — mirrors `app/Actions/Carriers/{Archive,Unarchive}CarrierAction.php`
- **Frontend wiring is a separate concern from the backend endpoint** — Carriers had the unarchive endpoint since issue #203 but it wasn't surfaced in the drop-menu until much later. Plan the UI wiring as its own issue, don't assume it rides along with the backend issue.
- The index's default filter should exclude archived records (see Track D) — don't ship archive without also planning how archived records get filtered/viewed.

## Track C — Sub-resource / child CRUD

Ask: does this resource have a child entity that needs its own add/edit/delete (e.g. Carrier → CarrierBranch)? Not every feature has this — don't assume it away, and don't assume it's needed either.

If yes, the child gets its **own full Track A** (migration, model, policy, requests, resource, actions, controller, routes, tests) plus:
- Child policy's `create` ability is authorized differently from `update`/`delete` (a common Laravel model-policy nuance — worth a reminder here, detail lives in `my-laravel-patterns` at implementation time).
- A modal-based add/edit UI on the parent's show page (mirrors `BranchModal.vue` + `BranchesCard.vue`), with a header count badge (mirrors the Documents card pattern) and per-row edit/delete icons.
- If the parent's create/edit form previously captured one instance of the child inline (e.g. "the HQ branch" during carrier creation), plan explicitly whether the edit form keeps doing that or defers entirely to the child's own CRUD once it exists — Carriers dropped it from the edit form (kept it on create, since you need at least one child to start) as its own issue.

## Track D — Filters + sorting

Ask: what's actually filterable/sortable for this resource? At minimum: search (which columns?) and archived-status toggle (if Track B applies). Additional filters are feature-specific (compare Clients: gender, age range, enrollment date, client type).

- `{X}Filter extends QueryFilter`, `Filterable` trait
- `{X}Sort extends Sort`, `Sortable` trait — same base classes Clients/Carriers both reuse, no new infra needed
- `IndexRequest` validates `search`/`sort`/`direction`/whatever filters apply; defaults matter (e.g. `archived` defaults to `false` so the index doesn't show archived records unless asked)
- Frontend: sortable column header(s) with asc/desc chevrons, a `FiltersDrawer.vue` (search + toggles), active-filter-count badge on the Filters button

## Track E — Export (two distinct shapes, don't conflate)

Ask which of these apply — they're separate issues with separate controllers/routes, not one "export feature":
- **Bulk Excel from the index** — respects current filters/sort, one route (`GET {resource}/export`), one `{X}Export` class (`FromQuery`/`WithHeadings`/`WithMapping`), one `Export{X}sToExcelAction`
- **Per-record PDF from the show page** — one route (`GET {resource}/{id}/export`), one blade view under `resources/views/exports/`, one `Export{X}ToPdfAction`

**Route-ordering gotcha:** the bulk-export route (`{resource}/export`) must be registered *before* the wildcard show route (`{resource}/{id}`), or the wildcard swallows it and "export" gets treated as an ID.

## Track F — Frontend pages & UX consistency

- **Breadcrumb rule**: index pages get **no breadcrumb**; show/edit pages do (via `setLayoutProps`/`defineOptions`). Got this wrong on Carriers' index once.
- **Index header, mobile vs. desktop** — mirrors `ClientsIndexHeader.vue`/Carriers' `Index.vue`: mobile is a `sm:hidden` row with the primary "Add" action on the left and Filters + icon-only (no label) Export on the right; desktop (`hidden sm:inline-flex`) shows all three buttons with full labels. The meta badge/sort-label row is `hidden sm:flex` (not shown on mobile at all).
- **Show header, mobile vs. desktop** — mirrors `ClientShowHeader.vue`/`CarrierShowHeader.vue`: mobile is a bled-edge-to-edge (`-mx-4 ... px-4`) white (`bg-surface`) centered hero (avatar, name, status/type badges, then action buttons, all centered) with a bottom border; desktop is a `hidden sm:flex` left-aligned split (avatar+details left, actions right).
- Status badge conventions: `tone="success" dot` for active, `tone="warning"` for archived, `tone="accent"` for counts (policies, filter-count) — reuse these tones, don't invent new ones per feature.
- Drop-menu conventions: `View` (not "View {Resource}"), `Edit`, a separator, then `Unarchive` (conditional on status) or `Archive` (danger) — no disabled/stubbed items for features that don't exist yet (Carriers briefly had a disabled "Add policy" stub; it was removed rather than shipped).
- No "Actions" column header label — an empty `<th>` instead, once cells have their own icon-button trigger.

## Track G — Wiring gotchas (easy to lose an hour to)

- `php artisan wayfinder:generate` alone omits `.form()` helpers — pass `--with-form` explicitly to match what the Vite plugin generates during normal dev.
- IDE-warning pass before considering any test-writing issue "done": `@noinspection PhpUnhandledExceptionInspection` above `handle()` calls in test closures (detail lives in `my-phpstorm-conventions` at implementation time).
