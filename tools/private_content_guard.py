#!/usr/bin/env python3
"""Scan Git snapshots without embedding or printing private identifiers."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], capture_output=True)
    if result.returncode:
        raise ValueError("Git operation failed; verify the requested object/range exists")
    return result.stdout


def rules_from(source: str | None) -> dict[str, list[str]]:
    if source:
        path = Path(source).resolve()
        root = Path(git("rev-parse", "--show-toplevel").decode().strip()).resolve()
        if path.is_relative_to(root):
            raise ValueError("Rules file must be outside the repository")
        raw = path.read_text(encoding="utf-8-sig")
    else:
        raw = os.environ.get("PRIVATE_CONTENT_RULES", "")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("Rules must be a JSON object")
    for key in ("deny", "review"):
        values = data.get(key, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            raise ValueError("Rules must contain lists of nonempty strings")
        data[key] = values
    if not data["deny"]:
        raise ValueError("At least one deny rule is required")
    return data


def decode(data: bytes) -> str:
    if data.startswith((b"\xff\xfe\x00\x00", b"\x00\x00\xfe\xff")):
        return data.decode("utf-32", errors="replace")
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16", errors="replace")
    return data.decode("utf-8-sig", errors="replace")


def inspect(text: str, rules: dict[str, list[str]]) -> list[tuple[str, int, int]]:
    hits = []
    for number, line in enumerate(text.splitlines(), 1):
        folded = line.casefold()
        for level, values in rules.items():
            if level not in ("deny", "review"):
                continue
            for index, term in enumerate(values, 1):
                if term.casefold() in folded:
                    hits.append((level, index, number))
    return hits


def safe_label(label: str, rules: dict[str, list[str]]) -> str:
    # JSON escaping also prevents filenames from injecting Actions log commands.
    import re
    for term in sorted(rules["deny"] + rules["review"], key=len, reverse=True):
        label = re.sub(re.escape(term), "[redacted]", label, flags=re.I)
    return json.dumps(label, ensure_ascii=True)


def entries(revision: str | None):
    if revision is None:
        raw = git("ls-files", "--stage", "-z")
        for entry in raw.split(b"\0"):
            if entry:
                meta, name = entry.split(b"\t", 1)
                mode, oid, stage = meta.split()
                if stage != b"0":
                    raise ValueError("Resolve unmerged index entries before scanning")
                yield mode, oid.decode(), name.decode("utf-8", errors="replace")
    else:
        raw = git("ls-tree", "-r", "-z", revision)
        for entry in raw.split(b"\0"):
            if entry:
                meta, name = entry.split(b"\t", 1)
                mode, kind, oid = meta.split()
                yield mode, oid.decode(), name.decode("utf-8", errors="replace")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules", help="Private JSON file outside repository; otherwise use PRIVATE_CONTENT_RULES")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--staged", action="store_true", help="Scan complete index snapshot")
    group.add_argument("--worktree", action="store_true", help="Scan local files including ignored/untracked files")
    group.add_argument("--tree", help="Scan one committed snapshot and its message")
    group.add_argument("--range", dest="commit_range", help="Scan every commit snapshot and message in a revision range")
    group.add_argument("--message-file", help="Scan a proposed commit message")
    args = parser.parse_args(argv)
    blocked = warnings = checked = 0
    cache: dict[str, str] = {}
    try:
        rules = rules_from(args.rules)

        def scan(label: str, text: str):
            nonlocal blocked, warnings, checked
            checked += 1
            for level, index, line in inspect(text, rules):
                blocked += level == "deny"
                warnings += level == "review"
                print(f"{'ERROR' if level == 'deny' else 'REVIEW'} {safe_label(label, rules)}:{line} rule={level.upper()}-{index:03d}")

        def snapshot(revision: str | None):
            for mode, oid, name in entries(revision):
                label = f"{revision or 'INDEX'}:{name}"
                scan(label + " [path]", name)
                if mode == b"160000":
                    raise ValueError("Submodule content requires a separate audit")
                if oid not in cache:
                    cache[oid] = decode(git("cat-file", "blob", oid))
                scan(label, cache[oid])
            if revision:
                scan(revision + " [commit-message]", decode(git("show", "-s", "--format=%B", revision)))

        if args.staged:
            snapshot(None)
        elif args.tree:
            snapshot(args.tree)
        elif args.commit_range:
            # No first-parent restriction: inspect commits introduced through merges too.
            commits = git("rev-list", args.commit_range).decode().splitlines()
            for commit in commits:
                snapshot(commit)
        elif args.message_file:
            scan("[commit-message]", decode(Path(args.message_file).read_bytes()))
        else:
            root = Path(git("rev-parse", "--show-toplevel").decode().strip())
            for folder, dirs, files in os.walk(root, followlinks=False):
                dirs[:] = [d for d in dirs if d != ".git" and not (Path(folder) / d).is_symlink()]
                for name in files:
                    path = Path(folder) / name
                    if name == ".git":
                        continue
                    label = path.relative_to(root).as_posix()
                    scan(label + " [path]", label)
                    scan(label, os.readlink(path) if path.is_symlink() else decode(path.read_bytes()))
    except (ValueError, OSError, UnicodeError):
        # Never echo exceptions: config values, Git stderr or private paths may leak.
        print("ERROR guard setup/read failure; check rules, Git objects and file access", file=sys.stderr)
        return 2
    print(f"Guard: checked={checked} blocked={blocked} review={warnings}")
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
