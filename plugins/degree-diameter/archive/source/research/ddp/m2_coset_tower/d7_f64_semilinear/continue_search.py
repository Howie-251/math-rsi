"""Continue the same six-branch scope without repeating the 2000-HH profile."""
from collections import Counter
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
profile_run=json.loads((HERE/'terminal.json').read_text())
prefix=profile_run['terminal']
assert prefix['status']=='PROFILE_COMPLETE_STOPPED'
assert prefix['next_candidate_cursor']==2437 and prefix['HH_pass']==2000
(HERE/'profile.run.json').write_text(json.dumps(profile_run,indent=2)+'\n')
prior=profile_run['budget_charged_seconds'];limit=180.0

def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();runs=[]

def run(args,log):
    remaining=max(1,math.ceil(limit-prior-(cpu()-start)))
    def cap(): resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining))
    before=cpu();wall=time.monotonic()
    with (HERE/log).open('w') as output:
        result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
    runs.append({'command':list(map(str,args)),'log':log,'returncode':result.returncode,
                 'cpu_seconds':cpu()-before,'wall_seconds':time.monotonic()-wall})
    if result.returncode: raise RuntimeError(f'{log}: exit {result.returncode}')

remaining=limit-prior-0.5
run([str(HERE/'search'),str(remaining),'4484088','2437',str(HERE/'production')],'production.log')
suffix=json.loads((HERE/'production.terminal.json').read_text())
counts={k:prefix[k]+suffix[k] for k in ['raw_visited','invalid','HH_pass','HH_skipped','BB_pass','three_root_BFS_scored']}
counts['legal']=counts['raw_visited']-counts['invalid']
counts['minimum_BB_missing']=min(prefix['minimum_BB_missing'],suffix['minimum_BB_missing'])
for histkey in ['BB_missing_histogram','score_histogram']:
    h=Counter(prefix[histkey])+Counter(suffix[histkey])
    counts[histkey]=dict(sorted(h.items(),key=lambda kv:int(kv[0])))
per_branch=suffix['per_first_branch']
for left,right in zip(prefix['per_first_branch'],per_branch):
    for k in ['raw_visited','invalid','HH_pass','HH_skipped','BB_pass','three_root_BFS_scored','head_block_zero']:
        right[k]+=left[k]
    right['legal']=right['raw_visited']-right['invalid']
    for k in ['minimum_BB_missing','best_bad_pairs']:
        values=[v for v in [left[k],right[k]] if v is not None]
        right[k]=min(values) if values else None
    for z in range(3):
        values=[v for v in [left['minimum_root_missing'][z],right['minimum_root_missing'][z]] if v is not None]
        right['minimum_root_missing'][z]=min(values) if values else None
        right['root_zero_counts'][z]+=left['root_zero_counts'][z]
    right['raw_total']=843051
    right['complete']=right['raw_visited']==843051
complete=suffix['next_candidate_cursor']==5058306
if complete:
    assert counts['raw_visited']==5058306 and counts['legal']==5058306
    assert counts['HH_pass']==4484088 and counts['HH_skipped']==574218
    assert all(row['complete'] for row in per_branch)
best_bb_file='profile.best_BB.json' if prefix['minimum_BB_missing']<=suffix['minimum_BB_missing'] else 'production.best_BB.json'
best_graph_prefix=None
postscore=None
if counts['BB_pass']:
    candidates=[(t['best_bad_pairs'],stem) for t,stem in [(prefix,'profile'),(suffix,'production')] if t['best_bad_pairs'] is not None]
    best_graph_prefix=min(candidates)[1]+'.best'
elif complete:
    best=json.loads((HERE/best_bb_file).read_text())
    S=best['S_ids']
    run([str(HERE/'search'),'check',str(S[0]),str(S[2]),str(S[4]),str(HERE/'minimum_BB_scored')],'minimum_BB_scored.log')
    postscore=json.loads((HERE/'minimum_BB_scored.json').read_text())
    best_graph_prefix='minimum_BB_scored'
    assert postscore['BB_missing']==counts['minimum_BB_missing']
    assert postscore['bad_unordered_pairs']>0
status=suffix['status']
if complete and counts['BB_pass']==0: status='COMPLETE_NO_BB_CANDIDATES'
result={'status':status,'scope':'Semilinear GF64 K=C21 semidirect C2, three noninvolutory inverse pairs, six normalized first generators',
        'worker_count':1,'cumulative_cpu_limit_seconds':limit,
        'budget_charged_seconds':prior+(cpu()-start),
        'prior_profile_and_preflight_budget_seconds':prior,
        'continuation_runs':runs,'raw_total':5058306,'HH_total_from_scope':4484088,
        'prefix_cursor_interval':[0,2437],
        'continuation_cursor_interval':[2437,suffix['next_candidate_cursor']],
        'next_candidate_cursor':suffix['next_candidate_cursor'],'next_parameters':suffix['next_parameters'],
        'counts':counts,'per_first_branch':per_branch,
        'best_BB_parameters_file':best_bb_file,'best_graph_prefix':best_graph_prefix,
        'single_postsearch_minBB_graph_scored':postscore,
        'independent_best_graph_verification':'pending' if best_graph_prefix else None,
        'candidate_D5':suffix['status']=='CANDIDATE_D5',
        'preflight_checks':'preflight.independent_check.json',
        'scope_proof':'NORMALIZATION.md'}
(HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['counts','per_first_branch','continuation_runs','single_postsearch_minBB_graph_scored']},indent=2))
print(json.dumps({k:v for k,v in counts.items() if not k.endswith('_histogram')},indent=2))
if postscore: print('postscore',postscore['root_missing_leaf_block_head'],postscore['bad_unordered_pairs'])
