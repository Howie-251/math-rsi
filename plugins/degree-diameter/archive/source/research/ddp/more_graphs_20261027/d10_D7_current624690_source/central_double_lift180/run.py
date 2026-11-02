import json
import pathlib
import re
import resource
import subprocess
import time

D=pathlib.Path(__file__).resolve().parent
source=json.loads((D.parent/'AUTHOR_construction.json').read_text())
assert source['order']==624690
assert source['construction']['group']=={'type':'metacyclic','N':6941,'M':90,'r':316}
positive=[tuple(map(int,re.fullmatch(r'x\^(\d+)\s+y\^(\d+)',s).groups())) for s in source['construction']['connection_set']]
assert positive==[(35,35),(509,5),(4285,37),(6911,49),(3639,34)]
(D/'SOURCE_BINDING.json').write_text(json.dumps({'source_recipe':'../AUTHOR_construction.json','source_order':624690,'source_group':[6941,90,316],'positive_normal_phase':positive,'source_recipe_literal_MATCH':True,'gauge_or_phase_relabeling_used':False,'source_BFS':0},indent=2)+'\n')
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
wall=time.monotonic()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_FIXED_CENTRAL_DOUBLELIFT','kernel_gate_or_graph_started':False},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_EXACT_KERNEL_GATE_THEN_CONDITIONAL_GRAPH','native_CPU_hard_limit':10,'only_one_rule':True,'source_BFS':0},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D)],text=True,capture_output=True)
native_process_cpu=cpu()-start-compile_cpu
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    r={'status':'UNKNOWN_OR_INVALID_NATIVE_EXIT','returncode':run.returncode,'actual_D':None}
else:
    r=json.loads((D/'NATIVE_RESULT.json').read_text())
if (D/'KERNEL_GATE.json').exists():
    r['kernel_gate']=json.loads((D/'KERNEL_GATE.json').read_text())
r.update(target_Delta=10,target_D=7,savedL=624690,compile_CPU_seconds=compile_cpu,native_process_CPU_seconds=native_process_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,source_BFS=0,parameter_rules_tested=1,new_lower_bounds=0)
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
term={'status':r['status'],'running':False,'pending':[],'actual_graphs':r.get('actual_graphs',0),'new_lower_bounds':0}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','actual_graphs','n','m','actual_D','kernel_target_word_count','root_R7_missing','first_R7_missing','native_CPU_seconds','native_process_CPU_seconds','total_parent_children_CPU_seconds'] if k in r}))
