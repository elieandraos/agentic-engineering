# Inertia Page Components

When a Laravel endpoint renders a new Inertia page component, create the corresponding Vue page
component within the same implementation boundary. A backend-only change is not complete when its
Inertia response names a page that does not yet exist.

## Rule

- Create the minimal Vue page component for every new Inertia component name the backend change renders.
- Keep the placeholder minimal when the issue does not include the real frontend implementation.
- Place the component at the project-approved path for that feature.
- Do not expand a backend issue into full frontend work merely to satisfy this rule.

## Example

```php
// Renders "Orders/Archived" — the endpoint's minimum working boundary requires this component to exist.
public function archived(): Response
{
    return Inertia::render('Orders/Archived', [
        'orders' => OrderResource::collection(Order::query()->archived()->paginate()),
    ]);
}
```

```vue
<!-- resources/js/pages/Orders/Archived.vue — minimal placeholder; the real UI is a later issue. -->
<script setup lang="ts">
defineProps<{ orders: unknown }>();
</script>

<template>
    <div>Archived orders</div>
</template>
```

## Why

The backend-to-Inertia boundary depends on the named Vue component being resolvable. A missing
component fails in more than one place:

- A root layout that lists the page in `@vite` (as Laravel's Inertia starter kits do) cannot find it in
  the Vite manifest, so the request errors instead of rendering.
- The client cannot resolve the page, even when the server response succeeds.
- In tests, `assertInertia()`'s component assertion fails when inertia-laravel's
  `testing.ensure_pages_exist` option is on (its default). Tests that call `withoutVite()` do not reach the
  manifest failure, so this assertion is what catches the gap there.

Treat the component's existence as part of the endpoint's minimum working boundary, even when the real
UI lands later. This rule does not prescribe page design or frontend component architecture.
