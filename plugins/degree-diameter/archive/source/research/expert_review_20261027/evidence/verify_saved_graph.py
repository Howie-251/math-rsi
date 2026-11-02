"""One final ordinary all-source BFS check of a saved explicit edge list."""
from collections import Counter, deque
from pathlib import Path
import argparse
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument('directory', type=Path)
parser.add_argument('--vertices', type=int, required=True)
parser.add_argument('--degree', type=int, required=True)
parser.add_argument('--target-diameter', type=int, required=True)
parser.add_argument('--expected-bad-pairs', type=int, required=True)
parser.add_argument('--save-bad-pairs', action='store_true')
args = parser.parse_args()
p = args.directory
output = p / 'best.independent_check.json'
assert not output.exists(), 'Reuse the saved final check; do not repeat it.'
started = time.process_time()
n = args.vertices
rows = [tuple(map(int, s.split())) for s in (p / 'best.edges').read_text().splitlines() if s.strip() and not s.startswith('#')]
assert rows[0] == (n, len(rows)-1), 'Expected explicit vertex/edge-count header.'
edges = rows[1:]
assert all(0 <= u < v < n for u, v in edges)
assert len(set(edges)) == len(edges)
adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
degrees = [len(row) for row in adj]
assert min(degrees) == max(degrees) == args.degree
hist = Counter()
misses = []
bad_pairs = []
diameter = 0
for root in range(n):
    dist = [-1]*n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1
                queue.append(v)
    assert -1 not in dist, 'Saved candidate is disconnected.'
    hist.update(dist)
    diameter = max(diameter, max(dist))
    misses.append(sum(d > args.target_diameter for d in dist))
    if args.save_bad_pairs:
        bad_pairs.extend((root, v) for v, d in enumerate(dist) if root < v and d > args.target_diameter)
assert sum(misses) % 2 == 0
bad = sum(misses)//2
assert bad == args.expected_bad_pairs
if args.save_bad_pairs:
    assert len(bad_pairs) == bad
report = dict(status='COMPLETE', n=n, edges=len(edges), simple=True,
              minimum_degree=min(degrees), maximum_degree=max(degrees),
              connected=True, roots_checked=n, diameter=diameter,
              target_diameter=args.target_diameter, bad_unordered_pairs=bad,
              root_radius_deficits=misses,
              ordered_distance_histogram=dict(sorted(hist.items())),
              method='Rebuild adjacency solely from saved explicit edges; ordinary deque BFS from every vertex; no search caches or group symmetry assumed.',
              CPU_seconds=time.process_time()-started, pending=[])
if args.save_bad_pairs:
    report['bad_pairs'] = bad_pairs
output.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['n','edges','diameter','bad_unordered_pairs','roots_checked','CPU_seconds']}))
