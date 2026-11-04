#!/usr/bin/env python3
"""Restore deduplicated historical paths to a NEW external working directory."""
from pathlib import Path
import argparse,hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('destination',type=Path);a=ap.parse_args()
    dest=a.destination.resolve()
    if dest==ROOT or ROOT in dest.parents:raise ValueError('Choose a directory outside the immutable handoff package')
    if dest.exists() and any(dest.iterdir()):raise ValueError('Destination must be empty')
    rows=json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))['files']
    for r in rows:
        src=ROOT/r['stored_path'];data=src.read_bytes()
        if hashlib.sha256(data).hexdigest()!=r['sha256']:raise ValueError('Hash mismatch: '+r['stored_path'])
        target=dest/r['target_path'];target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target)
    print('Restored',len(rows),'source paths under',dest)
    print('No optimization was started; see REPRODUCE.md before running historical scripts.')
if __name__=='__main__':main()
