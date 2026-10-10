#!/usr/bin/env python3
"""Report drift between the reader layer and the evidence it claims to rest on.

This is an *audit*, not a gate.  It surfaces three mechanically checkable
signals that `book/EDITORIAL-GATE.md` section 0.6 cares about:

1. years used in a profile that appear nowhere in its Case / Evidence layer;
2. profile -> Case / Evidence Ledger backlinks that are missing or broken;
3. quote-like passages at ledger and individual Evidence-record level.

A hit is a prompt to re-read the original source, not proof of an error.
Quote matching is a heuristic: quoted prose may be paraphrased, too short to match,
or unrelated to the sourced fact. An apparent quote is NOT proof of verification.
Approximate phrasing ("c. 2009") and phases the evidence layer has not yet
absorbed both produce legitimate hits, which is why this does not block merges.

Known limitation, measured 2026-10-09: the year check is a plain "does this
year string appear in the evidence text" test. Writing a note that *mentions*
a year - even a note saying the year is unsupported - makes the drift
disappear. CASE-007's 2009 left the drift list exactly this way, while
remaining unresolved in substance; the ledger now explains why.

So treat an empty drift list as weak evidence, not as confirmation. Read the
ledger, not just the audit output.

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
LONG_QUOTE_RE = re.compile(r'"[^"]{60,}"|“[^”]{20,}”')
CASE_LINK_RE = re.compile(r"\(\.\./\.\./cases/(CASE-\d{3}[^)\s]*\.md)\)")
LEDGER_LINK_RE = re.compile(r"\(\.\./\.\./evidence/(CASE-\d{3}[^)\s]*\.md)\)")
EVIDENCE_HEADING_RE = re.compile(r"(?m)^## (E\d{3})\b[^\n]*$")
SOURCE_CLASS_RE = re.compile(r"(?mi)^\s*-\s*(?:Source class|Class):\s*([^\n]+)")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def years(text: str) -> set[str]:
    return set(YEAR_RE.findall(text))


def evidence_records(text: str) -> list[tuple[str, str]]:
    """Extract record ID and body; headings outside E001-style records are ignored."""
    headings = list(EVIDENCE_HEADING_RE.finditer(text))
    return [
        (heading.group(1), text[heading.end():headings[i + 1].start() if i + 1 < len(headings) else len(text)])
        for i, heading in enumerate(headings)
    ]


def is_primary_record(body: str) -> bool:
    """Only explicit P0/P1 class declarations trigger a primary-source warning."""
    match = SOURCE_CLASS_RE.search(body)
    return bool(match and re.search(r"\bP[01]\b", match.group(1)))


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

    # Only numbered canonical ledgers count; README and intake notes are NOT ledgers.
    ledgers = sorted(EVIDENCE.glob("CASE-*-source-ledger.md"))
    ledger_with_quote = [p for p in ledgers if LONG_QUOTE_RE.search(read(p))]
    ledger_pct = (100 * len(ledger_with_quote)) // max(1, len(ledgers))

    # Per-record coverage is more informative than 'one quote somewhere in a ledger'.
    records = []
    for path in ledgers:
        for record_id, body in evidence_records(read(path)):
            records.append((
                path.name,
                record_id,
                len(body),
                bool(LONG_QUOTE_RE.search(body)),
                is_primary_record(body),
            ))

    mean_density = sum(item[2] for item in records) // max(1, len(records))
    thin = [item for item in records if item[2] < 700]
    no_quote = [item for item in records if not item[3]]
    primary_no_quote = [item for item in no_quote if item[4]]
    thin_no_quote = [item for item in thin if not item[3]]

    print("reader/evidence sync audit (report only, does not block merges)")
    print(f"profiles: {len(profiles)}, with backlink problems: {len(backlink_problems)}")
    for message in backlink_problems:
        print(f"  - {message}")
    print(f"profiles with year drift: {len(year_drift)}")
    for message in year_drift:
        print(f"  - {message}")
    print(f"canonical ledgers: {len(ledgers)}; with detectable long quotes: {len(ledger_with_quote)} ({ledger_pct}%)")
    print(f"numbered Evidence records: {len(records)}; without detectable long quote: {len(no_quote)}")
    print(f"  P0/P1 records without detectable long quote: {len(primary_no_quote)}")
    print(f"mean record-body length: {mean_density} chars; {len(thin)} records under 700 chars")
    print(f"  thin AND without detectable long quote: {len(thin_no_quote)}")
    print("First 12 P0/P1 record-level source-refresh candidates (not a severity ranking):")
    for name, record_id, chars, _, _ in primary_no_quote[:12]:
        print(f"  - {name} / {record_id}: {chars} chars")
    print("Heuristics only: quotes may be too short, misattributed or not checked against the original.")
    print("Re-read the original source before changing Evidence, Case or reader prose (EDITORIAL-GATE 0.6).")

    if args.strict and (backlink_problems or year_drift):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
