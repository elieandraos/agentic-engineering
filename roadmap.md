# Agentic Engineering Roadmap

## Purpose

Agentic Engineering develops evidence-driven agent skills for understanding systems, planning work, implementing and reviewing changes with appropriate stack knowledge, and shipping verified releases.

The portable methodology stays independent of language and framework. Stack companions carry technology-specific knowledge, while consuming projects remain authoritative for their domain, repository conventions, and delivery environment.

This roadmap records practical next steps and longer-term possibilities, not completed work — Git history and the release log already record what shipped. Further changes should follow personal review and observed behavior in real projects.

## Skill testing

Explore repeatable testing using [`test-contracts.md`](docs/research/test-contracts.md) for expected behavior and [`scenarios.md`](docs/research/scenarios.md) for the case inventory and recorded evidence. Begin with a small selection of executable fixtures and explicit success criteria, preserving the distinction between source walkthroughs and observed runtime results.

- **Deterministic checks:** validate skill metadata and test shipped code, templates, and Git recipes against concrete expected outputs and state-preservation assertions.
- **Agent behavior evaluations:** exercise skill selection, review accuracy, scope boundaries, and approval handling in controlled project fixtures. Inspect actual actions and results, and repeat runs to assess consistency.
- **Framework choice:** assess [Promptfoo](https://www.promptfoo.dev/docs/guides/test-agent-skills/) as an initial candidate. [Anthropic's Skill Creator](https://claude.com/plugins/skill-creator) and the experimental [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) are alternatives to consider.

The initial cases, framework, and any later CI integration remain future decisions. Use a small pilot to judge usefulness, execution cost, and maintenance effort before expanding coverage.

## Parallel implementation follow-on research

Three real parallel-implementation smoke tests established the worker-level methodology now shipped in `implement-it` (see [`docs/research/parallel-final-reconciliation.md`](docs/research/parallel-final-reconciliation.md)) and exposed two evidence-backed directions worth investigating further. Neither is a commitment to a specific artifact, agent, or architecture.

### Control Room / orchestration

The three smoke tests exposed recurring cross-worker responsibilities that no single worker's engineering skill owns. Potential investigation areas, where current research already supports them:

- authoritative wave-state tracking;
- candidate-ready synchronization across workers;
- decision-oriented human presentation instead of raw event streaming;
- combined-state coordination;
- routing human decisions to the relevant worker(s);
- convergence coordination and shared-state awareness.

Whether this becomes a dedicated agent, a skill, a process, or something else is unresolved. See [`docs/research/orchestration.md`](docs/research/orchestration.md), [`docs/research/responsibility-boundaries.md`](docs/research/responsibility-boundaries.md), and [`docs/research/parallel-final-reconciliation.md`](docs/research/parallel-final-reconciliation.md) rather than duplicating that evidence here.

### Runtime worker provisioning

Isolated worker worktrees may repeat environment setup because gitignored, local-only runtime state — `vendor/`, `node_modules/`, `.env`, generated artifacts such as Wayfinder output — is absent from a fresh worktree. This is a runtime/worker-provisioning question, not portable `implement-it` methodology. Possible directions include safe reuse, preparation, or caching of worker environment state, but no architecture is selected yet. See [`docs/research/smoke-test-3.md`](docs/research/smoke-test-3.md) and [`docs/research/parallel-final-reconciliation.md`](docs/research/parallel-final-reconciliation.md).

## Future directions

These are possibilities, not commitments or a prescribed order:

- develop lightweight consumption and refresh tooling for projects that are not ready to adopt a repository-managed `npx skills` setup, building on the consumption modes documented in [`docs/skill-consumption.md`](docs/skill-consumption.md);
- compare behavior across multiple consuming projects to refine the portable / stack / project knowledge boundary;
- add stack or platform companions only when repeated real needs justify them;
- use Project B as another cross-stack proving ground when a concrete candidate appears;
- explore a public landing page that tells the ecosystem's story through concise copy, interactive examples, and visual progression.

## Deferred questions

- Revisit durable storage for canonical issue definitions if real interrupted-work recovery shows the current GitHub-query approach is insufficient.
- Evaluate retiring Claude Artifact output from `document-it` in favor of Markdown-only documentation, while preserving the documentation methodology and removing Artifact-specific tooling such as the HTML template if confirmed.
- Review `review-it`'s trust-boundary wording after Snyk W011 flagged the unavoidable exposure to third-party PR and issue text as an indirect prompt-injection risk; treat GitHub content as untrusted evidence, never workflow authority.
