#!/usr/bin/env python3
"""Validate the declarative-migrations-test aggregate E2E portfolio."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_SCENARIO_CLASSES = {
    "forward-and-rollback",
    "idempotent-replay",
    "schema-drift-detection",
    "data-preservation",
    "failure-atomicity",
    "concurrent-migrator-locking",
    "cross-engine-compatibility",
    "upgrade-compatibility",
    "chaos-recovery",
    "cli-installation",
    "cli-mcp-contract",
    "contract-conformance",
    "security-boundary",
    "fuzz-and-property",
}

REQUIRED_AGGREGATE_SCENARIOS = {
    "lib-core-schema-and-generated-adapter-parity",
    "api-write-web-read-only-permissions",
    "web-mutation-routes-through-api",
    "shared-auth-audience-and-actor-handoff",
    "serialized-migrator-and-empty-post-apply-diff",
    "immutable-zed-package-install-and-lock",
    "exact-evidence-bundle-generation",
}

SECRET_PATTERNS = (
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"lin_api_[A-Za-z0-9]{20,}"),
    re.compile(r"cfat_[A-Za-z0-9_-]{20,}"),
    re.compile(r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY"),
)


class PortfolioError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PortfolioError(message)


def unique_strings(value: Any, path: str) -> list[str]:
    require(isinstance(value, list), f"{path} must be an array")
    require(all(isinstance(item, str) and item for item in value), f"{path} must contain non-empty strings")
    require(len(value) == len(set(value)), f"{path} contains duplicates")
    return value


def walk_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in walk_strings(item)]
    if isinstance(value, dict):
        return [text for key, item in value.items() for text in (*walk_strings(key), *walk_strings(item))]
    return []


def validate(data: dict[str, Any]) -> None:
    require(data.get("schema_version") == 1, "schema_version must be 1")
    require(data.get("portfolio_id") == "declmig-e2e-test", "portfolio_id mismatch")
    require(data.get("audited_at") == "2026-08-09", "audited_at must match the reconciliation date")
    require(data.get("aggregate_repository") == "declarative-migrations-test/declmig-e2e", "test aggregate repository mismatch")
    require(data.get("production_aggregate_repository") == "declarative-migrations/declmig-e2e", "production aggregate repository mismatch")
    require(data.get("production_contract") == "declarative-migrations/.github:e2e/declmig-e2e.contract.json", "production contract pointer mismatch")
    require(data.get("source_repository") == "declarative-migrations/declarative-postgres-migrate.rs", "source repository mismatch")
    require(data.get("source_ref_policy") == "full-commit-sha", "candidate source must use a full commit SHA")

    destructive = data.get("destructive_targets")
    require(isinstance(destructive, dict), "destructive_targets must be an object")
    require(destructive.get("allowed") is True, "test aggregate must permit destructive ephemeral testing")
    require(destructive.get("required_target_class") == "ephemeral-or-explicitly-disposable", "destructive targets must be disposable")
    require(destructive.get("production_credentials_allowed") is False, "production credentials are forbidden")
    require(destructive.get("production_database_targets_allowed") is False, "production database targets are forbidden")

    lanes = data.get("execution_lanes")
    require(isinstance(lanes, dict), "execution_lanes must be an object")
    require(set(lanes) == {"pull_request", "scheduled", "protected_manual"}, "execution lanes must be pull_request, scheduled, and protected_manual")
    pull_request = lanes["pull_request"]
    require(pull_request.get("secrets") is False, "pull-request validation must be secretless")
    require(pull_request.get("network_writes") is False, "pull-request validation must not perform network writes")
    for lane_name, lane in lanes.items():
        unique_strings(lane.get("scenarios"), f"execution_lanes.{lane_name}.scenarios")

    scenarios = data.get("scenario_repositories")
    require(isinstance(scenarios, dict), "scenario_repositories must be an object")
    require(REQUIRED_SCENARIO_CLASSES.issubset(set(scenarios)), "specialized scenario classes are incomplete")
    repositories: list[str] = []
    for scenario, names in scenarios.items():
        values = unique_strings(names, f"scenario_repositories.{scenario}")
        require(all(name.startswith("declarative-migrations-test/") for name in values), f"{scenario} references a repository outside the test organization")
        require("declarative-migrations-test/declmig-e2e" not in values, "the aggregate repository must not list itself as a specialized lane")
        repositories.extend(values)
    require(len(repositories) >= 16, "portfolio must map at least 16 specialized repository lanes")
    require(len(repositories) == len(set(repositories)), "specialized repositories must have one canonical scenario owner")

    aggregate_scenarios = set(unique_strings(data.get("required_new_aggregate_scenarios"), "required_new_aggregate_scenarios"))
    require(REQUIRED_AGGREGATE_SCENARIOS == aggregate_scenarios, "aggregate-only scenario set mismatch")

    evidence = data.get("evidence_bundle")
    require(isinstance(evidence, dict), "evidence_bundle must be an object")
    require(evidence.get("format") == "json-lines-plus-artifacts", "evidence format mismatch")
    require(evidence.get("immutable") is True, "evidence must be immutable")
    require(evidence.get("required_hash") == "sha256", "evidence must use SHA-256")
    required_fields = set(unique_strings(evidence.get("required_fields"), "evidence_bundle.required_fields"))
    require({"source_commit", "workflow_commit", "run_id", "scenario", "result", "artifact_sha256"}.issubset(required_fields), "evidence fields are incomplete")
    require(evidence.get("consumer") == "declarative-migrations/declmig-e2e", "production evidence consumer mismatch")
    require(data.get("promotion_rule") == "all-required-test-lanes-pass-before-production-aggregate", "promotion rule mismatch")

    for text in walk_strings(data):
        for pattern in SECRET_PATTERNS:
            require(pattern.search(text) is None, "portfolio contains secret-like material")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("portfolio", nargs="?", default="e2e/declmig-e2e.portfolio.json")
    args = parser.parse_args()
    path = Path(args.portfolio)
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        require(isinstance(parsed, dict), "portfolio root must be an object")
        validate(parsed)
    except (OSError, json.JSONDecodeError, PortfolioError) as exc:
        print(f"declmig portfolio validation failed: {exc}", file=sys.stderr)
        return 1

    repository_count = sum(len(value) for value in parsed["scenario_repositories"].values())
    print(
        "declmig test portfolio valid: "
        f"{len(parsed['scenario_repositories'])} scenario classes, "
        f"{repository_count} specialized repositories"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
