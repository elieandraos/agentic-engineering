<?php

declare(strict_types=1);

namespace App\Models\Concerns;

use App\Sorts\QuerySorter;
use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;

/**
 * Reusable support asset — my-laravel-stack.
 *
 * Target path in a consuming project: app/Models/Concerns/Sortable.php
 *
 * Requires Laravel ^13.7 or later for the #[Scope] attribute (see
 * rules/eloquent-attributes.md). Add `use Sortable;` to any model that should
 * accept a QuerySorter subclass via the `sort` scope.
 *
 * Before installing: check whether an equivalent trait already exists in the
 * target project's app/Models/Concerns/ directory. Reconcile rather than
 * overwrite it.
 */
trait Sortable
{
    #[Scope]
    protected function sort(Builder $query, QuerySorter $sorter): Builder
    {
        return $sorter->apply($query);
    }
}
