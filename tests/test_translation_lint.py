import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('translation_lint', Path(__file__).resolve().parents[1] / 'tools/translation_lint.py')
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)


class TranslationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'translations/en').mkdir(parents=True)
        self.source = self.root / 'source.md'
        self.target = self.root / 'translations/en/case.md'
        self.source.write_text('# CASE-001\n## Research\nC001 UNKNOWN H SUPPORTED RESEARCHING USD 10,000\n', encoding='utf-8')
        self.target.write_text('# CASE-001\n[source](../../source.md) [registry](../manifest.json)\n## Research\nC001 UNKNOWN H SUPPORTED RESEARCHING USD 10,000\n', encoding='utf-8')
        self.entry = dict(source='source.md', target='translations/en/case.md', doc_id='CASE-001', kind='case-translation', source_sha256=lint.digest(self.source), status='DRAFT', reviewer=None)
        self.save()

    def save(self):
        (self.root / 'translations/manifest.json').write_text(json.dumps(dict(version=1, canonical_language='zh', translations=[self.entry])), encoding='utf-8')

    def test_current_draft_passes(self):
        self.assertEqual(lint.validate(self.root), ([], []))

    def test_windows_newlines_do_not_cause_drift(self):
        previous = lint.digest(self.source)
        self.source.write_bytes(self.source.read_text(encoding='utf-8').replace('\n', '\r\n').encode('utf-8'))
        self.assertEqual(previous, lint.digest(self.source))

    def test_changed_source_requires_stale(self):
        self.source.write_text(self.source.read_text() + '\nNew evidence', encoding='utf-8')
        self.assertTrue(lint.validate(self.root)[0])
        self.entry['status'] = 'STALE'
        self.save()
        errors, warnings = lint.validate(self.root)
        self.assertFalse(errors)
        self.assertTrue(warnings)

    def test_changed_reviewed_translation_invalidates_review(self):
        self.entry.update(status='REVIEWED', reviewer='Human reviewer', reviewed_target_sha256=lint.digest(self.target))
        self.save()
        self.assertFalse(lint.validate(self.root)[0])
        self.target.write_text(self.target.read_text() + '\nChanged prose', encoding='utf-8')
        self.assertTrue(lint.validate(self.root)[0])

    def test_missing_id_number_and_link_fail(self):
        self.target.write_text('# CASE-001\n[source](../../source.md) [registry](../manifest.json) [broken](missing.md)\n## Research\nUNKNOWN H SUPPORTED RESEARCHING', encoding='utf-8')
        errors, _ = lint.validate(self.root)
        self.assertTrue(any('IDs differ' in error for error in errors))
        self.assertTrue(any('numeric' in error for error in errors))
        self.assertTrue(any('broken local link' in error for error in errors))

    def test_unregistered_translation_fails(self):
        (self.root / 'translations/en/unregistered.md').write_text('Draft', encoding='utf-8')
        self.assertTrue(lint.validate(self.root)[0])

    def test_escaping_source_fails(self):
        self.entry['source'] = '../private.md'
        self.save()
        self.assertTrue(lint.validate(self.root)[0])


if __name__ == '__main__':
    unittest.main()
