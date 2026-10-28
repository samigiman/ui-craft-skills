#!/usr/bin/env python3
"""Read-only source triage. Findings are review candidates, never AI detection."""
import argparse
import json
import os
import re
from pathlib import Path

EXTENSIONS = {'.css', '.scss', '.sass', '.less', '.html', '.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte', '.swift', '.dart'}
EXCLUDED = {'node_modules', '.git', '.next', '.nuxt', '.vercel', '.cache', 'dist', 'build', 'coverage', 'vendor', 'Pods', '.build', '.dart_tool', 'outputs', '_backups'}
RULES = [
    ('decorative-effect-name', re.compile(r'cursor[-_ ]?glow|pattern[-_ ]?canvas|dot[-_ ]?evolution|particles?[-_ ]?(?:canvas|background)|(?:canvas|background)[-_ ]?particles?', re.I), 'Inspect whether this effect serves the task and still runs when hidden.'),
    ('gradient-text', re.compile(r'background-clip\s*:\s*text|text-fill-color\s*:\s*transparent', re.I), 'Check hierarchy and rendered readability; a brand gradient may be intentional.'),
    ('animation-loop', re.compile(r'\brequestAnimationFrame\s*\('), 'Trace purpose and lifecycle; this may be a legitimate interaction.'),
    ('transition-all', re.compile(r'\btransition\s*:\s*all\b', re.I), 'Inspect affected properties and use explicit transitions when appropriate.'),
    ('overflow-mask', re.compile(r'\boverflow-x\s*:\s*(?:hidden|clip)\b', re.I), 'Measure the layout; this may be deliberate containment rather than a defect.'),
]

def scan(target, limit=200, max_files=2500):
    root = Path(target).expanduser()
    if not root.exists():
        raise ValueError('Target does not exist')
    if root.is_symlink():
        raise ValueError('Choose the explicit source path rather than a symlink')
    root = root.resolve()
    files = []
    if root.is_file():
        files = [root]
    else:
        for base, dirs, names in os.walk(root, followlinks=False):
            dirs[:] = sorted(d for d in dirs if d not in EXCLUDED and not (Path(base)/d).is_symlink())
            for name in sorted(names):
                path = Path(base)/name
                if path.suffix.lower() in EXTENSIONS and not path.is_symlink():
                    files.append(path)
                    if len(files) > max_files:
                        break
            if len(files) > max_files:
                break
    truncated_files = len(files) > max_files
    candidates, skipped, scanned = [], [], 0
    truncated_findings = False
    for path in files[:max_files]:
        label = path.name if root.is_file() else str(path.relative_to(root))
        try:
            if path.suffix.lower() not in EXTENSIONS:
                skipped.append({'path': label, 'reason': 'unsupported-source-type'})
                continue
            if path.stat().st_size > 2 * 1024 * 1024:
                skipped.append({'path': label, 'reason': 'over-2-MiB'})
                continue
            source = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError):
            skipped.append({'path': label, 'reason': 'unreadable-text'})
            continue
        scanned += 1
        for number, line in enumerate(source.splitlines(), 1):
            for rule, pattern, question in RULES:
                match = pattern.search(line)
                if match:
                    if len(candidates) >= limit:
                        truncated_findings = True
                        continue
                    a, b = max(0, match.start()-60), min(len(line), match.end()+100)
                    candidates.append({'path': label, 'line': number, 'rule': rule, 'excerpt': line[a:b].strip(), 'review': question})
    return {'purpose': 'source-triage-only', 'quality_verdict': None, 'files_scanned': scanned, 'file_limit_reached': truncated_files, 'finding_limit_reached': truncated_findings, 'candidates': candidates, 'skipped': skipped}

def positive(value):
    n = int(value)
    if n < 1:
        raise argparse.ArgumentTypeError('Must be positive')
    return n

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', help='One local source file or directory')
    parser.add_argument('--limit', type=positive, default=200, help='Maximum returned candidates')
    parser.add_argument('--max-files', type=positive, default=2500, help='Bounded source file count')
    args = parser.parse_args()
    try:
        result = scan(args.path, args.limit, args.max_files)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
