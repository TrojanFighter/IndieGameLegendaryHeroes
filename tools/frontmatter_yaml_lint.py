#!/usr/bin/env python3
"""Validate YAML frontmatter in Markdown files.

This check exists because repository-specific linters may successfully read fields
with ad-hoc parsing even when GitHub/Obsidian cannot parse the YAML itself.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def frontmatter_block(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[1:index])

    raise ValueError("opening frontmatter delimiter has no closing '---'")


def main() -> int:
    failures: list[str] = []
    checked = 0

    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue

        try:
            block = frontmatter_block(path)
        except ValueError as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")
            continue

        if block is None:
            continue

        checked += 1
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError as exc:
            mark = getattr(exc, "problem_mark", None)
            if mark is not None:
                location = f"frontmatter line {mark.line + 1}, column {mark.column + 1}"
            else:
                location = "unknown frontmatter location"
            failures.append(f"{path.relative_to(ROOT)}: {location}: {exc}")
            continue

        if parsed is not None and not isinstance(parsed, dict):
            failures.append(
                f"{path.relative_to(ROOT)}: frontmatter must parse to a YAML mapping, "
                f"got {type(parsed).__name__}"
            )

    if failures:
        print("YAML frontmatter validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"YAML frontmatter validation passed for {checked} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
