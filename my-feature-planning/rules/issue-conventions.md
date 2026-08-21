# Issue Conventions

Format for every drafted issue. See also the `feedback_github_issues` memory (no bracket prefixes, assign to self, ask about optional milestone/label) — that memory covers the general habit; this file covers the feature-planning-specific format on top of it.

This format applies to **canonical issue definitions** (see `SKILL.md`) — every rendered preview and every `gh issue create` call is generated from those, never from a prior rendered draft.

## Title convention

One form, for every issue regardless of layer, shape, or origin (planned, extension, bug, refactor, or discovered-work):

```
<Area/Capability>: <action or outcome>
```

- The title describes the change or observable outcome, not the implementation layer. Never encode backend-vs-frontend in the title itself — that distinction belongs to labels (e.g. the `TDD` label) and milestone/dependency metadata, not to the words a reader scans in GitHub's issue list. Whether an issue is backend/TDD or frontend/UI — and therefore whether it carries the `TDD` label — is a property of its actual scope/Tasks, not something derived from parsing the title; see "Milestone and label handling" below.
- Use a concise action ("add", "remove", "fix") or an observable outcome ("silently resets...", "returns invalid response for...") — whichever states the change most plainly.
- Add a UI/location qualifier (a page name, a settings area) only when it materially improves clarity — not by default, and never as a way to smuggle "this is the frontend one" back into the title.
- Keep it concise and scannable in GitHub's issue list — a title is a label a developer scans in a list of thirty open issues, not a summary of the Context section.

Examples:
- `Authentication: remove public registration`
- `Authentication: add admin-mediated 2FA reset`
- `Organization settings: add 2FA requirement toggle`
- `Organization members: add Reset 2FA action`
- `Authentication: Security settings silently reset unfinished 2FA`
- `Authentication: Security settings returns invalid response for incomplete 2FA`

This replaces the earlier Backend/TDD-vs-Frontend/UI title split (`{Feature}: <verb> a <thing>` vs. `{Feature} <area> — <description>`) that issues in this project used through Phase 21. **This is a forward-looking convention only** — it governs issues drafted from here forward. Do not rename or edit any existing GitHub issue title to match it; historical titles (Phase 17 through Phase 21, and #294–#296) stay exactly as created.

## GitHub issues must stand alone

See `SKILL.md`'s "GitHub issues must stand alone" for the full rule and its GOOD/BAD example. The two mechanical consequences of that rule live here:

### Reference syntax — real GitHub refs only

`#N` in an issue body is reserved exclusively for real GitHub issue/PR references — a legitimate dependency (`Depends on #120`), or a legitimate pointer to another real issue in the same set (`the in-app policy (#290)`). GitHub linkifies any `#` followed by digits, whether you meant it that way or not, so:

- Never write `#N` for a plan.md decision number, a canonical planning sequence number, or any other architecture-numbering scheme. `LOCKED decision #7` renders as a link to whatever issue or PR happens to be #7 in this repo — almost certainly unrelated.
- Never write `LOCKED #9` as shorthand — same problem, same fix.
- Never write `issue 5` meaning "canonical planning issue 5" once real GitHub numbers exist — at that point it must say `#<real number>`, or not reference it that way at all.
- Use natural, hash-free wording for plan decisions instead: `decision 7`, `decisions 7–10`, `the approved 2FA-requirement decision`.

Before an issue is created, every canonical planning sequence number in its body must already be resolved to either a real `#N` (if it's a genuine dependency on another issue in this set) or dropped in favor of a plain description (if it's a decision reference) — never left as a bare planning-only number.

### Plan section references are not load-bearing

Do not put `plan.md §2.5`, `§2.12`, or similar section citations into an issue body as a substitute for explanation. In this project specifically, `plan.md` sections get pruned once the corresponding work ships (its own commit history shows this happening repeatedly for past initiatives), so a `§`-citation is not durable execution documentation — it may point at nothing by the time someone reads the issue, possibly before every issue in the same milestone has even shipped.

If a plan section contains something important to the issue, summarize the relevant substance directly in Context or Acceptance Criteria. A brief `plan.md` pointer is allowed only when it's genuinely useful *in addition to* an already-complete explanation — never required to understand the issue, and generally omit it from the final body rather than include it out of habit.

## Issue body: context and outcome first, implementation second

The issue has to be useful to a developer who wasn't in the planning conversation — not just a checklist for whoever drafted it. Structure every issue body around this order:

1. **`## Context`** — why this issue exists: what problem it solves, what outcome should be true when it's done, the architectural/product constraints that actually matter, what's in scope, what's explicitly out of scope, and relevant dependencies. This is prose, not a task list.
2. **`## Tasks`** — where to work (see checklist format below).
3. **`## Acceptance Criteria`** — what must be true when the issue is done (see below). Not every issue needs this section — see the sizing note.
4. **`## Tests`** — the behavior/guarantees that need proof, when that's worth calling out separately from the acceptance criteria. Optional; see below.

Do not let the issue become a code blueprint. Technical file/class references belong in the issue when they help define scope or point to the relevant seam (e.g. "extends the same `QueryFilter` base Carriers uses"), but they support the Context/Acceptance Criteria, they don't replace them. None of these are appropriate in a planning-drafted issue:
- a walkthrough of every class/method to be written
- a copy of the architecture investigation that led to this issue
- a step-by-step coding tutorial
- an exact test implementation recipe (method names, assertion-by-assertion)

If a draft starts accumulating that kind of detail, it's a sign the issue is trying to do implementation's job, not planning's — cut it back to context, scope, and guarantees.

Context must explain a decision, never merely cite one. "Implements decision 7", "Per plan.md §2.5", and "See the architecture plan" are not Context — they name where an explanation could be found instead of giving it. A citation may *accompany* an explanation (it's fine to add "— decision 7" after a sentence that already stands on its own), but it never replaces the sentence. Test every Context section against: **could a developer who never saw the planning conversation open this issue tomorrow and understand what they're supposed to deliver and why?** If the honest answer is no, the Context isn't done — see `rules/review.md`'s "Issue-body content integrity" for how this gets validated mechanically before creation.

## Tasks — the checklist format

Every issue body includes a real, literal Markdown task list — not prose section headers with plain bullets inside them:

```markdown
## Tasks
- [ ] Migration + model changes
- [ ] FormRequest validation
- [ ] Action + Controller
- [ ] Policy ability
- [ ] Tests (action + controller)
```

Tailor the steps to what the issue actually covers — a small frontend-only issue might just be `- [ ] Component` / `- [ ] Wire into parent page`. The point is that GitHub renders these as checkboxes that get ticked as work lands, giving a visible in-progress state on an issue that spans more than one sitting. An example from this project: Phase 17's earliest issues used prose section headers (`## Route`, `## Implementation`, `## Tests`) with no literal checkboxes — nothing was actually checkable off — which is the gap this convention closes.

This must hold in the *actual created GitHub body*, not just the canonical definition draft — verify the literal `- [ ] ` syntax survived into what's about to be posted (`rules/review.md`'s "Issue-body content integrity"), not just that it was written correctly once upstream. Acceptance Criteria are never checkboxes, even when they look list-like — they stay ordinary `- ` bullets, since they describe standing guarantees, not one-time work to tick off.

## Acceptance criteria — guarantees, not restated tasks

A task checklist says where to work; it doesn't say what must remain true when the work is done. Acceptance criteria exist for the real architectural or product guarantees planning surfaced — not for restating a class name or file that's already in Tasks.

Good acceptance criteria capture things like:
- business rules
- security/authorization rules
- tenancy invariants
- lifecycle guarantees (e.g. "dispatch only after the mutation commits")
- observable outcomes (what a user or operator can actually see/do)
- explicit non-goals, wherever accidental scope expansion is likely

Don't pad trivial issues with this — a one-file frontend wiring issue is usually fine as tasks-only; not every issue needs an Acceptance Criteria section. See `SKILL.md`'s "Acceptance criteria vs. task checklists" and `rules/review.md`'s issue-quality checks.

## Tests — when it earns its own section

Most issues don't need a `## Tests` section distinct from Acceptance Criteria — the acceptance criteria already state what needs proving, and the Tasks checklist already includes a "write tests" line. Give Tests its own section only when there's real value in naming the specific behaviors/guarantees that need test coverage beyond what's already implied (e.g. a multi-audience event needs a test per audience, a tenancy boundary needs both an in-tenant and cross-tenant case). Keep it at the level of *what needs proving*, never *how to write the test* — no method names, no assertion-by-assertion recipe. That level of detail is implementation's job, not planning's.

## Milestone and label handling

This is a proposal-and-approval workflow, not a lookup-and-create one. Keep these three things distinct at every step: **project conventions** (patterns this repo has established, used only to *shape* a proposal), **proposed metadata** (what planning is suggesting for this feature), and **approved GitHub state** (what actually gets created, only after the user says so). Never let a convention alone justify creating something — a convention informs what to propose, it doesn't authorize creating it.

The workflow, in order:

1. **Query current state.**
   ```bash
   gh api repos/{owner}/{repo}/milestones -q '.[] | "\(.number): \(.title)"'
   gh label list
   ```
2. **Check applicable project conventions** for naming/numbering/color (this project's conventions are below; another project would supply its own).
3. **Propose the milestone and labels explicitly** — state the exact name(s) and color(s) being proposed, and which convention (if any) they follow.
4. **Show what already exists vs. what's proposed** — don't blur the two into one list. Make it obvious which lines are "already exists, will be reused" and which are "new, needs creation."
5. **Wait for explicit approval before creating anything.** Don't create a milestone or label speculatively while still drafting issue content, and don't create one just because a convention made the name obvious.

### Milestone rules

- If the user has already named or created the milestone (e.g. "milestone Phase 21 — Notifications"), reuse it exactly as given — don't propose a different number or name.
- Otherwise, don't guess the number or name — derive the proposal from the queried state and this project's convention, then confirm the feature name matches how the user has been referring to it in conversation.
- Create the milestone only after approval.

*This project's milestone-naming convention:* `Phase NN — {Feature Name}` (em dash, matching every existing milestone), `NN` being the next unused number.

Milestone closure is not decided here, and never at planning time. A delivery/phase milestone does have a completion lifecycle — closure happens after the release built from this milestone's work has been published and validated, and only once the milestone has no open issues at that point (`my-git-workflow`'s `rules/milestone-completion.md` owns that gate and the mutation itself). This skill's job stops at defining the milestone and its issue set; it never runs the closure gate, never proposes closing a milestone, and never treats "all currently-known issues closed" as a signal to act on. That distinction matters here specifically because this skill's own drafting work finishes long before a milestone reaches that gate — implementation, review, manual testing, and any small follow-up issue discovered along the way (and legitimately added to this still-open milestone, per `my-git-workflow`) all happen after this skill is done with a given batch of issues.

This is a forward-looking workflow decision, not an extraction of past repository practice — this project's full milestone history (checked before this rule existed) shows every milestone ever created was left open, including several where every issue was already closed. That's evidence about how things happened to be left under a different, unstated set of assumptions; it isn't preserved as a rule, and no existing milestone gets retroactively closed because this lifecycle now exists.

#### Milestone descriptions

A milestone description is optional — propose one only when the milestone's intent, boundaries, exclusions, governing principles, or completion criteria aren't already clear from the title and its issue set alone. It is not a default habit to fill in for every milestone.

This project's own history supports that bar rather than a blanket one: of 22 milestones created, only 6 ever carried a description, clustering into two situations — the earliest foundational milestones pinning down initial scope or exclusions (e.g. "No filters, exports or audit trails at this stage"), and cross-cutting rework milestones whose completion genuinely isn't self-evident from title/issues (e.g. an exit criterion paired with a literal verification command, or governing principles that anchor acceptance criteria stated later). Ordinary CRUD-feature milestones consistently shipped with no description at all — the constituent issues carried the meaning on their own.

When a description is warranted, propose its exact text alongside the milestone name/color in the same propose-then-approve step — never write one directly into GitHub without approval, same as any other metadata. When a milestone description exists, treat it as that milestone's contract: the same weight `plan.md`'s locked decisions carry for architecture, or an issue's Acceptance Criteria carry for a single issue. Issues drafted into that milestone should not silently contradict it, and a stated exit criterion or governing principle doesn't need to be re-derived per issue — but it shouldn't be undermined by one either.

This is forward-looking only. Do not add, edit, or backfill descriptions on existing milestones just because this rule now exists.

#### Backlog vs. delivery/phase milestones

A persistent catch-all milestone (this project's `Backlog`) is structurally different from a `Phase NN — {Feature}` delivery milestone — it's a standing holding pen for work not tied to a specific phase, not a scoped unit of delivery. In this project it has held both stray hardening/audit issues and cross-cutting improvements never attached to any phase, with issues opening and closing inside it continuously since it was created, alongside — not in place of — regular phase work.

Do not apply delivery-completion framing to a backlog-style milestone: no expectation that its issue set converges toward zero open issues, no completion-criteria description in the sense the previous section describes, and it is never subject to `my-git-workflow`'s post-release milestone-completion/closure lifecycle (`rules/milestone-completion.md`) — that gate applies to delivery/phase milestones only. A purely descriptive one-liner explaining its purpose is fine; it isn't a contract with an exit condition the way a phase milestone's description is.

When proposing a milestone for a new issue, treat "does this belong to a specific phase's delivery scope" and "does this belong in the standing backlog" as genuinely different questions. Don't default an issue into the backlog milestone just because its scope feels unclear — that's a signal to ask, not a reason to file it there automatically.

### Label rules

- Reuse exact existing labels when appropriate — don't recreate a label that already exists under a slightly different name.
- If a feature label is genuinely new, propose the exact name and color; don't create it before approval.
- Reuse established shared labels when project convention calls for them (e.g. a label every backend/TDD issue gets, regardless of feature).
- Any additional new label outside the normal feature label / established shared labels should be explicitly proposed and justified — don't introduce one just because it seems useful.

*This project's label conventions:* the feature's own label (e.g. `Carriers`, `Notifications`) is reused if it exists, or proposed with a color if new; `TDD` is an existing established shared label applied to every backend-only issue; per the `feedback_github_label_colors` memory, a genuinely new label gets the next unused Tailwind vivid hue at the 200 shade, rotating through the palette.

## Discovered-work issues

Issues coming out of `rules/discovered-work.md`'s intake follow the same Context → Tasks → Acceptance Criteria → Tests shape and the same self-containedness bar as any other issue, with one legitimate difference: the mechanism behind the finding isn't always fully resolved by the time the issue is written.

- **Context states what's confirmed vs. what's still a hypothesis or unknown, explicitly.** Don't let an unresolved mechanism get smoothed into a confident-sounding sentence that isn't actually proven. An issue drafted from Phase 22's #296 finding is the model: Context states plainly what's confirmed (a real 200 response, specific to unconfirmed-2FA accounts, unaffected by an earlier fix) separately from what's not yet confirmed (the exact server-side reason for the response mismatch) — a reader can tell which parts are fact and which are still open.
- **An unresolved mechanism can be one of the issue's own Tasks** — e.g. "Capture the actual request (headers included) to identify why..." — rather than blocking issue creation until the mechanism is fully understood. This is legitimate only when `rules/discovered-work.md`'s stopping condition was actually met (the remaining unknown needs implementation-adjacent tooling, or effort disproportionate to defining the issue), never as a shortcut around investigating.
- **A defect distinguished from intended behavior during investigation is scoped as what it actually is.** If investigation shows the "bug" is working as designed, the issue (if one is still warranted) is about the missing explanation or UX gap, not a mischaracterized code defect — the same #296 finding is the example: the mandatory-2FA redirect itself was correct behavior; the real fix was surfacing why it happened, not stopping it.

## Assignee

Always self (`--assignee "@me"`) unless told otherwise.

## No bracket prefixes

Titles are plain sentences — no `[Carriers]`, `[Backend]`, etc. The milestone and label already carry that categorization.
