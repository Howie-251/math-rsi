#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'search.terminal.json').exists(), 'No automatic restart'


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + children.ru_utime + children.ru_stime


start, wall = cpu(), time.monotonic()
old = HERE.parent / 'bicayley172'
best = json.loads((old / 'profile.best.json').read_text())
verified = json.loads((old / 'profile.best.independent_verify.json').read_text())
assert best['pair_counts'] == [0, 0] and best['internal_degree'] == 4 and best['odd_cross'] == 1
f = best['field_values']
A, B = f[:4], f[4:8]
T = [(0, 0), (f[8], 0), (f[9], 1)]
assert A == [0, 4, 11, 37] and B == [41, 16, 12, 24] and T == [(0, 0), (24, 0), (25, 1)]


def group_product(g, h):
    x, j = g
    y, k = h
    return ((x + (-1 if j else 1) * y) % 43, j ^ k)


def encode(side, g):
    return 86 * side + g[0] + 43 * g[1]


reconstructed = set()
for x in range(43):
    for j in range(2):
        g = x, j
        for side, reflections in enumerate([A, B]):
            for a in reflections:
                reconstructed.add(tuple(sorted((encode(side, g), encode(side, group_product(g, (a, 1)))))))
        for t in T:
            reconstructed.add(tuple(sorted((encode(0, g), encode(1, group_product(g, t))))))
data = list(map(int, (old / 'profile.best.edges').read_text().split()))
assert data[:2] == [172, 602] and len(data) == 1206
original = set(zip(data[2::2], data[3::2]))
assert len(original) == 602 and reconstructed == original
edge_u = [0] * 4 + [2] * 4 + [0] * 2 + [1] * 2 + [0, 1]
edge_v = [1] * 4 + [3] * 4 + [2] * 2 + [3] * 2 + [3, 2]
raw = A + B + [0, f[8]] + [0, -f[8] % 43] + [f[9], -f[9] % 43]


def expand(voltages):
    result = set()
    for a, b, voltage in zip(edge_u, edge_v, voltages):
        for x in range(43):
            result.add(tuple(sorted((43 * a + x, 43 * b + (x + voltage) % 43))))
    return result


assert expand(raw) == original
shifts = [0, -raw[0] % 43, -raw[8] % 43, -raw[12] % 43]
seed = [(voltage + shifts[b] - shifts[a]) % 43 for a, b, voltage in zip(edge_u, edge_v, raw)]
assert seed == [0, 4, 11, 37, 16, 34, 30, 42, 0, 24, 18, 37, 0, 18]
permutation = [43 * (v // 43) + (v % 43 + shifts[v // 43]) % 43 for v in range(172)]
image = {tuple(sorted((permutation[u], permutation[v]))) for u, v in original}
assert expand(seed) == image and len(image) == 602
calibration = {
    'status': 'EXACT_EDGE_RELABEL_MATCH', 'old_source': '../bicayley172/profile.best.edges',
    'old_group': 'F43 semidirect_minus1 C2',
    'old_group_product': '(x,j)(y,k)=(x+(-1)^j*y,j+k mod2)',
    'old_A_reflections': A, 'old_B_reflections': B, 'old_cross_T': T,
    'orbit_order': ['A0', 'A1', 'B0', 'B1'], 'encoding': '43*orbit+x',
    'edge_u': edge_u, 'edge_v': edge_v, 'raw_voltages': raw,
    'tree_edge_indices': [0, 8, 12], 'vertex_shifts': shifts,
    'vertex_relabel': 'new_x=old_x+vertex_shifts[orbit] mod43',
    'tree_gauged_seed_voltages': seed,
    'actual_D86_reconstruction_equals_all_old_edges': True,
    'raw_cyclic_voltage_edges_equal_all_old_edges': True,
    'tree_gauged_voltage_edges_equal_all_permuted_old_edges': True,
    'vertices': 172, 'edges': 602, 'new_BFS_runs_in_this_calibration': 0,
    'old_verified_diameter': verified['diameter'],
    'old_verified_bad_pairs': verified['bad_unordered_pairs'],
    'old_verified_ordered_distance_histogram': verified['ordered_distance_histogram'],
    'CPU_seconds': cpu() - start,
}
(HERE / 'calibration.json').write_text(json.dumps(calibration, indent=2) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'], cwd=HERE,
                   stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - start
remaining = 120 - preparation - 1
assert remaining > 0
metadata = {
    'mechanism': 'four-orbit C43 cyclic lift on the fixed4/2/1 multiplicity base',
    'n': 172, 'degree': 7, 'target_diameter': 3,
    'old_raw_parameters': 11, 'new_raw_parameters': 14,
    'old_after_field_translation_gauge': 9, 'new_after_tree_gauge': 11,
    'true_added_parameters_after_gauge': 2,
    'common_scalar_quotient_used': False,
    'tree_edge_indices': [0, 8, 12], 'fixed_tree_voltages': [0, 0, 0],
    'free_edge_indices': [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13],
    'old_coupling_equations_in_tree_gauge': ['v10=v13', 'v9+v11=v13 mod43'],
    'legality': 'voltages on each fixed unordered endpoint pair are distinct',
    'rng_seed': 20261026172, 'starts': 'one exact old seed plus32 distinct legal random starts',
    'segments_per_start_maximum': 9, 'strict_full_coordinate_moves_per_segment_maximum': 30,
    'between_segments': 'change two distinct free coordinates to different legal values',
    'neighbor_choice': 'best strict deficit reduction over the complete legal single-coordinate neighborhood',
    'score': 'sum of all four orbit-root radius3 deficits; exact bad pairs=43*sum/2',
    'full_BFS_roots_per_evaluation': 4, 'root_labels': [0, 43, 86, 129],
    'family_exhausted_by_this_bounded_search': False,
    'CPU_budget_seconds': 120, 'worker_count': 1,
    'preparation_calibration_compile_CPU_seconds': preparation,
    'process_CPU_limit_seconds': remaining,
    'independent_final': 'parent-owned; only final saved best; seed verification can transfer by the exact relabel',
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')


def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'search.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(),
           'worker_count': 1, 'preparation_CPU_seconds': preparation,
           'process_CPU_limit_seconds': remaining, 'CPU_budget_seconds': 120}
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Exit {code}; preserve outputs without restarting'
terminal = json.loads((HERE / 'search.terminal.json').read_text())
total = cpu() - start
terminal.update(preparation_calibration_compile_CPU_seconds=preparation,
                total_preparation_compile_run_CPU_seconds=total,
                wall_seconds=time.monotonic() - wall, CPU_budget_seconds=120,
                worker_count=1, restarts=0,
                independent_final='parent-owned; pending only for sole final saved best')
(HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
run.update(status=terminal['status'], running=False, exit_code=code,
           total_CPU_seconds=total, evaluations=terminal['legal_states_evaluated'])
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps({k: v for k, v in terminal.items() if k != 'per_start'}, indent=2), flush=True)
