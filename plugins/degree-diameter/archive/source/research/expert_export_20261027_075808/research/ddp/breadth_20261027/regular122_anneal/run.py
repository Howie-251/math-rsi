from pathlib import Path
from collections import deque
import json,os,resource,subprocess,time
out=Path(__file__).resolve().parent
assert not (out/'run.json').exists(), 'One bounded profile; no automatic restart.'
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
beg=cpu();wall=time.monotonic()
with (out/'compile.log').open('w') as f:subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=out,stdout=f,stderr=subprocess.STDOUT,check=True)
prep=cpu()-beg;limit=90-prep-2
assert limit>0
meta={'n':122,'degree':6,'target_D':3,'saved_baseline':120,'starts':8,'proposals_per_start':250000,'seeds':[20261027180+i for i in range(8)],'initialization':'fresh 6regular circulant +/-1,+/-2,+/-3, independently mixed by 10000 legal random two-edge switches; no uniform-distribution claim','method':'unrestricted degree-preserving two-edge Metropolis annealing; five 50000-proposal cooling epochs from temperature8 to0.1 per start','score':'exact all122-root radius3 bitset union; no orbit symmetry','budget_CPU_seconds':90,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':limit,'worker_count':1,'first_calibration':'one formal start independently ordinary-BFS all122 roots; score reused'}
(out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
with (out/'production.log').open('w') as log:
 p=subprocess.Popen([str(out/'search'),str(out),str(limit)],cwd=out,stdout=log,stderr=subprocess.STDOUT)
 run={'status':'RUNNING','running':True,'pid':p.pid,'driver_pid':os.getpid(),'CPU_budget_seconds':90,'worker_count':1}
 (out/'run.json').write_text(json.dumps(run,indent=2)+'\n')
 ready=out/'first.expected.json'
 while not ready.exists():
  assert p.poll() is None,'producer exited before formal candidate'
  time.sleep(.01)
 # Wait for the producer's short writes to finish before parsing.
 while True:
  try:expected=json.loads(ready.read_text());break
  except json.JSONDecodeError:time.sleep(.01)
 lines=(out/'first.edges').read_text().splitlines();n,m=map(int,lines[0].split());assert(n,m)==(122,366)
 adj=[set() for _ in range(n)];seen=set()
 for line in lines[1:]:
  u,v=map(int,line.split());assert 0<=u<v<n and (u,v) not in seen;seen.add((u,v));adj[u].add(v);adj[v].add(u)
 assert len(seen)==m and all(len(a)==6 for a in adj)
 deficits=[]
 for root in range(n):
  dist=[-1]*n;dist[root]=0;q=deque([root])
  while q:
   u=q.popleft()
   for v in adj[u]:
    if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
  deficits.append(sum(x<0 or x>3 for x in dist))
 assert deficits==expected['radius3_deficits']
 assert sum(deficits)//2==expected['bad_pairs']
 (out/'first.independent_calibration.json').write_text(json.dumps({'matches':True,'roots_checked':122,'ordinary_BFS_radius3_deficits':deficits,'bad_pairs':sum(deficits)//2,'formal_score_reused':True},indent=2)+'\n')
 (out/'first.calibrated').write_text('ok\n')
 code=p.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-beg,wall_seconds=time.monotonic()-wall)
run['status']=json.loads((out/'terminal.json').read_text())['status'] if code==0 else 'PROCESS_ERROR'
(out/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
