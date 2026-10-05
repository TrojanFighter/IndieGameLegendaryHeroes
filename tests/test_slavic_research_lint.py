import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('slavic_research_lint', Path(__file__).resolve().parents[1] / 'tools/slavic_research_lint.py')
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)


class SisterProgramTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.program = self.root / 'sister-projects/slavic'
        (self.program / 'evidence').mkdir(parents=True)
        (self.program / 'metadata').mkdir()
        (self.root / 'evidence').mkdir()
        (self.program / 'evidence/SLAVIC-001-topic.md').write_text('# SLAVIC-001 Topic\n', encoding='utf-8')
        self.registry = dict(version=1, program_id='SLAVIC', case_count=0, claim_count=0, profile_count=0,
                             topics=[dict(topic_id='SLAVIC-001', file='evidence/SLAVIC-001-topic.md')], variants=[])
        self.save()

    def save(self):
        (self.program / 'metadata/research-index.json').write_text(json.dumps(self.registry), encoding='utf-8')

    def test_clean_program_passes(self):
        self.assertEqual(lint.validate(self.root), [])

    def test_mixed_evidence_and_broken_link_fail(self):
        (self.root / 'evidence/SLAVIC-002-misplaced.md').write_text('Misplaced', encoding='utf-8')
        (self.program / 'README.md').write_text('[missing](missing.md)', encoding='utf-8')
        errors = lint.validate(self.root)
        self.assertTrue(any('mixed' in error for error in errors))
        self.assertTrue(any('broken local link' in error for error in errors))

    def test_variants_do_not_count_as_new_topics(self):
        (self.program / 'evidence/SLAVIC-001-variant.md').write_text('# SLAVIC-001 Variant\n', encoding='utf-8')
        self.registry['variants'].append(dict(topic_id='SLAVIC-001', file='evidence/SLAVIC-001-variant.md'))
        self.save()
        self.assertEqual(lint.validate(self.root), [])
        self.registry['topics'].append(self.registry['topics'][0])
        self.save()
        self.assertTrue(any('duplicate primary' in error for error in lint.validate(self.root)))

    def test_missing_or_unregistered_file_fails(self):
        (self.program / 'evidence/SLAVIC-002-extra.md').write_text('# SLAVIC-002 Extra\n', encoding='utf-8')
        self.assertTrue(lint.validate(self.root))

    def test_path_escape_fails(self):
        self.registry['topics'][0]['file'] = '../../outside.md'
        self.save()
        self.assertTrue(any('escapes' in error for error in lint.validate(self.root)))


if __name__ == '__main__':
    unittest.main()
