# Feature Classification

Classify before picking a checklist — applying resource assumptions (migrations, slugs, archive/unarchive, exports) to a capability with no CRUD spine is what over-scopes cross-cutting work; skipping shared-infrastructure thinking is what under-scopes it.

Applies identically whether the work is Planned or arrived via `rules/discovered-work.md`'s intake — a validated discovered finding still gets classified here, not assumed into a shape. Most discovered findings land in C (a defect inside something that already ships) or D (no user-facing capability, just a correction), but classify rather than assume.

## The four shapes

**A. New resource / vertical CRUD capability** — a brand-new first-class entity with its own lifecycle (Carriers, Agents). Has a natural migration/model/policy/controller spine. → `rules/resource-feature-checklist.md`.

**B. Cross-cutting application capability** — infrastructure or a capability that spans multiple existing domains rather than owning one table (Notifications, a future shared search/reporting layer, a background-processing pipeline, an external integration). No single resource owns it. → `rules/capability-checklist.md`.

**C. Extension of an existing capability** — new behavior bolted onto something that already ships (a new filter, a new export shape, a new child resource on an existing parent). Usually a narrow slice of `rules/resource-feature-checklist.md`'s tracks — walk only the tracks that actually changed, don't re-plan the whole resource.

**D. Architectural/refactor milestone** — no new user-facing capability, but a deliberate restructuring (a rename sweep, a tenancy cleanup, a pattern migration) that's worth its own milestone and issues. Use `rules/capability-checklist.md`'s framing loosely — the "what's out of scope" and "what must remain true" questions matter most here; most of the rest doesn't apply.

Don't over-think the taxonomy: an obvious owning table + lifecycle is A; no owning table is B; additive-to-something-that-exists is C; nothing user-facing changing is D. Ask the user only if it's genuinely unclear which shape fits.

## Worked examples

- Carriers, Agents → A
- Notifications (Phase 21: shared recipient infrastructure → automatic notifications → manual Notify → frontend listener/types/modal → resource integrations) → B
- "Add a filter for policy type to Clients" → C
- "Rework tenancy to use `OrganizationContext` everywhere" → D
