# Inertia Page Components

When a Laravel endpoint renders a new Inertia page component, create the corresponding Vue page component within the same implementation boundary.

A backend-only change is not complete when its Inertia response names a page that does not yet exist. In this stack, a missing component can fail the request through the Vite manifest instead of producing a normal page response.

This is especially important for controllers that introduce a new page name while the full frontend implementation is intentionally deferred. In that case, a minimal placeholder page is sufficient until the real page issue lands.

## Rule

- Create the minimal Vue page component for every new Inertia component name rendered by the backend change.
- Keep the placeholder minimal when the issue does not include the real frontend implementation.
- Place the component at the exact project-approved path for that feature or policy class.
- Do not expand a backend issue into full frontend work merely to satisfy this rule.

## Why

The backend-to-Inertia response boundary depends on the named Vue component being resolvable. Treat the component's existence as part of the endpoint's minimum working boundary, even when the component's real UI is implemented later.

This rule is specific to the Laravel + InertiaJS + Vue 3 stack and complements the stack's existing controller/resource guidance. It does not prescribe a particular page design or frontend component architecture.
