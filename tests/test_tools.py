import hashlib
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scanner = load('candidate_scanner', ROOT / 'skills/ui-deslop/scripts/scan_ui_candidates.py')
installer = load('skill_installer', ROOT / 'scripts/install.py')


class ScannerTests(unittest.TestCase):
    def test_candidates_and_source_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'ui.css'
            source.write_text('.cursor-glow { display:none; }\n.title { background-clip:text; }\n')
            before = hashlib.sha256(source.read_bytes()).hexdigest()
            result = scanner.scan(source)
            self.assertEqual({x['rule'] for x in result['candidates']}, {'decorative-effect-name', 'gradient-text'})
            self.assertIsNone(result['quality_verdict'])
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), before)

    def test_ordinary_style_is_not_a_quality_verdict(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'ui.css'
            source.write_text('body {font-family:Inter;color:purple;} .card {border-radius:24px;}')
            result = scanner.scan(source)
            self.assertEqual(result['candidates'], [])
            self.assertIsNone(result['quality_verdict'])

    def test_excluded_paths_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'src'
            root.mkdir()
            (root / 'node_modules').mkdir()
            (root / 'node_modules/bad.css').write_text('.cursor-glow {}')
            (root / '.env').write_text('KEY=synthetic-fixture')
            (root / 'real.css').write_text('.button { color:blue; }')
            outside = Path(tmp) / 'external.css'
            outside.write_text('.cursor-glow {}')
            (root / 'linked.css').symlink_to(outside)
            result = scanner.scan(root)
            self.assertEqual(result['files_scanned'], 1)
            self.assertEqual(result['candidates'], [])
            with self.assertRaises(ValueError):
                scanner.scan(root / 'linked.css')

    def test_limits_are_explicit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'a.css').write_text('.cursor-glow {}\n.x {transition:all 1s;}')
            (root / 'b.css').write_text('body {overflow-x:hidden;}')
            result = scanner.scan(root, limit=1, max_files=1)
            self.assertTrue(result['file_limit_reached'])
            self.assertTrue(result['finding_limit_reached'])
            self.assertEqual(len(result['candidates']), 1)

    def test_missing_source_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                scanner.scan(Path(tmp) / 'missing')


class InstallerTests(unittest.TestCase):
    def test_dry_run_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'new'
            planned = installer.install(installer.SKILLS, dest, dry_run=True)
            self.assertEqual(len(planned), 6)
            self.assertFalse(dest.exists())

    def test_selected_install_matches_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'skills'
            installer.install(['ui-deslop'], dest)
            self.assertEqual({p.name for p in dest.iterdir()}, {'ui-deslop'})
            for source in (installer.SOURCE / 'ui-deslop').rglob('*'):
                if source.is_file() and '__pycache__' not in source.parts and source.suffix != '.pyc':
                    self.assertEqual(source.read_bytes(), (dest / 'ui-deslop' / source.relative_to(installer.SOURCE / 'ui-deslop')).read_bytes())

    def test_conflict_preflight_preserves_all_existing_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            existing = dest / 'ui-deslop'
            existing.mkdir()
            marker = existing / 'mine.txt'
            marker.write_text('my existing skill')
            with self.assertRaises(FileExistsError):
                installer.install(['product-ui-direction', 'ui-deslop'], dest)
            self.assertFalse((dest / 'product-ui-direction').exists())
            self.assertEqual(marker.read_text(), 'my existing skill')

    def test_unknown_or_traversing_names_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ['unknown', '../outside', '/tmp/outside']:
                with self.assertRaises(ValueError):
                    installer.install([name], Path(tmp) / 'skills')

    def test_all_skills_install_and_repeat_refuses(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'skills'
            installed = installer.install(installer.SKILLS, dest)
            self.assertEqual(len(installed), 6)
            with self.assertRaises(FileExistsError):
                installer.install(installer.SKILLS, dest)


if __name__ == '__main__':
    unittest.main()
