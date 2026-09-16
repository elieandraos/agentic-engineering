# Inertia Pages

## Resolve rendered page components during backend implementation

When a Laravel controller returns an Inertia page, the referenced Vue page component should exist during the same implementation boundary, even when the issue is primarily backend work and the full page UI will be implemented later.

A missing component can cause the server-side Inertia response to fail when Vite tries to resolve the page. A minimal placeholder page is therefore a valid intermediate implementation when the real page belongs to a later issue.

For example, if a controller renders:

```php
return Inertia::render('Orders/Index');
```

ensure `resources/js/pages/Orders/Index.vue` exists before considering the backend endpoint complete.

Keep the placeholder minimal and replace or extend it when the owning frontend issue is implemented. Do not add a placeholder merely for structural symmetry when the endpoint does not actually render an Inertia page.

## Verification

When adding a new Inertia render target in a backend issue:

1. Confirm the referenced Vue component path and naming against the project's existing conventions.
2. Add the minimal component when the real UI is intentionally deferred.
3. Exercise the endpoint so a missing Vite component resolution cannot remain hidden behind otherwise passing backend tests.
