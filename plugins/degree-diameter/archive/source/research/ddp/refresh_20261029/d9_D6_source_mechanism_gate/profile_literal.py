"""Single source-eligibility gate. No distance or candidate calculations."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import json, os, resource, time

D = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
t0, c0 = time.monotonic(), time.process_time()
handle = {'pid': os.getpid(), 'started_utc': datetime.now(timezone.utc).isoformat(),
          'status': 'RUNNING', 'worker_count': 1, 'hard_cpu_seconds': 30}
(D/'HANDLE.json').write_text(json.dumps(handle, indent=2)+'\n')
rows = [list(map(int, line.split())) for line in (D/'source77418.adjlist.txt').read_text().splitlines()
        if line.strip() and not line.lstrip().startswith('#')]
n = 77418
assert len(rows) == n, (len(rows), n)
if all(len(row) == 10 and row[0] == i for i, row in enumerate(rows)):
    adj = [row[1:] for row in rows]
    fmt = 'explicit row label followed by nine neighbors'
elif all(len(row) == 9 for row in rows):
    adj = rows
    fmt = 'implicit row index with nine neighbors'
else:
    raise AssertionError('Adjacency format differs from the degree9 row contract')
for v, row in enumerate(adj):
    assert v not in row and len(row) == len(set(row))
    assert all(0 <= w < n for w in row)
A = [set(row) for row in adj]
assert all(v in A[w] for v, row in enumerate(adj) for w in row)
hist = Counter(map(len, adj))
free = [v for v, row in enumerate(adj) if len(row) < 9]
triangle = None
for v, row in enumerate(adj):
    for u in row:
        common = A[v] & A[u]
        if common:
            triangle = [v, u, min(common)]
            break
    if triangle:
        break
m = sum(map(len, adj))//2
cpu, wall = time.process_time()-c0, time.monotonic()-t0
result = {
 'status': 'SOURCE_REGULAR_NO_FREE_PORTS_STOP' if not free else 'FREE_PORT_PREDICTION_REFUTED_STOP_FOR_REVIEW',
 'n': n, 'm': m, 'simple': True, 'symmetric': True,
 'degree_histogram': dict(sorted(hist.items())), 'delta': max(hist),
 'literal_format': fmt, 'free_vertex_count_at_Delta9': len(free),
 'free_spare_slot_count_at_Delta9': sum(9-len(adj[v]) for v in free),
 'first_free_vertex': free[0] if free else None,
 'all9regular_prediction': 'SUPPORTED' if hist == Counter({9:n}) else 'REFUTED',
 'local_odd_cycle_witness': triangle, 'bipartite': False if triangle else None,
 'current_source_D6': 'inherited official source assertion; not recomputed',
 'retained_edge_append_at_Delta9': 'IMPOSSIBLE_BY_ZERO_OLD_SPARE_SLOTS' if not free else 'NOT_DECIDED',
 'geometry_orbit_label_binding': 'NOT_ATTEMPTED_NOT_NEEDED_AFTER_PORT_GATE',
 'cpu_seconds': cpu, 'wall_seconds': wall, 'pid': os.getpid(),
 'source_distance_BFS': 0, 'new_balls': 0, 'candidate_graphs': 0,
 'solver_calls': 0, 'secondary_source_10D6_scanned': False
}
(D/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
handle.update(status='TERMINAL', exit_code=0, cpu_seconds=cpu, wall_seconds=wall)
(D/'HANDLE.json').write_text(json.dumps(handle, indent=2)+'\n')
(D/'TERMINAL.json').write_text(json.dumps({'status': result['status'], 'pending': [],
 'actual_source_profile_workers':1,'new_numerical_jobs_queued':0,'exit_code':0},indent=2)+'\n')
print(json.dumps(result, indent=2))
