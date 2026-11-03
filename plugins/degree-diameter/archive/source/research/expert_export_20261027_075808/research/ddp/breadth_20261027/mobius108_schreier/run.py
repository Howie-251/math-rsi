from pathlib import Path
from collections import deque
import json,os,resource,subprocess,time
out=Path(__file__).resolve().parent
assert not (out/'run.json').exists(), 'One finite profile; no automatic restart.'
(out/'improvements').mkdir(exist_ok=True)
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
beg=cpu();wall=time.monotonic()
with (out/'compile.log').open('w') as f:subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=out,stdout=f,stderr=subprocess.STDOUT,check=True)
prep=cpu()-beg;limit=60-prep-2;assert limit>0
meta={'n':108,'field_prime':107,'infinity_label':107,'maximum_degree':4,'target_D':4,'saved_baseline':104,'planned_matrix_pairs':30000,'seed':20261027190,'method':'independent invertible2x2 matrices overF107, normalized by first nonzero entry; undirected edges x--A(x),x--B(x), dropping loops and merging repeated edges','sampling':'all invertible matrix pairs formal, including equal/inverse/identity transformations and disconnected graphs; singular raw matrix draws counted separately','no_graph_symmetry_assumed':True,'score':'all108-root exact radius4 via unions of radius2 balls','budget_CPU_seconds':60,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':limit,'worker_count':1}
(out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
with (out/'production.log').open('w') as log:
 p=subprocess.Popen([str(out/'search'),str(out),str(limit)],cwd=out,stdout=log,stderr=subprocess.STDOUT)
 run={'status':'RUNNING','running':True,'pid':p.pid,'driver_pid':os.getpid(),'worker_count':1,'CPU_budget_seconds':60};(out/'run.json').write_text(json.dumps(run,indent=2)+'\n')
 ready=out/'first.expected.json'
 while not ready.exists():
  assert p.poll() is None,'producer exited before formal candidate'
  time.sleep(.01)
 while True:
  try:expected=json.loads(ready.read_text());break
  except json.JSONDecodeError:time.sleep(.01)
 def act(m,x):
  a,b,c,d=m
  if x==107:return a*pow(c,105,107)%107 if c else 107
  den=(c*x+d)%107
  return (a*x+b)*pow(den,105,107)%107 if den else 107
 adj=[set() for _ in range(108)];edges=set()
 for m in [expected['matrix_A'],expected['matrix_B']]:
  a,b,c,d=m;assert (a*d-b*c)%107
  image=[act(m,x) for x in range(108)];assert len(set(image))==108
  for x,y in enumerate(image):
   if x!=y:edges.add(tuple(sorted((x,y))));adj[x].add(y);adj[y].add(x)
 assert max(map(len,adj))<=4
 lines=(out/'first.edges').read_text().splitlines();n,count=map(int,lines[0].split());assert n==108
 saved={tuple(map(int,line.split())) for line in lines[1:]};assert saved==edges and count==len(edges)
 deficits=[];component0=None
 for root in range(108):
  dist=[-1]*108;dist[root]=0;q=deque([root])
  while q:
   u=q.popleft()
   for v in adj[u]:
    if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
  deficits.append(sum(x<0 or x>4 for x in dist))
  if root==0:component0=sum(x>=0 for x in dist)
 assert deficits==expected['radius4_deficits'] and sum(deficits)//2==expected['bad_pairs'] and component0==expected['component0_size']
 (out/'first.independent_calibration.json').write_text(json.dumps({'matches':True,'direct_formula_edge_set_matches':True,'roots_checked':108,'radius4_deficits':deficits,'bad_pairs':sum(deficits)//2,'component0_size':component0,'formal_score_reused':True},indent=2)+'\n')
 (out/'first.calibrated').write_text('ok\n');code=p.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-beg,wall_seconds=time.monotonic()-wall)
run['status']=json.loads((out/'terminal.json').read_text())['status'] if code==0 else 'PROCESS_ERROR'
(out/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run,indent=2))
