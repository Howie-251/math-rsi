#!/usr/bin/env python3
"""Complete degree-12 necessary capacities; no field assignments or graph search."""
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
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + child.ru_utime + child.ru_stime


start, wall = cpu(), time.monotonic()
scalar = [pow(2, j, 29) for j in range(28)]
assert len(set(scalar)) == 28 and pow(2, 28, 29) == 1
assert pow(2, 14, 29) == 28 and pow(2, 4, 29) == 16
assert sum(math.comb(p + 13, p) for p in range(7)) == 38760
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'capacity.cpp', '-o', 'capacity'],
                   cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
compile_cpu = cpu() - start
subprocess.run([str(HERE / 'capacity'), 'calibrate', str(HERE), '0'], check=True)
sys.path.insert(0, str(HERE.parent / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms

case, = json.loads((HERE / 'calibration.cpp.json').read_text())
product = [[(j + k) % 28 for k in range(28)] for j in range(28)]
inverse = [(-j) % 28 for j in range(28)]
components = [{'phase': k, 'kind': 'pair'} for k in case['pair_phases']]
components += [{'phase': 14, 'kind': 'involution'} for _ in range(case['involution_count'])]
reference = affine_word_forms(29, product, inverse, scalar, components)
assert reference['raw_counts'] == case['raw_capacity']
assert reference['form_counts'] == case['form_counts']
packed = [sorted(sum(x << (5 * i) for i, x in enumerate(coeff)) for coeff in forms)
          for forms in reference['forms']]
assert packed == case['packed_forms']
preparation = cpu() - start
(HERE / 'calibration.check.json').write_text(json.dumps({
    'status': 'PASS_ONE_NEW_PURE_SYMBOLIC_CASE',
    'degree': 12, 'pair_phases': case['pair_phases'],
    'involution_count': case['involution_count'],
    'all_28_form_sets_match': True,
    'convolution_counts_match_direct_reduced_words': True,
    'graph_or_field_assignment_tested': False,
    'compile_CPU_seconds': compile_cpu,
    'preparation_compile_calibration_CPU_seconds': preparation,
    'reference_function': '../axis_cayley272/symbolic_affine_words.py',
}, indent=2) + '\n')
metadata = {
    'group': 'F29 additive semidirect_2 C28 = AGL1(29)',
    'order': 812, 'r': 2, 'action_order': 28,
    'primitive_root_checks': {'2^28': 1, '2^14': 28, '2^4': 16},
    'scalar_powers': scalar,
    'degree': 12, 'target_diameter': 3, 'saved_threshold': 810,
    'Moore_bound': 1597,
    'phase_pair_classes': list(range(14)), 'involution_phase': 14,
    'inverse_pair_counts': [14] + [29] * 13,
    'total_inverse_pairs': 391, 'nonidentity_involutions': 29,
    'group_product': '(x,j)(y,k)=(x+2^j*y mod29,j+k mod28)',
    'inverse': '(-2^-j*x mod29,-j mod28)',
    'pattern_order': 'increasing pair count, lexicographic nondecreasing pair phases',
    'total_patterns': 38760,
    'component_order': 'inverse-pair representatives then independent phase14 involutions',
    'packed_form_encoding': 'coefficient_i in bits5i..5i+4; actual values0..28',
    'ordinary_capacity': 'a*a*a+a*a+(2-2d)*a+(1-d)*delta0 in Z[C28]',
    'necessary_capacity_each_phase': 29,
    'normalization': 'first chi!=1 component set0 by common translation; remaining nonzero vector modulo common scalar',
    'projective_count_per_surviving_pattern': '(29^(m-1)-1)/28, m=12-pair_count',
    'no_additional_quotient_units_or_slot_permutation_reduction': True,
    'CPU_budget_seconds': 60, 'worker_count': 1,
    'field_assignments_tested': 0, 'graphs_generated': 0, 'BFS_runs': 0,
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
remaining = 60 - preparation - 1
assert remaining > 0


def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'capacity.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'capacity'), 'run', str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(),
           'worker_count': 1, 'start_cursor': 0, 'scope_patterns': 38760,
           'preparation_CPU_seconds': preparation,
           'remaining_process_CPU_seconds': remaining, 'total_CPU_budget_seconds': 60}
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
                total_recorded_CPU_seconds=total, CPU_budget_seconds=60,
                wall_seconds=time.monotonic() - wall, worker_count=1, restarts=0)
(HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
print(json.dumps(terminal, indent=2), flush=True)
