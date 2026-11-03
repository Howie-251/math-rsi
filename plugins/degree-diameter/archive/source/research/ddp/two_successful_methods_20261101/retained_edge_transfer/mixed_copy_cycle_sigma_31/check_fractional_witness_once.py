#!/usr/bin/env python3
"""Check one exact rational witness inside the unused original CPU budget."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from collections import Counter, defaultdict
import json
from pathlib import Path
import resource

resource.setrlimit(resource.RLIMIT_CPU,(5,5))
start=resource.getrusage(resource.RUSAGE_SELF)
import numpy as np
base=Path(__file__).resolve().parent
assert not (base/'FRACTIONAL_WITNESS_RESULT.json').exists()
previous=json.loads((base/'MILP_TERMINAL.json').read_text())
assert previous['all_processes_terminal'] and not previous['feasible_pins_saved']
inp=np.load(base/'G0_INPUT.npz')
offset=inp['indptr']; ids=inp['indices']; n=int(inp['n'])
pool=inp['pool']; spare=inp['spare']; capacities=dict(zip(map(int,pool),map(int,spare)))
params=json.loads((base/'PARAMETERS.json').read_text())
root=Path(__file__).resolve().parents[4]
# The producer's repository-relative source path is bound in PARAMETERS.
repo=next(p for p in base.parents if (p/'formal').is_dir() and (p/'research-wiki').is_dir())
b0_neighbors=list(map(int,(repo/params['source_B']).read_text().splitlines()[0].split()))
R={585*x+y for x in range(15) for y in b0_neighbors}
adj=[set(map(int,ids[offset[v]:offset[v+1]])) for v in range(n)]
port_set=set(params['B_absolute_labels'])
hist=defaultdict(Counter)
min_two=n; min_num=n*6; own_fail=[]; model_fail=[]
with (base/'FRACTIONAL_ALL_TARGET_COUNTS.tsv').open('w') as out:
    out.write('target\tkind\tclosed_B1_R\tclosed_B2_R\tcoverage_numerator_over7\n')
    for v in range(n):
        one=(adj[v]|{v})&R
        two=set(one)
        for w in adj[v]:
            two.update(adj[w]&R)
        a,b=len(one),len(two)
        numerator=b+5*a
        is_F=v>=8775 or (v//585<5 and v%585 in port_set)
        kind='F' if is_F else ('freed_U' if capacities.get(v)==1 else 'saturated_U')
        hist[kind][b]+=1
        min_two=min(min_two,b);min_num=min(min_num,numerator)
        if b<7:own_fail.append(v)
        if numerator<7:model_fail.append(v)
        out.write(f'{v}\t{kind}\t{a}\t{b}\t{numerator}\n')
r=resource.getrusage(resource.RUSAGE_SELF)
used=r.ru_utime+r.ru_stime-start.ru_utime-start.ru_stime
checks={'R_count120':len(R)==120,'R_all_exact_spare1':all(capacities.get(v)==1 for v in R),
    'all10070_own_B2_count_at_least7':not own_fail,
    'all10070_full_LP_coverage_numerator_at_least7':not model_fail,
    'per_helper_fractional_pin_budget':120<=26*7,
    'per_pin_fractional_load':6<=7,
    'original120CPU_not_reset':previous['child_CPU_seconds']+used<=120}
result={'status':'EXACT_RATIONAL_FULL_MODEL_LP_WITNESS_PASS' if all(checks.values())
    else 'ONE_OR_MORE_PREDICTIONS_REFUTED','checks':checks,'R_labels':sorted(R),
    'rational_assignment':'x[h,u]=1/7 for h0..5,u in R; otherwise0',
    'old_targets_checked':n,'min_own_B2_R_count':min_two,'min_full_numerator_over7':min_num,
    'own_prediction_failed_targets':own_fail,'full_LP_failed_targets':model_fail,
    'B2_count_histogram_by_target_kind':{k:dict(sorted(v.items())) for k,v in hist.items()},
    'CPU_seconds':used,'diagnostic_CPU_budget':5,
    'previous_full_MILP_CPU_seconds':previous['child_CPU_seconds'],
    'combined_original_model_CPU_seconds':previous['child_CPU_seconds']+used,
    'original_CPU_budget':120,'new_solver_runs':0,'new_integer_solution':False,
    'portfolio_parameter_Lean_increment':[0,0,0],
    'old585_BFS_R2_Steiner_field_Lean_retests':0}
(base/'FRACTIONAL_WITNESS_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(base/'FRACTIONAL_WITNESS_TERMINAL.json').write_text(json.dumps({'status':result['status'],
    'all_processes_terminal':True,'CPU_seconds':used,'combined_original_model_CPU_seconds':
    result['combined_original_model_CPU_seconds'],'original_CPU_budget':120,
    'no_MILP_restart':True,'portfolio_parameter_Lean_increment':[0,0,0]},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','min_own_B2_R_count',
    'min_full_numerator_over7','CPU_seconds','combined_original_model_CPU_seconds']}))
