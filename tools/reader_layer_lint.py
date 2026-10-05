#!/usr/bin/env python3
"""Check that the reader-facing layer stays aligned with the research backend.

The research corpus already has canonical machine indexes under metadata/.  This
checker deliberately does not create a second registry for the book layer.  It
only makes sure the public front door cannot silently freeze at an old case /
claim count, and that every narrative profile can be audited back to a Case and
its Evidence Ledger.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        err(f"{path.relative_to(ROOT)}: cannot parse JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        err(f"{path.relative_to(ROOT)}: top-level JSON must be an object")
        return {}
    return data


cases_doc = load_json(ROOT / "metadata/cases.json")
claims_doc = load_json(ROOT / "metadata/claims.json")
cases = cases_doc.get("cases", [])
claims = claims_doc.get("claims", [])

if not isinstance(cases, list):
    err("metadata/cases.json: cases must be a list")
    cases = []
if not isinstance(claims, list):
    err("metadata/claims.json: claims must be a list")
    claims = []

root_readme_path = ROOT / "README.md"
book_readme_path = ROOT / "book/README.md"
if not root_readme_path.exists():
    err("missing README.md")
    root_readme = ""
else:
    root_readme = root_readme_path.read_text(encoding="utf-8")
if not book_readme_path.exists():
    err("missing book/README.md")
    book_readme = ""
else:
    book_readme = book_readme_path.read_text(encoding="utf-8")

case_count = len(cases)
claim_count = len(claims)
ledger_count = sum(1 for item in cases if isinstance(item, dict) and item.get("evidence_ledger"))

# These are intentionally exact enough to catch a stale headline, but do not
# constrain prose elsewhere in the README.
required_headline_fragments = [
    f"**{case_count} 个编号 Case 档案**",
    f"**{ledger_count} 份对应 Evidence Ledger**",
    f"**{claim_count} 个跨案例 Claim**",
    f"## {case_count} 个编号案例档案",
]
for fragment in required_headline_fragments:
    if fragment not in root_readme:
        err(f"README.md: stale or missing generated-count phrase: {fragment!r}")

for status, count in Counter(item.get("research_status") for item in cases if isinstance(item, dict)).items():
    if not re.search(rf"\b{count} 个 {re.escape(str(status))}\b", root_readme):
        err(f"README.md: missing research maturity count: {count} {status}")

# The front door should expose every formal Case at least once.  It may link a
# Case more often in question-led reading paths; that is fine.
known_cases: dict[str, dict] = {}
for item in cases:
    if not isinstance(item, dict):
        continue
    case_id = str(item.get("case_id", ""))
    rel = str(item.get("file", ""))
    ledger = str(item.get("evidence_ledger", ""))
    if not case_id or not rel:
        continue
    known_cases[case_id] = item
    if f"({rel})" not in root_readme:
        err(f"README.md: formal case not reachable from front door: {case_id} -> {rel}")
    if not (ROOT / rel).exists():
        err(f"{case_id}: missing Case file {rel}")
    if ledger and not (ROOT / ledger).exists():
        err(f"{case_id}: missing Evidence Ledger {ledger}")

profiles_dir = ROOT / "book/profiles"
profiles = sorted(profiles_dir.glob("*.md")) if profiles_dir.exists() else []
case_link_re = re.compile(r"\(\.\./\.\./cases/(CASE-\d{3}[^)]*\.md)\)")
ledger_link_re = re.compile(r"\(\.\./\.\./evidence/(CASE-\d{3}[^)]*\.md)\)")

for profile in profiles:
    text = profile.read_text(encoding="utf-8")
    rel_profile = profile.relative_to(ROOT / "book").as_posix()
    case_links = case_link_re.findall(text)
    ledger_links = ledger_link_re.findall(text)
    if not case_links:
        err(f"book/{rel_profile}: missing audit backlink to a Case")
        continue
    if not ledger_links:
        err(f"book/{rel_profile}: missing audit backlink to an Evidence Ledger")
        continue

    case_ids = {re.match(r"CASE-\d{3}", name).group(0) for name in case_links}
    ledger_ids = {re.match(r"CASE-\d{3}", name).group(0) for name in ledger_links}
    if case_ids != ledger_ids:
        err(f"book/{rel_profile}: Case/Evidence backlinks disagree: {sorted(case_ids)} vs {sorted(ledger_ids)}")
    for case_id in case_ids:
        if case_id not in known_cases:
            err(f"book/{rel_profile}: references unknown {case_id}")

    if f"({rel_profile})" not in book_readme:
        err(f"book/README.md: profile is not listed: {rel_profile}")

if "[`book/`](book/)" not in root_readme and "[book/](book/)" not in root_readme:
    err("README.md: book reader layer is not linked from the front door")

if errors:
    print("reader-layer lint: FAIL")
    for message in errors:
        print(f"- {message}")
    sys.exit(1)

print(
    "reader-layer lint: OK "
    f"({case_count} cases, {ledger_count} case ledgers, {claim_count} claims, {len(profiles)} profiles)"
)
