#!/usr/bin/env python3
"""Compare a refined route prediction with already saved measurements."""
from collections import Counter,defaultdict
import csv
import json
from pathlib import Path
import resource

resource.setrlimit(resource.RLIMIT_CPU,(2,2))
started=resource.getrusage(resource.RUSAGE_SELF)
base=Path(__file__).resolve().parent
assert not (base/'LOOP_ROUTE_STRATA_RESULT.json').exists()
repo=next(p for p in base.parents if (p/'formal').is_dir() and (p/'research-wiki').is_dir())
old=json.loads((repo/'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PORT_R2.json').read_text())
old_r2=set(next(row['R2'] for row in old if row['port']==0))
params=json.loads((base/'PARAMETERS.json').read_text())
b_neighbors=set(map(int,(repo/params['source_B']).read_text().splitlines()[0].split()))
with (base/'ORDERED_LABEL_RECIPE.tsv').open() as f:
    recipes={int(r['label']):r for r in csv.DictReader(f,delimiter='\t')}
expected={'far':(8960,0,7,7),'B_distance2':(960,3,3,18),
    'R':(120,1,56,61),'F_over_b0':(20,24,56,176),'other_freed_U_over_b0':(10,24,72,192)}
observed=defaultdict(Counter);failed=[]
with (base/'FRACTIONAL_ALL_TARGET_COUNTS.tsv').open() as f:
    for row in csv.DictReader(f,delimiter='\t'):
        v=int(row['target']);rec=recipes[v]
        if rec['kind'] in ('old_center','clone') and int(rec['class_b_label'])==0:
            kind='F_over_b0'
        elif v>=8775:
            kind='far'
        else:
            y=v%585
            if y==0: kind='other_freed_U_over_b0'
            elif y in b_neighbors: kind='R'
            elif y in old_r2: kind='B_distance2'
            else: kind='far'
        measured=tuple(int(row[k]) for k in ('closed_B1_R','closed_B2_R','coverage_numerator_over7'))
        observed[kind][measured]+=1
        if measured!=expected[kind][1:]:
            failed.append({'target':v,'stratum':kind,'actual':list(measured),'expected':expected[kind][1:]})
checks={k:observed[k]==Counter({e[1:]:e[0]}) for k,e in expected.items()}
r=resource.getrusage(resource.RUSAGE_SELF)
used=r.ru_utime+r.ru_stime-started.ru_utime-started.ru_stime
previous=json.loads((base/'FRACTIONAL_WITNESS_RESULT.json').read_text())
full_witness=all(previous['checks'][k] for k in ['R_count120','R_all_exact_spare1',
    'all10070_full_LP_coverage_numerator_at_least7','per_helper_fractional_pin_budget','per_pin_fractional_load'])
result={'status':'ALL_REFINED_STRATUM_PREDICTIONS_MATCH' if all(checks.values()) else 'REFINED_PREDICTION_REFUTED',
    'prediction':'LOOP_ROUTE_STRATA_PREDICTION.md','checks':checks,
    'actual_strata':{k:[{'one':a,'two':b,'numerator':c,'targets':count}
        for (a,b,c),count in sorted(v.items())] for k,v in observed.items()},
    'mismatches':failed,'first_own_B2_ge7_prediction':'REFUTED_RETAINED',
    'full_rational_LP_witness_valid':full_witness,'integer_solution_proved':False,
    'CPU_seconds':used,'combined_original_model_CPU_seconds':previous['combined_original_model_CPU_seconds']+used,
    'original_CPU_budget':120,'data_reuse_only':True,'new_graph_traversals_or_solver_runs':0,
    'old585_R2_recomputed':False,'portfolio_parameter_Lean_increment':[0,0,0]}
(base/'LOOP_ROUTE_STRATA_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(base/'MODEL_BATCH_RESULT.json').write_text(json.dumps({
    'status':'FULL_INTEGER_MODEL_UNKNOWN_EXACT_FRACTIONAL_WITNESS_AND_ROUTE_STRATA_SUPPORTED'
        if all(checks.values()) and full_witness else 'MODEL_UNKNOWN_DIAGNOSTIC_SCOPE_REQUIRES_READING',
    'all_processes_terminal':True,'full_MILP_attempts':1,'full_MILP_CPU_seconds':previous['previous_full_MILP_CPU_seconds'],
    'fractional_witness_CPU_seconds':previous['CPU_seconds'],'saved_data_strata_CPU_seconds':used,
    'combined_model_CPU_seconds':result['combined_original_model_CPU_seconds'],
    'original_CPU_budget':120,'new_solver_after_timeout':False,
    'first_own_radius2_prediction_refuted':True,'full_exact_rational_LP_witness_valid':full_witness,
    'refined_strata_all_match':all(checks.values()),'no_integer_pins_or10076_graph':True,
    'whole_parameter_or_mechanism_excluded':False,'automatic_repeat_or_second_pattern':False,
    'portfolio_parameter_Lean_increment':[0,0,0]},indent=2)+'\n')
print(json.dumps(result))
