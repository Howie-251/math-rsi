import json
import pathlib
import resource
import subprocess
import time

HERE=pathlib.Path(__file__).resolve().parent
start=time.process_time()
zero=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-zero.ru_utime-zero.ru_stime
assert not (HERE/'CANDIDATE_RESULT.json').exists()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'candidate.cpp'),'-o',str(HERE/'candidate')],check=True)
compiled=cpu()
subprocess.run([str(HERE/'candidate'),str(HERE)],check=True,timeout=8)
r=json.loads((HERE/'CANDIDATE_RESULT.json').read_text())
r['compile_CPU_seconds']=compiled
r['total_candidate_batch_CPU_seconds']=cpu()
r['pending']=['Root independent acceptance'] if r['full_D9'] else []
(HERE/'CANDIDATE_RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
