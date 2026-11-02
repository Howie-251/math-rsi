"""A counterexample in the existing q41 graph, without any new construction."""
import json
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
source = OUT / 'q41_search/search.best.edges'
parameters = json.loads((OUT / 'q41_search/search.best.json').read_text())
q, k, L, B, n = 41, 20, 820, 205, 1066
data = list(map(int, source.read_text().split()))
assert data[:2] == [n, 2665]
edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
for neighbors in adj:
    neighbors.sort()

def bfs(leaf_only=False):
    distances = [-1] * n
    parent = [-1] * n
    distances[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if leaf_only and v >= L:
                continue
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                parent[v] = u
                queue.append(v)
    return distances, parent

full_distance, parent = bfs()
leaf_distance, _ = bfs(True)
powers = [pow(parameters['r'], i, q) for i in range(k)]
S = list(map(tuple, parameters['S_coordinates']))
K = [(0, i) for i in range(k)]

def product(g, h):
    x, i = g
    y, j = h
    return ((x + powers[i] * y) % q, (i + j) % k)

shortcut_elements = set(K) | {product(a, b) for a in K for b in S} | {product(a, b) for a in S for b in K}
shortcut_labels = {x + q * i for x, i in shortcut_elements}

# Independent state BFS counts routes that actually visit at least one head.
head_route_distance = [[-1] * n for _ in range(2)]
head_route_distance[0][0] = 0
queue = deque([(0, 0)])
while queue:
    u, seen_head = queue.popleft()
    for v in adj[u]:
        next_seen = int(bool(seen_head) or v >= L + B)
        if head_route_distance[next_seen][v] < 0:
            head_route_distance[next_seen][v] = head_route_distance[seen_head][u] + 1
            queue.append((v, next_seen))
state_shortcuts = {v for v in range(L) if 0 <= head_route_distance[1][v] <= 5}
assert state_shortcuts == shortcut_labels
full_within_five = [v for v in range(L) if 0 <= full_distance[v] <= 5]
no_head_shortcut = [v for v in full_within_five if v not in shortcut_labels]
counterexamples = [v for v in no_head_shortcut if leaf_distance[v] < 0 or leaf_distance[v] > 5]
assert counterexamples
target = counterexamples[0]
path = [target]
while path[-1] != 0:
    path.append(parent[path[-1]])
path.reverse()

def kind(v): return 'leaf' if v < L else 'block' if v < L + B else 'head'

def coordinates(v):
    if v < L:
        return {'x': v % q, 'quotient': v // q}
    if v < L + B:
        return {'x': (v - L) % q, 'block_index': (v - L) // q}
    return {'x': v - L - B}

assert len(path) - 1 == full_distance[target] <= 5
assert all(v < L + B for v in path)
assert any(L <= v < L + B for v in path)
assert all(v in adj[u] for u, v in zip(path, path[1:]))
result = {
    'status': 'EXISTING_GRAPH_COUNTEREXAMPLE_FOUND',
    'source': 'research/ddp/m2_coset_tower/q41_search/search.best.edges',
    'root_leaf': 0, 'target_leaf': target, 'target_coordinates': coordinates(target),
    'full_graph_distance': full_distance[target], 'leaf_only_distance': leaf_distance[target],
    'minimum_route_length_visiting_a_head': head_route_distance[1][target],
    'full_shortest_path': path,
    'full_shortest_path_vertex_types': [kind(v) for v in path],
    'full_shortest_path_coordinates': [coordinates(v) for v in path],
    'path_uses_block_but_no_head': True,
    'no_length_at_most_five_route_visits_head': True,
    'head_shortcut_set_formula': 'K union K*S union S*K, K={(0,i):i in C20}',
    'head_shortcut_formula_exactly_matches_seen_head_state_BFS': True,
    'head_shortcut_leaf_target_count': len(shortcut_labels),
    'all_full_graph_radius_five_leaf_target_count': len(full_within_five),
    'full_radius_five_leaf_targets_without_head_shortcut_count': len(no_head_shortcut),
    'among_them_leaf_only_distance_greater_than_five_count': len(counterexamples),
    'head_shortcut_leaf_targets': sorted(shortcut_labels),
    'full_radius_five_leaf_targets_without_head_shortcut': no_head_shortcut,
    'counterexample_leaf_targets': counterexamples,
    'counterexample_leaf_only_distance_histogram': dict(sorted(Counter(leaf_distance[v] for v in counterexamples).items())),
    'cpu_seconds': time.process_time() - START,
    'scope': 'Refutes only the asserted leaf-only-or-head-shortcut dichotomy. No claim about the separate numerical q<=31 conjecture; no new graph or search.',
}
(OUT / 'REVIEW_COUNTEREXAMPLE.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({key: value for key, value in result.items() if key not in ('head_shortcut_leaf_targets', 'full_radius_five_leaf_targets_without_head_shortcut', 'counterexample_leaf_targets')}, indent=2))
