# Lab. Plan. Implement. Review. Ship — with the right stack.

Investigate in the Lab. Plan the work. Implement the change. Review it. Ship it.

> A portable, evidence-driven methodology for understanding, planning, implementing, reviewing, and shipping software—with stack-specific companions where needed. Not a prompt collection for one repository or framework.

## The pipeline

| Stage | Skill and context | Result |
|---|---|---|
| Lab | [`lab-it`](skills/lab-it/) | Verified architecture understanding, or an approved `plan.md` |
| Plan | [`plan-it`](skills/plan-it/) | Implementation-ready GitHub issues |
| Implement | [`implement-it`](skills/implement-it/) + project context + applicable stack companion | Verified, reviewed implementation, committed |
| Review | [`review-it`](skills/review-it/) | Implementation assurance — findings, or a clean result |
| Ship | [`ship-it`](skills/ship-it/) | Milestone PR proposed, then release once merged |

These skills do not assume a language, framework, or project layout. The consuming project supplies those; each skill supplies the method. **PR approval and merge always stay with a human** — no skill in this pipeline merges its own work.

Use only the stage you need. [`plan-it`](skills/plan-it/) can start from a direct feature request or an approved `plan.md`; [`implement-it`](skills/implement-it/) can start from any approved GitHub issue, whether or not [`plan-it`](skills/plan-it/) created it, and invokes [`review-it`](skills/review-it/) before its own implementation gate; `review-it` is also independently callable on its own, reviewing any worktree, branch, or PR standalone, with no prior session in this ecosystem required.

## Document as you go

[`document-it`](skills/document-it/) creates, updates, and reviews explanatory architecture guides — in Markdown, a Claude Artifact, or both. It's an independently available companion, not a mandatory pipeline stage: call it whenever a guide needs writing or reconciling.

## Boring prompts

**Boring prompts. Serious engineering.**

State the goal, not the choreography. Investigation methods, planning checks, review checklists, and delivery rules already live in versioned, reviewable skills.

```shell
"Investigate how authentication works and prepare the change plan."  # lab-it
"Document the billing architecture."                                 # document-it
"Turn the approved plan into GitHub issues."                         # plan-it
"Implement issue #42."                                               # implement-it + stack companion when relevant
"Review this branch before I open a PR."                             # review-it
"Create the milestone PR."                                           # ship-it
```

The stages compose into a human workflow, but each prompt also works on its own.

## Implement with the right stack

Stack companions carry technology-specific implementation knowledge without becoming another pipeline stage.

* [`laravel-inertia-stack`](skills/laravel-inertia-stack/) — Laravel, InertiaJS, Vue 3, and Pest. It works alongside relevant Laravel Boost skills.
* A different stack can get its own companion when real use justifies it.

## Install

```shell
npx skills add elieandraos/agentic-engineering
```

Choose the skills you need, and the coding agent(s) to install them for (`-a/--agent`, e.g. `claude-code`) — that selects which agent reads the installed skills, not a set of subagent definitions this repository supplies. Install a stack companion only where it applies.

## Knowledge boundaries

The ecosystem keeps four kinds of knowledge separate:

* **Portable methodology** — [`lab-it`](skills/lab-it/), [`document-it`](skills/document-it/), [`plan-it`](skills/plan-it/), [`implement-it`](skills/implement-it/), [`review-it`](skills/review-it/), and [`ship-it`](skills/ship-it/); independent of language and framework.
* **Stack knowledge** — implementation conventions for one compatible stack.
* **Project knowledge** — domain rules and repository conventions owned by the consuming project.
* **First-party capabilities** — external skills such as Laravel Boost, composed with rather than copied or renamed.

## Evolution principle

Rules in this ecosystem evolve from demonstrated need and real use, not speculative generalization. See [`roadmap.md`](roadmap.md).

## License

[MIT](LICENSE)
