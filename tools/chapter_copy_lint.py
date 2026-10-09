#!/usr/bin/env python3
"""Keep reader-facing chapter prose free of research-backend vocabulary.

`book/BOOK-ARCHITECTURE.md` requires chapter prose to stay clear of backend
terms: evidence tiers (`P0`/`P1`/`S1`/`S2`), research statuses
(`RESEARCHING`, `SKELETON`), pipeline words (`lint`, `metadata`), and the
temporal-validity status labels (`DURABLE`, `CONDITIONAL`).

Two deliberate exceptions:

- markdown table rows: the temporal-validity card is a schema-bound structure
  whose status cells are canonical vocabulary, not prose;
- link labels: the end-of-chapter entry list names claims by their canonical
  English title, which may itself contain a backend word such as `runway`.

Everything else in a chapter file is reader prose and is checked.  This tool
does not judge style or readability; it only stops backend vocabulary from
leaking back into the chapter layer.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "book/chapters"

# Backend vocabulary that must not appear in chapter prose.
BANNED_TERMS = (
    "P0",
    "P1",
    "S1",
    "S2",
    "RESEARCHING",
    "SKELETON",
    "STABLE",
    "UNVERIFIED",
    "SUPPORTED",
    "metadata",
    "lint",
    "evidence_strength",
    "evidence ledger",
    "Evidence Ledger",
    "DURABLE",
    "CONDITIONAL",
    "runway",
    "证据增强",
    "承诺升级",
)

LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")

errors: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def term_pattern(term: str) -> re.Pattern[str]:
    # ASCII-only boundaries: a CJK neighbour such as "S1材料" must still match,
    # so \b cannot be used here (Python treats CJK characters as word chars).
    return re.compile(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])")


PATTERNS = [(term, term_pattern(term)) for term in BANNED_TERMS]

if not CHAPTERS_DIR.exists():
    err("missing book/chapters directory")
    chapters: list[Path] = []
else:
    chapters = sorted(CHAPTERS_DIR.glob("*.md"))
    if not chapters:
        err("book/chapters: no chapter files found")

for chapter in chapters:
    rel = chapter.relative_to(ROOT).as_posix()
    text = chapter.read_text(encoding="utf-8")
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if line.startswith("|"):
            continue  # schema-bound table row (temporal-validity card)
        prose = LINK_RE.sub(" ", line)
        for term, pattern in PATTERNS:
            if pattern.search(prose):
                err(f"{rel}:{lineno}: backend term {term!r} in reader prose")

if errors:
    print("chapter-copy lint: FAIL")
    for message in errors:
        print(f"- {message}")
    sys.exit(1)

print(f"chapter-copy lint: OK ({len(chapters)} chapter files)")
