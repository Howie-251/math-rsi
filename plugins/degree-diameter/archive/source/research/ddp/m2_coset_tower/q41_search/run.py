"""One source reconstruction and one profiled finite q41 coset-tower batch."""
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
EXE=HERE/'search'
BUDGET=120.0


def children_cpu():
    u=resource.getrusage(resource.RUSAGE_CHILDREN)
    return u.ru_utime+u.ru_stime


def main():
    start_own=time.process_time()
    start_children=children_cpu()
    def used():
        return time.process_time()-start_own+children_cpu()-start_children
    affinity=min(os.sched_getaffinity(0))
    os.sched_setaffinity(0,{affinity})
    def run(args,log,remaining):
        def limits():
            os.sched_setaffinity(0,{affinity})
            resource.setrlimit(resource.RLIMIT_CPU,(math.ceil(remaining),math.ceil(remaining)))
        before=children_cpu();wall=time.monotonic()
        with Path(log).open('w') as f:
            p=subprocess.run(list(map(str,args)),stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits)
        return dict(command=list(map(str,args)),returncode=p.returncode,
                    cpu_seconds=children_cpu()-before,wall_seconds=time.monotonic()-wall)
    compile_result=run(['g++','-O3','-std=c++17',HERE/'search.cpp','-o',EXE],HERE/'compile.log',BUDGET-used())
    assert compile_result['returncode']==0
    baseline=HERE/'q25_source_check'
    source_result=run([EXE,'check',25,2,246,292,251,260,baseline],HERE/'q25_source_check.log',BUDGET-used())
    assert source_result['returncode']==0
    def read_edges(path):
        data=list(map(int,path.read_text().split()))
        return data[:2],{tuple(data[i:i+2]) for i in range(2,len(data),2)}
    header,edges=read_edges(baseline.with_suffix('.edges'))
    source=ROOT/'research/ddp/m1_degree5_transfer/rithwik650_source.edges'
    old_header,old_edges=read_edges(source)
    def relabel(v):
        if 500<=v<625:
            z=v-500;return 500+5*(z%25)+z//25
        return v
    mapped={tuple(sorted((relabel(u),relabel(v)))) for u,v in edges}
    assert header==old_header==[650,1625]
    assert len(edges)==len(mapped)==1625 and mapped==old_edges
    best=json.loads(baseline.with_suffix('.json').read_text())
    assert best['root_missing_leaf_block_head']==[0,0,0] and best['bad_unordered_pairs']==0
    verify=run([ROOT/'computations/ddp/verify_graph',baseline.with_suffix('.edges'),5,5],
               HERE/'q25_source_check.generic_verify.json',BUDGET-used())
    assert verify['returncode']==0
    verified=json.loads((HERE/'q25_source_check.generic_verify.json').read_text())
    assert verified['roots_checked']==650 and verified['diameter']==5 and verified['bad_unordered_pairs']==0
    preflight=dict(status='EXACT_SOURCE_MATCH_UNDER_EXPLICIT_BLOCK_RELABELING',compile=compile_result,
        source_check=source_result,original_source=str(source),all_1625_edges_match=True,
        label_map='new block 500+x+25*b -> source 500+5*x+b; all leaf/head labels unchanged',
        three_root_missing=[0,0,0],generic_verify=verified,generic_verify_run=verify)
    (HERE/'preflight.json').write_text(json.dumps(preflight,indent=2)+'\n')
    print(json.dumps(dict(event='SOURCE_CHECK_PASSED',edges=1625,diameter=5,cpu_used=used())),flush=True)
    remaining=BUDGET-used()
    assert remaining>1
    prefix=HERE/'search'
    production=run([EXE,remaining-0.5,1000,prefix],HERE/'run.log',remaining)
    assert production['returncode']==0
    terminal=json.loads(prefix.with_suffix('.terminal.json').read_text())
    for c in terminal['counts'].values():
        assert c['raw_slots_visited']==c['invalid_duplicate_pairs']+c['valid_candidates']
        assert c['valid_candidates']==c['skipped_HH']+c['fully_scored']
        assert c['fully_scored']==sum(c['score_histogram'].values())
    if terminal['status']=='COMPLETE_NO_SOLUTION':
        a,b=terminal['counts']['A'],terminal['counts']['B']
        assert (a['raw_slots_visited'],a['invalid_duplicate_pairs'],a['valid_candidates'])==(15560,0,15560)
        assert (b['raw_slots_visited'],b['invalid_duplicate_pairs'],b['valid_candidates'])==(7391,19,7372)
        assert terminal['next_candidate_cursor']==22951
    result=dict(scope='Only q41 r2 C20 coset tower, inverse-pair plus two involutions and two inverse pairs',
        four_involutions_searched=False,normalization='Only x -> lambda*x; no inner conjugation translations',
        worker_count=1,cumulative_cpu_limit_seconds=BUDGET,cumulative_cpu_seconds=used(),
        preflight='preflight.json',production=production,terminal=terminal,
        profile=json.loads(prefix.with_suffix('.profile.json').read_text()) if prefix.with_suffix('.profile.json').exists() else None,
        independent_best_validation='pending')
    (HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='TERMINAL',status=terminal['status'],cpu_seconds=used(),
        counts=terminal['counts'],best=json.loads(prefix.with_suffix('.best.json').read_text())),indent=2),flush=True)


if __name__=='__main__':
    main()
