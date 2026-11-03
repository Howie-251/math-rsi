"""Reuse the saved GQ80 model and append all route-overlap integer cuts.

This entry point constructs data only. It never imports or calls a solver.
"""
import json
import os
import time
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

cpu0 = time.process_time()
wall0 = time.perf_counter()
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.sparse import coo_matrix, save_npz

HERE = Path(__file__).resolve().parent
OLD = HERE.parents[1] / 'breadth_20261027_wave11/gq80_paired_matchings'


def save(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + '\n')


geometry = json.loads((OLD / 'geometry.json').read_text())
model = json.loads((OLD / 'model.json').read_text())
variables = model['variables']
assert len(variables) == model['variable_count'] == 1560
assert len(model['degree_equations']) == 80
assert len(model['far_pair_covers']) == 1080
assert model['preassigned_edges'] == model['symmetry_constraints'] == []

lines = [set(row) for row in geometry['lines']]
incident = [set(row) for row in geometry['point_incident_lines']]
closed = [
    [{p} | set().union(*(lines[l] for l in incident[p])) for p in range(40)],
    [{l} | set().union(*(incident[p] for p in lines[l])) for l in range(40)],
]
assert all(len(c) == 13 for side in closed for c in side)
assert all(len(side[x] & side[y]) == 4
           for side in closed for x, y in combinations(range(40), 2))
edge_id = {(0 if row['side'] == 'point' else 1, row['u'], row['v']): i
           for i, row in enumerate(variables)}


def eid(side, u, v):
    return edge_id[side, min(u, v), max(u, v)]


rows, cols, data, lower, upper = [], [], [], [], []


def append(indices, coefficients, lo, hi):
    row = len(lower)
    rows.extend([row] * len(indices))
    cols.extend(indices)
    data.extend(coefficients)
    lower.append(lo)
    upper.append(hi)


for row in model['degree_equations']:
    append(row['vars'], [1] * len(row['vars']), 1, 1)
for row in model['far_pair_covers']:
    assert len(row['vars']) == 41
    append(row['vars'], [1] * len(row['vars']), 1, np.inf)
assert len(lower) == 1160 and len(data) == 47400

cuts = []
universe = set(range(40))
for side in (0, 1):
    for x, y in combinations(range(40), 2):
        z = universe - (closed[side][x] | closed[side][y])
        assert len(z) == 18
        selected = eid(side, x, y)
        for root in (x, y):
            c = closed[side][root]
            assert not c & z
            positive = sorted(eid(side, u, v) for u in c for v in z)
            assert len(positive) == len(set(positive)) == 234
            assert selected not in positive
            cuts.append(dict(side=side, matched_edge=[x, y], root=root,
                             closed_root=sorted(c), outside_both=sorted(z),
                             positive_variable_ids=positive,
                             selected_variable_id=selected,
                             selected_coefficient=-6, lower_bound=0))
            append(positive + [selected], [1] * 234 + [-6], 0, np.inf)

assert len(cuts) == 3120
assert len(lower) == 4280 and len(data) == 780600
matrix = coo_matrix((np.asarray(data, dtype=np.float64),
                     (np.asarray(rows, dtype=np.int32), np.asarray(cols, dtype=np.int32))),
                    shape=(4280, 1560)).tocsc()
assert matrix.nnz == 780600
save_npz(HERE / 'full_model.csc.npz', matrix)
np.save(HERE / 'lower.npy', np.asarray(lower, dtype=np.float64))
np.save(HERE / 'upper.npy', np.asarray(upper, dtype=np.float64))
save('overlap_cuts.json', {'schema': 'ordered_root_route_overlap_cut_v1',
                         'cut_count': len(cuts), 'cuts': cuts})
stats = dict(status='PREPARED_NO_SOLVER_CALL', prepared_at_utc=datetime.now(timezone.utc).isoformat(),
             original_geometry=str(OLD / 'geometry.json'), original_model=str(OLD / 'model.json'),
             original_incidence=str(OLD / 'incidence.edges'), variable_count=1560,
             original_degree_equations=80, original_cover_constraints=1080,
             new_route_overlap_cuts=3120, rows=4280, nnz=780600,
             positive_coefficients_per_new_row=234, selected_coefficient=-6,
             cut_rows_per_side=1560, variable_domain='binary',
             objective='zero feasibility objective', preselected_edges=[], symmetry_constraints=[],
             original_input_modified=False, geometry_reconstructed=False,
             solver_calls=0, graph_BFS_calls=0, candidate_graphs=0,
             preparation_CPU_seconds=time.process_time()-cpu0,
             preparation_wall_seconds=time.perf_counter()-wall0)
save('MODEL_STATS.json', stats)
save('terminal.json', stats | {'pending': 'Parent paper review before one solver invocation.'})
print(json.dumps(stats, indent=2), flush=True)
