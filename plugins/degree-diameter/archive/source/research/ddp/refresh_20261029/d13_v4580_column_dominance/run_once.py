import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'d13_v4580_fourguard'
assert sys.byteorder=='little'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start,wall=cpu(),time.monotonic()
meta=json.loads((SOURCE/'prepared.json').read_text())
K,N,W=len(meta['representatives']),meta['missing_count'],meta['mask_words_per_row']
assert (K,N,W)==(13057,2755,44)
subprocess.run(['g++','-std=c++17','-O2',str(HERE/'check.cpp'),'-o',str(HERE/'check')],check=True)
compile_cpu=cpu()-start
with (HERE/'RESULT.json').open('w') as out:
    subprocess.run([str(HERE/'check'),str(SOURCE/'prepared.masks.u64.bin'),str(K),str(W),str(N)],stdout=out,check=True)
x=json.loads((HERE/'RESULT.json').read_text())
reps=meta['representatives']
x['retained_guard_labels']=[reps[i] for i in x['retained_column_ids']]
x['removed_guard_labels']=[reps[i] for i in x['removed_column_ids']]
for row in x['drop_witnesses']:
    row['removed_guard_label']=reps[row['removed_column_id']]
    row['retained_superset_guard_label']=reps[row['retained_superset_column_id']]
x['column_id_convention']='zero-based index in unchanged prepared.json representatives'
x['targets']=meta['missing']
x['scope']={'source_n':meta['source_n'],'source_m':meta['source_m'],'prototype':4580,'mandatory_pins':meta['pins'],'guard_budget':4,'unit_cost':True,'conflicts':False}
x['compile_cpu_seconds']=compile_cpu
x['aggregate_cpu_seconds']=cpu()-start
x['wall_seconds']=time.monotonic()-wall
x['graph_reads']=x['ball_computations']=x['solver_calls']=x['new_graphs']=0
assert x['aggregate_cpu_seconds']<5
x['status']='COMPLETE_STRICT_COLUMN_DOMINANCE' if x['complete'] else 'CPU_BOUND_PARTIAL_NO_MODEL_CLAIM'
(HERE/'RESULT.json').write_text(json.dumps(x,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps({k:x[k] for k in ['status','complete','processed_columns','retained_count','removed_count','exact_witness_checks','aggregate_cpu_seconds','graph_reads','ball_computations','solver_calls','new_graphs']}|{'pending':[]},indent=2)+'\n')
print(json.dumps({k:v for k,v in x.items() if k not in ['retained_column_ids','removed_column_ids','retained_guard_labels','removed_guard_labels','drop_witnesses','targets']},indent=2))
