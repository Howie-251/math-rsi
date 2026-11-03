import json
import pathlib
import resource
import subprocess
import time

D=pathlib.Path(__file__).resolve().parent
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
wall=time.monotonic()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_ONE_FINITE22_EMBEDDING_BATCH','numeric_batch_started':False},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_AGGREGATE22_ROOTS_RUNNING','native_CPU_hard_limit':10,'source_BFS':0},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D)],text=True,capture_output=True)
native_process_cpu=cpu()-start-compile_cpu
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    records=[]
    stream=D/'CASES.jsonl'
    if stream.exists():
        records=[json.loads(line) for line in stream.read_text().splitlines() if line.strip()]
    cursor=json.loads((D/'cursor.json').read_text()) if (D/'cursor.json').exists() else None
    r={'status':'UNKNOWN_OR_INVALID_NATIVE_EXIT','returncode':run.returncode,'cases':records,'last_cursor':cursor,'actual_D':None}
else:
    r=json.loads((D/'NATIVE_RESULT.json').read_text())
r.update(target_Delta=8,target_D=7,savedL=139679,compile_CPU_seconds=compile_cpu,native_process_CPU_seconds=native_process_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,source_BFS=0,new_lower_bounds=0)
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
term={'status':r['status'],'running':False,'pending':[],'result':'RESULT.json','actual_graphs':r.get('actual_graphs',0),'full_hits':r.get('full_hits',0)}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','chosen_thin_phase','raw_minimum','embeddings_touched','embeddings_unattempted','gate_passers','actual_graphs','complete_identity_BFS','full_hits','native_CPU_seconds','native_process_CPU_seconds','total_parent_children_CPU_seconds'] if k in r}))
