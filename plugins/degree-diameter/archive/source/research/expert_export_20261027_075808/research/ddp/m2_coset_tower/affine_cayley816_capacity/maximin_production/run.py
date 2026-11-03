#!/usr/bin/env python3
from pathlib import Path
import json
import os
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent
assert not (HERE/'run.json').exists(), 'One authorized run; no restart.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();wall=time.monotonic()
sys.path.insert(0,str(SOURCE.parent/'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
selected=[]
for line in (SOURCE/'survivors.jsonl').open():
    row=json.loads(line)
    if row['minimum_symbolic_capacity']=={5:27,6:26}.get(row['pair_count'],-1):selected.append(row)
selected.sort(key=lambda row:(-row['minimum_symbolic_capacity'],row['cursor']))
assert len(selected)==76
assert sum(r['pair_count']==5 for r in selected)==28
assert sum(r['pair_count']==6 for r in selected)==48
assert sum(r['projective_marked_inputs']for r in selected)==46500312
product=[[(i+j)%48 for j in range(48)]for i in range(48)]
inverse=[(-j)%48 for j in range(48)];scalar=[pow(3,j,17)for j in range(48)]
assert scalar[16]==1 and scalar[8]==16 and scalar[24]==16
inputs=[];text=['76']
for index,row in enumerate(selected):
    phases=row['pair_phases'];p=len(phases);anchor=row['anchor_component']
    assert scalar[phases[anchor]]!=1
    variables=12-p-1
    components=[{'phase':j,'kind':'pair'}for j in phases]+[{'phase':24,'kind':'involution'}for _ in range(12-2*p)]
    symbolic=affine_word_forms(17,product,inverse,scalar,components)
    fibers=[]
    for j,original in enumerate(symbolic['forms']):
        anchored={c[:anchor]+c[anchor+1:]for c in original}
        assert len(original)==len(anchored)==row['symbolic_capacity'][j]
        fibers.append({'phase':j,'forms':sorted(anchored)})
    fibers.sort(key=lambda f:(len(f['forms']),f['phase']))
    scope=(17**variables-1)//16
    assert scope==row['projective_marked_inputs']
    inputs.append({'pattern_index':index,'source_cursor':row['cursor'],'pairs':p,'involutions':12-2*p,'pair_phases':phases,'anchor_component':anchor,'remaining_field_dimension':variables,'projective_scope':scope,'minimum_form_count':row['minimum_symbolic_capacity'],'fiber_test_order':[f['phase']for f in fibers],'form_counts_in_test_order':[len(f['forms'])for f in fibers]})
    text.append(' '.join(map(str,[row['cursor'],anchor,p,variables,scope]+phases)))
    for f in fibers:
        text.append(f"{f['phase']} {len(f['forms'])}")
        text.extend(' '.join(map(str,c))for c in f['forms'])
(HERE/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
(HERE/'inputs.txt').write_text('\n'.join(text)+'\n')
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start
# Includes observed selection/source-preparation command cost; no second production process.
source_setup_allowance=0.5
remaining=180-prep-source_setup_allowance-1
assert remaining>0
metadata={'group':'F17 semidirect_3 C48 = AGL1(17) x C3','n':816,'degree':12,'target_D':3,'patterns':76,'raw_marked_scope':46500312,'branches':[{'pairs':5,'involutions':2,'minimum_symbolic_fiber':27,'patterns':28,'per_pattern_scope':1508598},{'pairs':6,'involutions':0,'minimum_symbolic_fiber':26,'patterns':48,'per_pattern_scope':88741}],'normalization':'one true nonunit-action component field set to zero; remaining field vector has first nonzero coordinate1, no additional normalization','enumeration_order':'minimum form count descending, source cursor; leading coordinate ascending, lexicographic tail last coordinate fastest','fiber_order':'form count ascending, phase ascending','legality':'actual 12 group elements are all nonidentity and pairwise distinct before any fiber test','fiber_test':'exact values of all reduced words of length<=3; reject only after losses>m-17; full root BFS only after all48 fibers cover F17','CPU_budget_seconds':180,'worker_count':1,'preparation_CPU_seconds':prep,'source_setup_CPU_allowance_seconds':source_setup_allowance,'production_CPU_limit_seconds':remaining,'shutdown_reserve_seconds':1,'other67115_minus76_patterns':'not processed','best_graph_policy':'save only actual D3 through-case; no fallback graph','formal_prefix_calibration':'a few actual enumerated coordinates in first selected pattern of each branch, no additional BFS'}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
run={'status':'RUNNING','running':True,'worker_count':1,'raw_scope':46500312,'CPU_budget_seconds':180,'preparation_CPU_seconds':prep,'source_setup_CPU_allowance_seconds':source_setup_allowance,'production_CPU_limit_seconds':remaining,'driver_pid':os.getpid()}
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (HERE/'production.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
    code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,restarts=0)
run['budget_accounted_CPU_seconds']=run['total_recorded_CPU_seconds']+source_setup_allowance
if code==0:
    terminal=json.loads((HERE/'terminal.json').read_text())
    run.update(status=terminal['status'],processed_inputs=terminal['processed_inputs'],actual_full_root_BFS=terminal['actual_full_root_BFS'],saved_best_graph=terminal['saved_best_graph'])
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
