"""Independent original-graph integer-bitset coverage test; no candidate BFS."""
import json
import time
from collections import Counter
from pathlib import Path

start = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
data = list(map(int, (ROOT / 'research/ddp/m1_degree5_transfer/rithwik650_source.edges').read_text().split()))
n, m = data[:2]
edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
assert (n, m) == (650, 1625) and len(edges) == m
adj = [set() for _ in range(n)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
balls = []
for root in range(n):
    reached = {root}
    frontier = {root}
    for _ in range(4):
        frontier = set().union(*(adj[v] for v in frontier)) - reached
        reached.update(frontier)
    balls.append(sum(1 << v for v in reached))
edge_balls = [balls[u] | balls[v] for u, v in edges]
hist = Counter()
rejected = 0
best_pairs = []
best = n
for i, (a, b) in enumerate(edges):
    first = edge_balls[i]
    for j in range(i + 1, m):
        c, d = edges[j]
        if a == c or a == d or b == c or b == d:
            rejected += 1
            continue
        missing = n - (first | edge_balls[j]).bit_count()
        hist[missing] += 1
        if missing < best:
            best, best_pairs = missing, []
        if missing == best:
            best_pairs.append([i, j])
recorded = json.loads((OUT / 'complete.summary.json').read_text())
hist_json = {str(k): v for k, v in sorted(hist.items())}
assert hist_json == recorded['new_root_missing_histogram']
assert rejected == recorded['shared_endpoint_rejected']
assert sum(hist.values()) == recorded['disjoint_pairs']
result = {
    'status': 'COMPLETE_INDEPENDENT_EXACT_MATCH', 'source_vertices': n, 'source_edges': m,
    'total_unordered_edge_pairs': m * (m - 1) // 2,
    'shared_endpoint_rejected': rejected, 'disjoint_pairs': sum(hist.values()),
    'ball4_size_histogram': dict(sorted(Counter(x.bit_count() for x in balls).items())),
    'new_root_missing_histogram': hist_json, 'minimum_missing': best,
    'minimum_attaining_pairs': len(best_pairs), 'minimum_pair_edge_ids': best_pairs,
    'exact_recorded_histogram_match': True,
    'cpu_seconds': time.process_time() - start,
    'method': 'Independently build all closed radius-four balls from original adjacency, encode as Python integers, enumerate every disjoint original edge pair and count bits in the endpoint-ball union.',
    'scope': 'Necessary optimistic coverage before deletion; no candidate graph BFS. Zero pairs cover all original vertices.'
}
(OUT / 'independent_coverage_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'minimum_pair_edge_ids'}, indent=2))
