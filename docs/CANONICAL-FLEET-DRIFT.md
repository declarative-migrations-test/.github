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

## Aggregate portfolio status

Both requested aggregate orchestration repositories were provisioned through a narrowly scoped factory workflow and initialized through draft pull requests:

- `declarative-migrations-test/declmig-e2e`: candidate, destructive, failure-injection, concurrency, engine, and permission certification; bootstrap PR `declarative-migrations-test/declmig-e2e#1`.
- `declarative-migrations/declmig-e2e`: stable release-promotion orchestration consuming exact immutable evidence from the test organization; bootstrap PR `declarative-migrations/declmig-e2e#1`.

The aggregate repositories are portfolio overlays, not silent replacements for any specialized scenario repository. The central compressed factory manifest still must add the test-org aggregate explicitly before deterministic generated governance is treated as converged.

## Provisioning and promotion behavior

Each aggregate repository was initialized through a reviewable bootstrap branch and pull request. Production dependencies use immutable commit coordinates. GitHub Actions and the PostgreSQL service image are pinned by digest/SHA. Unavailable engines or credentials remain explicit source/environment gates rather than being reported as passing tests.

Pull-request validation remains credential-free. Database service credentials and expensive integration environments belong only in protected GitHub environments, scheduled jobs, or manual dispatches. Destructive targets are permitted only in the test organization and must use ephemeral or explicitly disposable infrastructure.

The machine-readable source for this finding is `docs/CANONICAL-FLEET-DRIFT.json`.
