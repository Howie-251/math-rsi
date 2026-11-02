#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time
from calibrate import check

HERE = Path(__file__).resolve().parent
assert not (HERE / 'run.json').exists(), 'No automatic restart.'


def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime


begin, wall = cpu(), time.monotonic()
source_file = HERE.parent / 'nonabelian4_256_search' / 'best.json'
source = json.loads(source_file.read_text())
assert source['group_name'] == 'Q64' and source['group_twist'] == 16
assert source['n'] == 256 and source['degree'] == 8
U, V, tree, free = [source[k] for k in ('edge_u', 'edge_v', 'tree_edge_indices', 'free_edge_indices')]
assert len(U) == len(V) == 16 and len(tree) == 3 and len(free) == 13
projection = [(g % 16) + 16 * (g // 32) for g in source['voltages']]
assert all(projection[e] == 0 for e in tree)
(HERE / 'source.json').write_text(json.dumps(source, indent=2) + '\n')
(HERE / 'input.txt').write_text('16\n' + '\n'.join(f'{u} {v}' for u, v in zip(U, V)) +
                              '\n' + ' '.join(map(str, tree)) + '\n' +
                              ' '.join(map(str, projection)) + '\n')
scope = {
    'group': 'Q64', 'central_element': [16, 0], 'quotient_group': 'D32',
    'source_parameters_file': str(source_file), 'source_independent_check': '../nonabelian4_256_search/best.independent_check.json',
    'source_projection': projection, 'edge_u': U, 'edge_v': V,
    'tree_edge_indices': tree, 'free_edge_indices': free,
    'quotient_encoding': 'a+16*phase, a in Z16', 'center_bit_order': free,
    'scope': 'change exactly one of13 free quotient values to each of31 alternatives; original projection excluded',
    'projection_order': 'ascending free-edge index, then ascending alternative quotient code',
    'planned_projections': 403, 'central_assignments_per_entered_projection': 8192,
    'projection_filter': 'reject if any of4x128 quotient target slots has no length<=3 walk',
    'legality': 'parallel edges with identical projection require opposite center bits; all actual parallel voltages distinct',
    'scoring': 'nonempty slot loses one lift iff its affine difference system holds; score by exact sparse subspace enumeration',
    'backtracking': 'skip only true reverse of the same edge ID; projected parallel edges remain separate',
    'maximum_CPU_seconds_including_preparation_and_calibration': 180,
    'worker_count': 1, 'no_BFS_in_production': True, 'no_extra_random_starts': True,
    'first_calibration': 'first entered projection and first legal center mask; four independent full BFS roots; score reused',
    'best_scope': 'only legal central lifts of quotient-complete projections actually scored',
    'final_full256_BFS_owner': 'parent',
}
(HERE / 'SCOPE.json').write_text(json.dumps(scope, indent=2) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'],
                   cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
preparation = cpu() - begin
remaining = 180 - preparation - 3
assert remaining > 0


def cap():
    limit = math.ceil(remaining) + 1
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


with (HERE / 'search.log').open('w') as log:
    process = subprocess.Popen([str(HERE / 'search'), str(HERE), str(remaining)], cwd=HERE,
                               stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {
        'status': 'RUNNING', 'running': True, 'pid': process.pid, 'driver_pid': os.getpid(),
        'preparation_CPU_seconds': preparation, 'process_CPU_limit_seconds': remaining,
        'CPU_budget_seconds': 180, 'worker_count': 1,
    }
    (HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
run.update(running=False, exit_code=code, restarts=0)
if code == 0:
    terminal = json.loads((HERE / 'search.terminal.json').read_text())
    if terminal['first_formal_center_saved']:
        calibration = check(HERE)
    else:
        calibration = {'status': 'NOT_APPLICABLE_ZERO_CENTER_PROJECTIONS', 'roots_checked': 0, 'CPU_seconds': 0}
        (HERE / 'first.independent_check.json').write_text(json.dumps(calibration, indent=2) + '\n')
    terminal.update(preparation_CPU_seconds=preparation, calibration=calibration,
                    total_CPU_seconds=cpu() - begin, wall_seconds=time.monotonic() - wall,
                    worker_count=1, restarts=0, CPU_budget_seconds=180,
                    pending=['parent final saved-best check'] if (HERE / 'best.edges').exists() else [])
    (HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
    run.update(status=terminal['status'], total_CPU_seconds=terminal['total_CPU_seconds'])
else:
    run['status'] = 'PROCESS_ERROR'
    run['total_CPU_seconds'] = cpu() - begin
(HERE / 'run.json').write_text(json.dumps(run, indent=2) + '\n')
print(json.dumps(run, indent=2), flush=True)
