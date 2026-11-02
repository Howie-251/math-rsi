#!/usr/bin/env python3
"""Check each frozen addition's current-graph R4 coverage and degree budget.

The original source graphs' D5 bounds are inherited, not recomputed here.
This is a conditional complete extension proof, not all-source BFS of each graph.
"""
import argparse
from collections import deque
import gzip
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent


def verify(family):
    degree_cap = family['degree']
    with gzip.open(HERE / 'bases' / f'degree{degree_cap}.adjlist.txt.gz', 'rt') as f:
        adjacency = []
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            row = list(map(int, line.split()))
            assert row[0] == len(adjacency)
            neighbors = set(row[1:])
            assert len(neighbors) == len(row) - 1
            adjacency.append(neighbors)
    assert len(adjacency) == family['base']['n']
    assert all(u not in row and len(row) <= degree_cap for u, row in enumerate(adjacency))
    assert all(0 <= v < len(adjacency) and u in adjacency[v]
               for u, row in enumerate(adjacency) for v in row)
    edges = sum(map(len, adjacency)) // 2
    assert edges == family['base']['m']
    checks = []
    for step in family['steps']:
        n = len(adjacency)
        assert step['source_n'] == step['new_vertex'] == n
        assert step['source_m'] == edges
        pins = step['pins']
        assert pins == sorted(set(pins)) and len(pins) <= degree_cap
        assert all(0 <= v < n and len(adjacency[v]) < degree_cap for v in pins)
        assert [len(adjacency[v]) for v in pins] == step['old_pin_degrees']
        seen = bytearray(n)
        queue = deque()
        for pin in pins:
            seen[pin] = 1
            queue.append((pin, 0))
        reached = len(pins)
        while queue:
            u, distance = queue.popleft()
            if distance == 4:
                continue
            for v in adjacency[u]:
                if not seen[v]:
                    seen[v] = 1
                    reached += 1
                    queue.append((v, distance + 1))
        assert reached == n, (degree_cap, step['new_n'], 'uncovered current vertices', n - reached)
        for pin in pins:
            adjacency[pin].add(n)
        adjacency.append(set(pins))
        edges += len(pins)
        assert len(adjacency) == step['new_n'] and edges == step['new_m']
        checks.append({'order': len(adjacency), 'edges': edges, 'old_vertices_covered': reached,
                       'current_R4_complete': True, 'degree_budget_pass': True})
    return {'degree': degree_cap, 'base_order': family['base']['n'],
            'inherited_source_D_at_most': 5, 'source_distance_rechecked': False,
            'complete_extension_checks': len(checks), 'steps': checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degree', type=int, choices=[11, 12, 13])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.process_time()
    families = json.loads((HERE / 'families.json').read_text())['families']
    selected = [args.degree] if args.degree else [11, 12, 13]
    results = [verify(families[str(d)]) for d in selected]
    report = {'status': 'PASS_ALL_SELECTED_CURRENT_GRAPH_COVERS',
              'extension_graphs_checked': sum(x['complete_extension_checks'] for x in results),
              'all_source_BFS_executed': False, 'source_D5_inherited': True,
              'CPU_seconds': time.process_time() - start, 'families': results}
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'families'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
