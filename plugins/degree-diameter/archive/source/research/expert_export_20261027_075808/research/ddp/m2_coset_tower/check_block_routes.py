"""Find an omitted target-head route in a saved graph; stop after first witness."""
import json
import time
from collections import deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]

def check(name, source, q, d, r, generators, labels):
    k, h = d * (d - 1), d - 1
    L, B = q * k, q * d
    power = [pow(r, i, q) for i in range(k)]
    S = set(map(tuple, generators))
    def product(g, v):
        x, i = g
        y, j = v
        return (x + power[i] * y) % q, (i + j) % k
    def rho(g):
        x, i = g
        return power[-i % k] * x % q
    def block(x, b):
        return L + d * x + b if labels == 'source650' else L + x + q * b
    def decode(vertex):
        if vertex < L:
            return {'type': 'leaf', 'x': vertex % q, 'quotient': vertex // q}
        if vertex < L + B:
            z = vertex - L
            x, b = divmod(z, d) if labels == 'source650' else (z % q, z // q)
            return {'type': 'block', 'x': x, 'block_index': b}
        return {'type': 'head', 'x': vertex - L - B}
    data = list(map(int, (ROOT / source).read_text().split()))
    n, m = data[:2]
    assert n == L + B + q
    edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
    assert len(edges) == m
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for neighbors in adj:
        neighbors.sort()
    root = block(0, 0)
    distance, parent = [-1] * n, [-1] * n
    distance[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
    assert -1 not in distance
    W = {(0, 0)}
    for _ in range(3):
        W |= {product(g, s) for g in W for s in S}
    U = {power[d * j] for j in range(h)}
    R1 = {0} | {rho(s) for s in S}
    common = {u * x % q for u in U for x in R1}
    Sx = {s[0] for s in S}
    bad_sets, good_sets, bfs_sets = {}, {}, {}
    predicted_bad, predicted_good = set(), set()
    for b in range(d):
        restricted = {rho(w) for w in W if w[1] % d == b}
        Tbad = common | {u * x % q for u in U for x in restricted}
        extra = {power[-b % k] * u * x % q for u in U for x in Sx}
        Tgood = Tbad | extra
        actual = {power[-b % k] * x % q for x in range(q) if distance[block(x, b)] <= 5}
        bad_sets[str(b)] = sorted(Tbad)
        good_sets[str(b)] = sorted(Tgood)
        bfs_sets[str(b)] = sorted(actual)
        predicted_bad.update(block(x, b) for x in range(q) if power[-b % k] * x % q in Tbad)
        predicted_good.update(block(x, b) for x in range(q) if power[-b % k] * x % q in Tgood)
    bfs_blocks = {v for v in range(L, L + B) if distance[v] <= 5}
    omitted = sorted(bfs_blocks - predicted_bad)
    witness = None
    if omitted:
        target = omitted[0]
        path = [target]
        while path[-1] != root:
            path.append(parent[path[-1]])
        path.reverse()
        target_info = decode(target)
        b, x = target_info['block_index'], target_info['x']
        witness = {
            'root_block': root, 'root_coordinates': decode(root), 'target_block': target,
            'target_coordinates': target_info, 'normalized_target': power[-b % k] * x % q,
            'full_graph_distance': distance[target], 'shortest_full_path': path,
            'shortest_full_path_coordinates': [decode(v) for v in path],
            'target_head_vertex': L + B + x,
            'shortest_path_visits_target_head': L + B + x in path,
            'Tbad_omits_target': target not in predicted_bad,
            'Tgood_contains_target': target in predicted_good,
        }
    return {
        'name': name, 'source': source, 'arithmetic': 'Z25' if q == 25 else f'F{q}',
        'q': q, 'degree': d, 'k': k, 'r': r, 'generators': sorted(S),
        'root_block': root, 'U': sorted(U), 'R1_equals_rho_W1': sorted(R1),
        'word_ball_W3_size': len(W), 'normalized_Tbad_by_b': bad_sets,
        'normalized_Tgood_by_b': good_sets, 'normalized_BFS_by_b': bfs_sets,
        'Tbad_predicted_block_labels': sorted(predicted_bad),
        'Tgood_predicted_block_labels': sorted(predicted_good),
        'BFS_reachable_block_labels': sorted(bfs_blocks),
        'Tbad_false_negative_labels': omitted,
        'Tbad_false_positive_labels': sorted(predicted_bad - bfs_blocks),
        'Tgood_false_negative_labels': sorted(bfs_blocks - predicted_good),
        'Tgood_false_positive_labels': sorted(predicted_good - bfs_blocks),
        'Tgood_matches_BFS_pointwise': predicted_good == bfs_blocks,
        'witness': witness,
    }

base = json.loads((ROOT / 'research/ddp/source650_hierarchy/algebraic_reconstruction.json').read_text())
cases = [('source650', 'research/ddp/m1_degree5_transfer/rithwik650_source.edges', 25, 5, 2,
          [g['element'] for g in base['generators']], 'source650')]
for name, subdir, degree in [('q41_best', 'q41_search', 5), ('d6_best', 'd6_q61', 6)]:
    params = json.loads((OUT / subdir / 'search.best.json').read_text())
    cases.append((name, f'research/ddp/m2_coset_tower/{subdir}/search.best.edges',
                  params['q'], degree, params['r'], params['S_coordinates'], 'q_first'))
results = []
for case in cases:
    result = check(*case)
    results.append(result)
    if result['witness'] is not None:
        break
output = {
    'status': 'EXISTING_GRAPH_COUNTEREXAMPLE_FOUND' if results[-1]['witness'] else 'NO_COUNTEREXAMPLE_IN_CHECKED_SAVED_GRAPHS',
    'R1_definition': 'rho(W1)={0} union rho(S)',
    'Tbad': 'U*R1 union U*rho({w in W3: quotient(w) mod d=b})',
    'Tgood_additional_term': 'r^(-b)*U*S_x',
    'checked_graph_count': len(results), 'stopped_on_first_actual_counterexample': results[-1]['witness'] is not None,
    'cpu_seconds': time.process_time() - START, 'graphs': results,
    'scope': 'Saved complete graphs only. Full BFS from block(0,0), pointwise target-block set comparison; no new graph or candidate search.',
}
(OUT / 'BLOCK_ROUTE_CHECK.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({k: v for k, v in output.items() if k != 'graphs'}, indent=2))
for result in results:
    print(json.dumps({
        'name': result['name'], 'Tbad_false_negative_count': len(result['Tbad_false_negative_labels']),
        'Tbad_false_positive_count': len(result['Tbad_false_positive_labels']),
        'Tgood_matches_BFS_pointwise': result['Tgood_matches_BFS_pointwise'], 'witness': result['witness'],
    }, indent=2))
