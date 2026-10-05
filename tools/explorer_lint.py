#!/usr/bin/env python3
"""Validate the Case Explorer's dependency contract without duplicating research lint.

The Explorer is a view over canonical metadata. This check protects the fields the UI
actually consumes and prevents case facts from being hard-coded into explorer/index.html.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "metadata" / "cases.json"
CLAIMS = ROOT / "metadata" / "claims.json"
INDEX = ROOT / "explorer" / "index.html"

CASE_REQUIRED = {
    "case_id",
    "file",
    "subject",
    "research_status",
    "evidence_strength",
    "explanatory_importance",
    "related_claims",
    "tags",
    "last_verified",
    "evidence_ledger",
    "contributor_audit",
    "market_access_audit",
}
CLAIM_REQUIRED = {"claim_id", "statement", "status"}
AUDIT_VALUES = {"pending", "partial", "complete", "unknown", "not_applicable"}
CONTEXT_VALUES = AUDIT_VALUES


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for path in (CASES, CLAIMS, INDEX):
        if not path.exists():
            fail(errors, f"missing Explorer dependency: {path.relative_to(ROOT)}")
    if errors:
        return report(errors)

    cases_doc = load(CASES)
    claims_doc = load(CLAIMS)
    cases = cases_doc.get("cases")
    claims = claims_doc.get("claims")
    if not isinstance(cases, list):
        fail(errors, "metadata/cases.json: cases must be a list")
        cases = []
    if not isinstance(claims, list):
        fail(errors, "metadata/claims.json: claims must be a list")
        claims = []

    claim_ids: set[str] = set()
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            fail(errors, f"claims[{i}] must be an object")
            continue
        missing = CLAIM_REQUIRED - claim.keys()
        if missing:
            fail(errors, f"{claim.get('claim_id', f'claims[{i}]')}: missing Explorer claim fields {sorted(missing)}")
        cid = claim.get("claim_id")
        if cid:
            if cid in claim_ids:
                fail(errors, f"duplicate claim_id: {cid}")
            claim_ids.add(cid)

    case_ids: set[str] = set()
    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(errors, f"cases[{i}] must be an object")
            continue
        cid = case.get("case_id", f"cases[{i}]")
        missing = CASE_REQUIRED - case.keys()
        if missing:
            fail(errors, f"{cid}: missing Explorer case fields {sorted(missing)}")
        if isinstance(cid, str):
            if cid in case_ids:
                fail(errors, f"duplicate case_id: {cid}")
            case_ids.add(cid)
        for field in ("file", "evidence_ledger"):
            value = case.get(field)
            if isinstance(value, str) and value:
                target = ROOT / value
                if not target.exists():
                    fail(errors, f"{cid}: {field} target does not exist: {value}")
        related = case.get("related_claims", [])
        if not isinstance(related, list):
            fail(errors, f"{cid}: related_claims must be a list")
        else:
            unknown = sorted(set(related) - claim_ids)
            if unknown:
                fail(errors, f"{cid}: Explorer would reference unknown claims {unknown}")
        if not isinstance(case.get("tags", []), list):
            fail(errors, f"{cid}: tags must be a list")
        for field in ("contributor_audit", "market_access_audit"):
            value = case.get(field)
            if value not in AUDIT_VALUES:
                fail(errors, f"{cid}: unsupported {field}={value!r}; update metadata or Explorer contract deliberately")
        if "context_audit" in case and case["context_audit"] not in CONTEXT_VALUES:
            fail(errors, f"{cid}: unsupported context_audit={case['context_audit']!r}")

    html = INDEX.read_text(encoding="utf-8")
    for expected in ("../metadata/cases.json", "../metadata/claims.json"):
        if expected not in html:
            fail(errors, f"explorer/index.html must consume canonical source {expected}")

    # A view should not quietly become a second hand-maintained case database.
    hardcoded = sorted(set(re.findall(r"CASE-\d{3}", html)))
    if hardcoded:
        fail(errors, f"explorer/index.html hard-codes Case IDs {hardcoded}; read them from metadata instead")

    return report(errors)


def report(errors: list[str]) -> int:
    if errors:
        print("Explorer contract check FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Explorer contract check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
