#!/usr/bin/env python3
from collections import Counter, deque
from pathlib import Path
import json
import math
import os
import random
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'search.terminal.json').exists(), 'No automatic restart'
Q, N = 43, 172
EDGE_U = [0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 0, 0, 1, 1]
EDGE_V = [1, 1, 1, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2]
TREE = [0, 6, 10]
FREE = [e for e in range(14) if e not in TREE]


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + child.ru_utime + child.ru_stime


start, wall = cpu(), time.monotonic()
base_adjacency = [[] for _ in range(4)]
for e, (a, b) in enumerate(zip(EDGE_U, EDGE_V)):
    base_adjacency[a].append((b, e, 1))
    base_adjacency[b].append((a, e, -1))
assert list(map(len, base_adjacency)) == [7] * 4
capacity_begin = cpu()
counts, projected_counts, raw_counts = [], [], []
for root in range(4):
    forms = [set() for _ in range(4)]
    raw = [0] * 4
    level = [(root, -1, (0,) * 14)]
    forms[root].add((0,) * 14)
    raw[root] += 1
    for length in range(1, 4):
        next_level = []
        for vertex, last_edge, coeff in level:
            for target, edge, direction in base_adjacency[vertex]:
                if edge == last_edge:
                    continue
                v = list(coeff)
                v[edge] = (v[edge] + direction) % Q
                v = tuple(v)
                forms[target].add(v)
                raw[target] += 1
                next_level.append((target, edge, v))
        level = next_level
    assert sum(raw) == 302
    counts.append(list(map(len, forms)))
    projected_counts.append([len({tuple(v[e] for e in FREE) for v in cell}) for cell in forms])
    raw_counts.append(raw)


def off_capacity(a, b, c):
    return a + 2 * b * c + a * a * (a - 1) // 2 + a * (3 * b * b + 3 * c * c - 2 * b - 2 * c)


a, b, c = 3, 2, 2
diag = 1 + sum(m * (m - 1) for m in (a, b, c)) + 6 * a * b * c
fa, fb, fc = off_capacity(a, b, c), off_capacity(b, a, c), off_capacity(c, a, b)
formula = [[diag, fa, fb, fc], [fa, diag, fc, fb], [fb, fc, diag, fa], [fc, fb, fa, diag]]
assert counts == projected_counts == formula == [[83, 68, 74, 74], [68, 83, 74, 74], [74, 74, 83, 68], [74, 74, 68, 83]]
(HERE / 'CAPACITY_CHECK.json').write_text(json.dumps({
    'scope': 'all reduced base walks of lengths0..3 from all4 roots, symbolic voltage forms only',
    'edge_u': EDGE_U, 'edge_v': EDGE_V, 'tree_edge_indices': TREE,
    'raw_walk_counts': raw_counts, 'distinct_voltage_form_counts': counts,
    'tree_gauge_projected_counts': projected_counts, 'analytic_formula_counts': formula,
    'all_counts_match': True, 'needed_each_fiber': 43, 'minimum_capacity': 68,
    'graph_generated_by_this_capacity_calculation': False,
    'CPU_seconds': cpu() - capacity_begin,
}, indent=2) + '\n')

start_seed, kick_seed = 20261026322, 20261026323
rng = random.Random(start_seed)
starts = []
for i in range(64):
    while True:
        state = [0] * 14
        for edge in FREE:
            unavailable = {state[e] for e in range(edge) if (EDGE_U[e], EDGE_V[e]) == (EDGE_U[edge], EDGE_V[edge])}
            state[edge] = rng.choice([v for v in range(Q) if v not in unavailable])
        if state not in starts:
            starts.append(state)
            break
assert all(len({v[e] for e in range(14) if EDGE_U[e] == a and EDGE_V[e] == b}) == sum(EDGE_U[e] == a and EDGE_V[e] == b for e in range(14)) for v in starts for a, b in set(zip(EDGE_U, EDGE_V)))
(HERE / 'starts.json').write_text(json.dumps({'start_rng': 'Python random.Random MT19937', 'start_seed': start_seed,
                                             'kick_rng': 'C++ mt19937_64', 'kick_seed': kick_seed,
                                             'states': starts}, indent=2) + '\n')
(HERE / 'starts.txt').write_text('64\n' + '\n'.join(' '.join(map(str, v)) for v in starts) + '\n')

# One independent Python construction/BFS for the first formal random start.
calibration_begin = cpu()
edges = set()
for source, target, voltage in zip(EDGE_U, EDGE_V, starts[0]):
    for x in range(Q):
        edges.add(tuple(sorted((Q * source + x, Q * target + (x + voltage) % Q))))
assert len(edges) == 602 and all(u != v for u, v in edges)
adjacency = [[] for _ in range(N)]
for u, v in edges:
    adjacency[u].append(v)
    adjacency[v].append(u)
assert all(len(v) == 7 for v in adjacency)
distances, histograms, misses = [], [], []
for root in [0, 43, 86, 129]:
    d = [-1] * N
    d[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                queue.append(v)
    distances.append(d)
    histograms.append(dict(sorted(Counter(d).items())))
    misses.append(sum(t < 0 or t > 3 for t in d))
(HERE / 'first.expected_distances.txt').write_text('\n'.join(' '.join(map(str, d)) for d in distances) + '\n')
(HERE / 'first.python_check.json').write_text(json.dumps({
    'scope': 'Only formal random start0; independent Python edge set and4 complete roots, no all-source test',
    'voltages': starts[0], 'n': N, 'm': len(edges), 'degree': 7,
    'root_misses': misses, 'root_distance_histograms': histograms,
    'bad_unordered_pairs': Q * sum(misses) // 2,
    'connected': all(-1 not in d for d in distances),
    'CPU_seconds': cpu() - calibration_begin,
}, indent=2) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'], cwd=HERE,
                   stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - start
remaining = 180 - preparation - 1
assert remaining > 0
metadata = {
    'mechanism': 'four-orbit C43 cyclic lift on balancedK4 multiplicities3/2/2',
    'n': 172, 'degree': 7, 'target_diameter': 3,
    'edge_u': EDGE_U, 'edge_v': EDGE_V, 'tree_edge_indices': TREE, 'free_edge_indices': FREE,
    'tree_gauge_dimension': 11, 'common_scalar_quotient_used': False,
    'old421_starts_used': 0, 'random_start_count': 64,
    'start_seed': start_seed, 'kick_seed': kick_seed,
    'segments_per_start_maximum': 9, 'strict_full_coordinate_moves_per_segment_maximum': 30,
    'neighbor_choice': 'best strict improvement over all legal single-coordinate values; no capacity filtering',
    'legality': 'distinct voltages within each fixed endpoint pair',
    'full_BFS_roots_per_evaluation': 4, 'root_labels': [0, 43, 86, 129],
    'score': 'sum of four root radius3 deficits; bad unordered pairs=43*sum/2',
    'first_formal_start': 'independent Python edge construction and4roots; C++ first score compared pointwise and reused',
    'family_exhausted_by_this_bounded_search': False,
    'CPU_budget_seconds': 180, 'worker_count': 1,
    'preparation_capacity_calibration_compile_CPU_seconds': preparation,
    'process_CPU_limit_seconds': remaining,
    'independent_final': 'parent-owned, only the final saved best',
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')


def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'search.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(), 'worker_count': 1,
           'preparation_CPU_seconds': preparation, 'process_CPU_limit_seconds': remaining,
           'CPU_budget_seconds': 180}
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Exit {code}; preserve outputs without restarting'
terminal = json.loads((HERE / 'search.terminal.json').read_text())
total = cpu() - start
terminal.update(preparation_capacity_calibration_compile_CPU_seconds=preparation,
                total_preparation_compile_run_CPU_seconds=total,
                wall_seconds=time.monotonic() - wall, CPU_budget_seconds=180,
                worker_count=1, restarts=0,
                independent_final='parent-owned; pending only for sole final saved best')
(HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
run.update(status=terminal['status'], running=False, exit_code=code,
           total_CPU_seconds=total, evaluations=terminal['legal_states_evaluated'])
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps({k: v for k, v in terminal.items() if k != 'per_start'}, indent=2), flush=True)
