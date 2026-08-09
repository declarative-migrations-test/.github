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

Both requested aggregate orchestration repositories are provisioned, their bootstrap pull requests are merged, and post-merge `main` certification is green:

- `declarative-migrations-test/declmig-e2e`: candidate, destructive, failure-injection, concurrency, engine, and permission certification; PR `#1`, merge `201779ef3af3f2516a01a8223ac1d02c073ca39c`, main run `31332843970`.
- `declarative-migrations/declmig-e2e`: stable release-promotion orchestration; PR `#1`, merge `ac9a8c23c736a53885da21a53ed34545eb1a103f`, main run `31332941841`.

Both certified exact DPM source commit `39d1d9da93127145a0d5b4d3e65bb23638f84ca9` against digest-pinned PostgreSQL 17. Both produced the same exact DPM binary SHA-256: `5445759b9d243e2f34957ecb63589b3320a5741ed854d1848708efb4d0b114bc`.

The aggregate repositories are portfolio overlays, not replacements for specialized scenario repositories. The central compressed factory manifest still must add the test-org aggregate explicitly before deterministic generated governance is fully converged.

## Promotion behavior

Pull-request validation remains credential-free. GitHub Actions, the Rust toolchain, source commit, and PostgreSQL service image use immutable identities. Destructive targets are permitted only in the test organization and must be ephemeral or explicitly disposable.

The initial PostgreSQL diff → verify → apply → catalog assertions → empty post-apply diff lane is complete. Cross-org evidence consumption, the broader engine/failure/concurrency matrix, permission-denial tests, Shared Auth handoff, `*-lib-core` parity, and immutable Zed package certification remain active work.

The machine-readable source for this finding is `docs/CANONICAL-FLEET-DRIFT.json`.
