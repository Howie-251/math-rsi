#!/usr/bin/env python3
"""Conditional independent verifier; prepare only until root authorizes a fresh run.

No producer modules, endpoint masks, CNF or SAT assignment are imported.
All distance traversals are on the actual 1368-point candidate, never its source.
"""
import argparse
from collections import Counter, deque
import csv
import json
from pathlib import Path
from time import process_time

N0 = 684
M0 = 2394
N = 1368
M = 5472


def read_edges(path, n, m, header_required):
    edges = set()
    first = True
    had_header = False
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
                    had_header = True
                    continue
                if header_required:
                    raise ValueError(f'{path}: expected header {n} {m}')
            if not (0 <= u < n and 0 <= v < n) or u == v:
                raise ValueError(f'{path}:{line_number}: invalid edge')
            if u > v:
                u, v = v, u
            if (u, v) in edges:
                raise ValueError(f'{path}:{line_number}: duplicate edge')
            edges.add((u, v))
    if len(edges) != m:
        raise ValueError(f'{path}: expected {m} distinct edges, got {len(edges)}')
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    for neighbors in adjacency:
        neighbors.sort()
    return edges, adjacency, had_header


def decode(v):
    tau, h = divmod(v, 342)
    a, b = divmod(h, 9)
    epsilon = a % 2
    return 18 * tau + 2 * b + epsilon, (a - epsilon) // 2


def encode(r, k):
    tau, q = divmod(r, 18)
    b, epsilon = divmod(q, 2)
    return 342 * tau + 9 * (epsilon + 2 * k) + b


def bfs(adjacency, root):
    distance = [-1] * N
    parent = [-1] * N
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
    result = [target]
    while result[-1] != root:
        q = parent[result[-1]]
        if q < 0:
            return []
        result.append(q)
    return result[::-1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, help='Accepted 684-point literal; optional header')
    parser.add_argument('--candidate', required=True, help='Actual 1368 5472 header edge file')
    parser.add_argument('--out', required=True)
    parser.add_argument('--cpu-budget', type=float, required=True)
    args = parser.parse_args()
    if args.cpu_budget <= 0:
        parser.error('--cpu-budget must be positive')
    started = process_time()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    result = {
        'status': 'STARTED_NOT_ACCEPTED',
        'source_file': str(Path(args.source).resolve()),
        'candidate_file': str(Path(args.candidate).resolve()),
        'source_parse_count': 0,
        'candidate_parse_count': 0,
        'source_BFS_roots': 0,
        'candidate_BFS_roots': 0,
        'CPU_budget_seconds': args.cpu_budget,
        'producer_code_or_masks_imported': False,
        'all_pair_pass': False,
    }
    try:
        result['source_parse_count'] = 1
        source_edges, source_adj, _ = read_edges(args.source, N0, M0, False)
        if any(len(a) != 7 for a in source_adj):
            raise ValueError('Literal source input is not 7-regular')
        result['candidate_parse_count'] = 1
        edges, adjacency, _ = read_edges(args.candidate, N, M, True)
        if any(len(a) != 8 for a in adjacency):
            raise ValueError('Candidate is not 8-regular')
        old0 = {(u, v) for u, v in edges if v < N0}
        old1 = {(u-N0, v-N0) for u, v in edges if u >= N0}
        if old0 != source_edges or old1 != source_edges:
            raise ValueError('Candidate induced copies do not equal literal source')
        matching0 = [-1] * N0
        matching1 = [-1] * N0
        cross = 0
        for u, v in edges:
            if u < N0 <= v:
                w = v - N0
                if matching0[u] >= 0 or matching1[w] >= 0:
                    raise ValueError('Cross edges are not a matching')
                matching0[u] = w
                matching1[w] = u
                cross += 1
        if cross != N0 or min(matching0) < 0 or min(matching1) < 0:
            raise ValueError('Cross edges are not a perfect matching')
        actual_map = []
        for r in range(36):
            s, shift = decode(matching0[encode(r, 0)])
            for k in range(19):
                s2, k2 = decode(matching0[encode(r, k)])
                if s2 != s or k2 != (k + shift) % 19:
                    raise ValueError(f'Actual matching violates K19 equivariance at orbit {r}')
            actual_map.append((r, s, shift, 19))
        if len({q[1] for q in actual_map}) != 36:
            raise ValueError('Actual orbit map is not a permutation')
        with (out / 'ACTUAL_K19_MATCHING.tsv').open('w', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t')
            writer.writerow(['source_orbit', 'target_orbit', 'shift', 'actual_points_bound'])
            writer.writerows(actual_map)
        result.update({
            'literal_structure_pass': True,
            'n': N, 'm': M, 'degree_histogram': {'8': N},
            'retained_source_edges_copy0': len(old0),
            'retained_source_edges_copy1': len(old1),
            'retained_source_edges_total': len(old0) + len(old1),
            'cross_perfect_matching_edges': cross,
            'actual_K19_matching_bound': True,
            'actual_orbit0_shift': actual_map[0][2],
            'orbit_label_schema': 'r=18*tau+2*b+epsilon; oldlabel=342*tau+9*(epsilon+2*k)+b',
        })
        maximum = 0
        witness4 = None
        with (out / 'ALL_ROOT_BFS.csv').open('w', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(['root', 'eccentricity', 'unreachable', 'distance_histogram'])
            for root in range(N):
                if process_time() - started >= args.cpu_budget:
                    result['status'] = 'UNKNOWN_FRESH_CPU_BUDGET'
                    result['next_unchecked_root'] = root
                    break
                distance, parent = bfs(adjacency, root)
                hist = Counter(distance)
                unreachable = hist.get(-1, 0)
                ecc = max(distance) if not unreachable else None
                writer.writerow([root, ecc, unreachable, json.dumps(dict(sorted(hist.items())))])
                result['candidate_BFS_roots'] += 1
                if unreachable or ecc > 4:
                    target = next(v for v, dv in enumerate(distance) if dv < 0 or dv > 4)
                    failure = {'root': root, 'target': target, 'distance': distance[target],
                               'shortest_path': route(parent, root, target) if distance[target] >= 0 else []}
                    (out / 'FIRST_BFS_FAILURE.json').write_text(json.dumps(failure, indent=2) + '\n')
                    result['status'] = 'FAIL_ACTUAL_CANDIDATE_D4'
                    result['first_failure'] = failure
                    break
                maximum = max(maximum, ecc)
                if witness4 is None and 4 in hist:
                    target = next(v for v, dv in enumerate(distance) if dv == 4)
                    witness4 = {'root': root, 'target': target, 'distance': 4,
                                'shortest_path': route(parent, root, target)}
            else:
                result.update({'status': 'PASS_FRESH_ACTUAL1368_ALL_ROOTS',
                               'all_pair_pass': True, 'actual_diameter': maximum,
                               'ordered_pairs': N * N})
        if witness4 is not None:
            (out / 'ACTUAL_DISTANCE4_WITNESS.json').write_text(json.dumps(witness4, indent=2) + '\n')
            result['distance4_witness'] = witness4
        result['unmeasured_candidate_roots'] = N - result['candidate_BFS_roots']
    except (OSError, ValueError) as error:
        result['status'] = 'FAIL_LITERAL_INPUT_OR_SCOPE_BINDING'
        result['error'] = str(error)
    result['process_CPU_seconds'] = process_time() - started
    (out / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    terminal = {'terminal': True, 'status': result['status'],
                'fresh_graph_accepted_by_root': False,
                'all_pair_pass': result['all_pair_pass'],
                'process_CPU_seconds': result['process_CPU_seconds'],
                'candidate_BFS_roots': result['candidate_BFS_roots'],
                'source_BFS_roots': 0}
    (out / 'TERMINAL.json').write_text(json.dumps(terminal, indent=2) + '\n')
    print(json.dumps(terminal))
    return 0 if result['all_pair_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
