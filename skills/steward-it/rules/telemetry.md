# Telemetry

## When this applies

Load for every non-trivial stewardship pass when session or runtime evidence may be available.
"May be available" is a reason to run the discovery procedure below, not a reason to skip it — do not
decide telemetry is unavailable before attempting it.

## Discovery (locate, then parse)

This is a repeated, confirmed failure mode in practice, not a hypothetical one: a stewardship pass
reports timing and token/context telemetry as "unavailable" without ever attempting to locate or open
the session's own log — even when that log exists, is well-formed, and contains everything the contract
below asks for. The miss is that discovery is never tried.

Before marking any field in this rule unavailable, actually attempt to locate and parse the underlying
session log:

1. **Recognize an identifiable session reference.** A Claude Code session's own system prompt normally
   names a path that embeds the session id — for example a scratchpad directory such as
   `/private/tmp/claude-<uid>/<project-slug>/<session-id>/scratchpad`. Other runtimes expose an
   equivalent session/log identifier. Treat the presence of such an identifier as the signal that
   session-level telemetry is reasonably discoverable, and proceed to locate the actual log — never
   treat the identifier itself, or the fact that it's merely present, as the telemetry.
2. **Locate the log file.** For Claude Code, each session is stored as a JSONL file at
   `~/.claude/projects/<project-slug>/<session-id>.jsonl`, where `<project-slug>` is the working
   directory's path with `/` replaced by `-`, and `<session-id>` is the identifier from step 1.
   - **Stewarding the current session:** derive both parts directly from the identifiable path already
     present in context.
   - **Stewarding a different or historical session** (for example, investigating an earlier session
     from within a later one): do not guess a session id. Search the same project directory for the
     JSONL whose content contains a known, distinguishing string (an issue number, a commit SHA, a
     quoted prompt) or whose modification time matches the known event window, and confirm the match
     before relying on it.
   - Confirm the file actually exists and is non-empty before proceeding.
3. **Parse it.** Each line is one JSON record. Read `type` (`user`, `assistant`, `system`, and so on).
   An `assistant` record normally carries a top-level `timestamp` (ISO-8601) and a `message.usage`
   object (`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`,
   `output_tokens_details.thinking_tokens`). A record may carry a top-level `attributionSkill` naming
   the skill responsible for that request. `tool_use` and its matching `tool_result` pair by
   `tool_use_id`. Use a script (Python, `jq`, or equivalent) to read and aggregate these — the file can
   be large, and eyeballing it is not a substitute for actually parsing it.
4. **Only once discovery and parsing have actually been attempted**, and the log is genuinely missing,
   unreadable, or lacking the specific field in question, mark that field unavailable — and say which
   step failed and why (no identifiable session reference existed; no matching file was found; the file
   existed but the field was absent; the file was inaccessible). "I have not looked yet" is never a
   valid basis for "unavailable."

**Do not treat ambient `<total_tokens left>` / context-window headroom indicators as session
consumption telemetry.** These figures describe remaining context budget, move non-monotonically
(compaction can raise them), and are not a record of input/output/cache/thinking tokens actually
consumed. They are not the session log, and their presence or behavior is never evidence that the
actual telemetry is unavailable — that determination can only follow the discovery procedure above.

## Evidence states

Report every telemetry field as one of exactly three states, and say which:

- **Measured** — read directly from the session log: a `timestamp` delta, a `message.usage` field, a
  top-level `attributionSkill` value, a matched `tool_use`/`tool_result` interval.
- **Reconstructed** — derived, not directly stated: a phase boundary inferred from an identifiable
  event (a `Skill` tool-use, a `git commit`, a Gate report or approval message, a `gh issue close`), or
  an interval computed across several measured timestamps. State what it was derived from.
- **Unavailable** — only after the discovery procedure above was actually attempted and the evidence is
  genuinely absent or inaccessible. State why (see step 4).

Never report a field "unavailable" when discovery was simply skipped. That distinction — "not yet
inspected" is not "unavailable" — is itself part of the report; see `report.md`.

## Timing

Report:

- total elapsed time;
- active execution time;
- human wait time;
- phase timing, reconstructed from identifiable events when the log doesn't state phases explicitly.

Human wait is excluded from active execution time. For Claude Code sessions, treat a confirmed
`AskUserQuestion` interaction as human wait from its tool-use event through the matching tool-result
event. Do not require the enclosing user turn to have `origin.kind == human`; observed sessions may
have `origin: None` on those result turns. A plain-text approval (a human reply following an assistant
report, with no `AskUserQuestion` involved) is also a measurable human-wait interval — the gap between
the report's timestamp and the next user turn's timestamp — and belongs alongside `AskUserQuestion`
intervals in the same accounting.

State each timing value as measured or reconstructed per "Evidence states" above; otherwise unavailable.

## Context and skill attribution

When `attributionSkill` is available, group meaningful token and cache usage by skill, including
unattributed requests, by aggregating the `message.usage` fields of the records that carry each skill's
attribution. Distinguish directly reported usage from inferred percentages or aggregates. Do not invent
skill attribution that the runtime does not expose.

Use telemetry as diagnostic evidence, not as a quality verdict. Large prompts, repeated loads, cache
footprints, and long phases justify investigation but do not prove waste by themselves.

## Historical evidence

Older file-size or workflow models may still appear in historical evidence such as prior scenario
records. Treat those as historical intent only — they are not runtime measurements and must not be
cited as current consumption proof.
