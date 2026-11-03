#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'capacity.terminal.json').exists(), 'No automatic restart'

def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + children.ru_utime + children.ru_stime

start, wall = cpu(), time.monotonic()
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'capacity.cpp', '-o', 'capacity'],
                   cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
compile_cpu = cpu() - start
subprocess.run([str(HERE / 'capacity'), 'calibrate', str(HERE), '0'], check=True)
sys.path.insert(0, str(HERE.parent / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
cases = json.loads((HERE / 'calibration.cpp.json').read_text())
product = [[(j + k) % 30 for k in range(30)] for j in range(30)]
inverse = [(-j) % 30 for j in range(30)]
scalar = [pow(3, j, 31) for j in range(30)]
assert len(set(scalar)) == 30
checks = []
for case in cases:
    components = [{'phase': k, 'kind': 'pair'} for k in case['pair_phases']]
    components += [{'phase': 15, 'kind': 'involution'} for _ in range(case['involution_count'])]
    reference = affine_word_forms(31, product, inverse, scalar, components)
    assert reference['raw_counts'] == case['raw_capacity']
    assert reference['form_counts'] == case['form_counts']
    packed = [sorted(sum(x << (5 * i) for i, x in enumerate(coeff)) for coeff in forms)
              for forms in reference['forms']]
    assert packed == case['packed_forms']
    checks.append({'degree': case['degree'], 'pair_phases': case['pair_phases'],
                   'involution_count': case['involution_count'], 'all_30_form_sets_match': True,
                   'convolution_counts_match_direct_reduced_words': True,
                   'graph_or_field_assignment_tested': False})
preparation = cpu() - start
(HERE / 'calibration.check.json').write_text(json.dumps({
    'status': 'PASS_TWO_NEW_PURE_SYMBOLIC_CASES', 'checks': checks,
    'compile_CPU_seconds': compile_cpu,
    'preparation_compile_calibration_CPU_seconds': preparation,
    'reference_function': '../axis_cayley272/symbolic_affine_words.py',
}, indent=2) + '\n')
metadata = {
    'group': 'F31 additive semidirect_3 C30', 'order': 930, 'r': 3, 'action_order': 30,
    'degrees': [11, 12], 'target_diameter': 3, 'saved_thresholds': {'11': 715, '12': 810},
    'Moore_bounds': {'11': 1222, '12': 1597},
    'phase_pair_classes': list(range(15)), 'involution_phase': 15,
    'inverse_pair_counts': [15] + [31] * 14, 'nonidentity_involutions': 31,
    'group_product': '(x,j)(y,k)=(x+3^j*y mod31,j+k mod30)',
    'inverse': '(-3^-j*x mod31,-j mod30)',
    'pattern_order': 'degree11 then12, increasing pair count, lexicographic nondecreasing pair phases',
    'degree11_patterns': 15504, 'degree12_patterns': 54264, 'total_patterns': 69768,
    'component_order': 'inverse-pair representatives then independent phase15 involutions',
    'packed_form_encoding': 'coefficient_i occupies bits5i..5i+4; values0..30',
    'ordinary_capacity': 'a*a*a + a*a + (2-2d)*a + (1-d)*delta0 in Z[C30]',
    'necessary_capacity_each_phase': 31,
    'normalization': 'first chi!=1 component set0 by common translation; all nonzero remaining vectors modulo common scalar',
    'projective_count_per_pattern': '(31^(m-1)-1)/30, m=degree-pair_count',
    'no_additional_quotient_units_or_slot_permutation_reduction': True,
    'CPU_budget_seconds': 120, 'worker_count': 1,
    'graphs_generated': 0, 'field_assignments_tested': 0, 'BFS_runs': 0,
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
remaining = 120 - preparation - 1
assert remaining > 0

def cap():
    value = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (value, value))

with (HERE / 'capacity.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'capacity'), 'run', str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(),
           'worker_count': 1, 'start_cursor': 0, 'scope_patterns': 69768,
           'preparation_CPU_seconds': preparation,
           'remaining_process_CPU_seconds': remaining, 'total_CPU_budget_seconds': 120}
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Process exit {code}; preserve outputs without automatic restart'
terminal = json.loads((HERE / 'capacity.terminal.json').read_text())
total = cpu() - start
run.update(status=terminal['status'], running=False, exit_code=code,
           next_cursor=terminal['next_cursor'], total_recorded_CPU_seconds=total)
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
terminal.update(preparation_compile_calibration_CPU_seconds=preparation,
                total_recorded_CPU_seconds=total, CPU_budget_seconds=120,
                wall_seconds=time.monotonic() - wall, worker_count=1, restarts=0)
(HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
print(json.dumps(terminal, indent=2), flush=True)
