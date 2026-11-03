#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import subprocess

base = Path(__file__).resolve().parent
assert not (base/'profile.run.json').exists(), 'This authorized profile is one run only.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
source=base.parent/'affine_cayley820_capacity/profile.best.edges'
data=list(map(int,source.read_text().split())); assert data[:2]==[820,4920]
def relabel(u):
    x,j=u%41,u//41
    return (j%2)*410+x+41*(j//2)
expected={tuple(sorted((relabel(u),relabel(v)))) for u,v in zip(data[2::2],data[3::2])}
def mul(a,b):
    x,j=a%41,a//41; y,k=b%41,b//41
    return (x+pow(25,j,41)*y)%41+41*((j+k)%10)
def inv(a):
    x,j=a%41,a//41
    return (-pow(25,(-j)%10,41)*x)%41+41*((-j)%10)
fields=[0,36,28,22,0,25,24,13,34,6,16,17,3,8]
internal=[]
for offset in (0,4):
    a,c=fields[offset]+41,fields[offset+1]+123
    internal.append([a,inv(a),c,inv(c),fields[offset+2]+205,fields[offset+3]+205])
cross=[fields[8+i]+41*(1 if i<3 else 8) for i in range(6)]
actual=set()
for side in range(2):
    for h in range(410):
        u=side*410+h
        for s in internal[side]:actual.add(tuple(sorted((u,side*410+mul(h,s)))))
        for t in (cross if side==0 else list(map(inv,cross))):actual.add(tuple(sorted((u,(1-side)*410+mul(h,t)))))
assert actual==expected and len(actual)==4920
(base/'calibration.edges.json').write_text(json.dumps({'source':str(source.relative_to(base.parent)), 'old_encoding':'x+41*j','new_encoding':'(j%2)*410+x+41*(j//2)','source_edges':4920,'new_edges':4920,'edge_sets_exactly_equal':True,'fields':fields,'A':internal[0],'B':internal[1],'T':cross,'CPU_seconds':cpu()-start},indent=2)+'\n')
with (base/'profile.compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','profile.cpp','-o','profile'],cwd=base,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start; remaining=120-prep-1; assert remaining>0
run={'status':'RUNNING','running':True,'worker_count':1,'CPU_budget_seconds':120,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':remaining,'conservative_shutdown_reserve_seconds':1,'fixed_seed':2026102624}
(base/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
with (base/'profile.log').open('w') as log:
    process=subprocess.Popen([str(base/'profile'),str(base),str(remaining)],cwd=base,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(base/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n');code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start)
if code==0:
    terminal=json.loads((base/'profile.terminal.json').read_text());run['status']=terminal['status'];run['evaluated_candidates']=terminal['evaluated_candidates'];run['best_score']=terminal['best_score']
else:run['status']='PROCESS_ERROR'
(base/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
