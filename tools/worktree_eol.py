"""Inspect LF/CRLF noise; repair only when tracked content matches the index."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repair', action='store_true')
    args = parser.parse_args()
    if args.repair and git('diff', '--cached', '--name-only'):
        print('STOP: staged changes exist. Review them before repair.')
        return 1
    plans, differences = [], []
    for record in git('ls-files', '--eol', '-z').split(b'\0'):
        if not record:
            continue
        flags, raw_name = record.split(b'\t', 1)
        if b'i/lf' not in flags and b'i/crlf' not in flags:
            continue  # Do not rewrite binaries or unclassified files.
        name = raw_name.decode('utf-8')
        path = ROOT / name
        if not path.is_file() or path.is_symlink():
            differences.append(name)
            continue
        current = path.read_bytes()
        indexed = git('show', ':' + name)
        if normalized(current) != normalized(indexed):
            differences.append(name)
        else:
            plans.append((name, path, current, normalized(current)))
    real_diff = git('diff', '--name-only')
    if differences or real_diff:
        print('STOP: actual tracked changes exist; no repair performed.')
        for name in differences:
            print(name)
        return 1
    count = sum(before != after for _, _, before, after in plans)
    print(f'Tracked text files: {len(plans)}; CRLF files: {count}; actual differences: 0')
    if not args.repair:
        print('Use --repair to configure this clone and normalize its working files.')
        return 0
    for key, value in [('core.autocrlf', 'false'), ('core.eol', 'lf'),
                       ('core.checkstat', 'minimal'), ('core.trustctime', 'false'),
                       ('core.ignorestat', 'false')]:
        git('config', '--local', key, value)
    for name, path, before, after in plans:
        # Recheck immediately before writing so intervening edits are not overwritten.
        if path.read_bytes() != before:
            print(f'STOP: concurrent edit detected: {name}')
            return 1
        if before != after:
            path.write_bytes(after)
    names = [name for name, _, _, _ in plans]
    for start in range(0, len(names), 50):
        git('add', '--renormalize', '--', *names[start:start + 50])
    if git('diff', '--cached', '--name-only'):
        print('STOP: index normalization produced changes; review before committing.')
        return 1
    print('Repair complete. No content changes staged; untracked files untouched.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
