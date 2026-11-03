"""Complete outer-coverage evaluation of the saved normalized f9 domain.

This reads the existing 10,080 triples; it does not regenerate that domain.
Scores use exact route multiplicities. Independent BFS is deliberately
left to a separate implementation reading only candidate.best.edges/json.
"""
from collections import Counter
from pathlib import Path
import csv
import json
import os
import resource
import signal
import time

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'computations/dd82/construction'
DOMAIN=BASE/'false_twins58_f9_domain_run/triples.txt'
OUT=BASE/'false_twins58_f9_coverage_run'
PARENT_RUN_ID='dd82-v3-f9-c7-20261013-0749'
F=(1,0,3,2,5,4)


class BudgetStop(Exception):pass


def alarm(*args):raise BudgetStop


def dump(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')


def inverse(p):
    q=[0]*6
    for a,b in enumerate(p):q[b]=a
    return tuple(q)


def coverage(triple):
    a,b,c=triple[:6],triple[6:12],triple[12:]
    ps=(None,a,b,c,inverse(c),inverse(b),inverse(a))
    hub=[]
    for x in range(6):
        row=[0]*6;row[x]+=1
        for e in range(1,7):row[ps[e][x]]+=1
        assert row==[1+int(y==F[x]) for y in range(6)]
        hub.append(row)
    matrices=[];zeros=[]
    for d in (1,2,3):
        matrix=[]
        for x in range(6):
            row=[0]*6;row[x]+=1;row[ps[d][x]]+=1
            for e in range(1,7):
                if e!=d:
                    # Row-source product P_e P_(d-e) applies e first.
                    row[ps[(d-e)%7][ps[e][x]]]+=1
            assert sum(row)==7
            matrix.append(row)
        assert all(sum(matrix[x][y] for x in range(6))==7 for y in range(6))
        matrices.append(matrix)
        zeros.append([(x,y) for x in range(6) for y in range(6) if matrix[x][y]==0])
    return 7*sum(map(len,zeros)),zeros,hub,matrices


def expand(triple):
    a,b,c=triple[:6],triple[6:12],triple[12:]
    edges=set()
    def add(u,v):
        assert u!=v
        pair=tuple(sorted((u,v)));assert pair not in edges
        edges.add(pair)
    # u=0, v=1; h=2; outer parents s_t=3+t.
    # Fixed fibre G_inf: 10+a; G_t: 16+6*t+a.
    for parent in range(2,10):add(0,parent);add(1,parent)
    for x in range(6):add(2,10+x)
    for t in range(7):
        for x in range(6):
            add(3+t,16+6*t+x)
            add(10+x,16+6*t+x)
    for d,p in enumerate((a,b,c),1):
        for t in range(7):
            for x in range(6):add(16+6*t+x,16+6*((t+d)%7)+p[x])
    assert len(edges)==232
    adjacency=[set() for _ in range(58)]
    for u,v in edges:adjacency[u].add(v);adjacency[v].add(u)
    assert [len(row) for row in adjacency]==[8]*58
    return sorted(edges),adjacency


def predicted_bad_pairs(zeros):
    bad=[]
    for d,missing in enumerate(zeros,1):
        for t in range(7):
            for x,y in missing:
                bad.append(tuple(sorted((16+6*t+x,16+6*((t+d)%7)+y))))
    assert len(bad)==len(set(bad))
    return sorted(bad)


def save_best(index,triple,bad,zeros,hub,matrices):
    edges,adj=expand(triple)
    predicted=predicted_bad_pairs(zeros)
    assert len(predicted)==bad
    sigma=list(range(58))
    for t in range(7):
        sigma[3+t]=3+(t+1)%7
        for x in range(6):sigma[16+6*t+x]=16+6*((t+1)%7)+x
    assert {tuple(sorted((sigma[u],sigma[v]))) for u,v in edges}==set(edges)
    dump(OUT/'candidate.best.json',dict(n=58,edges=edges,domain_line=index+1,
        A=triple[:6],B=triple[6:12],C=triple[12:],predicted_bad_pairs=bad,
        parent_run_id=PARENT_RUN_ID))
    (OUT/'candidate.best.edges').write_text('58 232\n'+''.join(f'{u} {v}\n' for u,v in edges))
    dump(OUT/'candidate.best.parameters.json',dict(domain_line=index+1,A=triple[:6],B=triple[6:12],C=triple[12:],
        normalized_defect_matching=F,hub_matrix=hub,outer_matrices=matrices,
        outer_zero_entries= zeros,predicted_bad_pair_list=predicted,
        vertex_labels=dict(twins=[0,1],fixed_parent=2,outer_parents='3+t, t=0..6',
                          fixed_fibre='10+a, a=0..5',outer_fibres='16+6*t+a'),
        order7_automorphism=sigma,automorphism_edges_verified=232,
        independent_bfs_status='pending separate implementation; no BFS run by search'))


def main():
    cpu_start=time.process_time();wall=time.monotonic()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'launch.json').exists(),'One outer-coverage episode'
    triples=[tuple(map(int,line.split())) for line in DOMAIN.read_text().splitlines() if line.strip()]
    assert len(triples)==10080 and len(set(triples))==10080
    for triple in triples:
        assert len(triple)==18
        for first in (0,6,12):
            p=triple[first:first+6]
            assert sorted(p)==list(range(6)) and all(x!=y for x,y in enumerate(p))
    dump(OUT/'launch.json',dict(parent_run_id=PARENT_RUN_ID,phase='finite outer-coverage experiment',
        domain=str(DOMAIN.relative_to(ROOT)),expected_triples=10080,cpu_budget_seconds=60,
        profile_prefix=64,one_cpu=True,independent_bfs='delegated to parent/separate implementation',
        workflow='ARIS DD82 mathematical adaptation',
        skills=['.agents/skills/proof-writer/SKILL.md','.agents/skills/experiment-bridge/SKILL.md'],
        adaptation=dict(plan='DD82_V3_ARIS_GEMINI_PLAN_20261013.md plus explicit assigned finite experiment',
            backend='local exact integer graph computation',code_review='local self-check; parent review separately',
            sanity='prefix expanded-edge direct/common-neighbour comparison; no independent BFS claim',
            disabled=['GPU training','paper scoring','hashes','extra manifest','automatic ablation'],
            external_review='Gemini direction/results handled by parent same-mechanism thread; not yet reviewed')))
    histogram=Counter();zero_hist=Counter();best=None;best_indices=[];evaluated=0
    single_pass=[0,0,0];pair_pass=[0,0,0];targets=[];complete=False;reason=None
    signal.signal(signal.SIGPROF,alarm);signal.setitimer(signal.ITIMER_PROF,58)
    first_time=time.process_time();profile=None
    try:
        with (OUT/'scores.csv').open('w',newline='') as f:
            writer=csv.writer(f);writer.writerow(['domain_line','zero_d1','zero_d2','zero_d3','bad_pairs'])
            for index,triple in enumerate(triples):
                bad,zeros,hub,matrices=coverage(triple)
                sizes=tuple(map(len,zeros));passed=[z==0 for z in sizes]
                # Small sanity milestone inside this episode, not another search.
                if index<64:
                    edges,adj=expand(triple)
                    direct_bad=[(u,v) for u in range(58) for v in range(u+1,58)
                                if v not in adj[u] and not (adj[u]&adj[v])]
                    assert direct_bad==predicted_bad_pairs(zeros)
                writer.writerow([index+1,*sizes,bad]);evaluated+=1
                histogram[bad]+=1;zero_hist[','.join(map(str,sizes))]+=1
                for d in range(3):single_pass[d]+=passed[d]
                for k,(i,j) in enumerate(((0,1),(0,2),(1,2))):pair_pass[k]+=passed[i] and passed[j]
                if best is None or bad<best:
                    best=bad;best_indices=[];save_best(index,triple,bad,zeros,hub,matrices)
                    print(json.dumps(dict(event='new_best',domain_line=index+1,bad_pairs=bad)),flush=True)
                if bad==best:best_indices.append(index+1)
                if bad==0:
                    targets.append(index+1);reason='target_found';break
                if index==63:
                    prefix_cpu=time.process_time()-first_time
                    projected=prefix_cpu*len(triples)/64
                    profile=dict(prefix_triples=64,prefix_cpu_seconds=prefix_cpu,
                        projected_total_cpu_seconds=projected,sanity_all_expanded_pairs_agree=True,
                        continue_full_domain=projected<55)
                    dump(OUT/'profile.json',profile);f.flush()
                    if projected>=55:reason='profile_exceeds_budget';break
            else:complete=True;reason='full_domain_exhausted'
    except BudgetStop:reason='cpu_budget_partial_domain'
    finally:signal.setitimer(signal.ITIMER_PROF,0)
    report=dict(parent_run_id=PARENT_RUN_ID,complete=complete,stop_reason=reason,
        expected_triples=10080,evaluated_triples=evaluated,hub_equation_checked=evaluated,
        three_outer_blocks_evaluated=evaluated,bad_pair_histogram=dict(sorted(histogram.items())),
        missing_block_tuple_histogram=dict(sorted(zero_hist.items())),single_block_pass_counts=single_pass,
        two_block_pass_counts=dict(zip(('1,2','1,3','2,3'),pair_pass)),target_lines=targets,
        best_bad_pairs=best,best_domain_lines=best_indices,best_graph='candidate.best.edges',
        all_evaluations_saved='scores.csv',profile=profile,
        cpu_seconds=time.process_time()-cpu_start,wall_seconds=time.monotonic()-wall,
        max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,cpu_budget_seconds=60,
        independent_bfs_status='pending parent/separate implementation',solver_calls=0,
        gemini_review_status='not yet reviewed',scope='f=9 order-seven automorphism branch at n=58 only')
    dump(OUT/'result.json',report)
    print(json.dumps({k:v for k,v in report.items() if k not in ('best_domain_lines','missing_block_tuple_histogram')}),flush=True)


if __name__=='__main__':main()
