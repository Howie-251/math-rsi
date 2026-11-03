"""Independent all-root BFS of exactly the two terminal saved reflection graphs."""
import json
import time
from collections import Counter, deque
from pathlib import Path

OUT = Path(__file__).resolve().parent
start = time.process_time()
results = []
for branch in ('mixed', 'both'):
    branch_start = time.process_time()
    path = OUT / f'complete_{branch}.best.edges'
    data = list(map(int, path.read_text().split()))
    n, m = data[:2]
    edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
    assert (n, m) == (656, 1640)
    assert len(edges) == m and len(set(edges)) == m
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(a) == 5 for a in adj)
    all_hist = Counter()
    eccentricity_hist = Counter()
    bad = 0
    roots = {}
    for root in range(n):
        distance = [-1] * n
        distance[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        assert -1 not in distance
        all_hist.update(distance)
        eccentricity_hist[max(distance)] += 1
        bad += sum(distance[v] > 5 for v in range(root + 1, n))
        if root in (0, 328):
            roots[str(root)] = {
                'distance_histogram': dict(sorted(Counter(distance).items())),
                'maximum_distance': max(distance),
                'missing_within_five': sum(d > 5 for d in distance),
            }
    result = {
        'branch': branch, 'input': path.name,
        'vertices': n, 'edges': m, 'simple': True,
        'degree_histogram': dict(sorted(Counter(map(len, adj)).items())),
        'connected': True, 'all_roots_checked': n,
        'diameter': max(eccentricity_hist), 'bad_unordered_pairs_beyond_five': bad,
        'ordered_distance_histogram': dict(sorted(all_hist.items())),
        'eccentricity_histogram': dict(sorted(eccentricity_hist.items())),
        'two_roots': roots,
        'cpu_seconds': time.process_time() - branch_start,
    }
    results.append(result)
output = {
    'status': 'COMPLETE_INDEPENDENT_ALL_ROOT_BFS',
    'method': 'Python parses each complete edge list and builds fresh adjacency, then deque BFS from every vertex; no search generator, group formula, distance cache, or two-root inference is used.',
    'graphs': results,
    'cpu_seconds': time.process_time() - start,
}
(OUT / 'reflection_best_independent_bfs.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
