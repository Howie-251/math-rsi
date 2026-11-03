"""Continue the complete authorized two-pair/two-involution scope from cursor 2000."""
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
assert prefix['next_candidate_cursor']==2000 and prefix['HH_pass']==2000
(HERE/'profile.run.json').write_text(json.dumps(profile_run,indent=2)+'\n')
normalization=json.loads((HERE/'normalization_inputs.json').read_text())
prior=profile_run['budget_charged_seconds'];limit=300.0

def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();runs=[]

def run(args,log):
    remaining=max(1,math.ceil(limit-prior-(cpu()-start)))
    def cap(): resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining))
    before=cpu();wall=time.monotonic()
    with (HERE/log).open('w') as output:
        child=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                               text=True,bufsize=1,preexec_fn=cap)
        for line in child.stdout:
            output.write(line);output.flush();print(line,end='',flush=True)
        returncode=child.wait()
    runs.append({'command':list(map(str,args)),'log':log,'returncode':returncode,
                 'cpu_seconds':cpu()-before,'wall_seconds':time.monotonic()-wall})
    if returncode: raise RuntimeError(f'{log}: exit {returncode}')

run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'production_search')],'production.compile.log')
remaining=limit-prior-(cpu()-start)-0.6
run([str(HERE/'production_search'),str(remaining),'38982510','2000',str(HERE/'production')],'production.log')
suffix=json.loads((HERE/'production.terminal.json').read_text())
counts={k:prefix[k]+suffix[k] for k in ['raw_visited','invalid','HH_pass','HH_skipped','BB_pass','three_root_BFS_scored']}
counts['legal']=counts['raw_visited']-counts['invalid']
counts['minimum_BB_missing']=min(prefix['minimum_BB_missing'],suffix['minimum_BB_missing'])
for name in ['BB_missing_histogram','score_histogram']:
    h=Counter(prefix[name])+Counter(suffix[name]);counts[name]=dict(sorted(h.items(),key=lambda kv:int(kv[0])))
per_branch=suffix['per_branch']
for left,right in zip(prefix['per_branch'],per_branch):
    for k in ['raw_visited','invalid','HH_pass','HH_skipped','BB_pass','three_root_BFS_scored','head_block_zero']:
        right[k]+=left[k]
    right['legal']=right['raw_visited']-right['invalid']
    for k in ['minimum_BB_missing','best_bad_pairs']:
        values=[v for v in [left[k],right[k]] if v is not None];right[k]=min(values) if values else None
    for z in range(3):
        values=[v for v in [left['minimum_root_missing'][z],right['minimum_root_missing'][z]] if v is not None]
        right['minimum_root_missing'][z]=min(values) if values else None
        right['root_zero_counts'][z]+=left['root_zero_counts'][z]
    right['complete']=right['raw_visited']==right['raw_total']
    b=right['branch']
    if b<40:
        row=normalization['type_i'][b//20]
        right['first_involution_code']=row['first_involution_code']
        right['second_involution_orbit_index']=b%20
        right['second_involution_code']=row['second_representative_codes'][b%20]
        right['expected_HH_total']=844350 if row['second_orbits'][b%20]['horizontal_class']=='BC42' else 748209
    else:
        right['first_pair_representative']=normalization['type_ii']['first_pair_representatives'][b-40]
        right['expected_HH_total']=1284696
complete=suffix['next_candidate_cursor']==41490060
if complete:
    assert counts['raw_visited']==counts['legal']==41490060
    assert counts['HH_pass']==38982510 and counts['HH_skipped']==2507550
    assert all(row['complete'] and row['HH_pass']==row['expected_HH_total'] for row in per_branch)
per_type={}
for typ in ['I','II']:
    rows=[r for r in per_branch if r['type']==typ]
    totals={k:sum(r[k] for r in rows) for k in ['raw_visited','invalid','legal','HH_pass','HH_skipped','BB_pass','three_root_BFS_scored','head_block_zero']}
    totals['root_zero_counts']=[sum(r['root_zero_counts'][z] for r in rows) for z in range(3)]
    totals['minimum_root_missing']=[min((r['minimum_root_missing'][z] for r in rows if r['minimum_root_missing'][z] is not None),default=None) for z in range(3)]
    totals['minimum_BB_missing']=min((r['minimum_BB_missing'] for r in rows if r['minimum_BB_missing'] is not None),default=None)
    totals['best_bad_pairs']=min((r['best_bad_pairs'] for r in rows if r['best_bad_pairs'] is not None),default=None)
    totals['complete']=all(r['complete'] for r in rows);per_type[typ]=totals
best_bb_file='profile.best_BB.json' if prefix['minimum_BB_missing']<=suffix['minimum_BB_missing'] else 'production.best_BB.json'
best_graph_prefix=None;postscore=None
if counts['BB_pass']:
    options=[(t['best_bad_pairs'],stem) for t,stem in [(prefix,'profile'),(suffix,'production')] if t['best_bad_pairs'] is not None]
    best_graph_prefix=min(options)[1]+'.best'
elif complete:
    best=json.loads((HERE/best_bb_file).read_text())
    run([str(HERE/'production_search'),'check',*map(str,best['S_ids']),str(HERE/'minimum_BB_scored')],'minimum_BB_scored.log')
    postscore=json.loads((HERE/'minimum_BB_scored.json').read_text());best_graph_prefix='minimum_BB_scored'
    assert postscore['BB_missing']==counts['minimum_BB_missing'] and postscore['bad_unordered_pairs']>0
status=suffix['status']
if complete and counts['BB_pass']==0: status='COMPLETE_NO_BB_CANDIDATES'
summary={'status':status,'scope':'Semilinear GF64 K=C21 semidirect C2, all normalized two noninvolutory inverse pairs plus two involutions, types I and II',
         'worker_count':1,'cumulative_cpu_limit_seconds':limit,
         'budget_charged_seconds':prior+(cpu()-start),
         'prior_profile_and_preflight_budget_seconds':prior,
         'continuation_runs':runs,'raw_total':41490060,'HH_total_from_scope':38982510,
         'prefix_cursor_interval':[0,2000],
         'continuation_cursor_interval':[2000,suffix['next_candidate_cursor']],
         'next_candidate_cursor':suffix['next_candidate_cursor'],'next_parameters':suffix['next_parameters'],
         'counts':counts,'per_type':per_type,'per_branch':per_branch,
         'first_million_observation':'production.first_million.json',
         'best_BB_parameters_file':best_bb_file,'best_graph_prefix':best_graph_prefix,
         'single_postsearch_minBB_graph_scored':postscore,
         'independent_best_graph_verification':'pending' if best_graph_prefix else None,
         'candidate_D5':suffix['status']=='CANDIDATE_D5',
         'best_full_score_scope':'Only BB-passing candidates receive full three-root BFS; rejected candidates have no claimed full-score minimum.',
         'scope_proof':'SCOPE.md','independent_input_lists':'normalization_inputs.json',
         'preflight_checks':'preflight.independent_check.json'}
(HERE/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['counts','per_branch','continuation_runs','single_postsearch_minBB_graph_scored']},indent=2),flush=True)
print(json.dumps({k:v for k,v in counts.items() if not k.endswith('_histogram')},indent=2),flush=True)
