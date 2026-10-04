#!/usr/bin/env python3
"""Validate Case Schema v2 Context–Situation–Action requirements.

CASE-001..CASE-026 are grandfathered Schema v1 cases. They migrate only when
case research supplies the missing historical context; library operations must
not invent facts merely to satisfy a new schema.

CASE-027+ must use Schema v2 from creation.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEGACY_MAX_CASE = 26
VALID_CONTEXT = {"pending", "partial", "complete"}
MATURE = {"REVIEW", "STABLE"}

errors: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def load_cases() -> list[dict[str, Any]]:
    path = ROOT / "metadata/cases.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        err(f"metadata/cases.json: cannot load: {exc}")
        return []
    raw = data.get("cases")
    if not isinstance(raw, list):
        err("metadata/cases.json: cases must be a list")
        return []
    return [x for x in raw if isinstance(x, dict)]


def case_number(case_id: str) -> int | None:
    m = re.fullmatch(r"CASE-(\d{3})", case_id)
    return int(m.group(1)) if m else None


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip().strip("\"'")
    return out


def has_heading(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE) is not None


def validate() -> None:
    cases = load_cases()
    legacy = 0
    v2 = 0
    migrated_legacy = 0

    for item in cases:
        cid = str(item.get("case_id", ""))
        number = case_number(cid)
        if number is None:
            continue  # structural lint owns invalid IDs

        schema_raw = item.get("schema_version", 1)
        try:
            schema_version = int(schema_raw)
        except (TypeError, ValueError):
            err(f"{cid}: schema_version must be an integer")
            continue

        status = str(item.get("research_status", ""))
        context = item.get("context_audit")

        if number > LEGACY_MAX_CASE and schema_version < 2:
            err(f"{cid}: CASE-{LEGACY_MAX_CASE + 1:03d}+ must use schema_version 2")

        if schema_version < 2:
            legacy += 1
            if status in MATURE:
                err(f"{cid}: {status} Case must migrate to Schema v2 and complete context audit")
            continue

        v2 += 1
        if number <= LEGACY_MAX_CASE:
            migrated_legacy += 1

        if context not in VALID_CONTEXT:
            err(f"{cid}: Schema v2 requires context_audit in {sorted(VALID_CONTEXT)}")

        rel = item.get("file")
        if not isinstance(rel, str):
            err(f"{cid}: missing Case file path")
            continue
        path = ROOT / rel
        if not path.exists():
            continue  # structural lint reports the missing file
        text = path.read_text(encoding="utf-8")

        required_headings = {
            "Context–Situation–Action Snapshot": r"^##\s+2\.\s+Context[–-]Situation[–-]Action Snapshot\s*$",
            "Era / Production Regime": r"^###\s+Era\s*/\s*Production Regime\s*$",
            "Actor Situation": r"^###\s+Actor Situation\s*$",
            "Action / Maneuver": r"^###\s+Action\s*/\s*Maneuver\s*$",
            "Anachronism Check": r"^###\s+Anachronism Check\s*$",
        }
        for label, pattern in required_headings.items():
            if not has_heading(text, pattern):
                err(f"{cid}: Schema v2 missing heading: {label}")

        fm = frontmatter(text)
        if not fm:
            err(f"{cid}: Schema v2 requires frontmatter")
        else:
            if fm.get("schema_version") != "2":
                err(f"{cid}: frontmatter schema_version must be 2")
            fm_context = fm.get("context_audit", "").lower()
            if context in VALID_CONTEXT and fm_context != str(context).lower():
                err(
                    f"{cid}: frontmatter context_audit={fm_context!r} "
                    f"!= metadata {context!r}"
                )

        if status in MATURE and context != "complete":
            err(f"{cid}: {status} requires context_audit=complete")

    print(
        "Context audit summary: "
        f"legacy_v1={legacy}, schema_v2={v2}, migrated_legacy={migrated_legacy}"
    )


if __name__ == "__main__":
    validate()
    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        print(f"context_audit_lint: FAILED with {len(errors)} error(s)", file=sys.stderr)
        raise SystemExit(1)
    print("context_audit_lint: OK")
