#!/usr/bin/env python3
"""The complete31-point chain-motif controller model; separate preparation and solving."""
from pathlib import Path
import argparse
import itertools
import json
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
assert (PROJECT/'.tools/lean-4.24.0-linux/bin/cadical').is_file()
parser=argparse.ArgumentParser()
mode=parser.add_mutually_exclusive_group(required=True)
mode.add_argument('--prepare-only',action='store_true')
mode.add_argument('--solve',action='store_true')
args=parser.parse_args()
started=time.process_time();wall=time.monotonic()
children0=resource.getrusage(resource.RUSAGE_CHILDREN)
N=31
triangles=[(0,1,2),(2,3,4),(4,5,6)]+[tuple(range(7+3*b,10+3*b)) for b in range(8)]
fixed_edges={tuple(sorted(e)) for t in triangles for e in itertools.combinations(t,2)}
fixed_degree=[sum(v in e for e in fixed_edges) for v in range(N)]
free=[v for v in range(N) if fixed_degree[v]==2]
assert len(fixed_edges)==33 and len(free)==29
assert [v for v in range(N) if fixed_degree[v]==4]==[2,4]
if args.prepare_only:
    assert not (HERE/'MODEL.json').exists(), 'This formula is already prepared.'
    stream=(HERE/'clauses.tmp').open('w')
    variables=clauses=0
    and_cache={}
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



    edge_variables={(u,v):fresh() for u,v in itertools.combinations(free,2) if (u,v) not in fixed_edges}
    assert len(edge_variables)==380

    def adj(u,v):
        if u==v:return False
        e=tuple(sorted((u,v)))
        return True if e in fixed_edges else edge_variables.get(e,False)

    for u in free:
        xs=[var for e,var in edge_variables.items() if u in e]
        clause(xs)
        for i,x in enumerate(xs):clause([-x]+xs[:i]+xs[i+1:])
        previous=None
        for x in xs:
            one,two=fresh(),fresh();clause([-x,one])
            if previous is None:clause([-two])
            else:
                p1,p2=previous
                clause([-p1,one]);clause([-p2,two]);clause([-x,-p1,two]);clause([-x,-p2])
            previous=one,two
    assert all(all(v not in e for e in edge_variables) for v in [2,4])

    # Canonicalize only the eight disjoint triangles outside initial labels0..6.
    prefix={}
    for block in range(8):
        start=7+3*block;previous=False
        for parent in range(start):
            current=either([previous]+[adj(parent,start+j) for j in range(3)])
            prefix[block,parent]=current
            clause([-current,previous,adj(parent,start)])
            previous=current
        clause([previous])
    for block in range(7):
        for parent in range(7+3*block):
            clause([-prefix[block+1,parent],prefix[block,parent]])

    r2={}
    for u in range(N):
        for v in range(u+1,N):
            r2[u,v]=either([both(adj(u,x),adj(x,v)) for x in range(N) if x not in (u,v)])
    def exact_two(u,v):return True if u==v else r2[tuple(sorted((u,v)))]
    for u in range(N):
        for v in range(u+1,N):
            clause([adj(u,v)]+[both(adj(u,x),exact_two(x,v)) for x in range(N) if x not in (u,v)])
    stream.close()
    cnf=HERE/'model.cnf'
    with cnf.open('w') as out:
        out.write(f'p cnf {variables} {clauses}\n')
        with (HERE/'clauses.tmp').open() as inp:
            for line in inp:out.write(line)
    model=dict(status='CNF_READY_NOT_SOLVED',controller_order=N,fixed_triangles=triangles,
               fixed_internal_edges=len(fixed_edges),centers_without_variable_edges=[2,4],free_vertices=free,
               extra_edge_variables=len(edge_variables),selected_extra_edges=29,expected_edges=62,
               all_variables=variables,clauses=clauses,
               route_condition='adjacency or exact3walk for every distinct pair; fixed triangles give self NB3',
               canonicalization='only eight new K3 blocks, initial motif0..6 fixed, ordered first-discovery parents',
               fixed_extra_edges=[],C33_capacity_cuts=False,solver_calls=0,solver_wall_limit=90,
               total_CPU_budget=110,encoding_CPU_seconds=time.process_time()-started)
    assert model['encoding_CPU_seconds']<5
    (HERE/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
    (HERE/'EDGE_VARIABLES.json').write_text(json.dumps([dict(edge=e,var=v) for e,v in edge_variables.items()],indent=2)+'\n')
    print(json.dumps(model),flush=True)
    raise SystemExit

assert args.solve
assert not (HERE/'HANDLE.json').exists(), 'Once-only solver was already started.'
assert not (HERE/'TERMINAL.json').exists(), 'This batch already terminated.'
model=json.loads((HERE/'MODEL.json').read_text())
assert model['status']=='CNF_READY_NOT_SOLVED'
cnf=HERE/'model.cnf';assert cnf.is_file()
edge_variables={tuple(r['edge']):r['var'] for r in json.loads((HERE/'EDGE_VARIABLES.json').read_text())}
assert len(edge_variables)==380

def limit():resource.setrlimit(resource.RLIMIT_CPU,(100,101))
command=[str(PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t','90',str(cnf)]
with (HERE/'solver.stdout').open('w') as out:
    proc=subprocess.Popen(command,stdout=out,stderr=out,preexec_fn=limit)
    handle=dict(status='RUNNING',pid=proc.pid,command=command,scope='complete31_chain_motif_380_edge_variables')
    (HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n');print(json.dumps(handle),flush=True)
    observation_expired=False
    try:code=proc.wait(timeout=105)
    except subprocess.TimeoutExpired:
        observation_expired=True;proc.kill();code=proc.wait()
result=dict(status='RAW_UNSAT_UNCERTIFIED' if code==20 else 'UNKNOWN',solver_exit_code=code,
            solver_calls=1,observation_expired=observation_expired,valid_controllers=0,complete3875_graphs=0)
if code==10:
    selected=set()
    for line in (HERE/'solver.stdout').read_text().splitlines():
        if line.startswith('v '):selected.update(int(x) for x in line[2:].split() if int(x)>0)
    literal_edges=fixed_edges|{e for e,var in edge_variables.items() if var in selected}
    assert len(literal_edges)==62
    G=[set() for _ in range(N)]
    for u,v in literal_edges:
        assert 0<=u<v<N;G[u].add(v);G[v].add(u)
    assert all(len(row)==4 for row in G)
    witnesses=[]
    for u in range(N):
        for v in range(N):
            if v in G[u]:witnesses.append(dict(u=u,v=v,adjacent=True));continue
            path=next(([u,x,y,v] for x in sorted(G[u]) for y in sorted(G[x]) if y!=u and v in G[y] and v!=x),None)
            assert path is not None
            witnesses.append(dict(u=u,v=v,path=path))
    with (HERE/'CONTROLLER31.edges').open('w') as out:
        out.write('31 62\n')
        for u,v in sorted(literal_edges):out.write(f'{u} {v}\n')
    (HERE/'CONTROLLER31.adjacency.json').write_text(json.dumps([sorted(row) for row in G],indent=2)+'\n')
    (HERE/'PAIR_WITNESSES.json').write_text(json.dumps(witnesses,indent=2)+'\n')
    result.update(status='CONTROLLER31_HIT_NEEDS_GENERAL_PORT_FACTORIZATION_AND_F5_GENERATION',
                  valid_controllers=1,checked_ordered_pairs=N*N,ports_generated=False)
children=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=children.ru_utime+children.ru_stime-children0.ru_utime-children0.ru_stime
solve_cpu=child_cpu+time.process_time()-started
result.update(child_CPU_seconds=child_cpu,driver_CPU_seconds=time.process_time()-started,
              preparation_CPU_seconds=model['encoding_CPU_seconds'],solve_CPU_seconds=solve_cpu,
              aggregate_CPU_seconds=model['encoding_CPU_seconds']+solve_cpu,total_CPU_budget=110,
              wall_seconds=time.monotonic()-wall,running=False)
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:
    (HERE/name).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
