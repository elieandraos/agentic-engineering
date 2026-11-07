# Global-Scope Tenancy

Applies only when a project enforces tenant read scoping with a global Eloquent scope that reads a
runtime tenant context (see "Tenant boundaries" in `blueprints/resource-controller.md`). The scope
protects queries that start from the scoped model; the paths below start elsewhere or run without a
context, and fail silently or only at runtime.

## Through relations skip the intermediate model's scopes

`HasManyThrough` and `HasOneThrough` join the intermediate table and apply only its soft-delete
constraint, never its other global scopes. The far model's scopes still apply. Constrain the
intermediate table in the relation definition:

```php
public function customers(): HasManyThrough
{
    return $this->hasManyThrough(Customer::class, Order::class, 'agent_id', 'id', 'id', 'customer_id')
        ->whereColumn('orders.team_id', 'customers.team_id');
}
```

## Hand-built relation subqueries skip definition constraints

`has()`, `whereHas()`, and `withCount()`/`withAggregate()` merge the relation's definition `where`
constraints into their subquery; calling `getRelationExistenceQuery()` directly does not. Prefer those
builder methods. When a subquery must be built by hand (for example an `orderBy` over a count), mirror
them: resolve the relation under `Relation::noConstraints()` and chain
`->mergeConstraintsFrom($relation->getQuery())`, so it filters exactly what `withCount()` counts. Only
`where` constraints merge, not joins. This applies to any constrained relation, not only tenancy.

## Route binding of models outside the scope

A model the tenant scope doesn't cover still resolves another tenant's record through implicit binding,
so the request reaches the policy and can confirm the record exists. Choose a binding mechanism that
rejects it with a 404 before the controller runs: scoped child bindings under a tenant-scoped parent,
an overridden `resolveRouteBindingQuery()`, an explicit `Route::bind()`, or bringing the model under the
scope. Whichever is chosen, a binding that depends on the tenant context must sit behind whatever
establishes that context; otherwise it fails with a server error or resolves unscoped.

## Queued work runs without the request's tenant context

A worker has no request, so the tenant context must be carried and established explicitly. Passing
models into the job or notification is not enough:

- Models restore without global scopes, but relations loaded at dispatch are reloaded through ordinary
  scoped queries while the job is unserialized, before `handle()` or job middleware runs. Dispatch
  without them (`#[WithoutRelations]`, or `$model->withoutRelations()`).
- Carry the tenant identifier explicitly, as a constructor argument or in Laravel `Context` (serialized
  into the job payload and hydrated before the job is unserialized), and establish the tenant context
  before any scoped query: a lazy-loaded relation, a count, a lookup.
- A long-running worker reuses one process across jobs and tenants. Clear or restore the tenant context
  when each job ends, including on failure (for example in job middleware with `try`/`finally`). A
  `scoped()` container binding is reset between jobs by `queue:work`; a static property, plain
  singleton, or runtime config value is not.

A synchronous queue, or a test that keeps the request's context, hides these failures. Exercise queued
work with no tenant context established.

## Testing

Cross-tenant isolation covers queries, not only endpoints. Index, search, and export queries, counts,
sorts, filters, and through relations each need a case that seeds another tenant's records and asserts
they are excluded. Point the foreign record at the current tenant's **own** related record: a foreign
record whose far model is also foreign is dropped by the far model's scope and hides the bug. For a sort,
assert the order, not only the count.
