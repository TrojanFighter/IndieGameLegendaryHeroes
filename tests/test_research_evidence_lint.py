from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import research_evidence_lint as lint


FULL_CITATION = """- Source class: P0 - official statement
- Title: Development announcement
- Institution: Example developer
- Published: 2024-06-07
- Accessed: 2026-10-05
- URL: https://example.org/announcement/42
"""


class SourceLocatorTests(unittest.TestCase):
    def setUp(self):
        lint.errors.clear()
        lint.warnings.clear()
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        root_patch = patch.object(lint, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)

    def ledger(self, content, *, v2=True):
        (self.root / "ledger.md").write_text(content, encoding="utf-8")
        return lint.parse_ledger("CASE-999", "ledger.md", require_locators=v2)

    def test_high_grade_without_locators_fails(self):
        self.ledger("## E001\n- Source class: P1\n- Confidence: HIGH\n")
        self.assertEqual(len(lint.errors), 5)

    def test_complete_citation_passes(self):
        self.ledger("## E001\n" + FULL_CITATION)
        self.assertEqual(lint.errors, [])

    def test_each_entry_needs_its_own_locator(self):
        self.ledger("## E001\n" + FULL_CITATION + "\n## E002\n- Source class: S1\n")
        self.assertTrue(lint.errors)
        self.assertTrue(all("E002" in message for message in lint.errors))

    def test_dynamic_page_explicit_unknown_date_passes(self):
        self.assertEqual(lint.source_locator_errors(FULL_CITATION.replace("2024-06-07", "UNKNOWN (dynamic page)")), [])
        self.assertTrue(lint.source_locator_errors(FULL_CITATION.replace("2024-06-07", "")))

    def test_intake_lead_cannot_qualify_as_supported_claim(self):
        registry = self.ledger("## E001\n- Source class: H - unverified lead\n")
        self.assertEqual(lint.errors, [])
        lint.validate_claim_evidence(
            {"C999": {"status": "SUPPORTED", "related_cases": ["CASE-999"], "evidence_ids": ["CASE-999:E001"]}},
            {"CASE-999:E001": registry["E001"]},
        )
        self.assertTrue(any("P0/P1/S1" in message for message in lint.errors))

    def test_legacy_ledger_remains_compatible(self):
        self.ledger("## E001\n- Source class: P0\n", v2=False)
        self.assertEqual(lint.errors, [])


if __name__ == "__main__":
    unittest.main()
