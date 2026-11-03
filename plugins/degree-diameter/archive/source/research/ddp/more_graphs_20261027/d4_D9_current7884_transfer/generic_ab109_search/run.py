import json
import pathlib
import resource
import subprocess
import time

HERE=pathlib.Path(__file__).resolve().parent
FORMS=HERE.parent/'phase_analysis/generic_ab109_forms/generic_ab109.forms.bin'
START=time.process_time()
C0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+r.ru_utime+r.ru_stime-C0.ru_utime-C0.ru_stime
assert not (HERE/'RESULT.json').exists()
assert FORMS.exists()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
compiled=cpu()
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'NATIVE_RUNNING','forms':str(FORMS),'budget_CPU_seconds':30,'compile_CPU_seconds':compiled},indent=2)+'\n')
with (HERE/'search.log').open('w') as log:
    subprocess.run([str(HERE/'search'),str(FORMS),str(HERE),str(29.5-cpu())],
                   stdout=log,stderr=log,check=True,timeout=45)
r=json.loads((HERE/'NATIVE_RESULT.json').read_text())
r['compile_CPU_seconds']=compiled
r['total_batch_CPU_seconds']=cpu()
r['actual_n']=11772 if r['hit'] else None
r['actual_D']=json.loads((HERE/'FIRST_HIT.json').read_text())['actual_global_D'] if r['hit'] else None
r['ordinary_bad_unordered_pairs']=0 if r['hit'] else None
r['hypothetical_n']=11772
r['unattempted_cases']=71286-r['cases_processed']
r['prediction']='SUPPORTED' if r['hit'] else 'UNRESOLVED' if r['CPU_limited'] else 'REFUTED'
r['pending']=['Root independent newgraph acceptance'] if r['hit'] else []
(HERE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(r,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':r['status'],'pending':r['pending'],'total_batch_CPU_seconds':r['total_batch_CPU_seconds']},indent=2)+'\n')
print(json.dumps(r,indent=2))
