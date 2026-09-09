# v2.0.3 — Release preparation

**Status: publication and post-publication cleanup authorized by the user; not yet published.** The reviewed implementation and documentation are ready. Publication still needs execution and verification.

## Release identity

- Tag and title: `v2.0.3`.
- Exact target commit: `db68fe72903060c7afc7ed87e28fccbdbc7dd9c8`.
- Previous release: [v2.0.2](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.2).
- This preparation file's own commit is after the target and does not change it.

This is a patch release: focused corrections and refinements to existing skills, with no new skill, ownership boundary, or approval gate.

## Reviewed scope

- `lab-it` investigation and decision-discussion improvements, including its README and dossier: approved through [3452a8f](https://github.com/elieandraos/agentic-engineering/commit/3452a8fdf677f9cbc9b9dc1ca4417ac36bc29af8).
- `review-it` finding traceability, abstraction usefulness, and independent test expectations: approved through [e72eb16](https://github.com/elieandraos/agentic-engineering/commit/e72eb16c0a8ef33f19ed6bfedccd4974ff7c6e6f).
- `review-it` dossier reconciled with those rules at [82e708b](https://github.com/elieandraos/agentic-engineering/commit/82e708b755c047857d768ccd154556a717e53526).
- Roadmap context monitoring retained; the completed adjacent-skill comparison item removed at the target commit.

Recorded validation is source review and scenario walkthroughs. No live skill, consumer, or browser execution is claimed.

## Complete release-note text

> More focused architecture discussions and more precise implementation reviews.
>
> ### What changed
>
> - **lab-it.** Scales investigation and questions to the request, reuses reliable findings, and focuses discussion on unresolved decisions. Familiar features can proceed toward issue planning without an unnecessary design interview. A `plan.md` is produced only when explicitly requested, through the existing approval procedure.
> - **review-it.** Connects findings to applicable requirements and project conventions, evaluates abstractions by their concrete costs, and checks that test expectations independently and meaningfully verify the intended behavior. Legitimate integration assertions and test-layer ownership are preserved.
> - **Documentation.** Updated the skill documentation and architecture dossiers. Added context monitoring during real useOrbit work to the roadmap and removed the completed adjacent-skill comparison item.
>
> ### Install / update
>
> ```shell
> npx skills add 'elieandraos/agentic-engineering#v2.0.3'
> ```
>
> Select the skills and agent targets your project uses, and refresh their complete directories.
>
> ### Validation
>
> Validated through source review and scenario walkthroughs. The recorded validation does not include live skill execution, a consumer run, or observed session token usage.

## Publication and cleanup

1. Fetch current remote state. Confirm the exact target remains reachable from `origin/main`. Check for an existing `v2.0.3` tag and release before creating anything. Reconcile an already-completed matching publication rather than duplicating it; stop on a conflicting target or release identity without moving a tag.
2. Create the tag at the exact target and publish a non-draft, non-prerelease GitHub release titled `v2.0.3`, using the release-note text above verbatim after stripping only the outer blockquote markers.
3. Read the remote tag and release back. Verify the tag's resolved commit, title, body, and published status.
4. Only after publication is verified, update `roadmap.md`'s current baseline to the published `v2.0.3` and its exact target, with a concise summary of this release and its actual validation. Preserve the real-use next steps, future directions, and deferred questions.
5. Delete this root `release-proposal.md`; its content remains in Git history and the public notes live on the release. Commit and push only the roadmap-baseline update and proposal deletion. Leave unrelated local work, all runtime skill files, and consuming projects untouched.
