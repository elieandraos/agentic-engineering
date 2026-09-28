# Post-Convergence Environment Evidence — Phase 26

Status: Evidence. Observed during normal useOrbit work after Agentic Engineering v2.2.0 was released.

## Observation

After the Phase 26 parallel implementation waves had converged into `feat/policies-http-frontend`, a later manual code-review session ran the full local test suite and reproduced:

```text
11 failed, 1276 passed (4099 assertions)
```

All 11 failures were HTTP 500 responses caused by Vite being unable to find four newly-added Inertia pages in `public/build/manifest.json`:

- `AgentPolicies/Index.vue`;
- `CarrierPolicies/Index.vue`;
- `ClientPolicies/Index.vue`;
- `PolicyMembers/Index.vue`.

Those pages had been created in parallel worker branches and later converged into the milestone branch. The local checkout's generated Vite manifest predated them.

Running `npm run build` refreshed the generated state; the affected tests then passed (21 tests, 159 assertions). CI on the same application commit was green because its test workflow builds frontend assets before Pest.

The Lab investigation also observed 12 worker worktrees still present after convergence, including one locked worktree.

## Classification

The observed failure has two layers.

### Stack-specific layer

A Laravel/Inertia/Vite application can produce false local HTTP-test failures after new page files arrive in a checkout whose generated Vite manifest is stale.

That belongs to stack knowledge. It is evidence for `laravel-inertia-stack`, not portable Agentic Engineering methodology.

### Lifecycle/runtime layer

Parallel convergence changes tracked source state, but v2.2.0 does not assign ownership for reconciling local generated/runtime state after convergence or for retiring worker worktrees that are no longer needed.

The portable question is broader than Vite:

> After parallel worker results converge, what runtime/environment state must be reconciled before the shared checkout can be treated as ready for subsequent local work, and what owns cleanup of completed worker workspaces?

Possible examples include generated manifests, generated routes, caches, dependency state, environment preparation, and stale worktrees. These examples are evidence, not a proposed portable checklist.

## Why this matters

The committed application state was correct and CI was green, but the developer's authoritative local checkout presented a false-red suite until generated state was refreshed. That creates avoidable debugging cost and can make correct converged work appear broken.

The leftover worktrees are a separate lifecycle-hygiene signal: preserving worker state during active work is valuable, but completed workers should not accumulate indefinitely without an explicit retention/cleanup decision.

## Boundary

Do not solve this by putting Vite commands or worktree-cleanup commands into portable `implement-it`.

The evidence may belong to different future owners:

- stack companion: knows which generated/runtime artifacts can become stale and how the stack safely refreshes them;
- runtime/provisioning layer: manages worker workspace lifecycle and local environment preparation;
- Control Room/orchestration candidate: may know when a wave has converged and when reconciliation/cleanup becomes relevant;
- portable methodology: only if repeated evidence shows a runtime-independent lifecycle invariant is missing.

## Extraction status

Retain and watch, with recurrence now established for workspace cleanup.

A later normal four-issue Phase 26 wave (`phase26-normal-parallel-wave.md`) completed successfully through convergence, push, and issue closure while all four current worker worktrees remained present. Twelve older clean/merged worktrees were removed only because the human explicitly requested housekeeping during the wave; runtime-created `worktree-agent-*` branches still remained afterward.

This strengthens the worker-workspace lifecycle finding: successful issue/wave completion does not currently retire temporary execution resources automatically, and no existing portable issue lifecycle owns that retirement.

The later wave did not reproduce the stale-Vite-manifest failure, so generated-state reconciliation remains a separate stack/runtime watch item rather than a generalized post-convergence procedure.

Do not solve the recurrence by adding an unconditional worktree-removal command to portable `implement-it`. Cleanup safety depends on whether a workspace is clean, merged, locked, interrupted, or still needed for recovery.

## Next evidence

During future real parallel waves, observe:

- whether generated/runtime state becomes stale again after convergence;
- whether combined verification already refreshes enough state when it runs;
- whether an explicit wave-level skip makes post-convergence reconciliation more important;
- when completed worker worktrees can be safely removed, and which layer can prove they are no longer needed;
- whether cleanup/reconciliation is naturally performed by the runtime, coordinating context, stack companion, or an existing lifecycle stage.
