#!/usr/bin/env python3
"""Run the single parent-selected group only after its capacity/start policy exists."""
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
assert not (HERE / 'run.json').exists(), 'No automatic restart.'
assert (HERE / 'group_definition.json').exists(), 'Await the parent-selected D64 or Q64.'
assert (HERE / 'start_policy.json').exists(), 'Await the parent-selected 64 initial phase codes.'
Q, N, E, D = 64, 256, 16, 8
U = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
V = [1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3]
TREE = [0, 3, 6]
FREE = [e for e in range(E) if e not in TREE]


def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime


begin, wall = cpu(), time.monotonic()
definition = json.loads((HERE / 'group_definition.json').read_text())
policy = json.loads((HERE / 'start_policy.json').read_text())
name, twist = definition['name'], definition['twist']
assert (name, twist) in [('D64', 0), ('Q64', 16)]
assert policy['group_name'] == name
assert policy['edge_u'] == U and policy['edge_v'] == V
assert policy['tree_edge_indices'] == TREE and policy['free_edge_indices'] == FREE
phase_codes = policy['initial_phase_codes']
assert len(phase_codes) == 64 and all(isinstance(c, int) and 0 <= c < 8192 for c in phase_codes)


def mul(g, h):
    x, s = g % 32, g // 32
    y, t = h % 32, h // 32
    return (x + (-1 if s else 1) * y + twist * s * t) % 32 + 32 * (s ^ t)


def inverse(g):
    x, s = g % 32, g // 32
    return (x + twist) % 32 + 32 if s else (-x) % 32


for g in range(Q):
    assert mul(g, 0) == mul(0, g) == g
    assert mul(g, inverse(g)) == mul(inverse(g), g) == 0
(HERE / 'group.txt').write_text(f'{name} {twist}\n')
(HERE / 'topology.txt').write_text('16 3\n' + '\n'.join(f'{a} {b}' for a, b in zip(U, V)) + '\n' + ' '.join(map(str, TREE)) + '\n')


def legal(state):
    return (len(state) == E and all(0 <= g < Q for g in state)
            and all(state[e] == 0 for e in TREE)
            and all(state[e] != state[f] for e in range(E) for f in range(e)
                    if (U[e], V[e]) == (U[f], V[f])))


start_seed, kick_seed = 20261027066, 20261027065
rng = random.Random(start_seed)
starts, used = [], set()
for code in phase_codes:
    while True:
        state, assigned = [0] * E, set(TREE)
        for bit, e in enumerate(FREE):
            phase = (code >> bit) & 1
            forbidden = {state[f] for f in assigned if (U[e], V[e]) == (U[f], V[f])}
            state[e] = rng.choice([x + 32 * phase for x in range(32) if x + 32 * phase not in forbidden])
            assigned.add(e)
        assert legal(state)
        if tuple(state) not in used:
            used.add(tuple(state))
            starts.append(state)
            break
assert len(starts) == 64
(HERE / 'starts.json').write_text(json.dumps({
    'source_seed_count': 0, 'fixed_random_count': 64,
    'group_name': name, 'initial_phase_codes': phase_codes,
    'free_edge_indices_in_bit_order': FREE,
    'start_rng': 'Python random.Random MT19937', 'start_seed': start_seed,
    'kick_rng': 'C++ mt19937_64', 'kick_seed': kick_seed, 'states': starts,
    'extra_x_quotient_or_scaling': False,
}, indent=2) + '\n')
(HERE / 'starts.txt').write_text('64\n' + '\n'.join(' '.join(map(str, s)) for s in starts) + '\n')

# Only the first formal start is independently calibrated; its C++ score is reused.
calibration_start = cpu()
edges = set()
for a, b, h in zip(U, V, starts[0]):
    for g in range(Q):
        target = mul(g, h)
        assert mul(target, inverse(h)) == g
        edges.add((Q * a + g, Q * b + target))
assert len(edges) == 1024 and all(a < b for a, b in edges)
adj = [[] for _ in range(N)]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)
assert all(len(row) == D and len(set(row)) == D for row in adj)
distances, histograms, misses = [], [], []
for root in (0, 64, 128, 192):
    dist = [-1] * N
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    distances.append(dist)
    histograms.append(dict(sorted(Counter(dist).items())))
    misses.append(sum(d < 0 or d > 3 for d in dist))
(HERE / 'first.expected_distances.txt').write_text('\n'.join(' '.join(map(str, d)) for d in distances) + '\n')
(HERE / 'first.expected_adjacency.txt').write_text('\n'.join(' '.join(map(str, sorted(row))) for row in adj) + '\n')
(HERE / 'first.python_check.json').write_text(json.dumps({
    'scope': 'only first formal selected-phase random start; independent full edge set and four complete BFS roots; no all-source test',
    'group_name': name, 'group_twist': twist, 'voltages': starts[0],
    'n': N, 'm': len(edges), 'degree': D, 'root_labels': [0, 64, 128, 192],
    'root_misses': misses, 'root_distance_histograms': histograms,
    'bad_unordered_pairs': Q * sum(misses) // 2,
    'connected': all(-1 not in d for d in distances), 'CPU_seconds': cpu() - calibration_start,
}, indent=2) + '\n')

with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'], cwd=HERE,
                   stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - begin
source_prep = json.loads((HERE / 'preparation.json').read_text())['CPU_seconds']
remaining = 180 - preparation - source_prep - 2
assert remaining > 0
metadata = {
    'mechanism': 'one selected order64 nonabelian group, four regular left-action orbits, K4 multiplicities332',
    'group_definition': definition, 'start_policy': policy,
    'n': N, 'degree': D, 'target_diameter': 3,
    'vertex_encoding': '64*orbit+g; g=x+32*s',
    'edge_u': U, 'edge_v': V, 'tree_edge_indices': TREE, 'free_edge_indices': FREE,
    'free_group_voltage_count': 13, 'extra_x_quotient_or_scaling': False,
    'source_seed_count': 0, 'fixed_random_start_count': 64,
    'start_seed': start_seed, 'kick_seed': kick_seed,
    'segments_per_start_maximum': 9, 'strict_full_coordinate_moves_per_segment_maximum': 30,
    'legality': 'parallel edges have distinct actual group elements; three tree voltages identity; no loops',
    'neighbor_choice': 'all63 alternative group elements for each free edge, choose best strict improvement; legal2-coordinate kick between segments',
    'capacity_filter_during_moves': False,
    'BFS_roots_per_legal_evaluation': 4, 'root_labels': [0, 64, 128, 192],
    'score': 'sum of four radius3 deficits; exact bad unordered pairs=64*sum/2',
    'first_formal_start': 'Python full edge set and four complete distance arrays; pointwise C++ comparison and reuse',
    'family_exhausted': False, 'CPU_budget_seconds': 180, 'worker_count': 1,
    'preparation_CPU_seconds': preparation, 'source_preparation_CPU_seconds': source_prep,
    'production_CPU_limit_seconds': remaining, 'shutdown_reserve_seconds': 2,
    'independent_final': 'parent-owned; one final best all256-root check',
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')


def cap():
    ceiling = math.ceil(remaining) + 1
    resource.setrlimit(resource.RLIMIT_CPU, (ceiling, ceiling))


with (HERE / 'search.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)], cwd=HERE,
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {
        'status': 'RUNNING', 'running': True, 'pid': process.pid, 'driver_pid': os.getpid(),
        'group_name': name, 'worker_count': 1,
        'preparation_CPU_seconds': preparation, 'source_preparation_CPU_seconds': source_prep,
        'process_CPU_limit_seconds': remaining, 'CPU_budget_seconds': 180,
    }
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
total = cpu() - begin + source_prep
run.update(running=False, exit_code=code, total_CPU_seconds=total, restarts=0)
if code == 0:
    terminal = json.loads((HERE / 'search.terminal.json').read_text())
    terminal.update(preparation_CPU_seconds=preparation, source_preparation_CPU_seconds=source_prep,
                    total_CPU_seconds=total, wall_seconds=time.monotonic() - wall,
                    CPU_budget_seconds=180, worker_count=1, restarts=0,
                    independent_final='parent-owned; pending sole final saved best')
    (HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
    run.update(status=terminal['status'], evaluations=terminal['legal_states_evaluated'])
else:
    run['status'] = 'PROCESS_ERROR'
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps(run, indent=2), flush=True)
