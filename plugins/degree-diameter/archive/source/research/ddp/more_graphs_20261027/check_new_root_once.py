"""One fresh-edge-list check for a genuinely new extension mechanism."""
from pathlib import Path
from collections import deque, Counter
import argparse
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument('graph', type=Path)
parser.add_argument('output', type=Path)
parser.add_argument('--degree', type=int, required=True)
parser.add_argument('--diameter', type=int, required=True)
args = parser.parse_args()
if args.output.exists():
    print(args.output.read_text())
    raise SystemExit(0)

start = time.process_time()
with args.graph.open() as stream:
    n, expected_m = map(int, stream.readline().split())
    adj = [[] for _ in range(n)]
    edges = set()
    for line in stream:
        u, v = map(int, line.split())
        assert 0 <= u < v < n
        assert (u, v) not in edges
        edges.add((u, v))
        adj[u].append(v)
        adj[v].append(u)
assert len(edges) == expected_m
maximum = max(map(len, adj))
assert maximum <= args.degree
root = n - 1
dist = [-1] * n
dist[root] = 0
queue = deque([root])
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] < 0:
            dist[v] = dist[u] + 1
            queue.append(v)
assert -1 not in dist and max(dist) <= args.diameter
result = dict(graph=str(args.graph), n=n, m=expected_m, simple=True,
    max_degree=maximum, new_root=root, new_root_max_distance=max(dist),
    new_root_reachable=n, new_root_distance_histogram=dict(sorted(Counter(dist).items())),
    independent_fresh_edge_list_new_root_check=True, roots_checked=1,
    all_source_BFS_executed=False,
    old_old_scope='Not recomputed here; production retains oldedges and the literal generator comparison checks the resultingedge set.',
    new_root_old_vertices_bad_count=0, CPU_seconds=time.process_time() - start)
args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False))
