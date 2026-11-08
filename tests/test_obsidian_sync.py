"""Regression: an incomplete Obsidian vault must not delete published articles."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class ObsidianSyncTest(unittest.TestCase):
    def test_partial_vault_preserves_published_articles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site, vault = root / 'site', root / 'vault'
            (site / 'scripts').mkdir(parents=True)
            script = site / 'scripts/sync-from-obsidian.sh'
            shutil.copyfile(Path(__file__).resolve().parents[1] / 'scripts/sync-from-obsidian.sh', script)
            for lang in ('cn', 'en'):
                target, source = site / 'content' / lang / 'stocks', vault / lang / 'stocks'
                target.mkdir(parents=True)
                source.mkdir(parents=True)
                (target / '002409.md').write_text('published Yoke research')
                (target / '06656.md').write_text('published Sigenergy research')
                (target / 'Yili.md').write_text('published Yili research')
                (target / 'existing.md').write_text('old')
                (source / 'existing.md').write_text('updated source article')
                (source / '300433.md').write_text('independent Lens article')
                (source / '.DS_Store').write_text('excluded')
            subprocess.run(['bash', str(script)], env={**os.environ, 'OBSIDIAN_PUBLISH_DIR': str(vault)}, check=True)
            for lang in ('cn', 'en'):
                target = site / 'content' / lang / 'stocks'
                for name, title in [('002409', 'Yoke'), ('06656', 'Sigenergy'), ('Yili', 'Yili')]:
                    self.assertEqual((target / (name + '.md')).read_text(), f'published {title} research')
                self.assertEqual((target / 'existing.md').read_text(), 'updated source article')
                self.assertEqual((target / '300433.md').read_text(), 'independent Lens article')
                self.assertFalse((target / '.DS_Store').exists())


if __name__ == '__main__':
    unittest.main()
