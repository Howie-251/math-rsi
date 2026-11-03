"""Small implementation controls; not an additional construction search family."""
from collections import Counter, deque
from itertools import product
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parent

def multiply(g, h, p, m, action):
    return ((g[0] + pow(action, g[1], p) * h[0]) % p, (g[1] + h[1]) % m)

def normalize(z, residues, p, action):
    direction = [(1 - pow(action, i, p)) % p for i in residues]
    pivot = next(i for i, x in enumerate(direction) if x)
    shift = -z[pivot] * pow(direction[pivot], -1, p) % p
    w = [(x + shift * v) % p for x, v in zip(z, direction)]
    if not any(w):
        return None
    scale = pow(next(x for x in w if x), -1, p)
    return tuple(x * scale % p for x in w)

def graph(residues, values, p, m, action):
    q = p * m
    edges = set()
    generators = list(zip(values, residues))
    for x, i in product(range(p), range(m)):
        g = (x, i)
        u = x * m + i
        edges.add((u, q + u))
        for side, indices in enumerate(((0, 1), (2, 3))):
            for index in indices:
                h = multiply(g, generators[index], p, m, action)
                v = h[0] * m + h[1]
                edges.add(tuple(sorted((side * q + u, side * q + v))))
    adj = [set() for _ in range(2 * q)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return edges, adj

def reason(residues, values, p, m, action):
    gs = list(zip(values, residues))
    if (0, 0) in gs:
        return 1
    if any(multiply(g, g, p, m, action) == (0, 0) for g in gs):
        return 2
    if any(gs[i] == gs[j] or multiply(gs[i], gs[j], p, m, action) == (0, 0)
           for i, j in ((0, 1), (2, 3))):
        return 3
    return 0

def distances(adj, root):
    d = [-1] * len(adj)
    d[root] = 0
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                todo.append(v)
    return d

def score_all(adj):
    all_distances = [distances(adj, root) for root in range(len(adj))]
    q = len(adj) // 2
    miss = [sum(d < 0 or d > 5 for d in all_distances[root]) for root in (0, q)]
    bad = sum(d < 0 or d > 5 for root, row in enumerate(all_distances) for d in row[root + 1:])
    assert bad * 2 == q * sum(miss)
    assert all(min(row) >= 0 for row in all_distances)
    return sum(miss), max(map(max, all_distances)), bad

def main():
    out = ROOT / 'regression'
    out.mkdir(exist_ok=True)
    results = []
    cases = [(7, 3, 2, [(0, 1, 1, 1), (1, 1, 1, 1), (1, 2, 0, 1)]),
             (5, 4, 2, [(0, 1, 0, 1), (1, 2, 1, 2), (1, 1, 1, 3), (1, 3, 0, 1)]),
             (13, 27, 3, [(1, 4, 2, 4)])]
    for p, m, action, skeletons in cases:
        prefix = out / f'p{p}_m{m}_r{action}'
        skeleton_file = prefix.with_suffix('.skeletons.txt')
        skeleton_file.write_text(''.join(' '.join(map(str, r)) + '\n' for r in skeletons))
        expected_hist = Counter()
        expected_illegal = Counter()
        point_count = 0
        for residues in skeletons:
            classes = Counter(normalize(z, residues, p, action) for z in product(range(p), repeat=4))
            assert classes.pop(None) == p
            assert len(classes) == p * p + p + 1
            assert set(classes.values()) == {p * (p - 1)}
            for values in classes:
                point_count += 1
                why = reason(residues, values, p, m, action)
                edges, adj = graph(residues, values, p, m, action)
                directly_legal = all(u != v for u, v in edges) and all(len(a) == 5 for a in adj)
                assert directly_legal == (why == 0)
                if why:
                    expected_illegal[why] += 1
                else:
                    if p == 13:
                        score = sum(sum(d < 0 or d > 5 for d in distances(adj, root))
                                    for root in (0, p * m))
                    else:
                        score, _, _ = score_all(adj)
                    expected_hist[score] += 1
        run = subprocess.run([str(ROOT / 'search_4plus1'), str(p), str(m), str(action), str(skeleton_file),
                              '10', str(prefix), 'full'], text=True, capture_output=True)
        prefix.with_suffix('.log').write_text(run.stdout + run.stderr)
        assert run.returncode == 0
        actual = json.loads(prefix.with_suffix('.summary.json').read_text())
        assert actual['skeletons_completed'] == len(skeletons)
        assert actual['projective_visited'] == point_count
        assert actual['score_histogram'] == {str(k): v for k, v in sorted(expected_hist.items())}
        assert actual['illegal_internal_identity'] == expected_illegal[1]
        assert actual['illegal_internal_involution'] == expected_illegal[2]
        assert actual['illegal_internal_pair_collision'] == expected_illegal[3]
        best = json.loads(prefix.with_suffix('.best.json').read_text())
        expected_edges, _ = graph(best['quotient_residues'], best['translation_values'], p, m, action)
        edge_lines = prefix.with_suffix('.best.edges').read_text().splitlines()
        assert tuple(map(int, edge_lines[0].split())) == (2 * p * m, 5 * p * m)
        assert expected_edges == {tuple(map(int, line.split())) for line in edge_lines[1:]}
        results.append({'p': p, 'm': m, 'r': action, 'projective_visited': point_count,
                        'legal': sum(expected_hist.values()), 'score_histogram': expected_hist,
                        'illegal_categories': expected_illegal, 'all_raw_translation_orbits_checked': True,
                        'all_roots_for_every_legal_graph_checked': p != 13,
                        'both_roots_for_every_legal_graph_checked': True, 'best_edge_set_exactly_matches': True})
        if p == 13:
            assert min(expected_hist) > 0
            verification = subprocess.run(['computations/ddp/verify_graph', str(prefix.with_suffix('.best.edges')),
                                           '5', '5'], text=True, capture_output=True)
            assert verification.returncode == 1
            verified = json.loads(verification.stdout)
            assert verified['min_degree'] == verified['max_degree'] == 5
            assert verified['bad_unordered_pairs'] == p * m * min(expected_hist) // 2
            prefix.with_suffix('.best.independent_bfs.json').write_text(verification.stdout)
    edges, adj = graph((1, 0, 1, 0), (0, 1, 1, 2), 7, 3, 2)
    assert all(len(a) == 5 for a in adj)
    positive_score, positive_diameter, positive_bad = score_all(adj)
    assert positive_score == 0
    result = {'regressions': results, 'specified_n42_control': {
        'quotient_residues': [1, 0, 1, 0], 'translation_values': [0, 1, 1, 2],
        'n': 42, 'degree': 5, 'diameter': positive_diameter, 'missing_sum': positive_score,
        'bad_pairs': positive_bad}}
    (out / 'check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
