# Recalculating the Dependency-Ready Set

After a validated issue closure (`rules/issue-closure.md`), recompute what's dependency-ready in
the current milestone before doing anything else. Closing one issue routinely unblocks others —
report that, don't wait to be asked.

## How to recompute it

1. List the open issues remaining in the milestone (`gh issue list --milestone "<name>" --state
   open`).
2. For each, read its body for dependency mentions (this project writes them as plain prose —
   "Depends on #120", "Depends on #290, #120" — not a structured field; read the issue body, don't
   assume a schema).
3. An issue is dependency-ready when every issue it depends on is closed. An issue with no stated
   dependency is a root issue and is always ready.
4. Everything else is blocked — note what it's blocked on, so the summary explains the graph, not
   just the ready list.

## Report the graph, recommend, let the human choose

Summarize compactly: which issues just became newly ready as a result of this closure, which were
already ready, and which are still blocked and on what. This is exactly what closing #120 surfaced:
three simultaneously-ready issues (#289, #290, #121) with different dependents, each blocked on
different upstream work.

Recommend one issue with a one-line rationale when there's a reasonable case for one (e.g. it
unblocks the most follow-on work, or it continues the same layer of the stack the last few issues
were in). When several ready issues are genuinely comparable and the choice is really a judgment
call, offer them as options rather than silently picking — this is a sequencing choice, and
`rules/review-gates.md`'s "multiple valid sequencing choices exist" stop applies here directly.

The human makes the final sequencing call, always. Recommending is not the same as choosing.

## Do not chain into the next issue

Closing an issue and recalculating the ready set ends this skill's work for that turn. Do not start
implementing the next issue — recommended or chosen — in the same pass. Starting the next issue is
its own new pass through this workflow (`SKILL.md`'s step 1), gated by its own explicit go-ahead,
even when the human's answer to "what's next" was immediate and unambiguous.
