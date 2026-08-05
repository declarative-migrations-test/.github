# declarative-migrations-test

Independent acceptance organization for **declarative-migrations**.

Forward/rollback, engine compatibility, locking, drift, failure atomicity, CLI, and MCP migration certification.

## Portfolio

| Repository | Class | Readiness | Primary dependency path |
|---|---|---|---|
| `postgres-forward-rollback` | database conformance | `ready` | `matrix` |
| `cockroach-forward-rollback` | database conformance | `ready` | `matrix` |
| `cross-engine-compatibility` | database conformance | `ready` | `matrix` |
| `concurrent-migrator-lock` | chaos/fault injection | `ready` | `matrix` |
| `failure-injection-atomicity` | chaos/fault injection | `ready` | `matrix` |
| `schema-drift-detection` | database conformance | `ready` | `matrix` |
| `cli-mcp-contract` | MCP contract | `ready` | `matrix` |

Pull requests run deterministic harness checks. Emulators, desktop matrices, live APIs/providers, databases, chaos, scale, and soaks are scheduled/manual. Missing upstreams or credentials are blocked readiness—not false passes or product regressions.

<!-- org-project-routing:start -->
## Planning and delivery

- [GitHub Project: declarative-migrations-test-project](https://github.com/orgs/declarative-migrations-test/projects/1)
- [Linear planning project](https://linear.app/denman/project/githubcomdeclarative-migrations-test-7e6b5d911bd8)
- [Detailed project-routing contract](../docs/PROJECTS.md)

GitHub owns code and delivery evidence; Linear owns planning and dependencies. The linked organization Project provides the cross-repository execution view.
<!-- org-project-routing:end -->
