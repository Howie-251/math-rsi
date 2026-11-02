"""Read the saved neighbor graph and validate its full distances independently."""
import csv
import json
import time
from collections import Counter, deque
from pathlib import Path

start = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
summary = json.loads((OUT / 'complete.summary.json').read_text())

def read_graph(path):
    data = list(map(int, path.read_text().split()))
    n, m = data[:2]
    edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
    assert len(edges) == m and len(set(edges)) == m
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u].add(v)
        adj[v].add(u)
    return n, set(edges), adj

n, source_edges, source_adj = read_graph(ROOT / summary['source'])
assert n == 651
legal_moves = [(x, y) for x in range(650) if x not in source_adj[650] for y in sorted(source_adj[x])]
assert len(legal_moves) == summary['legal_neighbor_count'] == 3230
rows = list(csv.DictReader((OUT / 'complete.moves.tsv').open(), delimiter='\t'))
assert len(rows) == summary['evaluated']
for i, row in enumerate(rows):
    assert (int(row['index']), int(row['x']), int(row['y'])) == (i, *legal_moves[i])
hist = Counter(int(row['bad_pairs']) for row in rows)
assert {str(k): v for k, v in hist.items()} == summary['score_histogram']
if summary['status'] == 'COMPLETE':
    assert len(rows) == len(legal_moves)
n, best_edges, adj = read_graph(OUT / 'complete.best.edges')
assert best_edges - source_edges == {tuple(sorted(summary['best_added_edge']))}
assert source_edges - best_edges == {tuple(sorted(summary['best_deleted_edge']))}
deficit = summary['best_new_deficit_vertex']
assert all(len(a) == (4 if v == deficit else 5) for v, a in enumerate(adj))
distance_hist = Counter()
bad_pairs = []
root_distance_histograms = {}
eccentricities = Counter()
for root in range(n):
    dist = [-1] * n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert -1 not in dist
    distance_hist.update(dist)
    eccentricities[max(dist)] += 1
    bad_pairs.extend([root, v] for v in range(root + 1, n) if dist[v] > 5)
    if root in (650, deficit):
        root_distance_histograms[str(root)] = dict(sorted(Counter(dist).items()))
assert len(bad_pairs) == summary['minimum']
result = {
    'status': 'COMPLETE_INDEPENDENT_CHECK',
    'source': summary['source'], 'best_graph': 'complete.best.edges',
    'vertices': n, 'edges': len(best_edges), 'simple': True, 'connected': True,
    'degree_histogram': dict(sorted(Counter(map(len, adj)).items())),
    'unique_degree_four_vertex': deficit,
    'exact_edge_difference': True,
    'added_edges': sorted(best_edges - source_edges),
    'deleted_edges': sorted(source_edges - best_edges),
    'legal_neighborhood_size': len(legal_moves),
    'evaluated_move_list_is_exact_prefix': True,
    'entire_neighborhood_evaluated': len(rows) == len(legal_moves),
    'per_move_score_histogram_matches_summary': True,
    'diameter': max(eccentricities), 'eccentricity_histogram': dict(sorted(eccentricities.items())),
    'bad_pairs': len(bad_pairs), 'bad_pair_list': bad_pairs,
    'bad_pairs_involving_original_new_vertex_650': sum(650 in pair for pair in bad_pairs),
    'bad_pairs_involving_moved_deficit': sum(deficit in pair for pair in bad_pairs),
    'ordered_distance_histogram': dict(sorted(distance_hist.items())),
    'special_root_distance_histograms': root_distance_histograms,
    'cpu_seconds': time.process_time() - start,
    'scope': 'Independent Python adjacency/BFS on the saved best graph only, plus full legal move-list and result-histogram consistency. No new search.'
}
(OUT / 'complete.independent_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'bad_pair_list'}, indent=2))
