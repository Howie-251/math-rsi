import datetime
import json
import pathlib
import resource
import subprocess
import time

HERE=pathlib.Path(__file__).resolve().parent
start=time.process_time()
child0=resource.getrusage(resource.RUSAGE_CHILDREN)
prior=0.36
def cpu():
    x=resource.getrusage(resource.RUSAGE_CHILDREN)
    return prior+time.process_time()-start+x.ru_utime+x.ru_stime-child0.ru_utime-child0.ru_stime
mandatory=json.loads((HERE/'MANDATORY_R5.json').read_text())
assert mandatory['missing_count']==4201
(HERE/'mandatory_missing.txt').write_text(' '.join(map(str,mandatory['missing']))+'\n')
handle={'status':'COMPILING_EXACT_FIXED_PROTOTYPE','started_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'prototype':19161,'mandatory_count':9,'guard_cap':2,'budget_CPU_seconds':30}
(HERE/'PROBE_HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'exact_guard.cpp'),'-o',str(HERE/'exact_guard')],check=True)
compile_cpu=cpu()-prior
handle.update(status='RUNNING_NATIVE_EXACT_GUARDS',compile_CPU_seconds=compile_cpu,
              native_budget_CPU_seconds=max(0,29.0-cpu()))
(HERE/'PROBE_HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
with (HERE/'exact_guard.log').open('w') as log:
    subprocess.run([str(HERE/'exact_guard'),str(HERE/'adjacency.csr.u32le.bin'),
                    str(HERE/'mandatory_missing.txt'),str(HERE),str(handle['native_budget_CPU_seconds'])],
                   stdout=log,stderr=log,check=True,timeout=60)
actual=json.loads((HERE/'EXACT_RESULT.json').read_text())
actual['compile_CPU_seconds']=compile_cpu
actual['total_batch_CPU_seconds']=cpu()
actual['prior_measure_compile_CPU_reserve']=prior
actual['scope']='Unique prototype19161 mandatory9 plus all24676 actual free guards, at most two; no source diameter BFS.'
actual['source_allBFS']=0
(HERE/'EXACT_RESULT.json').write_text(json.dumps(actual,indent=2)+'\n')
handle.update(status=actual['status'],total_batch_CPU_seconds=actual['total_batch_CPU_seconds'])
(HERE/'PROBE_HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
print(json.dumps(actual,indent=2))
