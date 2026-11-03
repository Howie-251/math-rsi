import json
from pathlib import Path
import resource
import subprocess
import time
P=Path(__file__).resolve().parent;start=time.process_time();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
profile=json.loads((P.parent/'SOURCE_PROFILE.json').read_text());pins=profile['free_vertices'];assert len(pins)==810
(P/'eligible.txt').write_text(''.join(str(v)+'\n' for v in pins))
compile=subprocess.run(['g++','-O3','-std=c++17',str(P/'cover.cpp'),'-o',str(P/'cover')],capture_output=True,text=True)
(P/'compile.log').write_text(compile.stdout+compile.stderr);compile.check_returncode();ccpu=cpu()
run=subprocess.run([str(P/'cover'),'build',str(P.parent/'source102060.author.adjlist.txt'),str(P),str(max(.01,2.95-ccpu))],capture_output=True,text=True)
(P/'build.log').write_text(run.stdout+run.stderr);run.check_returncode();r=json.loads((P/'NATIVE_PREFLIGHT.json').read_text())
r.update(compile_and_driver_before_native_CPU_seconds=ccpu,total_phase1_parent_children_CPU_seconds=cpu(),eligible_labels=pins,source_file='../source102060.author.adjlist.txt',radius4_file='radius4.u64le.bin',target_rows_file='target_rows.u64le.bin',target_support_file='target_support.u16le.bin',binary_schema='Native littleendian; R4file810rows×1595uint64, targetfile102060rows×13uint64, support102060uint16; bitindex is vertexID or eligiblecolumn index respectively.')
(P/'PREFLIGHT.json').write_text(json.dumps(r,indent=2)+'\n')
(P/'BUDGET.json').write_text(json.dumps(dict(total_budget_CPU_seconds=10,phase1_CPU_seconds=r['total_phase1_parent_children_CPU_seconds'],remaining_CPU_seconds=max(0,10-r['total_phase1_parent_children_CPU_seconds'])),indent=2)+'\n')
print(run.stdout,end='');print('phase1_total_CPU',r['total_phase1_parent_children_CPU_seconds'])
