"""Exercise discovery failures without installing or executing a specialist."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('availability', ROOT / 'skills/web-development-workflow/scripts/check_skills.py')
availability = importlib.util.module_from_spec(spec)
spec.loader.exec_module(availability)


class AvailabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.candidate = {'name': 'example-skill', 'directories': ['alias', 'example-skill'],
                          'bundled': False, 'resources': ['references/rule.md'],
                          'runtime': 'A successful browser operation is separate'}

    def create(self, directory='alias', name='example-skill', resource=True):
        location = self.root / directory
        location.mkdir(parents=True)
        (location / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Fixture\n---\n', encoding='utf-8')
        if resource:
            (location / 'references').mkdir()
            (location / 'references/rule.md').write_text('Fixture', encoding='utf-8')
        return location

    def inspect(self, roots=None):
        return availability.inventory(roots or [self.root], [self.candidate])['skills'][0]

    def test_missing_stays_missing_and_creates_nothing(self):
        row = self.inspect()
        self.assertEqual(row['disk_status'], 'missing')
        self.assertEqual(list(self.root.iterdir()), [])
        self.assertEqual(row['session_visibility'], 'unknown')
        self.assertEqual(row['runtime_status'], 'not_tested')

    def test_alias_and_duplicate_roots_are_resolved(self):
        self.create()
        row = self.inspect([self.root, self.root / '.'])
        self.assertEqual(row['disk_status'], 'present')
        self.assertEqual(len(row['copies']), 1)
        self.assertFalse(row['duplicate_copies'])
        self.assertEqual(row['runtime_status'], 'not_tested')

    def test_multiple_real_copies_are_reported(self):
        self.create()
        self.create(directory='example-skill')
        self.assertTrue(self.inspect()['duplicate_copies'])

    def test_missing_reference_is_incomplete(self):
        self.create(resource=False)
        row = self.inspect()
        self.assertEqual(row['disk_status'], 'incomplete')
        self.assertEqual(row['copies'][0]['missing_resources'], ['references/rule.md'])

    def test_wrong_frontmatter_name_is_invalid(self):
        self.create(name='different-skill')
        self.assertEqual(self.inspect()['disk_status'], 'invalid')

    def test_unreadable_entrypoint_is_reported(self):
        self.create()
        with patch.object(Path, 'read_text', side_effect=PermissionError('fixture')):
            self.assertEqual(self.inspect()['disk_status'], 'unreadable')

    def test_utf8_bom_and_crlf_are_supported(self):
        location = self.create()
        (location / 'SKILL.md').write_bytes(b'\xef\xbb\xbf---\r\nname: "example-skill"\r\ndescription: Fixture\r\n---\r\n')
        self.assertEqual(self.inspect()['disk_status'], 'present')


if __name__ == '__main__':
    unittest.main()
