# Declarative Migrations canonical test-fleet drift

Audit date: 2026-08-09

The current manifest in `zed-pkg-test/zed-pkg-e2e` defines twelve specialized repositories plus the organization `.github` repository for `declarative-migrations-test`.

## Current canonical coverage

Present:

- `.github`
- `cockroachdb-rollback-e2e`
- `data-preservation-e2e`
- `fuzz-property-e2e`
- `homebrew-install-e2e`
- `mysql-shadow-e2e`
- `postgres-lock-contention-e2e`
- `redshift-advisory-e2e`
- `schema-change-online-e2e`
- `snowflake-advisory-e2e`
- `sqlite-migration-e2e`

Missing from the declared canonical manifest:

- `cli-plan-e2e`
- `postgres-zero-downtime-e2e`

This reverses the stale 2026-08-05 finding: the seven repositories previously reported missing now exist, while two repositories previously reported present do not resolve. The manifest/factory remains the authority; this document records live drift and must not silently redefine the canonical fleet.

Several older migration test repositories also exist. They are intentional historical or independently added coverage and must be preserved; they do not replace the current canonical profiles.

## Aggregate portfolio gap

The specialized fleet is broad, but the two requested aggregate orchestration repositories do not yet exist:

- `declarative-migrations-test/declmig-e2e`: candidate, destructive, failure-injection, concurrency, engine, and permission certification.
- `declarative-migrations/declmig-e2e`: stable release-promotion orchestration consuming exact immutable evidence from the test organization.

The aggregate repositories are portfolio overlays, not silent replacements for any specialized scenario repository. The central factory manifest must add the test-org aggregate explicitly before generated governance is treated as converged.

## Required provisioning behavior

Each missing or new aggregate repository must be initialized through a reviewable bootstrap branch and pull request. Available production dependencies must use immutable commit coordinates. Unavailable engines or credentials must remain explicit source/environment gates rather than being reported as passing tests.

Pull-request validation must remain credential-free. Database service credentials and expensive integration environments belong only in protected GitHub environments, scheduled jobs, or manual dispatches. Destructive targets are permitted only in the test organization and must use ephemeral or explicitly disposable infrastructure.

The machine-readable source for this finding is `docs/CANONICAL-FLEET-DRIFT.json`.
