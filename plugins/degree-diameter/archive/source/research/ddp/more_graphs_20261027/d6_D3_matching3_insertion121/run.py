import json
import pathlib
import resource
import subprocess
import time

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'context/DD_PORTFOLIO_START_20261026/baselines/d6_D3_known.edges'
start=time.process_time()
c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
assert not (HERE/'RESULT.json').exists()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'probe.cpp'),'-o',str(HERE/'probe')],check=True)
compile_cpu=cpu()
with (HERE/'probe.log').open('w') as log:
    subprocess.run([str(HERE/'probe'),str(SOURCE),str(HERE),str(min(18.5,19.5-cpu()))],
                   stdout=log,stderr=log,check=True,timeout=35)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r['compile_CPU_seconds']=compile_cpu
r['total_batch_CPU_seconds']=cpu()
r['status']='FIRST_COMPLETE_HIT' if r['hit'] else 'UNKNOWN_CPU_LIMIT' if r['CPU_limited'] else 'FIXED_SOURCE_OPERATION_COMPLETE_NO_HIT'
r['newroot_gate_prediction']='SUPPORTED' if r['newroot_gate_pass'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED'
r['actual_n']=121 if r['hit'] else None
r['actual_D']=3 if r['hit'] else None
r['ordinary_bad_unordered_pairs']=0 if r['hit'] else None
r['hypothetical_n']=121
r['source_validation_inherited']=str(ROOT/'context/DD_PORTFOLIO_START_20261026/validation/d6_D3_bfs.json')
r['pending']=['Root independent first newparameter acceptance'] if r['hit'] else []
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
