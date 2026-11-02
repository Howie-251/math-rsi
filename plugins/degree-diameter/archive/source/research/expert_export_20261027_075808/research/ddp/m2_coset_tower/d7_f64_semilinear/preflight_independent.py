"""Independently reconstruct and check exactly the two saved semilinear samples."""
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
CHECKER = PROJECT / 'computations/ddp/verify_graph'
FIRST_PAIRS = [
    [(1, 1, 0), (2, 0, 1), (3, 3, 1)],
    [(1, 7, 1), (0, 1, 0), (2, 5, 1)],
]


def field_mul(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= 0x43
    return value


def field_pow(a, n):
    result = 1
    while n:
        if n & 1:
            result = field_mul(result, a)
        a = field_mul(a, a)
        n >>= 1
    return result


R = [field_pow(8, j) for j in range(21)]
FROB = [field_pow(x, 8) for x in range(64)]


def multiply(left, right):
    x, i, e = left
    y, j, f = right
    return (x ^ field_mul(R[i], FROB[y] if e else y),
            (i + (8 if e else 1) * j) % 21, e ^ f)


def inverse(element):
    x, i, e = element
    j = (-(8 if e else 1) * i) % 21
    return (field_mul(R[j], FROB[x] if e else x), j, e)


def leaf_label(element):
    x, i, e = element
    return x + 64 * (i + 21 * e)


def block_label(element):
    x, i, _ = element
    return 2688 + x + 64 * (i % 7)


def product_sets(left, right):
    return {multiply(a, b) for a in left for b in right}


def bfs(adjacency, root):
    distance = [-1] * len(adjacency)
    distance[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                queue.append(v)
    return distance


identity = (0, 0, 0)
H = {(0, 7 * j, e) for j in range(3) for e in range(2)}
K = {(0, i, e) for i in range(21) for e in range(2)}
assert len(set(R)) == 21 and field_pow(8, 21) == 1
results = []
for number, pairs in enumerate(FIRST_PAIRS):
    stem = OUT / f'preflight_{number}'
    saved = json.loads(stem.with_suffix('.json').read_text())
    generators = set(pairs) | {inverse(a) for a in pairs}
    assert len(generators) == 6 and identity not in generators
    assert generators == set(map(tuple, saved['S_coordinates']))
    assert sorted(map(leaf_label, generators)) == sorted(saved['S_ids'])
    assert all(multiply(a, inverse(a)) == identity and
               multiply(inverse(a), a) == identity for a in generators)

    expected_edges = set()
    for e in range(2):
        for i in range(21):
            for x in range(64):
                element = (x, i, e)
                u = leaf_label(element)
                for s in generators:
                    v = leaf_label(multiply(element, s))
                    assert u != v
                    expected_edges.add(tuple(sorted((u, v))))
                expected_edges.add((u, block_label(element)))
    for b in range(7):
        for x in range(64):
            expected_edges.add((2688 + x + 64 * b, 3136 + x))

    tokens = list(map(int, stem.with_suffix('.edges').read_text().split()))
    n, m = tokens[:2]
    assert (n, m) == (3200, 11200) and len(tokens) == 2 + 2 * m
    edge_list = [tuple(sorted(pair)) for pair in zip(tokens[2::2], tokens[3::2])]
    actual_edges = set(edge_list)
    assert len(actual_edges) == m and all(0 <= u < v < n for u, v in edge_list)
    assert actual_edges == expected_edges
    adjacency = [[] for _ in range(n)]
    for u, v in edge_list:
        adjacency[u].append(v)
        adjacency[v].append(u)
    assert set(map(len, adjacency)) == {7}

    roots = []
    root_distances = []
    for name, root in [('leaf', 0), ('block', 2688), ('head', 3136)]:
        distance = bfs(adjacency, root)
        assert -1 not in distance
        root_distances.append(distance)
        roots.append({
            'type': name, 'label': root, 'missing': sum(d > 5 for d in distance),
            'distance_histogram': dict(sorted(Counter(distance).items())),
            'missing_by_target_layer': {
                'leaf': sum(d > 5 for d in distance[:2688]),
                'block': sum(d > 5 for d in distance[2688:3136]),
                'head': sum(d > 5 for d in distance[3136:]),
            },
        })
    root_missing = [root['missing'] for root in roots]
    assert root_missing == saved['root_missing_leaf_block_head']
    weighted_bad = sum(weight * count for weight, count in
                       zip([2688, 448, 64], root_missing)) // 2
    assert weighted_bad == saved['bad_unordered_pairs']

    words = [{identity}]
    for _ in range(3):
        words.append(words[-1] | product_sets(words[-1], generators))
    term1 = product_sets(product_sets(H, words[3]), H)
    term2 = product_sets(product_sets(K, words[1]), H)
    term3 = product_sets(product_sets(H, words[1]), K)
    predicted_blocks = {block_label(a) for a in term1 | term2 | term3}
    actual_blocks = {u for u in range(2688, 3136) if root_distances[1][u] <= 5}
    masks = [sum(1 << x for x in range(64) if 2688 + x + 64 * b in actual_blocks)
             for b in range(7)]
    assert predicted_blocks == actual_blocks
    assert masks == saved['BB_masks']
    assert 448 - len(actual_blocks) == saved['BB_missing']

    process = subprocess.run([str(CHECKER), str(stem.with_suffix('.edges')), '7', '5'],
                             capture_output=True, text=True)
    assert process.returncode in (0, 1), process.stderr
    complete = json.loads(process.stdout)
    assert complete['roots_checked'] == 3200
    assert complete['bad_unordered_pairs'] == weighted_bad
    assert complete['unreachable_unordered_pairs'] == 0
    assert complete['min_degree'] == complete['max_degree'] == 7
    (OUT / f'preflight_{number}.independent_verify.json').write_text(
        json.dumps(complete, indent=2) + '\n')
    results.append({
        'sample': number, 'input_edges': stem.with_suffix('.edges').name,
        'generators': sorted(generators), 'n': n, 'm': m,
        'independently_reconstructed_edges_exactly_match': True,
        'missing_expected_edges': [], 'unexpected_saved_edges': [],
        'simple': True, 'degree': 7, 'connected': True,
        'three_roots': roots, 'weighted_bad_unordered_pairs': weighted_bad,
        'full_graph_check': complete,
        'BB_target_count': 448, 'BB_missing': 448 - len(actual_blocks),
        'BB_formula': 'H W3 H union K W1 H union H W1 K',
        'word_ball_sizes': list(map(len, words)),
        'BB_group_term_sizes': list(map(len, [term1, term2, term3])),
        'BB_masks': masks, 'all_saved_masks_match_BFS': True,
        'BB_formula_and_BFS_match_all_targets': True,
        'block_root_to_blocks_distances': root_distances[1][2688:3136],
    })

children = resource.getrusage(resource.RUSAGE_CHILDREN)
result = {
    'status': 'COMPLETE_TWO_SAVED_SAMPLES_NO_SEARCH',
    'field': 'F2[t]/(t^6+t+1), encoding t=2, r=8',
    'group_law': '(x,i,e)(y,j,f)=(x XOR r^i*y^(8^e), i+8^e*j mod21, e XOR f)',
    'sample_results': results,
    'python_cpu_seconds': time.process_time() - START,
    'checker_cpu_seconds': children.ru_utime + children.ru_stime
        - CHILD_START.ru_utime - CHILD_START.ru_stime,
    'scope': 'Only the two specified saved samples: exact edge-set reconstruction, three root BFS, BB formula/masks, one generic full-root check each.',
}
(OUT / 'preflight.independent_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({
    'status': result['status'],
    'samples': [{k: s[k] for k in ['sample', 'weighted_bad_unordered_pairs', 'BB_missing',
                                  'independently_reconstructed_edges_exactly_match']}
                | {'diameter': s['full_graph_check']['diameter'],
                   'root_missing': [r['missing'] for r in s['three_roots']]}
                for s in results],
    'python_cpu_seconds': result['python_cpu_seconds'],
    'checker_cpu_seconds': result['checker_cpu_seconds'],
}, indent=2))
