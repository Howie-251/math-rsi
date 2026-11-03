from pathlib import Path
from collections import deque
import json,os,resource,shutil,subprocess,time
P=Path(__file__).resolve().parent
assert not (P/'terminal.json').exists(), 'Do not restart a completed input scope.'
started=time.process_time();wall=time.monotonic()
def cpu():
 return time.process_time()-started+resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime+resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime
source=P.parent/'sources/bhakar104.edges'
shutil.copyfile(source,P/'source.edges')
data=[tuple(map(int,s.split())) for s in source.read_text().splitlines() if s.strip()]
assert data[0]==(104,208)
edges=data[1:]
first=next((i,j) for i in range(208) for j in range(i+1,208) if len(set(edges[i]+edges[j]))==4)
adj=[set() for _ in range(105)]
for k,(u,v) in enumerate(edges):
 if k not in first:adj[u].add(v);adj[v].add(u)
for x in edges[first[0]]+edges[first[1]]:adj[104].add(x);adj[x].add(104)
assert all(len(x)==4 for x in adj)
missing=[]
for r in range(105):
 d=[-1]*105;d[r]=0;q=deque([r])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 missing.append(sum(x<0 or x>4 for x in d))
(P/'first_expected.txt').write_text(' '.join(map(str,missing))+'\n')
(P/'first_calibration.json').write_text(json.dumps(dict(n=105,roots=105,deleted_edge_ids=first,bad_unordered_pairs=sum(missing)//2,method='ordinary independent Python BFS on the first formally selected insertion graph; C++ compares every root and reuses that score'),indent=2)+'\n')
scope='Fixed public104c source; replace each unordered pair of vertex-disjoint source edges by four spokes to one new vertex104. No other edge changes. All candidates simple4regular on105 vertices; target diameter4.'
(P/'inputs.json').write_text(json.dumps(dict(source=str(source),scope=scope,planned_raw_pairs=21528,planned_legal_candidates=20904,CPU_budget=30,workers=1),indent=2)+'\n')
subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=P,check=True)
(P/'run.json').write_text(json.dumps(dict(status='RUNNING',running=True,driver_pid=os.getpid(),scope=scope,CPU_budget=30),indent=2)+'\n')
worker=subprocess.Popen(['./search'],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
r=json.loads((P/'run.json').read_text());r['worker_pid']=worker.pid;(P/'run.json').write_text(json.dumps(r,indent=2)+'\n')
output,_=worker.communicate(timeout=30)
(P/'production.log').write_text(output);assert worker.returncode==0,output
terminal=json.loads((P/'production.json').read_text())
if not terminal['found_D4']:
 assert terminal['raw_pairs']==21528 and terminal['legal_candidates_scored']==20904 and terminal['overlapping_pairs']==624
terminal.update(total_measured_CPU_seconds=cpu(),wall_seconds=time.monotonic()-wall,scope=scope,entire_extension_family_exhausted=False,pending=['root independent saved-best graph check'])
(P/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
(P/'run.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal))
