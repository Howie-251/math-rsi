"""Complete small domain satisfying only the normalized f9 hub equation.

No graph distances or outer-fibre coverage conditions are evaluated.
Output triples are full permutations A,B,C in row-source image notation.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import json
import os
import resource
import signal
import time

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'computations/dd82/construction/false_twins58_f9_domain_run'


class BudgetStop(Exception):pass


def alarm(*args):raise BudgetStop


def dump(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')


def symmetric_matrix(p):
    m=[0]*36
    for u,v in enumerate(p):m[6*u+v]+=1;m[6*v+u]+=1
    return tuple(m)


def orient_residual(r):
    adjacent=[[v for v in range(6) if r[6*u+v]] for u in range(6)]
    unseen=set(range(6));components=[]
    while unseen:
        u=min(unseen)
        if len(adjacent[u])==1:
            v=adjacent[u][0]
            assert r[6*u+v]==2 and adjacent[v]==[u] and r[6*v+u]==2
            cycle=[u,v]
        else:
            assert len(adjacent[u])==2
            cycle=[u];previous=u;v=min(adjacent[u])
            while v!=u:
                assert v not in cycle and len(adjacent[v])==2
                cycle.append(v)
                w=next(x for x in adjacent[v] if x!=previous)
                previous,v=v,w
            assert len(cycle)>=3
        assert set(cycle)<=unseen
        unseen-=set(cycle);components.append(cycle)
    answers=[]
    for choices in product(*(range(1 if len(c)==2 else 2) for c in components)):
        p=[-1]*6
        for c,reverse in zip(components,choices):
            step=-1 if reverse else 1
            for i,u in enumerate(c):p[u]=c[(i+step)%len(c)]
        assert sorted(p)==list(range(6)) and all(u!=v for u,v in enumerate(p))
        assert symmetric_matrix(p)==r
        answers.append(tuple(p))
    assert len(answers)==len(set(answers)) and len(answers)<=4
    return answers,','.join(map(str,sorted(map(len,components))))


def main():
    start=time.process_time();wall=time.monotonic()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(5,6))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'launch.json').exists(),'Only one domain preparation'
    involution=[1,0,3,2,5,4]
    target=tuple(int(u!=v)+int(involution[u]==v) for u in range(6) for v in range(6))
    derangements=[p for p in permutations(range(6)) if all(u!=v for u,v in enumerate(p))]
    assert len(derangements)==265
    matrices=[symmetric_matrix(p) for p in derangements]
    dump(OUT/'launch.json',dict(cpu_budget_seconds=5,normalized_defect_matching=involution,
        derangements=265,ordered_AB_pairs=265**2,upper_bound_triples=4*265**2,
        graph_distance_evaluations=0,outer_coverage_evaluations=0))
    tested=valid_pairs=triples=0;components=Counter();orientations=Counter();complete=True
    cursor=None
    signal.signal(signal.SIGPROF,alarm);signal.setitimer(signal.ITIMER_PROF,4.5)
    try:
        with (OUT/'triples.txt').open('w') as out:
            for ai,a in enumerate(derangements):
                for bi,b in enumerate(derangements):
                    cursor=[ai,bi];tested+=1
                    residual=tuple(t-x-y for t,x,y in zip(target,matrices[ai],matrices[bi]))
                    if min(residual)<0:continue
                    assert all(sum(residual[6*u:6*u+6])==2 and residual[7*u]==0 for u in range(6))
                    cs,kind=orient_residual(residual)
                    valid_pairs+=1;components[kind]+=1;orientations[len(cs)]+=1
                    for c in cs:
                        out.write(' '.join(map(str,a+b+c))+'\n');triples+=1
    except BudgetStop:complete=False
    finally:signal.setitimer(signal.ITIMER_PROF,0)
    report=dict(complete=complete,stop_reason='full_hub_domain_prepared' if complete else 'cpu_budget_partial_domain',
        derangements=265,ordered_AB_pairs_expected=265**2,ordered_AB_pairs_tested=tested,
        nonnegative_residual_AB_pairs=valid_pairs,component_type_counts=dict(sorted(components.items())),
        orientations_per_residual_counts=dict(sorted(orientations.items())),triples_written=triples,
        all_triples_saved=True,triples_file='triples.txt',row_format='A images, then B images, then C images; six integers each',
        last_AB_indices=cursor,normalized_defect_matching=involution,
        graph_distance_evaluations=0,outer_coverage_evaluations=0,solver_calls=0,
        cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall,cpu_budget_seconds=5,
        scope='Exactly the normalized f9 C7 hub equation; complete graph coverage has not been tested')
    if complete:assert tested==265**2 and triples==sum(int(k)*v for k,v in orientations.items())
    dump(OUT/'result.json',report);print(json.dumps(report),flush=True)


if __name__=='__main__':main()
