# Declarative Migrations Certification

This organization independently certifies [`declarative-migrations/declarative-postgres-migrate.rs`](https://github.com/declarative-migrations/declarative-postgres-migrate.rs) against real PostgreSQL and CockroachDB instances. The live fleet is pinned to production commit `21eb846e356b2a5aff068b21e77903e6cca50452` until a reviewed dependency-update pull request advances it.

## Active certification lanes

- [`postgres-rollback-e2e`](https://github.com/declarative-migrations-test/postgres-rollback-e2e) — PostgreSQL 16 and 17: repeated forward migration, fail-closed gated rollback, explicit destructive rollback, idempotency, final convergence, and preserved rows.
- [`cockroachdb-rollback-e2e`](https://github.com/declarative-migrations-test/cockroachdb-rollback-e2e) — CockroachDB 25.2.4: the same repeated forward/rollback and data-preservation contract under CockroachDB schema semantics.
- [`failed-step-atomicity-e2e`](https://github.com/declarative-migrations-test/failed-step-atomicity-e2e) — Late-step failure injection, engine-specific catalog inspection, residual drift, operator repair, and eventual convergence on both engines.
- [`schema-drift-e2e`](https://github.com/declarative-migrations-test/schema-drift-e2e) — Unauthorized table, column, and index drift; diff exit `2`; gated apply exit `3`; explicitly approved repair on both engines.

## Reserved scaffold lanes

The following repositories exist but remain intentionally marked as scaffolds until a reviewed pull request adds executable assertions and a green live workflow:

- [`cross-version-matrix-e2e`](https://github.com/declarative-migrations-test/cross-version-matrix-e2e)
- [`concurrent-migration-e2e`](https://github.com/declarative-migrations-test/concurrent-migration-e2e)
- [`idempotent-replay-e2e`](https://github.com/declarative-migrations-test/idempotent-replay-e2e)
- [`data-preservation-e2e`](https://github.com/declarative-migrations-test/data-preservation-e2e)
- [`cli-install-e2e`](https://github.com/declarative-migrations-test/cli-install-e2e)
- [`homebrew-install-e2e`](https://github.com/declarative-migrations-test/homebrew-install-e2e)
- [`fuzz-property-e2e`](https://github.com/declarative-migrations-test/fuzz-property-e2e)
- [`mcp-contract-e2e`](https://github.com/declarative-migrations-test/mcp-contract-e2e)

The organization profile never treats a README-only repository as tested coverage. A lane becomes active only after its repository-local pull request passes the relevant live contract.
