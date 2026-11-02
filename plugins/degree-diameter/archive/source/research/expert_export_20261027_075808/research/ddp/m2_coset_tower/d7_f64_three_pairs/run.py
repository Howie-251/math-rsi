"""Two expanded GF64 samples, then one 2000-slot profile and bounded batch."""
from pathlib import Path
import json
import math
import os
import resource
import shutil
import subprocess
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
EXE=HERE/'search'
BUDGET=180.0


def mul(a,b):
    value=0
    while b:
        if b&1:value^=a
        b>>=1;a<<=1
        if a&64:a^=0x43
    return value


def children_cpu():
    usage=resource.getrusage(resource.RUSAGE_CHILDREN)
    return usage.ru_utime+usage.ru_stime


def main():
    own_start=time.process_time();child_start=children_cpu()
    def used():return time.process_time()-own_start+children_cpu()-child_start
    affinity=min(os.sched_getaffinity(0));os.sched_setaffinity(0,{affinity})
    def run(args,log,remaining):
        def limits():
            os.sched_setaffinity(0,{affinity})
            resource.setrlimit(resource.RLIMIT_CPU,(math.ceil(remaining),math.ceil(remaining)))
        before=children_cpu();wall=time.monotonic()
        with Path(log).open('w') as f:
            proc=subprocess.run(list(map(str,args)),stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits)
        return dict(command=list(map(str,args)),returncode=proc.returncode,cpu_seconds=children_cpu()-before,wall_seconds=time.monotonic()-wall)
    compilation=run(['g++','-O3','-std=c++17',HERE/'search.cpp','-o',EXE],HERE/'compile.log',BUDGET-used())
    assert compilation['returncode']==0
    powers=[1]
    for _ in range(41):powers.append(mul(powers[-1],8))
    assert powers[21]==1 and len(set(powers))==21
    orbit={};g=1
    for k in range(63):
        assert g not in orbit;orbit[g]=k%3;g=mul(g,2)
    assert g==1 and len(orbit)==63
    inverse=[mul(powers[-(a//64)%42],a%64)+64*(-(a//64)%42) for a in range(2688)]
    def product(a,b):return (a%64)^mul(powers[a//64],b%64) | (64*((a//64+b//64)%42))
    assert all(product(a,inverse[a])==product(inverse[a],a)==0 for a in range(2688))
    pairs=[[],[],[]];zero_pairs=[]
    for a in range(1,2688):
        if a<inverse[a]:
            if a%64:pairs[orbit[a%64]].append(a)
            else:zero_pairs.append(a)
    assert [len(p) for p in pairs]==[420,420,420] and len(zero_pairs)==20
    checks=[]
    for index,(first_i,j,k) in enumerate(((1,0,0),(7,123,321))):
        a=1+64*first_i;b=pairs[1][j];c=pairs[2][k]
        S=[a,inverse[a],b,inverse[b],c,inverse[c]]
        prefix=HERE/f'preflight_{index}'
        check=run([EXE,'check',*S,prefix],prefix.with_suffix('.log'),BUDGET-used())
        assert check['returncode']==0
        data=list(map(int,prefix.with_suffix('.edges').read_text().split()))
        assert data[:2]==[3200,11200]
        edges={tuple(data[z:z+2]) for z in range(2,len(data),2)}
        expected=set()
        for u in range(2688):
            for s in S:expected.add(tuple(sorted((u,product(u,s)))))
            expected.add((u,2688+u%64+64*((u//64)%7)))
        for block in range(448):expected.add((2688+block,3136+block%64))
        assert len(edges)==11200 and edges==expected
        score=json.loads(prefix.with_suffix('.json').read_text())
        verification=run([ROOT/'computations/ddp/verify_graph',prefix.with_suffix('.edges'),7,5],
                         prefix.with_suffix('.generic_verify.json'),BUDGET-used())
        assert verification['returncode'] in (0,1)
        verified=json.loads(prefix.with_suffix('.generic_verify.json').read_text())
        assert verified['n']==verified['roots_checked']==3200 and verified['m']==11200
        assert verified['min_degree']==verified['max_degree']==7 and verified['unreachable_unordered_pairs']==0
        assert verified['bad_unordered_pairs']==score['bad_unordered_pairs']
        checks.append(dict(first_i=first_i,pair_indices=[j,k],S_ids=S,exact_expanded_edge_set_match=True,
            root_missing=score['root_missing_leaf_block_head'],generic_result=verified,build_run=check,verification_run=verification))
        if score['bad_unordered_pairs']==0:
            shutil.copyfile(prefix.with_suffix('.edges'),HERE/'search.best.edges')
            shutil.copyfile(prefix.with_suffix('.json'),HERE/'search.best.json')
            result=dict(status='CANDIDATE_D5_DURING_PREFLIGHT',first_i=first_i,pair_indices=[j,k],
                        preflight_checks=checks,compile=compilation,cumulative_cpu_seconds=used(),
                        production_started=False,best=score)
            (HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps(result,indent=2),flush=True)
            return
    preflight=dict(status='GF64_GROUP_INVERSE_AND_TWO_EXPANDED_FULL_BFS_CHECKS_PASSED',compile=compilation,
        field_polynomial='t^6+t+1',primitive_g=2,primitive_order=63,r=8,action_order=21,
        all_group_inverses_checked=2688,inverse_pair_counts=[420,420,420],zero_translation_pairs=20,
        fallback_reason='This binary implements characteristic-two GF64, not the old characteristic-five F25 baseline',
        independent_scope_check='SCOPE.md and scope_check.json by math agent',checks=checks)
    (HERE/'preflight.json').write_text(json.dumps(preflight,indent=2)+'\n')
    print(json.dumps(dict(event='PREFLIGHT_PASSED',cpu_used=used(),planned_raw=1058400)),flush=True)
    remaining=BUDGET-used();assert remaining>1
    prefix=HERE/'search'
    production=run([EXE,remaining-0.5,2000,prefix],HERE/'run.log',remaining)
    if production['returncode']!=0:
        (HERE/'terminal.json').write_text(json.dumps(dict(status='EXECUTION_ERROR',production=production,cumulative_cpu_seconds=used(),automatic_restart=False),indent=2)+'\n')
        raise RuntimeError('batch failed; no restart')
    terminal=json.loads(prefix.with_suffix('.terminal.json').read_text())
    for c in terminal['counts'].values():
        assert c['raw_slots_visited']==c['invalid']+c['skipped_HH']+c['fully_scored']
        assert c['fully_scored']==sum(c['score_histogram'].values())
        assert c['invalid']==c['skipped_HH']==0
        if terminal['status']=='COMPLETE_NO_SOLUTION':assert c['raw_slots_visited']==c['fully_scored']==176400
    if terminal['status']=='COMPLETE_NO_SOLUTION':assert terminal['next_candidate_cursor']==1058400
    result=dict(scope='Only d7 GF64 C42 action-order21 three-inverse-pair family, six first quotients',
        other_generator_types_searched=False,worker_count=1,cumulative_cpu_limit_seconds=BUDGET,cumulative_cpu_seconds=used(),
        preflight='preflight.json',production=production,terminal=terminal,
        profile=json.loads(prefix.with_suffix('.profile.json').read_text()) if prefix.with_suffix('.profile.json').exists() else None,
        first_head_zero_saved=prefix.with_suffix('.first_head_zero.json').exists(),independent_best_validation='pending')
    (HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
    compact={kind:{k:v for k,v in c.items() if k!='score_histogram'} for kind,c in terminal['counts'].items()}
    print(json.dumps(dict(event='TERMINAL',status=terminal['status'],cpu_seconds=used(),counts=compact,
        profile=result['profile'],best=json.loads(prefix.with_suffix('.best.json').read_text())),indent=2),flush=True)


if __name__=='__main__':
    main()
