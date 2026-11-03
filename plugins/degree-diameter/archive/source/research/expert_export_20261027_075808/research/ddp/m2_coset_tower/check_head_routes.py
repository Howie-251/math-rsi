"""Exact set comparison of proposed head routing formulas on three saved graphs."""
import json
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]

def check(name, path, q, degree, r, generators, arithmetic, label_style):
    h = degree - 1
    k = degree * h
    if arithmetic == 'F25':
        def add(x, y):
            return (x % 5 + y % 5) % 5 + 5 * ((x // 5 + y // 5) % 5)
        def mul(x, y):
            a, b, c, d = x % 5, x // 5, y % 5, y // 5
            return (a * c + 2 * b * d) % 5 + 5 * ((a * d + b * c) % 5)
    else:
        def add(x, y): return (x + y) % q
        def mul(x, y): return x * y % q
    powers = [1]
    for _ in range(1, k):
        powers.append(mul(powers[-1], r))
    assert mul(powers[-1], r) == 1 and len(set(powers)) == k
    S = set(map(tuple, generators))
    def product(g, v):
        x, i = g
        y, j = v
        return add(x, mul(powers[i], y)), (i + j) % k
    def rho(g):
        x, i = g
        return mul(powers[-i % k], x)
    if label_style == 'source650':
        def leaf(x, i): return x + q * i
        def block(x, b): return q * k + degree * x + b
    elif label_style == 'q41':
        def leaf(x, i): return x + q * i
        def block(x, b): return q * k + x + q * b
    else:
        def leaf(x, i): return k * x + i
        def block(x, b): return q * k + degree * x + b
    def head(x): return q * k + q * degree + x
    data = list(map(int, (ROOT / path).read_text().split()))
    n, m = data[:2]
    edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
    assert n == q * (k + degree + 1) and len(edges) == m
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    assert {leaf(x, i) for x, i in S} == {v for v in adj[leaf(0, 0)] if v < q * k}
    distance = [-1] * n
    root = head(0)
    distance[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                queue.append(v)
    assert -1 not in distance
    words = [{(0, 0)}]
    for depth in range(1, 4):
        words.append(words[-1] | {product(w, s) for w in words[-1] for s in S})
    U = {powers[degree * j] for j in range(h)}
    assert len(U) == h
    rhoS = {rho(s) for s in S}
    TL = {rho(w) for w in words[3]} | {mul(x, u) for x in rhoS for u in U}
    TB = {mul(rho(w), u) for w in words[2] for u in U}
    TH = {0} | {mul(s[0], u) for s in S for u in powers}
    predictions = {
        'leaf': {leaf(x, i) for x in range(q) for i in range(k) if rho((x, i)) in TL},
        'block': {block(x, b) for x in range(q) for b in range(degree) if mul(x, powers[-b % k]) in TB},
        'head': {head(x) for x in range(q) if x in TH},
    }
    layers = {'leaf': set(range(q * k)), 'block': set(range(q * k, q * k + q * degree)),
              'head': set(range(q * k + q * degree, n))}
    comparison = {}
    for kind, labels in layers.items():
        actual = {v for v in labels if distance[v] <= 5}
        predicted = predictions[kind]
        comparison[kind] = {
            'total_targets': len(labels), 'predicted_reachable_count': len(predicted),
            'bfs_reachable_count': len(actual), 'missing_count': len(labels - actual),
            'sets_exactly_equal': actual == predicted,
            'predicted_reachable_labels': sorted(predicted), 'bfs_reachable_labels': sorted(actual),
            'predicted_only_labels': sorted(predicted - actual), 'bfs_only_labels': sorted(actual - predicted),
            'bfs_missing_labels': sorted(labels - actual),
        }
    result = {
        'name': name, 'source': path, 'arithmetic': arithmetic, 'q': q, 'degree': degree,
        'h': h, 'k': k, 'r_encoding': r, 'generators': sorted(S), 'label_style': label_style,
        'head_root': root, 'vertices': n, 'word_ball_sizes_W0_to_W3': list(map(len, words)),
        'U': sorted(U), 'rho_S': sorted(rhoS), 'T_leaf': sorted(TL), 'T_block': sorted(TB), 'T_head': sorted(TH),
        'head_root_distance_histogram': dict(sorted(Counter(distance).items())),
        'head_root_missing_total': sum(d > 5 for d in distance),
        'target_layer_comparisons': comparison,
        'all_three_layer_sets_exactly_equal': all(v['sets_exactly_equal'] for v in comparison.values()),
    }
    return result

base = json.loads((ROOT / 'research/ddp/source650_hierarchy/algebraic_reconstruction.json').read_text())
q41 = json.loads((OUT / 'q41_search/search.best.json').read_text())
f25 = json.loads((OUT / 'd4_q25/best.json').read_text())
results = [
    check('source650', 'research/ddp/m1_degree5_transfer/rithwik650_source.edges', 25, 5, 2,
          [g['element'] for g in base['generators']], 'Z25', 'source650'),
    check('q41_best', 'research/ddp/m2_coset_tower/q41_search/search.best.edges', 41, 5, q41['r'],
          q41['S_coordinates'], 'F41', 'q41'),
    check('d4_F25_best', 'research/ddp/m2_coset_tower/d4_q25/best.edges', 25, 4, 6,
          [f25['involution'], f25['a'], f25['a_inverse']], 'F25', 'd4_F25'),
]
output = {'status': 'COMPLETE_POINTWISE_SET_COMPARISON',
          'all_graphs_all_layers_exactly_equal': all(r['all_three_layer_sets_exactly_equal'] for r in results),
          'formulas': {'leaf': 'rho(W3) union rho(S)*U', 'block': 'rho(W2)*U', 'head': '{0} union S_x*<r>'},
          'cpu_seconds': time.process_time() - START, 'graphs': results}
(OUT / 'HEAD_ROUTE_CHECK.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({k: v for k, v in output.items() if k != 'graphs'}, indent=2))
for result in results:
    print(result['name'], json.dumps({
        'W_sizes': result['word_ball_sizes_W0_to_W3'],
        'T_sizes': [len(result[k]) for k in ('T_leaf', 'T_block', 'T_head')],
        'head_root': result['head_root'], 'head_missing': result['head_root_missing_total'],
        'layer_matches': {k: {field: data[field] for field in ('sets_exactly_equal', 'bfs_reachable_count', 'missing_count')}
                          for k, data in result['target_layer_comparisons'].items()},
    }))
