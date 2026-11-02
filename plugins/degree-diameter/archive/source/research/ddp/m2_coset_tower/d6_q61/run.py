"""Two old q41 samples, then one 2000-slot profile and bounded d6/q61 batch."""
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'q41_search'
EXE=HERE/'search'
BUDGET=180.0


def children_cpu():
    u=resource.getrusage(resource.RUSAGE_CHILDREN)
    return u.ru_utime+u.ru_stime


def main():
    start_own=time.process_time();start_children=children_cpu()
    def used():
        return time.process_time()-start_own+children_cpu()-start_children
    affinity=min(os.sched_getaffinity(0));os.sched_setaffinity(0,{affinity})
    def run(args,log,remaining):
        def limits():
            os.sched_setaffinity(0,{affinity})
            resource.setrlimit(resource.RLIMIT_CPU,(math.ceil(remaining),math.ceil(remaining)))
        before=children_cpu();wall=time.monotonic()
        with Path(log).open('w') as f:
            p=subprocess.run(list(map(str,args)),stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits)
        return dict(command=list(map(str,args)),returncode=p.returncode,cpu_seconds=children_cpu()-before,wall_seconds=time.monotonic()-wall)
    compile_result=run(['g++','-O3','-std=c++17',HERE/'search.cpp','-o',EXE],HERE/'compile.log',BUDGET-used())
    assert compile_result['returncode']==0
    def read_edges(path):
        data=list(map(int,path.read_text().split()))
        return data[:2],{tuple(data[i:i+2]) for i in range(2,len(data),2)}
    checks=[]
    for kind in ('A','B'):
        old=OLD/f'search.{kind}.best'
        expected=json.loads(old.with_suffix('.best.json').read_text())
        prefix=HERE/f'regression_{kind}'
        result=run([EXE,'check',5,41,2,*expected['S_ids'],prefix],prefix.with_suffix('.log'),BUDGET-used())
        assert result['returncode']==0
        actual=json.loads(prefix.with_suffix('.json').read_text())
        old_header,old_edges=read_edges(OLD/f'search.{kind}.best.edges')
        new_header,new_edges=read_edges(prefix.with_suffix('.edges'))
        assert old_header==new_header==[1066,2665] and old_edges==new_edges and len(new_edges)==2665
        assert actual['root_missing_leaf_block_head']==expected['root_missing_leaf_block_head']
        assert actual['bad_unordered_pairs']==expected['bad_unordered_pairs']
        checks.append(dict(old_sample=f'search.{kind}.best',exact_labelled_edge_set_match=True,
            three_root_missing=actual['root_missing_leaf_block_head'],bad_unordered_pairs=actual['bad_unordered_pairs'],run=result))
    (HERE/'preflight.json').write_text(json.dumps(dict(status='TWO_OLD_Q41_SAMPLES_MATCH',compile=compile_result,checks=checks,
        repeated_old_enumeration=False,extra_generic_full_root_checks=False),indent=2)+'\n')
    scope=dict(degree=6,q=61,r=4,m=30,n=2257,orbit_sizes=[1830,366,61],leaf_generator_count=5,
        involutions=61,noninvolutory_inverse_pairs=884,
        branches={'A1':dict(raw=390286,invalid=0,valid=390286,expected_HH_scored=289710),
                  'A0':dict(raw=25636,invalid=29,valid=25607,expected_HH_scored=12615),
                  'B':dict(raw=1564680,invalid=0,valid=1564680,expected_HH_scored=1369365)},
        all_raw=1980602,all_valid=1980573,all_expected_HH_scored=1671690,
        normalization='Only simultaneous x -> lambda*x; no inner translation conjugation',
        five_involution_family_searched=False,profile_first_raw_slots=2000,worker_count=1,cpu_budget_seconds=BUDGET,
        metrics_scope='HH-passing fully scored candidates only; no added BFS for metrics')
    (HERE/'scope.json').write_text(json.dumps(scope,indent=2)+'\n')
    print(json.dumps(dict(event='PREFLIGHT_PASSED',cpu_used=used(),planned_raw=1980602,planned_valid=1980573)),flush=True)
    remaining=BUDGET-used();assert remaining>1
    prefix=HERE/'search'
    production=run([EXE,remaining-0.5,2000,prefix],HERE/'run.log',remaining)
    if production['returncode']!=0:
        (HERE/'terminal.json').write_text(json.dumps(dict(status='EXECUTION_ERROR',production=production,cumulative_cpu_seconds=used(),automatic_restart=False),indent=2)+'\n')
        raise RuntimeError('batch failed; no restart')
    terminal=json.loads(prefix.with_suffix('.terminal.json').read_text())
    for kind,c in terminal['counts'].items():
        assert c['raw_slots_visited']==c['invalid_duplicate_pairs']+c['valid_candidates']
        assert c['valid_candidates']==c['skipped_HH']+c['fully_scored']
        assert c['fully_scored']==sum(c['score_histogram'].values())
        if terminal['status']=='COMPLETE_NO_SOLUTION':
            expected=scope['branches'][kind]
            assert (c['raw_slots_visited'],c['invalid_duplicate_pairs'],c['valid_candidates'],c['fully_scored'])==(expected['raw'],expected['invalid'],expected['valid'],expected['expected_HH_scored'])
    if terminal['status']=='COMPLETE_NO_SOLUTION':assert terminal['next_candidate_cursor']==1980602
    result=dict(scope='Only degree6 q61 r4 coset tower, A1/A0/B families',worker_count=1,cumulative_cpu_limit_seconds=BUDGET,
        cumulative_cpu_seconds=used(),preflight='preflight.json',production=production,terminal=terminal,
        profile=json.loads(prefix.with_suffix('.profile.json').read_text()) if prefix.with_suffix('.profile.json').exists() else None,
        first_head_zero_saved=prefix.with_suffix('.first_head_zero.json').exists(),independent_best_validation='pending')
    (HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
    compact={kind:{k:v for k,v in c.items() if k!='score_histogram'} for kind,c in terminal['counts'].items()}
    print(json.dumps(dict(event='TERMINAL',status=terminal['status'],cpu_seconds=used(),counts=compact,
        profile=result['profile'],best=json.loads(prefix.with_suffix('.best.json').read_text())),indent=2),flush=True)


if __name__=='__main__':
    main()
