#!/usr/bin/env python3
"""Research integrity checks for IndieGameLegendaryHeroes.

Markdown remains the human-readable research corpus. JSON under metadata/ is the
sidecar machine index. YAML frontmatter in Case files is optional: if present,
this linter checks it against the sidecar instead of requiring it.
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
NARRATIVE = {"unrated", "low", "medium", "high", "critical"}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_json(rel: str) -> dict[str, Any]:
    path = ROOT / rel
    if not path.exists():
        err(f"missing {rel}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        err(f"{rel}: invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        err(f"{rel}: top-level value must be an object")
        return {}
    return data


def markdown_rows(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or all(re.fullmatch(r":?-+:?", c or "-") for c in cells):
            continue
        rows.append(cells)
    return rows


def parse_simple_value(value: str) -> Any:
    value = value.strip()
    if value in {"", "null", "NULL", "~"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        return [] if not body else [x.strip().strip("\"'") for x in body.split(",")]
    return value.strip("\"'")


def optional_frontmatter(text: str) -> dict[str, Any] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        err("unclosed YAML-compatible frontmatter")
        return {}
    data: dict[str, Any] = {}
    for line in lines[1:end]:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if ":" not in s:
            err(f"invalid frontmatter line: {line!r}")
            continue
        key, value = s.split(":", 1)
        data[key.strip()] = parse_simple_value(value)
    return data


def case_index() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for cells in markdown_rows(ROOT / "cases/README.md"):
        if not re.fullmatch(r"CASE-\d{3}", cells[0]):
            continue
        if len(cells) != 4:
            err(f"cases/README.md: {cells[0]} must have 4 columns")
            continue
        cid, subject, purpose, status = cells
        if cid in out:
            err(f"cases/README.md: duplicate {cid}")
        out[cid] = {"subject": subject, "purpose": purpose, "status": status}
    return out


def claim_index() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for cells in markdown_rows(ROOT / "claims/README.md"):
        if not re.fullmatch(r"C\d{3}", cells[0]):
            continue
        if len(cells) != 3:
            err(f"claims/README.md: {cells[0]} must have 3 columns")
            continue
        cid, statement, status = cells
        if cid in out:
            err(f"claims/README.md: duplicate {cid}")
        out[cid] = {"statement": statement, "status": status}
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def validate_cases(doc: dict[str, Any], known_claims: set[str]) -> dict[str, dict[str, Any]]:
    raw = doc.get("cases", [])
    if not isinstance(raw, list):
        err("metadata/cases.json: cases must be a list")
        return {}
    required = {"case_id", "file", "subject", "research_status", "evidence_strength", "explanatory_importance", "narrative_value", "related_claims", "tags", "last_verified", "evidence_ledger"}
    out: dict[str, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            err("metadata/cases.json: every case must be an object")
            continue
        cid = str(item.get("case_id", "<missing>"))
        missing = required - set(item)
        if missing:
            err(f"metadata/cases.json: {cid} missing {sorted(missing)}")
        if not re.fullmatch(r"CASE-\d{3}", cid):
            err(f"metadata/cases.json: invalid case_id {cid!r}")
            continue
        if cid in out:
            err(f"metadata/cases.json: duplicate {cid}")
            continue
        out[cid] = item
        status = item.get("research_status")
        strength = item.get("evidence_strength")
        if status not in CASE_STATUSES:
            err(f"{cid}: invalid research_status {status!r}")
        if strength not in EVIDENCE_STRENGTH:
            err(f"{cid}: invalid evidence_strength {strength!r}")
        if item.get("explanatory_importance") not in IMPORTANCE:
            err(f"{cid}: invalid explanatory_importance")
        if item.get("narrative_value") not in NARRATIVE:
            err(f"{cid}: invalid narrative_value")
        related = item.get("related_claims")
        if not isinstance(related, list):
            err(f"{cid}: related_claims must be a list")
            related = []
        for claim_id in related:
            if claim_id not in known_claims:
                err(f"{cid}: unknown Claim {claim_id}")
        if len(related) != len(set(related)):
            err(f"{cid}: duplicate related_claims")
        tags = item.get("tags")
        if not isinstance(tags, list):
            err(f"{cid}: tags must be a list")
        last_verified = item.get("last_verified")
        if last_verified is not None and not DATE_RE.fullmatch(str(last_verified)):
            err(f"{cid}: last_verified must be YYYY-MM-DD or null")

        rel = str(item.get("file", ""))
        path = ROOT / rel
        if not path.exists():
            err(f"{cid}: missing file {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        heading = next((line for line in text.splitlines() if line.startswith("# ")), "")
        if cid not in heading:
            err(f"{rel}: first H1 heading does not contain {cid}")
        body_claims = re.search(r"^- Related Claims:\s*(.+)$", text, flags=re.MULTILINE)
        if body_claims:
            parsed = [x.strip() for x in body_claims.group(1).split(",") if x.strip()]
            if parsed != related:
                err(f"{rel}: Related Claims {parsed} != metadata {related}")
        else:
            warn(f"{rel}: no human-readable Related Claims line")

        fm = optional_frontmatter(text)
        if fm is not None:
            checks = {
                "case_id": cid,
                "status": status,
                "subject": item.get("subject"),
                "related_claims": related,
                "evidence_strength": str(strength).upper(),
                "explanatory_importance": str(item.get("explanatory_importance")).upper(),
                "narrative_value": str(item.get("narrative_value")).upper(),
                "last_verified": item.get("last_verified"),
            }
            for key, expected in checks.items():
                if key in fm and fm[key] != expected:
                    err(f"{rel}: optional frontmatter {key}={fm[key]!r} != metadata {expected!r}")

        ledger = item.get("evidence_ledger")
        if ledger is not None and not (ROOT / str(ledger)).exists():
            err(f"{cid}: missing evidence_ledger {ledger}")
        if ledger is None and status in {"REVIEW", "STABLE"}:
            err(f"{cid}: {status} requires evidence_ledger")
        if status == "STABLE" and re.search(r"\bTODO\b", text, re.I):
            err(f"{cid}: STABLE Case still contains TODO")
        if status != "SKELETON" and strength in {"none", "low"}:
            warn(f"{cid}: {status} but evidence_strength={strength}")

    disk = {p.relative_to(ROOT).as_posix() for p in (ROOT / "cases").glob("CASE-*.md")}
    reg = {str(v.get("file")) for v in out.values()}
    for path in sorted(disk - reg):
        err(f"unregistered Case file {path}")
    for path in sorted(reg - disk):
        err(f"registry points to non-Case file {path}")
    return out


def validate_claims(doc: dict[str, Any], known_cases: set[str]) -> dict[str, dict[str, Any]]:
    raw = doc.get("claims", [])
    if not isinstance(raw, list):
        err("metadata/claims.json: claims must be a list")
        return {}
    required = {"claim_id", "statement", "status", "evidence_strength", "explanatory_importance", "narrative_value", "related_cases", "evidence_ids", "last_reviewed"}
    out: dict[str, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            err("metadata/claims.json: every claim must be an object")
            continue
        cid = str(item.get("claim_id", "<missing>"))
        missing = required - set(item)
        if missing:
            err(f"metadata/claims.json: {cid} missing {sorted(missing)}")
        if not re.fullmatch(r"C\d{3}", cid):
            err(f"invalid claim_id {cid!r}")
            continue
        if cid in out:
            err(f"duplicate Claim {cid}")
            continue
        out[cid] = item
        status = item.get("status")
        strength = item.get("evidence_strength")
        if status not in CLAIM_STATUSES:
            err(f"{cid}: invalid status {status!r}")
        if strength not in EVIDENCE_STRENGTH:
            err(f"{cid}: invalid evidence_strength {strength!r}")
        if item.get("explanatory_importance") not in IMPORTANCE:
            err(f"{cid}: invalid explanatory_importance")
        if item.get("narrative_value") not in NARRATIVE:
            err(f"{cid}: invalid narrative_value")
        related = item.get("related_cases")
        if not isinstance(related, list):
            err(f"{cid}: related_cases must be a list")
            related = []
        for case_id in related:
            if case_id not in known_cases:
                err(f"{cid}: unknown Case {case_id}")
        if len(related) != len(set(related)):
            err(f"{cid}: duplicate related_cases")
        evidence_ids = item.get("evidence_ids")
        if not isinstance(evidence_ids, list):
            err(f"{cid}: evidence_ids must be a list")
            evidence_ids = []
        if status in {"SUPPORTED", "VERIFIED"} and not evidence_ids:
            err(f"{cid}: {status} requires evidence_ids")
        if status == "SUPPORTED" and strength in {"none", "low"}:
            err(f"{cid}: SUPPORTED but evidence_strength={strength}")
        if status == "VERIFIED" and strength != "high":
            err(f"{cid}: VERIFIED requires evidence_strength=high")
        if status == "REFUTED" and not evidence_ids:
            warn(f"{cid}: REFUTED but evidence_ids is empty")
        last = item.get("last_reviewed")
        if last is not None and not DATE_RE.fullmatch(str(last)):
            err(f"{cid}: last_reviewed must be YYYY-MM-DD or null")
    return out


def crosscheck(cases: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]) -> None:
    ci = case_index()
    qi = claim_index()
    for cid in sorted(set(cases) | set(ci)):
        if cid not in cases:
            err(f"cases/README.md indexes unregistered {cid}")
        elif cid not in ci:
            err(f"cases/README.md missing {cid}")
        elif ci[cid]["status"] != cases[cid].get("research_status"):
            err(f"cases/README.md: {cid} status={ci[cid]['status']} != metadata={cases[cid].get('research_status')}")
    for cid in sorted(set(claims) | set(qi)):
        if cid not in claims:
            err(f"claims/README.md indexes unregistered {cid}")
        elif cid not in qi:
            err(f"claims/README.md missing {cid}")
        else:
            if qi[cid]["status"] != claims[cid].get("status"):
                err(f"claims/README.md: {cid} status drift")
            if norm(qi[cid]["statement"]) != norm(str(claims[cid].get("statement", ""))):
                err(f"claims/README.md: {cid} statement differs from metadata")
    for case_id, case in cases.items():
        for claim_id in case.get("related_claims", []):
            if claim_id in claims and case_id not in claims[claim_id].get("related_cases", []):
                err(f"asymmetric relation: {case_id} -> {claim_id}")
    for claim_id, claim in claims.items():
        for case_id in claim.get("related_cases", []):
            if case_id in cases and claim_id not in cases[case_id].get("related_claims", []):
                err(f"asymmetric relation: {claim_id} -> {case_id}")


def stats(cases: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]) -> dict[str, Any]:
    def counts(values: list[str]) -> dict[str, int]:
        return dict(sorted(Counter(values).items()))
    return {
        "cases": {
            "evidence_strength": counts([str(v.get("evidence_strength")) for v in cases.values()]),
            "explanatory_importance": counts([str(v.get("explanatory_importance")) for v in cases.values()]),
            "narrative_value": counts([str(v.get("narrative_value")) for v in cases.values()]),
            "status": counts([str(v.get("research_status")) for v in cases.values()]),
            "total": len(cases),
        },
        "claims": {
            "evidence_strength": counts([str(v.get("evidence_strength")) for v in claims.values()]),
            "explanatory_importance": counts([str(v.get("explanatory_importance")) for v in claims.values()]),
            "narrative_value": counts([str(v.get("narrative_value")) for v in claims.values()]),
            "status": counts([str(v.get("status")) for v in claims.values()]),
            "total": len(claims),
        },
        "source": ["metadata/cases.json", "metadata/claims.json"],
        "version": 1,
    }


def check_stats(snapshot: dict[str, Any], write: bool) -> None:
    path = ROOT / "metadata/research-stats.json"
    expected = json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if write:
        path.write_text(expected, encoding="utf-8")
    elif not path.exists():
        err("metadata/research-stats.json missing; run --write-stats")
    elif path.read_text(encoding="utf-8") != expected:
        err("metadata/research-stats.json is stale; run --write-stats")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--write-stats", action="store_true")
    args = parser.parse_args()
    cdoc = load_json("metadata/cases.json")
    qdoc = load_json("metadata/claims.json")
    known_claims = {str(x.get("claim_id")) for x in qdoc.get("claims", []) if isinstance(x, dict) and x.get("claim_id")}
    known_cases = {str(x.get("case_id")) for x in cdoc.get("cases", []) if isinstance(x, dict) and x.get("case_id")}
    cases = validate_cases(cdoc, known_claims)
    claims = validate_claims(qdoc, known_cases)
    crosscheck(cases, claims)
    snapshot = stats(cases, claims)
    check_stats(snapshot, args.write_stats)
    print(f"Research corpus summary: Cases={len(cases)} {snapshot['cases']['status']}; Claims={len(claims)} {snapshot['claims']['status']}")
    for msg in warnings:
        print(f"WARNING: {msg}", file=sys.stderr)
    for msg in errors:
        print(f"ERROR: {msg}", file=sys.stderr)
    if errors:
        print(f"research_lint: FAILED with {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"research_lint: OK with {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
