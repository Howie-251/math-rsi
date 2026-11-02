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
receipt=json.loads((D/'SOURCE_RECEIPT.json').read_text())
assert receipt['first_row_matches_generator_IDS']
start=cpu()
wall=time.monotonic()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_FIXED_Q137_RULE','capacity_or_graph_run_started':False},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_SOURCE_ARITHMETIC_CAPACITY_THEN_SOLE_GRAPH','native_CPU_hard_limit':10,'only_one_rule':True},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D)],text=True,capture_output=True)
native_including_export_cpu=cpu()-start-compile_cpu
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    r={'status':'UNKNOWN_OR_INVALID_RULE_NATIVE_EXIT','returncode':run.returncode,'actual_D':None}
else:
    r=json.loads((D/'NATIVE_RESULT.json').read_text())
if (D/'CAPACITY.json').exists():
    cap=json.loads((D/'CAPACITY.json').read_text())
    r['quotient_minimum_raw_count']=cap['minimum_raw_count']
    r['quotient_capacity_passes']=cap['passes']
r.update(target_Delta=7,target_D=7,savedL=56952,compile_CPU_seconds=compile_cpu,native_process_CPU_seconds_including_optional_export=native_including_export_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,source_q113_BFS=0,parameter_rules_tested=1,new_lower_bounds=0)
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
term={'status':r['status'],'running':False,'pending':[],'actual_graphs':r.get('actual_graphs',0),'new_lower_bounds':0}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','quotient_minimum_raw_count','actual_graphs','n','m','actual_D','root_R7_missing','first_R7_missing','native_CPU_seconds','native_process_CPU_seconds_including_optional_export','total_parent_children_CPU_seconds'] if k in r}))
