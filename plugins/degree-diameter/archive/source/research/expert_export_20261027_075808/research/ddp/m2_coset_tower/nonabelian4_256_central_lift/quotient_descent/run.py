#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json
import os
import random
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
SOURCE = PARENT.parent / 'nonabelian4_256_search'
assert not (HERE / 'run.json').exists(), 'One authorized profile; do not restart'


def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


def dump(name, value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n')


start, wall = cpu(), time.monotonic()
source=json.loads((SOURCE/'best.json').read_text())
assert source['score']['bad_unordered_pairs']==832
eu,ev,tree,free=source['edge_u'],source['edge_v'],source['tree_edge_indices'],source['free_edge_indices']
q=[(h%32)%16+16*(h//32) for h in source['voltages']]
z=sum(((source['voltages'][e]%32)//16)<<k for k,e in enumerate(free))
assert len(free)==13 and all(q[e]==0 for e in tree)
groups={}
for e, endpoints in enumerate(zip(eu,ev)):groups.setdefault(endpoints,[]).append(e)


def legal_projection(q):
    return all(max(Counter(q[e] for e in group).values())<=2 for group in groups.values())


assert legal_projection(q)
start1=q.copy();start1[8]=31;start1[13]=29
assert legal_projection(start1) and start1!=q
starts=[q,start1];rng=random.Random(20261027080);draws=0
while len(starts)<16:
    draws+=1; candidate=[0]*16
    for e in free:candidate[e]=rng.randrange(32)
    if legal_projection(candidate) and candidate not in starts:starts.append(candidate)
dump('starts.json',{'source':'old832 projection; observed two-coordinate cursor52852;14 fresh conditional-uniform projections',
                    'seed':20261027080,'fresh_count':14,'raw_uniform_projection_draws':draws,'starts':starts})
with (HERE/'starts.txt').open('w') as f:
    f.write('16\n');f.write('\n'.join(' '.join(map(str,s)) for s in starts)+'\n')
with (HERE/'input.txt').open('w') as f:
    f.write('16\n');f.write('\n'.join(f'{a} {b}' for a,b in zip(eu,ev))+'\n')
    f.write(' '.join(map(str,tree))+'\n'+' '.join(map(str,q))+'\n')
dist=json.loads((SOURCE/'best.independent_distances.json').read_text())
assert len(dist)==256 and all(len(r)==256 for r in dist)
reference=[[v if 0<=v<=3 else -1 for v in dist[64*r]] for r in range(4)]
assert sum(v<0 for row in reference for v in row)==26
with (HERE/'source_reference.txt').open('w') as f:
    f.write(f'{z} 26\n');f.write('\n'.join(' '.join(map(str,row)) for row in reference)+'\n')
with (HERE/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=180-prep-1
assert remaining>0
metadata={'status':'AUTHORIZED_BOUNDED_PROFILE','group':'Q64 central quotient D32','n':256,'degree':8,'target_D':3,
          'base_multiplicities':[3,3,2,2,3,3],'tree':tree,'free_edges':free,
          'starts':16,'source_start':0,'observed_two_coordinate_start':1,'fresh_starts':14,
          'fresh_seed':20261027080,'kick_rng':'std::mt19937_64 seeded20261027080, separate from Python start generator',
          'segments_per_start':9,'maximum_strict_moves_per_segment':30,'full_single_coordinate_neighborhood':403,
          'objective':'lexicographic(L=2*Nempty+Nsingleton-distinct-affine-forms,Nempty,minimum actual center deficit only when L0)',
          'projection_legality':'up to2 identical quotient voltages among parallel edges; full GF2 legality system must be consistent',
          'phase_filter':None,'kicks':'two distinct free coordinates, both changed; retain only final GF2-legal projection',
          'center_search':'only L0 projections; all8192 masks considered subject to legality, exact sparse bad-affine-subspace score; immediate stop at0',
          'source_calibration':'four roots*256 radius3 entries compared to saved independent source distances; no BFS and no source8192 scan',
          'best_policy':'if no L0, only projection/L artifact; otherwise unique best actual center lift saved',
          'CPU_budget_seconds':180,'worker_count':1,'preparation_compile_CPU_seconds':prep,
          'process_CPU_limit_seconds':remaining,'entire_family_exhausted':False}
dump('metadata.json',metadata)
with (HERE/'search.log').open('w') as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],stdout=log,stderr=subprocess.STDOUT)
    run={'status':'RUNNING','running':True,'pid':process.pid,'driver_pid':os.getpid(),'worker_count':1,
         'CPU_budget_seconds':180,'preparation_compile_CPU_seconds':prep,'process_CPU_limit_seconds':remaining,
         'starts':16,'fresh_starts':14,'start1_two_coordinate_cursor':52852}
    dump('run.json',run);print(json.dumps(run),flush=True);code=process.wait()
assert code==0, f'Exit {code}; preserve cursor and outputs, no automatic restart'
terminal=json.loads((HERE/'search.terminal.json').read_text())
total=cpu()-start
terminal.update(preparation_compile_CPU_seconds=prep,total_measured_CPU_seconds=total,
                wall_seconds=time.monotonic()-wall,CPU_budget_seconds=180,worker_count=1,restarts=0,
                pending=['Root independent final validation of saved graph'] if terminal['saved_graph'] else [])
dump('terminal.json',terminal)
run.update(status=terminal['status'],running=False,exit_code=code,total_CPU_seconds=total,
           evaluated_legal_projections=terminal['evaluated_legal_projections'],best=terminal['best'])
dump('run.json',run);print(json.dumps(terminal,indent=2),flush=True)
