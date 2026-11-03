#!/usr/bin/env python3
"""Exact cyclic-orbit auxiliary graph model; no fixed permutation template."""
from pathlib import Path
import json
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
assert not (HERE/'TERMINAL.json').exists(), 'Fixed batch already finished'
START=time.process_time();WALL=time.monotonic()
child0=resource.getrusage(resource.RUSAGE_CHILDREN)
stream=(HERE/'clauses.tmp').open('w')
variables=clauses=0
and_cache={}


def fresh():
    global variables
    variables+=1
    return variables


def clause(values):
    global clauses
    if any(x is True for x in values):return
    values=[x for x in values if x is not False]
    stream.write(' '.join(map(str,values))+' 0\n');clauses+=1


def both(a,b):
    if a is False or b is False:return False
    if a is True:return b
    if b is True or a==b:return a
    key=tuple(sorted((a,b)))
    if key in and_cache:return and_cache[key]
    out=fresh();and_cache[key]=out
    clause([-out,a]);clause([-out,b]);clause([out,-a,-b])
    return out


def either(values):
    if any(x is True for x in values):return True
    values=sorted(set(x for x in values if x is not False))
    if not values:return False
    if len(values)==1:return values[0]
    out=fresh();clause([-out]+values)
    for x in values:clause([out,-x])
    return out


def key(u,v):
    a,l=divmod(u,8);b,m=divmod(v,8)
    if l<m:return (l,m,(b-a)%8)
    if l>m:return (m,l,(a-b)%8)
    d=(b-a)%8
    return (l,l,min(d,(-d)%8))


orbits={}
for u in range(64):
    for v in range(u+1,64):orbits.setdefault(key(u,v),[]).append((u,v))
assert len(orbits)==256
edge_vars={}
for k in sorted(orbits):
    l,m,d=k
    if not (d==0 and (l^m) in (1,2,4)):edge_vars[k]=fresh()
assert len(edge_vars)==244


def adj(u,v):
    if u==v:return False
    k=key(u,v)
    return edge_vars[k] if k in edge_vars else True


for label in range(8):
    xs=[adj(label,v) for v in range(64) if v!=label and adj(label,v) is not True]
    assert len(xs)==60
    # At least two actual neighbor occurrences, including repeated orbit vars.
    clause(xs)
    for i,x in enumerate(xs):clause([-x]+xs[:i]+xs[i+1:])
    prev=None
    for x in xs:
        one,two=fresh(),fresh();clause([-x,one])
        if prev is None:clause([-two])
        else:
            p1,p2=prev
            clause([-p1,one]);clause([-p2,two]);clause([-x,-p1,two]);clause([-x,-p2])
        prev=(one,two)
canonical_odd=[(0,0,1),(0,1,1),(0,3,1),(0,7,1)]
clause([edge_vars[k] for k in canonical_odd])

r2={}
for k in sorted(orbits):
    l,m,d=k;u=l;v=8*d+m
    r2[k]=either([adj(u,v)]+[both(adj(u,w),adj(w,v)) for w in range(64) if w not in (u,v)])


def reach2(u,v):return True if u==v else r2[key(u,v)]


targets=[]
for k in sorted(orbits):
    l,m,d=k
    if d==0:continue
    u=l;v=8*d+m
    clause([reach2(u,v)]+[both(adj(u,w),reach2(w,v)) for w in range(64) if w not in (u,v)])
    targets.append(k)
assert len(targets)==228
stream.close()
cnf=HERE/'model.cnf'
with cnf.open('wb') as out:
    out.write(f'p cnf {variables} {clauses}\n'.encode())
    with (HERE/'clauses.tmp').open('rb') as inp:
        while block:=inp.read(1024*1024):out.write(block)
meta=dict(status='CNF_READY',extra_edge_orbit_variables=244,pair_orbits=256,
          crosspencil_distance_orbits=228,all_variables=variables,clauses=clauses,
          degree_inputs='60 neighbor occurrences per label; repeated orbit vars retained',
          canonical_odd_orbits=canonical_odd,wall_limit_seconds=120,hard_CPU_limit_seconds=140,
          encoding_CPU_seconds=time.process_time()-START)
(HERE/'MODEL.json').write_text(json.dumps(meta,indent=2)+'\n')
(HERE/'EDGE_ORBITS.json').write_text(json.dumps([dict(key=k,var=q,edges=orbits[k]) for k,q in edge_vars.items()],separators=(',',':'))+'\n')
print(json.dumps(meta),flush=True)


def limit():resource.setrlimit(resource.RLIMIT_CPU,(140,141))


command=[str(PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t','120',str(cnf)]
with (HERE/'solver.stdout').open('w') as output:
    proc=subprocess.Popen(command,stdout=output,stderr=output,preexec_fn=limit)
    handle=dict(status='RUNNING',pid=proc.pid,stage='ONE_CYCLIC_ORBIT_SAT',command=command)
    (HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n');print(json.dumps(handle),flush=True)
    expired=False
    try:code=proc.wait(timeout=145)
    except subprocess.TimeoutExpired:expired=True;proc.kill();code=proc.wait()
result=dict(status='RAW_UNSAT_UNCERTIFIED' if code==20 else 'UNKNOWN',solver_exit_code=code,
            solver_calls=1,wall_observation_expired=expired,auxiliary_positive_graphs=0,main1088_graphs=0)
if code==10:
    selected=set()
    for line in (HERE/'solver.stdout').read_text().splitlines():
        if line.startswith('v '):selected.update(int(x) for x in line[2:].split() if int(x)>0)
    G=[{u^1,u^2,u^4} for u in range(64)]
    selected_orbits=[]
    for k,q in edge_vars.items():
        if q in selected:
            selected_orbits.append(k)
            for u,v in orbits[k]:G[u].add(v);G[v].add(u)
    assert all(len(row)==5 and u not in row for u,row in enumerate(G))
    checked=0
    for root in range(64):
        visited={root}
        for _ in range(3):visited|={v for u in list(visited) for v in G[u]}
        assert len(visited)==64
        checked+=1
    with (HERE/'K64.edges').open('w') as out:
        out.write('64 160\n')
        for u,row in enumerate(G):
            for v in sorted(row):
                if u<v:out.write(f'{u} {v}\n')
    (HERE/'K64_ADJACENCY.json').write_text(json.dumps([sorted(row) for row in G])+'\n')
    (HERE/'HIT_ORBITS.json').write_text(json.dumps(selected_orbits,indent=2)+'\n')
    result.update(status='K64_D3_HIT_NEEDS_INDEPENDENT_CHECK',auxiliary_positive_graphs=1,
                  producer_roots_checked=checked,degree=5,D_at_most=3)
children=resource.getrusage(resource.RUSAGE_CHILDREN)
cpu=children.ru_utime+children.ru_stime-child0.ru_utime-child0.ru_stime
result.update(child_CPU_seconds=cpu,driver_CPU_seconds=time.process_time()-START,
              aggregate_CPU_seconds=cpu+time.process_time()-START,wall_seconds=time.monotonic()-WALL)
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',pid=proc.pid,result='RESULT.json'))+'\n')
print(json.dumps(result),flush=True)
