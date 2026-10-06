#!/usr/bin/env python3
"""Evidence-reference and audit-maturity checks.

This complements tools/research_lint.py. The first linter protects structural
integrity; this one protects research maturity claims by checking that Claim
Evidence references resolve to real ledger entries and that high-risk Case
myths (solo/micro-team, zero-marketing/market-access) complete explicit audits
before a Case can reach REVIEW/STABLE.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
AUDIT_STATES = {"pending", "partial", "complete", "not_applicable"}
SMALL_TEAM_TAGS = {"solo", "micro-team", "three-person-team"}
QUALIFYING_SOURCE_CLASSES = {"P0", "P1", "S1"}
REF_RE = re.compile(r"^(CASE-\d{3}):(E\d{3,})$")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_json(rel: str) -> dict[str, Any]:
    path = ROOT / rel
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"{rel}: cannot load JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        err(f"{rel}: top-level value must be an object")
        return {}
    return data


def source_class_token(raw: str) -> str:
    # Examples: "P0 — contemporaneous primary", "P0/P1 — creator postmortem"
    prefix = raw.strip().split("—", 1)[0].strip()
    for token in ("P0", "P1", "S1", "S2", "H"):
        if token in prefix:
            return token
    return "UNKNOWN"


def source_locator_errors(block: str) -> list[str]:
    """Check citation fields, not whether the cited page proves a claim."""
    fields = {
        key.strip().lower(): value.strip()
        for key, value in re.findall(r"^-[ \t]+([^:\n]+):[ \t]*([^\n]+)$", block, re.M)
    }
    issues = []
    url_ok = bool(re.search(r"https?://[^\s<>]+", fields.get("url", "")))
    nonpublic_locator = fields.get("locator", "")
    source_class = fields.get("source class", "")
    personal_communication_ok = (
        source_class.upper().startswith("P0")
        and re.match(r"PERSONAL COMMUNICATION\b", nonpublic_locator, re.I)
    )
    if not url_ok and not personal_communication_ok:
        issues.append("missing specific source URL or accepted P0 personal-communication locator")
    if not fields.get("title") or fields["title"].upper().startswith("UNKNOWN"):
        issues.append("missing source title")
    author = next((fields[key] for key in ("author", "institution", "author / institution") if fields.get(key)), "")
    if not author or author.upper().startswith("UNKNOWN"):
        issues.append("missing author or institution")
    published = next((fields[key] for key in ("published", "publication date") if fields.get(key)), "")
    if not re.match(r"(?:\d{4}-\d{2}-\d{2}|UNKNOWN\b)", published, re.I):
        issues.append("missing publication date or explicit UNKNOWN")
    if not re.match(r"\d{4}-\d{2}-\d{2}\b", fields.get("accessed", "")):
        issues.append("missing access date")
    return issues


def parse_ledger(case_id: str, rel: str, *, require_locators: bool = False) -> dict[str, str]:
    path = ROOT / rel
    if not path.exists():
        err(f"{case_id}: evidence ledger missing: {rel}")
        return {}
    lines = path.read_text(encoding="utf-8").splitlines()
    out: dict[str, str] = {}
    blocks: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines:
        m = re.match(r"^##\s+(E\d{3,})\b", line.strip())
        if m:
            current = m.group(1)
            if current in out:
                err(f"{rel}: duplicate Evidence ID {current}")
            out[current] = "UNKNOWN"
            blocks[current] = []
            continue
        if current:
            blocks[current].append(line)
            m = re.match(r"^-\s+(?:Class|Source class):\s*(.+)$", line.strip(), flags=re.I)
            if m:
                out[current] = source_class_token(m.group(1))
    for eid, cls in out.items():
        if cls == "UNKNOWN":
            warn(f"{rel}: {eid} has no parseable source class")
        if require_locators and cls in {"P0", "P1", "S1", "S2"}:
            for issue in source_locator_errors("\n".join(blocks[eid])):
                err(f"{rel}: {eid}: {issue}")
    return out


def build_evidence_registry(cases: dict[str, dict[str, Any]]) -> dict[str, str]:
    registry: dict[str, str] = {}
    for case_id, item in cases.items():
        ledger = item.get("evidence_ledger")
        if not ledger:
            continue
        for eid, source_class in parse_ledger(
            case_id, str(ledger), require_locators=item.get("schema_version") == 2
        ).items():
            ref = f"{case_id}:{eid}"
            if ref in registry:
                err(f"duplicate global Evidence ref {ref}")
            registry[ref] = source_class
    return registry


def validate_case_audits(cases: dict[str, dict[str, Any]]) -> None:
    for case_id, item in cases.items():
        status = str(item.get("research_status", ""))
        tags = set(item.get("tags") or [])
        claims = set(item.get("related_claims") or [])

        contributor = item.get("contributor_audit")
        market = item.get("market_access_audit")
        if contributor not in AUDIT_STATES:
            err(f"{case_id}: invalid contributor_audit={contributor!r}")
        if market not in AUDIT_STATES:
            err(f"{case_id}: invalid market_access_audit={market!r}")

        needs_contributor = bool(tags & SMALL_TEAM_TAGS)
        needs_market = "C010" in claims or "market-access" in tags

        if needs_contributor and contributor == "not_applicable":
            err(f"{case_id}: small-team/solo Case cannot mark contributor_audit not_applicable")
        if needs_market and market == "not_applicable":
            err(f"{case_id}: C010/market-access Case cannot mark market_access_audit not_applicable")

        if status == "RESEARCHING":
            if needs_contributor and contributor == "pending":
                warn(f"{case_id}: RESEARCHING small-team Case still has contributor_audit=pending")
            if needs_market and market == "pending":
                warn(f"{case_id}: RESEARCHING market-access Case still has market_access_audit=pending")

        if status in {"REVIEW", "STABLE"}:
            if needs_contributor and contributor != "complete":
                err(f"{case_id}: {status} requires contributor_audit=complete")
            if needs_market and market != "complete":
                err(f"{case_id}: {status} requires market_access_audit=complete")


def validate_claim_evidence(
    claims: dict[str, dict[str, Any]],
    registry: dict[str, str],
) -> None:
    for claim_id, item in claims.items():
        status = str(item.get("status", ""))
        related_cases = set(item.get("related_cases") or [])
        refs = item.get("evidence_ids") or []
        if not isinstance(refs, list):
            err(f"{claim_id}: evidence_ids must be a list")
            continue

        classes: list[str] = []
        for ref in refs:
            ref = str(ref)
            m = REF_RE.fullmatch(ref)
            if not m:
                err(f"{claim_id}: invalid Evidence ref {ref!r}; expected CASE-001:E001")
                continue
            case_id = m.group(1)
            if case_id not in related_cases:
                err(f"{claim_id}: Evidence {ref} comes from Case not listed in related_cases")
            if ref not in registry:
                err(f"{claim_id}: Evidence ref does not resolve: {ref}")
                continue
            classes.append(registry[ref])

        if status in {"SUPPORTED", "VERIFIED"}:
            if not refs:
                err(f"{claim_id}: {status} requires at least one Evidence ref")
            if not any(cls in QUALIFYING_SOURCE_CLASSES for cls in classes):
                err(f"{claim_id}: {status} requires at least one P0/P1/S1 Evidence source")

        if status == "VERIFIED" and not any(cls in {"P0", "P1"} for cls in classes):
            warn(f"{claim_id}: VERIFIED has no P0/P1 source; review whether status is too strong")

        if status == "REFUTED" and refs and not any(cls in QUALIFYING_SOURCE_CLASSES for cls in classes):
            warn(f"{claim_id}: REFUTED relies only on weak/H evidence classes")


def main() -> int:
    case_doc = load_json("metadata/cases.json")
    claim_doc = load_json("metadata/claims.json")
    raw_cases = case_doc.get("cases", [])
    raw_claims = claim_doc.get("claims", [])
    cases = {
        str(x.get("case_id")): x
        for x in raw_cases
        if isinstance(x, dict) and x.get("case_id")
    }
    claims = {
        str(x.get("claim_id")): x
        for x in raw_claims
        if isinstance(x, dict) and x.get("claim_id")
    }

    validate_case_audits(cases)
    registry = build_evidence_registry(cases)
    validate_claim_evidence(claims, registry)

    print(f"Evidence registry: {len(registry)} parsed evidence records")
    for msg in warnings:
        print(f"WARNING: {msg}", file=sys.stderr)
    for msg in errors:
        print(f"ERROR: {msg}", file=sys.stderr)
    if errors:
        print(f"research_evidence_lint: FAILED with {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"research_evidence_lint: OK with {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
