# Skill Resolution and Scope Evidence — useOrbit

Status: Evidence. Observed during normal useOrbit work after Agentic Engineering v2.2.0 was released.

## Observation

A fresh Claude Code session in useOrbit was asked to continue Phase 26. It concluded that the installed `implement-it` did not support parallel milestone execution.

That conclusion contradicted canonical v2.2.0. Investigation found two same-named installations:

- project: useOrbit's tracked `.agents/skills/implement-it`, byte-identical to Agentic Engineering v2.2.0;
- personal: `~/.agents/skills/implement-it`, byte-identical to v2.1.4.

Claude Code loaded the personal copy. Its documented same-name precedence is enterprise over personal over project, so the stale personal v2.1.4 copy correctly shadowed the repository-managed v2.2.0 copy.

The personal installation was accidental. Session/runtime evidence traced it to a 2026-09-21 wrong-tool installation followed by an unscoped named `skills update` that touched user scope. The later 2026-09-22 project refresh used explicit project scope and correctly refreshed only useOrbit's managed copy, leaving the stale personal copy in place.

## Behavioral consequence

The repository state was correct:

- `skills-lock.json` described the intended project installation;
- the tracked managed files were v2.2.0;
- the project discovery symlink was correct.

The effective runtime behavior was still v2.1.4 because a higher-precedence same-named skill existed outside the repository.

This produced a material methodology regression: the session reported that parallel implementation was unsupported because the activated v2.1.4 copy predated the parallel-wave rules.

A saved project note mentioning a v2.2.0 post-convergence gap actually contradicted that conclusion, but the session treated it as confirmation instead of rechecking activation provenance.

## Cleanup incident

The duplicate audit found `implement-it` was the only same-named personal/project skill. Other personal skills were intentional and non-conflicting.

A supported-looking cleanup was then attempted with the locally installed skills CLI 1.5.23:

```text
skills remove implement-it -g -y
```

The command successfully removed the personal installation and its lock entry, but while run from inside useOrbit it also deleted the project's tracked `.agents/skills/implement-it` directory. The project discovery symlink remained and became dangling.

Inspection indicated that the CLI's removal path selection could fall back to a path under the current working directory for an agent without a defined global folder. This is observed behavior in that CLI/version, not a portable Agentic Engineering rule about every skills runtime.

No manual cleanup followed. Because the repository-managed skill files were tracked, recovery was exact:

```text
git restore .agents/skills/implement-it
```

Post-recovery verification established:

- all tracked project skill files restored;
- project symlink resolved again;
- project copy remained byte-identical to v2.2.0;
- parallel-wave rules were present;
- personal `implement-it` remained absent;
- project `skills-lock.json` was unchanged;
- no unrelated user skill changed;
- the consuming repository returned to its pre-cleanup Git state.

## Findings

### Declared project state is not effective runtime state

A repository-managed install proves what the project contains and intends to expose. It does not, by itself, prove which same-named skill a runtime will activate when other scopes exist.

Runtime activation provenance matters when behavior conflicts with the managed copy.

### Explicit scope is necessary but not always a sufficient safety boundary

The existing consumption guidance already requires explicit project scope for repository-managed refreshes. Keep that rule.

This incident adds a different warning: do not assume a CLI scope flag proves that no other filesystem scope can be mutated. Skill-management commands should be followed by verification of the repository-managed state, especially when cleaning a cross-scope conflict.

Do not generalize the observed `-g` removal behavior to other CLI versions or runtimes without evidence.

### Git-tracked managed copies are a recovery boundary

The repository-managed model worked as intended after the CLI unexpectedly deleted project files: Git showed the exact mutation and restored the canonical managed copy without reconstructing it from memory or the network.

This is positive evidence for committing managed skill files rather than relying only on machine-local installation state.

## Candidate documentation correction

`docs/skill-consumption.md` should distinguish:

```text
project installation / lock integrity
            !=
effective runtime activation
```

For runtimes with multiple skill scopes, document that same-named higher-precedence skills can shadow a repository-managed copy. Claude Code's observed/documented precedence is a concrete example, not a portable precedence rule.

Also document proportional post-command verification for skill-management operations that can cross scopes.

## Methodology boundary

Do not change `implement-it` from this incident. Its v2.2.0 rules were correct.

Do not yet require every skill activation checkpoint to print version/path/source. That may impose ceremony on normal runs without evidence that it is proportionate.

Retain activation provenance as a Control Room/runtime question: when observed behavior contradicts the project's managed methodology, establish which skill copy the runtime actually activated before diagnosing the methodology itself.
