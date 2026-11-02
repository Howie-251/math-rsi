#!/usr/bin/env python3
"""Generate both domains; optimize only still-open orbit 4 once; direct BFS."""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import json
import os
import random
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'variable_fiber_candidates60_run'


def dump(path,value):
    path.write_text(json.dumps(value,indent=2)+'\n')


def write_edges(path,edges):
    path.write_text('60 240\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))


def seed(orbit,domain):
    rng=random.Random(20261012+orbit);edges=set();shifts=[]
    def add(u,v):
        assert u!=v
        edges.add(tuple(sorted((u,v))))
    for i,d in enumerate(domain['d']):
        local=set()
        if d==1:local={(x,x+5) for x in range(5)}
        elif d==2:local={tuple(sorted((x,(x+1)%10))) for x in range(10)}
        elif d==3:
            local={(x,x+5) for x in range(5)}
            local|={tuple(sorted((x,(x+1)%5))) for x in range(5)}
            local|={tuple(sorted((x+5,(x+2)%5+5))) for x in range(5)}
        else:assert d==0
        for u,v in local:add(10*i+u,10*i+v)
    for i,j in combinations(range(6),2):
        chosen=sorted(rng.sample(range(10),domain['Q'][i][j]))
        shifts.append(dict(fibers=[i,j],shifts=chosen))
        for t in chosen:
            for x in range(10):add(10*i+x,10*j+(x+t)%10)
    assert len(edges)==240
    path=OUT/f'orbit{orbit}.seed.edges';write_edges(path,edges)
    dump(OUT/f'orbit{orbit}.seed.json',dict(orbit=orbit,n=60,edges=sorted(edges),domain=domain,
        random_seed=20261012+orbit,cyclic_shifts=shifts,
        internal_graphs={0:'empty',1:'pairs x--x+5',2:'cycle C10',3:'Petersen outer +1, inner +2, spokes'},
        optimization_status='not started; orbit analytically closed before optimization' if orbit==1 else 'single bounded run follows'))
    return path


def verify(path,domain):
    rows=path.read_text().splitlines();assert tuple(map(int,rows[0].split()))==(60,240)
    edges=[tuple(map(int,row.split())) for row in rows[1:]]
    assert len(edges)==len(set(edges))==240
    ns=[set() for _ in range(60)]
    for u,v in edges:
        assert 0<=u<v<60
        ns[u].add(v);ns[v].add(u)
    assert all(len(row)==8 for row in ns)
    for u in range(60):
        for j in range(6):
            expected=domain['d'][u//10] if j==u//10 else domain['Q'][u//10][j]
            assert sum(v//10==j for v in ns[u])==expected
    bad=[];distance_histogram=Counter();diameter=0
    for u in range(60):
        dist={u:0};queue=deque([u])
        while queue:
            x=queue.popleft()
            for y in ns[x]:
                if y not in dist:dist[y]=dist[x]+1;queue.append(y)
        assert len(dist)==60
        diameter=max(diameter,max(dist.values()))
        for v in range(u+1,60):
            distance_histogram[dist[v]]+=1
            if dist[v]>2:bad.append(dict(pair=[u,v],fibers=[u//10,v//10],distance=dist[v],
                zero_defect_block=domain['defect_quotient'][u//10][v//10]==0,
                common_neighbors=sorted(ns[u]&ns[v]),neighbors_u=sorted(ns[u]),neighbors_v=sorted(ns[v])))
    defect=[[len(ns[u]&ns[v])+int(v in ns[u])-7*int(u==v)-1 for v in range(60)] for u in range(60)]
    assert all(sum(row)==5 for row in defect)
    for u in range(60):
        for j in range(6):assert sum(defect[u][10*j:10*j+10])==domain['defect_quotient'][u//10][j]
    blocks=[]
    for i in range(6):
        for j in range(i,6):
            values=[defect[u][v] for u in range(10*i,10*i+10) for v in range(10*j,10*j+10) if u<v]
            missing=values.count(-1);excess=sum(max(0,x) for x in values)
            assert all(x>=-1 for x in values)
            target=domain['defect_quotient'][i][j]
            assert excess-missing==(5 if i==j else 10)*target
            blocks.append(dict(fibers=[i,j],defect_quotient_entry=target,missing_pairs=missing,
                positive_route_excess=excess,defect_histogram=dict(sorted(Counter(values).items()))))
    result=dict(n=60,edges=240,degree_histogram=dict(Counter(map(len,ns))),
        equitable_internal_and_cross_degrees_verified=True,diameter=diameter,
        distance_histogram=dict(sorted(distance_histogram.items())),bad_pair_count=len(bad),
        zero_defect_block_bad_pairs=sum(w['zero_defect_block'] for w in bad),
        bad_pairs=bad,route_defect=defect,route_defect_row_sums=[sum(row) for row in defect],
        quotient_defect_row_blocks_verified=True,block_statistics=blocks)
    dump(path.with_suffix('.verification.json'),result)
    return {k:result[k] for k in ('n','edges','degree_histogram','diameter','bad_pair_count','zero_defect_block_bad_pairs','block_statistics')}


def limits():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))


def main():
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'resources.json').exists(),'No unchanged bounded-search repeat.'
    data=json.loads((HERE/'six_fiber_variable_internal_run/verification.json').read_text())['orbits']
    domains={1:data[0],4:data[3]};checks={}
    for orbit,domain in domains.items():
        path=seed(orbit,domain);checks[f'orbit{orbit}_seed']=verify(path,domain)
    domain=domains[4]
    flat=[4]+domain['d']+[x for row in domain['Q'] for x in row]+[x for row in domain['defect_quotient'] for x in row]
    (OUT/'orbit4.domain.txt').write_text(' '.join(map(str,flat))+'\n')
    cmd=[str(HERE/'variable_fiber_candidates60_search.bin'),str(OUT/'orbit4.domain.txt'),
         str(OUT/'orbit4.seed.edges'),str(OUT/'orbit4')]
    began=time.monotonic()
    with (OUT/'orbit4.search.log').open('w') as out:
        p=subprocess.Popen(cmd,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    resources=dict(command=cmd,exit_code=p.returncode,wall_seconds=time.monotonic()-began,
        user_cpu_seconds=usage.ru_utime,system_cpu_seconds=usage.ru_stime,
        total_cpu_seconds=usage.ru_utime+usage.ru_stime,max_rss_kib=usage.ru_maxrss,
        threads=1,process_cpu_limit_seconds=30,internal_optimization_budget_seconds=27,
        orbit1_optimization_runs=0,orbit4_optimization_runs=1)
    dump(OUT/'resources.json',resources);assert p.returncode==0
    report=json.loads((OUT/'orbit4.search.json').read_text())
    for name in ('best_bad','best_zero','best_energy'):
        checks['orbit4_'+name]=verify(OUT/f'orbit4.{name}.edges',domain)
        assert checks['orbit4_'+name]['bad_pair_count']==report[name]['bad_pairs']
        assert checks['orbit4_'+name]['zero_defect_block_bad_pairs']==report[name]['zero_block_bad_pairs']
    dump(OUT/'verification.json',checks)
    print(json.dumps(dict(resources=resources,search={k:v for k,v in report.items() if k!='energy_progress'},
        graph_checks={k:{a:v[a] for a in ('diameter','bad_pair_count','zero_defect_block_bad_pairs')} for k,v in checks.items()}),indent=2))


if __name__=='__main__':main()
