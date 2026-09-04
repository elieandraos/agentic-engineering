# Agentic Engineering

**Lab. Plan. Ship. Build with the right stack.**  
Understand in the Lab. Plan the work. Build with the Stack. Ship the change.

> A portable, evidence-driven methodology for architecting, planning, and delivering software — plus stack-specific companions that carry technology knowledge without leaking it into the portable core. Not a prompt collection for one repository or framework.

## The pipeline

<table>
<thead>
<tr>
<th width="140">Skill</th>
<th>What it does</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="skills/lab-it/"><code>lab-it</code></a></td>
<td>Investigate a system, answer architecture questions, and trace behavior across layers → an architecture guide, a focused guide update, or an approved <code>plan.md</code>.</td>
</tr>
<tr>
<td><a href="skills/plan-it/"><code>plan-it</code></a></td>
<td>Turn a feature request or approved <code>plan.md</code> into reviewed, implementation-ready GitHub issues.</td>
</tr>
<tr>
<td><a href="skills/ship-it/"><code>ship-it</code></a></td>
<td>Implement an approved GitHub issue, verify the result, shape the commits, and carry it through delivery.</td>
</tr>
</tbody>
</table>

```shell
lab-it                     # understand the system
plan-it                    # plan the work in GitHub
ship-it + stack companion  # build, verify, and deliver
```

These skills do not assume a language, framework, or project layout. The consuming project supplies those; each skill supplies the method.

Use only the stage you need. `plan-it` can start from a direct feature request or an approved `plan.md`; `ship-it` can start from any approved GitHub issue, whether or not `plan-it` created it.

## Build with the right stack

Stack companions carry technology-specific implementation knowledge without becoming another pipeline stage.

* [`laravel-inertia-stack`](skills/laravel-inertia-stack/) — Laravel, InertiaJS, Vue 3, and Pest. It works alongside relevant Laravel Boost skills and guides `plan-it` and `ship-it`; `ship-it` still performs the implementation.
* A different stack can get its own companion when real use justifies it.

## Install

```shell
npx skills add elieandraos/agentic-engineering
```

Choose the skills and agents you need. Install a stack companion only where it applies.

## Knowledge boundaries

The ecosystem keeps four kinds of knowledge separate:

* **Portable methodology** — `lab-it`, `plan-it`, and `ship-it`; independent of language and framework.
* **Stack knowledge** — implementation conventions for one compatible stack.
* **Project knowledge** — domain rules and repository conventions owned by the consuming project.
* **First-party capabilities** — external skills such as Laravel Boost, composed with rather than copied or renamed.

See [`docs/skill-authoring-methodology.md`](docs/skill-authoring-methodology.md) for the full model.

## Evolution principle

Rules in this ecosystem evolve from demonstrated need and real use, not speculative generalization. See [`roadmap.md`](roadmap.md).
