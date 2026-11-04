#!/usr/bin/env python3
"""Prepare one archived mother-code certificate and run the literal C++ checker."""
import argparse
import json
from pathlib import Path
import subprocess
import time

if not __debug__:
    raise RuntimeError('Do not disable input-binding assertions with Python -O')

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'archive/source'
ap = argparse.ArgumentParser()
ap.add_argument('--index', type=int, default=169)
ap.add_argument('--output-dir', type=Path, required=True)
ap.add_argument('--cxx', default='c++')
args = ap.parse_args()
out = args.output_dir.resolve()
if out.is_relative_to(SOURCE.resolve()):
    raise ValueError('Output must be outside the frozen source archive')
m = json.loads((SOURCE/'evidence/manifest.json').read_text())
r = next((r for r in m['records'] if r['snapshot172_index'] == args.index), None)
if r is None:
    ap.error(f'Unknown snapshot172_index: {args.index}')
a, p = r['original_scan'], r['pair_graph']
def file(rel):
    x = (SOURCE/rel).resolve()
    if not x.is_relative_to(SOURCE.resolve()) or not x.is_file():
        raise ValueError(f'Input not distributed: {rel}; see archive/INVENTORY.json')
    return x
inp = json.loads(file(a['input_path']).read_text())
result = json.loads(file(a['result_path']).read_text())
representatives = json.loads(file(m['actual_matrix_snapshot']).read_text())['representatives']
snapshot = next((s for s in representatives if s['snapshot172_index'] == args.index), None)
if snapshot is None:
    ap.error(f'Missing matrix snapshot for snapshot172_index: {args.index}')
assert r['actual_generator_rows_40bit_int'] == snapshot['generator_rows_40bit_int']
assert a['scan_rows'] == inp['rows'] == result['rows']
count = result['accepted_count']
assert count == a['accepted_count'] == a['saved_count'] == result['saved_count']
assert p['pair_count'] == count*(count-1)//2
fmt = int(p['rejection_witness_format'].startswith('TSV'))
assert fmt or p['rejection_witness_format'] == 'uint8 base-message per lexicographic pair'
lines = ['LITERAL_PAIR_REPLAY_V1', f'1 {count} {p["pair_count"]}',
         f'{args.index} {count} {p["pair_count"]} {fmt}', r['case']]
for values in (r['actual_generator_rows_40bit_int'], inp['rows'], inp['free'],
               inp['pivots'], a['coordinate_permutation_actual_to_input']):
    lines.append(' '.join(map(str, values)))
lines += [str(file(a['F_path'])), str(file(p['rejection_witness_path'])), 'END']
out.mkdir(parents=True, exist_ok=False)
plan = out/'literal_cases.txt'
plan.write_text('\n'.join(lines)+'\n')
binary = out/'replay_selected'
commands = [[args.cxx, '-std=c++17', '-O3', str(ROOT/'tools/replay_selected.cpp'), '-o', str(binary)],
            [str(binary), str(plan), str(out/'case_results.jsonl'), str(out/'native_result.json'), '60']]
runs = []
for cmd in commands:
    start = time.monotonic()
    process = subprocess.run(cmd, text=True, capture_output=True, timeout=90)
    runs.append(dict(command=cmd, returncode=process.returncode, stdout=process.stdout,
                     stderr=process.stderr, wall_seconds=time.monotonic()-start))
    (out/'PROCESS.json').write_text(json.dumps(runs, indent=2)+'\n')
    if process.returncode:
        raise RuntimeError(process.stderr)
actual = json.loads((out/'native_result.json').read_text())
assert actual['status'] == 'PASS' and actual['cases_completed'] == 1
assert actual['F_count'] == count and actual['pairs_replayed'] == p['pair_count']
assert actual['all_F_actual_distances_checked'] == count*128
assert actual['all_streams_exact_EOF'] and actual['F_domains_rerun'] == 0
print(json.dumps(dict(scope='one complete saved mother-code certificate, not a full quotient scan',
                     original_index=args.index, case=r['case'], result=actual), indent=2))
