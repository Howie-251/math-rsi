#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'd11_production.terminal.json').exists(), 'No automatic restart'

def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + children.ru_utime + children.ru_stime

start, wall = cpu(), time.monotonic()
original = json.loads((HERE / 'd11_tight_linear.survivors.json').read_text())
selected = [row for row in original if row['degree'] == 11 and row['pair_count'] == 5]
selected.sort(key=lambda row: (-row['rank_mod31'], row['cursor']))
assert len(selected) == 38
assert Counter(row['nullspace_dimension'] for row in selected) == {3: 10, 4: 20, 5: 8}
assert sum(row['projective_marked_inputs_after_linear_constraints'] for row in selected) == 8260050
inputs, text = [], ['38']
for index, row in enumerate(selected):
    basis = row['nullspace_basis_after_anchor']
    dimension = row['nullspace_dimension']
    assert len(basis) == dimension and all(len(v) == 5 for v in basis)
    assert row['field_variables'] == 6 and row['involution_count'] == 1
    scope = (31 ** dimension - 1) // 30
    assert scope == row['projective_marked_inputs_after_linear_constraints']
    item = {'pattern_index': index, 'source_symbolic_cursor': row['cursor'],
            'pair_phases': row['pair_phases'], 'involution_phase': 15,
            'anchor_component': row['anchor_component'], 'rank': row['rank_mod31'],
            'nullspace_dimension': dimension, 'basis': basis,
            'raw_marked_scope': scope,
            'normalization': 'first nonzero z coordinate is1; no original-field leading1 requirement'}
    inputs.append(item)
    numbers = [row['cursor'], row['rank_mod31'], dimension, row['anchor_component'], scope]
    numbers += row['pair_phases'] + [value for vector in basis for value in vector]
    text.append(' '.join(map(str, numbers)))
(HERE / 'd11_production.inputs.json').write_text(json.dumps(inputs, indent=2) + '\n')
(HERE / 'd11_production.inputs.txt').write_text('\n'.join(text) + '\n')
with (HERE / 'd11_production.compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'd11_production.cpp', '-o', 'd11_production'],
                   cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - start
capacity = json.loads((HERE / 'terminal.json').read_text())
linear = json.loads((HERE / 'd11_tight_linear.terminal.json').read_text())
prior = capacity['total_recorded_CPU_seconds'] + linear['CPU_seconds']
remaining = 180 - prior - preparation - 1
assert remaining > 0
metadata = {'group': 'F31 semidirect_3 C30', 'n': 930, 'degree': 11, 'target_diameter': 3,
            'scope': 'only the 38 five-inverse-pair plus one-reflection modes',
            'raw_marked_scope': 8260050,
            'dimension_count': {'3': 10, '4': 20, '5': 8},
            'projective_sum': '10*993 + 20*30784 + 8*954305 = 8260050',
            'order': 'rank2 thenrank1 thenrank0; within rank increasing source symbolic cursor; z first-nonzero position then base31 tail',
            'full_BFS_per_legal_input': True, 'right_multiplication_table': 'precomputed group arithmetic, not candidate distance cache',
            'exact_legality': '11 distinct nonidentity inverse-closed actual group elements',
            'field_embedding': 'anchor0; remaining original fields=sum(z[k]*basis[k]) mod31',
            'important_regression': 'phases[1,1,4,11,12], z(1,0,0) gives fields(0,15,25,1,0,0), retained',
            'other_37_four_pair_modes': 'not searched', 'degree12': 'not searched',
            'budget_policy': 'conservatively include prior capacity and tight-linear CPU in the180s total',
            'CPU_budget_seconds': 180, 'worker_count': 1,
            'prior_capacity_and_linear_CPU_seconds': prior,
            'new_preparation_compile_CPU_seconds': preparation,
            'process_CPU_limit_seconds': remaining,
            'independent_final': 'parent-owned; only the final saved best graph'}
(HERE / 'd11_production.metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')

def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))

with (HERE / 'd11_production.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'd11_production'), str(HERE), str(remaining)],
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(),
           'worker_count': 1, 'start_cursor': 0, 'scope': 8260050,
           'prior_capacity_and_linear_CPU_seconds': prior,
           'new_preparation_compile_CPU_seconds': preparation,
           'process_CPU_limit_seconds': remaining, 'total_CPU_budget_seconds': 180}
    (HERE / 'd11_production.run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Process exited{code}; preserve outputs and do not automatically restart'
terminal = json.loads((HERE / 'd11_production.terminal.json').read_text())
new_total = cpu() - start
terminal.update(new_preparation_compile_run_CPU_seconds=new_total,
                prior_capacity_and_linear_CPU_seconds=prior,
                cumulative_including_prior_CPU_seconds=prior + new_total,
                cumulative_CPU_budget_seconds=180,
                wall_seconds=time.monotonic() - wall, worker_count=1, restarts=0,
                independent_final='parent-owned; pending only for the sole final best graph')
(HERE / 'd11_production.summary.json').write_text(json.dumps(terminal, indent=2) + '\n')
run.update(status=terminal['status'], running=False, exit_code=code,
           next_cursor=terminal['next_cursor'], cumulative_including_prior_CPU_seconds=prior + new_total)
(HERE / 'd11_production.run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps(terminal, indent=2), flush=True)
