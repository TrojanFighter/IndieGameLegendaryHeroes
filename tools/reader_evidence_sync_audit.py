#!/usr/bin/env python3
"""Report drift between the reader layer and the evidence it claims to rest on.

This is an *audit*, not a gate.  It surfaces three mechanically checkable
signals that `book/EDITORIAL-GATE.md` section 0.6 cares about:

1. years used in a profile that appear nowhere in its Case / Evidence layer;
2. profile -> Case / Evidence Ledger backlinks that are missing or broken;
3. how many ledgers preserve at least one verbatim quote.

A hit is a prompt to re-read the original source, not proof of an error.
Approximate phrasing ("c. 2009") and phases the evidence layer has not yet
absorbed both produce legitimate hits, which is why this does not block merges.
Exit status is 0 unless --strict is passed, and even then only drift from
categories 1 and 2 counts.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "book/profiles"
CASES = ROOT / "cases"
EVIDENCE = ROOT / "evidence"

YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")
LONG_QUOTE_RE = re.compile(r'"[^"]{60,}"')
CASE_LINK_RE = re.compile(r"\(\.\./\.\./cases/(CASE-\d{3}[^)\s]*\.md)\)")
LEDGER_LINK_RE = re.compile(r"\(\.\./\.\./evidence/(CASE-\d{3}[^)\s]*\.md)\)")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def years(text: str) -> set[str]:
    return set(YEAR_RE.findall(text))


def main() -> int:
    parser = argparse.ArgumentParser(description="reader/evidence sync audit")
    parser.add_argument("--strict", action="store_true", help="exit 1 when either hard category reports drift")
    args = parser.parse_args()

    profiles = sorted(p for p in PROFILES.glob("*.md") if p.name != "README.md")
    if not profiles:
        print("reader/evidence sync audit: no profiles found")
        return 1

    backlink_problems: list[str] = []
    year_drift: list[str] = []

    for profile in profiles:
        text = read(profile)
        rel = profile.relative_to(ROOT).as_posix()
        case_links = CASE_LINK_RE.findall(text)
        ledger_links = LEDGER_LINK_RE.findall(text)

        if not case_links:
            backlink_problems.append(f"{rel}: no Case backlink")
        if not ledger_links:
            backlink_problems.append(f"{rel}: no Evidence Ledger backlink")
        for name in case_links:
            if not (CASES / name).exists():
                backlink_problems.append(f"{rel}: missing case file {name}")
        for name in ledger_links:
            if not (EVIDENCE / name).exists():
                backlink_problems.append(f"{rel}: missing ledger file {name}")

        evidence_text = "".join(read(CASES / n) for n in case_links)
        evidence_text += "".join(read(EVIDENCE / n) for n in ledger_links)
        missing = sorted(years(text) - years(evidence_text))
        if missing:
            year_drift.append(f"{rel}: {', '.join(missing)}")

    ledgers = sorted(EVIDENCE.glob("*.md"))
    with_quote = [p for p in ledgers if LONG_QUOTE_RE.search(read(p))]
    pct = (100 * len(with_quote)) // max(1, len(ledgers))

    print("reader/evidence sync audit (report only, does not block merges)")
    print(f"profiles: {len(profiles)}, with backlink problems: {len(backlink_problems)}")
    for message in backlink_problems:
        print(f"  - {message}")
    print(f"profiles with year drift: {len(year_drift)}")
    for message in year_drift:
        print(f"  - {message}")
    print(f"ledgers: {len(ledgers)}, with >=1 verbatim quote: {len(with_quote)} ({pct}%)")
    print("Re-read the original source for each hit before editing anything (EDITORIAL-GATE 0.6).")

    if args.strict and (backlink_problems or year_drift):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
