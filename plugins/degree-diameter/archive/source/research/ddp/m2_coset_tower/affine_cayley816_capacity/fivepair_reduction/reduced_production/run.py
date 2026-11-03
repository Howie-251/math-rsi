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
sys.path.insert(0, str(HERE.parents[2] / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
assert not (HERE / 'terminal.json').exists(), 'No automatic restart'


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + child.ru_utime + child.ru_stime


start, wall = cpu(), time.monotonic()
rows = json.loads((HERE.parent / 'reduced_dimension_inputs.json').read_text())
assert len(rows) == 1091 and sum(r['remaining_projective_inputs'] for r in rows) == 84607626
scalar = [pow(3, j, 17) for j in range(48)]
product = [[(i + j) % 48 for j in range(48)] for i in range(48)]
inverse = [(-j) % 48 for j in range(48)]
inputs = []
with (HERE / 'inputs.txt').open('w') as out:
    out.write('1091\n')
    for index, row in enumerate(rows):
        assert cpu() - start < 54, 'Preparation budget; retain files without restarting'
        dim, anchor = row['final_dimension'], row['anchor_component']
        assert 3 <= dim <= 5 and len(row['pair_phases']) == 5
        basis = row['basis_in_original_anchored_coordinates']
        assert len(basis) == dim and all(len(v) == 6 for v in basis)
        scope = (17 ** dim - 1) // 16
        assert scope == row['remaining_projective_inputs']
        phases = row['pair_phases'] + [24, 24]
        assert anchor == next(i for i, j in enumerate(phases) if scalar[j] != 1)
        components = [{'phase': j, 'kind': 'pair'} for j in row['pair_phases']]
        components += [{'phase': 24, 'kind': 'involution'} for _ in range(2)]
        original = affine_word_forms(17, product, inverse, scalar, components)
        forms = []
        for cell in original['forms']:
            anchored = [c[:anchor] + c[anchor+1:] for c in cell]
            forms.append(sorted({tuple(sum(x*y for x, y in zip(c, b)) % 17 for b in basis) for c in anchored}))
        assert list(map(len, forms)) == row['final_form_counts']
        order = sorted(range(48), key=lambda j: (len(forms[j]), j))
        item = {'pattern_index': index, 'source_cursor': row['source_cursor'],
                'represented_original_mode_cursors': row['member_cursors'],
                'pair_phases': row['pair_phases'], 'anchor_component': anchor,
                'original_field_slots': 7, 'basis': basis, 'nullspace_dimension': dim,
                'scope': scope, 'fiber_test_order': order,
                'fiber_form_counts_in_test_order': [len(forms[j]) for j in order]}
        inputs.append(item)
        numbers = [row['source_cursor'], anchor, 5, dim, scope] + row['pair_phases']
        numbers += [x for v in basis for x in v]
        out.write(' '.join(map(str, numbers)) + '\n')
        for phase in order:
            assert len(forms[phase]) >= 17
            out.write(' '.join(map(str, [phase, len(forms[phase])] + [x for v in forms[phase] for x in v])) + '\n')
        if (index + 1) % 200 == 0:
            print(json.dumps({'event': 'PREPARING', 'patterns': index + 1, 'CPU_seconds': cpu()-start}), flush=True)
(HERE / 'inputs.json').write_text(json.dumps(inputs, indent=2) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'], cwd=HERE,
                   stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - start
remaining = 60 - preparation - 1
assert remaining > 0
metadata = {
    'scope': 'All1091 surviving five-pair/two-reflection phase17 representatives with reduced nullspace dimension3..5',
    'group': 'F17 semidirect_3 C48', 'n': 816, 'degree': 12, 'target_D': 3,
    'actual_scope_patterns': 1091, 'represented_original_modes': 2168,
    'actual_marked_projective_inputs': 84607626,
    'projective_normalization': 'only first nonzero z=1; restore6 anchored fields through saved basis, then insert anchor zero',
    'legality': '12 actual nonidentity distinct elements:5 inverse pairs and2 phase24 reflections',
    'exact_route_filter': 'evaluate every restricted coefficient form in all48 fibers, each must cover F17',
    'full_BFS': 'only after all exact fibers cover; graph saved only on actual D3',
    'diagnostic_failure_graphs': False,
    'calibration': 'one legal member of actual production prefix with original fields first nonzero different from1; all48 actual word masks checked',
    'CPU_budget_seconds': 60, 'worker_count': 1,
    'preparation_compile_CPU_seconds': preparation, 'process_CPU_limit_seconds': remaining,
    'preprocessing_CPU_separate_previous_authorization': True,
    'dimension6_representatives_processed': 0, 'new_random_seeds': 0,
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')


def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'production.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(), 'worker_count': 1,
           'preparation_CPU_seconds': preparation, 'process_CPU_limit_seconds': remaining,
           'CPU_budget_seconds': 60, 'start_cursor': 0, 'scope': 84607626}
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Exit {code}; preserve outputs without automatic restart'
terminal = json.loads((HERE / 'terminal.json').read_text())
total = cpu() - start
summary = dict(terminal, preparation_compile_CPU_seconds=preparation,
               preparation_compile_run_CPU_seconds=total,
               wall_seconds=time.monotonic() - wall, worker_count=1, restarts=0,
               CPU_budget_seconds=60, pending=['Independent final D3 verification'] if terminal['saved_best_graph'] else [])
(HERE / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
run.update(status=terminal['status'], running=False, exit_code=code,
           total_CPU_seconds=total, processed_inputs=terminal['processed_inputs'])
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k != 'per_pattern'}, indent=2), flush=True)
