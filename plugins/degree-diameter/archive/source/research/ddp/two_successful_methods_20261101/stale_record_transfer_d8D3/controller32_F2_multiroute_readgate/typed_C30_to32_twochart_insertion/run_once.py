import time
START=time.process_time()
from pathlib import Path
from collections import deque
import subprocess,json,resource,os
HERE=Path(__file__).resolve().parent
PRIOR=3.223515283

def save(n,o):(HERE/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one-shot generator attempted')
save('ATTEMPT.json',{'status':'STARTED','prior_prep_CPU':PRIOR,'case_cap':30})
old=json.loads((HERE.parent/'EXISTING_C30_BINARY_CHART_INPUT.json').read_text())
C=old['typed_controller']['controller']
(HERE/'INPUT_CONTROLLER.txt').write_text('\n'.join(' '.join(map(str,row))for row in C)+'\n')
r0=resource.getrusage(resource.RUSAGE_CHILDREN)
with(HERE/'COMPILE.log').open('w')as f:
 c=subprocess.run(['g++','-O3','-std=c++17','run.cpp','-o','run'],cwd=HERE,stdout=f,stderr=subprocess.STDOUT)
r1=resource.getrusage(resource.RUSAGE_CHILDREN)
compilecpu=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime
if c.returncode:save('RESULT.json',{'status':'UNKNOWN_COMPILE_FAIL','code':c.returncode,'compile_CPU':compilecpu});raise RuntimeError('compile fail')
def limit():resource.setrlimit(resource.RLIMIT_CPU,(24,24))
with(HERE/'NATIVE.log').open('w')as f:
 p=subprocess.Popen([str(HERE/'run')],cwd=HERE,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limit)
 save('HANDLE.json',{'PID':p.pid,'status':'RUNNING','native_cap20CPU':True,'prior':PRIOR,'compile_CPU':compilecpu})
 ret=p.wait()
r2=resource.getrusage(resource.RUSAGE_CHILDREN)
nativechild=r2.ru_utime+r2.ru_stime-r1.ru_utime-r1.ru_stime
nat=json.loads((HERE/'NATIVE_RESULT.json').read_text())if(HERE/'NATIVE_RESULT.json').exists()else {'status':'UNKNOWN_NATIVE_TERMINATED_WITHOUT_RESULT','returncode':ret}
producer=False;roots=0
maps=[[[2,1,4],[2,1,4],[1,2,7],[1,2,7]],[[2,1,4],[2,1,4],[2,1,7],[2,1,7]]];V=[1,2,4,7]
def app(c,x):return(c[0]if x&1 else 0)^(c[1]if x&2 else 0)^(c[2]if x&4 else 0)
if nat.get('hit'):
 cc=[list(map(int,row.split()))for row in(HERE/'HIT_CONTROLLER.txt').read_text().splitlines()]
 m=maps[nat['hit_chart']];edges=set()
 for u in range(32):
  for x in range(8):
   for port in range(4):
    for lam in [0,1]:
     v=8*cc[u][port]+(app(m[port],x)^(V[port]if lam else 0));a=8*u+x
     assert a!=v;edges.add(tuple(sorted((a,v))))
 assert len(edges)==1024
 with(HERE/'candidate_d8_D3_n256.edges').open('w')as f:
  f.write('256 1024\n')
  for u,v in sorted(edges):f.write(f'{u} {v}\n')
 adj=[[]for _ in range(256)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 assert all(len(set(z))==len(z)==8 for z in adj)
 producer=True
 for root in range(256):
  d=[-1]*256;d[root]=0;q=deque([root])
  while q:
   u=q.popleft()
   for v in adj[u]:
    if d[v]<0:d[v]=d[u]+1;q.append(v)
  roots+=1
  if -1 in d or max(d)>3:producer=False;break
 save('PARAMETERS.json',{'n':256,'m':1024,'degree':8,'controller':cc,'maps_columncodes':m,'stepoffsets':V,'bar':[1,0,3,2],'tails':nat['hit_tails'],'producer_roots':roots,'producer_D3':producer,'fresh_Lean_ARIS':'PENDING'if producer else 'NOT_TRIGGERED'})
status='CANDIDATE256_PRODUCER_PASS_PENDING_FRESH'if producer else nat['status']
result={'status':status,'native':nat,'compile_CPU':compilecpu,'native_child_CPU':nativechild,'driver_CPU':time.process_time()-START,'prior_read_prep_CPU':PRIOR,'case_CPU':PRIOR+compilecpu+nativechild+time.process_time()-START,'case_cap':30,'producer_roots':roots,'producer_pass':producer,'graph_generated':nat.get('hit',False),'source_oldBFS_Lean_ARIS_solver':0,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'two fixedARC/R charts; one typedC30 insertionfamily,378450raw controls and simple4neighbor filter; not generalC32/binarylifts/8D3','terminal':True,'next':'STOP_NO_OTHERCHART_ORFAMILY_TIMER_AUTOMATIC'}
save('RESULT.json',result);save('TERMINAL.json',result)
print(json.dumps(result,ensure_ascii=False),flush=True)
