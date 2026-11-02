"""One source parse and eight complete writers after root's actual public gate."""
import csv
import json
from pathlib import Path
import resource
import subprocess
from time import process_time,perf_counter

root=Path(__file__).resolve().parent
assert not (root/'RESULT.json').exists(),'This production batch already completed.'
start=process_time();wall=perf_counter();receipts=[]
source=root.parent.parent
public=source.parents[1]/'public_baseline_audit/P33_CLONE_DEGREE65_72_WINDOW_20261101.json'
assert public.is_file(),str(public)
centers=list(csv.DictReader((root.parent/'INTERFACE_ORDERED_CENTERS.csv').open()))
assert len(centers)==1650
pins=[[]for _ in centers]
for row in csv.DictReader((root.parent/'INTERFACE_PINS.tsv').open(),delimiter='\t'):
    pins[int(row['center_index'])].append(int(row['source_pin_label']))
with (root/'CENTERS_INPUT.txt').open('w')as f:
    f.write('1650\n')
    for i,c in enumerate(centers):
        assert int(c['center_index'])==i and len(pins[i])==64
        f.write(' '.join(map(str,[int(c['source_center_label']),64,*pins[i]]))+'\n')
with (root/'ORDERED_CLONE_RECIPE.tsv').open('w')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['j','copy','base_index','point_index','spread_index','point_label','spread_line','source_center_label','new_label','immutable_source_degree'])
    for copy in range(8):
        for i,c in enumerate(centers):
            j=1650*copy+i
            w.writerow([j,copy,i,c['point_index'],c['spread_index'],c['point_label'],c['line_label'],c['source_center_label'],160050+j,64])
with (root/'PREFIX_LOADS.csv').open('w')as f:
    w=csv.writer(f);w.writerow(['clone_prefix','added_edges','source_vertices',*[f'old_load{i}_count'for i in range(9)],'max_old_load','new_degree'])
    for prefix in range(13201):
        copies,partial=divmod(prefix,1650);hist=[0]*9
        if copies==0:hist[0]=160050-64*partial;hist[1]=64*partial
        else:
            hist[0]=54450;hist[copies]=105600-64*partial
            if partial:hist[copies+1]=64*partial
        assert sum(hist)==160050
        w.writerow([prefix,64*prefix,160050,*hist,(prefix+1649)//1650,64 if prefix else 0])
(root/'graphs').mkdir(exist_ok=True)
def child_run(name,args,limit=None):
    before=resource.getrusage(resource.RUSAGE_CHILDREN);t=perf_counter()
    def cap():
        seconds=max(1,int(limit));resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    with (root/(name+'.stdout')).open('w')as out,(root/(name+'.stderr')).open('w')as err:
        try:r=subprocess.run(args,cwd=root,stdout=out,stderr=err,preexec_fn=cap if limit else None,timeout=55);code=r.returncode
        except subprocess.TimeoutExpired:code='wall_timeout'
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    receipts.append({'stage':name,'exit_code':code,'CPU_seconds':cpu,'wall_seconds':perf_counter()-t})
    return code
code=child_run('compile',['g++','-O3','-std=c++17','produce.cpp','-o','produce'])
if code==0:
    used=sum(r['CPU_seconds']for r in receipts)+process_time()-start
    remaining=30-used
    assert remaining>1
    code=child_run('produce',['./produce',str(source/'graph_d64_D3_n160050.edges'),str(remaining-0.5)],remaining)
    if code==0:result=json.loads((root/'produce.stdout').read_text())
    else:result={'status':'UNKNOWN_PRODUCTION_PROCESS_STOP','production_complete':False,'exit_code':code}
else:result={'status':'COMPILE_FAILED','production_complete':False,'exit_code':code}
result.update({'receipts':receipts,'public_gate_document':str(public),'ordered_clone_recipe_rows':13200,
               'prefix_load_rows_including_zero':13201,'source_edgefile_parses':1 if code==0 else 'see_process_stop',
               'independent_acceptance':'pending_separate_fresh_validation',
               'new_graph_count_accepted_by_producer':0,'wrapper_CPU_seconds':process_time()-start,
               'accounted_CPU_seconds':sum(r['CPU_seconds']for r in receipts)+process_time()-start,
               'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':30,'workers':1,
               'running':False,'active_processes':[]})
if code==0:
    result['production_complete']=True
    for c in result['cases']:
        case=root/'cases'/('d'+str(c['degree_cap'])+'_n'+str(c['n']));case.mkdir(parents=True,exist_ok=True)
        per=dict(c,status='PASS_PRODUCTION_PENDING_FRESH_ACCEPTANCE',independent_acceptance='pending',running=False,active_processes=[])
        for name in ['RESULT.json','TERMINAL.json']:(case/name).write_text(json.dumps(per,indent=2)+'\n')
for name in ['RESULT.json','TERMINAL.json']:(root/name).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
