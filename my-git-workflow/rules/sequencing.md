# Recalculating the Dependency-Ready Set

## Principle

> After a validated issue closure, recompute the dependency-ready set in the current milestone
> before deciding what work comes next. Closing one issue can unblock several others — surface that
> proactively, rather than waiting to be asked.

This phase starts only after a validated closure (`rules/issue-closure.md`) — never before.

## Recompute the dependency-ready set

1. List the open issues remaining in the current milestone:

   ```
   gh issue list --milestone "<name>" --state open
   ```

2. For each issue, read its actual dependency information. Never assume a particular structured
   field or textual syntax — dependencies are represented however the project's established issue
   convention records them. `my-feature-planning`'s issue/dependency convention owns that
   representation; this rule only reads and evaluates the resulting graph, and does not redesign or
   invent one.
3. An issue is dependency-ready when every issue it depends on is closed.
4. An issue with no stated dependency is a root issue, and is always ready.
5. Everything else is blocked — record what each blocked issue is still waiting on.

## Report the graph, recommend, let the human choose

Summarize compactly, in categories — never a flat ready list:

- which issues just became newly ready because of this closure;
- which were already ready;
- which are still blocked, and on what.

For example: issue {A} closes, issues {B} and {C} become ready, and issue {D} remains blocked on
{E}.

Recommend one ready issue, with a concise rationale, when the evidence gives a reasonable basis —
e.g. it unblocks the most follow-on work, or it continues the same implementation layer/context the
recent work was in. When several ready issues are genuinely comparable and the choice is a real
judgment call, present them as options instead of silently picking one — this is a sequencing
choice, and `rules/review-gates.md`'s "multiple valid sequencing choices" stop applies here
directly.

Recommendation is not authorization: investigate enough to recommend when possible, but never
convert a genuine sequencing judgment into an automatic choice. The human always makes the final
sequencing decision.

## Do not chain into the next issue

Recalculating and reporting the ready set ends this workflow pass. Do not start implementing the
recommended or chosen next issue in the same pass — even when the human's answer is immediate and
unambiguous. Starting the next issue is a new pass through `my-git-workflow`, with its own explicit
authorization.

## Do / Don't

**Do**
- Recompute readiness from current issue state after every validated closure.
- Explain newly ready, already ready, and blocked work — not just a flat ready list.
- Recommend when the evidence supports one, with a concise rationale.
- Let the human make the sequencing decision.

**Don't**
- Assume a dependency syntax the project doesn't actually use.
- Silently pick between genuinely comparable ready issues.
- Treat a recommendation, or an immediate human answer, as authorization to start implementing.
- Chain straight into the next issue within the same pass.
