import json
from pathlib import Path
import resource
import subprocess
import time
P=Path(__file__).resolve().parent;start=time.process_time();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
c=subprocess.run(['g++','-O3','-std=c++17',str(P/'probe.cpp'),'-o',str(P/'probe')],capture_output=True,text=True)
(P/'compile.log').write_text(c.stdout+c.stderr);c.check_returncode();compile_cpu=cpu()
run=subprocess.run([str(P/'probe'),str(P),'5'],capture_output=True,text=True)
(P/'run.log').write_text(run.stdout+run.stderr);run.check_returncode()
r=json.loads((P/'NATIVE_RESULT.json').read_text())
r.update(target_Delta=16,target_D=4,savedL=16384,source_n=9720,new_central_order=9,source9720_BFS_repeated=0,ordinary_bad_unordered_pairs=None,compile_and_driver_before_native_CPU_seconds=compile_cpu,total_parent_children_CPU_seconds=cpu())
for case in r['cases']:
    extra=case['extra_plain_power'];f=P/f'power{extra}_missing_states.json'
    if f.exists():
        miss=json.loads(f.read_text());by={}
        for vertex in miss['missing_vertex_ids']:by.setdefault(vertex//81,[]).append(vertex%81)
        miss['missing_by_controller']=[dict(controller=g,SL2_index=g//9,central=g%9,missing_count=len(xs),missing_fiber_ids=xs) for g,xs in sorted(by.items())]
        f.write_text(json.dumps(miss,indent=2)+'\n')
        case['missing_receipt']=f.name
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps(dict(status=r['status'],running=False,pending=[],native_CPU_seconds=r['native_CPU_seconds'],source9720_BFS_repeated=0),indent=2)+'\n')
print(run.stdout,end='');print('native_CPU',r['native_CPU_seconds'],'compile_CPU',compile_cpu,'total_CPU',r['total_parent_children_CPU_seconds'])
