#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
relationships = json.loads((root / "repository-relationships.json").read_text())
expected = [
    ".github",
    "postgres-rollback-e2e",
    "cockroachdb-rollback-e2e",
    "cross-version-matrix-e2e",
    "concurrent-migration-e2e",
    "failed-step-atomicity-e2e",
    "schema-drift-e2e",
    "idempotent-replay-e2e",
    "data-preservation-e2e",
    "cli-install-e2e",
    "homebrew-install-e2e",
    "fuzz-property-e2e",
    "mcp-contract-e2e",
]
active = {
    ".github",
    "postgres-rollback-e2e",
    "cockroachdb-rollback-e2e",
    "failed-step-atomicity-e2e",
    "schema-drift-e2e",
}
rows = relationships["repositories"]
observed = [row["name"] for row in rows]
assert observed == expected, (observed, expected)
assert relationships["schema_version"] == 2
assert relationships["organization"] == "declarative-migrations-test"
assert relationships["production"]["commit"] == "21eb846e356b2a5aff068b21e77903e6cca50452"
assert {row["name"] for row in rows if row["state"] == "active"} == active
assert all(row["state"] in {"active", "scaffold"} for row in rows)
assert all(isinstance(row["coverage"], str) and row["coverage"] for row in rows)
for path in [
    "profile/README.md",
    "SECURITY.md",
    "repository-relationships.json",
    "workflow-templates/dpm-certification.yml",
    "workflow-templates/dpm-certification.properties.json",
]:
    assert (root / path).is_file(), path
print("organization profile contract validated")
