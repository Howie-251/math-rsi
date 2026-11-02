import time
START=time.process_time()
from pathlib import Path
import json,subprocess,resource
HERE=Path(__file__).resolve().parent
PRIOR=.812939922+.25

def save(n,o):(HERE/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one source252 family already attempted')
save('ATTEMPT.json',{'status':'STARTED','prior_read_prep':PRIOR,'casecap':10})
edges=[tuple(map(int,l.split()))for l in(HERE/'SOURCE252_RAW.edges').read_text().splitlines()if l.strip()]
assert len(edges)==len(set(tuple(sorted(x))for x in edges))==630
assert all(0<=a<252 and 0<=b<252 and a!=b for a,b in edges)
deg=[0]*252
for a,b in edges:deg[a]+=1;deg[b]+=1
assert set(deg)=={5}
with(HERE/'SOURCE_CANONICAL.edges').open('w')as f:
 f.write('252 630 5\n')
 for a,b in sorted(tuple(sorted(x))for x in edges):f.write(f'{a} {b}\n')
save('SOURCE_BINDING.json',{'n':252,'m':630,'maxdegree':5,'degreehist':{'5':252},'primaryraw':'SOURCE252_RAW.edges/noheader','new_source_literal_parse':1,'source_D4':'inherited primaryandoldvalidatedcache; no newD4BFS'})
c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with(HERE/'COMPILE.log').open('w')as f:c=subprocess.run(['g++','-O3','-std=c++17','run.cpp','-o','run'],cwd=HERE,stdout=f,stderr=subprocess.STDOUT)
c1=resource.getrusage(resource.RUSAGE_CHILDREN);assert c.returncode==0
compilecpu=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime
def limit():resource.setrlimit(resource.RLIMIT_CPU,(8,8))
with(HERE/'RUN.log').open('w')as f:
 p=subprocess.Popen([str(HERE/'run')],cwd=HERE,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limit)
 save('HANDLE.json',{'PID':p.pid,'status':'RUNNING_ONE_FIXED_SOURCE_ALL_TWOCUTS','compile_CPU':compilecpu,'prior_read_prep':PRIOR})
 code=p.wait()
c2=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=c2.ru_utime+c2.ru_stime-c1.ru_utime-c1.ru_stime
nat=json.loads((HERE/'NATIVE_RESULT.json').read_text())if(HERE/'NATIVE_RESULT.json').exists()else{'status':'UNKNOWN_NATIVE_EXIT','returncode':code}
r={'status':nat['status'],'native':nat,'compile_CPU':compilecpu,'native_child_CPU':cpu,'driver_CPU':time.process_time()-START,'prior_read_prep_CPU':PRIOR,'case_CPU':PRIOR+compilecpu+cpu+time.process_time()-START,'casecap':10,'target':[5,4,253],'source_graph_D4_revalidation_Lean_ARIS_solver':0,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'one actualRajiv252source;alltwo vertex-disjointsourceedgecuts +new4star, nootheredits; notgeneral5D4','next':'fresh/latestpublic/Lean/reviews ifhit; otherwiseSTOP_NOCUT_ORSEED_LADDER','terminal':True}
save('RESULT.json',r);save('TERMINAL.json',r)
print(json.dumps(r,ensure_ascii=False),flush=True)
