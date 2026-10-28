#!/usr/bin/env python3
"""Copy selected skills into a local agent skill directory without overwriting."""
import argparse
import os
import shutil
from pathlib import Path

SKILLS = (
    'product-ui-direction', 'ui-deslop', 'reference-led-web-design',
    'commerce-ux-refinement', 'responsive-ui-verification', 'operational-dashboard-ux',
)
SOURCE = Path(__file__).resolve().parents[1] / 'skills'


def install(names, destination, dry_run=False):
    names = list(dict.fromkeys(names))
    if not names:
        raise ValueError('Select at least one skill')
    for name in names:
        if name not in SKILLS:
            raise ValueError('Unknown skill: ' + name)
        source = SOURCE / name
        if not (source / 'SKILL.md').is_file():
            raise ValueError('Missing SKILL.md: ' + name)
        if source.is_symlink() or any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError('Source symlinks are not installed: ' + name)
    destination = Path(destination).expanduser()
    if destination.is_symlink():
        raise ValueError('Use an explicit destination rather than a symlink')
    if destination.exists() and not destination.is_dir():
        raise ValueError('Destination is not a directory')
    for name in names:
        if os.path.lexists(destination / name):
            raise FileExistsError('Existing skill left untouched: ' + name)
    if dry_run:
        return [str(destination / name) for name in names]
    destination.mkdir(parents=True, exist_ok=True)
    installed = []
    for name in names:
        # copytree refuses even a newly appeared destination; no overwrite retry.
        shutil.copytree(SOURCE / name, destination / name,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
        installed.append(str(destination / name))
    return installed


def main():
    default_root = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--all', action='store_true', help='Install all six skills')
    selection.add_argument('--skill', nargs='+', choices=SKILLS, help='Install selected skills')
    parser.add_argument('--dest', type=Path, default=default_root / 'skills')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    args = parser.parse_args()
    try:
        paths = install(SKILLS if args.all else args.skill, args.dest, args.dry_run)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')
    verb = 'Would install' if args.dry_run else 'Installed'
    for path in paths:
        print(verb + ': ' + path)
    if not args.dry_run:
        print('Start a new Codex turn to discover the installed skills.')


if __name__ == '__main__':
    main()
