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


def contained(path):
    resolved = path.resolve()
    require(resolved == ROOT or ROOT in resolved.parents, 'A package path escapes the repository')
    return resolved


def main():
    plugin = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
    marketplace = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
    require(plugin['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Unexpected manifest schema')
    require(plugin['name'] == 'web-development-workflow', 'Unexpected plugin identity')
    require(re.fullmatch(r'\d+\.\d+\.\d+', plugin['version']), 'Version must be a semantic release number')
    require(plugin['license'] == 'MIT' and (ROOT / 'LICENSE').is_file(), 'MIT license missing')
    require('com.openai' in plugin['extensions'], 'OpenAI presentation metadata missing')
    entry = marketplace['plugins'][0]
    require(entry['name'] == plugin['name'], 'Marketplace and plugin identity differ')
    require(entry['source']['source'] == 'local', 'Expected contained local catalog entry')
    require(entry['source']['path'].startswith('./'), 'Marketplace paths must start with ./')
    require(contained(ROOT / entry['source']['path']) == ROOT, 'Marketplace points at another plugin')
    require(entry['policy']['installation'] == 'AVAILABLE', 'Unexpected installation policy')
    require(entry['policy']['authentication'] == 'ON_INSTALL', 'Unexpected catalog authentication policy')

    skill = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    require(skill.startswith('---\nname: web-development-workflow\n'), 'Skill identity/frontmatter missing')
    require(re.search(r'^description: .+', skill, re.M), 'Skill description missing')
    require((SKILL / 'agents/openai.yaml').is_file(), 'Skill interface metadata missing')
    expected_templates = ['PRD.md', 'TECHNICAL_REQUIREMENTS.md', 'APP_FLOW.md', 'DESIGN.md', 'BACKEND_SCHEMA.md', 'IMPLEMENTATION_PLAN.md']
    for name in expected_templates:
        require((SKILL / 'assets/templates' / name).is_file(), f'Missing template: {name}')

    source = json.loads((SKILL / 'references/guide-source.json').read_text(encoding='utf-8'))
    pdf = SKILL / 'references' / source['pdf']
    require(pdf.read_bytes().startswith(b'%PDF-'), 'Invalid PDF header')
    require(hashlib.sha256(pdf.read_bytes()).hexdigest() == source['sha256'], 'PDF fingerprint mismatch')
    text = (SKILL / 'references' / source['searchable_text']).read_text(encoding='utf-8')
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
            destination = contained(file.parent / name) if name else file
            require(destination.exists(), f'Broken local link in {file.relative_to(ROOT)}: {link}')
            if separator and fragment.startswith('pdf-page-'):
                require(f'## PDF page {fragment.removeprefix("pdf-page-")}' in destination.read_text(encoding='utf-8'), 'Missing guide page anchor')
            links += 1
    print(f'PASS: {len(tracked)} package files; {links} local links; 16 page fingerprints; one planning PDF; manifests and templates.')


if __name__ == '__main__':
    main()
