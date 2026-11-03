"""Check one saved triangle-head sample; preparation alone executes no graph work.

Run only after the parent confirms that all sample files are final:
    python independent_preflight.py [stem]
The default stem is preflight, relative to this script's directory.
"""
import json
import resource
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[3]
A_ORDER, K_ORDER = 147, 42
LEAVES, BLOCKS, HEADS, VERTICES = 6174, 882, 147, 7203
BLOCK_START, HEAD_START = 6174, 7056


def a_decode(x):
    return x % 7, (x // 7) % 7, x // 49


def a_encode(u, v, w):
    return (u % 7) + 7 * (v % 7) + 49 * (w % 3)


def a_add(x, y):
    u, v, w = a_decode(x)
    s, t, z = a_decode(y)
    return a_encode(u+s, v+t, w+z)


def a_negative(x):
    u, v, w = a_decode(x)
    return a_encode(-u, -v, -w)


def k_decode(k):
    return k % 7, k // 7


def k_multiply(k, l):
    b, j = k_decode(k)
    d, ell = k_decode(l)
    return (b + pow(4, j, 7)*d) % 7 + 7*((j+ell) % 6)


def k_inverse(k):
    b, j = k_decode(k)
    inverse_j = -j % 6
    return (-pow(4, inverse_j, 7)*b) % 7 + 7*inverse_j


def action(k, x):
    b, j = k_decode(k)
    u, v, w = a_decode(x)
    return a_encode(pow(3, 5*j, 7)*u + b*pow(3, j, 7)*v,
                    pow(3, j, 7)*v, w)


def bfs(adjacency, root):
    distances = [-1]*len(adjacency)
    distances[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distances[v] == -1:
                distances[v] = distances[u]+1
                queue.append(v)
    return distances


def is_missing(distance):
    return distance == -1 or distance > 5


def main():
    start = time.process_time()
    child_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    stem = OUT / (sys.argv[1] if len(sys.argv) > 1 else 'preflight')
    score_path = Path(str(stem)+'.json')
    saved = json.loads(score_path.read_text()) if score_path.exists() else {}
    parameter_path = Path(str(stem)+'.parameters.json')
    if not parameter_path.exists():
        parameter_path = score_path
    parameters = json.loads(parameter_path.read_text())

    def require_match(condition, stage, details):
        if not condition:
            Path(str(stem)+'.independent_mismatch.json').write_text(json.dumps({
                'status':'STOPPED_AT_ACTUAL_MISMATCH_NO_RERUN', 'stage':stage,
                'input_stem':stem.name, 'details':details,
            }, indent=2)+'\n')
            raise AssertionError(stage)

    S = set(parameters['S'])
    assert len(parameters['S']) == len(S) == 7
    assert 0 not in S and all(0 <= s < LEAVES for s in S)
    if 'S' in saved:
        assert S == set(saved['S'])

    # Independently derived arithmetic; no producer tables or caches are read.
    action_table = [[action(k, x) for x in range(A_ORDER)] for k in range(K_ORDER)]
    k_product = [[k_multiply(k, l) for l in range(K_ORDER)] for k in range(K_ORDER)]
    k_inverses = [k_inverse(k) for k in range(K_ORDER)]

    def multiply(g, h):
        x, k = g % A_ORDER, g // A_ORDER
        y, l = h % A_ORDER, h // A_ORDER
        return a_add(x, action_table[k][y]) + A_ORDER*k_product[k][l]

    def inverse(g):
        x, k = g % A_ORDER, g // A_ORDER
        inverse_k = k_inverses[k]
        return a_negative(action_table[inverse_k][x]) + A_ORDER*inverse_k

    assert {inverse(s) for s in S} == S
    assert all(multiply(s, inverse(s)) == multiply(inverse(s), s) == 0 for s in S)

    expected_edges = set()
    for g in range(LEAVES):
        for s in S:
            neighbor = multiply(g, s)
            assert g != neighbor
            expected_edges.add(tuple(sorted((g, neighbor))))
        x, k = g % A_ORDER, g // A_ORDER
        _, j = k_decode(k)
        expected_edges.add((g, BLOCK_START+x+A_ORDER*j))
    for j in range(6):
        for x in range(A_ORDER):
            expected_edges.add((BLOCK_START+x+A_ORDER*j, HEAD_START+x))
    triangle_edges = set()
    for u in range(7):
        for v in range(7):
            triangle = [HEAD_START+a_encode(u, v, w) for w in range(3)]
            for i, j in [(0,1), (0,2), (1,2)]:
                triangle_edges.add((triangle[i], triangle[j]))
    assert len(triangle_edges) == 147
    expected_edges |= triangle_edges

    edge_path = Path(str(stem)+'.edges')
    tokens = list(map(int, edge_path.read_text().split()))
    n, m = tokens[:2]
    assert (n, m) == (VERTICES, 28812) and len(tokens) == 2+2*m
    edge_list = [tuple(sorted(pair)) for pair in zip(tokens[2::2], tokens[3::2])]
    actual_edges = set(edge_list)
    assert len(actual_edges) == m and all(0 <= u < v < n for u, v in edge_list)
    require_match(actual_edges == expected_edges, 'independent_edge_set', {
        'missing_expected_edges':sorted(expected_edges-actual_edges),
        'unexpected_saved_edges':sorted(actual_edges-expected_edges),
    })
    assert {edge for edge in actual_edges if edge[0] >= HEAD_START} == triangle_edges
    adjacency = [[] for _ in range(n)]
    for u, v in edge_list:
        adjacency[u].append(v)
        adjacency[v].append(u)
    assert set(map(len, adjacency)) == {8}

    layers = [('leaf', 0, BLOCK_START), ('block', BLOCK_START, HEAD_START),
              ('head', HEAD_START, VERTICES)]
    roots = []
    root_distances = []
    for layer, root, _ in layers:
        distances = bfs(adjacency, root)
        root_distances.append(distances)
        roots.append({
            'layer': layer, 'root': root,
            'missing': sum(is_missing(d) for d in distances),
            'unreachable': distances.count(-1),
            'distance_histogram': dict(sorted(Counter(distances).items())),
            'missing_by_target_layer': [sum(is_missing(d) for d in distances[lo:hi])
                                        for _, lo, hi in layers],
        })
    if 'root_missing' in saved:
        require_match([r['missing'] for r in roots] == saved['root_missing'], 'root_missing', {
            'saved':saved['root_missing'], 'independent_roots':roots,
        })
    if 'root_missing_by_target_layer' in saved:
        require_match([r['missing_by_target_layer'] for r in roots] == saved['root_missing_by_target_layer'],
                      'root_layer_missing', {'saved':saved['root_missing_by_target_layer'], 'independent_roots':roots})
    ordered_bad = sum(size*root['missing'] for size, root in zip([LEAVES, BLOCKS, HEADS], roots))
    assert ordered_bad % 2 == 0
    weighted_bad = ordered_bad // 2
    if 'bad_unordered_pairs' in saved:
        assert weighted_bad == saved['bad_unordered_pairs']
    ll, lb, lh = roots[0]['missing_by_target_layer']
    bl, bb, bh = roots[1]['missing_by_target_layer']
    hl, hb, hh = roots[2]['missing_by_target_layer']
    assert LEAVES*lb == BLOCKS*bl and LEAVES*lh == HEADS*hl and BLOCKS*bh == HEADS*hb
    pair_types = {'LL':LEAVES*ll//2, 'LB':LEAVES*lb, 'LH':LEAVES*lh,
                  'BB':BLOCKS*bb//2, 'BH':BLOCKS*bh, 'HH':HEADS*hh//2}
    assert sum(pair_types.values()) == weighted_bad

    # New BB formula for this triangle-head tower, not the prior tower formula.
    # D_j is the action of (b=0,j); H is {(b,0): b in F7}.
    def h_orbit(x):
        return {action_table[b][x] for b in range(7)}

    words = [{0}]
    for _ in range(3):
        words.append(words[-1] | {multiply(w, s) for w in words[-1] for s in S})
    term_HS = {y for s in S for y in h_orbit(s % A_ORDER)}
    triangle_shifts = {a_encode(0,0,1), a_encode(0,0,2)}
    predicted_by_j = []
    term_sizes = []
    for j in range(6):
        term_words = {y for w in words[3] if k_decode(w // A_ORDER)[1] == j
                      for y in h_orbit(w % A_ORDER)}
        term_shifted = set()
        for s in words[1]:
            x_s = s % A_ORDER
            j_s = k_decode(s // A_ORDER)[1]
            shifted = action_table[7*((j-j_s) % 6)][x_s]
            term_shifted.update(h_orbit(shifted))
        predicted_by_j.append(term_words | term_HS | term_shifted | triangle_shifts)
        term_sizes.append({'j':j, 'H_W3_at_j':len(term_words), 'H_S':len(term_HS),
                           'H_D_shift_W1':len(term_shifted), 'head_triangle_shifts':2})
    actual_by_j = [{x for x in range(A_ORDER)
                    if 0 <= root_distances[1][BLOCK_START+x+A_ORDER*j] <= 5}
                   for j in range(6)]
    mismatches = [{'x':x, 'coordinates':a_decode(x), 'j':j,
                   'predicted':x in predicted_by_j[j],
                   'actual_distance':root_distances[1][BLOCK_START+x+A_ORDER*j]}
                  for j in range(6) for x in range(A_ORDER)
                  if (x in predicted_by_j[j]) != (x in actual_by_j[j])]
    require_match(not mismatches, 'BB_pointwise_formula', {'mismatches':mismatches,
        'formula_masks':[sum(1 << x for x in r) for r in predicted_by_j],
        'BFS_masks':[sum(1 << x for x in r) for r in actual_by_j]})
    bb_masks = [sum(1 << x for x in reachable) for reachable in predicted_by_j]
    if 'BB_masks' in saved:
        assert bb_masks == saved['BB_masks']
    bb_missing = sum(A_ORDER-len(reachable) for reachable in actual_by_j)
    if 'BB_missing' in saved:
        assert bb_missing == saved['BB_missing']
    if 'original_BB_missing' in saved:
        assert bb_missing == saved['original_BB_missing']

    # Exactly one call to the existing independent full-source checker.
    process = subprocess.run([str(PROJECT / 'computations/ddp/verify_graph'),
                              str(edge_path), '8', '5'], capture_output=True, text=True)
    assert process.returncode in (0,1), process.stderr
    complete = json.loads(process.stdout)
    assert complete['roots_checked'] == VERTICES
    assert complete['min_degree'] == complete['max_degree'] == 8
    assert complete['bad_unordered_pairs'] == weighted_bad
    Path(str(stem)+'.independent_verify.json').write_text(json.dumps(complete, indent=2)+'\n')
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = {
        'status':'COMPLETE_ONE_SAVED_TRIANGLE_HEAD_SAMPLE_NO_SEARCH',
        'input_edges':edge_path.name, 'input_parameters':parameter_path.name,
        'generator_codes':sorted(S), 'n':n, 'm':m,
        'arithmetic':'A=F7^2 x C3, componentwise modular addition, not XOR; inverse=(-k^-1*x,k^-1)',
        'independent_edges_exactly_equal':True, 'simple':True, 'degree':8,
        'head_triangle_edges_checked':len(triangle_edges),
        'connected':complete['unreachable_unordered_pairs'] == 0,
        'representative_roots':roots, 'weighted_bad_unordered_pairs':weighted_bad,
        'bad_unordered_pairs_by_type':pair_types,
        'input_selection':saved.get('selection', 'specified_single_saved_sample'),
        'full_graph_check':complete,
        'BB_formula':'H*(W3 horizontal components with word quotient j) union H*S_x union H*{D_(j-j_s)x_s:s in W1} union {(0,0,1),(0,0,2)}',
        'BB_word_ball_sizes':list(map(len, words)), 'BB_term_sizes':term_sizes,
        'BB_target_count':BLOCKS, 'BB_all_targets_pointwise_match':True,
        'BB_missing':bb_missing, 'BB_masks':bb_masks,
        'BB_BFS_masks':[sum(1 << x for x in reachable) for reachable in actual_by_j],
        'BB_BFS_distances_in_label_order':root_distances[1][BLOCK_START:HEAD_START],
        'BB_mismatches':mismatches,
        'python_cpu_seconds':time.process_time()-start,
        'checker_cpu_seconds':children.ru_utime+children.ru_stime-child_start.ru_utime-child_start.ru_stime,
        'scope':'Only the one named saved sample; no previous graph or candidate search.',
    }
    Path(str(stem)+'.independent_check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','n','m','independent_edges_exactly_equal',
                                          'weighted_bad_unordered_pairs','BB_missing',
                                          'BB_all_targets_pointwise_match','python_cpu_seconds',
                                          'checker_cpu_seconds']}, indent=2))
    print(json.dumps(complete, indent=2))


if __name__ == '__main__':
    main()
