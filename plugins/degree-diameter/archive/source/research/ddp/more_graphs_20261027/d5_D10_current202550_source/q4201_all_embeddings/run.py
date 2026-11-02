import json
import pathlib
import resource
import subprocess
import time

D=pathlib.Path(__file__).resolve().parent
source=json.loads((D.parent/'AUTHOR_construction.json').read_text())
assert source['order']==202550
assert source['construction']['group']=={'type':'metacyclic','N':4051,'M':25,'r':4}
assert source['construction']['loops']==[[0,'y^3'],[1,'x^178 y^8']]
assert source['construction']['links']==[[0,1,'1'],[0,1,'x y^2'],[0,1,'x^2122 y^15']]
cap=json.loads((D/'ROOT_CONTROL_CAPACITY.json').read_text())
assert cap['chosen_source_base']==0 and cap['chosen_target_controller']==34
assert cap['minimum_raw_count']==34605 and cap['raw_prefixes_per_root']==1747626
assert cap['passes_necessary_capacity']
(D/'THIN_INPUT.txt').write_text('0 34\n')
binding={'source_recipe':'../AUTHOR_construction.json','source_bind_MATCH':True,'normalization':'phasejprime17j,beta4cubed64,sourcecentered178/-1929','left_law':True,'source_BFS':0,'raw_capacity_inherited_from_parent':'ROOT_CONTROL_CAPACITY.json','producer_raw_reenumeration':0,'chosen_source_base':0,'chosen_target_controller':34,'raw_minimum':34605}
(D/'SOURCE_BINDING.json').write_text(json.dumps(binding,indent=2)+'\n')
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
wall=time.monotonic()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_ONE_FINITE20_EMBEDDING_BATCH','numeric_batch_started':False},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_AGGREGATE20_EXACT_IMAGES_AND_CONDITIONAL_TWO_BASE_BFS','native_CPU_hard_limit':10,'source_BFS':0},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D)],text=True,capture_output=True)
native_process_cpu=cpu()-start-compile_cpu
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    cases=[]
    if (D/'CASES.jsonl').exists():
        cases=[json.loads(line) for line in (D/'CASES.jsonl').read_text().splitlines() if line.strip()]
    cursor=json.loads((D/'cursor.json').read_text()) if (D/'cursor.json').exists() else None
    r={'status':'UNKNOWN_OR_INVALID_NATIVE_EXIT','returncode':run.returncode,'cases':cases,'last_cursor':cursor}
else:r=json.loads((D/'NATIVE_RESULT.json').read_text())
r.update(target_Delta=5,target_D=10,savedL=202550,compile_CPU_seconds=compile_cpu,native_process_CPU_seconds=native_process_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,source_BFS=0,producer_raw_capacity_enumerations=0,new_lower_bounds=0)
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
term={'status':r['status'],'running':False,'pending':[],'actual_graphs':r.get('actual_graphs',0),'full_hits':r.get('full_hits',0),'result':'RESULT.json'}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n');(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','chosen_source_base','chosen_target_controller','embeddings_touched','embeddings_unattempted','gate_passers','actual_graphs','complete_base_BFS','full_hits','native_CPU_seconds','native_process_CPU_seconds','total_parent_children_CPU_seconds'] if k in r}))
