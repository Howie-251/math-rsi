"""Exactly one saved AGL(1,8) sample; independent action/edges and nonnormal BB."""
import json
import resource
import subprocess
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
CHILD_START = resource.getrusage(resource.RUSAGE_CHILDREN)
OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[3]
parameters = json.loads((OUT / 'preflight.parameters.json').read_text())
saved = json.loads((OUT / 'preflight.json').read_text())
structure = json.loads((OUT / 'structure.json').read_text())
S = set(parameters['S'])
assert S == set(saved['S']) == {255, 263, 254, 1153, 4752, 1291, 4237}


def fm(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return value


FIELD_INV = {a: next(b for b in range(1, 8) if fm(a, b) == 1) for a in range(1, 8)}
K = [(a, b) for a in range(1, 8) for b in range(8)]
KI = {k: i for i, k in enumerate(K)}
MASKS = [(x << 1) | (x.bit_count() % 2) for x in range(128)]
assert MASKS == structure['A_masks']
assert K == list(map(tuple, structure['K_coordinates']))


def permute_mask(mask, k):
    a, b = k
    image = 0
    for coordinate in range(8):
        if mask & (1 << coordinate):
            image |= 1 << (fm(a, coordinate) ^ b)
    return image


ACTION = [[permute_mask(mask, k) >> 1 for mask in MASKS] for k in K]
KMUL = [[KI[(fm(a, c), b ^ fm(a, d))] for c, d in K] for a, b in K]
KINV = [KI[(FIELD_INV[a], fm(FIELD_INV[a], b))] for a, b in K]


def multiply(g, h):
    x, k = g % 128, g // 128
    y, l = h % 128, h // 128
    return (x ^ ACTION[k][y]) + 128 * KMUL[k][l]


def inverse(g):
    x, k = g % 128, g // 128
    return ACTION[KINV[k]][x] + 128 * KINV[k]


def linear(a, x):
    return ACTION[KI[(a, 0)]][x]


def translation(b, x):
    return ACTION[KI[(1, b)]][x]


assert len(S) == 7 and 0 not in S and {inverse(s) for s in S} == S
assert [s for s in sorted(S) if inverse(s) == s] == [254, 255, 263]
assert all(multiply(s, inverse(s)) == multiply(inverse(s), s) == 0 for s in S)
expected_edges = set()
for g in range(7168):
    for s in S:
        neighbor = multiply(g, s)
        assert g != neighbor
        expected_edges.add(tuple(sorted((g, neighbor))))
    x, k = g % 128, g // 128
    expected_edges.add((g, 7168 + x + 128 * K[k][1]))
for b in range(8):
    for x in range(128):
        expected_edges.add((7168 + x + 128 * b, 8192 + x))

tokens = list(map(int, (OUT / 'preflight.edges').read_text().split()))
n, m = tokens[:2]
assert (n, m) == (8320, 33280) and len(tokens) == 2 + 2 * m
edge_list = [tuple(sorted(pair)) for pair in zip(tokens[2::2], tokens[3::2])]
actual_edges = set(edge_list)
assert len(actual_edges) == m and all(0 <= u < v < n for u, v in edge_list)
assert actual_edges == expected_edges
adj = [[] for _ in range(n)]
for u, v in edge_list:
    adj[u].append(v)
    adj[v].append(u)
assert set(map(len, adj)) == {8}

roots = []
distances = []
layers = [('leaf', 0, 7168), ('block', 7168, 8192), ('head', 8192, 8320)]
for layer, root, _ in layers:
    dist = [-1] * n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert -1 not in dist
    distances.append(dist)
    roots.append({'layer': layer, 'root': root, 'missing': sum(d > 5 for d in dist),
                  'distance_histogram': dict(sorted(Counter(dist).items())),
                  'missing_by_target_layer': [sum(d > 5 for d in dist[lo:hi]) for _, lo, hi in layers]})
assert [r['missing'] for r in roots] == saved['root_missing']
assert [r['missing_by_target_layer'] for r in roots] == saved['root_missing_by_target_layer']
weighted_bad = sum(size * r['missing'] for size, r in zip([7168, 1024, 128], roots)) // 2
assert weighted_bad == saved['bad_unordered_pairs']

words = [{0}]
for _ in range(3):
    words.append(words[-1] | {multiply(w, s) for w in words[-1] for s in S})
R0 = {linear(a, w % 128) for w in words[3] if K[w // 128][1] == 0 for a in range(1, 8)}
R1 = {linear(FIELD_INV[K[w // 128][1]], w % 128) for w in words[3] if K[w // 128][1] != 0}
P = {linear(a, s % 128) for s in words[1] for a in range(1, 8)}
Q = {linear(a, translation(K[s // 128][1], s % 128)) for s in words[1] for a in range(1, 8)}
M0 = R0 | P | Q
M1 = R1 | P | {translation(1, q) for q in Q}
predicted_by_b = [M0] + [{linear(b, x) for x in M1} for b in range(1, 8)]
actual_by_b = [{x for x in range(128) if distances[1][7168 + x + 128*b] <= 5} for b in range(8)]
assert all(predicted == actual for predicted, actual in zip(predicted_by_b, actual_by_b))
BB_missing = sum(128 - len(reachable) for reachable in actual_by_b)
assert BB_missing == (128-len(M0)) + 7*(128-len(M1)) == 217
BB_mismatches = [{'x': x, 'b': b} for b in range(8) for x in range(128)
                 if (x in predicted_by_b[b]) != (x in actual_by_b[b])]
assert not BB_mismatches

process = subprocess.run([str(PROJECT / 'computations/ddp/verify_graph'),
                          str(OUT / 'preflight.edges'), '8', '5'], capture_output=True, text=True)
assert process.returncode in (0, 1), process.stderr
complete = json.loads(process.stdout)
assert complete['roots_checked'] == 8320
assert complete['bad_unordered_pairs'] == weighted_bad
assert complete['unreachable_unordered_pairs'] == 0
assert complete['min_degree'] == complete['max_degree'] == 8
(OUT / 'preflight.independent_verify.json').write_text(json.dumps(complete, indent=2) + '\n')
children = resource.getrusage(resource.RUSAGE_CHILDREN)
result = {
    'status': 'COMPLETE_ONE_SAVED_D8_SAMPLE_NO_SEARCH',
    'input': 'preflight.edges', 'generator_codes': sorted(S),
    'group_arithmetic': 'F8 poly0b1011; K(a,b)(c,d)=(ac,b+ad); G(x,k)(y,l)=(x+action(k)y,kl)',
    'independent_edges_exactly_equal': True, 'n': n, 'm': m,
    'simple': True, 'connected': True, 'degree': 8,
    'representative_roots': roots, 'weighted_bad_unordered_pairs': weighted_bad,
    'full_graph_check': complete,
    'BB_formula_source': '../NONNORMAL_BLOCK_CRITERIA.md',
    'BB_old_normal_H_formula_used': False,
    'BB_word_ball_sizes': list(map(len, words)),
    'BB_R0': sorted(R0), 'BB_R1': sorted(R1), 'BB_P': sorted(P), 'BB_Q': sorted(Q),
    'BB_M0': sorted(M0), 'BB_M1': sorted(M1),
    'BB_set_sizes': {'R0':len(R0), 'R1':len(R1), 'P':len(P), 'Q':len(Q), 'M0':len(M0), 'M1':len(M1)},
    'BB_target_count': 1024, 'BB_missing': BB_missing,
    'BB_all_targets_pointwise_match': True, 'BB_mismatches': BB_mismatches,
    'BB_predicted_masks_by_b': [sum(1 << x for x in a) for a in predicted_by_b],
    'BB_BFS_masks_by_b': [sum(1 << x for x in a) for a in actual_by_b],
    'BB_BFS_distances_in_label_order': distances[1][7168:8192],
    'python_cpu_seconds': time.process_time() - START,
    'checker_cpu_seconds': children.ru_utime + children.ru_stime - CHILD_START.ru_utime - CHILD_START.ru_stime,
    'scope': 'One specified saved sample only; independent expansion, three root BFS and one generic full8320root check. No other graph or generator search.',
}
(OUT / 'preflight.independent_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'n', 'm', 'independent_edges_exactly_equal',
                                       'weighted_bad_unordered_pairs', 'BB_set_sizes', 'BB_missing',
                                       'BB_all_targets_pointwise_match', 'python_cpu_seconds',
                                       'checker_cpu_seconds']}, indent=2))
print(json.dumps(complete, indent=2))
