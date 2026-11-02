#!/usr/bin/env python3
"""Bind one frozen candidate and run its new-root necessary distance gate."""
from collections import Counter, deque
from pathlib import Path
import json
import resource
import time

started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
here = Path(__file__).resolve().parent
project = here.parents[3]
source_dir = project / 'research/ddp/more_graphs_20261027/d13_D4_current6804'
recipe = json.loads((source_dir / 'construction.json').read_text())
group = recipe['construction']['controller']['group']
assert group == {'type': 'metacyclic', 'N': 7, 'M': 12, 'r': 2}
assert recipe['order'] == 6804
zchart = next(c for c in recipe['construction']['charts'] if c['symbol'] == 'z')
xstar = (0, 0, 2, 0)
assert zchart['M'] == [[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]]
assert zchart['d'] == [0,0,1,0]
assert tuple((-xstar[i] + zchart['d'][i]) % 3 for i in range(4)) == xstar
fiber_code = sum(xstar[i] * 3**i for i in range(4))

powers = []
i = j = 0
for k in range(12):
    powers.append((i,j))
    i, j = (i + pow(2,j,7)) % 7, (j+1) % 12
assert (i,j) == (0,0) and powers[6] == (0,6)
T = [81*(i+7*j) + fiber_code for i,j in powers]
expected_T = [18,666,1395,1719,2367,3096,3420,4068,4797,5121,5769,6498]
assert T == expected_T
M = [(T[k], T[k+6]) for k in range(6)]
assert len(set(T)) == 12

adj = [[] for _ in range(6804)]
edges = set()
for line in (source_dir / 'source6804.edges').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    u,v = map(int,line.split())
    edges.add(tuple(sorted((u,v))))
    adj[u].append(v)
    adj[v].append(u)
assert len(edges) == 44226
assert all(tuple(sorted(e)) in edges for e in M)
params = {
    'source': str((source_dir / 'source6804.edges').relative_to(project)),
    'recipe': str((source_dir / 'construction.json').relative_to(project)),
    'x_star': xstar, 'fiber_code': fiber_code, 'a_powers': powers,
    'T': T, 'deleted_matching': M, 'new_vertex': 6804,
    'candidate_order_if_generated': 6805,
    'candidate_edges_if_generated': 44232,
    'six_edges_present_and_disjoint': True,
}
(here / 'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n')

dist = [-1]*6804
toward_T = [-1]*6804
queue = deque(T)
for v in T:
    dist[v] = 0
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] < 0:
            dist[v] = dist[u]+1
            toward_T[v] = u
            queue.append(v)
assert min(dist) == 0
maxdist = max(dist)
failed = next((v for v in range(6804) if dist[v] > 3), None)
witness_path = []
if failed is not None:
    v = failed
    while v != -1:
        witness_path.append(v)
        v = toward_T[v]
(here / 'DISTANCES_TO_T.json').write_text(json.dumps(dist)+'\n')
result = {
    'status': 'REJECTED_NEW_ROOT_DISTANCE_GATE' if failed is not None else 'PASSED_NEW_ROOT_GATE_READY_FOR_CANDIDATE',
    't_max': maxdist,
    'distance_histogram': dict(sorted(Counter(dist).items())),
    'vertices_with_t_greater_than_3': sum(t>3 for t in dist),
    'first_failure': failed,
    'first_failure_distance_to_T': None if failed is None else dist[failed],
    'first_failure_shortest_path_to_T': witness_path,
    'candidate_new_root_distance_to_witness': None if failed is None else dist[failed]+1,
    'source_multi_source_bfs_runs': 1,
    'source_all_root_bfs_runs': 0,
    'candidate_graphs_generated': 0,
    'candidate_bfs_runs': 0,
    'cpu_seconds': time.process_time()-started,
}
(here / 'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if failed is not None:
    (here / 'TERMINAL.json').write_text(json.dumps({**result,'running':False,'pending':[]},indent=2)+'\n')
print(json.dumps(result,separators=(',',':')))
