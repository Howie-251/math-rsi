"""Exact quotient/path diagnosis; no optimization trajectory."""
from collections import Counter, deque
from pathlib import Path
import json
import resource
import time

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[2]
SOURCE = PROJECT / 'computations/ddp/m1/d5_four_one/p37_m9_r7.search.best.edges'
P, M, Q, N = 37, 9, 333, 666

def vertex(base, x):
    side, residue = divmod(base, M)
    return side * Q + x * M + residue

def label(v):
    side, rest = divmod(v, Q)
    x, residue = divmod(rest, M)
    return [side, x, residue]

def bfs(adj, root):
    dist = [-1] * len(adj)
    dist[root] = 0
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                todo.append(v)
    return dist

def main():
    started = time.monotonic()
    cpu_started = time.process_time()
    lines = SOURCE.read_text().splitlines()
    assert tuple(map(int, lines[0].split())) == (N, 5 * N // 2)
    source_edges = {tuple(map(int, line.split())) for line in lines[1:]}
    adj = [set() for _ in range(N)]
    for u, v in source_edges:
        adj[u].add(v)
        adj[v].add(u)
    # Orient each base edge according to its positive generator, including loops.
    rows = []
    for side, name, value, residue in [(0, 'a', 1, 0), (0, 'c', 0, 1),
                                        (1, 'b', 21, 4), (1, 'd', 15, 4)]:
        for i in range(M):
            rows.append({'u': side * M + i, 'v': side * M + (i + residue) % M,
                         'voltage': value * pow(7, i, P) % P, 'generator': name, 'residue': i})
    for i in range(M):
        rows.append({'u': i, 'v': M + i, 'voltage': 0, 'generator': 'cross', 'residue': i})
    assert len(rows) == 45
    base_adj = [[] for _ in range(18)]
    lifted = set()
    for eid, row in enumerate(rows):
        u, v, voltage = row['u'], row['v'], row['voltage']
        base_adj[u].append((v, eid, 1))
        base_adj[v].append((u, eid, -1))
        if u == v:
            assert voltage != 0
        for x in range(P):
            lifted.add(tuple(sorted((vertex(u, x), vertex(v, (x + voltage) % P)))))
    assert lifted == source_edges
    assert all(len(a) == 5 for a in base_adj)
    assert all(len(a) == 5 for a in adj)
    groups = Counter(tuple(sorted((r['u'], r['v']))) for r in rows)
    assert sum(r['u'] == r['v'] for r in rows) == 9
    assert sum(v == 2 for v in groups.values()) == 9

    def extend(form, eid, sign):
        d = dict(form)
        d[eid] = (d.get(eid, 0) + sign) % P
        if not d[eid]:
            del d[eid]
        return tuple(sorted(d.items()))

    formal_counts, actual_counts, defective = [], [], []
    histogram = Counter()
    bad_pairs = set()
    root_missing = []
    distances_by_root = []
    for root in range(18):
        reached = {(root, ())}
        frontier = reached.copy()
        for _ in range(5):
            new = {(v, extend(form, eid, sign)) for u, form in frontier
                   for v, eid, sign in base_adj[u]}
            new.difference_update(reached)
            reached.update(new)
            frontier = new
        buckets = [set() for _ in range(18)]
        for target, form in reached:
            buckets[target].add(form)
        values = [{sum(coef * rows[eid]['voltage'] for eid, coef in form) % P
                   for form in forms} for forms in buckets]
        dist = bfs(adj, vertex(root, 0))
        assert min(dist) == 0 and max(dist) == 6
        observed = [set() for _ in range(18)]
        missing_labels = []
        for v, distance in enumerate(dist):
            side, x, residue = label(v)
            target = side * M + residue
            if distance <= 5:
                observed[target].add(x)
            else:
                missing_labels.append([side, x, residue])
                for shift in range(P):
                    bad_pairs.add(tuple(sorted((vertex(root, shift), vertex(target, (x + shift) % P)))))
        assert observed == values
        fc = [len(forms) for forms in buckets]
        ac = [len(x) for x in values]
        formal_counts.append(fc)
        actual_counts.append(ac)
        root_missing.append({'root': root, 'missing': missing_labels})
        distances_by_root.append(dict(sorted(Counter(dist).items())))
        for target in range(18):
            histogram[fc[target]] += 1
            if ac[target] < P:
                defective.append({'root': root, 'target': target, 'formal_count': fc[target],
                                  'actual_count': ac[target], 'missing_voltages': sorted(set(range(P)) - values[target])})
    score = sum(P - x for row in actual_counts for x in row)
    assert score == 36 and len(bad_pairs) == P * score // 2 == 666
    bad_adj = [set() for _ in range(N)]
    for u, v in bad_pairs:
        bad_adj[u].add(v)
        bad_adj[v].add(u)
    seen = set()
    components = []
    for u in range(N):
        if u in seen:
            continue
        found = {u}
        todo = [u]
        seen.add(u)
        while todo:
            v = todo.pop()
            for w in bad_adj[v] - seen:
                seen.add(w)
                found.add(w)
                todo.append(w)
        components.append(len(found))
    result = {
        'source': str(SOURCE.relative_to(PROJECT)), 'n': N, 'degree': 5, 'target_diameter': 5,
        'quotient_vertices': 18, 'quotient_edges': 45, 'loops': 9, 'parallel_edge_pairs': 9,
        'edge_voltages': rows, 'exact_seed_edge_equality': True,
        'minimum_formal_fiber_capacity': min(map(min, formal_counts)),
        'formal_capacity_histogram': dict(sorted(histogram.items())), 'formal_counts': formal_counts,
        'actual_counts': actual_counts, 'defective_fibers': defective,
        'all18_symbolic_evaluations_exactly_equal_original_BFS_sets': True,
        'root_missing': root_missing, 'root_distance_histograms': distances_by_root,
        'representative_missing_sum': score, 'bad_unordered_pairs': len(bad_pairs),
        'bad_pair_types': {str(k): v for k, v in Counter((u // Q, v // Q) for u, v in bad_pairs).items()},
        'bad_graph_component_sizes': dict(sorted(Counter(components).items())),
        'bad_graph_degree_counts_by_side': [dict(sorted(Counter(len(bad_adj[u]) for u in range(side * Q, (side + 1) * Q)).items())) for side in (0, 1)],
        'cpu_seconds': time.process_time() - cpu_started, 'wall_seconds': time.monotonic() - started,
    }
    (OUT / 'diagnosis.json').write_text(json.dumps(result, indent=2) + '\n')
    (OUT / 'base.txt').write_text('37 18 45\n' + ''.join(f"{r['u']} {r['v']} {r['voltage']}\n" for r in rows))
    print(json.dumps({k: result[k] for k in ('minimum_formal_fiber_capacity', 'formal_capacity_histogram',
                     'representative_missing_sum', 'bad_unordered_pairs', 'bad_pair_types',
                     'bad_graph_component_sizes', 'cpu_seconds', 'wall_seconds')}))

if __name__ == '__main__':
    main()
