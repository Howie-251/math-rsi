#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'production.terminal.json').exists(), 'No automatic restart'


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + child.ru_utime + child.ru_stime


started, wall = cpu(), time.monotonic()
wanted = [[3, 4, 4, 6, 7, 11], [5, 7, 9, 10, 12, 12]]
saved = [json.loads(s) for s in (HERE.parent / 'survivors.jsonl').read_text().splitlines()]
rows = [next(s for s in saved if s['pair_phases'] == phase) for phase in wanted]
basis = [[int(i == j) for j in range(5)] for i in range(5)]
scope = (29 ** 5 - 1) // 28
assert scope == 732541
inputs, lines = [], ['2']
for k, row in enumerate(rows):
    assert row['degree'] == 12 and row['pair_count'] == 6 and row['involution_count'] == 0
    assert row['field_variables'] == 6 and row['anchor_component'] == 0
    assert row['minimum_symbolic_capacity'] == 45
    assert row['projective_marked_inputs'] == scope
    inputs.append({'pattern_index': k, 'source_symbolic_cursor': row['cursor'],
                   'pair_phases': row['pair_phases'], 'involution_count': 0,
                   'anchor_component': 0, 'normalized_parameter_dimension': 5,
                   'basis': basis, 'additional_linear_constraints': 'none',
                   'marked_scope': scope, 'expected_legal': 29 ** 4,
                   'expected_illegal_duplicate_pair': (29 ** 4 - 1) // 28})
    numbers = [row['cursor'], 0, 5, 0, scope] + row['pair_phases']
    numbers += [x for v in basis for x in v]
    lines.append(' '.join(map(str, numbers)))
(HERE / 'production.inputs.json').write_text(json.dumps(inputs, indent=2) + '\n')
(HERE / 'production.inputs.txt').write_text('\n'.join(lines) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'production.cpp', '-o', 'production'],
                   cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - started
remaining = 120 - preparation - 1
assert remaining > 0
metadata = {
    'group': 'F29 semidirect_2 C28', 'n': 812, 'degree': 12, 'target_diameter': 3,
    'pair_phase_modes': wanted, 'raw_marked_scope': 1465082,
    'per_mode_scope': 732541, 'expected_legal_if_complete': 1414562,
    'expected_illegal_if_complete': 50520,
    'normalization': 'translate first nontrivial-action field to0, then normalize only first nonzero remaining coordinate to1',
    'field_embedding': 'fields=(0,z0,z1,z2,z3,z4); identity basis, no extra linear constraints',
    'order': 'listed mode order, first nonzero parameter position, base29 tail in slot order',
    'full_BFS_per_legal_input': True,
    'exact_legality': '12 distinct nonidentity actual elements supplied as six true inverse pairs',
    'other_8611_symbolic_modes': 'not searched',
    'CPU_budget_seconds': 120, 'worker_count': 1,
    'preparation_compile_CPU_seconds': preparation,
    'process_CPU_limit_seconds': remaining,
    'independent_final': 'parent-owned; only the final saved best graph',
}
(HERE / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')


def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'production.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'production'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(),
           'worker_count': 1, 'start_cursor': 0, 'scope': 1465082,
           'preparation_compile_CPU_seconds': preparation,
           'process_CPU_limit_seconds': remaining, 'total_CPU_budget_seconds': 120}
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    exit_code = process.wait()
assert exit_code == 0, f'Exit {exit_code}; preserve outputs without automatic restart'
terminal = json.loads((HERE / 'production.terminal.json').read_text())
if terminal['status'] == 'COMPLETE_NO_SOLUTION':
    assert terminal['counts']['raw_marked_inputs'] == 1465082
    assert terminal['counts']['legal_generating_sets'] == 1414562
    assert terminal['counts']['illegal_generating_sets'] == 50520
    for item in terminal['per_pattern']:
        assert item['counts']['raw_marked_inputs'] == 732541
        assert item['counts']['legal_generating_sets'] == 707281
        assert item['counts']['illegal_generating_sets'] == 25260
total = cpu() - started
terminal.update(preparation_compile_CPU_seconds=preparation,
                total_preparation_compile_run_CPU_seconds=total,
                CPU_budget_seconds=120, worker_count=1, restarts=0,
                wall_seconds=time.monotonic() - wall,
                independent_final='parent-owned; pending only for sole final best graph')
(HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
run.update(status=terminal['status'], running=False, exit_code=exit_code,
           next_cursor=terminal['next_cursor'], total_CPU_seconds=total)
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps({k: v for k, v in terminal.items() if k != 'root_deficit_histogram'}, indent=2), flush=True)
