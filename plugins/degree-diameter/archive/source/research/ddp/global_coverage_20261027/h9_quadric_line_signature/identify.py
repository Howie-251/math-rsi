"""Recover ambient-quadric line witnesses, never H9 incidence adjacency."""
from pathlib import Path
from itertools import product, combinations
from array import array
import json
import lzma
import time
import resource

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
assert json.loads((OUT / 'PREDICTION.json').read_text())['frozen_before_coordinate_generation_and_line_test']
BASE = ROOT / 'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout'

# F9 = F3[t]/(t^2+1), x+y*t encoded x+3*y, exactly as the author's point order.
add = [[(a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3) for b in range(9)] for a in range(9)]
mul = [[((a % 3) * (b % 3) - (a // 3) * (b // 3)) % 3 +
        3 * (((a % 3) * (b // 3) + (a // 3) * (b % 3)) % 3) for b in range(9)] for a in range(9)]
neg = [(-a % 3) % 3 + 3 * ((-(a // 3)) % 3) for a in range(9)]
inv = [0] + [next(b for b in range(1, 9) if mul[a][b] == 1) for a in range(1, 9)]
cube = [mul[mul[a][a]][a] for a in range(9)]

def norm(v):
    k = inv[next(x for x in v if x)]
    return tuple(mul[k][x] for x in v)

def on_quadric(v):
    return add[add[mul[v[0]][v[4]]][mul[v[1]][v[5]]]][mul[v[2]][v[6]]] == mul[v[3]][v[3]]

points = []
projective_candidates = 0
for lead in range(7):
    prefix = (0,) * lead + (1,)
    for tail in product(range(9), repeat=6-lead):
        v = prefix + tail
        projective_candidates += 1
        if on_quadric(v):
            points.append(v)
assert len(points) == 66430
index = {v: i for i, v in enumerate(points)}
with lzma.open(BASE / 'partial_fold_source/tau.txt.xz', 'rt') as f:
    tau = list(map(int, f.read().split()))
phi = [tau[tau[p]] for p in range(66430)]
# A complete cheap ordering calibration: tau^2 is coordinate Frobenius at every point.
assert all(points[phi[p]] == tuple(cube[x] for x in v) for p, v in enumerate(points))
qdata = json.loads((BASE / 'Q_data.json').read_text())
state = json.loads((BASE / 'witness12_state.json').read_text())['states']
split_reps = {p for p, st in zip(qdata['generic_point_representatives'], state) if st != 0}
label = [p if phi[p] == p or min(p, phi[p]) in split_reps else min(p, phi[p]) for p in range(66430)]
labels = sorted(set(label))
assert len(labels) == 41356
core_number = {p: i for i, p in enumerate(labels)}
fold = [core_number[x] for x in label]
lifts = [[] for _ in range(41356)]
for p, v in enumerate(fold):
    lifts[v].append(p)
assert all(1 <= len(v) <= 2 for v in lifts)
(OUT / 'point_coords.u8.bin').write_bytes(bytes(x for v in points for x in v))
(OUT / 'point_to_core.u16.bin').write_bytes(array('H', fold).tobytes())

def span_ids(x, y):
    line = [norm(tuple(add[x[j]][mul[t][y[j]]] for j in range(7))) for t in range(9)] + [y]
    if not all(on_quadric(v) for v in line):
        return None
    ids = tuple(sorted(index[v] for v in line))
    assert len(set(ids)) == 10
    return ids

def is_h9_line(x, y):
    def grass(i, j):
        return add[mul[x[i]][y[j]]][neg[mul[x[j]][y[i]]]]
    return all(grass(i, j) == grass(k, l) for i, j, k, l in
               [(1,2,3,4), (5,4,3,2), (2,0,3,5), (6,5,3,0), (0,1,3,6), (4,6,3,1)])

screen = json.loads((ROOT / 'research/ddp/global_coverage_20261027/h9_line_signature/necessary_filter.json').read_text())
subjects = [r for r in screen['records'] if r['pre165']]
assert len(subjects) == 675
records = []
tested_lift_pairs = 0
unique_quadric_candidates = 0
for row in subjects:
    if time.process_time() - START > 54:
        break
    pins = row['A_i']
    A = set(pins)
    seen = set()
    witness = None
    local_tested = local_unique = 0
    for a, b in combinations(pins, 2):
        for p, q in product(lifts[a], lifts[b]):
            tested_lift_pairs += 1
            local_tested += 1
            ids = span_ids(points[p], points[q])
            if ids is None or ids in seen:
                continue
            seen.add(ids)
            unique_quadric_candidates += 1
            local_unique += 1
            image = sorted(set(fold[t] for t in ids))
            if set(image) <= A:
                witness = dict(original_point_labels=list(ids),
                               original_point_coordinates=[list(points[t]) for t in ids],
                               folded_image=image, extra_anchors=sorted(A-set(image)),
                               image_size=len(image), defining_pin_pair=[a,b],
                               defining_original_pair=[p,q],
                               is_H9_incidence_line=is_h9_line(points[p], points[q]))
                break
        if witness:
            break
    record = dict(vertex=row['vertex'], A_i=pins, matched=witness is not None,
                  tested_lift_pairs=local_tested, unique_quadric_lines_tested=local_unique,
                  witness=witness)
    records.append(record)
    if len(records) == 1:
        (OUT / 'first41502.json').write_text(json.dumps(record, indent=2) + '\n')
    if witness is None:
        break

failed = next((r['vertex'] for r in records if not r['matched']), None)
matched = sum(r['matched'] for r in records)
status = 'FALSIFIED' if failed is not None else ('ALL675_MATCH' if len(records) == 675 else 'UNKNOWN_CPU_LIMIT')
result = dict(prediction_id='P_Qline', status=status, total_subjects=675,
              subjects_tested=len(records), subjects_matched=matched, first_failed_vertex=failed,
              projective_candidates=projective_candidates, quadric_points=66430,
              point_coordinate_order_calibration='all66430 Frobenius images equal tau^2',
              core_vertices=41356, core_fold_label_convention='author sorted least-point labels; split7959 from cached witness',
              tested_original_lift_pairs=tested_lift_pairs, unique_quadric_candidates=unique_quadric_candidates,
              records=records, cached_point_coordinates='point_coords.u8.bin:66430x7,uint8',
              cached_point_to_core='point_to_core.u16.bin:66430,uint16,native-endian',
              H9_incidence_lines_generated=False, BFS_performed=False, new_graphs=0,
              new_lower_bounds=0, CPU_seconds=time.process_time()-START)
(OUT / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'records'}, indent=2))
print('FIRST', json.dumps(records[0], separators=(',', ':')))
