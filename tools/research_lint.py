#!/usr/bin/env python3
"""Research integrity checks for IndieGameLegendaryHeroes.

The Markdown files remain the human-readable research corpus.  The JSON files under
metadata/ are sidecar indexes for status, relationships, ratings and future search/
AI tooling.  This linter keeps the two layers synchronized without requiring YAML
frontmatter or third-party Python dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

CASE_STATUSES = {"SKELETON", "RESEARCHING", "REVIEW", "STABLE"}
CLAIM_STATUSES = {"UNVERIFIED", "WEAK", "SUPPORTED", "CONTESTED", "VERIFIED", "REFUTED"}
EVIDENCE_STRENGTH = {"none", "low", "medium", "high"}
IMPORTANCE = {"unrated", "low", "medium", "high", "critical"}
NARRATIVE_VALUE = {"unrated", "low", "medium", "high", "critical"}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

errors: list[str] = []
warnings: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def load_json(rel: str) -> dict[str, Any]:
    path = ROOT / rel
    if not path.exists():
        err(f"missing {rel}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"{rel}: invalid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        err(f"{rel}: top-level value must be an object")
        return {}
    return value


def markdown_rows(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or all(re.fullmatch(r":?-+:?", cell or "-") for cell in cells):
            continue
        rows.append(cells)
    return rows


def read_case_index() -> dict[str, dict[str, str]]:
    path = ROOT / "cases" / "README.md"
    out: dict[str, dict[str, str]] = {}
    for cells in markdown_rows(path):
        if not re.fullmatch(r"CASE-\d{3}", cells[0]):
            continue
        if len(cells) != 4:
            err(f"cases/README.md: {cells[0]} must have 4 columns, found {len(cells)}")
            continue
        cid, subject, purpose, status = cells
        if cid in out:
            err(f"cases/README.md: duplicate Case ID {cid}")
            continue
        out[cid] = {"subject": subject, "purpose": purpose, "status": status}
    if not out:
        err("cases/README.md: no Case rows found")
    return out


def read_claim_index() -> dict[str, dict[str, str]]:
    path = ROOT / "claims" / "README.md"
    out: dict[str, dict[str, str]] = {}
    for cells in markdown_rows(path):
        if not re.fullmatch(r"C\d{3}", cells[0]):
            continue
        if len(cells) != 3:
            err(f"claims/README.md: {cells[0]} must have 3 columns, found {len(cells)}")
            continue
        cid, statement, status = cells
        if cid in out:
            err(f"claims/README.md: duplicate Claim ID {cid}")
            continue
        out[cid] = {"statement": statement, "status": status}
    if not out:
        err("claims/README.md: no Claim rows found")
    return out


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def validate_cases(case_doc: dict[str, Any], claim_ids: set[str]) -> dict[str, dict[str, Any]]:
    raw = case_doc.get("cases", [])
    if not isinstance(raw, list):
        err("metadata/cases.json: cases must be a list")
        return {}

    cases: dict[str, dict[str, Any]] = {}
    required = {
        "case_id", "file", "subject", "research_status", "evidence_strength",
        "explanatory_importance", "narrative_value", "related_claims", "tags",
        "last_verified", "evidence_ledger",
    }

    for item in raw:
        if not isinstance(item, dict):
            err("metadata/cases.json: every case must be an object")
            continue
        missing = required - set(item)
        cid = str(item.get("case_id", "<missing>"))
        if missing:
            err(f"metadata/cases.json: {cid} missing fields {sorted(missing)}")
        if not re.fullmatch(r"CASE-\d{3}", cid):
            err(f"metadata/cases.json: invalid case_id {cid!r}")
            continue
        if cid in cases:
            err(f"metadata/cases.json: duplicate Case ID {cid}")
            continue
        cases[cid] = item

        status = item.get("research_status")
        if status not in CASE_STATUSES:
            err(f"metadata/cases.json: {cid} invalid research_status {status!r}")
        strength = item.get("evidence_strength")
        if strength not in EVIDENCE_STRENGTH:
            err(f"metadata/cases.json: {cid} invalid evidence_strength {strength!r}")
        importance = item.get("explanatory_importance")
        if importance not in IMPORTANCE:
            err(f"metadata/cases.json: {cid} invalid explanatory_importance {importance!r}")
        narrative = item.get("narrative_value")
        if narrative not in NARRATIVE_VALUE:
            err(f"metadata/cases.json: {cid} invalid narrative_value {narrative!r}")

        rel = item.get("related_claims")
        if not isinstance(rel, list):
            err(f"metadata/cases.json: {cid} related_claims must be a list")
            rel = []
        if len(rel) != len(set(rel)):
            err(f"metadata/cases.json: {cid} has duplicate related_claims")
        for claim_id in rel:
            if claim_id not in claim_ids:
                err(f"metadata/cases.json: {cid} references unknown Claim {claim_id}")

        tags = item.get("tags")
        if not isinstance(tags, list):
            err(f"metadata/cases.json: {cid} tags must be a list")
        elif len(tags) != len(set(tags)):
            err(f"metadata/cases.json: {cid} has duplicate tags")

        last_verified = item.get("last_verified")
        if last_verified is not None and not DATE_RE.fullmatch(str(last_verified)):
            err(f"metadata/cases.json: {cid} last_verified must be YYYY-MM-DD or null")

        rel_path = str(item.get("file", ""))
        path = ROOT / rel_path
        if not path.exists():
            err(f"metadata/cases.json: {cid} file does not exist: {rel_path}")
            continue
        if not path.name.startswith(cid):
            err(f"metadata/cases.json: {cid} file name does not begin with Case ID: {rel_path}")
        text = path.read_text(encoding="utf-8")
        first_line = text.splitlines()[0] if text.splitlines() else ""
        if cid not in first_line:
            err(f"{rel_path}: first heading does not contain {cid}")

        body_claims = re.search(r"^- Related Claims:\s*(.+)$", text, flags=re.MULTILINE)
        if body_claims:
            parsed = [part.strip() for part in body_claims.group(1).split(",") if part.strip()]
            if parsed != rel:
                err(f"{rel_path}: Related Claims {parsed} != metadata {rel}")
        else:
            warn(f"{rel_path}: no human-readable Related Claims line found")

        ledger = item.get("evidence_ledger")
        if ledger is not None:
            ledger_path = ROOT / str(ledger)
            if not ledger_path.exists():
                err(f"metadata/cases.json: {cid} evidence_ledger missing: {ledger}")
        elif status in {"REVIEW", "STABLE"}:
            err(f"metadata/cases.json: {cid} is {status} but has no evidence_ledger")

        if status == "STABLE" and re.search(r"\bTODO\b", text, flags=re.IGNORECASE):
            err(f"{rel_path}: STABLE Case still contains TODO")
        if status != "SKELETON" and strength in {"none", "low"}:
            warn(f"metadata/cases.json: {cid} is {status} but evidence_strength={strength}")

    disk_files = {str(p.relative_to(ROOT)) for p in (ROOT / "cases").glob("CASE-*.md")}
    registry_files = {str(item.get("file")) for item in cases.values()}
    for path in sorted(disk_files - registry_files):
        err(f"metadata/cases.json: unregistered Case file {path}")
    for path in sorted(registry_files - disk_files):
        err(f"metadata/cases.json: registry points to non-Case file {path}")
    return cases


def validate_claims(claim_doc: dict[str, Any], case_ids: set[str]) -> dict[str, dict[str, Any]]:
    raw = claim_doc.get("claims", [])
    if not isinstance(raw, list):
        err("metadata/claims.json: claims must be a list")
        return {}

    claims: dict[str, dict[str, Any]] = {}
    required = {
        "claim_id", "statement", "status", "evidence_strength",
        "explanatory_importance", "narrative_value", "related_cases",
        "evidence_ids", "last_reviewed",
    }

    for item in raw:
        if not isinstance(item, dict):
            err("metadata/claims.json: every claim must be an object")
            continue
        cid = str(item.get("claim_id", "<missing>"))
        missing = required - set(item)
        if missing:
            err(f"metadata/claims.json: {cid} missing fields {sorted(missing)}")
        if not re.fullmatch(r"C\d{3}", cid):
            err(f"metadata/claims.json: invalid claim_id {cid!r}")
            continue
        if cid in claims:
            err(f"metadata/claims.json: duplicate Claim ID {cid}")
            continue
        claims[cid] = item

        status = item.get("status")
        if status not in CLAIM_STATUSES:
            err(f"metadata/claims.json: {cid} invalid status {status!r}")
        strength = item.get("evidence_strength")
        if strength not in EVIDENCE_STRENGTH:
            err(f"metadata/claims.json: {cid} invalid evidence_strength {strength!r}")
        if item.get("explanatory_importance") not in IMPORTANCE:
            err(f"metadata/claims.json: {cid} invalid explanatory_importance {item.get('explanatory_importance')!r}")
        if item.get("narrative_value") not in NARRATIVE_VALUE:
            err(f"metadata/claims.json: {cid} invalid narrative_value {item.get('narrative_value')!r}")

        related = item.get("related_cases")
        if not isinstance(related, list):
            err(f"metadata/claims.json: {cid} related_cases must be a list")
            related = []
        if len(related) != len(set(related)):
            err(f"metadata/claims.json: {cid} has duplicate related_cases")
        for case_id in related:
            if case_id not in case_ids:
                err(f"metadata/claims.json: {cid} references unknown Case {case_id}")

        evidence_ids = item.get("evidence_ids")
        if not isinstance(evidence_ids, list):
            err(f"metadata/claims.json: {cid} evidence_ids must be a list")
            evidence_ids = []
        if status in {"SUPPORTED", "VERIFIED"} and not evidence_ids:
            err(f"metadata/claims.json: {cid} is {status} but evidence_ids is empty")
        if status == "VERIFIED" and strength != "high":
            err(f"metadata/claims.json: {cid} is VERIFIED but evidence_strength={strength!r}, expected high")
        if status == "SUPPORTED" and strength in {"none", "low"}:
            err(f"metadata/claims.json: {cid} is SUPPORTED but evidence_strength={strength!r}")
        if status == "REFUTED" and not evidence_ids:
            warn(f"metadata/claims.json: {cid} is REFUTED but evidence_ids is empty")

        last_reviewed = item.get("last_reviewed")
        if last_reviewed is not None and not DATE_RE.fullmatch(str(last_reviewed)):
            err(f"metadata/claims.json: {cid} last_reviewed must be YYYY-MM-DD or null")

    return claims


def crosscheck_indexes(cases: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]) -> None:
    case_index = read_case_index()
    claim_index = read_claim_index()

    if set(case_index) != set(cases):
        for cid in sorted(set(cases) - set(case_index)):
            err(f"cases/README.md: missing {cid}")
        for cid in sorted(set(case_index) - set(cases)):
            err(f"cases/README.md: indexes unregistered {cid}")
    for cid in sorted(set(case_index) & set(cases)):
        if case_index[cid]["status"] != cases[cid].get("research_status"):
            err(
                f"cases/README.md: {cid} status={case_index[cid]['status']} "
                f"but metadata={cases[cid].get('research_status')}"
            )

    if set(claim_index) != set(claims):
        for cid in sorted(set(claims) - set(claim_index)):
            err(f"claims/README.md: missing {cid}")
        for cid in sorted(set(claim_index) - set(claims)):
            err(f"claims/README.md: indexes unregistered {cid}")
    for cid in sorted(set(claim_index) & set(claims)):
        if claim_index[cid]["status"] != claims[cid].get("status"):
            err(
                f"claims/README.md: {cid} status={claim_index[cid]['status']} "
                f"but metadata={claims[cid].get('status')}"
            )
        if normalize_space(claim_index[cid]["statement"]) != normalize_space(str(claims[cid].get("statement", ""))):
            err(f"claims/README.md: {cid} statement differs from metadata/claims.json")


def crosscheck_relations(cases: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]) -> None:
    for case_id, case in cases.items():
        for claim_id in case.get("related_claims", []):
            if claim_id in claims and case_id not in claims[claim_id].get("related_cases", []):
                err(f"asymmetric relation: {case_id} -> {claim_id}, but reverse link is missing")
    for claim_id, claim in claims.items():
        for case_id in claim.get("related_cases", []):
            if case_id in cases and claim_id not in cases[case_id].get("related_claims", []):
                err(f"asymmetric relation: {claim_id} -> {case_id}, but reverse link is missing")


def make_stats(cases: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        "version": 1,
        "source": ["metadata/cases.json", "metadata/claims.json"],
        "cases": {
            "total": len(cases),
            "status": dict(sorted(Counter(str(v.get("research_status")) for v in cases.values()).items())),
            "evidence_strength": dict(sorted(Counter(str(v.get("evidence_strength")) for v in cases.values()).items())),
            "explanatory_importance": dict(sorted(Counter(str(v.get("explanatory_importance")) for v in cases.values()).items())),
            "narrative_value": dict(sorted(Counter(str(v.get("narrative_value")) for v in cases.values()).items())),
        },
        "claims": {
            "total": len(claims),
            "status": dict(sorted(Counter(str(v.get("status")) for v in claims.values()).items())),
            "evidence_strength": dict(sorted(Counter(str(v.get("evidence_strength")) for v in claims.values()).items())),
            "explanatory_importance": dict(sorted(Counter(str(v.get("explanatory_importance")) for v in claims.values()).items())),
            "narrative_value": dict(sorted(Counter(str(v.get("narrative_value")) for v in claims.values()).items())),
        },
    }


def check_or_write_stats(stats: dict[str, Any], write: bool) -> None:
    path = ROOT / "metadata" / "research-stats.json"
    expected = json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if write:
        path.write_text(expected, encoding="utf-8")
        return
    if not path.exists():
        err("metadata/research-stats.json missing; run: python tools/research_lint.py --write-stats")
        return
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        err("metadata/research-stats.json is stale; run: python tools/research_lint.py --write-stats")


def print_summary(stats: dict[str, Any]) -> None:
    print("Research corpus summary")
    print(f"  Cases:  {stats['cases']['total']} — {stats['cases']['status']}")
    print(f"  Claims: {stats['claims']['total']} — {stats['claims']['status']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="CI mode; warnings stay non-fatal, structural drift fails")
    parser.add_argument("--write-stats", action="store_true", help="rewrite metadata/research-stats.json from canonical metadata")
    args = parser.parse_args()

    case_doc = load_json("metadata/cases.json")
    claim_doc = load_json("metadata/claims.json")

    claim_ids = {
        str(item.get("claim_id"))
        for item in claim_doc.get("claims", [])
        if isinstance(item, dict) and item.get("claim_id")
    }
    case_ids = {
        str(item.get("case_id"))
        for item in case_doc.get("cases", [])
        if isinstance(item, dict) and item.get("case_id")
    }

    cases = validate_cases(case_doc, claim_ids)
    claims = validate_claims(claim_doc, case_ids)
    crosscheck_indexes(cases, claims)
    crosscheck_relations(cases, claims)

    stats = make_stats(cases, claims)
    check_or_write_stats(stats, args.write_stats)
    print_summary(stats)

    for message in warnings:
        print(f"WARNING: {message}", file=sys.stderr)
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)

    if errors:
        print(f"research_lint: FAILED with {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"research_lint: OK with {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
