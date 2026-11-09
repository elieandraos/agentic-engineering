# Security audit

Use the checks that match the requested scope and the system's actual trust boundaries. Start
from the entry points the system exposes and the data that crosses them. A policy, middleware,
validation class, or security setting counts only when a traced path reaches it.

Whether a caller can read or change another owner's or tenant's records, and how untrusted
search, filter, and sort input reaches queries, belongs to [Database audit](database.md). Apply
those checks there and report each finding in one module.

## Authorization and access control

- Build the inventory from registered entry points: routes with their effective middleware and
  guards, API and administrative surfaces, broadcast channels, signed or token links, webhook
  receivers, and console commands where in scope. Do not build it from the policy files.
- For each entry point in scope, trace the identity that reaches it and the check that runs
  before the effect. A control that only the UI applies, such as a hidden button, is absent.
- Check capabilities that are not record-scoped: membership and role changes, invitations,
  ownership transfer, account and security settings, support or impersonation access, and
  cross-tenant administration. Compare the permission that comparable effects require across
  workflows.
- For invitation, token, and signed-link flows, check expiry, single use, binding to the intended
  identity, and behavior after the related membership or record changes.
- Verify a material gap with a request from an identity that the system should refuse.

## Input trust

- Identify server-owned fields such as owner, tenant, creator, role, status, and price. Trace each
  write path from request to persistence. Check whether a submitted key can reach a server-owned
  field through mass assignment, a nested payload, or input that validation does not cover.
- Check that server-side validation covers what the effect depends on: types, ranges, enumerated
  values, and referenced records with their state. Client-side or pre-submit validation is not
  enforcement.
- Check redirect targets and URLs built from input against an allow-list.

## Sensitive-data exposure

- Inventory where data leaves the server: page and shared props, API responses, exports and
  generated documents, emails, notifications and broadcasts, logs and error reports, queue
  payloads, and URLs.
- For each output in scope, compare the fields emitted with the fields the consumer needs. Inspect
  the serialized output for a representative record, not only the serializer definition. Include
  hidden attributes, relations loaded for another purpose, and values shared with every page.
- Check that queue payloads carry identifiers or minimal snapshots, not credentials, tokens, or
  full sensitive records.
- Check that logs and error reports do not record credentials, tokens, or personal data from
  request input or exception context.

## Files and external input

- For uploads, check content-based type validation, size limits, the storage disk and its
  visibility, generated storage names, and where files wait before processing.
- For downloads, check authorization on every path that serves a file, the lifetime of temporary
  or signed URLs, and headers built from user-supplied names.
- Check file paths built from input for reads, writes, and deletes.
- Where the system has the path, check outbound requests built from input for destination
  restrictions, including redirects. Check inbound webhooks for sender authenticity and replay
  handling before side effects. Check that shell commands receive input as separate arguments.
  Check that stored content rendered as HTML is escaped or sanitized.

## Configuration and dependencies

- Read the effective configuration of the target environment: debug output, session and cookie
  flags, CSRF exemptions, CORS, trusted proxies and hosts, and authentication throttling. Example
  environment files and local values are not evidence for production. If the target environment
  is unavailable, mark these checks unverified.
- Check tracked files for committed credentials and keys.
- Run the package managers' read-only advisory audits against the lockfiles, for example
  `composer audit --locked` and `npm audit --omit=dev`. Do not install, update, or fix packages.
  Report an audit that could not run as unverified.
- For each advisory, establish whether the affected package ships to production and whether the
  application reaches the affected feature. Report a match with unverified reachability as an
  affected version, not as an exploitable vulnerability.

## Security scoring rubric

Use these category weights with the score breakdown in the main skill.

| Category | Points | What to assess |
|---|---:|---|
| Authorization and access control | 30 | Checks at every entry point in scope, capabilities beyond record scoping, and token or link flows. |
| Input trust | 20 | Protection of server-owned fields and server-side validation of what each effect depends on. |
| Sensitive-data exposure | 25 | Fields emitted through responses, props, exports, messages, logs, and queue payloads compared with what each consumer needs. |
| Files and external input | 15 | Upload, storage, and download handling, and external inputs such as outbound URLs, webhooks, commands, and rendered HTML. |
| Configuration and dependencies | 10 | Effective security configuration of the target environment, committed secrets, and reachable dependency advisories. |
