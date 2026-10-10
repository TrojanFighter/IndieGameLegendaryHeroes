"""Focused regression tests for the reporting-only reader/evidence audit."""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reader_evidence_sync_audit", ROOT / "tools" / "reader_evidence_sync_audit.py"
)
audit = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(audit)


class RecordLevelAuditTests(unittest.TestCase):
    def test_numbered_records_not_top_level_notes(self):
        body = (
            "# Ledger\n## Introduction\nIgnore this.\n"
            "## E001 — Alpha income\n- Source class: P0 — interview\n"
            "Something specific.\n"
            "## E002 — Steam income\n- Source class: S1 — analysis\n"
            "A different revenue phase.\n"
            "## Next work\nNot an Evidence record.\n"
        )
        sections = audit.evidence_records(body)
        self.assertEqual([n for n, _ in sections], ["E001", "E002"])
        self.assertIn("Alpha income", body)
        self.assertIn("Something specific.", sections[0][1])
        self.assertIn("A different revenue phase.", sections[1][1])

    def test_one_quoted_record_does_not_cover_other_records(self):
        quoted = (
            '## E001 — First\n- Source class: P1\n'
            + '“' + '这是一段足够长的受访者原话，需要逐字核对原始采访来源。' + '”'
            + '\n## E002 — Second\n- Source class: P0\nJust a paraphrase.\n'
        )
        sections = audit.evidence_records(quoted)
        self.assertTrue(audit.LONG_QUOTE_RE.search(sections[0][1]))
        self.assertFalse(audit.LONG_QUOTE_RE.search(sections[1][1]))
        self.assertTrue(audit.is_primary_record(sections[0][1]))
        self.assertTrue(audit.is_primary_record(sections[1][1]))

    def test_source_class_not_inferred_from_other_body_text(self):
        self.assertFalse(audit.is_primary_record("- Source class: S2\nMentions P0 sources."))
        self.assertFalse(audit.is_primary_record("- Claim use: compare P0 and P1"))
        self.assertTrue(audit.is_primary_record("- Class: P0/P1 — mixed contemporaneous and retrospective"))


if __name__ == "__main__":
    unittest.main()
