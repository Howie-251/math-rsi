from pathlib import Path
import json,subprocess,time,resource
P=Path(__file__).resolve().parent
assert not(P/'RESULT.json').exists()
start=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
assert json.loads((P/'PREDICTION.json').read_text())['status']=='FROZEN_BEFORE_SINGLE_MATCHING_EDGE_DELETION_TESTS'
subprocess.run(['g++','-O3','-std=c++17',str(P/'probe.cpp'),'-o',str(P/'probe')],check=True)
compiled=cpu()
with(P/'probe.log').open('w')as log:
 subprocess.run([str(P/'probe'),str(P.parent/'source972.edges'),str(P)],check=True,stdout=log,stderr=log,timeout=10)
r=json.loads((P/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compiled,total_batch_CPU_seconds=cpu(),
 prediction='SUPPORTED' if r['safe_edges'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED',
 actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,
 pending=['One safe-cut selection and one newH exactcover, at most5CPU']if r['safe_edges'] else [])
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
