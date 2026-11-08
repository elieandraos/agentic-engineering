# Database audit

Use the checks that match the requested scope and the system's actual data paths. Follow the
database engine and versions used by the application, tests, and intended deployment. Record
material differences between them. Use checked-in schema definitions and the actual schema and
index inventory when available.

## Data access and tenant isolation

- Identify the ownership boundary and how a trusted identity establishes it. Trace relevant reads
  and writes through user-facing requests, direct data APIs, exports, jobs, or other paths the
  system exposes. Check which authorization and data filters apply on each path.
- Verify each relevant path with the identity and context it actually uses. For example, test a
  background job without request context when it normally runs that way. Check returned, stored,
  or emitted data and indirect effects such as ordering. A denied destination can still have
  sensitive data in the output that links to it.
- Check nested lookups, joins, relationship writes, and deliberate scope bypasses. A correctly
  scoped primary record can still reference a record owned by someone else. Confirm what enforces
  ownership on both sides of a relationship.
- Where tenants exist, test a request from one tenant using another tenant's record ID. Separately,
  when the schema permits a mismatched relationship and a lookup trusts it, create that link in
  disposable data and check the resulting output. Establish whether a supported write path can
  create the mismatch.
- Trace untrusted search, filter, and sort inputs into query construction. Check how values are
  bound and how caller-selected identifiers or sort directions are constrained.

## Record lifecycle and integrity

- Identify which records depend on the record being changed. Compare the intended behavior on
  archive, delete, and restore, where supported, with the database constraints and application
  visibility rules. Check whether the action changes a status, hides the row, or removes it.
- Exercise the normal action on a record with dependents. Verify what happens afterward in the
  relevant screens, exports, and jobs. Include historical dependents when the product keeps
  history. Verify that the action works for an unlinked record when the product allows it.
- When a lifecycle action makes a record unavailable, also check whether a later create or
  update can still link to that record.
- Check that the database and application together enforce the relevant invariants. For example,
  an existing foreign key may still point to a row hidden by a soft delete. Verify whether the
  dependent operation can still resolve that row.

## Concurrent writes and stale data

- For writes whose correctness depends on mutable state, identify a realistic overlap between two
  requests or jobs. Trace what each operation reads, validates, locks, and writes. Check the
  relevant competing write paths.
- If the operation uses a lock, verify that it reads the protected state inside the transaction
  and uses that state for decisions and writes. Recheck earlier validations that depend on changed
  values. If another mechanism protects the write, verify the guarantee that mechanism provides.
  Evaluate uniqueness, stale-state protection, and atomicity separately.
- Reproduce stale-state behavior with an earlier read followed by a database change and then the
  operation under test. If the finding depends on actual contention, lock behavior, or isolation
  semantics, use separate transactions or connections on the relevant engine.

## Query counts and N+1

- Measure total queries at the normal operation boundary, including response construction or export
  mapping. Compare a small nonempty result with a larger one. Use distinct related records where
  repeated fixtures could hide per-row lookups.
- Keep conditions comparable. Hold the clock, populated sections, filters, and pagination or export
  chunk boundaries steady. Separate fixed setup or per-section queries from queries that grow with
  each result row.
- Trace any growth to its source. Explain which dimension drives it, such as result rows,
  export chunks, or history depth. Judge impact using the expected size of that dimension.

## Query cost and indexes

- Start with the queries the app actually runs for the affected filters, search, ordering,
  and pagination. Measure the page query, count, and other expensive parts separately when
  they contribute to the same operation.
- When an index or launch-readiness decision depends on scale, benchmark in a disposable
  database on the intended engine. Use synthetic data at a realistic workload and at a larger
  plausible workload. Match the distribution that drives the query, including rows per tenant,
  common filters, and related records where relevant. Use tens of thousands of rows when
  that scale answers the question. If the target engine or representative workload is unavailable,
  state what remains unverified.
- Record dataset sizes and distributions, engine and version, execution plans, repeated timings,
  and the indexes the optimizer selected. Compare before and after under comparable conditions.
  Identify forced plans and label extrapolations as estimates.
- Record how to seed the data and rerun the measurements. Identify any temporary data or probes
  kept for reruns and how to remove them.
- Recommend an index or rewrite when the measured benefit justifies its cost for the workload.
  Check that a rewrite preserves results, including date boundaries, sort order, and pagination.
  Where the test and deployed engines differ, verify behavior on the engines that matter.
  If performance is adequate, recommend deferring the change and name the condition for revisiting it.
