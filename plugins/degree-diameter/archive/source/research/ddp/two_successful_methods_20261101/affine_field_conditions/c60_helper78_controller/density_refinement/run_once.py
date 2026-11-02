#!/usr/bin/env python3
"""One new necessary-density refinement, with a separate 27-CPU solve."""
import itertools
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = HERE.parents[5]
STAGE = HERE.parents[2]
START = time.process_time()
WALL = time.monotonic()
CHILD_START = resource.getrusage(resource.RUSAGE_CHILDREN)
resource.setrlimit(resource.RLIMIT_CPU, (2, 30))
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime - CHILD_START.ru_utime - CHILD_START.ru_stime


if (HERE / 'SOLVER_STARTED.json').exists():
    raise SystemExit('The only density-refined solve has already started; no restart.')
old_result = json.loads((BASE / 'TERMINAL.json').read_text())
assert old_result['status'] == 'UNKNOWN'
old_cpu = old_result['total_scope_CPU_seconds']
triples = json.loads((HERE / 'TRIPLE_FILTER.json').read_text())
classification_cpu = triples['enumeration_CPU_seconds']
params = json.loads((STAGE / 'f7_c60_d35/PARAMETERS.json').read_text())
graph = params['controller']
edges = sorted((u, v) for u, row in enumerate(graph) for v in row if u < v)
assert len(edges) == 150 and len(triples['forbidden_independent_triples']) == 6840


def x(v, i):
    return 1 + 18 * v + i


appended = []
for i in range(6, 18):
    for u, v in edges:
        appended.append(f'{-x(u, i)} {-x(v, i)} 0\n')
independence_count = len(appended)
for i in range(6, 18):
    for u, v, w in triples['forbidden_independent_triples']:
        appended.append(f'{-x(u, i)} {-x(v, i)} {-x(w, i)} 0\n')
assert independence_count == 1800 and len(appended) == 83880
old_cnf = (BASE / 'model.cnf').read_text()
header = 'p cnf 44460 145047\n'
assert old_cnf.count(header) == 1
new_cnf = old_cnf.replace(header, 'p cnf 44460 228927\n', 1)
(HERE / 'model.cnf').write_text(new_cnf + ''.join(appended))
prepare_cpu = time.process_time() - START + classification_cpu
assert prepare_cpu < 2
model = {'status': 'MODEL_COMPLETE', 'source': 'same fixed accepted Bhakar C60',
         'helper_graph': 'same fixed 2K3+3K4', 'variables': 44460,
         'base_clauses_preserved_verbatim': 145047, 'clauses': 228927,
         'new_independence_clauses': 1800,
         'new_forbidden_low_neighbor_union_triple_clauses': 82080,
         'accepted_density_candidate_triples': 19260,
         'preparation_CPU_seconds_including_classification': prepare_cpu,
         'old_scope_CPU_seconds': old_cpu, 'new_solver_CPU_limit': 27,
         'new_solver_wall_limit': 45, 'combined_scope_CPU_limit': 90,
         'density_constraints_are_necessary_redundant_cuts': True,
         'source_author': params['controller_author'], 'continuation_of_old_solver_state': False}
dump('MODEL.json', model)
print(json.dumps(model), flush=True)
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))


def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (27, 27))


command = [str(ROOT / '.tools/lean-4.24.0-linux/bin/cadical'), '-t', '26',
           '-w', str(HERE / 'solver_solution.txt'), str(HERE / 'model.cnf')]
dump('SOLVER_STARTED.json', {'command': command, 'solver_calls_this_refinement': 1,
                          'parent_pid': os.getpid(), 'no_third_timer': True})
start_solver_wall = time.monotonic()
wall_timeout = False
with (HERE / 'SOLVER.log').open('w') as log:
    p = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                         preexec_fn=limit, start_new_session=True)
    dump('HANDLE.json', {'status': 'RUNNING', 'pid': p.pid,
                         'parent_pid': os.getpid(), 'command': command, 'no_third_timer': True})
    try:
        code = p.wait(timeout=45)
    except subprocess.TimeoutExpired:
        wall_timeout = True
        os.killpg(p.pid, signal.SIGTERM)
        try:
            code = p.wait(timeout=1)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)
            code = p.wait()
solver_cpu = child_cpu()
solver_wall = time.monotonic() - start_solver_wall
raw = (HERE / 'SOLVER.log').read_text()
status = {10: 'SAT', 20: 'UNSAT'}.get(code, 'UNKNOWN')
result = {**model, 'status': status, 'solver_exit_code': code,
          'solver_CPU_seconds': solver_cpu, 'solver_wall_seconds': solver_wall,
          'wall_timeout': wall_timeout, 'solver_calls_this_refinement': 1,
          'solver_calls_combined_scope': 2, 'timer_continuation_allowed': False,
          'controller_generated': False, 'fiber_generated': False,
          'old_fiber_BFS_calls': 0, 'Lean_calls': 0, 'Gemini_calls': 0,
          'global_record_claim': False}
if status == 'SAT':
    positive = set()
    for line in (HERE / 'solver_solution.txt').read_text().splitlines():
        if line.startswith('v '):
            positive.update(int(z) for z in line[2:].split() if int(z) > 0)
    colors = []
    for v in range(60):
        assigned = [i for i in range(18) if x(v, i) in positive]
        assert len(assigned) == 1
        colors.append(assigned[0])
    cliques = [list(range(0, 3)), list(range(3, 6)), list(range(6, 10)),
               list(range(10, 14)), list(range(14, 18))]
    literal = set(edges)
    literal.update((v, 60 + colors[v]) for v in range(60))
    literal.update((60 + i, 60 + j) for c in cliques for i, j in itertools.combinations(c, 2))
    with (HERE / 'controller78.literal.edges').open('w') as f:
        f.write('# 78 vertices, undirected simple edges, zero-based labels\n')
        f.writelines(f'{u} {v}\n' for u, v in sorted(literal))
    dump('PIN_PARTITION.json', {'old_vertex_color': colors,
         'pin_groups': [[v for v in range(60) if colors[v] == i] for i in range(18)]})
    # Copy the previously reviewed independent verifier, adapting only the
    # one-level-deeper source path. Original UNKNOWN artifacts stay untouched.
    verifier = (BASE / 'verify_witness.py').read_text()
    verifier = verifier.replace("HERE.parent.parent / 'f7_c60_d35/PARAMETERS.json'",
                                "HERE.parent.parent.parent / 'f7_c60_d35/PARAMETERS.json'")
    (HERE / 'verify_witness.py').write_text(verifier)
    remaining = 89.5 - old_cpu - classification_cpu - child_cpu() - (time.process_time() - START)
    assert remaining > 0
    checked = subprocess.run([sys.executable, str(HERE / 'verify_witness.py')],
                             capture_output=True, text=True, timeout=min(remaining, 10))
    (HERE / 'VERIFY.log').write_text(checked.stdout + checked.stderr)
    result['independent_verifier_exit'] = checked.returncode
    if checked.returncode == 0:
        result['verification'] = json.loads((HERE / 'VERIFIED.json').read_text())
        result['controller_generated'] = True
        result['status'] = 'SAT_CONTROLLER_INDEPENDENTLY_VERIFIED'
    else:
        result['status'] = 'SAT_VERIFICATION_FAILED'
result['new_scope_CPU_seconds'] = classification_cpu + child_cpu() + time.process_time() - START
result['combined_scope_CPU_seconds'] = old_cpu + result['new_scope_CPU_seconds']
result['new_scope_wall_seconds'] = time.monotonic() - WALL
assert result['combined_scope_CPU_seconds'] < 90
result['conclusion'] = ('Bounded UNKNOWN; same H18 case remains open; all authorized continuation ends.'
                        if status == 'UNKNOWN' else
                        'Only the same fixed-source H18 case is excluded by this necessary-cut refinement.'
                        if status == 'UNSAT' else 'Literal controller verification required and reported above.')
dump('TERMINAL.json', result)
dump('HANDLE.json', {'status': result['status'], 'solver_exit_code': code, 'no_third_timer': True})
print(json.dumps(result, indent=2), flush=True)
