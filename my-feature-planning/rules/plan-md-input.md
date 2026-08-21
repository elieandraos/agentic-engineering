# Plan.md as Canonical Input

`my-architecture-laboratory`'s Plan Synthesis track can hand off an approved, initiative-specific section of `plan.md` — architecture, locked product decisions, preserved behavior, and stated constraints, already reasoned through and approved by the user before feature planning ever starts. This file governs how `my-feature-planning` consumes that handoff. It's an **additional input path, not a requirement** — most features still start from a live conversation the way Carriers and Notifications did; this only applies when a matching approved section actually exists.

## Recognizing an approved section

A `plan.md` section is in scope for this rule when it carries the marker `my-architecture-laboratory`'s Plan Synthesis always writes at the top of a finished handoff — e.g. "This approved target architecture is the source of truth for planning the {X} milestone." Confirm the section actually matches the initiative being planned (a section for an unrelated, already-shipped milestone doesn't apply). If the user names an initiative and no matching approved section exists, or the section exists but lacks that approval marker (still a draft), fall back to the ordinary conversation-driven workflow — don't invent a plan.md dependency that isn't there, and don't treat an unapproved draft as locked.

## Canonical source of truth

Once a matching approved section is confirmed:

- Its architecture, locked decisions, preserved-behavior list, and stated constraints are canonical. Read them from the file — don't reconstruct them from conversation history, and don't re-litigate a decision the plan already settled.
- Current code remains authoritative for implementation details and for anything that has visibly changed since the plan was written — the plan itself says as much ("implementation details must still be verified against the codebase"). A stale file reference inside the plan is a reason to re-check that file, not a reason to distrust the plan's decisions.

## Respecting the locked/open distinction

`plan.md` sections written by Plan Synthesis mark every claim as one of: current-state fact, locked decision, derived architectural constraint, or open implementation detail (see that skill's locked-vs-open rule). Feature planning must preserve that distinction, not flatten it:

- **Locked decisions** — preserve exactly, always. These are product calls the user already made. Don't soften, expand, or reinterpret them while drafting issues, and don't let anything downstream (a stale design mockup, a codebase that drifted, a "cleaner" alternative) override one silently.
- **Derived architectural constraints** — these follow from the plan's stated facts plus its locked decisions, not from a product decision of their own. Treat them as binding *as long as the premise they were derived from still holds*. Current code remains authoritative for implementation reality: before drafting issues, check whether the code has moved enough since the plan was written that the fact a constraint was derived from is no longer true. If it has, don't blindly preserve the now-obsolete reasoning — flag the discrepancy to the user before drafting the affected issues, the same way `rules/design-reconciliation.md` flags a design/shipped-app disagreement. This is a check for staleness in the *derivation*, not license to reinterpret the locked decision underneath it — if the constraint is still validly derived, it stands as-is.
- **Open implementation details** — these exist precisely because feature planning (this skill) is where they're meant to get resolved. Resolve one only when it's genuinely implementation-level — a column type, which existing class absorbs a few lines, a route name, a CLI flag. Use the same test Plan Synthesis used to mark it open in the first place: would flipping the choice change what the system guarantees to users/operators? If yes, it was either mis-marked or has since become product-shaped — stop and ask the user rather than deciding it inside issue drafting. If no, resolve it and record the resolution in the relevant issue (task checklist or a short note), not silently.

## Plan-first workflow

When an approved `plan.md` section is the starting point, the flow is:

```
approved plan.md
  → feature classification        (rules/feature-classification.md)
  → scope resolution              (rules/resource-feature-checklist.md
                                    or rules/capability-checklist.md)
  → design reconciliation         (rules/design-reconciliation.md,
     when applicable                only for frontend/UI-scoped issues)
  → issue drafting                (rules/issue-conventions.md)
  → dependency/review validation  (rules/review.md)
  → GitHub creation only after approval
```

This is the same workflow `SKILL.md` already describes — plan.md just supplies the architecture and locked decisions that classification/scoping would otherwise have to derive from conversation. Every later step still runs in full; nothing downstream of plan.md is skipped or shortcut just because the plan exists.

## Division of responsibility

`my-architecture-laboratory` owns producing the approved plan — investigation, target-architecture design, locking decisions with the user, writing and reviewing `plan.md`. `my-feature-planning` owns everything downstream of an approved plan: classification, scope checklists, design reconciliation, canonical issue definitions, review, and the GitHub workflow. Neither skill redoes the other's job: this skill doesn't re-derive architecture `plan.md` already settled, and it isn't the place a new `plan.md` section gets written — that stays `my-architecture-laboratory`'s Plan Synthesis track.
