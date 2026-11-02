from pathlib import Path
from collections import deque
import json,random,resource,subprocess,time,sys,os

OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3]
T=time.process_time();CH=resource.getrusage(resource.RUSAGE_CHILDREN);W=time.monotonic()
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np
def used():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-T+r.ru_utime+r.ru_stime-CH.ru_utime-CH.ru_stime
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2)+'\n')
fixed=sorted((3*g+a,3*g+b) for g in range(11) for a in range(3) for b in range(a+1,3))
starts=[];draws=[]
for i in range(8):
 rng=random.Random(20261027540+i);draw=0
 while True:
  order=list(range(33));rng.shuffle(order);draw+=1
  es=sorted(tuple(sorted((order[j],order[(j+1)%33]))) for j in range(33))
  if all(u//3!=v//3 for u,v in es):break
 assert len(set(es))==33;starts.append(es);draws.append(draw)
save('inputs.json',dict(n=33,degree=4,target_D=3,fixed_triangles=[[3*g+a for a in range(3)] for g in range(11)],fixed_edges=fixed,external_degree=2,external_edges_per_start=starts,start_seeds=list(range(20261027540,20261027548)),start_rejection_draws=draws,mutation_seed=20261027548,proposals_per_start=100000,objective='L=sum over all ordered pairs max(0,27-(I+3A+9A^2+27A^3)[u,v])',target_is_only_a_necessary_controller_condition=True,CPU_budget_seconds=45,workers=1,extra_triangles_allowed=True,old_scope_difference='The old31 fixed9K3+K4/diamond and fixed31 SAT do not cover this33-vertex11-disjoint-K3 factor and degree2 external port system.'))
text=['33 8 33']
for es in starts:text.extend(f'{u} {v}' for u,v in es)
(OUT/'inputs.txt').write_text('\n'.join(text)+'\n')
with (OUT/'compile.log').open('w') as log:subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=OUT,stdout=log,stderr=log,check=True)
subprocess.run(['./search','calibrate'],cwd=OUT,check=True)
def read_edges(name):
 rows=[tuple(map(int,s.split())) for s in (OUT/name).read_text().splitlines()];assert rows[0]==(33,66);return rows[1:]
def matrix(es):
 a=np.zeros((33,33),dtype=np.int64)
 for u,v in es:a[u,v]=a[v,u]=1
 assert int(a.sum())==132 and np.all(a.sum(axis=1)==4)
 return a
first=read_edges('first.edges');a=matrix(first);a2=a@a;a3=a2@a;upper=np.eye(33,dtype=np.int64)+3*a+9*a2+27*a3
cpp=np.loadtxt(OUT/'first.capacity.txt',dtype=np.int64);assert np.array_equal(cpp,upper)
expected=json.loads((OUT/'first.score.json').read_text());lack=int(np.maximum(0,27-upper).sum());slots=int((upper<27).sum());assert expected['lack']==lack and expected['slots']==slots
adj=[[] for _ in range(33)]
for u,v in first:adj[u].append(v);adj[v].append(u)
bad=0;diam=0
for r in range(33):
 dist=[-1]*33;dist[r]=0;q=deque([r])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
 bad+=sum(x<0 or x>3 for x in dist);diam=max(diam,max(dist))
assert bad%2==0 and bad//2==expected['bad']
save('first_calibration.json',dict(n=33,edges=66,degree=4,independent_integer_numpy_A2_A3=True,all_1089_capacity_entries_match=True,capacity_deficit_ordered=lack,insufficient_ordered_slots=slots,ordinary_BFS_roots=33,ordinary_diameter=diam,bad_unordered_pairs_gt3=bad//2,first_score_reused=True,CPU_used_before_production_seconds=used()))
(OUT/'first.cached.txt').write_text(f'{lack} {slots} {bad//2}\n')
remaining=max(0.,45.-used()-.5)
save('run.json',dict(status='RUNNING_PRODUCTION',running=True,remaining_production_CPU_seconds=remaining,CPU_used_before_production_seconds=used()))
with (OUT/'production.log').open('w') as log:
 proc=subprocess.Popen(['./search','search',str(remaining)],cwd=OUT,stdout=log,stderr=log);save('process.json',dict(pid=proc.pid,driver_pid=os.getpid()));assert proc.wait()==0
term=json.loads((OUT/'production_terminal.json').read_text());best=json.loads((OUT/'best.json').read_text());es=read_edges('best.edges');a=matrix(es)
assert len(set(es))==66 and set(fixed)<=set(es)
external=set(es)-set(fixed);assert len(external)==33 and all(u//3!=v//3 for u,v in external)
external_degree=[0]*33
for u,v in external:external_degree[u]+=1;external_degree[v]+=1
assert external_degree==[2]*33
a2=a@a;a3=a2@a;upper=np.eye(33,dtype=np.int64)+3*a+9*a2+27*a3
assert int(np.maximum(0,27-upper).sum())==best['capacity_deficit_ordered']
capacity=dict(formula='I+3A+9A^2+27A^3',minimum_upper_bound=int(upper.min()),deficit_ordered=int(np.maximum(0,27-upper).sum()),insufficient_ordered_slots=int((upper<27).sum()),exact_three_step_missing_ordered=int((a3==0).sum()),triangles=int(np.trace(a3))//6,upper=upper.tolist(),insufficient_slots=[dict(u=int(u),v=int(v),capacity_upper=int(upper[u,v])) for u,v in zip(*np.where(upper<27))],actual_fiber_lift_generated=False,only_a_necessary_condition=True)
save('best.capacity.json',capacity)
term.update(dict(total_measured_CPU_seconds=used(),total_wall_seconds=time.monotonic()-W,preparation_and_calibration_CPU_seconds=json.loads((OUT/'first_calibration.json').read_text())['CPU_used_before_production_seconds'],CPU_budget_seconds=45,workers=1,restarts=0,only_partial_controller=True,fiber_lift_generated=False,pending=['root independent final saved-controller BFS'],fixed_edges_verified=True,external_degree_two_verified=True))
save('terminal.json',term);save('run.json',term)
print(json.dumps(term))
