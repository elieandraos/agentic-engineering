# Resource Controller Blueprint

## Boundary

`laravel-best-practices`'s `routing.md` already owns general resource/CRUD controller organization, the
thin-controller principle, and the Form-Request-vs-inline validation boundary. This file does not restate
any of that — it owns only the concrete composition of those principles with this stack's specific
classes.

## Core composition

**Controller → Form Request → Policy/`#[Authorize]` → Action → Resource → Inertia/HTTP response.**

- **Controller** — coordinates HTTP/Inertia behavior only: resolve the Form Request, authorize
  (declaratively, before the method body runs), delegate the mutation to an Action, build the Resource
  for a read path, and return the Inertia response or redirect. No business logic in the method body.
- **Form Request** — owns validation and request normalization (`prepareForValidation()` — see
  `request-normalization.md`), never business logic.
- **Policy / `#[Authorize]`** — owns access enforcement, resolved before the method body runs (see
  `authorization.md`).
- **Action** — owns mutations and business workflows: DB writes wrapped in `DB::transaction()`, audit
  fields, side effects dispatched with `->afterCommit()` outside the transaction (see
  `actions-pattern.md`).
- **Resource** — owns the response/Inertia data contract (see `resources.md`).

### Worked example — full CRUD

```php
// StoreOrderRequest
final class StoreOrderRequest extends FormRequest
{
    public function rules(): array
    {
        return [
            'customer_id' => ['required', 'integer', 'exists:customers,id'],
            'notes' => ['nullable', 'string', 'max:1000'],
        ];
    }
}
```

```php
// OrdersController
final class OrdersController extends Controller
{
    #[Authorize('viewAny', Order::class)]
    public function index(IndexOrderRequest $request): Response
    {
        $orders = Order::query()->paginate();

        return Inertia::render('Orders/Index', [
            'orders' => OrderResource::collection($orders),
        ]);
    }

    #[Authorize('create', Order::class)]
    public function store(StoreOrderRequest $request, CreateOrderAction $action): RedirectResponse
    {
        $order = $action->handle($request->user(), $request->validated());

        Inertia::flash('toast', ['type' => 'success', 'message' => __('Order created.')]);

        return to_route('orders.show', $order);
    }

    #[Authorize('view', 'order')]
    public function show(Order $order): Response
    {
        return Inertia::render('Orders/Show', [
            'order' => OrderResource::make($order),
        ]);
    }

    #[Authorize('update', 'order')]
    public function update(UpdateOrderRequest $request, Order $order, UpdateOrderAction $action): RedirectResponse
    {
        $order = $action->handle($request->user(), $order, $request->validated());

        Inertia::flash('toast', ['type' => 'success', 'message' => __('Order updated.')]);

        return to_route('orders.show', $order);
    }

    #[Authorize('delete', 'order')]
    public function destroy(Order $order, DeleteOrderAction $action): RedirectResponse
    {
        $action->handle($order);

        Inertia::flash('toast', ['type' => 'success', 'message' => __('Order deleted.')]);

        return to_route('orders.index');
    }
}
```

This example omits `create`/`edit`: a feature that renders dedicated create/edit Inertia pages implements
them the same way as `index`/`show`; a feature that doesn't (an API-style or modal-driven UI) simply has
no route for them. See "Non-CRUD and single-action controllers" below — omitting a resourceful method is
normal, not a gap to fill.

## What the controller must make explicit

### Redirects and flash messages

Flash a toast, then redirect with `to_route()`:

```php
Inertia::flash('toast', ['type' => 'success', 'message' => __('Order created.')]);

return to_route('orders.show', $order);
```

### Route-model binding behavior

State explicitly, for each authorized method, whether the model instance is already bound by the route
(authorize against the route parameter directly — `view`/`update`/`delete`) or must be resolved via a
named child policy plus the parent's route parameter (`create`/`viewAny` on a child resource — see
`authorization.md`). This distinction is not obvious from the attribute's own signature and is easy to
get wrong silently.

### Tenant boundaries — only when the project is multi-tenant

Tenancy is conditional, not a requirement of every project or every controller. This blueprint does not
prescribe one portable tenancy mechanism — a scoped route binding, a global Eloquent scope, and a
Policy-layer check against a request-scoped context are all valid designs, and none of them is *the*
answer to prescribe here. When a project genuinely is multi-tenant, identify, for the resource at hand,
where each of these is actually enforced:

- **Read scoping** — does the `index`/`show` query itself filter by tenant, or is that left to a global
  scope?
- **Authorization** — does the Policy check tenant membership?
- **Creation-time assignment** — does the Action stamp the tenant, and from what source?
- **Route-model isolation** — can a route parameter resolve to another tenant's record at all, and if
  so, what rejects it?

A project may answer these differently than another project on the same stack. Identify the actual
mechanism in the code under review rather than assuming any one of them.

## Non-CRUD and single-action controllers are first-class

Do not manufacture CRUD symmetry a feature does not have. Four real, non-exceptional shapes:

**A single-action `__invoke` controller** for an operation that isn't one of the seven resourceful
actions:

```php
final class OrdersArchiveController extends Controller
{
    #[Authorize('archive', 'order')]
    public function __invoke(Request $request, Order $order, ArchiveOrderAction $action): RedirectResponse
    {
        $action->handle($request->user(), $order);

        Inertia::flash('toast', ['type' => 'success', 'message' => __('Order archived.')]);

        return to_route('orders.index');
    }
}
```

**A single-action controller with no Inertia involvement at all** — for example a binary export
(`Illuminate\Http\Response` here, not Inertia's `Response`):

```php
final class OrdersPdfExportController extends Controller
{
    #[Authorize('view', 'order')]
    public function __invoke(Order $order, ExportOrderToPdfAction $action): \Illuminate\Http\Response
    {
        return $action->handle($order);
    }
}
```

**A single-action controller returning a Resource directly**, for an XHR/partial-update flow rather than
a page navigation:

```php
final class OrderNotesUpdateController extends Controller
{
    #[Authorize('update', 'note')]
    public function __invoke(UpdateOrderNoteRequest $request, OrderNote $note, UpdateOrderNoteAction $action): OrderNoteResource
    {
        $note = $action->handle($note, $request->validated());

        return OrderNoteResource::make($note);
    }
}
```

**A controller implementing fewer than the seven resourceful methods, with none of them mapped to
Inertia** — a pure API-style sub-resource controller embedded in an otherwise Inertia application:

```php
final class LabelsController extends Controller
{
    #[Authorize('viewAny', Label::class)]
    public function index(IndexLabelRequest $request): AnonymousResourceCollection
    {
        return LabelResource::collection(Label::query()->orderBy('name')->get());
    }

    #[Authorize('create', Label::class)]
    public function store(StoreLabelRequest $request, CreateLabelAction $action): LabelResource
    {
        return LabelResource::make($action->handle($request->user(), $request->validated('name')));
    }

    #[Authorize('delete', 'label')]
    public function destroy(Label $label, DeleteLabelAction $action): \Illuminate\Http\Response
    {
        $action->handle($label);

        return response()->noContent();
    }
}
```

Never introduce a generic shared `CrudController` base merely to force structural symmetry, and never add
a `create`/`edit`/`show` method a feature has no route for.

## Explicitly out of the core

Not part of this blueprint's mandatory contract — optional patterns, loaded only when a feature genuinely
needs them:

- **Exports** (PDF/Excel) — a real, separate pattern (see the single-action export example above), not a
  CRUD requirement.
- **Filters and sorters** — see `filters-pattern.md`; the base classes ship as reusable assets
  (`assets/app/Filters/`, `assets/app/Sorts/`), not as part of this blueprint's core.
- **Admin-oriented list tooling** — bulk operations, admin tables, and similar administration-specific
  capabilities.
