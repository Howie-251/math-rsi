"""Single cached3640-line degree pass for current degree13 source."""
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
assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_Q3DEFINED_FULLLINE_DEGREE_FILTER'
source = ROOT / 'research/ddp/more_graphs_20261027/h9_baer_nonstable_global_pool/F3_lines.json'
lines = json.loads(source.read_text())['records']
assert len(lines) == 3640
fold = array('H')
fold.frombytes((BASE / 'point_to_core13.u16.bin').read_bytes())
degree = (BASE / 'degree13.u8.bin').read_bytes()
assert len(fold) == 66430 and len(degree) == 51417
qdata = json.loads((ROOT / 'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json').read_text())
fixed = set(qdata['H3_point_representatives'])
assert len(fixed) == 364
rawcoords = (ROOT / 'research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin').read_bytes()
freefixed = [p for p in sorted(fixed) if degree[fold[p]] < 13]
freefixedset = set(freefixed)
fixedhist, blockhist, sizehist = Counter(), Counter(), Counter()
rows, pool = [], {}
for row in lines:
    raw = row['Q9point_ids10']
    pins = tuple(sorted({fold[p] for p in raw}))
    h3 = sorted(set(raw) & fixed)
    assert len(raw) == 10 and len(h3) == 4 and len(pins) <= 10
    bad = [p for p in pins if degree[p] >= 13]
    fixedfree = len(set(h3) & freefixedset)
    fixedhist[fixedfree] += 1
    blockhist[len(bad)] += 1
    sizehist[len(pins)] += 1
    rows.append({'line_index': row['line_index'], 'fixed_raw_points4': h3,
                 'free_fixed_points': fixedfree, 'saturated_pins': bad})
    if not bad:
        pool.setdefault(pins, {'line_index': row['line_index'], 'pins': list(pins),
                              'anchor_cap': 13 - len(pins), 'point_ids10': raw,
                              'RREF_basis': row['RREF_basis'],
                              'pin_degrees': [degree[p] for p in pins]})
records = [pool[k] for k in sorted(pool)]
result = {
    'status': 'COMPLETE_FIXED3640_Q_LINE_D13_DEGREE_POOL',
    'source_n': 51417, 'source_m': 324451, 'degree_cap': 13,
    'raw_lines': len(lines), 'degree_legal_distinct_pinsets': len(records),
    'all_F3_defined_lines_hit_saturated_pin': not records,
    'H3_fixed_points': 364, 'H3_free_points': len(freefixed),
    'H3_saturated_points': 364 - len(freefixed),
    'fixed_free_points_per_line_histogram': dict(sorted(fixedhist.items())),
    'every_line_hit_by_saturated_H3_point': fixedhist[4] == 0,
    'saturated_pin_count_histogram': dict(sorted(blockhist.items())),
    'mandatory_pin_count_histogram': dict(sorted(sizehist.items())),
    'P_AT_LEAST_ONE_FREE_LINE': 'SUPPORTED' if records else 'REFUTED',
    'CPU_seconds': time.process_time() - START, 'CPU_limit_seconds': 5,
    'BFS': 0, 'R4_evaluations': 0, 'anchor_tests': 0, 'new_graphs': 0,
    'scope': 'Only all3640 F3-defined fullsingular Q9lines; no non-F3-defined Qlines or changedsource.',
}
(OUT / 'pool13.json').write_text(json.dumps({'source_n': 51417, 'target_degree': 13, 'records': records}, indent=2) + '\n')
(OUT / 'fixed108_pattern.json').write_text(json.dumps({
    'free_fixed_points': [{'original_point': p, 'core_vertex': fold[p], 'degree': degree[fold[p]],
                           'coordinates': list(rawcoords[7*p:7*p+7])} for p in freefixed],
    'H3_degree_histogram': dict(sorted(Counter(degree[fold[p]] for p in fixed).items())),
    'line_fixed_free_histogram': dict(sorted(fixedhist.items())), 'records': rows,
}, indent=2) + '\n')
(OUT / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
(OUT / 'terminal.json').write_text(json.dumps({**result, 'running': False, 'pending': []}, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
