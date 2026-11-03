"""Construct one exact double interface for each allowed internal-type pair.

Four direct matrix checks; no graph search, permutation enumeration, or SAT.
"""
from pathlib import Path
import json
import os
import time


def internal(kind):
    matrix = [[0] * 10 for _ in range(10)]
    cycles = [list(range(10))] if kind == 'C10' else [list(range(5)), list(range(5, 10))]
    for cycle in cycles:
        for i, u in enumerate(cycle):
            v = cycle[(i + 1) % len(cycle)]
            matrix[u][v] = matrix[v][u] = 1
    return matrix


def main():
    cpu = min(os.sched_getaffinity(0))
    os.sched_setaffinity(0, {cpu})
    start = time.process_time()
    neighbors = [[(2 * u) % 5, 5 + (2 * u) % 5] for u in range(10)]
    y = [[int(v in neighbors[u]) for v in range(10)] for u in range(10)]
    assert all(sum(row) == 2 for row in y)
    assert all(sum(y[u][v] for u in range(10)) == 2 for v in range(10))
    checks = []
    for left in ('C10', '2C5'):
        for right in ('C10', '2C5'):
            d, e = internal(left), internal(right)
            counts = [[y[u][v] + sum(d[u][k] * y[k][v] + y[u][k] * e[k][v]
                                     for k in range(10))
                       for v in range(10)] for u in range(10)]
            assert all(value == 1 for row in counts for value in row)
            checks.append(dict(left=left, right=right, minimum_entry=1, maximum_entry=1,
                               exact_interface_equation=True))
    result = dict(scope='One explicit local interface for each allowed ordered internal-type pair; no full 60-vertex graph',
                  Y=y, neighbor_rows=neighbors, checks=checks,
                  cpu_seconds=time.process_time() - start, pinned_cpu=cpu,
                  graph_search=False, solver_used=False)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key not in ('Y', 'neighbor_rows')}, indent=2))


if __name__ == '__main__':
    main()
