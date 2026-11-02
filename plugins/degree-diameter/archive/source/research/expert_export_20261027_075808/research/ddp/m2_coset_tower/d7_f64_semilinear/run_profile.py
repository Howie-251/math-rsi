"""Require the two independent new-group preflights, then stop at 2000 HH passes."""
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
prepare=json.loads((HERE/'prepare.terminal.json').read_text())
if prepare['status']=='PREFLIGHT_D5_CANDIDATE':
    raise SystemExit('Preflight found D5: independent candidate acceptance precedes any profile.')
checks=[]
for row in prepare['samples']:
    j=row['sample_index']
    v=json.loads((HERE/f'preflight_{j}.independent_verify.json').read_text())
    assert v['n']==3200 and v['m']==11200
    assert v['min_degree']==7 and v['max_degree']==7
    assert v['roots_checked']==3200 and v['unreachable_unordered_pairs']==0
    assert v['bad_unordered_pairs']==row['three_root_bad_pairs']
    checks.append({'sample_index':j,'file':f'preflight_{j}.independent_verify.json',
                   'diameter':v['diameter'],'bad_unordered_pairs':v['bad_unordered_pairs'],
                   'checker_seconds':v['seconds']})
# The source agent's independent new-group edge reconstruction is separately recorded.
edge_check=json.loads((HERE/'preflight.independent_check.json').read_text())
assert edge_check['status']=='COMPLETE_TWO_SAVED_SAMPLES_NO_SEARCH'
assert len(edge_check['sample_results'])==2
for row in edge_check['sample_results']:
    assert row['independently_reconstructed_edges_exactly_match']
    assert row['all_saved_masks_match_BFS']
    assert row['BB_formula_and_BFS_match_all_targets']

def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime

start=cpu();prior=prepare['cumulative_cpu_seconds'];limit=60.0
# Charge the independently recorded Python and checker CPU to the same budget.
independent_time=edge_check['python_cpu_seconds']+edge_check['checker_cpu_seconds']
remaining=limit-prior-independent_time-0.5
def cap():
    hard=max(1,math.ceil(remaining))
    resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
args=[str(HERE/'search'),str(remaining),'2000','0',str(HERE/'profile')]
wall=time.monotonic()
with (HERE/'profile.log').open('w') as output:
    result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
elapsed=time.monotonic()-wall
if result.returncode:
    raise RuntimeError(f'profile exit {result.returncode}; see profile.log')
terminal=json.loads((HERE/'profile.terminal.json').read_text())
metadata={
    'field':'F2[t]/(t^6+t+1)','polynomial_binary':67,'r':8,'r_order':21,
    'Frobenius_exponent':8,'K_order':42,'H_order':6,
    'group_product':'(x,a,e)*(y,b,f)=(x+r^a*y^(8^e),a+8^e*b mod21,e+f mod2)',
    'group_inverse':'(x,a,e)^-1=(r^(-8^e*a)*x^(8^e),-8^e*a mod21,e)',
    'encoding':'x+64*(a+21*e)','layer_sizes':[2688,448,64],
    'first_representatives':[[1,1,0],[1,1,1],[1,3,0],[1,3,1],[1,7,0],[1,7,1]],
    'normalization_proof':'NORMALIZATION.md',
    'normalization':'Choose an A21 pair required by HH; genuine K rotation conjugation normalizes its x to1 and changes a for e=1; Frobenius and inversion give a in1,3,7.',
    'inverse_pairs_file':'profile.inverse_pairs.json','inverse_pairs_count':1300,
    'inverse_pair_class_counts':{'zero_x':19,'A21':420,'BC42':861},
    'other_pairs_include_noninvolutory_a0_e1':True,
    'pair_table_order':'ascending encoded id g with g<actual_semilinear_inverse(g)',
    'input_order':'first branch outer, then j<k in the ascending pair table with the first pair removed',
    'inputs_per_first_branch':843051,'raw_total':5058306,
    'HH_pass_per_first_branch':747348,'HH_total':4484088,
    'all_other_two_pairs_are_distinct_and_different_from_first':True,
    'filters':['exact K-orbit HH','exact HW3H union KW1H union HW1K BB','ordinary actual-graph three-root BFS'],
    'no_cyclic_group_inverse_or_center_quotient_used':True,
    'profile_HH_target':2000,'full_search_authorized_in_this_run':False,
    'stop_on_actual_three_root_D5':True
}
(HERE/'profile_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
summary={'status':terminal['status'],'worker_count':1,'cumulative_cpu_limit_seconds':limit,
         'prepare_cpu_seconds':prior,'profile_process_cpu_seconds':cpu()-start,
         'cumulative_local_cpu_seconds':prior+(cpu()-start),
         'independent_checker_time_reserved_seconds':independent_time,
         'budget_charged_seconds':prior+(cpu()-start)+independent_time,
         'profile_command':args,'profile_returncode':result.returncode,'profile_wall_seconds':elapsed,
         'preflight_checks':checks,'independent_edge_reconstruction':'preflight.independent_check.json',
         'profile_metadata':'profile_metadata.json','terminal':terminal,
         'continued_beyond_profile':False}
(HERE/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in terminal.items() if k not in ['BB_missing_histogram','score_histogram','per_first_branch']},indent=2))
print('budget_charged_seconds',summary['budget_charged_seconds'])
