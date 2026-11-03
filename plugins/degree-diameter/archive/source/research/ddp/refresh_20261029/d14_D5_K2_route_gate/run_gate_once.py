#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
start=time.process_time()
initial=resource.getrusage(resource.RUSAGE_CHILDREN)
pred=json.loads((OUT/'PREDICTION.json').read_text())
assert not (OUT/'RESULT.json').exists()
meta=json.loads((ROOT/pred['free_order_metadata']).read_text())
free=meta['free_vertices']
assert meta['complete'] and len(free)==3685 and meta['source_n']==94186 and meta['source_m']==657452
assert meta['words_per_row']==1472 and free==sorted(set(free))
(OUT/'FREE_ORDER.txt').write_text('\n'.join(map(str,free))+'\n')
def childcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
compile_start=childcpu()
p=subprocess.run(['g++','-std=c++17','-O2',str(OUT/'gate.cpp'),'-o',str(OUT/'gate')],capture_output=True,text=True)
assert p.returncode==0,p.stderr
compile_cpu=childcpu()-compile_start
remaining=10-compile_cpu-(time.process_time()-start)-.2
assert remaining>0
with (OUT/'native.log').open('w') as log:
    p=subprocess.run([str(OUT/'gate'),str(ROOT/pred['source_graph']),str(ROOT/pred['old_R4_cache']),str(OUT/'FREE_ORDER.txt'),str(OUT),str(remaining)],stdout=log,stderr=log,timeout=30)
assert p.returncode==0,p.returncode
r=json.loads((OUT/'NATIVE_RESULT.json').read_text())
total=childcpu()+time.process_time()-start
r.update(running=False,compile_CPU_seconds=compile_cpu,driver_CPU_seconds=time.process_time()-start,aggregate_CPU_seconds=total,CPU_budget_seconds=10,workers=1,source_graph=pred['source_graph'],old_R4_cache=pred['old_R4_cache'],new_R3_cache='allfree_R3.u64le.bin',K2_constructed=False,pending=[])
assert total<10
(OUT/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(OUT/'TERMINAL.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)
