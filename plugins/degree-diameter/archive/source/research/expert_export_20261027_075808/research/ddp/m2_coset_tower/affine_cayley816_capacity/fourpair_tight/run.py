#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'terminal.json').exists(), 'No automatic restart'


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + child.ru_utime + child.ru_stime


start, wall = cpu(), time.monotonic()
linear = json.loads((HERE / 'linear.terminal.json').read_text())
rows = json.loads((HERE / 'survivors.json').read_text())
assert len(rows) == 10 and linear['remaining_projective_inputs'] == 15085980
prior = linear['CPU_seconds']
inputs, lines = [], ['10']
for row in rows:
    assert row['pair_count'] == row['involution_count'] == 4
    assert row['final_dimension'] == 6
    basis = row['basis_in_original_anchored_coordinates']
    assert len(basis) == 6 and all(len(v) == 7 for v in basis)
    scope = (17 ** 6 - 1) // 16
    assert scope == row['projective_inputs_after_closure'] == 1508598
    order = sorted(range(48), key=lambda j: (len(row['restricted_forms_by_phase'][j]), j))
    item = {'source_cursor': row['cursor'], 'pair_phases': row['pair_phases'],
            'anchor_component': row['anchor_component'], 'original_field_slots': 8,
            'basis': basis, 'projective_dimension': 6, 'scope': scope,
            'fiber_test_order': order,
            'fiber_form_counts_in_test_order': [len(row['restricted_forms_by_phase'][j]) for j in order]}
    inputs.append(item)
    numbers = [row['cursor'], row['anchor_component'], 4, 6, scope] + row['pair_phases']
    numbers += [x for v in basis for x in v]
    lines.append(' '.join(map(str, numbers)))
    for phase in order:
        forms = row['restricted_forms_by_phase'][phase]
        assert len(forms) >= 17 and all(len(v) == 6 for v in forms)
        lines.append(' '.join(map(str, [phase, len(forms)] + [x for v in forms for x in v])))
(HERE / 'inputs.json').write_text(json.dumps(inputs, indent=2) + '\n')
(HERE / 'inputs.txt').write_text('\n'.join(lines) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'], cwd=HERE,
                   stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - start
remaining = 120 - prior - preparation - 1
assert remaining > 0
metadata = {
    'scope': 'Only12 four-pair/four-reflection capacity survivors;2 rejected by iterated necessary linear closure,10 actually enumerated',
    'group': 'F17 semidirect_3 C48', 'n': 816, 'degree': 12, 'target_D': 3,
    'original_marked_projective_inputs': 307754004,
    'actual_scope_patterns': 10, 'actual_marked_projective_inputs': 15085980,
    'projective_normalization': 'only first nonzero z=1; original fields restored through saved6x7 basis with anchor zero',
    'legality': '12 actual nonidentity elements all distinct,4 inverse pairs and4 phase24 reflections',
    'exact_route_filter': 'evaluate every restricted coefficient form in each of48fibers; require all17 values in each fiber',
    'full_BFS': 'only after all exact fibers cover; save graph only on actual D3',
    'diagnostic_failure_graphs': False,
    'restoration_calibration': 'one independent Python actual≤3word-set comparison already saved; C++ checks restored field tuple, no repeated word or BFS calibration',
    'CPU_budget_seconds': 120, 'worker_count': 1,
    'linear_CPU_seconds': prior,
    'preparation_compile_CPU_seconds': preparation,
    'process_CPU_limit_seconds': remaining,
    'other_branches_processed': 0,
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')


def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'production.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(), 'worker_count': 1,
           'linear_CPU_seconds': prior, 'preparation_CPU_seconds': preparation,
           'process_CPU_limit_seconds': remaining, 'CPU_budget_seconds': 120,
           'start_cursor': 0, 'scope': 15085980}
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Exit {code}; preserve outputs without automatic restart'
terminal = json.loads((HERE / 'terminal.json').read_text())
new_total = cpu() - start
summary = dict(terminal, linear_CPU_seconds=prior, preparation_compile_CPU_seconds=preparation,
               new_preparation_compile_run_CPU_seconds=new_total,
               total_including_linear_CPU_seconds=prior + new_total,
               wall_seconds=time.monotonic() - wall, worker_count=1, restarts=0,
               CPU_budget_seconds=120,
               independent_final='needed only if a genuine D3 graph was saved')
(HERE / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
run.update(status=terminal['status'], running=False, exit_code=code,
           total_including_linear_CPU_seconds=prior + new_total,
           processed_inputs=terminal['processed_inputs'])
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k != 'per_pattern'}, indent=2), flush=True)
