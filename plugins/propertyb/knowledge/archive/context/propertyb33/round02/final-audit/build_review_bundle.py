#!/usr/bin/env python3
"""Package the T33 reading edition, source closure, and reproducibility evidence."""
from pathlib import Path
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'aris4math_t33_review_bundle.zip'


def source_closure():
    pending = ['Aris4Math.ThirtyThree.Main', 'Aris4Math.Main']
    seen = set()
    result = set()
    while pending:
        module = pending.pop()
        if module in seen:
            continue
        seen.add(module)
        path = ROOT / 'formal' / Path(*module.split('.')).with_suffix('.lean')
        if not path.is_file():
            raise FileNotFoundError(path)
        result.add(path)
        pending.extend(re.findall(r'^import\s+(Aris4Math(?:\.[\w]+)*)\s*$', path.read_text(), re.M))
    return result


def main():
    required = [
        'HANDOFF_FOR_REVIEW_33.md', 'PROOF_PACKAGE_33.html',
        'proofs/propertyb33/PROOF_PACKAGE.md',
        'context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md',
        'context/propertyb33/FORMAL_VERIFICATION.md',
        'context/propertyb33/round02/final-audit/PROOF_AUDIT.md',
        'context/propertyb33/round02/final-audit/PROOF_AUDIT.json',
        'context/propertyb33/round02/final-assembly/main-build.log',
        'context/propertyb33/round02/final-assembly/original-statement-import-audit.log',
        'formal/lean-toolchain', 'formal/lakefile.toml', 'formal/lake-manifest.json',
        'formal/ReviewAudit33.lean', 'formal/ReviewAudit.lean', 'formal/README_T33.md',
        'PROOF_PACKAGE_33.html.review.json',
        'context/propertyb33/round02/final-assembly/main-build.meta.json',
        'context/propertyb33/round02/final-assembly/original-statement-post-build-audit.log',
        'context/propertyb33/round02/final-assembly/original-statement-post-build-audit.meta.json',
        'research-wiki/claims/propertyb-m5-ge34.md',
    ]
    files = source_closure()
    for rel in required:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(path)
        files.add(path)
    for rel in ['context/propertyb33/round01', 'context/propertyb33/round02',
                'computations/propertyb33', 'proofs/propertyb33',
                '.aris/traces/proof-checker/2026-10-13_t33_run01',
                '.aris/traces/render-html/2026-10-13_t33_run01']:
        for path in (ROOT / rel).rglob('*'):
            if (path.is_file() and not path.is_symlink()
                    and path.suffix in {'.md', '.json', '.txt', '.log', '.lean', '.py', '.tex', '.pdf'}
                    and '__pycache__' not in path.parts
                    and path.name != 'bundle-files.json'):
                files.add(path)
    relative = sorted(path.relative_to(ROOT).as_posix() for path in files)
    with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for rel in relative:
            bundle.write(ROOT / rel, arcname='aris4math_t33/' + rel)
    with zipfile.ZipFile(OUT) as bundle:
        bad = bundle.testzip()
        if bad is not None:
            raise RuntimeError(f'Archive readback failed: {bad}')
    record = {'archive': OUT.name, 'files': relative, 'file_count': len(relative),
              'archive_bytes': OUT.stat().st_size,
              'verification': 'Source import closure and archive readback only; no fresh extracted build claimed.'}
    (Path(__file__).parent / 'bundle-files.json').write_text(json.dumps(record, indent=2) + '\n')
    print(f'{OUT.name}: {len(relative)} files, {OUT.stat().st_size} bytes')


if __name__ == '__main__':
    main()
