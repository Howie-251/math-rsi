#!/usr/bin/env python3
"""Create a portable source/evidence snapshot, preserving project-relative paths."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PREFIX = 'aris4math_propertyB_20261030'
ARCHIVE = ROOT / 'aris4math_propertyB_k5_12_general_lean_20261030.zip'
SKIP_PARTS = {'.lake', '.tools', '.git', '__pycache__', '.pytest_cache',
              'node_modules', 'software', 'reproduction-runs', 'extracted', 'portable-test'}
SKIP_SUFFIX = {'.zip', '.pyc', '.olean', '.ilean', '.o', '.trace'}
PAGES = ['START_HERE_20261030.html', 'PROPERTY_B_GENERAL_BOUND.html',
         'PROPERTY_B_GENERAL_LEAN.html', 'PROPERTY_B_SMALL_K_6_11.html',
         'K12_LOCK_COMPARISON.html', 'M6_GE67.html', 'M8_M9_IMPROVEMENTS.html', 'M5_GE33.html', 'M5_GE34.html',
         'M5_GE35.html', 'PROPERTY_B_TOOLKIT.html']
ALIASES = {'README.md': 'README_COLLABORATOR_20261030.md',
           'START_HERE.html': 'START_HERE_20261030.html'}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.ids = set()
        self.math = 0
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.targets.append(attrs['href'])
        if tag in {'img', 'script'} and attrs.get('src'):
            self.targets.append(attrs['src'])
        self.math += tag == 'mjx-container'
        self.scripts += tag == 'script'


def allowed(path):
    return (path.is_file() and not path.is_symlink()
            and not SKIP_PARTS.intersection(path.relative_to(ROOT).parts)
            and path.suffix not in SKIP_SUFFIX
            and path.name not in {'.DS_Store', 'PACKAGE_CHECKS.json'}
            and not path.name.startswith('~$'))


def gather():
    files = set()

    def add(relative):
        path = ROOT / relative
        if not path.exists():
            raise FileNotFoundError(relative)
        if path.is_dir():
            files.update(p for p in path.rglob('*') if allowed(p))
        elif allowed(path):
            files.add(path)

    for rel in ['context/collaborator-handoff-20261021',
                'context/propertyb-m6-66-20261029',
                'context/propertyb-m6-67-diagnosis-20261029',
                'context/propertyb-m6-67-progress-20261029',
                'context/propertyb-m7-131-20261029',
                'context/propertyb-m8-267-20261029',
                'context/propertyb-m9-543-20261029',
                'context/propertyb-k12-4664-20261029',
                'context/propertyb-small-updates-20261029',
                '.aris/traces/proof-checker/2026-10-29_m6-ge67',
                '.aris/traces/proof-checker/2026-10-29_m8-m9',
                '.aris/traces/render-html/2026-10-29_small-689-final',
                '.aris/traces/render-html/2026-10-29_small-89-final-status',
                '.aris/traces/render-html/2026-10-29_m6-ge67',
                'formal', 'proofs', 'computations', 'results', 'research-wiki',
                'ref', 'propertyB_small_k', 'figures/propertyb_bounds',
                'context/collaborator-small-k-20261019', 'context/propertyb-general',
                'context/propertyb-general-lean-growth', 'context/propertyb-general-lean-pilot',
                'context/propertyb34-reader', 'context/rendering',
                'context/collaborator-handoff-20261030',
                '.aris/traces/render-html/2026-10-21_refined-criterion-labels']:
        add(rel)
    for name in PAGES + list(ALIASES.values()) + [
            'M5_GE35.md', 'PROOF_PACKAGE.html', 'PROOF_PACKAGE.md', 'PROOF_PACKAGE_FULL.md',
            'PROOF_PACKAGE_33.html', 'PROPERTY_B_TOOLKIT.md',
            'FORMAL_SPEC.md', 'FORMAL_SPEC_PROPERTYB_34.md',
            'HANDOFF_FOR_REVIEW.md', 'HANDOFF_FOR_REVIEW_33.md',
            'HANDOFF_PROPERTYB_GENERAL.md']:
        add(name)
    for manifest in ['small_k_paths.json', 'general_paths.json']:
        data = json.loads((ROOT / 'context/collaborator-handoff-20261021' / manifest).read_text())
        paths = data if isinstance(data, list) else data['include_paths']
        for rel in paths:
            add(rel)
    lean = json.loads((ROOT / 'context/collaborator-handoff-20261021/lean_paths.json').read_text())
    for entry in lean['entries'].values():
        for rel in entry.get('evidence', []):
            add(rel)
    for rel in ['M6_GE67.html.review.json', 'M8_M9_IMPROVEMENTS.html.review.json',
                'PROPERTY_B_GENERAL_BOUND.html.review.json',
                'README_COLLABORATOR_20261021.md', 'START_HERE_20261021.html',
                'M6_GE67.md', 'M8_M9_IMPROVEMENTS.md',
                'PROPERTY_B_SMALL_K_6_11.html.review.json',
                '.aris/traces/render-html/2026-10-21_collaborator-small-k']:
        if (ROOT / rel).exists():
            add(rel)

    # All immediate navigation from the delivered readers and new guides must work.
    checked_sources = [ROOT / name for name in PAGES]
    checked_sources += [ROOT / 'README_COLLABORATOR_20261030.md']
    checked_sources += list(HERE.glob('*GUIDE.md')) + [HERE / 'LEAN_REPRODUCE.md']
    if (HERE / 'PORTABLE_REPRODUCE.md').exists():
        checked_sources.append(HERE / 'PORTABLE_REPRODUCE.md')
    if (HERE / 'portability_paths.json').exists():
        payload = json.loads((HERE / 'portability_paths.json').read_text())
        for rel in (payload if isinstance(payload, list) else payload['include_paths']):
            add(rel)
    for path in checked_sources:
        text = path.read_text()
        if path.suffix == '.html':
            parser = Links()
            parser.feed(text)
            hrefs = parser.targets
        else:
            hrefs = re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)', text)
        for href in hrefs:
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT):
                raise ValueError(f'Nonportable reader link: {path.name}: {href}')
            add(target.relative_to(ROOT))
    return files


def audit_imports(root):
    sources = sorted((root / 'formal').rglob('*.lean'))
    missing = []
    for path in sources:
        for line in path.read_text().splitlines():
            if not line.startswith('import '):
                continue
            for module in line.split('--', 1)[0].split()[1:]:
                if module == 'Aris4Math' or module.startswith('Aris4Math.'):
                    target = root / 'formal' / Path(*module.split('.')).with_suffix('.lean')
                    if not target.is_file():
                        missing.append([str(path.relative_to(root)), module])
    if missing:
        raise ValueError(f'Missing Lean imports: {missing}')
    return {'lean_source_files': len(sources), 'missing_project_imports': [],
            'fresh_lean_build': False}


def audit_pages(root):
    reports = []
    for name in PAGES + ['START_HERE.html']:
        path = root / name
        parser = Links()
        parser.feed(path.read_text())
        missing = []
        local_count = 0
        for href in parser.targets:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            local_count += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.exists():
                missing.append(href)
            elif target == path and url.fragment and unquote(url.fragment) not in parser.ids:
                missing.append(href)
        if missing:
            raise ValueError(f'Missing extracted reader links in {name}: {missing}')
        if parser.scripts:
            raise ValueError(f'Unexpected offline reader scripts: {name}')
        reports.append({'page': name, 'local_links': local_count,
                        'embedded_math': parser.math, 'missing_links': []})
    return reports


def main():
    files = gather()
    contents = sorted((str(p.relative_to(ROOT)), p.stat().st_size) for p in files)
    manifest = ('Property B collaborator snapshot: 2026-10-30\n'
                'Start: START_HERE.html or README.md\n'
                'General k>=12: complete Lean. Small k: see per-result status.\n'
                'Small k=5..12: 35,67,131,267,543,1112,2275,4664; individual status in README.\n'
                'Toolchain/cache not bundled; source dependencies are pinned.\n\n'
                + '\n'.join(f'{size:>12}  {rel}' for rel, size in contents) + '\n'
                + '\nReader aliases:\n' + '\n'.join(f'{a} <- {b}' for a,b in ALIASES.items()) + '\n')
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for relative, _ in contents:
            bundle.write(ROOT / relative, f'{PREFIX}/{relative}')
        for alias, original in ALIASES.items():
            bundle.write(ROOT / original, f'{PREFIX}/{alias}')
        bundle.writestr(f'{PREFIX}/PACKAGE_CONTENTS.txt', manifest)
    with tempfile.TemporaryDirectory(prefix='propertyb-collaborator-') as tmp:
        with zipfile.ZipFile(ARCHIVE) as bundle:
            bundle.extractall(tmp)  # ZIP CRC is checked during reads.
        extracted = Path(tmp) / PREFIX
        for relative, size in contents:
            if (extracted / relative).stat().st_size != size:
                raise ValueError(f'Extraction size mismatch: {relative}')
        report = {'archive': ARCHIVE.name, 'snapshot': '2026-10-30',
                  'file_count': len(contents) + len(ALIASES) + 2,
                  'source_bytes': sum(s for _, s in contents),
                  'extensions': dict(Counter(Path(p).suffix for p,_ in contents)),
                  'extraction_and_crc': 'PASS',
                  'reader_navigation': audit_pages(extracted),
                  'lean_source_imports': audit_imports(extracted),
                  'fresh_full_certificate_replay': False,
                  'portable_replay_evidence': 'context/collaborator-handoff-20261030/PORTABILITY_CHECKS.json',
                  'scope': 'Archive, reader-navigation and Lean source-dependency checks; no fresh Lean build. Selected portable numerical replay is reported separately; mathematical states are unchanged.'}
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    (HERE / 'PACKAGE_CHECKS.json').write_text(encoded)
    with zipfile.ZipFile(ARCHIVE, 'a', zipfile.ZIP_DEFLATED) as bundle:
        bundle.writestr(f'{PREFIX}/PACKAGE_CHECKS.json', encoded)
    print(json.dumps({'archive': str(ARCHIVE), 'bytes': ARCHIVE.stat().st_size,
                      'files': report['file_count'], 'checks': 'PASS'}, indent=2))


if __name__ == '__main__':
    main()
