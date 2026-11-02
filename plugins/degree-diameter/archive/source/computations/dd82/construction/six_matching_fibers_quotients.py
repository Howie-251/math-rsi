"""Complete necessary-quotient screen for six matching fibers of size ten.

Analytic bounds force the three listed row types. Enumerate every labeled
symmetric matrix built from those types, then check every cross capacity.
No graph solver or 60-vertex graph search is used.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path
import json
import os
import resource
import time


def main():
    output = Path(__file__).with_suffix('.json')
    assert not output.exists(), 'No unchanged rerun'
    cpu = min(os.sched_getaffinity(0))
    os.sched_setaffinity(0, {cpu})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    started_cpu, started_wall = time.process_time(), time.monotonic()
    row_types = [(3, 3, 1, 0, 0), (3, 2, 2, 0, 0), (3, 2, 1, 1, 0)]
    patterns = sorted({p for row in row_types for p in permutations(row)})
    options = []
    for i in range(6):
        by_prefix = defaultdict(list)
        for pattern in patterns:
            row = pattern[:i] + (0,) + pattern[i:]
            by_prefix[row[:i]].append(row)
        options.append(by_prefix)
    pairs = list(combinations(range(6), 2))
    q = [[0] * 6 for _ in range(6)]
    complete = 0
    minima = Counter()
    survivors = set()
    best_minimum, best_q = -1, None

    def visit(i):
        nonlocal complete, best_minimum, best_q
        if i == 6:
            complete += 1
            minimum = min(3 * q[a][b] + sum(q[a][k] * q[k][b] for k in range(6))
                          for a, b in pairs)
            minima[minimum] += 1
            if minimum > best_minimum:
                best_minimum, best_q = minimum, [row[:] for row in q]
            if minimum >= 10:
                survivors.add(tuple(q[a][b] for a, b in pairs))
            return
        prefix = tuple(q[i][:i])
        for row in options[i].get(prefix, ()):
            for j in range(i + 1, 6):
                q[i][j] = q[j][i] = row[j]
            visit(i + 1)
        for j in range(i + 1, 6):
            q[i][j] = q[j][i] = 0

    visit(0)
    remaining = set(survivors)
    orbits = []
    while remaining:
        code = min(remaining)
        matrix = [[0] * 6 for _ in range(6)]
        for (i, j), value in zip(pairs, code):
            matrix[i][j] = matrix[j][i] = value
        orbit = {tuple(matrix[p[i]][p[j]] for i, j in pairs) for p in permutations(range(6))}
        assert orbit <= survivors
        remaining.difference_update(orbit)
        capacities = [[None if i == j else 3 * matrix[i][j] +
                       sum(matrix[i][k] * matrix[k][j] for k in range(6))
                       for j in range(6)] for i in range(6)]
        orbits.append(dict(Q=matrix, labeled_orbit_size=len(orbit), cross_capacities=capacities))
    result = dict(
        scope='All symmetric zero-diagonal integer 6x6 Q with row sum seven surviving the proved row bounds',
        row_types=row_types,
        distinct_row_patterns=len(patterns),
        symmetric_labeled_matrices=complete,
        minimum_cross_capacity_histogram=dict(sorted(minima.items())),
        best_minimum_cross_capacity=best_minimum,
        best_quotient=best_q,
        surviving_labeled_matrices=len(survivors),
        surviving_unlabeled_matrices=len(orbits),
        survivors_up_to_S6=orbits,
        cpu_seconds=time.process_time() - started_cpu,
        wall_seconds=time.monotonic() - started_wall,
        pinned_cpu=cpu,
        cpu_limit_seconds=10,
        solver_used=False,
        full_graph_search=False,
    )
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
