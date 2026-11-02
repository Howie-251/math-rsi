import json
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PARENT = HERE.parent
start = time.process_time()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
rows = [json.loads(s) for s in (PARENT/'EDGE_CRITICAL_MATCHINGS.jsonl').read_text().splitlines()]
assert len(rows) == 3250
assert all(not(set(r['L']) & set(r['R'])) for r in rows if r['type']=='FF' and r['maximum_matching'] < 9)
with (HERE/'cached_edge_critical_input.txt').open('w') as f:
    f.write(str(len(rows))+'\n')
    for r in rows:
        f.write(' '.join(map(str,[*r['edge'],r['maximum_matching'],*r['L'],*r['R'],*r['critical_row_masks'],{'FF':0,'FP':1,'PP':2}[r['type']]]))+'\n')
compile_result = subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],capture_output=True,text=True)
(HERE/'compile.log').write_text(compile_result.stdout+compile_result.stderr)
assert compile_result.returncode==0
compiled = resource.getrusage(resource.RUSAGE_CHILDREN)
source = ROOT/'research/ddp/more_graphs_20261027/d3d4_transfer/source650.implicit_adj.txt'
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_NATIVE','source':str(source),'hard_native_CPU_seconds':10,'parent_A2_reused':str(PARENT/'A2.u16le.bin')},indent=2)+'\n')
run = subprocess.run([str(HERE/'search'),str(source),str(HERE/'cached_edge_critical_input.txt'),str(PARENT/'A2.u16le.bin'),str(HERE)],capture_output=True,text=True)
(HERE/'run.log').write_text(run.stdout+run.stderr)
after = resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu(r):return r.ru_utime+r.ru_stime
receipt={'exit_code':run.returncode,'compile_CPU_seconds':cpu(compiled)-cpu(before),'native_process_CPU_seconds':cpu(after)-cpu(compiled),'driver_CPU_seconds':time.process_time()-start}
if run.returncode==0:
    result=json.loads((HERE/'NATIVE_RESULT.json').read_text())
    result['receipt']=receipt
else:
    result={'status':'UNKNOWN_CPU_OR_EXECUTION_ERROR','receipt':receipt,'actual_D':None,'ordinary_unordered_bad_pairs':None}
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':result['status'],**receipt},indent=2)+'\n')
print(json.dumps(result,indent=2))
