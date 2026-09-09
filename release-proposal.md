# Next release — working draft

**Status: unreleased working draft.** Each change recorded below carries its own review status — approved or pending — stated with that entry, not a single status for the whole draft. The release version, final scope, exact target commit, release notes, and publication remain separate decisions.

The latest published baseline is [v2.0.2](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.2). Its completed proposal remains available in [Git history](https://github.com/elieandraos/agentic-engineering/blob/3271db87fa5ea437817bfdce877e602f7bb2827e/release-proposal.md).

## Recorded changes

- **lab-it — proportional investigation and decision discussions.** Reuse reliable findings, inspect only as far as the request needs, and ask about unresolved material choices in dependency order. Use concrete scenarios to clarify ambiguity and identify when more evidence is needed. Familiar features can finish with a verified answer and a recommendation to use `plan-it`; resolving an architectural decision does not automatically produce a document. An explicitly requested `plan.md` retains the existing synthesis and approval procedure. Recommendations grant no approval and do not erase decisions already explicitly approved. The skill README and architecture dossier are reconciled. Source review approved at [3452a8f](https://github.com/elieandraos/agentic-engineering/commit/3452a8fdf677f9cbc9b9dc1ca4417ac36bc29af8).
- **Roadmap — observe context during real useOrbit work.** Compare modeled workflow estimates with session context observations and task outcomes before deciding on reporting improvements or context budgets. Recorded at [23f46dd](https://github.com/elieandraos/agentic-engineering/commit/23f46dd993b7c6c42bd198c524d9eff01a3fae98).
- **review-it — finding traceability, abstraction usefulness, and independent test expectations.** A finding that depends on a requirement or project convention now names that source concisely alongside its evidence and consequence, never inventing one where none exists and never requiring a requirement-by-requirement table. The Maintainability check adds a concrete removal/inlining thought experiment before flagging an abstraction as unnecessary complexity, and requires a stated consequence — a single caller or a thin wrapper alone, or a boundary the project has already established, is not by itself a finding. Test adequacy now flags an assertion whose expected side is built by re-exercising the same logic it's meant to prove rather than proving the behavior independently, while preserving legitimate integration assertions and established test-layer ownership (illustrated, where the Laravel companion is installed, by its Pest blueprint and test-ownership rule) and introducing no blanket ban on mocks, database assertions, or any particular test style. Implemented, pending Control Room review.

## Draft public release notes

> More focused architecture discussions and clearer guidance for familiar features.
>
> ### What changed
>
> - **lab-it.** Scales investigation and questions to the work. Reuses reliable findings, addresses unresolved decisions in a useful order, and clarifies ambiguous choices through concrete examples. Familiar features can proceed toward issue planning without an unnecessary design interview. A `plan.md` is produced only when explicitly requested, through the existing approval procedure.
> - **Documentation.** Updated the `lab-it` README and architecture dossier. Added context monitoring during real useOrbit work to the roadmap.
>
> ### Validation
>
> Reviewed source changes and walked through familiar-feature, architectural-decision, and explicitly requested plan scenarios. Recorded validation does not include live skill or consumer execution; context estimates are not observed session usage.

## Before publication

Reconcile the final change set, choose the version and exact target commit, finalize release notes and installation guidance, and obtain explicit publication authorization.
