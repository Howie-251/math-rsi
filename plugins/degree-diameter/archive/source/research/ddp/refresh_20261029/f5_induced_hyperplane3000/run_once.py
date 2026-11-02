#!/usr/bin/env python3
"""One authorized induced graph and one BFS; no search or solver."""
from pathlib import Path
from collections import Counter, deque
from array import array
import json
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

def main():
    start = time.process_time()
    source = BASE / 'f5_full_d20_D3/graph_d20_D3_n3750.edges'
    # This is the sole read of the source edge table in this task.
    rows = [tuple(map(int, line.split())) for line in source.read_text().splitlines()
            if line.strip() and not line.startswith('#')]
    n, m = rows[0]
    edges = rows[1:]
    assert (n, m, len(edges)) == (3750, 37500, 37500)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for nb in adj:
        nb.sort()
        assert len(nb) == 20
    # A literal adjacency cache lets the forthcoming prepare step reuse this read.
    cache = array('H', (w for nb in adj for w in nb))
    assert cache.itemsize == 2
    with (HERE / 'source_adjacency.u16.bin').open('wb') as f:
        cache.tofile(f)
    def retain(v):
        c = v % 125
        return (c % 5 + c // 5 % 5 + c // 25) % 5 != 0
    old_ids = [v for v in range(n) if retain(v)]
    old_to_new = {v: i for i, v in enumerate(old_ids)}
    new_edges = [(old_to_new[u], old_to_new[v]) for u, v in edges
                 if u in old_to_new and v in old_to_new]
    newadj = [[old_to_new[w] for w in adj[v] if w in old_to_new] for v in old_ids]
    degrees = Counter(map(len, newadj))
    assert len(old_ids) == 3000 and len(new_edges) == 24000
    assert degrees == {16: 3000}
    target = 626
    assert retain(target)
    selected = None
    for z in range(18 * 125, 19 * 125):
        if retain(z):
            continue
        mids = sorted(set(adj[z]).intersection(adj[target]))
        starts = [x for x in adj[z] if x < 125 and retain(x)]
        if mids and starts:
            selected = (starts[0], z, mids[0], target)
            break
    assert selected is not None
    x, z, w, target = selected
    assert [v // 125 for v in selected] == [0, 18, 29, 5]
    assert all(v in adj[u] for u, v in zip(selected, selected[1:]))
    assert retain(x) and not retain(z)
    # Exactly one actual graph BFS, on this induced graph only.
    root = old_to_new[x]
    distance = [-1] * 3000
    parent = [-1] * 3000
    distance[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in newadj[u]:
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
    target_distance = distance[old_to_new[target]]
    assert target_distance < 0 or target_distance > 3
    target_shortest = []
    if target_distance >= 0:
        v = old_to_new[target]
        while v != -1:
            target_shortest.append(old_ids[v])
            v = parent[v]
        target_shortest.reverse()
    fibers = []
    for a in range(30):
        missed = [v for v in old_ids if v // 125 == a
                  and (distance[old_to_new[v]] < 0 or distance[old_to_new[v]] > 3)]
        fibers.append({'controller': a, 'retained': 100,
                       'missing_R3_count': len(missed), 'missing_old_ids': missed})
    with (HERE / 'induced_n3000_d16.edges').open('w') as f:
        f.write(f'{len(old_ids)} {len(new_edges)}\n')
        for u, v in new_edges:
            f.write(f'{u} {v}\n')
    (HERE / 'OLD_LABEL_MAP.json').write_text(json.dumps({
        'new_to_old': old_ids, 'new_label_rule': 'increasing retained old labels',
        'retention_rule': '(x0+x1+x2) mod 5 != 0',
        'source_adjacency_cache': 'native unsigned 16-bit; 3750 rows, 20 sorted neighbors per row',
    }, indent=2) + '\n')
    (HERE / 'ROOT_DISTANCES.json').write_text(json.dumps({
        'root_old': x, 'root_new': root, 'distances_in_new_label_order': distance,
        'fiber_missing': fibers,
    }, indent=2) + '\n')
    result = {
        'status': 'COMPLETE_SINGLE_RULE_REJECTED_BY_LITERAL_PAIR',
        'source': str(source.relative_to(HERE.parents[3])),
        'source_edge_table_reads': 1, 'source_BFS_runs': 0,
        'graphs_generated': 1, 'induced_BFS_roots': 1,
        'n': len(old_ids), 'm': len(new_edges),
        'degree_histogram': dict(degrees),
        'old_unique_shortest_path': list(selected),
        'controller_path': [0, 18, 29, 5], 'ports': [0, 2, 1],
        'path_uniqueness_basis': 'Saved unique controller distance-three path plus full-rank noise map; no new source BFS.',
        'deleted_path_vertices': [v for v in selected if not retain(v)],
        'bad_pair_old_ids': [x, target],
        'bad_pair_new_ids': [root, old_to_new[target]],
        'bad_pair_induced_distance': target_distance,
        'one_induced_shortest_path_old_ids': target_shortest,
        'root_distance_histogram': dict(sorted(Counter(distance).items())),
        'root_R3_size': sum(0 <= d <= 3 for d in distance),
        'root_R3_missing': sum(d < 0 or d > 3 for d in distance),
        'fiber_missing_counts': [f['missing_R3_count'] for f in fibers],
        'paper_bound_not_global_measurement': {
            'fiber_pair': [0, 5], 'retained_targets_in_fiber5': 100,
            'minimum_bad_retained_sources_in_fiber0_per_target': 20,
            'unordered_bad_pairs_lower_bound': 2000,
            'scope': 'Provided route argument; only the stated single root was measured here.',
        },
        'global_diameter_computed': False, 'global_bad_pair_count_computed': False,
        'CPU_seconds': time.process_time() - start,
        'pending': [], 'new_record': False,
    }
    (HERE / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status','n','m','degree_histogram',
        'bad_pair_old_ids','bad_pair_induced_distance','old_unique_shortest_path',
        'deleted_path_vertices','root_R3_size','root_R3_missing','fiber_missing_counts','CPU_seconds']}))

if __name__ == '__main__':
    main()
