#!/usr/bin/env python3
"""The one predicted F25 point against six F5-defined planes; no graph."""
import json
import os
import resource
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
start = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
P = json.loads((ROOT / 'research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json').read_text())
C, T, L = P['controller'], P['matrices'], P['directions']
assert C[0][1] == 20 and P['inverse_ports'][1] == 0 and L[0] == [1, 0, 0]
assert 2 not in {x*x % 5 for x in range(5)}
def mv(A, x):
    return [sum(a*b for a,b in zip(row,x)) % 5 for row in A]
def normal(a, b):
    n = [(a[1]*b[2]-a[2]*b[1]) % 5,
         (a[2]*b[0]-a[0]*b[2]) % 5,
         (a[0]*b[1]-a[1]*b[0]) % 5]
    scale = pow(next(x for x in n if x), -1, 5)
    return [scale*x % 5 for x in n]
rows = []
for kind, j, v in ([('pre', i, mv(T[1], L[i])) for i in range(4) if i != 1]
                   + [('post', j, L[j]) for j in range(4) if j != 0]):
    n = normal(L[0], v)
    assert n[0] == 0
    # F25 element a+b*alpha is represented by [a,b].
    value = [n[1], n[2]]
    assert value != [0, 0]
    rows.append({'kind': kind, 'other_port': j, 'normal_over_F5': n,
                 'normal_dot_target_in_F25_basis_1_alpha': value, 'target_in_plane': False})
assert len({tuple(r['normal_over_F5']) for r in rows}) == 6
result = {'status': 'PREDICTED_SINGLE_TARGET_UNREACHABLE_SUPPORTED', 'pid': os.getpid(),
          'field': 'F5[alpha]/(alpha^2-2)', 'source': {'controller': 0, 'field': [[0,0]]*3},
          'target': {'controller': 20, 'field': [[0,0],[1,0],[0,1]]},
          'port': 1, 'inverse_port': 0, 'planes': rows,
          'inverse_and_rank_preservation': 'Every identity and nonzero F5 determinant is preserved by the injective field extension.',
          'reachable_target_fiber_size_by_proved_formula': 3625,
          'target_fiber_size': 15625, 'missing_target_coordinates_by_formula': 12000,
          'graph_generated': False, 'BFS': False, 'matrix_search': False,
          'CPU_seconds': time.process_time()-start, 'pending': []}
(HERE / 'F25_COUNTEREXAMPLE.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'planes'}), flush=True)
