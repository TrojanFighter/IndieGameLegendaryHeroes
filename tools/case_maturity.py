#!/usr/bin/env python3
"""Derive Case research maturity without creating a second fact source.

The script reads metadata/cases.json only. It never edits Case status. Its job is
to identify structural blockers and research gaps, and to reject premature
promotion to REVIEW/STABLE.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "metadata" / "cases.json"

DONE_AUDIT = {"complete", "n/a", "na", "not_applicable", "bounded_unknown"}
LOW_EVIDENCE = {"none", "low", "unrated", ""}


def norm(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip().lower()


def derive(case: dict[str, Any]) -> dict[str, Any]:
    case_id = case["case_id"]
    formal = str(case.get("research_status", "")).upper()
    evidence = norm(case.get("evidence_strength"))
    schema_version = case.get("schema_version")
    context = norm(case.get("context_audit"))
    contributor = norm(case.get("contributor_audit"))
    market = norm(case.get("market_access_audit"))

    blockers: list[str] = []
    gaps: list[str] = []
    warnings: list[str] = []

    case_file = ROOT / case.get("file", "")
    ledger_file = ROOT / case.get("evidence_ledger", "")

    if formal == "SKELETON":
        blockers.append("formal_status_skeleton")
    if evidence in LOW_EVIDENCE:
        blockers.append(f"evidence_strength_{evidence or 'missing'}")
    if not case_file.is_file():
        blockers.append("case_file_missing")
    if not ledger_file.is_file():
        blockers.append("evidence_ledger_missing")

    # Schema v1 is legitimate legacy data, but it is not graduation-ready.
    if schema_version != 2:
        gaps.append("legacy_schema_v1_requires_case_research_migration")
    elif context not in DONE_AUDIT:
        gaps.append(f"context_audit_{context or 'missing'}")

    if contributor not in DONE_AUDIT:
        gaps.append(f"contributor_audit_{contributor or 'missing'}")
    if market not in DONE_AUDIT:
        gaps.append(f"market_access_audit_{market or 'missing'}")

    # Weak Signals / H / UNKNOWN are deliberately not machine blockers. Their
    # materiality and recoverability belong to adversarial Graduation Review.
    warnings.append("manual_adversarial_review_required_before_stable")

    if blockers:
        derived = "BLOCKED"
    elif gaps:
        derived = "NEEDS_RESEARCH"
    elif formal == "STABLE":
        derived = "STABLE"
    else:
        derived = "REVIEW_READY"

    if blockers:
        next_action = "resolve_hard_blockers"
    elif "legacy_schema_v1_requires_case_research_migration" in gaps:
        next_action = "migrate_case_to_schema_v2_during_lane_b_research"
    elif any(item.startswith("context_audit_") for item in gaps):
        next_action = "complete_context_situation_action_audit"
    elif any(item.startswith("contributor_audit_") for item in gaps):
        next_action = "complete_contributor_perimeter_audit"
    elif any(item.startswith("market_access_audit_") for item in gaps):
        next_action = "complete_market_access_audit"
    elif derived == "REVIEW_READY":
        next_action = "run_adversarial_graduation_review"
    else:
        next_action = "maintain_stable_case_only_on_material_delta"

    return {
        "case_id": case_id,
        "formal_status": formal,
        "derived_state": derived,
        "blockers": blockers,
        "research_gaps": gaps,
        "warnings": warnings,
        "next_action": next_action,
    }


def load_cases() -> list[dict[str, Any]]:
    payload = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    return payload["cases"]


def build_report() -> dict[str, Any]:
    rows = [derive(case) for case in load_cases()]
    summary: dict[str, int] = {}
    for row in rows:
        summary[row["derived_state"]] = summary.get(row["derived_state"], 0) + 1
    return {
        "derived": True,
        "source": "metadata/cases.json",
        "summary": dict(sorted(summary.items())),
        "cases": rows,
    }


def check_premature_promotions(report: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for row in report["cases"]:
        if row["formal_status"] in {"REVIEW", "STABLE"} and row["derived_state"] in {
            "BLOCKED",
            "NEEDS_RESEARCH",
        }:
            errors.append(
                f"{row['case_id']}: formal status {row['formal_status']} is premature; "
                f"derived={row['derived_state']} blockers={row['blockers']} gaps={row['research_gaps']}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full derived report as JSON instead of a compact table.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail only when a Case has been promoted to REVIEW/STABLE before structural gates are ready.",
    )
    args = parser.parse_args()

    report = build_report()

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        summary = report["summary"]
        print("Case maturity (derived, non-canonical):")
        print("  " + ", ".join(f"{key}={value}" for key, value in summary.items()))
        for row in report["cases"]:
            if row["derived_state"] != "REVIEW_READY" and row["formal_status"] != "STABLE":
                print(
                    f"  {row['case_id']}: {row['derived_state']} -> {row['next_action']}"
                )

    if args.check:
        errors = check_premature_promotions(report)
        if errors:
            print("\nPremature Case promotion detected:")
            for error in errors:
                print(f"  ERROR: {error}")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
