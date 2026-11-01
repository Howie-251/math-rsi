#!/usr/bin/env python3
"""Exact block-event inclusion-exclusion; no coloring enumeration."""
import json
from math import comb
from pathlib import Path
from time import process_time


def canonical(shared):
    blocks = [set() for _ in range(5)]
    vertex = 0
    for indices in shared:
        for i in indices:
            blocks[i].add(vertex)
        vertex += 1
    for block in blocks:
        while len(block) < 4:
            block.add(vertex)
            vertex += 1
    assert vertex == 18
    assert all(len(block) == 4 for block in blocks)
    assert len(set(map(frozenset, blocks))) == 5
    return blocks


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def conflict_count(blocks, blue):
    # Expand (union red-block indicators)*(union blue-block indicators).
    # A block assigned to both colors has zero contribution, so use disjoint
    # nonempty block-index subsets. Intersecting vertex unions also give zero.
    unions = []
    for mask in range(32):
        unions.append(set().union(*(blocks[i] for i in range(5) if mask >> i & 1)))
    total = 0
    terms = nonzero = 0
    for red_mask in range(1, 32):
        for blue_mask in range(1, 32):
            if red_mask & blue_mask:
                continue
            terms += 1
            red_union, blue_union = unions[red_mask], unions[blue_mask]
            if red_union & blue_union:
                continue
            count = choose(18 - len(red_union) - len(blue_union), blue - len(blue_union))
            if count:
                nonzero += 1
            total += (-1) ** (red_mask.bit_count() + blue_mask.bit_count()) * count
    assert 0 <= total <= comb(18, blue)
    return {'conflict': total, 'sample_space': comb(18, blue),
            'disjoint_index_terms': terms, 'nonzero_terms': nonzero}


def main():
    started = process_time()
    shapes = {
        'one_triple': [(0, 1, 2)],
        'two_doubles_same_pair': [(0, 1), (0, 1)],
        'two_doubles_adjacent_pairs': [(0, 1), (1, 2)],
        'two_doubles_disjoint_pairs': [(0, 1), (2, 3)],
    }
    rows = []
    for name, shared in shapes.items():
        blocks = canonical(shared)
        multiplicities = [sum(v in block for block in blocks) for v in range(18)]
        assert sum(multiplicities) == 20
        assert sum(m - 1 for m in multiplicities) == 2
        rows.append({'shape': name, 'blocks': [sorted(block) for block in blocks],
                     'multiplicities': sorted(multiplicities, reverse=True),
                     'eight_blue_ten_red': conflict_count(blocks, 8),
                     'nine_blue_nine_red': conflict_count(blocks, 9)})
    result = {'status': 'PASS', 'method': 'two nonempty block-subset inclusion-exclusion',
              'shape_count': 4, 'rows': rows, 'cpu_seconds': process_time() - started,
              'scope': 'single-center five distinct four-block families covering exactly 18 points; incidence 20',
              'not_performed': ['literal coloring enumeration', 'hypergraph search', 'joint four-center compatibility']}
    Path(__file__).with_name('RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'cpu_seconds': result['cpu_seconds'],
                      'values': [[r['shape'], r['eight_blue_ten_red']['conflict'], r['nine_blue_nine_red']['conflict']] for r in rows]}))

if __name__ == '__main__':
    main()
