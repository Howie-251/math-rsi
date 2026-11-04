#!/usr/bin/env python3
"""Copy available scientific files and restore deduplicated research aliases, skipping the five declared generated tables."""
from pathlib import Path
import argparse
import json
import shutil


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('destination', type=Path)
    a = ap.parse_args()
    archive = Path(__file__).resolve().parents[1] / 'archive'
    source, dest = archive / 'source', a.destination.resolve()
    if dest == source or source in dest.parents:
        raise ValueError('Destination must be outside the frozen source archive')
    if dest.exists() and any(dest.iterdir()):
        raise ValueError('Destination must be empty')
    omitted = {r['path'] for r in json.loads((archive / 'INVENTORY.json').read_text())['omitted_files']}
    shutil.copytree(source, dest, dirs_exist_ok=True)
    skipped, restored = [], 0
    for row in json.loads((source / 'inventory.json').read_text())['files']:
        if row['stored_path'] in omitted:
            skipped.append(row['target_path'])
            continue
        src, target = source / row['stored_path'], dest / row['target_path']
        if src.stat().st_size != row['size_bytes']:
            raise ValueError('Unexpected source size: ' + row['stored_path'])
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        restored += 1
    base = 'research/optimization_20261028_q4/'
    required = [base + name for name in [
        'prepare_data.py', 'keys.bin', 'generate_models.cpp', 'edges.bin',
        'face_pair_lookup.bin', 'vertex_flag_codes.bin', 'evaluate.cpp',
        'model.py', 'sdp_core.py', 'full_meta.npz', 'full_C.npz',
        'face_orbit_meta.npz', 'face_block_0.npz', 'face_block_1.npz',
        'face_block_3.npz', 'face_block_6.npz', 'face_block_7.npz',
        'q5control_best.npz']]
    required.append('research/q5_empty_moment_20261028/column_lift.py')
    missing = [name for name in required if not (dest / name).is_file()]
    result = {'restored_logical_files': restored, 'skipped_generated_targets': skipped,
              'required_aliases_checked': required, 'missing_required_aliases': missing,
              'key_aliases_present': not missing,
              'source_unchanged': True, 'optimization_started': False,
              'next': 'In destination/research/optimization_20261028_q4 run prepare_data.py then compile/run generate_models.cpp; see reproduction.md'}
    (dest / 'SEARCH_MATERIALIZATION.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    if missing:
        raise ValueError('Required search inputs missing: ' + ', '.join(missing))


if __name__ == '__main__':
    main()
