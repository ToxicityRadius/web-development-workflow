"""Offline package-integrity checks; Python standard library only."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/web-development-workflow'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def contained(path, root):
    resolved = path.resolve()
    require(resolved == root or root in resolved.parents, 'A package path escapes the repository')
    return resolved


def validate_package(root):
    # Explicit root permits isolated negative fixtures without touching the checkout.
    ROOT = root.resolve()
    SKILL = ROOT / 'skills/web-development-workflow'
    plugin = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
    marketplace = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
    require(plugin['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Unexpected manifest schema')
    require(plugin['name'] == 'web-development-workflow', 'Unexpected plugin identity')
    require(re.fullmatch(r'\d+\.\d+\.\d+', plugin['version']), 'Version must be a semantic release number')
    require(plugin['license'] == 'MIT AND Apache-2.0' and (ROOT / 'LICENSE').is_file(), 'Package license expression missing')
    require('com.openai' in plugin['extensions'], 'OpenAI presentation metadata missing')
    entry = marketplace['plugins'][0]
    require(entry['name'] == plugin['name'], 'Marketplace and plugin identity differ')
    require(entry['source']['source'] == 'local', 'Expected contained local catalog entry')
    require(entry['source']['path'].startswith('./'), 'Marketplace paths must start with ./')
    require(contained(ROOT / entry['source']['path'], ROOT) == ROOT, 'Marketplace points at another plugin')
    require(entry['policy']['installation'] == 'AVAILABLE', 'Unexpected installation policy')
    require(entry['policy']['authentication'] == 'ON_INSTALL', 'Unexpected catalog authentication policy')

    routes = json.loads((SKILL / 'references/skill-routing.json').read_text(encoding='utf-8'))
    require(routes['schema_version'] == 1, 'Unknown routing schema')
    names = [row['name'] for row in routes['skills']]
    require(len(names) == len(set(names)), 'Duplicate routing identities')
    bundled = {row['name'] for row in routes['skills'] if row['bundled']}
    require(bundled == {'workflow-interface-design', 'workflow-interface-review', 'workflow-mobile-web'}, 'Unexpected bundled core')
    for row in routes['skills']:
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', row['name']), 'Invalid routing name')
        require(row['directories'] and row['runtime'], 'Routing requirements missing')
        for directory in row['directories']:
            require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', directory), 'Unsafe skill directory alias')
        for resource in row['resources']:
            contained(ROOT / 'skills' / row['name'] / resource, ROOT / 'skills' / row['name'])
    expected_skills = bundled | {'web-development-workflow'}
    actual_skills = {path.parent.name for path in (ROOT / 'skills').glob('*/SKILL.md')}
    require(actual_skills == expected_skills, 'Missing or unexpected skill entrypoint')
    for name in sorted(expected_skills):
        directory = ROOT / 'skills' / name
        skill = (directory / 'SKILL.md').read_text(encoding='utf-8')
        require(skill.startswith(f'---\nname: {name}\n'), f'Skill identity/frontmatter missing: {name}')
        require(re.search(r'^description: .+', skill, re.M), f'Skill description missing: {name}')
        metadata = (directory / 'agents/openai.yaml').read_text(encoding='utf-8')
        require(f'Use ${name}' in metadata, f'Skill prompt identity missing: {name}')
        if name in bundled:
            require('allow_implicit_invocation: true' in metadata, 'Bundled adapters must remain available for task-based selection')
            require((directory / 'ADAPTER_LICENSE.txt').read_bytes() == (ROOT / 'LICENSE').read_bytes(), 'Adapter MIT license differs')
    for row in routes['skills']:
        if row['bundled']:
            for resource in row['resources']:
                require((ROOT / 'skills' / row['name'] / resource).exists(), f'Bundled resource missing: {resource}')

    lock = json.loads((ROOT / 'third-party.lock.json').read_text(encoding='utf-8'))
    require(lock['schema_version'] == 1, 'Unknown provenance schema')
    require({bundle['skill'] for bundle in lock['bundles']} == bundled and len(lock['bundles']) == 3, 'Bundled provenance differs')
    locked_paths = set()
    for bundle in lock['bundles']:
        require(re.fullmatch(r'[0-9a-f]{40}', bundle['commit']), 'Source must use an immutable commit')
        require(bundle['source_license'] == ('Apache-2.0' if bundle['skill'] == 'workflow-interface-design' else 'MIT'), 'Source license differs')
        require(bundle['adapter_license'] == 'MIT', 'Adapter license missing')
        expected_paths = {f"skills/{bundle['skill']}/references/upstream.md", f"skills/{bundle['skill']}/LICENSE.txt"}
        require({record['local_path'] for record in bundle['files']} == expected_paths and len(bundle['files']) == 2, 'Source/license provenance incomplete')
        for record in bundle['files']:
            path = contained(ROOT / record['local_path'], ROOT)
            require(path.is_file(), f"Missing licensed source: {record['local_path']}")
            require(hashlib.sha256(path.read_bytes()).hexdigest() == record['sha256'], f"Pinned source fingerprint mismatch: {record['local_path']}")
            expected_url = f"https://raw.githubusercontent.com/{bundle['repository']}/{bundle['commit']}/{record['upstream_path']}"
            require(record['url'] == expected_url, 'Source URL is not pinned to its recorded commit')
            locked_paths.add(record['local_path'])
    actual_sources = {path.relative_to(ROOT).as_posix() for name in bundled
                      for path in (ROOT / 'skills' / name).rglob('*')
                      if path.is_file() and (path.name == 'upstream.md' or path.name == 'LICENSE.txt')}
    require(locked_paths == actual_sources, 'Unrecorded upstream source')
    require((ROOT / 'THIRD_PARTY_NOTICES.md').is_file(), 'Third-party notices missing')
    expected_templates = ['PRD.md', 'TECHNICAL_REQUIREMENTS.md', 'APP_FLOW.md', 'DESIGN.md', 'BACKEND_SCHEMA.md', 'IMPLEMENTATION_PLAN.md']
    for name in expected_templates:
        require((SKILL / 'assets/templates' / name).is_file(), f'Missing template: {name}')

    source = json.loads((SKILL / 'references/guide-source.json').read_text(encoding='utf-8'))
    pdf = contained(SKILL / 'references' / source['pdf'], ROOT)
    require(pdf.read_bytes().startswith(b'%PDF-'), 'Invalid PDF header')
    require(hashlib.sha256(pdf.read_bytes()).hexdigest() == source['sha256'], 'PDF fingerprint mismatch')
    text = contained(SKILL / 'references' / source['searchable_text'], ROOT).read_text(encoding='utf-8')
    pages = re.findall(r'## PDF page (\d{2})\n\n\[View source page\]\(planning-guide.pdf#page=\d+\)\n\n```text\n(.*?)\n```', text, re.S)
    require(len(pages) == source['page_count'] == 16, 'Guide must contain all 16 pages')
    for index, (number, page) in enumerate(pages):
        require(int(number) == index + 1, 'Guide page order differs')
        require(hashlib.sha256(page.encode()).hexdigest() == source['page_text_sha256'][index], f'Page {number} text changed without an updated source record')

    tracked = [path for path in ROOT.rglob('*') if path.is_file() and not any(part in {'.git', '__pycache__', 'dist'} for part in path.relative_to(ROOT).parts)]
    pdfs = [path for path in tracked if path.suffix.lower() == '.pdf']
    require(pdfs == [pdf], 'Only the planning toolkit PDF belongs in this package')
    links = 0
    for file in tracked:
        if file.suffix.lower() not in {'.md', '.json', '.yaml', '.yml', '.py', '.txt'}:
            continue
        body = file.read_text(encoding='utf-8')
        require(not re.search(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{24,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)', body), f'Possible credential in {file.relative_to(ROOT)}')
        # Match an actual drive/home path without embedding a private user's name.
        require(not re.search(r'[A-Za-z]:[\\/]+[Uu]sers[\\/]+', body), f'Workstation path in {file.relative_to(ROOT)}')
        if file.suffix.lower() != '.md':
            continue
        for link in re.findall(r'\]\(([^)]+)\)', body):
            if re.match(r'^[a-z][a-z0-9+.-]*:', link, re.I):
                continue
            name, separator, fragment = link.partition('#')
            destination = contained(file.parent / name, ROOT) if name else file
            require(destination.exists(), f'Broken local link in {file.relative_to(ROOT)}: {link}')
            if separator and fragment.startswith('pdf-page-'):
                require(f'## PDF page {fragment.removeprefix("pdf-page-")}' in destination.read_text(encoding='utf-8'), 'Missing guide page anchor')
            links += 1
    return f'PASS: {len(tracked)} package files; {links} local links; 4 skills; 6 pinned source/license files; 16 page fingerprints; one planning PDF.'


def main():
    print(validate_package(ROOT))


if __name__ == '__main__':
    main()
