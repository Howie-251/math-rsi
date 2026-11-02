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
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_ONE_FROZEN_CIRCLEPOLE_RULE','phase_numeric_run_started':False,'graph_constructed':False},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_PHASE_GATE_THEN_CONDITIONAL_GRAPH','native_CPU_hard_limit':10,'only_one_rule':True},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D)],text=True,capture_output=True)
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    r={'status':'UNKNOWN_OR_INVALID_RULE_NATIVE_EXIT','returncode':run.returncode,'actual_D':None}
else:
    r=json.loads((D/'NATIVE_RESULT.json').read_text())
phase=D/'PHASE_PREFLIGHT.json'
if phase.exists():
    r['phase_preflight']=json.loads(phase.read_text())
r.update(target_Delta=11,target_D=4,savedL=3645,compile_CPU_seconds=compile_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,source_BFS_repeated=0,parameter_rules_tested=1,new_lower_bounds=0)
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
term={'status':r['status'],'running':False,'pending':[],'actual_graphs':r.get('actual_graphs',0),'new_lower_bounds':0}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','actual_graphs','n','m','actual_D','R4_roots_checked','failed_source','first_missing_target','failed_root_R4_missing','native_CPU_seconds','total_parent_children_CPU_seconds','phase_preflight'] if k in r}))
