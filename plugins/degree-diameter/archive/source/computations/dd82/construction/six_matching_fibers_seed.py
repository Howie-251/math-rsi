"""Expand the explicit degree-one-fiber quotient seed; no search."""
from pathlib import Path
import json
import os
import time


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    started = time.process_time()
    output = Path(__file__).with_suffix('')
    output.mkdir(exist_ok=True)
    quotient = [
        [0, 0, 1, 1, 2, 3],
        [0, 0, 2, 3, 1, 1],
        [1, 2, 0, 1, 3, 0],
        [1, 3, 1, 0, 0, 2],
        [2, 1, 3, 0, 0, 1],
        [3, 1, 0, 2, 1, 0],
    ]
    spoke = [(u + 5) % 10 for u in range(10)]
    rotation = [(u + 1) % 5 for u in range(5)] + [5 + (u + 2) % 5 for u in range(5)]
    p = [set() for _ in range(10)]
    for u in range(10):
        p[u].add(spoke[u])
        p[u].add(rotation[u])
        p[rotation[u]].add(u)
    y = [{u, rotation[u]} for u in range(10)]
    for u in range(10):
        for v in range(10):
            entry = int(spoke[u] == v) + len(y[u] & y[v]) + len(p[u] & p[v])
            assert entry == 1 + 4 * int(u == v)
    edges = set()

    def add(u, v):
        assert u != v
        edges.add(tuple(sorted((u, v))))

    for i in range(6):
        for u in range(5):
            add(10 * i + u, 10 * i + spoke[u])
    for i in range(6):
        for j in range(i + 1, 6):
            for u in range(10):
                targets = {u} if quotient[i][j] == 1 else y[u] if quotient[i][j] == 2 else p[u] if quotient[i][j] == 3 else set()
                for v in targets:
                    add(10 * i + u, 10 * j + v)
    degree = [0] * 60
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    assert len(edges) == 240 and degree == [8] * 60
    seed = dict(n=60, edges=sorted(edges), quotient=quotient,
                coordinate='vertex 10*fiber+u; layers u<5 and u>=5',
                internal_matching=spoke, directed_rotation=rotation,
                q1_interfaces='identity in both orientations',
                q2_interfaces='Y=I+R from lower-index to higher-index fiber, transpose in reverse',
                q3_interfaces='Petersen adjacency P in both orientations',
                same_fiber_matrix_identity_verified=True,
                generator_cpu_seconds=time.process_time() - started,
                graph_search=False)
    path = output / 'seed.edges.json'
    path.write_text(json.dumps(seed, indent=2) + '\n')
    print(json.dumps(dict(path=str(path), n=60, edges=240, degree=8,
                         generator_cpu_seconds=seed['generator_cpu_seconds'])))


if __name__ == '__main__':
    main()
