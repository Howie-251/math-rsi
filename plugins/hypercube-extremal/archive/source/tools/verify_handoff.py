#!/usr/bin/env python3
"""Verify archived-source provenance and, when present, the complete package manifest."""
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(2**20),b''):h.update(b)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--require-manifest',action='store_true');a=ap.parse_args()
    failures=[];checked={}
    inv=json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
    for r in inv['files']:
        rel=r['stored_path'];p=(ROOT/rel).resolve()
        if ROOT not in p.parents:failures.append('Unsafe path '+rel);continue
        if not p.is_file():failures.append('Missing '+rel);continue
        if rel not in checked:checked[rel]=(p.stat().st_size,digest(p))
        if checked[rel]!=(r['size_bytes'],r['sha256']):failures.append('Mismatch '+rel)
    manifest=ROOT/'SHA256SUMS.json'
    if manifest.exists():
        m=json.loads(manifest.read_text(encoding='utf-8'))
        entries=m.get('files',m)
        if isinstance(entries,list):entries={r['path']:r['sha256'] for r in entries}
        actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p!=manifest}
        for rel in actual-set(entries):failures.append('Unmanifested file '+rel)
        for rel in set(entries)-actual:failures.append('Manifest file absent '+rel)
        for rel,value in entries.items():
            h=value['sha256'] if isinstance(value,dict) else value
            p=(ROOT/rel).resolve()
            if ROOT not in p.parents or not p.is_file() or digest(p)!=h:failures.append('Manifest mismatch '+rel)
        print('Manifest entries checked:',len(entries))
    elif a.require_manifest:failures.append('Package SHA256SUMS.json is missing')
    else:print('Package manifest pending; checking source inventory only.')
    print('Source logical paths:',len(inv['files']),'unique stored files:',len(checked))
    for f in failures:print('FAIL:',f)
    if failures:sys.exit(1)
    print('PASS: SHA-256, file sizes, deduplicated source mapping.')
if __name__=='__main__':main()
