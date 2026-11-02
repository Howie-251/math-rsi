import datetime
import json
import pathlib
import resource
import subprocess
import time

D = pathlib.Path(__file__).resolve().parent
def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime
start = cpu()
wall = time.monotonic()
(D / 'checkpoint.json').write_text(json.dumps({'status':'COMPILING', 'native_CPU_limit':3, 'time_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}, indent=2)+'\n')
subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')], check=True)
compiled = cpu()
(D / 'checkpoint.json').write_text(json.dumps({'status':'NATIVE_RUNNING', 'compile_CPU_seconds':compiled-start, 'native_CPU_limit':3}, indent=2)+'\n')
r = subprocess.run([str(D/'probe'),str(D)], text=True, capture_output=True)
(D/'native.log').write_text(r.stdout+r.stderr)
if r.returncode:
    result = {'status':'UNKNOWN_NATIVE_PROCESS_EXIT','returncode':r.returncode,'full_hits':0}
else:
    result = json.loads((D/'NATIVE_RESULT.json').read_text())
result['compile_CPU_seconds'] = compiled-start
result['total_parent_children_CPU_seconds'] = cpu()-start
result['wall_seconds'] = time.monotonic()-wall
result['source9720_all_roots_BFS_repeated'] = 0
result['ordinary_bad_unordered_pairs'] = None
(D/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps({'status':result['status'],'result':'RESULT.json','full_hits':result['full_hits']}, indent=2)+'\n')
(D/'terminal.json').write_text(json.dumps({'status':result['status'],'pending':[],'time_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}, indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','coarse_frames_checked','actual_models_checked','full_hits','native_CPU_seconds','total_parent_children_CPU_seconds'] if k in result}))
