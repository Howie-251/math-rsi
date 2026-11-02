"""Sequential new-scope queue; stop at the first failed module."""
import json
from pathlib import Path
import subprocess
from time import process_time,perf_counter

D=Path(__file__).resolve().parent
start=process_time();wall=perf_counter();prefix='GQ77Published33CloneFamily'
modules=[prefix+f'InputChunk{i:02d}'for i in range(1,20)]+[prefix+'Inputs',prefix+'Exact',prefix+'Audit']
done=[];failed=None
state_path=D/'STAGE_STATE.json'
for mod in modules:
    state=json.loads(state_path.read_text());state.update(status='NEW_MODULE_QUEUE_ACTIVE',running=True,active_modules=[mod])
    state_path.write_text(json.dumps(state,indent=2)+'\n')
    r=subprocess.run(['python3','compile.py',mod,'60'],cwd=D,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    receipt=json.loads((D/(mod+'_RESULT.json')).read_text())
    print(json.dumps(receipt),flush=True)
    if r.returncode:
        print(r.stdout[-12000:],flush=True);failed=mod;break
    done.append(mod)
    state=json.loads(state_path.read_text())
    if 'InputChunk'in mod:state['finite_chunks_compiled']=1+sum('InputChunk'in x for x in done)
    if mod.endswith('Inputs'):state['inputs_compiled']=True
    if mod.endswith('Exact'):state['exact_compiled']=True
    if mod.endswith('Audit'):state['audit_compiled']=True
    state.update(running=False,active_modules=[])
    state_path.write_text(json.dumps(state,indent=2)+'\n')
state=json.loads(state_path.read_text());state.update(status='NEW_QUEUE_FAILED'if failed else 'KERNEL_QUEUE_COMPLETE_EXTERNAL_BINDING_PENDING',running=False,active_modules=[])
state_path.write_text(json.dumps(state,indent=2)+'\n')
result={'status':'FAILED'if failed else 'COMPLETE','modules_completed':done,'failed_module':failed,
        'CPU_seconds':process_time()-start,'wall_seconds':perf_counter()-wall,'running':False,'active_processes':[]}
(D/'QUEUE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
