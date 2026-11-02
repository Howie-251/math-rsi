#!/usr/bin/env python3
import time
START = time.process_time()
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import traceback

HERE = Path(__file__).resolve().parent
PRIOR = .8
PREP = .2
CAP = 20.
resource.setrlimit(resource.RLIMIT_CPU, (19, 20))
BASE_CHILD = resource.getrusage(resource.RUSAGE_CHILDREN)


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime - BASE_CHILD.ru_utime - BASE_CHILD.ru_stime


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + '\n')


write('HANDLE.json', {'status': 'COMPILING', 'pid': os.getpid(), 'single_worker': True,
    'prior_CPU_seconds': PRIOR, 'preparation_charge_CPU_seconds': PREP, 'case_cap_CPU_seconds': CAP})
try:
    command = ['g++', '-std=c++17', '-O2', str(HERE / 'gate.cpp'), '-o', str(HERE / 'gate')]
    compiled = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    (HERE / 'COMPILE_STDOUT.txt').write_text(compiled.stdout)
    (HERE / 'COMPILE_STDERR.txt').write_text(compiled.stderr)
    compile_cpu = child_cpu()
    if compiled.returncode:
        raise RuntimeError(f'compiler failed exit {compiled.returncode}')
    remaining = CAP - PRIOR - PREP - (time.process_time() - START) - compile_cpu - .2
    if remaining <= 0:
        raise RuntimeError('budget consumed before numeric gate')

    def limit_child():
        hard = min(20, math.ceil(remaining))
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    with (HERE / 'STDOUT.txt').open('w') as stdout, (HERE / 'STDERR.txt').open('w') as stderr:
        command = [str(HERE / 'gate'), str(HERE), str(remaining)]
        process = subprocess.Popen(command, stdout=stdout, stderr=stderr, preexec_fn=limit_child)
        write('HANDLE.json', {'status': 'RUNNING', 'pid': os.getpid(), 'native_pid': process.pid,
            'remaining_native_CPU_seconds': remaining, 'compile_CPU_seconds': compile_cpu,
            'single_worker': True, 'case_cap_CPU_seconds': CAP})
        rc = process.wait()
    if rc:
        raise RuntimeError(f'native gate exit {rc}; preserve spent cost/logs')
    result = json.loads((HERE / 'NATIVE_RESULT.json').read_text())
    result.update({'compile_exit_code': compiled.returncode, 'native_exit_code': rc,
        'compile_CPU_seconds': compile_cpu, 'source_BFS_field_solver_Lean_or_reviews': 0,
        'scope': 'fixed C8 semidirect additive Z32 by action3, positive phases1/2/3/4, all four normal residues; common odd-unit normalization; includes actual degree7 cases',
        'next': 'STOP; first hit requires fresh acceptance, otherwise no additional group/phase/action/domain'})
except Exception as exc:
    result = {'status': 'UNKNOWN_GLOBAL256_PROCESS_OR_INPUT_FAILURE', 'error': str(exc),
        'traceback': traceback.format_exc(), 'next': 'STOP preserve failure and spent CPU'}
parent = time.process_time() - START
children = child_cpu()
total = PRIOR + PREP + parent + children
result.update({'prior_read_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'actual_parent_CPU_seconds': parent, 'actual_all_children_CPU_seconds': children,
    'wholecase_CPU_seconds': total, 'wholecase_CPU_cap_seconds': CAP})
write('RESULT.json', result)
write('TERMINAL.json', {**result, 'terminal': True, 'active_processes': 0})
write('HANDLE.json', {'status': result['status'], 'pid': os.getpid(), 'terminal': True,
    'active_processes': 0, 'wholecase_CPU_seconds': total})
print(json.dumps({k: result[k] for k in ('status', 'capacity_pass', 'phases',
    'connected_parameters_checked', 'degree7_checked', 'degree8_checked', 'full_hit',
    'wholecase_CPU_seconds', 'error') if k in result}))
