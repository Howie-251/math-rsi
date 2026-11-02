#!/usr/bin/env python3
"""Independent literal-edge validator; no producer maps or graph caches are read."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import resource
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (30, 31))
    started = time.process_time()
    result = {
        'checked_UTC': datetime.now(timezone.utc).isoformat(),
        'graph_file': str(args.graph.resolve()),
        'command': [sys.executable, *sys.argv],
        'pid': os.getpid(),
        'input_scope': 'Only the literal n/m edge list; no producer maps or cached balls.',
        'CPU_budget_seconds': 30,
        'expected_n': 3750,
        'expected_m': 37500,
        'expected_degree': 20,
        'target_D': 3,
        'roots_checked': 0,
        'all3750roots_checked': False,
        'new_global_record_claim': False,
        'source_or_old103_reverified': False,
        'complete_Lean_instance': False,
    }
    with args.graph.open() as stream:
        n, declared_m = map(int, next(stream).split())
        assert (n, declared_m) == (3750, 37500)
        adjacency = [[] for _ in range(n)]
        edge_set = set()
        repeated = loops = 0
        edge_rows = 0
        for line in stream:
            if not line.strip():
                continue
            u, v = map(int, line.split())
            assert 0 <= u < n and 0 <= v < n
            edge_rows += 1
            loops += u == v
            edge = (min(u, v), max(u, v))
            repeated += edge in edge_set
            edge_set.add(edge)
            adjacency[u].append(v)
            adjacency[v].append(u)
    degrees = list(map(len, adjacency))
    result.update(n=n, declared_m=declared_m, m=len(edge_set), edge_rows=edge_rows,
                  repeated_edges=repeated, loops=loops,
                  simple=loops == repeated == 0,
                  min_degree=min(degrees), max_degree=max(degrees),
                  degree_histogram=dict(Counter(degrees)),
                  reconstructed_from_literal_edges=True)
    assert result['simple'] and edge_rows == declared_m == len(edge_set)
    assert min(degrees) == max(degrees) == 20
    root_layers = []
    ordered = [0, 0, 0, 0]
    first_counterexample = None
    budget_exhausted = False
    for source in range(n):
        if time.process_time() - started > 28.5:
            budget_exhausted = True
            break
        distances = [-1] * n
        distances[source] = 0
        queue = [source]
        layers = [1, 0, 0, 0]
        for u in queue:
            following = distances[u] + 1
            if following > 3:
                continue
            for v in adjacency[u]:
                if distances[v] == -1:
                    distances[v] = following
                    layers[following] += 1
                    queue.append(v)
        root_layers.append(layers)
        for distance, count in enumerate(layers):
            ordered[distance] += count
        if len(queue) != n:
            first_counterexample = {
                'source': source,
                'first_target_not_reached_within3': distances.index(-1),
                'reached_within3': len(queue),
            }
            break
    passed = len(root_layers) == n and first_counterexample is None
    result.update(
        status='PASS_COMPLETE_LITERAL_GRAPH_D3' if passed else
               'CPU_BUDGET_PARTIAL' if budget_exhausted else 'REFUTED_D3',
        roots_checked=len(root_layers), all3750roots_checked=len(root_layers) == n,
        target_D_passed=passed,
        connected=True if root_layers and sum(root_layers[0]) == n else None,
        diameter_exact=3 if passed and ordered[3] else None,
        ordered_distance_counts_including_self=ordered,
        ordered_counts_scope='All ordered vertex pairs' if passed else 'Only completed roots',
        root_layer_counts=root_layers,
        root_layer_index='Array index is source vertex; columns are distances 0,1,2,3',
        first_counterexample=first_counterexample,
        budget_exhausted=budget_exhausted,
        CPU_seconds=time.process_time() - started,
    )
    if passed:
        assert sum(ordered) == n * n
        assert ordered[0] == n and ordered[1] == 2 * declared_m
        assert all(value % 2 == 0 for value in ordered[1:])
        result['ordinary_unordered_distance_counts'] = {
            str(distance): ordered[distance] // 2 for distance in range(1, 4)
        }
        result['ordinary_bad_unordered_pairs_D3'] = 0
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items()
                      if key != 'root_layer_counts'}, ensure_ascii=False, indent=2))
    return 0 if passed else 2


if __name__ == '__main__':
    raise SystemExit(main())
