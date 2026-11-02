"""Run only the authorized 2000-HH prefix after one independent involution preflight."""
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
prepared=json.loads((HERE/'prepare.terminal.json').read_text())
assert prepared['scope_lists_match'] and prepared['both_type_I_twenty_orbits_match_member_by_member']
if prepared['status']=='PREFLIGHT_D5_CANDIDATE': raise SystemExit('Independent acceptance of preflight D5 precedes profiling.')
independent=json.loads((HERE/'preflight.independent_check.json').read_text())
assert len(independent['sample_results'])==1
row=independent['sample_results'][0]
assert row['independently_reconstructed_edges_exactly_match']
assert row['all_saved_masks_match_BFS'] and row['BB_formula_and_BFS_match_all_targets']
verify=json.loads((HERE/'preflight.independent_verify.json').read_text())
assert verify['n']==3200 and verify['m']==11200
assert verify['min_degree']==7 and verify['max_degree']==7
assert verify['roots_checked']==3200 and verify['unreachable_unordered_pairs']==0
assert verify['bad_unordered_pairs']==prepared['sample_bad_pairs']
normalization=json.loads((HERE/'normalization_inputs.json').read_text())

def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime

start=cpu();limit=60.0
independent_cpu=independent['python_cpu_seconds']+independent['checker_cpu_seconds']
normalization_cpu=normalization['cpu_seconds']
prior=prepared['cumulative_cpu_seconds']+independent_cpu+normalization_cpu
remaining=limit-prior-0.5
def cap():
    hard=max(1,math.ceil(remaining));resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
args=[str(HERE/'search'),str(remaining),'2000','0',str(HERE/'profile')]
wall=time.monotonic()
with (HERE/'profile.log').open('w') as output:
    result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
elapsed=time.monotonic()-wall
if result.returncode: raise RuntimeError(f'profile exit {result.returncode}; see profile.log')
terminal=json.loads((HERE/'profile.terminal.json').read_text())
metadata={
    'group_engine':'engine.hpp, same checked semilinear multiplication/inverse as d7_f64_semilinear; legality now requires exactly two nonidentity involutions',
    'group_product':'(x,a,e)*(y,b,f)=(x+r^a*y^(8^e), a+8^e*b mod21,e+f mod2)',
    'inverse':'(r^(-8^e*a)*x^(8^e), -8^e*a mod21,e)',
    'field_polynomial_binary':67,'r_encoding':8,'r_order':21,
    'encoding':'x+64*(a+21e)','layer_sizes':[2688,448,64],
    'normalization_proof':'SCOPE.md','independent_machine_scope':'normalization_inputs.json',
    'actual_machine_scope':'generated_scope.json','all_representatives_and_orbit_members_matched':True,
    'type_I':{'first_involutions':[[1,0,0],[1,0,1]],
              'second_involution_representatives':'20 Frobenius2 orbits for each first, each represented by minimum encoded id; full orbit members retained',
              'other_pairs':'all unordered distinct pairs from 1300 true inverse pairs',
              'raw_total':33774000,'HH_total':31274334},
    'type_II':{'involutions':'all unordered distinct choices from the 45 actual non-A21 involutions',
               'first_pair_representatives':normalization['type_ii']['first_pair_representatives'],
               'other_pair':'all 1299 true inverse pairs excluding the fixed first pair',
               'raw_total':7716060,'HH_total':7708176},
    'raw_total':41490060,'HH_total':38982510,
    'enumeration_order':'TypeI: first involution index, second orbit index, pair j<k. Then TypeII: first pair branch, involution j<k, other pair index in 1299-list.',
    'Frobenius_map':'(x,a,e)->(x^2,2a mod21,e)',
    'no_arbitrary_field_scaling_or_extra_reduction':True,
    'filters':['actual HH orbit coverage','exact HW3H union KW1H union HW1K','actual three-root BFS'],
    'profile_HH_target':2000,'profile_prefix_is_not_unbiased_sample':True,
    'full_production_started':False,'stop_on_actual_D5':True,
    'one_involution_preflight_only':True,'old_preflights_repeated':False
}
(HERE/'profile_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
summary={'status':terminal['status'],'worker_count':1,'cumulative_cpu_limit_seconds':limit,
         'prepare_cpu_seconds':prepared['cumulative_cpu_seconds'],
         'independent_sample_cpu_seconds':independent_cpu,
         'independent_normalization_cpu_seconds':normalization_cpu,
         'profile_process_and_driver_cpu_seconds':cpu()-start,
         'budget_charged_seconds':prior+(cpu()-start),
         'profile_command':args,'profile_returncode':result.returncode,'profile_wall_seconds':elapsed,
         'independent_sample':'preflight.independent_check.json',
         'profile_metadata':'profile_metadata.json','terminal':terminal,
         'continued_beyond_profile':False}
(HERE/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in terminal.items() if k not in ['per_branch','BB_missing_histogram','score_histogram']},indent=2))
print('budget_charged_seconds',summary['budget_charged_seconds'])
