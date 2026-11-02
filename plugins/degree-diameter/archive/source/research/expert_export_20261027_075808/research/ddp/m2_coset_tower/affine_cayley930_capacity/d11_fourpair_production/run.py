#!/usr/bin/env python3
from pathlib import Path
import json
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent
assert not (HERE/'run.json').exists(), 'One authorized production run; do not restart.'
sys.path.insert(0,str(SOURCE.parent/'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();wall=time.monotonic()
saved=json.loads((SOURCE/'d11_tight_linear.survivors.json').read_text())
selected=sorted([row for row in saved if row['degree']==11 and row['pair_count']==4],key=lambda row:row['cursor'])
assert len(selected)==37
quadratic=json.loads((SOURCE/'D11_FOURPAIR_QUADRATIC.json').read_text())
surplus=json.loads((SOURCE/'d11_surplus_one.json').read_text())
assert surplus['modes_remaining']==37 and surplus['modes_with_new_linear_constraints']==0
assert quadratic['patterns_with_forced_linear_rows']==0
product=[[(i+j)%30 for j in range(30)]for i in range(30)]
inverse=[(-i)%30 for i in range(30)];scalar=[pow(3,j,31)for j in range(30)]
inputs=[];text=['37']
for index,row in enumerate(selected):
    assert row['field_variables']==7 and row['involution_count']==3
    assert row['anchor_component']==0 and row['rank_mod31']==0 and row['nullspace_dimension']==6
    basis=row['nullspace_basis_after_anchor'];assert basis==[[int(i==j)for j in range(6)]for i in range(6)]
    phases=row['pair_phases'];assert len(set(phases))==4 and all(1<=j<=14 for j in phases)
    components=[{'phase':j,'kind':'pair'}for j in phases]+[{'phase':15,'kind':'involution'}for _ in range(3)]
    symbolic=affine_word_forms(31,product,inverse,scalar,components)
    anchor=row['anchor_component']
    fibers=[]
    for j,original in enumerate(symbolic['forms']):
        anchored={c[:anchor]+c[anchor+1:]for c in original}
        restricted={tuple(sum(x*y for x,y in zip(c,b))%31 for b in basis)for c in anchored}
        assert len(original)==len(anchored)==len(restricted)==row['restricted_form_counts'][j]
        fibers.append({'phase':j,'forms':sorted(restricted)})
    fibers.sort(key=lambda fiber:(len(fiber['forms']),fiber['phase']))
    scope=(31**6-1)//30;assert scope==row['projective_marked_inputs_after_linear_constraints']
    item={'pattern_index':index,'source_cursor':row['cursor'],'pair_phases':phases,'anchor_component':anchor,'basis':basis,'projective_scope':scope,'legal_scope':31**4*29,'fiber_test_order':[f['phase']for f in fibers],'form_counts_in_test_order':[len(f['forms'])for f in fibers]}
    inputs.append(item)
    text.append(' '.join(map(str,[row['cursor'],anchor,scope]+phases)))
    for fiber in fibers:
        text.append(f"{fiber['phase']} {len(fiber['forms'])}")
        text.extend(' '.join(map(str,c))for c in fiber['forms'])
assert sum(x['projective_scope']for x in inputs)==1094587872
(HERE/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
(HERE/'inputs.txt').write_text('\n'.join(text)+'\n')
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=600-prep-1;assert remaining>0
metadata={'group':'F31 semidirect_3 C30','n':930,'degree':11,'target_D':3,'patterns':37,'raw_marked_scope':1094587872,'legal_marked_scope':37*31**4*29,'scope_per_pattern':29583456,'normalization':'anchor original component0=0; first nonzero nullspace coordinate z=1, remaining arbitrary; identity saved nullspace basis','enumeration_order':'source cursor, increasing leading nonzero coordinate, lexicographic tail with z5 fastest','fiber_order':'increasing number of distinct restricted forms, then quotient phase','rejection':'after t forms yielding u distinct values reject iff t-u>m-31','pre_BFS_tests':'exact original legality first; all30 exact fiber coverage tests; then true inverse-closed S check and full root BFS','first_100000':'same production cursor, no separate profiling prefix','CPU_budget_seconds':600,'worker_count':1,'preparation_CPU_seconds':prep,'production_CPU_limit_seconds':remaining,'conservative_shutdown_reserve_seconds':1,'old_five_pair_branch':'untouched','final_independent_check':'parent-owned only if an actual BFS candidate is saved'}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
run={'status':'RUNNING','running':True,'worker_count':1,'raw_scope':1094587872,'CPU_budget_seconds':600,'preparation_CPU_seconds':prep,'production_CPU_limit_seconds':remaining,'driver_pid':__import__('os').getpid()}
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (HERE/'production.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall)
if code==0:
    terminal=json.loads((HERE/'terminal.json').read_text());run.update(status=terminal['status'],processed_inputs=terminal['processed_inputs'],actual_full_root_BFS=terminal['actual_full_root_BFS'])
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
