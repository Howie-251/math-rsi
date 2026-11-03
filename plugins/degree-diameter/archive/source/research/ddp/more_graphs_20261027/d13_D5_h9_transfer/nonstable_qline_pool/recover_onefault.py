"""Recover omitted diagnostic literals from the same cached scope, not a new trial."""
from array import array
from collections import Counter
from pathlib import Path
import json
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (1, 2))
OUT = Path(__file__).resolve().parent
BASE = OUT.parent
ROOT = BASE.parents[3]
assert json.loads((OUT / 'singlefault_PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_SINGLEFAULT_LITERAL_OR_COVER_EXPERIMENT'
ADD = [[(a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3) for b in range(9)] for a in range(9)]
MUL = [[((a % 3) * (b % 3) - (a // 3) * (b // 3)) % 3 +
        3 * (((a % 3) * (b // 3) + (a // 3) * (b % 3)) % 3) for b in range(9)] for a in range(9)]
INV = [0] + [next(b for b in range(1, 9) if MUL[a][b] == 1) for a in range(1, 9)]
points = [tuple(p) for p in json.loads((ROOT / 'research/ddp/more_graphs_20261027/h9_baer_plane_pool/orbit.json').read_text())['coefficient_points_PG2F9']]
idx = {p: i for i, p in enumerate(points)}


def conjugate(p):
    v = [MUL[MUL[x][x]][x] for x in p]
    scale = INV[next(x for x in v if x)]
    return tuple(MUL[scale][x] for x in v)


phi = [idx[conjugate(p)] for p in points]
closures = []
for line_id, dual in enumerate(points):
    if phi[line_id] <= line_id:
        continue
    line = [i for i, p in enumerate(points)
            if ADD[ADD[MUL[dual[0]][p[0]]][MUL[dual[1]][p[1]]]][MUL[dual[2]][p[2]]] == 0]
    closure = sorted(set(line) | {phi[i] for i in line})
    assert len(line) == 10 and len(closure) == 19
    closures.append((line_id, line, closure))
assert len(closures) == 39
flat = json.loads((ROOT / 'research/ddp/more_graphs_20261027/h9_baer_plane_pool/planes.json').read_text())['records']
nonflat = json.loads((ROOT / 'research/ddp/more_graphs_20261027/h9_baer_nonflat_F3_pool/nonflat_planes.json').read_text())['records']
planes = [('flat', r['plane_index'], r['basis_y_x_z'], r['point_ids91']) for r in flat]
planes += [('nonflat', r['nonflat_plane_index'], r['RREF_basis'], r['Q9_point_ids91']) for r in nonflat]
fold = array('H')
fold.frombytes((BASE / 'point_to_core13.u16.bin').read_bytes())
degree = (BASE / 'degree13.u8.bin').read_bytes()
diagnostics, pool = [], []
for kind, plane_index, basis, ids in planes:
    for line_id, line, closure in closures:
        pins = sorted({fold[ids[i]] for i in closure})
        blocked = [p for p in pins if degree[p] >= 13]
        if len(blocked) != 1:
            continue
        deleted = blocked[0]
        remaining = [p for p in pins if p != deleted]
        record = {
            'diagnostic_index': len(diagnostics),
            'diagnostic_recovery_from_same_scope': True,
            'full_pins': pins, 'full_pin_count': len(pins),
            'deleted_saturated_pin': deleted, 'blocked_pins': blocked,
            'mandatory_pins': remaining, 'remaining_pin_count': len(remaining),
            'anchor_cap': 13 - len(remaining),
            'mandatory_pin_degrees': [degree[p] for p in remaining],
            'source_n': 51417, 'source_m': 324451,
            'deleted_pin_must_not_be_readded': True,
            'core_R4_guarantee_after_deletion': False,
            'requires_full_actual_R4_over_core_and_extras': True,
            'witness': {'plane_kind': kind, 'plane_index': plane_index,
                        'plane_basis': basis, 'line_dual_id': line_id,
                        'conjugate_line_dual_id': phi[line_id],
                        'line_dual': points[line_id],
                        'line_rawpoint_ids10': [ids[i] for i in line],
                        'wholeclass_rawpoint_ids19': [ids[i] for i in closure],
                        'deleted_pin_rawpoint_preimages': [ids[i] for i in closure if fold[ids[i]] == deleted]},
        }
        assert all(d < 13 for d in record['mandatory_pin_degrees'])
        diagnostics.append(record)
        if len(remaining) <= 13:
            pool.append(record)
assert len(diagnostics) == 12
summary = {
    'status': 'OMITTED_SINGLEFAULT_LITERALS_RECOVERED',
    'diagnostic_recovery_from_same_scope': True,
    'new_line_experiments': 0, 'original_scope_reopened': False,
    'diagnostic_literals': len(diagnostics), 'cap13_pool_records': len(pool),
    'full_pin_count_histogram': dict(sorted(Counter(r['full_pin_count'] for r in diagnostics).items())),
    'remaining_pin_count_histogram': dict(sorted(Counter(r['remaining_pin_count'] for r in diagnostics).items())),
    'anchor_cap_histogram': dict(sorted(Counter(r['anchor_cap'] for r in diagnostics).items())),
    'blockedpin_histogram': dict(sorted(Counter(r['deleted_saturated_pin'] for r in diagnostics).items())),
    'CPU_seconds': time.process_time() - START, 'CPU_limit_seconds': 1,
    'BFS': 0, 'R4_evaluations': 0, 'anchor_tests': 0,
    'prediction_state': 'FROZEN_NOT_YET_TESTED_COMPLETE_R4',
}
(OUT / 'singlefault_diagnostics.json').write_text(json.dumps({'summary': summary, 'records': diagnostics}, indent=2) + '\n')
(OUT / 'singlefault_pool.json').write_text(json.dumps({
    'source_n': 51417, 'target_degree': 13,
    'diagnostic_recovery_from_same_scope': True,
    'proof_scope': 'Unique saturated pin removed; no automatic coreR4. Require actualR4 of selectedneighbors over all51417oldvertices.',
    'records': pool,
}, indent=2) + '\n')
(OUT / 'singlefault_recovery_result.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2), flush=True)
