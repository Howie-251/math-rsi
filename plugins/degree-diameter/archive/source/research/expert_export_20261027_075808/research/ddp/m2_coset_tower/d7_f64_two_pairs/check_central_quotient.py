"""Fixed-layer distance calibration of the saved F64 graph and its central quotient."""
import json
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
SOURCE = ROOT / 'research/ddp/m2_coset_tower/d7_f64_three_pairs/search.best.edges'
PARAMS = ROOT / 'research/ddp/m2_coset_tower/d7_f64_three_pairs/search.best.json'
params = json.loads(PARAMS.read_text())
raw = list(map(int, SOURCE.read_text().split()))
n, m = raw[:2]
assert (n, m) == (3200, 11200)
edges = [tuple(raw[i:i + 2]) for i in range(2, len(raw), 2)]
assert len(edges) == len(set(edges)) == m
original_adj = [set() for _ in range(n)]
for u, v in edges:
    original_adj[u].add(v)
    original_adj[v].add(u)
assert all(len(a) == 7 for a in original_adj)

def center(v):
    return v % 64 + 64 * ((v // 64 + 21) % 42) if v < 2688 else v

assert {tuple(sorted((center(u), center(v)))) for u, v in edges} == set(edges)
assert all(center(v) != v and center(center(v)) == v for v in range(2688))
assert all(center(v) == v for v in range(2688, 3200))

def project(v):
    return v % 64 + 64 * ((v // 64) % 21) if v < 2688 else v - 1344

quotient_edges = set()
dropped_loops = 0
for u, v in edges:
    a, b = project(u), project(v)
    if a == b:
        dropped_loops += 1
    else:
        quotient_edges.add(tuple(sorted((a, b))))
quotient_adj = [set() for _ in range(1856)]
for u, v in quotient_edges:
    quotient_adj[u].add(v)
    quotient_adj[v].add(u)
with (OUT / 'CENTRAL_QUOTIENT.edges').open('w') as out:
    out.write(f'1856 {len(quotient_edges)}\n')
    for u, v in sorted(quotient_edges):
        out.write(f'{u} {v}\n')

def bfs(adj, root):
    dist = [-1] * len(adj)
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert -1 not in dist
    return dist

def missing_layers(dist, L, B):
    return {'leaf': sum(d > 5 for d in dist[:L]),
            'block': sum(d > 5 for d in dist[L:L + B]),
            'head': sum(d > 5 for d in dist[L + B:]),
            'total': sum(d > 5 for d in dist)}

root_checks = []
for kind, original_root in [('block', 2688), ('head', 3136)]:
    quotient_root = project(original_root)
    before = bfs(original_adj, original_root)
    after = bfs(quotient_adj, quotient_root)
    fixed_mismatches = [{'old_vertex': v, 'quotient_vertex': project(v),
                         'original_distance': before[v], 'quotient_distance': after[project(v)]}
                        for v in range(2688, 3200) if before[v] != after[project(v)]]
    pair_mismatches = []
    for qv in range(1344):
        a, b = qv, qv + 1344
        if not before[a] == before[b] == after[qv]:
            pair_mismatches.append({'original_pair': [a, b], 'quotient_vertex': qv,
                                    'original_distances': [before[a], before[b]], 'quotient_distance': after[qv]})
    root_checks.append({
        'root_type': kind, 'original_root': original_root, 'quotient_root': quotient_root,
        'original_missing_by_target_layer': missing_layers(before, 2688, 448),
        'quotient_missing_by_target_layer': missing_layers(after, 1344, 448),
        'all_448_block_and_64_head_distances_pointwise_equal': not fixed_mismatches,
        'all_1344_leaf_pairs_both_original_distances_equal_quotient': not pair_mismatches,
        'fixed_layer_mismatches': fixed_mismatches, 'leaf_pair_mismatches': pair_mismatches,
        'original_distance_by_vertex': before, 'quotient_distance_by_vertex': after,
    })

def field_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= 0x43
    return out

power = [1]
for _ in range(1, 21):
    power.append(field_mul(power[-1], 8))
assert len(set(power)) == 21 and field_mul(power[-1], 8) == 1
S_original = list(map(tuple, params['S_coordinates']))
S = {(x, i % 21) for x, i in S_original}
S.discard((0, 0))

def product(g, v):
    x, i = g
    y, j = v
    return x ^ field_mul(power[i], y), (i + j) % 21

def set_product(A, B):
    return {product(a, b) for a in A for b in B}

W = [{(0, 0)}]
for _ in range(3):
    W.append(W[-1] | set_product(W[-1], S))
H = {(0, 0), (0, 7), (0, 14)}
K = {(0, i) for i in range(21)}
terms = {
    'H_W3_H': set_product(set_product(H, W[3]), H),
    'K_W1_H': set_product(set_product(K, W[1]), H),
    'H_W1_K': set_product(set_product(H, W[1]), K),
}
TBB = set().union(*terms.values())
assert set_product(TBB, H) == TBB
formula_blocks = {1344 + x + 64 * (i % 7) for x, i in TBB}
block_root_dist = root_checks[0]['quotient_distance_by_vertex']
bfs_blocks = {v for v in range(1344, 1792) if block_root_dist[v] <= 5}
formula_missed = sorted(bfs_blocks - formula_blocks)
formula_extra = sorted(formula_blocks - bfs_blocks)
assert {x + 64 * i for x, i in S} == {v for v in quotient_adj[0] if v < 1344}
BB = {
    'formula': 'T_BB=H W3 H union K W1 H union H W1 K',
    'quotient_group': 'GF64 semidirect C21, r=8 of order21',
    'quotient_H': sorted(H), 'quotient_K_order': len(K), 'projected_generators': sorted(S),
    'word_ball_sizes_W0_to_W3': list(map(len, W)),
    'group_element_count_by_term': {key: len(value) for key, value in terms.items()},
    'union_group_element_count': len(TBB),
    'formula_reachable_block_labels': sorted(formula_blocks),
    'BFS_reachable_block_labels': sorted(bfs_blocks),
    'all_448_block_targets_pointwise_equal': not formula_missed and not formula_extra,
    'formula_false_negative_labels': formula_missed, 'formula_false_positive_labels': formula_extra,
    'formula_missing_block_count': 448 - len(formula_blocks),
}
result = {
    'status': 'COMPLETE_FIXED_ROOT_CENTRAL_QUOTIENT_CALIBRATION',
    'source': str(SOURCE.relative_to(ROOT)),
    'original_vertices': n, 'original_edges': m,
    'quotient_vertices': 1856, 'quotient_edges': len(quotient_edges),
    'quotient_degree_histogram': dict(sorted(Counter(map(len, quotient_adj)).items())),
    'dropped_projected_selfloops': dropped_loops,
    'deduplicated_projected_edges': m - dropped_loops - len(quotient_edges),
    'center_action_is_exact_original_graph_automorphism': True,
    'center_action': 'leaf(x,i)->leaf(x,i+21 mod42); every block and head is fixed',
    'label_map': {'original_leaf': 'x+64*i', 'quotient_leaf': 'x+64*(i mod21)',
                  'original_block': '2688+x+64*b', 'quotient_block': '1344+x+64*b',
                  'original_head': '3136+x', 'quotient_head': '1792+x'},
    'fixed_root_checks': root_checks, 'BB_formula_check': BB,
    'all_checks_passed': all(not r['fixed_layer_mismatches'] and not r['leaf_pair_mismatches'] for r in root_checks)
                          and BB['all_448_block_targets_pointwise_equal'],
    'cpu_seconds': time.process_time() - START,
    'scope': 'Exactly two original roots and their two quotient roots; no 3200-root repeat, no leaf-root distance inference, no candidate search.',
}
(OUT / 'CENTRAL_QUOTIENT_CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
brief = {key: value for key, value in result.items() if key not in ('fixed_root_checks', 'BB_formula_check')}
brief['fixed_root_checks'] = [{key: value for key, value in r.items() if 'distance_by_vertex' not in key} for r in root_checks]
brief['BB_formula_check'] = {key: value for key, value in BB.items() if key not in ('formula_reachable_block_labels', 'BFS_reachable_block_labels')}
print(json.dumps(brief, indent=2))
