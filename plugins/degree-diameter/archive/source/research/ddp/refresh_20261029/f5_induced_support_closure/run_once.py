import json
from pathlib import Path
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3]
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN)
assert not (OUT/'RESULT.json').exists()
pred=json.loads((OUT/'PREDICTION.json').read_text())
words=json.loads((ROOT/pred['input']).read_text());assert len(words)==258
(OUT/'RULES.txt').write_text('\n'.join(' '.join(map(str,w['vertices'])) for w in words)+'\n')
def children():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
p=subprocess.run(['g++','-std=c++17','-O2',str(OUT/'check.cpp'),'-o',str(OUT/'check')],capture_output=True,text=True)
assert p.returncode==0,p.stderr
compile_cpu=children();remaining=5-compile_cpu-(time.process_time()-start)-.1
assert remaining>0
with (OUT/'native.log').open('w') as log:p=subprocess.run([str(OUT/'check'),str(OUT/'RULES.txt'),str(OUT),str(remaining)],stdout=log,stderr=log,timeout=15)
assert p.returncode==0
d=json.loads((OUT/'NATIVE_RESULT.json').read_text())
mask=d['largest_proper_mask'];Q=[i for i in range(30) if mask>>i&1]
violated=[]
for index,word in enumerate(words):
 u,a,b,v=word['vertices']
 if u in Q and v in Q and (a not in Q or b not in Q):violated.append(index)
assert not violated and len(Q)<30
counter=len(Q)>=16
status='H_REFUTED_EXACT_MAXIMUM' if counter and d['complete'] else 'H_REFUTED_LITERAL_COUNTEREXAMPLE' if counter else 'H_SUPPORTED_COMPLETE_CLOSURE_ENUMERATION' if d['complete'] else 'PARTIAL_NO_DECISION'
result=dict(d,status=status,running=False,prediction_H='REFUTED' if counter else 'SUPPORTED' if d['complete'] else 'UNRESOLVED',maximum_is_exact=d['complete'],literal_largest_proper_support=Q,missing_fibers=[i for i in range(30) if i not in Q],all258_direct_checks_pass=True,violated_rule_indices=violated,compile_CPU_seconds=compile_cpu,aggregate_CPU_seconds=children()+time.process_time()-start,CPU_budget_seconds=5,source_graph_reads=0,graph_BFS=0,SAT_calls=0,new_graphs=0,pending=[])
assert result['aggregate_CPU_seconds']<5
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
