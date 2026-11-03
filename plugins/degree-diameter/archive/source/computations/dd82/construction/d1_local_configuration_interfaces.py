#!/usr/bin/env python3
"""Expand every leave matching of the ten supplied (10_3) configurations.

This verifies local matrices, not a complete order-60 graph or the external
classification's completeness. No search over general graphs occurs.
"""
import itertools
import json
from pathlib import Path
import resource
import time

BASE = Path(__file__).resolve().parent


def matchings(adj, remaining):
    if not remaining:
        yield []
        return
    u = min(remaining)
    for v in sorted(adj[u] & remaining):
        for tail in matchings(adj, remaining - {u, v}):
            yield [(u, v)] + tail


def gram(rows):
    return [[len(a & b) for b in rows] for a in rows]


def cycle_type(adj):
    assert all(len(a) == 2 for a in adj)
    unseen = set(range(10))
    sizes = []
    while unseen:
        todo = [min(unseen)]
        unseen.remove(todo[0])
        size = 0
        while todo:
            u = todo.pop()
            size += 1
            for v in adj[u] & unseen:
                unseen.remove(v)
                todo.append(v)
        sizes.append(size)
    return sorted(sizes)


def expand(blocks):
    rows = [{j for j, b in enumerate(blocks) if i in b} for i in range(10)]
    assert all(len(r) == 3 for r in rows)
    assert len(blocks) == 10 and all(len(b) == 3 for b in blocks)
    zz = gram(rows)
    assert all(zz[i][j] <= 1 for i in range(10) for j in range(i))
    leave = [{j for j in range(10) if j != i and zz[i][j] == 0}
             for i in range(10)]
    assert all(len(r) == 3 for r in leave)
    choices = []
    for matching in matchings(leave, set(range(10))):
        mate = {}
        for u, v in matching:
            mate[u], mate[v] = v, u
        factor = [leave[i] - {mate[i]} for i in range(10)]
        edges = [(i, j) for i in range(10) for j in sorted(factor[i]) if i < j]
        assert len(edges) == 10
        y_rows = [{j for j, e in enumerate(edges) if i in e} for i in range(10)]
        yy = gram(y_rows)
        assert all(int(mate[i] == j) + yy[i][j] + zz[i][j]
                   == 1 + 4 * (i == j) for i in range(10) for j in range(10))
        choices.append({'matching': matching, 'factor_edges': edges,
                        'factor_cycle_type': cycle_type(factor),
                        'Y_row_supports': [sorted(r) for r in y_rows]})
    return {'Z_row_supports': [sorted(r) for r in rows],
            'leave_edges': [(i, j) for i in range(10) for j in sorted(leave[i]) if i < j],
            'matching_count': len(choices), 'choices': choices}


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
    start = time.process_time()
    source = json.loads((BASE / 'd1_10_3_catalog/10_3_grunbaum.json').read_text())
    result = {'scope': 'All perfect matchings of primal and dual leaves for the ten supplied configurations; one-sided local equation only',
              'classification_source': source['source_url'], 'configurations': []}
    for item in source['configurations']:
        blocks = [set(b) for b in item['blocks']]
        primal = expand(blocks)
        dual_blocks = [{j for j, b in enumerate(blocks) if i in b} for i in range(10)]
        dual = expand(dual_blocks)
        result['configurations'].append({'grunbaum_number': item['grunbaum_number'],
                                        'primal': primal, 'dual': dual})
    result['cpu_seconds'] = time.process_time() - start
    result['cpu_limit_seconds'] = 10
    result['local_equations_verified'] = True
    result['total_primal_choices'] = sum(x['primal']['matching_count'] for x in result['configurations'])
    result['total_dual_choices'] = sum(x['dual']['matching_count'] for x in result['configurations'])
    out = BASE / 'd1_10_3_catalog/local_interfaces.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'configurations'}, indent=2))
    for x in result['configurations']:
        print(x['grunbaum_number'], [(side, x[side]['matching_count'],
              sorted({tuple(c['factor_cycle_type']) for c in x[side]['choices']}))
              for side in ('primal', 'dual')])


if __name__ == '__main__':
    main()
