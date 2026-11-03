"""One specified AGL(1,7) sample; independent edges, full BFS, nonnormal BB."""
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
structure = json.loads((OUT / 'profile_structure.json').read_text())
S = set(parameters['S'])
assert S == set(saved['S']) == {21, 24, 1887, 2532, 1970, 2331}


def fm(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return result


def fp(a, n):
    result = 1
    for _ in range(n):
        result = fm(result, a)
    return result


Z = [fp(2, i) for i in range(7)]
K = [(a, b, e) for e in range(2) for b in range(3) for a in range(7)]
KI = {k: i for i, k in enumerate(K)}


def action(k, x):
    a, b, e = k
    u, v = x % 8, x // 8
    if e:
        u, v = v, u
    return fm(Z[a], fp(u, 2**b)) + 8 * fm(Z[-a % 7], fp(v, 2**b))


ACTION = [[action(k, x) for x in range(64)] for k in K]
KMUL = [[KI[((a + (-1 if e else 1) * 2**b * c) % 7, (b+d) % 3, e ^ f)]
         for c, d, f in K] for a, b, e in K]
KINV = [KI[(-(-1 if e else 1) * 2**(-b % 3) * a % 7, -b % 3, e)] for a, b, e in K]
LINEAR_K = {((-1 if e else 1) * 2**b) % 7: KI[(0, b, e)] for b in range(3) for e in range(2)}
assert [LINEAR_K[a] for a in range(1, 7)] == structure['multiplicative_L_K_codes'][1:]


def multiply(g, h):
    x, k = g % 64, g // 64
    y, l = h % 64, h // 64
    return (x ^ ACTION[k][y]) + 64 * KMUL[k][l]


def inverse(g):
    x, k = g % 64, g // 64
    return ACTION[KINV[k]][x] + 64 * KINV[k]


def linear(coefficient, x):
    return ACTION[LINEAR_K[coefficient]][x]


def translation(offset, x):
    return ACTION[KI[(offset % 7, 0, 0)]][x]


assert len(S) == 6 and 0 not in S and {inverse(s) for s in S} == S
assert sorted(s for s in S if inverse(s) == s) == [21, 24]
assert all(multiply(s, inverse(s)) == multiply(inverse(s), s) == 0 for s in S)
expected_edges = set()
for g in range(2688):
    for s in S:
        neighbor = multiply(g, s)
        assert g != neighbor
        expected_edges.add(tuple(sorted((g, neighbor))))
    x, k = g % 64, g // 64
    expected_edges.add((g, 2688 + x + 64 * K[k][0]))
for a in range(7):
    for x in range(64):
        expected_edges.add((2688 + x + 64 * a, 3136 + x))

tokens = list(map(int, (OUT / 'preflight.edges').read_text().split()))
n, m = tokens[:2]
assert (n, m) == (3200, 11200) and len(tokens) == 2 + 2 * m
edge_list = [tuple(sorted(pair)) for pair in zip(tokens[2::2], tokens[3::2])]
actual_edges = set(edge_list)
assert len(actual_edges) == m and all(0 <= u < v < n for u, v in edge_list)
assert actual_edges == expected_edges
adj = [[] for _ in range(n)]
for u, v in edge_list:
    adj[u].append(v)
    adj[v].append(u)
assert set(map(len, adj)) == {7}

roots = []
distances = []
layers = [('leaf', 0, 2688), ('block', 2688, 3136), ('head', 3136, 3200)]
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
weighted_bad = sum(size * r['missing'] for size, r in zip([2688, 448, 64], roots)) // 2
assert weighted_bad == saved['bad_unordered_pairs']

words = [{0}]
for _ in range(3):
    words.append(words[-1] | {multiply(w, s) for w in words[-1] for s in S})
R0 = {linear(a, w % 64) for w in words[3] if K[w // 64][0] == 0 for a in range(1, 7)}
R1 = {linear(pow(K[w // 64][0], -1, 7), w % 64) for w in words[3] if K[w // 64][0] != 0}
P = {linear(a, s % 64) for s in words[1] for a in range(1, 7)}
Q = {linear(a, translation(-K[s // 64][0], s % 64)) for s in words[1] for a in range(1, 7)}
M0 = R0 | P | Q
M1 = R1 | P | {translation(1, q) for q in Q}
predicted_by_a = [M0] + [{linear(a, x) for x in M1} for a in range(1, 7)]
actual_by_a = [{x for x in range(64) if distances[1][2688 + x + 64*a] <= 5} for a in range(7)]
assert all(predicted == actual for predicted, actual in zip(predicted_by_a, actual_by_a))
BB_missing = sum(64 - len(reachable) for reachable in actual_by_a)
assert BB_missing == (64-len(M0)) + 6*(64-len(M1)) == 25
two_masks = [sum(1 << x for x in M0), sum(1 << x for x in M1)]
assert two_masks == saved['BB_masks_M0_M1']
BB_mismatches = [{'x': x, 'a': a} for a in range(7) for x in range(64)
                 if (x in predicted_by_a[a]) != (x in actual_by_a[a])]
assert not BB_mismatches

process = subprocess.run([str(PROJECT / 'computations/ddp/verify_graph'),
                          str(OUT / 'preflight.edges'), '7', '5'], capture_output=True, text=True)
assert process.returncode in (0, 1), process.stderr
complete = json.loads(process.stdout)
assert complete['roots_checked'] == 3200
assert complete['bad_unordered_pairs'] == weighted_bad
assert complete['unreachable_unordered_pairs'] == 0
assert complete['min_degree'] == complete['max_degree'] == 7
(OUT / 'preflight.independent_verify.json').write_text(json.dumps(complete, indent=2) + '\n')
children = resource.getrusage(resource.RUSAGE_CHILDREN)
result = {
    'status': 'COMPLETE_ONE_SAVED_D7_NONNORMAL_H_SAMPLE_NO_SEARCH',
    'input': 'preflight.edges', 'generator_codes': sorted(S),
    'independent_edges_exactly_equal': True, 'n': n, 'm': m,
    'simple': True, 'connected': True, 'degree': 7,
    'representative_roots': roots, 'weighted_bad_unordered_pairs': weighted_bad,
    'full_graph_check': complete,
    'BB_formula_source': '../NONNORMAL_BLOCK_CRITERIA.md',
    'BB_base_field': 'F7; scalar inverse and translation negation are mod7, distinct from A=F8^2 arithmetic',
    'BB_old_normal_H_formula_used': False,
    'BB_word_ball_sizes': list(map(len, words)),
    'BB_R0': sorted(R0), 'BB_R1': sorted(R1), 'BB_P': sorted(P), 'BB_Q': sorted(Q),
    'BB_M0': sorted(M0), 'BB_M1': sorted(M1),
    'BB_set_sizes': {'R0':len(R0), 'R1':len(R1), 'P':len(P), 'Q':len(Q), 'M0':len(M0), 'M1':len(M1)},
    'BB_masks_M0_M1': two_masks, 'BB_saved_two_masks_exactly_match': True,
    'BB_target_count': 448, 'BB_missing': BB_missing,
    'BB_all_targets_pointwise_match': True, 'BB_mismatches': BB_mismatches,
    'BB_predicted_masks_by_a': [sum(1 << x for x in a) for a in predicted_by_a],
    'BB_BFS_masks_by_a': [sum(1 << x for x in a) for a in actual_by_a],
    'BB_BFS_distances_in_label_order': distances[1][2688:3136],
    'python_cpu_seconds': time.process_time() - START,
    'checker_cpu_seconds': children.ru_utime + children.ru_stime - CHILD_START.ru_utime - CHILD_START.ru_stime,
    'scope': 'One specified saved sample only; independent expansion, three root BFS and one generic full3200root check. No other graph or generator search.',
}
(OUT / 'preflight.independent_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'n', 'm', 'independent_edges_exactly_equal',
                                       'weighted_bad_unordered_pairs', 'BB_set_sizes', 'BB_missing',
                                       'BB_all_targets_pointwise_match', 'python_cpu_seconds',
                                       'checker_cpu_seconds']}, indent=2))
print(json.dumps(complete, indent=2))
