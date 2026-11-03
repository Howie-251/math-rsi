import json
import pathlib
import resource
import subprocess
import time

D=pathlib.Path(__file__).resolve().parent
SOURCE=D.parents[1]/'d3_D8_current360_Q8_source'
source=json.loads((SOURCE/'AUTHOR_construction.json').read_text())
assert source['degree']==3 and source['order']==360
assert source['construction']['links']==[[0,2,'1'],[0,3,'1'],[0,4,'1'],[1,4,'1'],[1,2,'i^3'],[1,3,'v(0,1) j^3']]
models=json.loads((SOURCE/'representation_analysis/TARGET_CONTROLS.json').read_text())
model=next(x for x in models['models'] if x['q']==7)
capacity=json.loads((D/'CONTROL_CAPACITY_ROOT.json').read_text())
formal=json.loads((D/'UNIVERSAL_ENDPOINT_RESULT_ROOT.json').read_text())
assert capacity['results']['9']['minimum_raw_count']==29
assert capacity['results']['10']['minimum_raw_count']==66
assert formal['results']['9']['universal_distinct_count']==20
assert formal['results']['9']['strict_universal_obstruction']
assert formal['results']['10']['universal_distinct_count']==53
assert not formal['results']['10']['strict_universal_obstruction']
assert model['abstract_Q8_mul_table']==capacity['Q8_multiplication']
names=model['names']
text=['7 10']
for matrix in model['matrices']:
    text.append(' '.join(str(x) for row in matrix for x in row))
for row in capacity['Q8_multiplication']:text.append(' '.join(map(str,row)))
for u,v,normal,h in model['links']:text.append(f'{u} {v} {normal[0]} {normal[1]} {names.index(h)}')
for base,normal,h in model['semi_edges']:text.append(f'{base} {normal[0]} {normal[1]} {names.index(h)}')
(D/'INPUT.txt').write_text('\n'.join(text)+'\n')
recipe={'source_recipe':str((SOURCE/'AUTHOR_construction.json').relative_to(D.parents[3])),'source_old_BFS':0,'group_law':'(v,Q)*(w,R)=(v+rho(Q)w,Q*R)','vertex_encoding':'base*(8*q*q)+h*q*q+q*v1+v2','source_vector_rule':'Q8regular-torsor equivariantmap, notcoordinate/reductionmap','q5_status':'STRICT_FORMAL_GATE_REJECTED_BEFORE_GRAPH','q7_model':{k:v for k,v in model.items() if k not in ['graph_generated','wordscan_run','BFS_run']},'capacity_cache':'CONTROL_CAPACITY_ROOT.json','formal_gate':'UNIVERSAL_ENDPOINT_RESULT_ROOT.json'}
(D/'RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
wall=time.monotonic()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_Q7_ONLY_AFTER_Q5_FORMAL_REJECTION','capacity_word_scans_by_producer':0,'source_BFS':0},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_Q7_ACTUAL_GRAPH_AND_ALL5_ROOTS','native_CPU_hard_limit':10,'q5_actual_graph':0},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D)],text=True,capture_output=True)
native_process_cpu=cpu()-start-compile_cpu
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:r={'status':'UNKNOWN_OR_INVALID_NATIVE_EXIT','returncode':run.returncode,'actual_D':None}
else:r=json.loads((D/'NATIVE_RESULT.json').read_text())
r.update(compile_CPU_seconds=compile_cpu,native_process_CPU_seconds=native_process_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,producer_capacity_wordscans=0,source360_BFS=0)
result={'status':'BOTH_FROZEN_Q8_ORBIT_CONTROLS_TERMINAL' if not run.returncode else r['status'],'q5':{'status':'STRICT_UNIVERSAL_FORMAL_GATE_REJECTED','target_Delta':3,'target_D':9,'savedL':600,'n_hypothetical':1000,'raw_minimum':29,'formal_endpoints_at_witness_slot':20,'required_fiber_size':25,'actual_graphs':0,'BFS':0,'actual_D':None},'q7':r,'actual_graphs':int(not run.returncode),'producer_BFS_complete':r.get('BFS_complete',0),'producer_capacity_wordscans':0,'source360_BFS':0,'new_lower_bounds':0}
(D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
term={'status':result['status'],'running':False,'pending':[],'actual_graphs':result['actual_graphs'],'q5_graphs':0,'q7_BFS_complete':r.get('BFS_complete',0),'new_lower_bounds':0}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n');(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({'status':result['status'],'q5':result['q5'],'q7_status':r['status'],'q7_n':r.get('n'),'q7_actual_D':r.get('actual_D'),'q7_BFS_complete':r.get('BFS_complete'),'native_CPU_seconds':r.get('native_CPU_seconds'),'total_parent_children_CPU_seconds':r['total_parent_children_CPU_seconds']}))
