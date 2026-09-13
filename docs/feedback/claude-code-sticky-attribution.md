# We submitted feedback to Anthropic: `attributionSkill` telemetry is sticky

> A real Claude Code runtime finding from Agentic Engineering work.

## The short version

During a `useOrbit` implementation session, `steward-it` discovered something strange in the Claude Code session log:

**`attributionSkill` does not appear to mean "the skill that caused this turn."**

Instead, it stays set to the **last Skill that was loaded** until another Skill is loaded.

So Claude can load `my-phpstorm-conventions`, then spend 10+ minutes doing ordinary implementation work, while all of those later assistant records still say:

```text
attributionSkill: my-phpstorm-conventions
```

That makes a report like "my-phpstorm-conventions used 6.5M cache tokens" misleading. Those records may simply have inherited its label. The runtime field is therefore useful as a **last-skill marker**, but not reliable as per-turn skill attribution.

## What we observed

The behavior was found while stewarding a real `useOrbit` implementation session.

Concrete evidence from the session log:

- session: `714b2f65-df0e-45e4-b5f2-8c4c5ef3deba`
- `my-phpstorm-conventions` was activated at about `20:03:16Z`;
- **175 assistant records** remained tagged `my-phpstorm-conventions`;
- those records continued through roughly 12 minutes of normal implementation work, including controller, resource, and test edits;
- the next Skill invocation was `review-it` at about `20:15:45Z`;
- the attribution changed only after that next Skill invocation.

The important part is that the work between those two Skill calls was not PhpStorm-conventions guidance. The label simply persisted.

## Why this matters

Agentic Engineering's `steward-it` reports usage by skill because we want to understand where time and context are going.

A sticky attribution field can make that accounting look more precise than it really is.

For example, a report might show:

```text
my-phpstorm-conventions    6.5M cache-read
laravel-inertia-stack      1.8M cache-read
implement-it               0.8M cache-read
```

That does **not** prove that those skills actually consumed those amounts of context independently. Some records may simply inherit the most recently loaded Skill label.

## How we reproduced it

The behavior has a simple reproduction:

1. Invoke the Skill mechanism once for a skill, for example `my-phpstorm-conventions`.
2. Perform many normal turns afterward: Bash, Read, Edit, tests, file changes, etc.
3. Do not invoke another Skill.
4. Inspect the raw Claude Code session JSONL.
5. The later assistant records continue to carry the first skill's `attributionSkill` value.
6. Invoke another Skill.
7. The attribution value changes to the newly invoked skill.

That is why we believe this is a **runtime telemetry semantics problem**, not an Agentic Engineering skill problem.

## We sent feedback to Anthropic

Claude Code's built-in feedback flow accepted the report successfully.

**Feedback receipt / ID:**

```text
79a76f51-15d8-4316-b980-08a1dccdec6b
```

**Feedback title:**

> `attributionSkill in session log is sticky to last Skill invocation, not per-turn`

**Area:** `session telemetry / attributionSkill`

The submitted report included the behavior, reproduction steps, session-log evidence, and the observed 175-record example.

We intentionally classified this as **no Agentic Engineering failure**. The problem appears to be in the runtime telemetry itself.

## Can we track the fix?

The feedback receipt is our current identifier, but the Claude Code feedback flow does not give us a public ticket with status tracking. A public Claude Code GitHub issue can be useful if Anthropic or the community later files one, but the receipt itself is not a normal GitHub issue number.

For now, the practical way to find out whether this is fixed is:

- keep the receipt ID above;
- watch Claude Code release notes and the public `anthropics/claude-code` issue tracker;
- after a relevant Claude Code update, rerun the small reproduction above and inspect the session JSONL again;
- update this page with the result.

## Current Agentic Engineering response

Until the runtime changes, `steward-it` treats skill-attributed usage cautiously.

The important distinction is:

> **`attributionSkill` is evidence of the most recently invoked Skill, not proven evidence that every later turn was produced by that Skill.**

We should not invent a fake fix in Agentic Engineering for a runtime field whose semantics belong to Claude Code.

## Why this is here

This is one of the things we want Agentic Engineering to preserve: real engineering work can uncover problems **outside the application and outside the skill system itself**.

The useful path was:

```text
real work
  -> steward-it
  -> raw session evidence
  -> classify as external/runtime limitation
  -> send reproducible feedback upstream
  -> keep the receipt and reproduction here
```

That turns a weird "I think Claude did something strange" moment into a small, reproducible engineering finding we can revisit later.

## Status

**Status:** Reported to Anthropic. Awaiting any runtime change or public tracking reference.

**Discovered:** September 2026, during `useOrbit` Policies implementation work.

**Last verified:** The sticky behavior was directly observed in session JSONL during the stewardship pass that produced this feedback.
