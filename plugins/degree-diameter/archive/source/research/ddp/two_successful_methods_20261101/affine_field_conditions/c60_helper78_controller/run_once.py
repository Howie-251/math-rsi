#!/usr/bin/env python3
"""One fixed CNF, one bounded CaDiCaL solve; no continuation mode."""
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
ROOT = HERE.parents[4]
SOURCE = HERE.parent.parent / 'f7_c60_d35'
START = time.process_time()
WALL = time.monotonic()
CHILD_START = resource.getrusage(resource.RUSAGE_CHILDREN)
resource.setrlimit(resource.RLIMIT_CPU, (20, 90))
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime - CHILD_START.ru_utime - CHILD_START.ru_stime


if (HERE / 'TERMINAL.json').exists() or (HERE / 'SOLVER_STARTED.json').exists():
    raise SystemExit('This one-shot scope has already been started; timer continuation forbidden.')

params = json.loads((SOURCE / 'PARAMETERS.json').read_text())
old = params['controller']
assert len(old) == 60 and all(len(row) == 5 for row in old)
edges = sorted((u, v) for u, row in enumerate(old) for v in row if u < v)
assert len(edges) == len(set(edges)) == 150
cliques = [list(range(0, 3)), list(range(3, 6)), list(range(6, 10)),
           list(range(10, 14)), list(range(14, 18))]
component = {i: c for c, group in enumerate(cliques) for i in group}
loads = [4] * 6 + [3] * 12
crosspairs = [(i, j) for i in range(18) for j in range(i + 1, 18)
              if component[i] != component[j]]
assert len(crosspairs) == 129
# Exactly two old steps, including the return to v; not closed radius two.
a2 = [sorted({u for w in old[v] for u in old[w]}) for v in range(60)]

clauses = []
nvars = 1080
groups = {}


def var():
    global nvars
    nvars += 1
    return nvars


def x(v, i):
    return 1 + 18 * v + i


def neg(lit):
    return not lit if isinstance(lit, bool) else -lit


def add(*lits):
    if any(lit is True for lit in lits):
        return
    out = tuple(dict.fromkeys(lit for lit in lits if lit is not False))
    clauses.append(out)


def finish_group(name, start):
    groups[name] = {'first_clause': start + 1, 'last_clause': len(clauses),
                    'clauses': len(clauses) - start}


start = len(clauses)
for v in range(60):
    add(*(x(v, i) for i in range(18)))
    for i, j in itertools.combinations(range(18), 2):
        add(-x(v, i), -x(v, j))
finish_group('old_vertex_exactly_one', start)

start = len(clauses)
thresholds = []
for i, load in enumerate(loads):
    width = load + 1
    s = [[True] + [False] * width]
    for t in range(1, 61):
        row = [True]
        for k in range(1, width + 1):
            z = var()
            a, b, pin = s[t - 1][k], s[t - 1][k - 1], x(t - 1, i)
            # z iff a OR (pin AND b), with all directions retained.
            add(neg(a), z)
            add(-pin, neg(b), z)
            add(-z, a, pin)
            add(-z, a, b)
            row.append(z)
        s.append(row)
    add(s[60][load])
    add(-s[60][load + 1])
    thresholds.append(s)
finish_group('helper_exact_load_threshold_equivalences', start)

start = len(clauses)
minorders = [(a, b) for c in cliques for a, b in zip(c, c[1:])]
minorders += [(0, 3), (6, 10), (10, 14)]
for i, j in minorders:
    for v in range(60):
        add(-x(v, j), thresholds[i][v][1])
finish_group('legal_helper_minimum_pin_symmetry', start)

start = len(clauses)
for i, j in crosspairs:
    witnesses = []
    for u, v in edges:
        for a, b in ((u, v), (v, u)):
            z = var()
            add(-z, x(a, i))
            add(-z, x(b, j))
            add(z, -x(a, i), -x(b, j))
            witnesses.append(z)
    add(*witnesses)
finish_group('all_cross_component_helper_pairs', start)

start = len(clauses)
for i in range(18):
    clique = cliques[component[i]]
    for v in range(60):
        lits = [x(v, j) for j in clique]
        lits += [x(u, i) for u in a2[v]]
        lits += [x(w, j) for w in old[v] for j in clique if j != i]
        add(*lits)
finish_group('all_helper_old_exact_three_walk_conditions', start)

cnf = HERE / 'model.cnf'
with cnf.open('w') as f:
    f.write('c Fixed Bhakar C60, H=2K3+3K4, exact A^3 positivity\n')
    f.write(f'p cnf {nvars} {len(clauses)}\n')
    for clause in clauses:
        f.write(' '.join(map(str, clause)) + ' 0\n')
prepare_cpu = time.process_time() - START
assert prepare_cpu < 20
meta = {
    'source_controller': str(SOURCE / 'PARAMETERS.json'),
    'source_route_certificate': str(SOURCE / 'CONTROLLER_ROUTE_CERTIFICATE.json'),
    'source_author': params['controller_author'],
    'source_author_recipe': params['controller_author_recipe'],
    'source_edges': 150, 'source_vertices': 60,
    'helper_cliques': cliques, 'pin_loads': loads,
    'cross_component_unordered_pairs': 129,
    'old_vertex_color_variables': 1080, 'variables': nvars,
    'clauses': len(clauses), 'clause_groups': groups,
    'minimum_pin_orders': minorders,
    'old_vertex_0_forced_to_size4_orbit': False,
    'A2_is_exact_two_steps_including_self': True,
    'preparation_CPU_seconds': prepare_cpu,
    'preparation_CPU_budget_seconds': 20,
    'solver_CPU_budget_seconds': 60,
    'solver_wall_budget_seconds': 90,
    'total_scope_CPU_budget_seconds': 90,
    'old_fiber_BFS_calls': 0, 'fiber_generated': False,
    'matching_decomposition_assumed': False,
    'ports': 'sorted-neighbor local dart ports; arbitrary cross-port charts supplied separately'
}
dump('MODEL.json', meta)
print(json.dumps({'phase': 'MODEL_COMPLETE', **{k: meta[k] for k in
    ('variables', 'clauses', 'preparation_CPU_seconds')}}), flush=True)

# Lift only this process's own preparation limit; child has its own hard cap.
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))


def solver_limit():
    resource.setrlimit(resource.RLIMIT_CPU, (59, 60))


command = [str(ROOT / '.tools/lean-4.24.0-linux/bin/cadical'), '-t', '59',
           '-w', str(HERE / 'solver_solution.txt'), str(cnf)]
dump('SOLVER_STARTED.json', {'command': command, 'solver_calls': 1,
     'parent_pid': os.getpid(), 'wall_start_monotonic': time.monotonic()})
solver_start = time.monotonic()
timed_out = False
with (HERE / 'SOLVER.log').open('w') as log:
    p = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                         preexec_fn=solver_limit, start_new_session=True)
    dump('HANDLE.json', {'pid': p.pid, 'parent_pid': os.getpid(), 'command': command,
         'status': 'RUNNING_SINGLE_SOLVE', 'no_continuation': True})
    try:
        solver_exit = p.wait(timeout=90)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(p.pid, signal.SIGTERM)
        try:
            solver_exit = p.wait(timeout=1)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)
            solver_exit = p.wait()
solver_cpu = children_cpu()
solver_wall = time.monotonic() - solver_start
raw = (HERE / 'SOLVER.log').read_text()
status = ('SAT' if 's SATISFIABLE' in raw else
          'UNSAT' if 's UNSATISFIABLE' in raw else 'UNKNOWN')
result = {**meta, 'status': status, 'solver_calls': 1,
          'solver_exit_code': solver_exit, 'solver_CPU_seconds': solver_cpu,
          'solver_wall_seconds': solver_wall, 'wall_timeout': timed_out,
          'timer_continued': False, 'controller_generated': False,
          'Lean_calls': 0, 'Gemini_calls': 0, 'full_fiber_generated': False,
          'global_record_claim': False}
print(json.dumps({'phase': 'SOLVER_TERMINAL', 'status': status,
                  'solver_CPU_seconds': solver_cpu,
                  'solver_wall_seconds': solver_wall}), flush=True)

if status == 'SAT':
    # Decode only color variables; graph verification is a separate program.
    soltext = (HERE / 'solver_solution.txt').read_text()
    positive = set()
    for line in soltext.splitlines():
        if line.startswith('v '):
            positive.update(int(z) for z in line[2:].split() if int(z) > 0)
    colors = []
    for v in range(60):
        assigned = [i for i in range(18) if x(v, i) in positive]
        assert len(assigned) == 1, (v, assigned)
        colors.append(assigned[0])
    pins = [[v for v in range(60) if colors[v] == i] for i in range(18)]
    literal = set(edges)
    literal.update((v, 60 + colors[v]) for v in range(60))
    literal.update((60 + i, 60 + j) for c in cliques
                   for i, j in itertools.combinations(c, 2))
    with (HERE / 'controller78.literal.edges').open('w') as f:
        f.write('# 78 vertices, undirected simple edges, zero-based labels\n')
        for u, v in sorted(literal):
            f.write(f'{u} {v}\n')
    dump('PIN_PARTITION.json', {'old_vertex_color': colors, 'pin_groups': pins})
    remaining = 89 - children_cpu() - (time.process_time() - START)
    assert remaining > 0
    checked = subprocess.run([sys.executable, str(HERE / 'verify_witness.py')],
                             capture_output=True, text=True, timeout=min(20, remaining))
    (HERE / 'VERIFY.log').write_text(checked.stdout + checked.stderr)
    result['independent_verifier_exit'] = checked.returncode
    if checked.returncode == 0:
        result['verification'] = json.loads((HERE / 'VERIFIED.json').read_text())
        result['controller_generated'] = True
        result['status'] = 'SAT_CONTROLLER_INDEPENDENTLY_VERIFIED'
    else:
        result['status'] = 'SAT_VERIFICATION_FAILED'

result['total_scope_CPU_seconds'] = children_cpu() + time.process_time() - START
result['total_scope_wall_seconds'] = time.monotonic() - WALL
result['scope'] = 'Fixed accepted Bhakar C60; preserve all edges; H=2K3+3K4; stated exact pin loads'
if status == 'UNKNOWN':
    result['conclusion'] = 'Bounded UNKNOWN only; fixed model and broader controller families remain open; no timer continuation.'
elif status == 'UNSAT':
    result['conclusion'] = 'Only this fixed-source H decomposition is excluded, conditional on the saved reviewed exact translation.'
dump('TERMINAL.json', result)
dump('HANDLE.json', {'status': result['status'], 'solver_exit_code': solver_exit,
                      'no_continuation': True})
print(json.dumps(result, indent=2), flush=True)
