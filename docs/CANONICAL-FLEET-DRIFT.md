# Declarative Migrations canonical test-fleet drift

Audit date: 2026-08-05

The current manifest in `zed-pkg-test/zed-pkg-e2e` defines twelve specialized repositories plus the organization `.github` repository for `declarative-migrations-test`.

## Current canonical coverage

Present:

- `.github`
- `cli-plan-e2e`
- `data-preservation-e2e`
- `fuzz-property-e2e`
- `homebrew-install-e2e`
- `postgres-zero-downtime-e2e`

Missing:

- `cockroachdb-rollback-e2e`
- `mysql-shadow-e2e`
- `postgres-lock-contention-e2e`
- `redshift-advisory-e2e`
- `schema-change-online-e2e`
- `snowflake-advisory-e2e`
- `sqlite-migration-e2e`

Several older migration test repositories also exist. They are intentional historical or independently added coverage and must be preserved; they do not replace the current canonical profiles.

## Required provisioning behavior

Each missing repository must be initialized through a reviewable bootstrap branch and pull request. Available production dependencies must use immutable commit coordinates. Unavailable engines or credentials must remain explicit source/environment gates rather than being reported as passing tests.

Pull-request validation must remain credential-free. Database service credentials and expensive integration environments belong only in protected GitHub environments, scheduled jobs, or manual dispatches.

The machine-readable source for this finding is `docs/CANONICAL-FLEET-DRIFT.json`.
