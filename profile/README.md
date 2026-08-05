# Declarative Migrations Certification

This organization independently certifies [`declarative-migrations/declarative-postgres-migrate.rs`](https://github.com/declarative-migrations/declarative-postgres-migrate.rs) against real PostgreSQL and CockroachDB instances. Production is pinned at `21eb846e356b2a5aff068b21e77903e6cca50452` until a reviewed dependency-update pull request advances the fleet.

## Repositories

- [`postgres-forward-rollback`](https://github.com/declarative-migrations-test/postgres-forward-rollback) — Repeated forward and destructive rollback certification against live PostgreSQL with schema convergence and data-preservation assertions.
- [`cockroach-forward-rollback`](https://github.com/declarative-migrations-test/cockroach-forward-rollback) — Repeated forward and destructive rollback certification against a live CockroachDB instance under Cockroach DDL semantics.
- [`cross-engine-compatibility`](https://github.com/declarative-migrations-test/cross-engine-compatibility) — Portable-plan, catalog-signature, and cross-dialect refusal certification across PostgreSQL and CockroachDB.
- [`concurrent-migrator-lock`](https://github.com/declarative-migrations-test/concurrent-migrator-lock) — Concurrent migrator stress certification, final convergence proof, idempotent replay, and actionable contender failure classification.
- [`failure-injection-atomicity`](https://github.com/declarative-migrations-test/failure-injection-atomicity) — Fault-injection certification for partial DDL failure, residual drift reporting, operator repair, and eventual convergence on both engines.
- [`schema-drift-detection`](https://github.com/declarative-migrations-test/schema-drift-detection) — Unauthorized schema drift detection and fail-closed apply certification against live PostgreSQL and CockroachDB.
- [`cli-mcp-contract`](https://github.com/declarative-migrations-test/cli-mcp-contract) — CLI exit-code, flags-to-environment, JSON-plan, and guarded JSON-RPC/MCP adapter contract certification.

The fleet covers repeated forward/rollback cycles, cross-engine portability, concurrent migrators, injected partial failures, unauthorized drift, CLI semantics, and a guarded JSON-RPC/MCP adapter contract.
