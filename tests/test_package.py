"""Negative integrity fixtures are isolated from the real package."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_validator', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageTests(unittest.TestCase):
    def fixture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name) / 'package'
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'dist'))
        return root

    def test_real_package(self):
        self.assertTrue(validator.validate_package(ROOT).startswith('PASS:'))

    def test_missing_upstream_license_fails(self):
        root = self.fixture()
        (root / 'skills/workflow-interface-review/LICENSE.txt').unlink()
        with self.assertRaisesRegex(ValueError, 'resource missing|Missing licensed source'):
            validator.validate_package(root)

    def test_changed_pinned_source_fails(self):
        root = self.fixture()
        source = root / 'skills/workflow-mobile-web/references/upstream.md'
        source.write_bytes(source.read_bytes() + b'\nUnreviewed change\n')
        with self.assertRaisesRegex(ValueError, 'fingerprint mismatch'):
            validator.validate_package(root)

    def test_unsafe_routing_alias_fails(self):
        root = self.fixture()
        path = root / 'skills/web-development-workflow/references/skill-routing.json'
        routes = json.loads(path.read_text(encoding='utf-8'))
        routes['skills'][0]['directories'] = ['../outside']
        path.write_text(json.dumps(routes), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Unsafe skill directory'):
            validator.validate_package(root)

    def test_broken_local_link_fails(self):
        root = self.fixture()
        with (root / 'README.md').open('a', encoding='utf-8') as file:
            file.write('\n[Missing resource](missing-resource.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken local link'):
            validator.validate_package(root)


if __name__ == '__main__':
    unittest.main()
