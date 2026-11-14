"""A stale vault must never deploy missing or withdrawn stock articles."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HUGO = os.environ.get('HUGO_BIN') or shutil.which('hugo')

@unittest.skipUnless(HUGO, 'Set HUGO_BIN to test the real Hugo build')
class StockPublishGuardTest(unittest.TestCase):
    def test_stale_sync_fails_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            for name in ['content', 'layouts', 'data', 'static']:
                shutil.copytree(ROOT / name, site / name)
            shutil.copyfile(ROOT / 'hugo.toml', site / 'hugo.toml')
            def build():
                return subprocess.run([HUGO, '--source', str(site)], capture_output=True, text=True)
            result = build()
            self.assertEqual(result.returncode, 0, result.stderr)
            article = site / 'content/cn/stocks/002409.md'
            original = article.read_text()
            article.unlink()
            result = build()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Required stock article missing', result.stderr + result.stdout)
            article.write_text(original.replace('title: "雅克科技"', 'title: "蓝思科技"'))
            result = build()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Stock identity mismatch', result.stderr + result.stdout)
            article.write_text(original)
            (site / 'content/cn/stocks/300433.md').write_text('---\ntitle: 蓝思科技\ndate: 2026-07-01\n---\nWithdrawn article\n')
            result = build()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Withdrawn Lens Technology article', result.stderr + result.stdout)

if __name__ == '__main__':
    unittest.main()
