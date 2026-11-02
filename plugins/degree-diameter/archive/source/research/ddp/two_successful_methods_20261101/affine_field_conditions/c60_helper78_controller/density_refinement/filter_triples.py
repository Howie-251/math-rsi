#!/usr/bin/env python3
"""Reproduce the exact density candidate classification, without a solver."""
import collections
import itertools
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent


def classify():
    start = time.process_time()
    graph = json.loads((HERE.parents[2] / 'f7_c60_d35/PARAMETERS.json').read_text())['controller']
    neighbors = [set(row) for row in graph]
    masks = [sum(1 << v for v in row) for row in graph]
    histogram = collections.Counter()
    bad, allowed = [], []
    rejected_edges = 0
    for u, v, w in itertools.combinations(range(60), 3):
        if v in neighbors[u] or w in neighbors[u] or w in neighbors[v]:
            rejected_edges += 1
            continue
        size = (masks[u] | masks[v] | masks[w]).bit_count()
        histogram[size] += 1
        (allowed if size >= 14 else bad).append([u, v, w])
    return {'triples_total': 34220, 'rejected_nonindependent': rejected_edges,
            'independent_triples': sum(histogram.values()),
            'independent_neighbor_union_histogram': dict(sorted(histogram.items())),
            'rejected_independent_neighbor_union_below14': len(bad),
            'accepted_independent_neighbor_union_atleast14': len(allowed),
            'enumeration_CPU_seconds': time.process_time() - start,
            'forbidden_independent_triples': bad, 'allowed_triples': allowed}


if __name__ == '__main__':
    result = classify()
    (HERE / 'TRIPLE_FILTER.json').write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps({k: v for k, v in result.items() if not isinstance(v, list)}, indent=2))
