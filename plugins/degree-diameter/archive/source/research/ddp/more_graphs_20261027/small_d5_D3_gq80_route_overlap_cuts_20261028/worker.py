"""One bounded feasibility call on the complete saved GQ80 overlap-cut model."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json
import math
import resource
import time
from datetime import datetime, timezone
from pathlib import Path

cpu0 = time.process_time()
wall0 = time.perf_counter()
HERE = Path(__file__).resolve().parent
stats = json.loads((HERE / 'MODEL_STATS.json').read_text())
hard = max(1, math.floor(55 - stats['preparation_CPU_seconds']))
resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))
import warnings
import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import load_npz

OLD = HERE.parents[1] / 'breadth_20261027_wave11/gq80_paired_matchings'


def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


A = load_npz(HERE / 'full_model.csc.npz')
lb = np.load(HERE / 'lower.npy')
ub = np.load(HERE / 'upper.npy')
assert A.shape == (4280, 1560) and A.nnz == 780600
assert len(lb) == len(ub) == 4280
save('RUN_HANDLE.json', dict(status='SOLVING_SINGLE_FULL_MODEL', pid=os.getpid(),
     started_at_utc=datetime.now(timezone.utc).isoformat(), solver_limit_seconds=45,
     aggregate_CPU_hard_seconds=55, worker_CPU_hard_seconds=hard,
     inherited_preparation_CPU_seconds=stats['preparation_CPU_seconds'],
     solver_calls_started=1, rows=4280, binary_variables=1560, nnz=780600))
solver_cpu0, solver_wall0 = time.process_time(), time.perf_counter()
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter('always')
    result = milp(c=np.zeros(1560), integrality=np.ones(1560), bounds=Bounds(0, 1),
                  constraints=LinearConstraint(A, lb, ub),
                  options=dict(time_limit=45.0, threads=1, presolve=True, disp=True))
solver_cpu = time.process_time() - solver_cpu0
solver_wall = time.perf_counter() - solver_wall0
incumbent = result.x is not None
out = dict(scipy_version=scipy.__version__, solver_status=int(result.status),
           solver_message=str(result.message), solver_success=bool(result.success),
           incumbent_reported=incumbent, solver_CPU_seconds=solver_cpu,
           solver_wall_seconds=solver_wall, warnings=[str(x.message) for x in caught],
           mip_node_count=getattr(result, 'mip_node_count', None),
           mip_gap=getattr(result, 'mip_gap', None), objective=getattr(result, 'fun', None),
           solver_calls=1, graph_BFS_calls=0, candidate_graphs=int(incumbent),
           actual_D=None, ordinary_bad_unordered_pairs=None)
if incumbent:
    bits = np.rint(result.x).astype(np.int8)
    assert np.max(np.abs(bits-result.x)) < 1e-5
    assert np.all((bits == 0) | (bits == 1))
    values = A @ bits
    assert np.all(values >= lb) and np.all(values <= ub)
    model = json.loads((OLD / 'model.json').read_text())
    selected = [i for i, value in enumerate(bits) if value]
    assert len(selected) == 40
    matchings = [[], []]
    for i in selected:
        v = model['variables'][i]
        matchings[0 if v['side'] == 'point' else 1].append([v['u'], v['v']])
    source_rows = (OLD / 'incidence.edges').read_text().splitlines()
    assert source_rows[0].split() == ['80', '160']
    edges = [tuple(map(int, row.split())) for row in source_rows[1:] if row.strip()]
    for side in (0, 1):
        assert len(matchings[side]) == 20
        assert sorted(x for pair in matchings[side] for x in pair) == list(range(40))
        edges.extend((u+40*side, v+40*side) for u, v in matchings[side])
    edges = sorted(tuple(sorted(e)) for e in edges)
    assert len(edges) == len(set(edges)) == 200
    degrees = [0] * 80
    for u, v in edges:
        assert u != v
        degrees[u] += 1
        degrees[v] += 1
    assert set(degrees) == {5}
    (HERE / 'candidate.edges').write_text('80 200\n' + ''.join(f'{u} {v}\n' for u, v in edges))
    save('candidate.matchings.json', dict(point_matching=matchings[0], line_matching=matchings[1],
         selected_variable_ids=selected, n=80, m=200, degree=5,
         all_original_degree_and_cover_constraints_pass=True, all_3120_new_cuts_pass=True,
         original_cover_minimum=float(min(values[80:1160])),
         overlap_cut_minimum=float(min(values[1160:])), graph_BFS_calls=0,
         pending='Parent all-80-source BFS on the exported candidate.'))
    status = 'EXACT_CONSTRAINT_INCUMBENT_AWAITS_ROOT_FULL_BFS'
elif result.status == 2:
    status = 'SOLVER_DECLARED_INFEASIBLE_UNCERTIFIED'
else:
    status = 'UNKNOWN_NO_INCUMBENT_WINDOW_CLOSED'
out.update(status=status, worker_CPU_seconds=time.process_time()-cpu0,
           worker_wall_seconds=time.perf_counter()-wall0,
           inherited_preparation_CPU_seconds=stats['preparation_CPU_seconds'],
           total_measured_CPU_before_driver=stats['preparation_CPU_seconds']+time.process_time()-cpu0,
           worker_CPU_hard_seconds=hard, configured_aggregate_CPU_hard_seconds=55)
save('RESULT.json', out)
save('terminal.json', out)
save('RUN_HANDLE.json', out | {'pid': os.getpid(), 'finished_at_utc': datetime.now(timezone.utc).isoformat()})
print(json.dumps(out, indent=2), flush=True)
