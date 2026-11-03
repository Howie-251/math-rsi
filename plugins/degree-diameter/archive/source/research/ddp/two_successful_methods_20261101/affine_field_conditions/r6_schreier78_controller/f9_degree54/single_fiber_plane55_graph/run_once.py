#!/usr/bin/env python3
"""One bounded complete production, preserving original source edges."""
import time
START = time.process_time()
import csv
import json
import resource
import subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
CPU_START_CHILDREN=resource.getrusage(resource.RUSAGE_CHILDREN)
BUDGET=30.0

def children_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-CPU_START_CHILDREN.ru_utime-CPU_START_CHILDREN.ru_stime

def total_cpu():
    return time.process_time()-START+children_cpu()

def limit_child():
    resource.setrlimit(resource.RLIMIT_CPU,(27,28))

phases=[]
def run(name,command):
    before=total_cpu()
    with (HERE/(name+'.stdout')).open('w') as out, (HERE/(name+'.stderr')).open('w') as err:
        p=subprocess.run(command,stdout=out,stderr=err,preexec_fn=limit_child)
    phases.append({'phase':name,'command':command,'returncode':p.returncode,'CPU_seconds_including_driver':total_cpu()-before})
    if p.returncode:
        terminal={'status':'FAIL','steps':phases,'total_CPU_seconds':total_cpu(),'CPU_budget_seconds':BUDGET,'single_worker':True,'all_children_terminal':True}
        (HERE/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
        raise SystemExit(p.returncode)

p=json.loads((BASE/'single_fiber_plane55_interface/PARAMETERS.json').read_text())
pinrows=list(csv.DictReader((BASE/'single_fiber_plane55_interface/PINS.csv').open()))
pins=[[] for _ in range(81)]
for r in pinrows:pins[int(r['j'])].append(int(r['pin_old_label']))
with (HERE/'ORDERED_PINS.tsv').open('w') as f:
    for j,c in enumerate(p['center_old_labels']):
        assert len(pins[j])==54
        f.write(' '.join(str(v) for v in [j,c,56862+j,*sorted(pins[j])])+'\n')
run('compile',['g++','-O2','-std=c++17',str(HERE/'generate.cpp'),'-o',str(HERE/'generate')])
run('generate',[str(HERE/'generate'),str(BASE/'graph_d54_D3_n56862.edges'),str(HERE/'ORDERED_PINS.tsv'),str(HERE)])
result=json.loads((HERE/'generate.stdout').read_text())
assert result['status']=='PRODUCTION_PASS'
(HERE/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
p.update({
    'scope':'One complete retained-edge expansion of accepted56862source',
    'source':'../PARAMETERS.json','source_edge_file':'../graph_d54_D3_n56862.edges',
    'interface':'../single_fiber_plane55_interface/PARAMETERS.json',
    'source_vertices':56862,'source_edges':1535274,'source_degree':54,
    'n':56943,'m':1539648,'Delta':55,'D':3,
    'degree_histogram':{'54':52569,'55':4374},
    'retained_source_edges':1535274,'new_vertices':81,'new_edges':4374,
    'new_new_edges':0,'max_old_pin_load':1,
    'clone_rule':'new56862+j has exactly immutable accepted sourceN54 of center_j; no new-new edges',
    'center_literal_source_neighbor_binding':'All81centers/4374pins compared to complete original literal source at generation',
    'ordered_pin_rows':'ORDERED_PINS.tsv','prefix_degree_checks':'PREFIX_LOADS.csv',
    'pins':'../single_fiber_plane55_interface/PINS.csv',
    'ordered_centers':'../single_fiber_plane55_interface/CENTER_SEQUENCE.csv',
    'source_edge_file_read':True,'source_edgefile_reads':1,
    'edge_file':'graph_d55_D3_n56943.edges',
    'edge_file_format':'No header; a b with a<b; globally lexsorted; each edge once',
    'complete_extension_graph_generated':True,'public_gate_complete_here':False,
    'public_gate_completed_by_root':True,
    'public_gate_receipt':'../../../../public_baseline_audit/DEGREE55_SINGLE_FIBER_TARGET_GATE_20261101.json',
    'public_best_located':56375,'public_difference':568,
    'global_record_or_priority_certified':False,'Lean_complete_here':False,
    'BFS_performed_here':False,'independent_acceptance_done_here':False,
    'all_prefix_D3_proof':'PROOF.md',
    'predicted_new_root_histogram':{'histogram':[1,54,2477,54411],'roots':81},
})
(HERE/'PARAMETERS.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
assert total_cpu()<BUDGET
terminal={'status':'PRODUCTION_PASS','total_CPU_seconds':total_cpu(),'CPU_budget_seconds':BUDGET,'single_worker':True,'all_children_terminal':True,'steps':phases,'BFS_solver_Lean_runs':0,'source_BFS_repeated':False,'new_graph_counted_by_producer':False,'measurement_boundary':'Python imports/preparation, exact interface conversion, one C++compile, original literal source/pin binding, fullgraph creation, result aggregation'}
(HERE/'TERMINAL.json').write_text(json.dumps(terminal,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':result,'terminal':terminal},ensure_ascii=False))
