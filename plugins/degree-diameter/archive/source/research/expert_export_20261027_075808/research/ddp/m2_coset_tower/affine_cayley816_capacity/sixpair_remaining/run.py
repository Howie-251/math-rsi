#!/usr/bin/env python3
from pathlib import Path
import json
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent
assert not (HERE/'run.json').exists(), 'One authorized production process; do not restart.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();wall=time.monotonic()
old=json.loads((SOURCE/'maximin_production/inputs.json').read_text())
old_terminal=json.loads((SOURCE/'maximin_production/terminal.json').read_text())
assert old_terminal['patterns_completed']==76 and old_terminal['processed_inputs']==46500312
excluded={r['source_cursor']for r in old if r['pairs']==6}
assert len(excluded)==48
selected=[];all_six=0
for line in (SOURCE/'survivors.jsonl').open():
    row=json.loads(line)
    if row['pair_count']==6:
        all_six+=1
        if row['cursor']not in excluded:selected.append(row)
assert all_six==50728 and len(selected)==50680
selected.sort(key=lambda r:(-r['minimum_symbolic_capacity'],r['cursor']))
assert all(r['minimum_symbolic_capacity']<26 for r in selected)
assert len({r['cursor']for r in selected})==len(selected)
assert sum(r['projective_marked_inputs']for r in selected)==4497393880
hist={};anchor_hist={};contains_zero=contains_kernel=contains_repeat=0
with (HERE/'inputs.txt').open('w')as text,(HERE/'inputs.jsonl').open('w')as detail:
    text.write('50680\n')
    for index,row in enumerate(selected):
        phases=row['pair_phases'];anchor=row['anchor_component']
        assert row['field_variables']==6 and row['involution_count']==0
        assert row['projective_marked_inputs']==88741 and pow(3,phases[anchor],17)!=1
        assert anchor==next(j for j,x in enumerate(phases)if pow(3,x,17)!=1)
        counts=row['symbolic_capacity'];assert min(counts)>=17
        text.write(' '.join(map(str,[row['cursor'],anchor]+phases+counts))+'\n')
        detail.write(json.dumps({'pattern_index':index,'source_cursor':row['cursor'],'pair_phases':phases,'anchor_component':anchor,'minimum_form_count':row['minimum_symbolic_capacity'],'capacity_by_phase':counts,'projective_scope':88741})+'\n')
        h=row['minimum_symbolic_capacity'];hist[h]=hist.get(h,0)+1
        anchor_hist[anchor]=anchor_hist.get(anchor,0)+1
        contains_zero+=0 in phases;contains_kernel+=16 in phases;contains_repeat+=len(set(phases))<6
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start
source_prep=json.loads((HERE/'source_preparation.json').read_text())['CPU_seconds']
remaining=600-prep-source_prep-5
assert remaining>0
metadata={'group':'F17 semidirect_3 C48','n':816,'degree':12,'target_D':3,'pair_count':6,'involution_count':0,'patterns':50680,'per_pattern_scope':88741,'raw_scope':4497393880,'order':'minimum form count descending, then source cursor ascending; leading nonzero position ascending, tail lexicographic','excluded_previously_complete_source_cursors':sorted(excluded),'minimum_form_count_histogram':hist,'anchor_component_histogram':anchor_hist,'patterns_containing_phase0':contains_zero,'patterns_containing_phase16':contains_kernel,'patterns_with_repeated_pair_phase':contains_repeat,'normalization':'one nonunit-action anchor field0, then remaining5-dimensional vector leading nonzero1; no further normalization','preparation':'C++ builds complete reduced-word symbolic forms only for current mode; check all48 counts against saved capacity, delete true anchor column, deduplicate, sort fibers by count/phase','actual_rejection':'generic12-element legality; then actual fiber values, strict duplicate losses > m-17; full root BFS only after all48 fibers cover','CPU_budget_seconds':600,'worker_count':1,'preparation_CPU_seconds':prep,'source_preparation_CPU_seconds':source_prep,'production_CPU_limit_seconds':remaining,'shutdown_reserve_seconds':5,'first100000':'part of formal cursor; no restarted profiling pass','other_branches':'five/four pairs untouched; previous48 six-pair modes excluded','previous_sixpair_rate_CPU_seconds':0.75205,'previous_sixpair_rate_marked_inputs':4259568,'old_rate_full_scope_estimate_CPU_seconds':0.75205/4259568*4497393880,'best_graph_policy':'save only D3 through-case; no fallback when zero through'}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
run={'status':'RUNNING','running':True,'worker_count':1,'CPU_budget_seconds':600,'raw_scope':4497393880,'driver_pid':os.getpid(),'preparation_CPU_seconds':prep,'source_preparation_CPU_seconds':source_prep,'production_CPU_limit_seconds':remaining}
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (HERE/'production.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
    code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start+source_prep,wall_seconds=time.monotonic()-wall,restarts=0)
if code==0:
    terminal=json.loads((HERE/'terminal.json').read_text())
    run.update(status=terminal['status'],processed_inputs=terminal['processed_inputs'],patterns_completed=terminal['patterns_completed'],actual_full_root_BFS=terminal['actual_full_root_BFS'],saved_best_graph=terminal['saved_best_graph'])
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
