"""One bounded public-object reproduction; no automatic second search."""
import csv
import json
from pathlib import Path
import resource
import subprocess
from time import process_time,perf_counter

root=Path(__file__).resolve().parent
assert not (root/'RESULT.json').exists(),'This one-shot reproduction attempt already completed.'
start=process_time();wall=perf_counter();receipts=[]
source=json.loads((root.parent/'PARAMETERS.json').read_text())
old=json.loads((root.parent/'partial_ovoid65_gate/cubic_coset22/PRECHECK_RESULT.json').read_text())
points=source['points'];lines=[r['points']for r in source['lines']]
assert len(points)==len(lines)==400 and len(old['point_ids'])==22
with (root/'INPUT.txt').open('w')as f:
    f.write('400 400 22\n')
    for row in lines:f.write(' '.join(map(str,row))+'\n')
    f.write(' '.join(map(str,old['point_ids']))+'\n')
def child_run(name,args,limit=None):
    before=resource.getrusage(resource.RUSAGE_CHILDREN);t=perf_counter()
    def cap():
        seconds=max(1,int(limit));resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    with (root/(name+'.stdout')).open('w')as out,(root/(name+'.stderr')).open('w')as err:
        try:r=subprocess.run(args,cwd=root,stdout=out,stderr=err,preexec_fn=cap if limit else None,timeout=50);code=r.returncode
        except subprocess.TimeoutExpired:code='wall_timeout'
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    receipts.append({'stage':name,'exit_code':code,'CPU_seconds':cpu,'wall_seconds':perf_counter()-t})
    return code
# Reserve a conservative quarter-second for prior short input discovery commands.
preparation_allowance=0.25
code=child_run('compile',['g++','-O3','-std=c++17','find33.cpp','-o','find33'])
if code==0:
    used=sum(r['CPU_seconds']for r in receipts)+process_time()-start+preparation_allowance
    remaining=30-used
    assert remaining>1
    code=child_run('search',['./find33',str(remaining-0.5)],remaining)
    if code==0:result=json.loads((root/'search.stdout').read_text())
    else:result={'status':'UNKNOWN_PROCESS_STOP','found33':False,'public_object_reproduction_only':True}
else:result={'status':'COMPILE_FAILED','found33':False,'public_object_reproduction_only':True}
if code==0:
    ids=result['point_ids'];assert len(ids)==len(set(ids))==result['best_valid_size']
    def B(x,y):return (x[0]*y[2]+3*x[1]*y[3]-x[2]*y[0]-3*x[3]*y[1])%7
    with (root/'SELECTED_PAIR_PROOF.csv').open('w')as f:
        writer=csv.writer(f);writer.writerow(['i','j','point_i','point_j','B_mod7'])
        for i,p in enumerate(ids):
            for j,q in enumerate(ids[:i]):
                b=B(points[p],points[q]);assert b!=0;writer.writerow([i,j,p,q,b])
    selected=set(ids);loads=[len(selected.intersection(line))for line in lines];assert max(loads)<=1
    owners=[source['point_spread_owner'][p]for p in ids];assert len(set(owners))==len(ids)
    actual={'status':'PASS_SELECTED_POINTS_PAIRWISE_NONCOLLINEAR','point_ids':ids,
            'points_mod7':[points[p]for p in ids],'point_spread_owners':owners,
            'B_formula':'x0*y2+3*x1*y3-x2*y0-3*x3*y1 mod7',
            'selected_pair_checks':len(ids)*(len(ids)-1)//2,
            'line_intersection_histogram':{str(k):loads.count(k)for k in sorted(set(loads))},
            'source_point_order':'parent PARAMETERS.json points list unchanged'}
    (root/'ACTUAL_POINTS.json').write_text(json.dumps(actual,indent=2)+'\n')
    result['selected_pair_checks']=actual['selected_pair_checks']
    result['line_intersection_histogram']=actual['line_intersection_histogram']
    if result['found33']:
        assert len(ids)==33;result['status']='PASS_REPRODUCED_PUBLISHED_PARTIAL_OVOID33'
result.update({'receipts':receipts,'wrapper_CPU_seconds':process_time()-start,
               'prior_input_discovery_CPU_allowance_seconds':preparation_allowance,
               'accounted_CPU_seconds':sum(r['CPU_seconds']for r in receipts)+process_time()-start+preparation_allowance,
               'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':30,'workers':1,
               'running':False,'active_processes':[],'new_graph_or_method_claim':False})
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
