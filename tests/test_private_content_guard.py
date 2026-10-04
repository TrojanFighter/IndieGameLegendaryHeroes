"""Behavior tests use only fictional identifiers and isolated temporary repos."""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCANNER = Path(__file__).resolve().parents[1] / "tools/private_content_guard.py"
spec = importlib.util.spec_from_file_location("guard", SCANNER)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        self.repo.mkdir()
        self.rules = self.base / "rules.json"
        self.rules.write_text(json.dumps({"deny": ["CONFIDENTIAL_TEST_PROJECT", "虚构私有代号"], "review": ["TEST_CONTEXT_TERM"]}), encoding="utf-8")
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "commit.gpgsign", "false")

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.repo, stderr=subprocess.DEVNULL).decode().strip()

    def run_guard(self, *args, rules=None):
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        env.pop("PRIVATE_CONTENT_RULES", None)
        command = [sys.executable, str(SCANNER)]
        if rules is not False:
            command += ["--rules", str(rules or self.rules)]
        return subprocess.run(command + list(args), cwd=self.repo, env=env, capture_output=True, text=True, encoding="utf-8")

    def commit(self, text, message="test"):
        (self.repo / "research.txt").write_text(text, encoding="utf-8")
        self.git("add", "research.txt")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def test_industry_terms_remain_public(self):
        self.commit("Devolver 11 bit Steam publisher vertical slice runway PRODUCT_LED_SCALING")
        result = self.run_guard("--tree", "HEAD")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_added_then_removed_commit_still_blocked(self):
        base = self.commit("public")
        bad = self.commit("confidential_test_project")
        self.commit("public")
        self.assertEqual(self.run_guard("--tree", "HEAD").returncode, 0)
        result = self.run_guard("--range", base + "..HEAD")
        self.assertEqual(result.returncode, 1)
        self.assertIn(bad, result.stdout)
        self.assertNotIn("confidential_test_project", result.stdout.lower())

    def test_index_not_worktree_and_message(self):
        self.commit("public")
        path = self.repo / "research.txt"
        path.write_text("CONFIDENTIAL_TEST_PROJECT", encoding="utf-8")
        self.git("add", "research.txt")
        path.write_text("public", encoding="utf-8")
        self.assertEqual(self.run_guard("--staged").returncode, 1)
        self.assertEqual(self.run_guard("--worktree").returncode, 0)
        message = self.base / "message.txt"
        message.write_text("CONFIDENTIAL_TEST_PROJECT", encoding="utf-8")
        self.assertEqual(self.run_guard("--message-file", str(message)).returncode, 1)

    def test_filename_and_unicode_redacted(self):
        path = self.repo / "CONFIDENTIAL_TEST_PROJECT.txt"
        path.write_text("虚构私有代号", encoding="utf-16")
        self.git("add", ".")
        result = self.run_guard("--staged")
        self.assertEqual(result.returncode, 1)
        self.assertIn("[redacted]", result.stdout)
        self.assertNotIn("CONFIDENTIAL_TEST_PROJECT", result.stdout)
        self.assertNotIn("虚构私有代号", result.stdout)

    def test_missing_invalid_or_in_repo_config_fails_closed(self):
        self.assertEqual(self.run_guard("--worktree", rules=False).returncode, 2)
        self.rules.write_text('{"deny": []}', encoding="utf-8")
        self.assertEqual(self.run_guard("--worktree").returncode, 2)
        inside = self.repo / "private-rules.json"
        inside.write_text('{"deny": ["CONFIDENTIAL_TEST_PROJECT"]}', encoding="utf-8")
        result = self.run_guard("--worktree", rules=inside)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("CONFIDENTIAL_TEST_PROJECT", result.stderr)

    def test_review_is_not_automatic_leak(self):
        self.commit("TEST_CONTEXT_TERM")
        result = self.run_guard("--tree", "HEAD")
        self.assertEqual(result.returncode, 0)
        self.assertIn("REVIEW", result.stdout)
        self.assertNotIn("TEST_CONTEXT_TERM", result.stdout)

    def test_merge_introduced_commits_are_scanned(self):
        base = self.commit("public")
        branch = self.git("branch", "--show-current")
        self.git("checkout", "-qb", "side")
        bad = self.commit("CONFIDENTIAL_TEST_PROJECT")
        self.commit("public")
        self.git("checkout", "-q", branch)
        self.git("merge", "--no-ff", "-qm", "merge", "side")
        result = self.run_guard("--range", base + "..HEAD")
        self.assertEqual(result.returncode, 1)
        self.assertIn(bad, result.stdout)


if __name__ == "__main__":
    unittest.main()
