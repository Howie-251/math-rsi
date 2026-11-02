import os
for key in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS']:
    os.environ[key] = '1'
import time
started = time.process_time()
import collections
import json
from pathlib import Path
import resource
import warnings

D = Path(__file__).resolve().parent
C = D.parent
prior = json.loads((C/'root_repair1_anchor_gate/TERMINAL.json').read_text())['case_CPU_seconds']
resource.setrlimit(resource.RLIMIT_CPU, (19, 19))

def save(name, data):
    (D/name).write_text(json.dumps(data, indent=2)+'\n')

def mark(status, **extra):
    save('HANDLE.json', dict(status=status, pid=os.getpid(),
         case_CPU_seconds=prior+time.process_time()-started,
         case_CPU_budget_seconds=20, **extra))

mark('BUILDING_ONE_JOINT_MODEL', running=True)
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix

n = 106
A = [set() for _ in range(n)]
with (C/'source106.header.edges').open() as f:
    assert f.readline().strip() == '106 582'
    for line in f:
        u, v = map(int, line.split())
        A[u].add(v)
        A[v].add(u)
pairs = [(u, v) for u in range(n) for v in range(u+1, n)]
yindex = {p: n+i for i, p in enumerate(pairs)}
old = [p for p in pairs if p[1] in A[p[0]]]
tindex = {p: n+len(pairs)+i for i, p in enumerate(old)}
nvars = n+len(pairs)+len(old)
ri, ci, values, lower, upper = [], [], [], [], []

def yi(u, v):
    return yindex[(min(u, v), max(u, v))]

def row(terms, lo=-np.inf, hi=np.inf):
    k = len(lower)
    for j, value in terms:
        ri.append(k)
        ci.append(j)
        values.append(value)
    lower.append(lo)
    upper.append(hi)

row([(u, 1) for u in range(n)], 10, 11)
for u in range(n):
    row([(u, 1)]+[(v, 1) for v in A[u]], 1)
for (u, v), y in yindex.items():
    row([(y, 1), (u, -1)], hi=0)
    row([(y, 1), (v, -1)], hi=0)
for u in range(n):
    terms = [(yi(u, v), 1) for v in range(n) if v != u]
    terms += [(v, -1) for v in A[u]]
    row(terms+[(u, -(10-len(A[u])))], hi=0)
    # When selected: old degree after the new edge is at least10.
    # When outside: the bound is automatically relaxed by11.
    row(terms+[(u, -(20-len(A[u])))], lo=-11)
for v in range(n):
    for u in range(n):
        if u == v or u in A[v]:
            continue
        common = A[v] & A[u]
        row([(v, -1), (u, 1)]+[(w, -1) for w in common]
            +[(yi(v, w), 1) for w in A[u]], lo=-len(common))
for (u, v), t in tindex.items():
    row([(t, 1), (u, -1)], hi=0)
    row([(t, 1), (v, -1)], hi=0)
    row([(t, 1), (u, -1), (v, -1)], lo=-1)
objective = np.zeros(nvars)
for (u, v), y in yindex.items():
    objective[y] = -1 if v in A[u] else 1
for t in tindex.values():
    objective[t] = 1
matrix = coo_matrix((values, (ri, ci)), shape=(len(lower), nvars)).tocsc()
save('MODEL_SCOPE.json', dict(binary_variables=nvars, pin_selectors=n,
     internal_edge_variables=len(pairs), original_edge_scope_variables=len(old),
     constraints=len(lower), nonzeros=len(values),
     generation_rule='Only old edges induced by selected10..11 pins may change',
     objective='Minimum count of deleted plus added old edges',
     solver_calls=1, source_revalidation=False, source_BFS=0))
mark('RUNNING_UNIQUE_INTERNAL_REPAIR_SOLVER', running=True,
     model_variables=nvars, model_rows=len(lower), solver_wall_limit_seconds=10)
solve_start = time.process_time()
with warnings.catch_warnings(record=True) as caught:
    result = milp(objective, integrality=np.ones(nvars), bounds=Bounds(0, 1),
        constraints=LinearConstraint(matrix, np.array(lower), np.array(upper)),
        options={'time_limit': 10.0, 'threads': 1})
solver_CPU = time.process_time()-solve_start
raw = dict(status=int(result.status), message=str(result.message),
           success=bool(result.success), solver_CPU_seconds=solver_CPU,
           warnings=[str(w.message) for w in caught])
for key in ['mip_node_count', 'mip_dual_bound', 'mip_gap', 'fun']:
    value = getattr(result, key, None)
    if value is not None:
        raw[key] = float(value)
save('SOLVER_RETURN.json', raw)
status = 'UNKNOWN_NO_INTEGER_CANDIDATE'
summary = dict(solver=raw, candidate_generated=False,
               graph_increment=0, Lean_increment=0)
if result.x is not None:
    rounded = np.rint(result.x).astype(int)
    assert np.max(np.abs(result.x-rounded)) < 1e-5
    pins = [u for u in range(n) if rounded[u]]
    B = [set(x) for x in A]+[set(pins)]
    for (u, v), y in yindex.items():
        if rounded[u] and rounded[v]:
            if rounded[y]:
                B[u].add(v); B[v].add(u)
            else:
                B[u].discard(v); B[v].discard(u)
    for u in pins:
        B[u].add(n)
    bad = [(u, v) for u in range(n+1) for v in range(u+1, n+1)
           if v not in B[u] and not (B[u] & B[v])]
    assert 10 <= len(pins) <= 11 and max(map(len, B)) <= 11 and not bad
    deleted = [[u, v] for u, v in old if v not in B[u]]
    added = [[u, v] for u, v in pairs if v not in A[u] and v in B[u]]
    edges = [(u, v) for u in range(n+1) for v in sorted(B[u]) if u < v]
    (D/'graph_d11_D2_n107.edges').write_text(
        f'107 {len(edges)}\n'+''.join(f'{u} {v}\n' for u, v in edges))
    save('PARAMETERS.json', dict(source='../source106.header.edges', pins=pins,
         deleted_old_edges=deleted, added_old_edges=added,
         frozen_cross_and_outside_edges=True))
    status = 'VALID_COMPLETE107_CANDIDATE_INDEPENDENT_ACCEPTANCE_PENDING'
    summary.update(candidate_generated=True, n=107, m=len(edges), pins=pins,
        deleted_old_edges=len(deleted), added_old_edges=len(added),
        degree_histogram=dict(collections.Counter(map(len, B))),
        common_neighbor_pair_checks=107*106//2, bad_pairs=bad)
elif result.status == 2:
    status = 'SOLVER_INFEASIBLE_FIXED_INTERNAL_PIN_REWIRING_SCOPE'
    summary['independent_infeasibility_proof'] = False
summary.update(status=status, prior_case_CPU_seconds=prior,
    batch_CPU_seconds=time.process_time()-started,
    case_CPU_seconds=prior+time.process_time()-started,
    case_CPU_budget_seconds=20, solver_calls=1, source_BFS=0)
save('RESULT.json', summary)
mark(status, running=False)
save('TERMINAL.json', dict(status=status, running=False,
     batch_CPU_seconds=time.process_time()-started,
     case_CPU_seconds=prior+time.process_time()-started,
     case_CPU_budget_seconds=20, solver_calls=1))
print(json.dumps(summary), flush=True)
