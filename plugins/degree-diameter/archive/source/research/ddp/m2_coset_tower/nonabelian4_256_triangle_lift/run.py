#!/usr/bin/env python3
"""One authorized, non-restarting constrained-triangle construction profile."""
from pathlib import Path
import json
import os
import random
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'nonabelian4_256_search'
assert not (HERE / 'run.json').exists(), 'One authorized profile; do not restart'


def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


def mul(g, h):
    x, s = g % 32, g // 32
    y, t = h % 32, h // 32
    return (x + (-y if s else y) + 16 * s * t) % 32 + 32 * (s ^ t)


def inverse(g):
    return (g % 32 + 16) % 32 + 32 if g // 32 else (-g) % 32


def quotient(g):
    return g % 16 + 16 * (g // 32)


def section(q):
    return q % 16 + 32 * (q // 16)


start, wall = cpu(), time.monotonic()
source = json.loads((SOURCE / 'best.json').read_text())
assert source['score']['bad_unordered_pairs'] == 832
eu, ev = source['edge_u'], source['edge_v']
tree = source['tree_edge_indices']
free = [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14]
edge_masks = [0] * 16
for k, e in enumerate(free):
    edge_masks[e] = 1 << k
edge_masks[12] = edge_masks[2] ^ edge_masks[7]
edge_masks[15] = edge_masks[9] ^ edge_masks[11]
assert edge_masks[12] == 18 and edge_masks[15] == 320


def baseline(q):
    h = [0] * 16
    for e in free:
        h[e] = section(q[e])
    h[12] = mul(mul(inverse(h[2]), 16), h[7])
    h[15] = mul(mul(inverse(h[9]), 16), h[11])
    return h


def derive_projection(q):
    h = baseline(q)
    q[12], q[15] = quotient(h[12]), quotient(h[15])
    return q


def legal_projection(q):
    h = baseline(q)
    assert list(map(quotient, h)) == q
    pivots = {}
    for e in range(16):
        for f in range(e):
            if (eu[e], ev[e], q[e]) != (eu[f], ev[f], q[f]):
                continue
            rhs = 1 ^ ((h[e] >> 4) & 1) ^ ((h[f] >> 4) & 1)
            row = edge_masks[e] ^ edge_masks[f] | (rhs << 11)
            for k in range(10, -1, -1):
                if row & (1 << k):
                    if k in pivots:
                        row ^= pivots[k]
                    else:
                        pivots[k] = row
                        break
            else:
                if row & (1 << 11):
                    return False
    return True


q = list(map(quotient, source['voltages']))
assert derive_projection(q.copy()) == q
z = sum(((source['voltages'][e] >> 4) & 1) << k for k, e in enumerate(free))
h0 = baseline(q)
h = [h0[e] ^ (16 * ((z & edge_masks[e]).bit_count() % 2)) for e in range(16)]
assert h == source['voltages'] and z == 198
assert h0[12] == 38 and h0[15] == 63
assert mul(mul(h[2], h[12]), inverse(h[7])) == 16
assert mul(mul(h[9], h[15]), inverse(h[11])) == 16
assert all(q[e] == 0 for e in tree) and legal_projection(q)
dump('source_parameter_check.json', {
    'source_voltages': h, 'baseline_voltages': h0, 'projection': q,
    'independent_edges': free, 'edge_center_masks': edge_masks,
    'center_mask': z, 'full_source_restored': True,
    'triangle_products': [16, 16], 'new_BFS_runs': 0,
})
starts = [q]
rng = random.Random(20261027091)
draws = 0
while len(starts) < 16:
    draws += 1
    candidate = [0] * 16
    for e in free:
        candidate[e] = rng.randrange(32)
    derive_projection(candidate)
    if legal_projection(candidate) and candidate not in starts:
        starts.append(candidate)
dump('starts.json', {
    'source': 'old832 projection;15 fresh constrained legal projections',
    'seed': 20261027091, 'fresh_count': 15,
    'raw_uniform_independent_projection_draws': draws, 'starts': starts,
})
with (HERE / 'starts.txt').open('w') as f:
    f.write('16\n' + '\n'.join(' '.join(map(str, s)) for s in starts) + '\n')
with (HERE / 'input.txt').open('w') as f:
    f.write('16\n' + '\n'.join(f'{a} {b}' for a, b in zip(eu, ev)) + '\n')
    f.write(' '.join(map(str, tree)) + '\n' + ' '.join(map(str, q)) + '\n')
dist = json.loads((SOURCE / 'best.independent_distances.json').read_text())
assert len(dist) == 256 and all(len(r) == 256 for r in dist)
reference = [[v if 0 <= v <= 3 else -1 for v in dist[64 * r]] for r in range(4)]
assert sum(v < 0 for row in reference for v in row) == 26
with (HERE / 'source_reference.txt').open('w') as f:
    f.write(f'{z} 26\n' + '\n'.join(' '.join(map(str, row)) for row in reference) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'],
                   cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
prep = cpu() - start
remaining = 180 - prep - 1
assert remaining > 0
metadata = {
    'status': 'AUTHORIZED_BOUNDED_PROFILE', 'group': 'Q64 central quotient D32',
    'n': 256, 'degree': 8, 'target_D': 3,
    'base_multiplicities': [3, 3, 2, 2, 3, 3], 'tree': tree,
    'independent_edges': free, 'dependent_edges': [12, 15],
    'dependent_full_voltages': ['h12=inv(h2)*c*h7', 'h15=inv(h9)*c*h11'],
    'edge_center_masks': edge_masks,
    'starts': 16, 'source_start': 0, 'fresh_starts': 15,
    'fresh_seed': 20261027091,
    'kick_rng': 'std::mt19937_64 seeded20261027091, separate from Python starts',
    'segments_per_start': 9, 'maximum_strict_moves_per_segment': 30,
    'full_single_coordinate_neighborhood': 341,
    'objective': 'lexicographic(L=2*Nempty+Nsingleton distinct forms,Nempty,minimum center deficit only when L0)',
    'projection_legality': 'general GF2 consistency: equal parallel projections impose (mask_e XOR mask_f).z = 1 XOR baselinebit_e XOR baselinebit_f',
    'phase_filter': None,
    'kicks': 'two distinct independent coordinates changed; dependencies recomputed; legal GF2 required',
    'center_search': 'only L0 projections; exact2048 center assignments subject to general GF2 legality; immediate stop at0',
    'source_calibration': 'four roots*256 saved radius3 entries; no new BFS or source2048 scan',
    'best_policy': 'if no L0, only projection/L; otherwise unique best actual center lift',
    'CPU_budget_seconds': 180, 'worker_count': 1,
    'preparation_compile_CPU_seconds': prep,
    'process_CPU_limit_seconds': remaining, 'entire_family_exhausted': False,
}
dump('metadata.json', metadata)
with (HERE / 'search.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT)
    run = {
        'status': 'RUNNING', 'running': True, 'pid': process.pid,
        'driver_pid': os.getpid(), 'worker_count': 1, 'CPU_budget_seconds': 180,
        'preparation_compile_CPU_seconds': prep,
        'process_CPU_limit_seconds': remaining, 'starts': 16, 'fresh_starts': 15,
    }
    dump('run.json', run)
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Exit {code}; preserve cursor and outputs, no automatic restart'
terminal = json.loads((HERE / 'search.terminal.json').read_text())
total = cpu() - start
terminal.update(
    preparation_compile_CPU_seconds=prep, total_measured_CPU_seconds=total,
    wall_seconds=time.monotonic() - wall, CPU_budget_seconds=180,
    worker_count=1, restarts=0,
    pending=['Root independent final validation of saved graph'] if terminal['saved_graph'] else [],
)
dump('terminal.json', terminal)
run.update(status=terminal['status'], running=False, exit_code=code,
           total_CPU_seconds=total,
           evaluated_legal_projections=terminal['evaluated_legal_projections'],
           best=terminal['best'])
dump('run.json', run)
print(json.dumps(terminal, indent=2), flush=True)
