"""One fixed-center geometric enumeration; degree checks only, no distances."""
import json
import resource
import sys
import time
from array import array
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
assert json.loads((OUT / 'PREDICTION.json').read_text())['frozen_before_candidate_enumeration']
GEOMETRY = OUT.parent / 'h9_quadric_line_signature'
sys.path.insert(0, str(GEOMETRY))
from geometry import ADD, MUL, normalize, line_points

neg = [(-a % 3) % 3 + 3 * ((-(a // 3)) % 3) for a in range(9)]
raw = (GEOMETRY / 'point_coords.u8.bin').read_bytes()
points = [tuple(raw[7*i:7*i+7]) for i in range(66430)]
index = {p: i for i, p in enumerate(points)}
fold = array('H')
fold.frombytes((GEOMETRY / 'point_to_core.u16.bin').read_bytes())
assert len(fold) == 66430
center_source = OUT.parent / 'h9_quadric_center/RESULT.json'
centers = json.loads(center_source.read_text())
assert centers['pending'] == [] and len(centers['records']) == 675
assert centers['tested_selected_lines'] == 675
center_groups = {}
for record in centers['records']:
    y = tuple(record['center_coordinates'])
    if y not in center_groups:
        center_groups[y] = dict(center_original_label=record['center_original_label'],
                                center_coordinates=list(y),
                                first_source_vertex=record['vertex'],
                                basis=record['line_basis_coordinates'], source_vertices=[])
    center_groups[y]['source_vertices'].append(record['vertex'])

degrees = []
source = ROOT / 'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
with source.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):
            continue
        row = list(map(int, line.split()))
        assert row[0] == len(degrees)
        degrees.append(len(row)-1)
assert len(degrees) == 42342 and max(degrees) == 12

def h9_line(x, z):
    def p(i, j):
        return ADD[MUL[x[i]][z[j]]][neg[MUL[x[j]][z[i]]]]
    return all(p(i,j) == p(k,l) for i,j,k,l in
               [(1,2,3,4),(5,4,3,2),(2,0,3,5),(6,5,3,0),(0,1,3,6),(4,6,3,1)])

original_seen = set()
fold_seen = set()
pool_by_pins = {}
counts = Counter({name: 0 for name in [
    'raw_geometric_lines', 'unique_original_lines', 'duplicate_original_line_tuples',
    'unique_fold_pin_tuples', 'duplicate_fold_pin_tuples',
    'excluded_new_vertex_degree_original_lines',
    'excluded_saturated_core_pin_original_lines', 'degree_feasible_original_lines']})
blocked_hist = Counter()
pin_size_hist = Counter()
feasible_pin_size_hist = Counter()
exclusion_examples = []
center_rows = []
complete = True
for y, meta in sorted(center_groups.items(), key=lambda kv: kv[1]['center_original_label']):
    if time.process_time() - START > 27:
        complete = False
        break
    x, z = map(tuple, meta['basis'])
    before = counts.copy()
    for a in range(9):
        u = normalize(tuple(ADD[x[j]][neg[MUL[a][y[j]]]] for j in range(7)))
        for b in range(9):
            v = normalize(tuple(ADD[z[j]][neg[MUL[b][y[j]]]] for j in range(7)))
            counts['raw_geometric_lines'] += 1
            assert not h9_line(u, v)
            line = line_points(u, v)
            ids = tuple(sorted(index[p] for p in line))
            if ids in original_seen:
                counts['duplicate_original_line_tuples'] += 1
                continue
            original_seen.add(ids)
            counts['unique_original_lines'] += 1
            pins = tuple(sorted({fold[p] for p in ids}))
            if pins in fold_seen:
                counts['duplicate_fold_pin_tuples'] += 1
            else:
                fold_seen.add(pins)
                counts['unique_fold_pin_tuples'] += 1
            pin_size_hist[len(pins)] += 1
            blocked = [p for p in pins if degrees[p] >= 12]
            blocked_hist[len(blocked)] += 1
            if len(pins) > 12:
                counts['excluded_new_vertex_degree_original_lines'] += 1
                continue
            if blocked:
                counts['excluded_saturated_core_pin_original_lines'] += 1
                if len(exclusion_examples) < 12:
                    exclusion_examples.append(dict(center_original_label=meta['center_original_label'],
                        dual_coordinates=[1,a,b], original_point_labels=list(ids), pins=list(pins),
                        saturated_core_pins=blocked,
                        pin_current_degrees=[degrees[p] for p in pins]))
                continue
            counts['degree_feasible_original_lines'] += 1
            feasible_pin_size_hist[len(pins)] += 1
            witness = dict(center_original_label=meta['center_original_label'],
                           center_coordinates=list(y), first_source_vertex=meta['first_source_vertex'],
                           center_source_vertices=meta['source_vertices'], dual_coordinates=[1,a,b],
                           line_basis_coordinates=[list(u),list(v)], original_point_labels=list(ids))
            if pins not in pool_by_pins:
                pool_by_pins[pins] = dict(pins=list(pins), pin_current_degrees=[degrees[p] for p in pins],
                                          new_vertex_degree=len(pins), geometric_witnesses=[])
            pool_by_pins[pins]['geometric_witnesses'].append(witness)
    center_rows.append({**meta, 'enumeration_counts':dict(counts-before)})

pool = [pool_by_pins[k] for k in sorted(pool_by_pins)]
status = ('COMPLETE_NONEMPTY_DEGREE_POOL' if pool else 'COMPLETE_EMPTY_DEGREE_POOL') if complete else 'UNKNOWN_CPU_LIMIT_PARTIAL_POOL'
result = dict(prediction_id='P_Qline_degree_pool', status=status,
              prediction_outcome=('SUPPORTED_NECESSARY_DEGREE_ONLY' if pool else 'REFUTED_FIXED_CENTER_SCOPE') if complete else 'UNKNOWN',
              base_n=42342, base_m=sum(degrees)//2, target_n=42343, target_Delta=12, target_D=5,
              input_source_witnesses=675, distinct_recovered_centers=len(center_groups),
              centers_enumerated=len(center_rows), expected_raw_lines=81*len(center_groups),
              counts=dict(counts), fold_pin_count_histogram=dict(pin_size_hist),
              saturated_pin_count_histogram=dict(blocked_hist),
              degree_feasible_pin_count_histogram=dict(feasible_pin_size_hist),
              degree_feasible_distinct_pinsets=len(pool),
              excluded_saturated_core_pin_distinct_pinsets=len(fold_seen)-len(pool),
              current_core_degree_histogram=dict(Counter(degrees[:41356])),
              current_full_graph_degree_histogram=dict(Counter(degrees)),
              exclusion_examples=exclusion_examples, center_records=center_rows,
              pool=pool, pending=[] if complete else ['remaining centers not enumerated; no automatic continuation'],
              original_line_or_selected_witness_uniqueness_assumed=False,
              degree_infeasibility_scope='Fixed full42342 source; only81-line flatplanes of centers from the frozen675 selected witnesses',
              BFS_performed=False, R4_scored=False, anchors_optimized=False,
              new_graphs_generated=0, new_lower_bounds=0, CPU_seconds=time.process_time()-START)
(OUT / 'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT / 'pool.json').write_text(json.dumps({'base_n':42342,'new_vertex':42342,'target_Delta':12,'target_D':5,'records':pool},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['center_records','pool','exclusion_examples']},indent=2))
if pool:
    print('FIRST_FEASIBLE', json.dumps(pool[0]))
