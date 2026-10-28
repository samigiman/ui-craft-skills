#!/usr/bin/env python3
"""Validate the collection's structure and metadata, not design quality."""
import re
import sys
from pathlib import Path
try:
    import yaml
except ImportError:
    raise SystemExit('Install development dependencies: python3 -m pip install -r requirements-dev.txt')

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'product-ui-direction', 'ui-deslop', 'reference-led-web-design',
    'commerce-ux-refinement', 'responsive-ui-verification', 'operational-dashboard-ux',
}


def validate(root=ROOT):
    errors = []
    folders = {p.name for p in (root / 'skills').iterdir() if p.is_dir() and p.name != '__pycache__'}
    if folders != EXPECTED:
        errors.append('Skill folders differ from the expected collection')
    for name in sorted(EXPECTED):
        folder = root / 'skills' / name
        try:
            text = (folder / 'SKILL.md').read_text()
            match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
            if not match:
                raise ValueError('Missing frontmatter')
            front = yaml.safe_load(match.group(1))
            if front.get('name') != name or not isinstance(front.get('description'), str) or not front['description'].strip():
                raise ValueError('Invalid name or description')
            if '[TODO:' in text:
                raise ValueError('Unfinished scaffold')
            interface = yaml.safe_load((folder / 'agents/openai.yaml').read_text())
            ui = interface['interface']
            if not 25 <= len(ui['short_description']) <= 64 or '$' + name not in ui['default_prompt']:
                raise ValueError('Invalid UI metadata')
            if interface.get('policy', {}).get('allow_implicit_invocation', True) is not True:
                raise ValueError('Automatic discovery must remain available')
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
            errors.append(name + ': ' + str(error))
    for file in root.rglob('*.md'):
        if '.git' in file.relative_to(root).parts:
            continue
        for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
            if re.match(r'[a-z]+:', link) or link.startswith('#'):
                continue
            target = link.split('#', 1)[0]
            if target and not (file.parent / target).exists():
                errors.append(str(file.relative_to(root)) + ': broken link ' + link)
    return errors


if __name__ == '__main__':
    issues = validate()
    if issues:
        print('\n'.join(issues), file=sys.stderr)
        raise SystemExit(1)
    print('6 skills: structure, metadata and local Markdown links valid.')
    print('This check makes no design-quality or agent-performance claim.')
