"""Fixed nonstable-line wholeclass pool; no graph-distance calculation."""
from array import array
from collections import Counter
from pathlib import Path
import json
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
OUT = Path(__file__).resolve().parent
BASE = OUT.parent
ROOT = BASE.parents[3]
assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_NONSTABLE_LINE_POOL'
ADD = [[(a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3) for b in range(9)] for a in range(9)]
MUL = [[((a % 3) * (b % 3) - (a // 3) * (b // 3)) % 3 +
        3 * (((a % 3) * (b // 3) + (a // 3) * (b % 3)) % 3) for b in range(9)] for a in range(9)]
INV = [0] + [next(b for b in range(1, 9) if MUL[a][b] == 1) for a in range(1, 9)]
points = [tuple(p) for p in json.loads((ROOT / 'research/ddp/more_graphs_20261027/h9_baer_plane_pool/orbit.json').read_text())['coefficient_points_PG2F9']]
idx = {p: i for i, p in enumerate(points)}


def frobenius(p):
    v = [MUL[MUL[x][x]][x] for x in p]
    scale = INV[next(x for x in v if x)]
    return tuple(MUL[scale][x] for x in v)


phi = [idx[frobenius(p)] for p in points]
local_lines = []
for line_id, dual in enumerate(points):
    if phi[line_id] == line_id:
        continue
    # Each conjugate pair has the identical closure; evaluate it once.
    if line_id > phi[line_id]:
        continue
    line = [i for i, p in enumerate(points)
            if ADD[ADD[MUL[dual[0]][p[0]]][MUL[dual[1]][p[1]]]][MUL[dual[2]][p[2]]] == 0]
    conjugate = {phi[i] for i in line}
    closure = sorted(set(line) | conjugate)
    fixed = [i for i in closure if phi[i] == i]
    assert len(line) == 10 and len(closure) == 19 and len(fixed) == 1
    local_lines.append((line_id, phi[line_id], line, closure, fixed[0]))
assert len(local_lines) == 39
flat = json.loads((ROOT / 'research/ddp/more_graphs_20261027/h9_baer_plane_pool/planes.json').read_text())['records']
nonflat = json.loads((ROOT / 'research/ddp/more_graphs_20261027/h9_baer_nonflat_F3_pool/nonflat_planes.json').read_text())['records']
planes = [('flat', r['plane_index'], r['basis_y_x_z'], r['point_ids91']) for r in flat]
planes += [('nonflat', r['nonflat_plane_index'], r['RREF_basis'], r['Q9_point_ids91']) for r in nonflat]
assert len(planes) == 1120
fold = array('H')
fold.frombytes((BASE / 'point_to_core13.u16.bin').read_bytes())
degree = (BASE / 'degree13.u8.bin').read_bytes()
assert len(fold) == 66430 and len(degree) == 51417
hist, badhist, legalhist = Counter(), Counter(), Counter()
pool, degree_allowed, fixedfree, oversized = {}, 0, 0, 0
for plane_kind, plane_index, basis, ids in planes:
    for line_id, conjugate_id, line, closure, fixed in local_lines:
        pins = tuple(sorted({fold[ids[i]] for i in closure}))
        assert 10 <= len(pins) <= 19
        hist[len(pins)] += 1
        bad = [v for v in pins if degree[v] >= 13]
        badhist[len(bad)] += 1
        fixedfree += degree[fold[ids[fixed]]] < 13
        if bad:
            continue
        degree_allowed += 1
        legalhist[len(pins)] += 1
        if len(pins) > 13:
            oversized += 1
            continue
        if pins not in pool:
            pool[pins] = {'pins': list(pins), 'anchor_cap': 13 - len(pins),
                          'mandatory_pin_count': len(pins),
                          'pin_current_degrees': [degree[v] for v in pins],
                          'witness': {'plane_kind': plane_kind, 'plane_index': plane_index,
                                      'plane_basis': basis, 'line_dual_id': line_id,
                                      'conjugate_line_dual_id': conjugate_id,
                                      'line_dual': points[line_id],
                                      'line_rawpoint_ids10': [ids[i] for i in line],
                                      'wholeclass_rawpoint_ids19': [ids[i] for i in closure],
                                      'fixed_rawpoint_id': ids[fixed]}}
records = [pool[k] for k in sorted(pool)]
result = {
    'status': 'COMPLETE_NONSTABLE_Q_LINE_FIXED1120_PLANES_D13_POOL',
    'source_n': 51417, 'source_m': 324451, 'delta': 13,
    'F3_defined_planes': 1120, 'nonstable_lines_per_plane': 78,
    'nominal_line_occurrences': 87360, 'actual_conjugate_closure_tests': 43680,
    'conjugate_duplicates_skipped_by_identical_closure': 43680,
    'stable_lines_evaluated': 0, 'unique_closures_with_free_fixed_point': fixedfree,
    'actual_pin_count_histogram_all_closures': dict(sorted(hist.items())),
    'saturated_pin_count_histogram': dict(sorted(badhist.items())),
    'degree_allowed_closures': degree_allowed,
    'degree_allowed_pin_count_histogram': dict(sorted(legalhist.items())),
    'degree_allowed_but_over13_closures': oversized,
    'degree_and_size_feasible_unique_pinsets': len(records),
    'pool_pin_count_histogram': dict(sorted(Counter(len(r['pins']) for r in records).items())),
    'prediction_verdict': 'SUPPORTED' if records else 'REFUTED',
    'CPU_seconds': time.process_time() - START, 'CPU_limit_seconds': 5,
    'BFS': 0, 'R4_evaluations': 0, 'anchor_tests': 0, 'new_graphs': 0,
    'scope': 'Only non-F3-stable Q9lines in1120 cachedF3defined planes, with fullphi-class closures, unchanged51417source.',
}
(OUT / 'pool13.json').write_text(json.dumps({'source_n': 51417, 'target_degree': 13, 'records': records}, indent=2) + '\n')
(OUT / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
(OUT / 'terminal.json').write_text(json.dumps({**result, 'running': False}, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
