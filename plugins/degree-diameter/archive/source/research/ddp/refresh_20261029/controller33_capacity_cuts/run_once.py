#!/usr/bin/env python3
"""Prepare the stronger exact controller formula, or solve that existing formula once."""
from pathlib import Path
import argparse
import itertools
import json
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
assert (PROJECT / '.tools/lean-4.24.0-linux/bin/cadical').is_file()
parser = argparse.ArgumentParser()
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument('--prepare-only', action='store_true')
mode.add_argument('--solve', action='store_true')
args = parser.parse_args()
started = time.process_time()
wall = time.monotonic()
children0 = resource.getrusage(resource.RUSAGE_CHILDREN)
if args.prepare_only:
    assert not (HERE / 'MODEL.json').exists(), 'Prepared formula already exists; do not overwrite it.'
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

    # Full first-discovery block canonicalization; every connected graph has a representative.
    prefix = {}
    for block in range(1, 11):
        previous = False
        for parent in range(3*block):
            current = either([previous] + [adj(parent, 3*block+j) for j in range(3)])
            prefix[block, parent] = current
            # At the first true prefix, the edge must hit this block's representative.
            clause([-current, previous, adj(parent, 3*block)])
            previous = current
        clause([previous])
    for block in range(1, 10):
        for parent in range(3*block):
            clause([-prefix[block+1, parent], prefix[block, parent]])

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

    assert (variables, clauses) == (31845, 109466)
    baseline = dict(all_variables=variables, clauses=clauses)
    stages = []
    triple_count = 0
    for A in range(11):
        for B in range(A + 1, 11):
            es = [(3*A+a, 3*B+b) for a in range(3) for b in range(3)]
            for chosen in itertools.combinations(es, 3):
                perfect = len({u for u,v in chosen}) == 3 and len({v for u,v in chosen}) == 3
                if not perfect:
                    clause([-adj(u,v) for u,v in chosen])
                    triple_count += 1
    assert triple_count == 4290
    stages.append(dict(name='nonmatching_triples', all_variables=variables, clauses=clauses, added_clauses=triple_count))

    m3_flags = []
    incident = [[] for _ in range(11)]
    for A in range(11):
        for B in range(A + 1, 11):
            terms = []
            for permutation in itertools.permutations(range(3)):
                xs = [adj(3*A+a, 3*B+permutation[a]) for a in range(3)]
                terms.append(both(both(xs[0], xs[1]), xs[2]))
            flag = either(terms)
            incident[A].append(flag); incident[B].append(flag)
            m3_flags.append(dict(blocks=[A,B], flag=flag, matching_terms=terms))
    for flags in incident:
        assert len(flags) == 10
        for a,b in itertools.combinations(flags,2):
            clause([-a,-b])
    stages.append(dict(name='exact_m3_and_block_matching', all_variables=variables, clauses=clauses))

    weighted = [[] for _ in range(N)]
    pair_terms = []
    for A in range(11):
        for B in range(A + 1, 11):
            es = [(3*A+a, 3*B+b) for a in range(3) for b in range(3)]
            for e,f in itertools.combinations(es,2):
                (a,b),(c,d) = e,f
                z = both(adj(a,b), adj(c,d))
                if a == c:
                    third = next(v for v in range(3*B,3*B+3) if v not in (b,d))
                    weights = [(a,2),(b,2),(d,2),(third,1)]
                elif b == d:
                    third = next(v for v in range(3*A,3*A+3) if v not in (a,c))
                    weights = [(b,2),(a,2),(c,2),(third,1)]
                else:
                    weights = [(v,1) for v in (a,b,c,d)]
                for v,weight in weights:
                    weighted[v].extend([z]*weight)
                pair_terms.append(dict(edges=[e,f], literal=z, weights=weights))
    assert len(pair_terms) == 1980
    assert all(len(xs) == 330 for xs in weighted)

    def at_most_three_occurrences(xs):
        # Intentionally preserve duplicates: two copies of x count as weight2.
        previous = None
        for x in xs:
            current = [fresh() for _ in range(3)]
            clause([-x,current[0]])
            if previous is None:
                clause([-current[1]]); clause([-current[2]])
            else:
                for j in range(3):
                    clause([-previous[j],current[j]])
                for j in range(1,3):
                    clause([-x,-previous[j-1],current[j]])
                clause([-x,-previous[2]])
            previous = current
    for xs in weighted:
        at_most_three_occurrences(xs)
    stages.append(dict(name='weighted_pair_capacity_at_most3', all_variables=variables, clauses=clauses))
    stream.close()
    cnf = HERE / 'model.cnf'
    with cnf.open('w') as output:
        output.write(f'p cnf {variables} {clauses}\n')
        with (HERE / 'clauses.tmp').open() as source:
            for line in source:
                output.write(line)
    model = dict(status='CNF_READY_NOT_SOLVED', controller_order=N, extra_edge_variables=495,
                 all_variables=variables, clauses=clauses,
                 condition='adjacent or exact-three-walk for every distinct pair; fixed triangles handle self',
                 fixed_extra_edges=[[0,3],[0,6]], solver_wall_limit=60, total_CPU_budget=90,
                 canonicalization='ordered first-discovery block parents, earliest touch at 3*block',
                 inherited_baseline=baseline, stages=stages,
                 forbidden_nonmatching_triples=triple_count, exact_m3_flags=len(m3_flags),
                 pair_conjunction_terms=len(pair_terms), weighted_occurrences_per_vertex=330,
                 weighted_bound_per_vertex=3, solver_calls=0,
                 encoding_CPU_seconds=time.process_time()-started)
    (HERE / 'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
    (HERE / 'EDGE_VARIABLES.json').write_text(json.dumps([dict(edge=k,var=v) for k,v in edge_variables.items()],indent=2)+'\n')
    (HERE / 'CAPACITY_TERMS.json').write_text(json.dumps(dict(m3_flags=m3_flags,pair_terms=pair_terms,weighted_inputs=weighted),indent=2)+'\n')
    print(json.dumps(model),flush=True)
    raise SystemExit

# --solve never executes the preparation branch or rewrites its CNF.
assert args.solve
assert not (HERE / 'HANDLE.json').exists(), 'This once-only solver invocation already has a handle.'
assert not (HERE / 'TERMINAL.json').exists(), 'The fixed batch is already terminal.'
model = json.loads((HERE / 'MODEL.json').read_text())
assert model['status'] == 'CNF_READY_NOT_SOLVED'
N = model['controller_order']
cnf = HERE / 'model.cnf'
assert cnf.is_file()
edge_variables = {tuple(row['edge']):row['var'] for row in json.loads((HERE/'EDGE_VARIABLES.json').read_text())}
assert len(edge_variables) == 495

def limit():
    resource.setrlimit(resource.RLIMIT_CPU,(70,71))

command = [str(PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t','60',str(cnf)]
with (HERE/'solver.stdout').open('w') as output:
    proc = subprocess.Popen(command,stdout=output,stderr=output,preexec_fn=limit)
    handle = dict(status='RUNNING',pid=proc.pid,command=command,
                  scope='complete33_triangle_factor_canonical_route_capacity_cuts')
    (HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
    print(json.dumps(handle),flush=True)
    observation_expired = False
    try:
        code = proc.wait(timeout=75)
    except subprocess.TimeoutExpired:
        observation_expired = True;proc.kill();code=proc.wait()
result = dict(status='RAW_UNSAT_UNCERTIFIED' if code == 20 else 'UNKNOWN',
              solver_exit_code=code,solver_calls=1,observation_expired=observation_expired,
              valid_controllers=0,complete4125_graphs=0)
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
solve_cpu = child_cpu+time.process_time()-started
result.update(child_CPU_seconds=child_cpu,driver_CPU_seconds=time.process_time()-started,
              preparation_CPU_seconds=model['encoding_CPU_seconds'],solve_CPU_seconds=solve_cpu,
              aggregate_CPU_seconds=model['encoding_CPU_seconds']+solve_cpu,
              total_CPU_budget=90,wall_seconds=time.monotonic()-wall,running=False)
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:
    (HERE/name).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
