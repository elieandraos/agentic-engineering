# Design Reconciliation

Design mockups drift from what actually ships. This isn't a failure mode to prevent — it's normal, because real decisions get made mid-implementation that never get folded back into the design source. The job here is to **surface** drift, not silently resolve it in either direction.

## This pass is conditional, not universal

Only run this when an issue has frontend/UI scope. Backend-only issues, and cross-cutting capabilities with no UI surface, skip this file entirely — don't go looking for a `_design/*.jsx` mockup that has no reason to exist. Don't assume `_design/` exists or is complete, either: it's gitignored and doesn't persist across machine restarts, and a mockup may predate the feature being planned (e.g. `_design/notifications.jsx` only covers the bell dropdown/index page shipped in an earlier phase — it has no mockup for a manual-Notify modal added later). Check for a matching file before assuming one is missing or present.

## Where design lives

Per the `project-design-files` memory: design files from Claude Design live at `_design/` in the project root. Read from there directly — e.g. `_design/agents-screen.jsx`, `_design/carrier-detail.jsx`. If frontend/UI work genuinely needs a design reference and the matching file is missing (or only covers an earlier, unrelated version of the page), ask the user to re-share the Claude Design URL or confirm the intended UI rather than inventing layout.

## The reconciliation pass

Before drafting **any** frontend/UI-wiring issue for a feature:

1. Read the matching `_design/*.jsx` mockup(s) for the page(s) this issue covers.
2. Read the equivalent already-shipped page(s) elsewhere in the app (e.g. if planning an index page, read the existing index-page component for a sibling resource, not just the design).
3. Classify what you find into one of four cases. Case is what determines the action — don't skip straight to an outcome without naming which case applies.

## The four cases

**A. Design is older than the shipped implementation, and the shipped implementation clearly represents the newer product decision.** Real decisions got made mid-implementation that never made it back into the design source — this is normal, not a failure to prevent. Use the shipped application as the implementation precedent. Mention the drift if it's useful context, but don't stop for a decision unless a genuine, still-unresolved product question remains underneath it.

**B. Design and shipped implementation represent genuinely different product choices, and neither one clearly supersedes the other.** Stop and flag it (see "What 'flag it' means in practice" below) — do not pick a side silently. This is the only case that blocks drafting until the user weighs in.

**C. Design describes genuinely new UI with no shipped equivalent.** Follow the design, subject to the normal planning rules — there's nothing to reconcile because nothing shipped yet contradicts it.

**D. `plan.md` contains an explicitly locked design decision** (see `rules/plan-md-input.md`) covering what this pass would otherwise resolve — a UI shape, an interaction pattern. The plan decision remains authoritative; a stale design mockup never gets to silently override it, no matter which of A/B/C it would otherwise look like. Still run the reconciliation pass for context — `_design/` and the shipped app can both have moved since the plan was written — but its job here is to confirm nothing material has changed underneath the locked call, not to re-decide it. If a mockup actively disagrees with the locked decision, that's flagged exactly like case B, and the user confirms the locked decision stands (or explicitly amends it) rather than the mockup winning by default.

## What "flag it" means in practice

Compile the disagreements into a short list and hand it to the user before drafting the affected issues — one line each: what the design shows, what the shipped app (or the locked plan.md decision) actually does/has, and (if you have an opinion) which one you'd lean toward and why. Let the user decide; this is a product call, not an engineering one.

## Examples from this project

**Case B (genuine disagreement, flagged):** `_design/new-carrier.jsx` and `_design/carrier-detail.jsx` still reference `onboarded_date` (a required date field), `is_hq` (a boolean flag marking one branch as headquarters), and `contact.department` — none of which exist anywhere in the shipped `Carrier`/`CarrierBranch` schema. The original GitHub issues (#198, #199, #208, #209) were written *from* the design and inherited the same fields, then the fields were quietly dropped during implementation without either the design or the issues being updated. Nobody made a documented decision to drop them — it just happened. That's exactly the kind of drift this pass exists to catch before it repeats on the next feature. (In hindsight this reads as case A — the shipped schema was the newer decision — but because no one had ever surfaced or confirmed that call, it had to be treated as an unresolved case B at the time it was caught.)

**Case C (genuinely new UI, design followed):** `_design/notifications.jsx` (Phase 21) only mocks the bell dropdown and notifications index page shipped in an earlier phase (document-upload notifications) and has no mockup at all for the manual-Notify modal/reason picker added in Phase 21. There's nothing to reconcile because the design is silent, not contradicting — the right move was to follow the shipped app's existing form pattern (`InviteMemberModal.vue`) instead.

**Case D (locked plan.md decision holds against a stale mockup):** planning the Global Search capability (Phase 22), `plan.md` locked an inline-dropdown search UI in `AppTopNav.vue`, explicitly rejecting a command-palette/⌘K overlay. `_design/app-shell.jsx`'s `TopNav` mockup nonetheless showed a ⌘K-triggered search button — drawn before Agents/Carriers were in scope and never updated. Flagging it (rather than either silently following the stale mockup or silently ignoring it) let the user confirm the locked decision stood.
