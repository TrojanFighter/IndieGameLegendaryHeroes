"""Check sister-program boundaries, topic registration and local links."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(root):
    program = root / 'sister-projects/slavic'
    errors = []
    try:
        registry = json.loads((program / 'metadata/research-index.json').read_text(encoding='utf-8'))
        if registry['version'] != 1 or registry['program_id'] != 'SLAVIC':
            raise ValueError('unsupported program registry')
        topics, variants = registry['topics'], registry['variants']
        identifiers, paths = set(), set()
        for entry in topics:
            identity = entry['topic_id']
            if not re.fullmatch(r'SLAVIC-\d{3}', identity) or identity in identifiers:
                errors.append(f'invalid or duplicate primary topic: {identity}')
            identifiers.add(identity)
        for entry in variants:
            if entry['topic_id'] not in identifiers:
                errors.append(f'variant lacks a primary topic: {entry["topic_id"]}')
        for entry in topics + variants:
            name, identity = entry['file'], entry['topic_id']
            path = (program / name).resolve()
            if not path.is_relative_to((program / 'evidence').resolve()):
                errors.append(f'ledger escapes program evidence directory: {name}')
                continue
            if name in paths:
                errors.append(f'duplicate file registration: {name}')
            paths.add(name)
            if not path.exists():
                errors.append(f'missing ledger: {name}')
                continue
            if not path.name.startswith(identity + '-') or not path.read_text(encoding='utf-8').startswith('# ' + identity + ' '):
                errors.append(f'topic identity differs from file or title: {name}')
        discovered = {p.relative_to(program).as_posix() for p in (program / 'evidence').glob('SLAVIC-*.md')}
        if discovered != paths:
            errors.append(f'ledger inventory differs: {sorted(discovered ^ paths)}')
        for field, folder, pattern in [('case_count', 'cases', 'CASE-*.md'),
                                       ('claim_count', 'claims', 'C[0-9]*.md'),
                                       ('profile_count', 'book/profiles', '*.md')]:
            if registry[field] != len(list((program / folder).glob(pattern))):
                errors.append(f'{field}: recorded count differs from files')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'invalid program registry: {exc}')
    for path in (root / 'evidence').glob('SLAVIC*.md'):
        errors.append(f'Slavic research still mixed into independent evidence: {path.name}')
    for path in program.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        links = re.findall(r'\]\(([^)]+)\)', text)
        for link in links:
            if re.match(r'[a-z]+:', link) or link.startswith('#'):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'{path.relative_to(root)}: broken local link {link}')
    return errors


def main():
    errors = validate(ROOT)
    for error in errors:
        print('ERROR:', error)
    if errors:
        return 1
    registry = json.loads((ROOT / 'sister-projects/slavic/metadata/research-index.json').read_text(encoding='utf-8'))
    print(f'Slavic research: {len(registry["topics"])} topics, {len(registry["variants"])} retained variants; '
          f'Cases={registry["case_count"]}, Claims={registry["claim_count"]}, Profiles={registry["profile_count"]}. Links and boundaries: OK.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
