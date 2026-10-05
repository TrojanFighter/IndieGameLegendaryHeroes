"""Validate translation identity, source versions and local links; no auto-review."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    content = path.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def inside(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("path escapes repository")
    return path


def validate(root):
    errors, warnings = [], []
    try:
        registry = json.loads((root / 'translations/manifest.json').read_text(encoding='utf-8'))
        if registry['version'] != 1 or registry['canonical_language'] != 'zh':
            raise ValueError('unsupported registry version or canonical language')
        entries = registry['translations']
        if not isinstance(entries, list) or not entries:
            raise ValueError('empty translation registry')
    except (ValueError, KeyError, OSError) as exc:
        return [f'Invalid translation registry: {exc}'], []
    targets = set()
    for entry in entries:
        try:
            source = inside(root, entry['source'])
            target = inside(root, entry['target'])
            name = entry['target']
            if not target.is_relative_to((root / 'translations/en').resolve()):
                raise ValueError('English target must be under translations/en')
            if name in targets:
                raise ValueError('duplicate target')
            targets.add(name)
            if entry['kind'] not in {'entry', 'translation', 'case-translation'}:
                raise ValueError('unknown translation kind')
            status = entry['status']
            if status not in {'DRAFT', 'REVIEWED', 'STALE'}:
                raise ValueError('unknown status')
            if not re.fullmatch(r'[0-9a-f]{64}', entry['source_sha256']):
                raise ValueError('invalid source hash')
            original = source.read_text(encoding='utf-8-sig')
            english = target.read_text(encoding='utf-8-sig')
            if digest(source) != entry['source_sha256']:
                if status == 'STALE':
                    warnings.append(f'{name}: STALE; compare the Chinese source before use')
                else:
                    errors.append(f'{name}: source changed; update translation or declare STALE')
            elif status == 'STALE':
                warnings.append(f'{name}: explicitly STALE; review before changing status')
            if status == 'REVIEWED':
                if not isinstance(entry.get('reviewer'), str) or not entry['reviewer'].strip():
                    raise ValueError('REVIEWED requires an identified human reviewer')
                if entry.get('reviewed_target_sha256') != digest(target):
                    raise ValueError('reviewed translation changed; re-review or return to DRAFT')
            links = re.findall(r'\]\(([^)]+)\)', english)
            resolved_links = {
                (target.parent / link.split('#')[0]).resolve()
                for link in links if not re.match(r'[a-z]+:', link)
            }
            if source not in resolved_links or (root / 'translations/manifest.json').resolve() not in resolved_links:
                raise ValueError('missing source or registry link')
            for link in re.findall(r'\]\(([^)]+)\)', english):
                if re.match(r'[a-z]+:', link) or link.startswith('#'):
                    continue
                linked = (target.parent / link.split('#')[0]).resolve()
                if not linked.is_relative_to(root.resolve()) or not linked.exists():
                    errors.append(f'{name}: broken local link {link}')
            if entry['kind'] == 'case-translation' and status != 'STALE':
                identity = entry['doc_id']
                if not re.fullmatch(r'CASE-\d{3}', identity):
                    raise ValueError('invalid Case ID')
                ids = lambda text: set(re.findall(r'\b(?:CASE-\d{3}|C\d{3})\b', text))
                if ids(original) != ids(english):
                    errors.append(f'{name}: Case / Claim IDs differ')
                levels = lambda text: [len(m) for m in re.findall(r'^(#{2,6}) ', text, re.M)]
                if levels(original) != levels(english):
                    errors.append(f'{name}: research section hierarchy differs')
                for marker in ['UNKNOWN', 'SUPPORTED', 'RESEARCHING', 'H']:
                    if re.search(r'\b' + marker + r'\b', original) and not re.search(r'\b' + marker + r'\b', english):
                        errors.append(f'{name}: missing uncertainty marker {marker}')
                numbers = lambda text: set(re.findall(r'(?<![\w])\d+(?:[,–.-]\d+)*(?![\w])', text))
                missing = numbers(original) - numbers(english)
                if missing:
                    errors.append(f'{name}: source numeric tokens absent: {sorted(missing)}')
        except (KeyError, TypeError, ValueError, OSError) as exc:
            errors.append(f'Translation entry error: {exc}')
    discovered = {p.relative_to(root).as_posix() for p in (root / 'translations/en').rglob('*.md')}
    for name in sorted(discovered - targets):
        errors.append(f'{name}: unregistered English document')
    return errors, warnings


def main():
    errors, warnings = validate(ROOT)
    for warning in warnings:
        print(f'WARNING: {warning}')
    for error in errors:
        print(f'ERROR: {error}')
    print(f'Translation checks: {len(errors)} errors, {len(warnings)} warnings. Semantic and human review remain required.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
