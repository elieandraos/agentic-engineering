# Eloquent Attributes

`laravel-best-practices`'s `eloquent.md` already demonstrates `#[Scope]` mechanics by example. This file
owns only the narrow delta: migrating off the legacy `scope`-prefixed naming convention, and the version
requirement.

Define local Eloquent scopes with the `#[Scope]` attribute, not the legacy `scope`-prefixed method-name
convention. Requires Laravel `^13.7` or later, where the attribute was introduced.

```php
// ✅ attribute-based
use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;

final class Order extends Model
{
    #[Scope]
    protected function filter(Builder $query, QueryFilter $filters): Builder
    {
        return $filters->apply($query);
    }
}

// ❌ legacy naming convention — do not use for new scopes
public function scopeFilter(Builder $query, QueryFilter $filters): Builder
{
    return $filters->apply($query);
}
```

- The method name is the scope name itself — no `scope` prefix (`filter`, not `scopeFilter`).
- Method visibility is `protected`.
- The call site is unchanged either way: `Order::query()->filter(...)`.
