"""Read known skill files only. Disk presence never establishes session/runtime readiness."""
import argparse
import json
from pathlib import Path
import re

SKILL = Path(__file__).resolve().parents[1]


def default_roots():
    return [SKILL.parent, Path.home() / '.agents/skills', Path.home() / '.codex/skills']


def inventory(roots, candidates):
    roots = list(dict.fromkeys(Path(root).expanduser().resolve() for root in roots))
    rows = []
    for candidate in candidates:
        copies = []
        seen = set()
        for root in roots:
            for directory in candidate['directories']:
                location = (root / directory).resolve()
                if location in seen:
                    continue
                seen.add(location)
                entrypoint = location / 'SKILL.md'
                try:
                    if not entrypoint.is_file():
                        continue
                    body = entrypoint.read_text(encoding='utf-8-sig')
                    header = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', body, re.S)
                    match = re.search(r'^name:\s*[\"\']?([a-z0-9-]+)[\"\']?\s*$', header[1], re.M) if header else None
                    valid = match is not None and match[1] == candidate['name']
                    missing = [name for name in candidate['resources'] if not (location / name).exists()]
                    status = 'invalid' if not valid else 'incomplete' if missing else 'present'
                    copies.append({'path': str(location), 'disk_status': status, 'missing_resources': missing})
                except (OSError, UnicodeError) as error:
                    copies.append({'path': str(location), 'disk_status': 'unreadable', 'error': type(error).__name__})
        status = ('present' if any(copy['disk_status'] == 'present' for copy in copies)
                  else copies[0]['disk_status'] if copies else 'missing')
        rows.append({'name': candidate['name'], 'bundled': candidate['bundled'],
                     'disk_status': status, 'copies': copies, 'duplicate_copies': len(copies) > 1,
                     'session_visibility': 'unknown', 'runtime_status': 'not_tested',
                     'runtime_requirement': candidate['runtime']})
    return {'schema_version': 1, 'roots': [str(root) for root in roots],
            'scope': 'Known files only; no activation, installation, network or runtime checks',
            'skills': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill-root', action='append', type=Path,
                        help='Inspect only this root (repeat for multiple roots)')
    parser.add_argument('--json', action='store_true', help='Print a machine-readable report')
    args = parser.parse_args()
    candidates = json.loads((SKILL / 'references/skill-routing.json').read_text(encoding='utf-8'))['skills']
    report = inventory(args.skill_root if args.skill_root is not None else default_roots(), candidates)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(report['scope'])
        for row in report['skills']:
            duplicate = ' (multiple copies; select explicitly)' if row['duplicate_copies'] else ''
            print(f"{row['name']}: {row['disk_status']}{duplicate}")
        print('Confirm the current session catalogue and execute relevant tools separately.')


if __name__ == '__main__':
    main()
