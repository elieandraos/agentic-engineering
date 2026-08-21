# Cross-Cutting Capability Checklist

Load this when `rules/feature-classification.md` says **B (cross-cutting capability)**, or loosely for **D (architectural/refactor milestone)**. Unlike `rules/resource-feature-checklist.md`, there's no owning table/model to walk tracks against — the job is to discover scope and dependencies by answering these questions directly, roughly in order. This is not architecture documentation; its only job is to produce correct issue scope and dependency ordering.

An example used throughout this file: this project's Notifications capability (Phase 21) — shared recipient infrastructure → automatic notifications → manual Notify → frontend listener/types/modal → resource integrations.

Resolve each explicitly — skip only what's genuinely not applicable, don't silently drop a question because it's inconvenient to answer:

1. **What problem/capability is being introduced?** One or two sentences. An example from this project: "the org now has roles but no owner visibility into member/admin activity" (Notifications).
2. **What shared infrastructure is needed, and does it need its own issue?** First identify the thing every other piece of the feature builds on. Then decide the split with this rule, not by default:
   - If the infrastructure is a coherent, independently testable outcome on its own — landable and verifiable with no user-visible change — it can be its own issue.
   - If the infrastructure can't actually be proven correct without a real consumer exercising it, bundle the smallest meaningful pilot integration into the same issue rather than shipping untested scaffolding.
   - Don't create "infrastructure with no consumer" just because splitting it out sounds architecturally neat — let the actual dependency structure and testability decide, not a habit of always carving infrastructure into its own issue.
   - An example from this project: Notifications' shared recipient infrastructure (the `User::activeInCurrentOrganization()` and `User::privileged()` model scopes, composed with event-specific exclusions directly in each Action) was independently testable with no user-visible change, so it qualified as its own first issue under the first bullet.
3. **Which existing domains/features produce or consume it?** An example from this project: Clients/Carriers/Agents produce archive events; OrganizationMembers produces role-change/removal events; Documents consumes manual Notify.
4. **What are the key runtime paths?** Where does this get triggered from, and where does it surface? (e.g. an Action call site → a queued notification → a bell dropdown/toast.)
5. **What security / authorization / tenancy boundaries matter?** Name the actual invariant, not just "add auth" — an example from this project: "tenant scope comes from `OrganizationContext`, never actor identity" was the invariant that mattered for Notifications.
6. **Which business events or integration points need wiring?** Enumerate them concretely (e.g. archive, unarchive, role change, removal — not "various lifecycle events").
7. **What reusable backend pieces exist already?** (e.g. an existing envelope/notification base class, an existing policy ability to reuse instead of inventing a new one.)
8. **What reusable frontend pieces exist already?** An example from this project: an existing modal pattern like `InviteMemberModal.vue` was used as the model for a new modal, instead of inventing a new form pattern.
9. **What user-visible integrations sit on top?** Where does this capability actually surface to a user, and on which existing pages?
10. **Which existing capabilities need nominal/refactor changes?** Renames, signature changes, tenancy cleanups that ride along because they're now inconsistent with the new work — call these out as their own small issue rather than silently folding them into a bigger one. An example from this project: the `DocumentsUploadBatchProcessed` rename and the `RemoveOrganizationMemberRequest` tenancy cleanup rode along with Notifications this way.
11. **What is explicitly out of scope?** State it, don't leave it implicit. An example from this project: Notifications explicitly excluded email, digests, free-text messaging, and deferred removed-member email.
12. **Do future extension seams need to be checked at all?** This question is conditional — only ask it when at least one of these is true:
   - Extensibility is explicitly part of the feature's stated goal.
   - The architecture actually introduces an explicit extension point (a registry, a strategy interface, a config-driven adapter list).
   - An issue or its acceptance criteria claims future adopters can join through a minimal, enumerated integration surface — that claim needs verifying (see `rules/review.md`'s extensibility-claim validation).
   Otherwise, skip it — don't invent a hypothetical future requirement just to fill out the checklist. When it does apply, name the seam and confirm it already exists in the current design rather than proposing new work. An example from this project: Notifications' design already left room for a future `mail` channel per notification class and a future Notes-mention recipient rule, so this question was a verification, not new scope.

The answers to 2–4 usually become the shared-infrastructure issue and its immediate dependents; 6 usually becomes the bulk of the backend batch; 9–10 usually become the frontend batch plus any cleanup issues.
