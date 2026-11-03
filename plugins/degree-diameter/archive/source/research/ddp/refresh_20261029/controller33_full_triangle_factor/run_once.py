#!/usr/bin/env python3
"""One exact shared-route controller SAT, retaining the complete fixed family."""
from pathlib import Path
import itertools
import json
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
assert not (HERE / 'TERMINAL.json').exists(), 'The fixed batch is already terminal'
started = time.process_time()
wall = time.monotonic()
children0 = resource.getrusage(resource.RUSAGE_CHILDREN)
N = 33
stream = (HERE / 'clauses.tmp').open('w')
variables = clauses = 0
and_cache = {}


def fresh():
    global variables
    variables += 1
    return variables


def clause(xs):
    global clauses
    if any(x is True for x in xs):
        return
    xs = [x for x in xs if x is not False]
    stream.write(' '.join(map(str, xs)) + ' 0\n')
    clauses += 1


def both(a, b):
    if a is False or b is False:
        return False
    if a is True:
        return b
    if b is True or a == b:
        return a
    key = tuple(sorted((a, b)))
    if key not in and_cache:
        z = fresh()
        and_cache[key] = z
        clause([-z, a])
        clause([-z, b])
        clause([z, -a, -b])
    return and_cache[key]


def either(xs):
    if any(x is True for x in xs):
        return True
    xs = sorted(set(x for x in xs if x is not False))
    if not xs:
        return False
    if len(xs) == 1:
        return xs[0]
    z = fresh()
    clause([-z] + xs)
    for x in xs:
        clause([z, -x])
    return z


edge_variables = {(u, v): fresh() for u in range(N) for v in range(u + 1, N)
                  if u // 3 != v // 3}
assert len(edge_variables) == 495


def adj(u, v):
    if u == v:
        return False
    if u // 3 == v // 3:
        return True
    return edge_variables[tuple(sorted((u, v)))]


for u in range(N):
    xs = [adj(u, v) for v in range(N) if v // 3 != u // 3]
    assert len(xs) == 30
    clause(xs)
    for i, x in enumerate(xs):
        clause([-x] + xs[:i] + xs[i+1:])
    previous = None
    for x in xs:
        one, two = fresh(), fresh()
        clause([-x, one])
        if previous is None:
            clause([-two])
        else:
            p1, p2 = previous
            clause([-p1, one])
            clause([-p2, two])
            clause([-x, -p1, two])
            clause([-x, -p2])
        previous = one, two
clause([adj(0, 3)])
clause([adj(0, 6)])

r2 = {}
for u in range(N):
    for v in range(u + 1, N):
        r2[u, v] = either([both(adj(u, x), adj(x, v))
                          for x in range(N) if x not in (u, v)])


def exact_two(u, v):
    return True if u == v else r2[tuple(sorted((u, v)))]


for u in range(N):
    for v in range(u + 1, N):
        clause([adj(u, v)] + [both(adj(u, x), exact_two(x, v))
                              for x in range(N) if x not in (u, v)])
stream.close()
cnf = HERE / 'model.cnf'
with cnf.open('w') as output:
    output.write(f'p cnf {variables} {clauses}\n')
    with (HERE / 'clauses.tmp').open() as source:
        for line in source:
            output.write(line)
model = dict(status='CNF_READY', controller_order=N, extra_edge_variables=495,
             all_variables=variables, clauses=clauses,
             condition='adjacent or exact-three-walk for every distinct pair; self has fixed triangle',
             fixed_extra_edges=[[0, 3], [0, 6]], solver_wall_limit=90,
             encoding_CPU_seconds=time.process_time()-started)
(HERE / 'MODEL.json').write_text(json.dumps(model, indent=2)+'\n')
(HERE / 'EDGE_VARIABLES.json').write_text(json.dumps(
    [dict(edge=k, var=v) for k, v in edge_variables.items()], indent=2)+'\n')
print(json.dumps(model), flush=True)


def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (100, 101))


command = [str(PROJECT / '.tools/lean-4.24.0-linux/bin/cadical'), '-q', '-t', '90', str(cnf)]
with (HERE / 'solver.stdout').open('w') as output:
    proc = subprocess.Popen(command, stdout=output, stderr=output, preexec_fn=limit)
    handle = dict(status='RUNNING', pid=proc.pid, command=command,
                  scope='complete33_triangle_factor_shared_routes')
    (HERE / 'HANDLE.json').write_text(json.dumps(handle, indent=2)+'\n')
    print(json.dumps(handle), flush=True)
    observation_expired = False
    try:
        code = proc.wait(timeout=105)
    except subprocess.TimeoutExpired:
        observation_expired = True
        proc.kill()
        code = proc.wait()
result = dict(status='RAW_UNSAT_UNCERTIFIED' if code == 20 else 'UNKNOWN',
              solver_exit_code=code, solver_calls=1, observation_expired=observation_expired,
              valid_controllers=0, complete4125_graphs=0)
if code == 10:
    selected = set()
    for line in (HERE / 'solver.stdout').read_text().splitlines():
        if line.startswith('v '):
            selected.update(int(x) for x in line[2:].split() if int(x) > 0)
    G = [{3*(u//3)+j for j in range(3) if 3*(u//3)+j != u} for u in range(N)]
    extra = [set() for _ in range(N)]
    for (u, v), var in edge_variables.items():
        if var in selected:
            G[u].add(v)
            G[v].add(u)
            extra[u].add(v)
            extra[v].add(u)
    assert all(len(G[u]) == 4 and len(extra[u]) == 2 for u in range(N))
    witnesses = []
    for u in range(N):
        for v in range(N):
            if v in G[u]:
                witnesses.append(dict(u=u, v=v, adjacent=True))
                continue
            path = next(([u, x, y, v] for x in sorted(G[u]) for y in sorted(G[x])
                         if y != u and v in G[y] and v != x), None)
            assert path is not None
            witnesses.append(dict(u=u, v=v, path=path))
    controller = [[-1]*4 for _ in range(N)]
    for u in range(N):
        t, j = divmod(u, 3)
        controller[u][0], controller[u][1] = 3*t+(j+1)%3, 3*t+(j-1)%3
    unseen = set(range(N))
    cycles = []
    while unseen:
        root = min(unseen)
        cycle, previous, current = [], None, root
        while True:
            cycle.append(current)
            unseen.remove(current)
            following = min(extra[current]) if previous is None else next(x for x in extra[current] if x != previous)
            controller[current][2] = following
            controller[following][3] = current
            previous, current = current, following
            if current == root:
                break
        cycles.append(cycle)
    assert all(set(row) == G[u] and len(set(row)) == 4 for u, row in enumerate(controller))
    inverse = [1, 0, 3, 2]
    assert all(controller[controller[u][p]][inverse[p]] == u for u in range(N) for p in range(4))
    with (HERE / 'CONTROLLER33.edges').open('w') as output:
        output.write('33 66\n')
        for u in range(N):
            for v in sorted(G[u]):
                if u < v:
                    output.write(f'{u} {v}\n')
    for name, obj in [('CONTROLLER33.json', controller), ('PAIR_WITNESSES.json', witnesses),
                      ('EXTRA_CYCLES.json', cycles)]:
        (HERE / name).write_text(json.dumps(obj, indent=2)+'\n')
    result.update(status='CONTROLLER33_HIT_NEEDS_F5_FULL_GENERATION', valid_controllers=1,
                  checked_ordered_pairs=N*N, extra_cycles=[len(c) for c in cycles])
children = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = children.ru_utime+children.ru_stime-children0.ru_utime-children0.ru_stime
result.update(child_CPU_seconds=child_cpu, driver_CPU_seconds=time.process_time()-started,
              aggregate_CPU_seconds=child_cpu+time.process_time()-started,
              wall_seconds=time.monotonic()-wall, running=False)
for name in ['RESULT.json', 'TERMINAL.json', 'HANDLE.json']:
    (HERE / name).write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result), flush=True)
