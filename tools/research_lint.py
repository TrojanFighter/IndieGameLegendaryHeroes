#!/usr/bin/env python3
"""Repository integrity checks for IndieGameLegendaryHeroes.

No third-party dependencies. The linter intentionally reads the canonical Markdown
files instead of maintaining a parallel database.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CASE_STATUSES = {"SKELETON", "RESEARCHING", "REVIEW", "STABLE"}
CLAIM_STATUSES = {"UNVERIFIED", "WEAK", "SUPPORTED", "CONTESTED", "VERIFIED", "REFUTED"}
RATINGS = {"UNRATED", "NONE", "LOW", "MEDIUM", "HIGH"}
CASE_REQUIRED = {
    "type",
    "case_id",
    "status",
    "subject",
    "related_claims",
    "evidence_strength",
    "explanatory_importance",
    "narrative_value",
    "last_verified",
}

errors: list[str] = []
warnings: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def parse_scalar(value: str):
    value = value.strip()
    if value in {"null", "NULL", "~", ""}:
        return None
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        if not body:
            return []
        return [item.strip().strip('"\'') for item in body.split(",")]
    return value.strip('"\'')


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        err(f"{path.relative_to(ROOT)}: missing YAML-compatible frontmatter")
        return {}
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        err(f"{path.relative_to(ROOT)}: unclosed frontmatter")
        return {}

    data: dict[str, object] = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            err(f"{path.relative_to(ROOT)}: invalid frontmatter line: {line!r}")
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        if key in data:
            err(f"{path.relative_to(ROOT)}: duplicate frontmatter key {key}")
        data[key] = parse_scalar(value)
    return data


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


def read_claim_index() -> dict[str, dict[str, str]]:
    path = ROOT / "claims" / "README.md"
    claims: dict[str, dict[str, str]] = {}
    for cells in markdown_rows(path):
        if not re.fullmatch(r"C\d{3}", cells[0]):
            continue
        if len(cells) != 6:
            err(f"claims/README.md: {cells[0]} must have exactly 6 columns; found {len(cells)}")
            continue
        cid, statement, status, evidence, importance, narrative = cells
        if cid in claims:
            err(f"claims/README.md: duplicate Claim ID {cid}")
            continue
        claims[cid] = {
            "statement": statement,
            "status": status,
            "evidence_strength": evidence,
            "explanatory_importance": importance,
            "narrative_value": narrative,
        }
        if status not in CLAIM_STATUSES:
            err(f"claims/README.md: {cid} invalid status {status}")
        for field, value in (
            ("evidence_strength", evidence),
            ("explanatory_importance", importance),
            ("narrative_value", narrative),
        ):
            if value not in RATINGS:
                err(f"claims/README.md: {cid} invalid {field} {value}")
        if status == "VERIFIED" and evidence in {"NONE", "LOW", "UNRATED"}:
            err(f"claims/README.md: {cid} is VERIFIED but evidence_strength={evidence}")
    if not claims:
        err("claims/README.md: no machine-readable Claim rows found")
    return claims


def read_case_index() -> dict[str, str]:
    path = ROOT / "cases" / "README.md"
    index: dict[str, str] = {}
    for cells in markdown_rows(path):
        if not re.fullmatch(r"CASE-\d{3}", cells[0]):
            continue
        if len(cells) < 4:
            err(f"cases/README.md: malformed row for {cells[0]}")
            continue
        cid, status = cells[0], cells[3]
        if cid in index:
            err(f"cases/README.md: duplicate Case ID {cid}")
        index[cid] = status
    return index


def check_relative_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\((\.\./[^)#]+)\)", text):
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            warn(f"{path.relative_to(ROOT)}: relative link escapes repository: {target}")
            continue
        if not resolved.exists():
            err(f"{path.relative_to(ROOT)}: broken relative link {target}")


def check_cases(claims: dict[str, dict[str, str]]) -> tuple[dict[str, dict[str, object]], dict[str, int]]:
    cases: dict[str, dict[str, object]] = {}
    counts = {status: 0 for status in CASE_STATUSES}
    for path in sorted((ROOT / "cases").glob("CASE-*.md")):
        meta = parse_frontmatter(path)
        if not meta:
            continue
        missing = CASE_REQUIRED - set(meta)
        if missing:
            err(f"{path.relative_to(ROOT)}: missing frontmatter keys {sorted(missing)}")
        cid = str(meta.get("case_id", ""))
        if not re.fullmatch(r"CASE-\d{3}", cid):
            err(f"{path.relative_to(ROOT)}: invalid case_id {cid!r}")
            continue
        if not path.name.startswith(cid):
            err(f"{path.relative_to(ROOT)}: filename does not match case_id {cid}")
        if cid in cases:
            err(f"duplicate Case ID {cid}")
        cases[cid] = meta

        if meta.get("type") != "case":
            err(f"{path.relative_to(ROOT)}: type must be 'case'")
        status = str(meta.get("status", ""))
        if status not in CASE_STATUSES:
            err(f"{path.relative_to(ROOT)}: invalid status {status}")
        else:
            counts[status] += 1
        for field in ("evidence_strength", "explanatory_importance", "narrative_value"):
            value = str(meta.get(field, ""))
            if value not in RATINGS:
                err(f"{path.relative_to(ROOT)}: invalid {field} {value}")
        related = meta.get("related_claims")
        if not isinstance(related, list):
            err(f"{path.relative_to(ROOT)}: related_claims must use [C001, C002] list syntax")
        else:
            for claim_id in related:
                if claim_id not in claims:
                    err(f"{path.relative_to(ROOT)}: references unknown Claim {claim_id}")
        last_verified = meta.get("last_verified")
        if last_verified is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(last_verified)):
            err(f"{path.relative_to(ROOT)}: last_verified must be YYYY-MM-DD or null")
        if status != "SKELETON" and meta.get("evidence_strength") == "NONE":
            warn(f"{path.relative_to(ROOT)}: active Case has evidence_strength=NONE")
        check_relative_links(path)
    if not cases:
        err("cases/: no Case files found")
    return cases, counts


def crosscheck_case_index(cases: dict[str, dict[str, object]]) -> None:
    index = read_case_index()
    for cid, meta in cases.items():
        if cid not in index:
            err(f"cases/README.md: missing {cid}")
            continue
        if index[cid] != meta.get("status"):
            err(f"cases/README.md: {cid} status={index[cid]} but frontmatter={meta.get('status')}")
    for cid in index:
        if cid not in cases:
            err(f"cases/README.md: indexes missing file {cid}")


def print_summary(claims: dict[str, dict[str, str]], cases: dict[str, dict[str, object]], case_counts: dict[str, int]) -> None:
    claim_counts = {status: 0 for status in CLAIM_STATUSES}
    for item in claims.values():
        claim_counts[item["status"]] += 1
    print("Research corpus summary")
    print(f"  Cases:  {len(cases)}")
    print("  Case status: " + ", ".join(f"{k}={case_counts[k]}" for k in sorted(case_counts)))
    print(f"  Claims: {len(claims)}")
    print("  Claim status: " + ", ".join(f"{k}={claim_counts[k]}" for k in sorted(claim_counts)))


def main() -> int:
    claims = read_claim_index()
    cases, case_counts = check_cases(claims)
    crosscheck_case_index(cases)
    print_summary(claims, cases, case_counts)

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
