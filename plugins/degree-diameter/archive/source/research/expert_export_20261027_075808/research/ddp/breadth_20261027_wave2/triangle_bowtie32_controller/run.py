from pathlib import Path
from collections import deque
import json,random,resource,subprocess,time,sys,os

OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3]
T=time.process_time();CH=resource.getrusage(resource.RUSAGE_CHILDREN);W=time.monotonic()
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np

N=32;M=64;EXT=31
def used():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-T+r.ru_utime+r.ru_stime-CH.ru_utime-CH.ru_stime
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2)+'\n')
triangles=[[0,1,2],[0,3,4]]+[list(range(s,s+3)) for s in range(5,32,3)]
assert len(triangles)==11
fixed=sorted(tuple(sorted((t[a],t[b]))) for t in triangles for a in range(3) for b in range(a+1,3))
fixedset=set(fixed);assert len(fixed)==len(fixedset)==33
fixeddegree=[0]*N
for u,v in fixed:fixeddegree[u]+=1;fixeddegree[v]+=1
assert fixeddegree==[4]+[2]*31
starts=[];draws=[]
for i in range(8):
 rng=random.Random(20261027560+i);draw=0
 while True:
  order=list(range(1,32));rng.shuffle(order);draw+=1
  es=sorted(tuple(sorted((order[j],order[(j+1)%EXT]))) for j in range(EXT))
  if all(e not in fixedset for e in es):break
 assert len(set(es))==EXT and all(u>0 and v>0 for u,v in es)
 starts.append(es);draws.append(draw)
save('inputs.json',dict(n=N,degree=4,target_D=3,fixed_triangles=triangles,fixed_edges=fixed,fixed_degree=fixeddegree,external_degree=[0]+[2]*31,external_edges_per_start=starts,start_seeds=list(range(20261027560,20261027568)),start_rejection_draws=draws,mutation_seed=20261027568,proposals_per_start=100000,objective='L=sum over all ordered pairs max(0,27-(I+3A+9A^2+27A^3)[u,v])',target_is_only_a_necessary_controller_condition=True,CPU_budget_seconds=45,workers=1,OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1,extra_triangles_allowed=True,old_scope_difference='Fixed overlap of prescribed triangles changes from disjoint33 to one shared vertex at32; no old31 source, no changed old SAT, no further skeleton queue.'))
text=[f'{N} 8 {EXT} {len(fixed)}']+[f'{u} {v}' for u,v in fixed]
for es in starts:text.extend(f'{u} {v}' for u,v in es)
(OUT/'inputs.txt').write_text('\n'.join(text)+'\n')
with (OUT/'compile.log').open('w') as log:subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=OUT,stdout=log,stderr=log,check=True)
subprocess.run(['./search','calibrate'],cwd=OUT,check=True)
def read_edges(name):
 rows=[tuple(map(int,s.split())) for s in (OUT/name).read_text().splitlines()];assert rows[0]==(N,M);return rows[1:]
def matrix(es):
 a=np.zeros((N,N),dtype=np.int64)
 for u,v in es:a[u,v]=a[v,u]=1
 assert int(a.sum())==2*M and np.all(a.sum(axis=1)==4)
 return a
first=read_edges('first.edges');a=matrix(first);a2=a@a;a3=a2@a;upper=np.eye(N,dtype=np.int64)+3*a+9*a2+27*a3
cpp=np.loadtxt(OUT/'first.capacity.txt',dtype=np.int64);assert np.array_equal(cpp,upper)
expected=json.loads((OUT/'first.score.json').read_text());lack=int(np.maximum(0,27-upper).sum());slots=int((upper<27).sum());assert expected['lack']==lack and expected['slots']==slots
adj=[[] for _ in range(N)]
for u,v in first:adj[u].append(v);adj[v].append(u)
bad=0;diam=0
for r in range(N):
 dist=[-1]*N;dist[r]=0;q=deque([r])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
 bad+=sum(x<0 or x>3 for x in dist);diam=max(diam,max(dist))
assert bad%2==0 and bad//2==expected['bad']
save('first_calibration.json',dict(n=N,edges=M,degree=4,independent_integer_numpy_A2_A3=True,all_capacity_entries_match=True,ordered_slots_checked=N*N,capacity_deficit_ordered=lack,insufficient_ordered_slots=slots,ordinary_BFS_roots=N,ordinary_diameter=diam,bad_unordered_pairs_gt3=bad//2,first_score_reused=True,CPU_used_before_production_seconds=used()))
(OUT/'first.cached.txt').write_text(f'{lack} {slots} {bad//2}\n')
remaining=max(0.,45.-used()-.5)
save('run.json',dict(status='RUNNING_PRODUCTION',running=True,remaining_production_CPU_seconds=remaining,CPU_used_before_production_seconds=used()))
with (OUT/'production.log').open('w') as log:
 proc=subprocess.Popen(['./search','search',str(remaining)],cwd=OUT,stdout=log,stderr=log);save('process.json',dict(pid=proc.pid,driver_pid=os.getpid()));assert proc.wait()==0
term=json.loads((OUT/'production_terminal.json').read_text());best=json.loads((OUT/'best.json').read_text());es=read_edges('best.edges');a=matrix(es)
assert len(set(es))==M and fixedset<=set(es)
external=set(es)-fixedset;assert len(external)==EXT and all(u>0 and v>0 for u,v in external)
externaldegree=[0]*N
for u,v in external:externaldegree[u]+=1;externaldegree[v]+=1
assert externaldegree==[0]+[2]*31
a2=a@a;a3=a2@a;upper=np.eye(N,dtype=np.int64)+3*a+9*a2+27*a3
assert int(np.maximum(0,27-upper).sum())==best['capacity_deficit_ordered']
save('best.capacity.json',dict(formula='I+3A+9A^2+27A^3',minimum_upper_bound=int(upper.min()),deficit_ordered=int(np.maximum(0,27-upper).sum()),insufficient_ordered_slots=int((upper<27).sum()),exact_three_step_missing_ordered=int((a3==0).sum()),triangles=int(np.trace(a3))//6,upper=upper.tolist(),insufficient_slots=[dict(u=int(u),v=int(v),capacity_upper=int(upper[u,v])) for u,v in zip(*np.where(upper<27))],actual_fiber_lift_generated=False,only_a_necessary_condition=True))
term.update(dict(total_measured_CPU_seconds=used(),total_wall_seconds=time.monotonic()-W,preparation_and_calibration_CPU_seconds=json.loads((OUT/'first_calibration.json').read_text())['CPU_used_before_production_seconds'],CPU_budget_seconds=45,workers=1,OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1,restarts=0,only_partial_controller=True,fiber_lift_generated=False,pending=['root independent final saved-controller BFS'],fixed_edges_verified=True,external_degree_verified=True))
save('terminal.json',term);save('run.json',term)
print(json.dumps(term))
