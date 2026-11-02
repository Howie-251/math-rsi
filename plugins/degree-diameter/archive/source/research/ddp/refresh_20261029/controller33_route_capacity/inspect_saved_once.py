#!/usr/bin/env python3
"""One short-cycle/NB3 statistic on two saved small controllers."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]


def inspect(name, adj, blocks):
    n = len(adj)
    assert all(len(row) == 4 for row in adj)
    assert all(u not in adj[u] and u in adj[v] for u, row in enumerate(adj) for v in row)
    blockof = {u: b for b, block in enumerate(blocks) for u in block}
    assert len(blockof) == n and all(len(b) == 3 for b in blocks)
    assert all(v in adj[u] for block in blocks for u, v in combinations(block, 2))
    extra = [{v for v in adj[u] if blockof[v] != blockof[u]} for u in range(n)]
    assert all(len(row) == 2 for row in extra)
    triangles = [list(x) for x in combinations(range(n), 3)
                 if all(v in adj[u] for u, v in combinations(x, 2))]
    t = [sum(u in x for x in triangles) for u in range(n)]
    cycles = []
    for a, b, c, d in combinations(range(n), 4):
        for cycle in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            edges = list(zip(cycle, cycle[1:] + cycle[:1]))
            if all(v in adj[u] for u, v in edges):
                cycles.append({'vertices': list(cycle),
                               'extra_edge_count': sum(blockof[u] != blockof[v] for u, v in edges)})
    q = [sum(u in x['vertices'] for x in cycles) for u in range(n)]
    nb = [[0] * n for _ in range(n)]
    for u in range(n):
        for a in adj[u]:
            for b in adj[a] - {u}:
                for c in adj[b] - {a}:
                    nb[u][c] += 1
        assert sum(nb[u]) == 36
    rows = []
    for u in range(n):
        nonneighbors = [v for v in range(n) if v != u and v not in adj[u]]
        count = sum(nb[u][v] for v in nonneighbors)
        assert nb[u][u] == 2*t[u]
        assert sum(nb[u][v] for v in adj[u]) == 2*q[u]
        assert count == 36-2*t[u]-2*q[u]
        missing = [v for v in nonneighbors if nb[u][v] == 0]
        duplicates = sum(max(nb[u][v]-1, 0) for v in nonneighbors)
        assert duplicates-len(missing) == 41-n-2*(t[u]+q[u])
        rows.append({'vertex': u, 'triangles': t[u], 'fourcycles': q[u],
                     'sum_t_c4': t[u]+q[u], 'nonadjacent_NB3_sum': count,
                     'missing_nonadjacent_targets': missing,
                     'duplicate_excess': duplicates})
    quotient = []
    pair_weights = [0] * n
    for a, b in combinations(range(len(blocks)), 2):
        edges = [[u, v] for u in blocks[a] for v in blocks[b] if v in extra[u]]
        m = len(edges)
        matching = len({u for u, v in edges}) == len({v for u, v in edges}) == m
        quotient.append({'blocks': [a, b], 'multiplicity': m,
                         'extra_edges': edges, 'is_matching': matching})
        for (u, v), (w, z) in combinations(edges, 2):
            if u != w and v != z:
                for endpoint in (u, v, w, z):
                    pair_weights[endpoint] += 1
            elif u == w:
                third = next(x for x in blocks[b] if x not in (v, z))
                for endpoint in (u, v, z):
                    pair_weights[endpoint] += 2
                pair_weights[third] += 1
            else:
                assert v == z
                third = next(x for x in blocks[a] if x not in (u, w))
                for endpoint in (v, u, w):
                    pair_weights[endpoint] += 2
                pair_weights[third] += 1
    unmixed = [u for u in range(n) if len({blockof[v] for v in extra[u]}) == 1]
    remaining = set(range(n))
    fcycles = []
    while remaining:
        root = min(remaining)
        cycle = [root]
        previous, current = None, root
        while True:
            nxt = min(extra[current] - ({previous} if previous is not None else set()))
            if nxt == root:
                break
            cycle.append(nxt)
            previous, current = current, nxt
        assert len(cycle) >= 3
        remaining.difference_update(cycle)
        fcycles.append(cycle)
    f3 = sum(len(c) == 3 for c in fcycles)
    assert len(triangles) == len(blocks)+len(unmixed)+f3
    q2 = sum(x['extra_edge_count'] == 2 for x in cycles)
    assert q2 == sum(x['multiplicity']*(x['multiplicity']-1)//2 for x in quotient)
    triple_neighbors = {str(a): [b if x == a else x for entry in quotient
                                if entry['multiplicity'] == 3
                                for x, b in [entry['blocks']] if a in (x, b)]
                        for a in range(len(blocks))}
    violations = {
        'local_sum_above4': [r for r in rows if r['sum_t_c4'] > 4],
        'multiplicity_above3': [x for x in quotient if x['multiplicity'] > 3],
        'three_edges_not_matching': [x for x in quotient if x['multiplicity'] == 3 and not x['is_matching']],
        'block_with_multiple_triple_neighbors': {a: bs for a, bs in triple_neighbors.items() if len(bs) > 1},
        'weighted_pair_sum_above3': [{'vertex': u, 'weight': pair_weights[u]} for u in range(n) if pair_weights[u] > 3]
    }
    for u, row in enumerate(rows):
        lower = pair_weights[u]
        exact_twoF_t = sum(u in x and sum(blockof[a] != blockof[b] for a, b in combinations(x, 2)) == 2 for x in triangles)
        exact_twoF_q = sum(u in x['vertices'] and x['extra_edge_count'] == 2 for x in cycles)
        assert lower == exact_twoF_t + exact_twoF_q
        assert lower <= t[u] + q[u] - 1
        row.update(weighted_pair_sum=lower, total_cycle_budget_minus_pair_lower_bound=t[u]+q[u]-1-lower)
    return {
        'name': name, 'n': n, 'm': sum(map(len, adj))//2, 'designated_blocks': blocks,
        'triangles_total': len(triangles), 'fourcycles_total': len(cycles),
        'unmixed_vertices': unmixed, 'extra_cycles': fcycles,
        'sum_t_c4_histogram': dict(sorted(Counter(t[u]+q[u] for u in range(n)).items())),
        'quotient_multiplicity_histogram': dict(sorted(Counter(x['multiplicity'] for x in quotient).items())),
        'fourcycles_by_extra_edge_count': dict(sorted(Counter(x['extra_edge_count'] for x in cycles).items())),
        'weighted_pair_sum_histogram': dict(sorted(Counter(pair_weights).items())),
        'cycle_budget_minus_pair_lower_bound_histogram': dict(sorted(Counter(t[u]+q[u]-1-pair_weights[u] for u in range(n)).items())),
        'actual_missing_nonadjacent_ordered_pairs': sum(len(r['missing_nonadjacent_targets']) for r in rows),
        'local_identity_all_vertices_exact': True,
        'own_order_capacity_bound': (41-n)//2,
        'own_order_capacity_bound_holds': all(t[u]+q[u] <= (41-n)//2 for u in range(n)),
        'C33_restriction_violations': violations,
        'rows': rows, 'quotient': quotient, 'triangles': triangles, 'fourcycles': cycles
    }


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
    start = time.process_time()
    pred = json.loads((OUT/'PREDICTION.json').read_text())
    source = ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
    ports = json.loads(source.read_text())['controller']
    adj30 = [set(row) for row in ports]
    # The saved successful C30's triangle factor is not its port0/1 cycles.
    # Reuse its previously established literal partition, without rediscovery.
    structure = json.loads((source.parent/'controller_structure.json').read_text())
    blocks30 = structure['triangles']
    with (ROOT/pred['inputs']['C33_best']).open() as stream:
        n, m = map(int, next(stream).split())
        assert (n, m) == (33, 66)
        adj33 = [set() for _ in range(n)]
        for line in stream:
            u, v = map(int, line.split())
            adj33[u].add(v)
            adj33[v].add(u)
    observations = [inspect('C30_success', adj30, blocks30),
                    inspect('C33_saved_best', adj33, [list(range(3*b, 3*b+3)) for b in range(11)])]
    best = observations[1]
    violations = best['C33_restriction_violations']
    prediction_supported = any(bool(x) for x in violations.values())
    elapsed = time.process_time()-start
    result = {'status': 'SINGLE_SAVED_PAIR_STATISTIC_COMPLETE',
              'prediction': 'SUPPORTED' if prediction_supported else 'REFUTED_SAVED_BEST_PASSES_THESE_NECESSARY_GATES',
              'observations': observations, 'CPU_seconds': elapsed, 'CPU_budget_seconds': 2,
              'workers': 1, 'controllers_generated': 0, 'optimization_proposals': 0,
              'BFS_calls': 0, 'SAT_calls': 0, 'C11_cases_evaluated': 0,
              'main_Wiki_changed': False, 'pending': []}
    (OUT/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
    summary = {'status': result['status'], 'prediction': result['prediction'], 'CPU_seconds': elapsed,
               'controllers': [{k: x[k] for k in [
                   'name','n','triangles_total','fourcycles_total','sum_t_c4_histogram',
                   'quotient_multiplicity_histogram','actual_missing_nonadjacent_ordered_pairs',
                   'own_order_capacity_bound_holds','weighted_pair_sum_histogram',
                   'cycle_budget_minus_pair_lower_bound_histogram','C33_restriction_violations']}
                               for x in observations]}
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
