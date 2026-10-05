import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('worktree_eol', Path(__file__).resolve().parents[1] / 'tools/worktree_eol.py')
eol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eol)


class WorktreeEolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.previous_root = eol.ROOT
        eol.ROOT = self.root
        self.addCleanup(setattr, eol, 'ROOT', self.previous_root)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'core.autocrlf', 'false')
        (self.root / '.gitattributes').write_bytes(b'*.md text eol=lf\n')
        (self.root / 'note.md').write_bytes(b'# Public note\nOriginal text\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'Public fixture')

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL)

    def run_repair(self):
        import sys
        from unittest.mock import patch
        with patch.object(sys, 'argv', ['worktree_eol.py', '--repair']):
            return eol.main()

    def test_lf_rewrite_remains_clean_after_repair(self):
        self.assertEqual(self.run_repair(), 0)
        note = self.root / 'note.md'
        note.write_bytes(note.read_bytes())  # Simulate an editor saving the same LF text.
        self.assertEqual(self.git('status', '--porcelain'), b'')
        self.assertEqual(self.git('config', '--local', 'core.autocrlf').strip(), b'false')

    def test_real_edit_is_preserved_and_blocks_repair(self):
        note = self.root / 'note.md'
        changed = b'# Public note\nActual research edit\n'
        note.write_bytes(changed)
        self.assertEqual(self.run_repair(), 1)
        self.assertEqual(note.read_bytes(), changed)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), b'')

    def test_staged_change_blocks_repair(self):
        (self.root / 'note.md').write_bytes(b'Changed text\n')
        self.git('add', 'note.md')
        before = self.git('diff', '--cached')
        self.assertEqual(self.run_repair(), 1)
        self.assertEqual(before, self.git('diff', '--cached'))


if __name__ == '__main__':
    unittest.main()
