"""Continue the authorized quotient frontend from the original saved cursor."""
from collections import Counter
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
profile_run=json.loads((HERE/'run_profile.terminal.json').read_text())
prefix=profile_run['terminal']
prior_cpu=profile_run['cumulative_cpu_seconds']
assert prefix['next_candidate_cursor']==12386
assert prefix['HH_pass']==2000
assert prefix['BH_full_pass']==0
limit=180.0


def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime


start=cpu()
runs=[]


def run(args,log):
    remaining=max(1,math.ceil(limit-prior_cpu-(cpu()-start)))
    def child_limit():
        resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining))
    before=cpu()
    wall=time.monotonic()
    with (HERE/log).open('w') as output:
        result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=child_limit)
    runs.append({'command':list(map(str,args)),'log':log,'returncode':result.returncode,
                 'cpu_seconds':cpu()-before,'wall_seconds':time.monotonic()-wall})
    if result.returncode:
        raise RuntimeError(f'{log}: exit {result.returncode}')


run(['g++','-O3','-std=c++17',str(HERE/'profile.cpp'),'-o',str(HERE/'frontend')], 'frontend.compile.log')
remaining=limit-prior_cpu-(cpu()-start)-0.5
run([str(HERE/'frontend'),str(remaining),'5693310',str(prefix['next_candidate_cursor']),str(HERE/'frontend')], 'frontend.log')
suffix=json.loads((HERE/'frontend.terminal.json').read_text())
combined={k:prefix[k]+suffix[k] for k in [
    'raw_visited','HH_pass','HH_skipped','BB_pass','BH_full_pass',
    'block_root_zero_among_BB_pass','head_root_zero_among_BB_pass']}
combined['minimum_BB_missing']=min(prefix['minimum_BB_missing'],suffix['minimum_BB_missing'])
hist=Counter(prefix['BB_missing_histogram'])+Counter(suffix['BB_missing_histogram'])
combined['BB_missing_histogram']=dict(sorted(hist.items(),key=lambda kv:int(kv[0])))
per_y=suffix['per_y']
# The original prefix was entirely y=0, so no arbitrary allocation is needed.
assert prefix['next_parameters']['y']==0
for key in ['raw_visited','HH_pass','HH_skipped','BB_pass','BH_full_pass',
            'block_root_zero_among_BB_pass','head_root_zero_among_BB_pass']:
    per_y['0'][key]+=prefix[key]
old=per_y['0']['minimum_BB_missing']
per_y['0']['minimum_BB_missing']=min(prefix['minimum_BB_missing'],449 if old is None else old)
for values in per_y.values():
    values['complete']=values['raw_visited']==values['raw_total_for_y']
complete=suffix['next_candidate_cursor']==prefix['raw_total']
if complete:
    assert combined['raw_visited']==13127680
    assert combined['HH_pass']==5693310
    assert all(row['complete'] for row in per_y.values())
    status='COMPLETE_NO_BH_CANDIDATES' if combined['BH_full_pass']==0 else 'COMPLETE_BH_CANDIDATES_REQUIRE_LIFT_CHECK'
else:
    status=suffix['status']
result={'status':status,'scope':'All normalized F64 C42 two-pair/two-involution projections; quotient HH, BB and fixed-root BH tests only',
        'worker_count':1,'cumulative_cpu_limit_seconds':limit,
        'cumulative_cpu_seconds':prior_cpu+(cpu()-start),
        'prior_profile_cpu_seconds':prior_cpu,'continuation_runs':runs,
        'raw_total':13127680,'HH_total_from_scope':5693310,
        'prefix_cursor_interval':[0,12386],
        'continuation_cursor_interval':[12386,suffix['next_candidate_cursor']],
        'next_candidate_cursor':suffix['next_candidate_cursor'],
        'next_parameters':suffix['next_parameters'],
        'counts':combined,'per_y':per_y,
        'best_BB_parameters_file':'profile.best_BB.json' if prefix['minimum_BB_missing']<=suffix['minimum_BB_missing'] else 'frontend.best_BB.json',
        'BH_survivors_file':'frontend.BH_survivors.jsonl',
        'legal_lift_constraints':'Four parity variables, bit order inv1/invy/pair_a/pair_b; p=i mod2, y=0 forces invy=1, y=1 requires inv1!=invy, repeated pair projections require different pair bits',
        'C42_lift_assignments_checked':0,
        'BB_failures_prove_original_D5_failure':True,
        'BH_pass_is_not_D5_acceptance':True}
(HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['counts','per_y','continuation_runs']},indent=2))
print(json.dumps({k:v for k,v in combined.items() if k!='BB_missing_histogram'},indent=2))
