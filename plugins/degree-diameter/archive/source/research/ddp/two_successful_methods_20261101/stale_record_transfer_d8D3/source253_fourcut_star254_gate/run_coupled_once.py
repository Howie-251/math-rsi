#!/usr/bin/env python3
"""Single compiler and native coupled-domain batch, with cumulative CPU ledger."""
import time
START = time.process_time()
import csv
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import traceback

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
PRIOR = 1.868182278
PREP = .20
CAP = 20.
resource.setrlimit(resource.RLIMIT_CPU, (19, 20))
CHILD0 = resource.getrusage(resource.RUSAGE_CHILDREN)


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + '\n')


def children_cpu():
    value = resource.getrusage(resource.RUSAGE_CHILDREN)
    return value.ru_utime + value.ru_stime - CHILD0.ru_utime - CHILD0.ru_stime


write('COUPLED_HANDLE.json', {
    'status': 'PREPARING_INPUT', 'pid': os.getpid(), 'single_worker': True,
    'prior_case_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'wholecase_CPU_cap_seconds': CAP,
})
result = None
try:
    # Read literal source once as this new problem's construction input.
    with (REPO / 'context/DD_PORTFOLIO_START_20261026/baselines/d8_D3_known.edges').open() as stream:
        assert tuple(map(int, next(stream).split())) == (253, 1012)
        source = sorted(tuple(map(int, line.split())) for line in stream if line.strip())
    with (HERE / 'COUPLED_INPUT.txt').open('w') as out:
        out.write(str(len(source)) + '\n')
        for u, v in source:
            out.write(f'{u} {v}\n')
        for kind in range(4):
            cached = json.loads((HERE / f'GATE_TYPE{kind}_OBLIGATIONS_AND_CLASSES.json').read_text())
            vertex = [0] * 253
            for o in cached['obligations']:
                for v in o['hitset']:
                    vertex[v] |= 1 << o['obligation_id']
            out.write(str(cached['profile']['positive_label']) + '\n')
            out.write(' '.join(map(str, vertex)) + '\n')
            with (HERE / f'GATE_TYPE{kind}_ALL997_EDGE_MASKS.tsv').open() as inp:
                rows = list(csv.DictReader(inp, delimiter='\t'))
            assert len(rows) == 997
            out.write(str(len(rows)) + '\n')
            for row in rows:
                out.write(f"{row['source_positive_edge_index']} {row['h']} {row['hs']} {int(row['mask_hex'], 16)}\n")
            with (HERE / f'REPAIR_TYPE{kind}_ALL_NONEDGE_MASKS.tsv').open() as inp:
                rows = list(csv.DictReader(inp, delimiter='\t'))
            assert len(rows) == 30378
            out.write(str(len(rows)) + '\n')
            for row in rows:
                out.write(f"{row['a']} {row['b']} {int(row['mask_hex'], 16)}\n")
    compile_command = ['g++', '-std=c++17', '-O2', str(HERE / 'coupled_once.cpp'), '-o', str(HERE / 'coupled_once')]
    write('COUPLED_HANDLE.json', {'status': 'COMPILING', 'pid': os.getpid(), 'command': compile_command,
        'prior_case_CPU_seconds': PRIOR, 'wholecase_CPU_cap_seconds': CAP})
    compiled = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    (HERE / 'COUPLED_COMPILE_STDOUT.txt').write_text(compiled.stdout)
    (HERE / 'COUPLED_COMPILE_STDERR.txt').write_text(compiled.stderr)
    compile_cpu = children_cpu()
    if compiled.returncode:
        raise RuntimeError(f'compiler exit {compiled.returncode}; see saved stderr')
    parent_elapsed = time.process_time() - START
    remaining = CAP - PRIOR - PREP - parent_elapsed - compile_cpu - .20
    if remaining <= 0:
        raise RuntimeError('cumulative CPU budget exhausted before native run')

    def set_child_limit():
        hard = min(20, math.ceil(remaining))
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    command = [str(HERE / 'coupled_once'), str(HERE), str(remaining)]
    with (HERE / 'COUPLED_STDOUT.txt').open('w') as stdout, (HERE / 'COUPLED_STDERR.txt').open('w') as stderr:
        child = subprocess.Popen(command, stdout=stdout, stderr=stderr, preexec_fn=set_child_limit)
        write('COUPLED_HANDLE.json', {'status': 'RUNNING_NATIVE', 'pid': os.getpid(), 'native_pid': child.pid,
            'command': command, 'remaining_native_CPU_seconds': remaining, 'compile_CPU_seconds': compile_cpu,
            'prior_case_CPU_seconds': PRIOR, 'wholecase_CPU_cap_seconds': CAP})
        returncode = child.wait()
    if returncode:
        raise RuntimeError(f'native exit {returncode}; preserve input/logs')
    result = json.loads((HERE / 'COUPLED_NATIVE_RESULT.json').read_text())
    result.update({'compile_exit_code': compiled.returncode, 'native_exit_code': returncode,
                   'compile_CPU_seconds': compile_cpu, 'literal_source_parse_count': 1,
                   'source_D3_BFS_field_words_revalidation': 0,
                   'scope': 'global necessary coupled gate for fixed CM253 five disjoint cuts + one original nonedge repair + one8star; actual candidates only for one frozen type/repair',
                   'next': 'STOP; root handles any complete candidate and any scope change'})
except Exception as exc:
    result = {'status': 'UNKNOWN_COUPLED_PROCESS_OR_INPUT_FAILURE', 'error': str(exc),
              'traceback': traceback.format_exc(), 'scope': 'no uncompleted-domain NO conclusion',
              'next': 'STOP preserve failure and spent budget'}

parent_cpu = time.process_time() - START
child_cpu = children_cpu()
total = PRIOR + PREP + parent_cpu + child_cpu
result.update({'prior_case_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'actual_parent_CPU_seconds': parent_cpu, 'actual_children_CPU_seconds': child_cpu,
    'wholecase_CPU_seconds': total, 'wholecase_CPU_cap_seconds': CAP})
write('COUPLED_RESULT.json', result)
write('COUPLED_TERMINAL.json', {**result, 'terminal': True, 'active_processes': 0})
write('COUPLED_HANDLE.json', {'status': result['status'], 'pid': os.getpid(), 'terminal': True,
    'active_processes': 0, 'wholecase_CPU_seconds': total})
print(json.dumps({k: result[k] for k in ('status', 'profiles', 'frozen_first_type', 'frozen_repair',
    'actual_final_candidate_count', 'newroot_pass', 'oldroot_fail_candidates', 'full_hit',
    'wholecase_CPU_seconds', 'error') if k in result}))
