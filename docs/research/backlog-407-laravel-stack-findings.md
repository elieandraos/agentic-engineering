# Backlog #407 Laravel stack findings

> **Status:** reconciliation record for the v2.2.3 patch candidate. These findings come from normal
> useOrbit Backlog issue #407 implementation and are classified against `laravel-inertia-stack` v2.2.2.
> This document records why a finding did or did not become portable stack guidance; it is not useOrbit
> project documentation.

## Included in the patch

| Finding | Classification | Destination | Portable lesson |
| --- | --- | --- | --- |
| A create page that already shape-checked its enum preselections still read related-record IDs with `$request->integer()`, so `?client_id[]=5` preselected record 1 | MODIFY | `rules/request-normalization.md` (existing query-state section) | The v2.2.2 wording and example were enum-only; the shape check applies to every query-derived scalar preselection. `integer()` fails silently by casting a non-empty array to `1`, unlike `enum()`, which throws. |
| Select and filter option lists reused full detail resources (~40 client fields, including contact, birth date, address, emergency contact and audit fields) where consumers read only `id` and a label; introduced independently in three changes and kept through a shared-options refactor | MODIFY + routing row | `rules/resources.md`, `SKILL.md` routing | Inertia serializes every prop into the page response. An option list is a distinct consumer and needs an explicit projection chosen for it; the implementation form (mapped array or small dedicated resource) stays with the project. |

## Already covered or not yet promoted

### Nested validation keys in user-facing copy

A Form Request with nested fields lacked `attributes()`, so messages showed dotted keys. Same finding and
classification as `phase26-laravel-stack-findings.md`: framework-owned, project application. **No
change.**

## Boundary of v2.2.3

Evidence is one project. Candidate 1 is strong (the gap sat beside code already following the rule);
candidate 2 is moderate (three independent introductions in one project, generic Inertia mechanism). No
new rule file, no new naming convention for option resources, and no Vue-side guidance.
