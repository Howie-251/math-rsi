"""Bounded profile only: six-label positive overlap graph, no signed search."""
from itertools import combinations
from math import comb
from pathlib import Path
import json
import time

EDGES = tuple(combinations(range(6), 2))
INDEX = {e:i for i,e in enumerate(EDGES)}


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a, *rest = vertices
    for b in rest:
        for tail in matchings([v for v in rest if v != b]):
            yield (INDEX[tuple(sorted((a,b)))],)+tail


PM = tuple(matchings(list(range(6))))
assert len(PM) == 15


def c4(g,d):
    private = [4-v for v in d]
    total = 0
    for mask in range(64):
        n = sum(private[i] for i in range(6) if mask>>i&1)
        n += sum(v for (a,b),v in zip(EDGES,g) if mask>>a&1 and mask>>b&1)
        total += (-1)**(6-mask.bit_count()) * (comb(n,4) if n>=4 else 0)
    return total


def main():
    start = time.process_time()
    budget = 2.0
    g,d = [0]*15,[0]*6
    counts = {}
    completed_e = []
    samples = []
    visited = 0
    stopped = False

    def rec(i,e,target):
        nonlocal visited, stopped
        if stopped:return
        if i == 15:
            if e != target:return
            visited += 1
            if visited%256 == 0 and time.process_time()-start > budget:
                stopped = True
                return
            c = sum(g[a]*g[b]*g[c] for a,b,c in PM)
            if c<=4:
                key=f'E{target}_PM{c}'
                counts[key]=counts.get(key,0)+1
                if counts[key]==1 or counts[key]%1000==0:
                    value=c4(g,d)
                    samples.append(dict(E=target,PM=c,C4=value,
                                        sufficient_bound=38+(24-target-7)*c,
                                        vector=list(g)))
            return
        a,b=EDGES[i]
        for v in range(min(4-d[a],4-d[b],target-e)+1):
            g[i]=v;d[a]+=v;d[b]+=v
            rec(i+1,e+v,target)
            d[a]-=v;d[b]-=v
            if stopped:break
        g[i]=0

    for e in range(6,13):
        rec(0,0,e)
        if stopped:break
        completed_e.append(e)
    result=dict(status='bounded_profile_partial' if stopped else 'domain_count_complete',
                budget_process_seconds=budget, process_seconds=time.process_time()-start,
                completed_E=completed_e, labelled_graphs_visited=visited,
                partial_counts=counts, samples=samples,edge_order=EDGES)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('samples','edge_order')}))
    print('sample_count',len(samples),'weak_bound_failures',sum(s['C4']<=s['sufficient_bound'] for s in samples))


if __name__=='__main__':main()
