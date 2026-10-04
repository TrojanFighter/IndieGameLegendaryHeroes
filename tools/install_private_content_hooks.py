#!/usr/bin/env python3
"""Install local-only guards; never replace an existing hook."""
import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path

from private_content_guard import rules_from


def install():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules", required=True)
    args = parser.parse_args()
    rules_from(args.rules)
    existing = subprocess.run(["git", "config", "--get", "core.hooksPath"], capture_output=True)
    if existing.returncode == 0:
        raise ValueError("Existing core.hooksPath; integrate guards manually")
    raw = subprocess.check_output(["git", "rev-parse", "--git-path", "hooks"]).decode().strip()
    hooks = Path(raw).resolve()
    scanner = Path(__file__).with_name("private_content_guard.py").resolve()
    command = " ".join(shlex.quote(p) for p in [Path(sys.executable).as_posix(), scanner.as_posix(), "--rules", Path(args.rules).resolve().as_posix()])
    contents = {
        "pre-commit": f'#!/bin/sh\nexec {command} --staged\n',
        "commit-msg": f'#!/bin/sh\nexec {command} --message-file "$1"\n',
        "pre-push": '#!/bin/sh\nset -eu\nwhile read local_ref local_oid remote_ref remote_oid; do\n'
        '  case "$local_oid" in *[!0]*) ;; *) continue ;; esac\n'
        '  case "$remote_oid" in *[!0]*) scan_range="$remote_oid..$local_oid" ;; *) scan_range="$local_oid" ;; esac\n'
        f'  {command} --range "$scan_range"\ndone\n',
    }
    if any((hooks / name).exists() for name in contents):
        raise ValueError("Existing hook; integrate manually without overwriting")
    hooks.mkdir(parents=True, exist_ok=True)
    for name, content in contents.items():
        path = hooks / name
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        if os.name != "nt":
            path.chmod(0o755)
    print("Installed pre-commit, commit-msg and pre-push guards locally")


if __name__ == "__main__":
    try:
        install()
    except (ValueError, OSError, UnicodeError, subprocess.SubprocessError):
        print("Hook installation failed; existing configuration was not replaced", file=sys.stderr)
        raise SystemExit(2)
