#!/usr/bin/env python3
"""Conditional literal verifier for fixed-P joint-port365, not executed at preparation.
Only standard-library code; no producer route masks, matching model or solver imports.
"""
import argparse
from collections import Counter, deque
import csv
import json
from pathlib import Path
from time import process_time

OLD_N, OLD_M, N, M = 364, 714, 365, 730
CUTS = {(43, 58), (151, 314)}
PINS = {43, 58, 151, 314}


def read_graph(path, n, m, require_header):
    edges = set()
    first = True
    with Path(path).open() as stream:
        for line_number, line in enumerate(stream, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            fields = line.split()
            if len(fields) != 2:
                raise ValueError(f'{path}:{line_number}: expected two integers')
            u, v = map(int, fields)
            if first:
                first = False
                if (u, v) == (n, m):
                    continue
                if require_header:
                    raise ValueError(f'{path}: expected {n} {m} header')
            if not (0 <= u < n and 0 <= v < n) or u == v:
                raise ValueError(f'{path}:{line_number}: invalid edge')
            edge = (min(u, v), max(u, v))
            if edge in edges:
                raise ValueError(f'{path}:{line_number}: duplicate edge')
            edges.add(edge)
    if len(edges) != m:
        raise ValueError(f'{path}: expected {m} edges, got {len(edges)}')
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    for row in adjacency:
        row.sort()
    return edges, adjacency


def bfs(adjacency, root):
    distance, parent = [-1] * N, [-1] * N
    distance[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
    return distance, parent


def route(parent, root, target):
    path = [target]
    while path[-1] != root:
        previous = parent[path[-1]]
        if previous < 0:
            return []
        path.append(previous)
    return path[::-1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--candidate', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--cpu-budget', required=True, type=float)
    args = parser.parse_args()
    if args.cpu_budget <= 0:
        parser.error('--cpu-budget must be positive')
    started = process_time()
    out = Path(args.out);out.mkdir(parents=True, exist_ok=True)
    result = {'status': 'STARTED_NOT_ACCEPTED', 'all_pair_pass': False,
              'source_parse_count': 0, 'candidate_parse_count': 0,
              'source_BFS_roots': 0, 'candidate_BFS_roots': 0,
              'source_file': str(Path(args.source).resolve()),
              'candidate_file': str(Path(args.candidate).resolve()),
              'CPU_budget_seconds': args.cpu_budget,
              'producer_masks_or_model_imported': False}
    try:
        result['source_parse_count'] = 1
        source, source_adj = read_graph(args.source, OLD_N, OLD_M, False)
        ports = {v for v, row in enumerate(source_adj) if len(row) == 3}
        core = {v for v, row in enumerate(source_adj) if len(row) == 4}
        if len(ports) != 28 or len(core) != 336 or ports | core != set(range(OLD_N)):
            raise ValueError('Source literal is not the natural364/714 with28ports')
        if not CUTS <= source or not PINS <= core:
            raise ValueError('Fixed two source core cuts are not bound')
        result['candidate_parse_count'] = 1
        final, adjacency = read_graph(args.candidate, N, M, True)
        if any(len(row) != 4 for row in adjacency):
            raise ValueError('Candidate is not simple4regular')
        if set(adjacency[OLD_N]) != PINS:
            raise ValueError('New star is not the frozen P={43,58,151,314}')
        final_old = {(u, v) for u, v in final if v < OLD_N}
        removed = source - final_old
        matching = final_old - source
        if removed != CUTS:
            raise ValueError('Actual removed source edges differ from the fixedcuts')
        if len(matching) != 14:
            raise ValueError('Actual added old-old edges are not14portmatchingedges')
        matching_degree = Counter()
        for u, v in matching:
            if u not in ports or v not in ports:
                raise ValueError('New old-old edge has a nonport endpoint')
            matching_degree[u] += 1;matching_degree[v] += 1
        if set(matching_degree) != ports or set(matching_degree.values()) != {1}:
            raise ValueError('Actual port edges do not form a perfectmatching')
        expected = (source - CUTS) | matching | {(u, OLD_N) for u in PINS}
        if final != expected:
            raise ValueError('Literal candidate edge delta is not the authorizedrule')
        delta = {'removed_source_edges': sorted(CUTS),
                 'added_port_matching': sorted(matching), 'new_star_pins': sorted(PINS),
                 'old_source_edges_retained': len(source - CUTS),
                 'candidate_degree_histogram': {'4': N}}
        (out / 'ACTUAL_EDGE_DELTA.json').write_text(json.dumps(delta, indent=2) + '\n')
        result.update({'literal_binding_pass': True, 'n': N, 'm': M,
                       'degree_histogram': {'4': N}, 'old_edges_retained': 712,
                       'old_edges_deleted': 2, 'new_port_edges': 14, 'star_edges': 4})
        witness5 = None
        diameter = 0
        roots = [OLD_N] + list(range(OLD_N))
        with (out / 'ALL_ROOT_BFS.csv').open('w', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(['root', 'eccentricity', 'unreachable', 'distance_histogram'])
            for root in roots:
                if process_time() - started >= args.cpu_budget:
                    result['status'] = 'UNKNOWN_FRESH_CPU_BUDGET'
                    result['next_unchecked_root'] = root
                    break
                distance, parent = bfs(adjacency, root)
                hist = Counter(distance)
                unreachable = hist.get(-1, 0)
                ecc = None if unreachable else max(distance)
                writer.writerow([root, ecc, unreachable, json.dumps(dict(sorted(hist.items())))])
                result['candidate_BFS_roots'] += 1
                if unreachable or ecc > 5:
                    target = next(t for t, dt in enumerate(distance) if dt < 0 or dt > 5)
                    failure = {'root': root, 'target': target, 'distance': distance[target],
                               'shortest_path': route(parent, root, target) if distance[target] >= 0 else []}
                    result['status'] = 'FAIL_ACTUAL_CANDIDATE_D5'
                    result['first_failure'] = failure
                    (out / 'FIRST_BFS_FAILURE.json').write_text(json.dumps(failure, indent=2) + '\n')
                    break
                diameter = max(diameter, ecc)
                if witness5 is None and 5 in hist:
                    target = next(t for t, dt in enumerate(distance) if dt == 5)
                    witness5 = {'root': root, 'target': target, 'distance': 5,
                                'shortest_path': route(parent, root, target)}
            else:
                result.update({'status': 'PASS_FRESH365_ALL_ROOTS', 'all_pair_pass': True,
                               'actual_diameter': diameter, 'ordered_pairs': N * N})
        if witness5 is not None:
            result['actual_distance5_witness'] = witness5
            (out / 'DISTANCE5_WITNESS.json').write_text(json.dumps(witness5, indent=2) + '\n')
        result['unmeasured_candidate_roots'] = N - result['candidate_BFS_roots']
    except (OSError, ValueError) as error:
        result['status'] = 'FAIL_LITERAL_BINDING'
        result['error'] = str(error)
    result['process_CPU_seconds'] = process_time() - started
    (out / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    terminal = {'terminal': True, 'status': result['status'],
                'all_pair_pass': result['all_pair_pass'], 'root_accepted': False,
                'candidate_BFS_roots': result['candidate_BFS_roots'], 'source_BFS_roots': 0,
                'process_CPU_seconds': result['process_CPU_seconds']}
    (out / 'TERMINAL.json').write_text(json.dumps(terminal, indent=2) + '\n')
    print(json.dumps(terminal))
    return 0 if result['all_pair_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
