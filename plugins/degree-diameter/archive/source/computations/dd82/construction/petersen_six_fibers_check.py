#!/usr/bin/env python3
"""Independent full BFS check of an expanded edge list, with all bad-pair witnesses.
Reads no search/generator code. Parameter file is used only to compare expected count.
"""
import argparse
from collections import Counter,deque
import json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('edges',type=Path);ap.add_argument('--params',type=Path);args=ap.parse_args()
    rows=[list(map(int,l.split())) for l in args.edges.read_text().splitlines() if l.strip()]
    n,m=rows[0];assert n==60 and m==len(rows)-1
    adj=[set() for _ in range(n)];seen=set()
    for u,v in rows[1:]:
        assert 0<=u<n and 0<=v<n and u!=v
        edge=tuple(sorted((u,v)));assert edge not in seen;seen.add(edge)
        adj[u].add(v);adj[v].add(u)
    distance_hist=Counter();bad=[];bad_by_fiber_pair=Counter()
    for u in range(n):
        ds=[-1]*n;ds[u]=0;q=deque([u])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if ds[w]<0:ds[w]=ds[v]+1;q.append(w)
        for v in range(u+1,n):
            distance_hist[ds[v]]+=1
            if ds[v]<0 or ds[v]>2:
                bad.append({'u':u,'v':v,'distance':ds[v],'common_neighbors':sorted(adj[u]&adj[v]),'neighbors_u':sorted(adj[u]),'neighbors_v':sorted(adj[v])})
                bad_by_fiber_pair[f'{u//10},{v//10}']+=1
    degree_hist=Counter(map(len,adj));assert degree_hist=={8:60} and m==240
    # Verify the claimed order-five graph automorphism directly on edge set.
    sigma=[10*((u//10+1)%5)+u%10 if u<50 else 50+(u%5+1)%5+5*(u%10//5) for u in range(60)]
    assert {tuple(sorted((sigma[u],sigma[v]))) for u,v in seen}==seen
    assert all(sum(v//10==f for v in adj[u])==(3 if u//10==f else 1) for u in range(n) for f in range(6))
    within_bad=[b for b in bad if b['u']//10==b['v']//10];assert not within_bad
    # Actual overlap of the two internal-neighbor triples, in both directions.
    overlap_hist=Counter();overlap_violations=[]
    for i in range(6):
        for j in range(i+1,6):
            match={u:next(v for v in adj[u] if v//10==j) for u in range(10*i,10*i+10)}
            for u in match:
                v=match[u]
                left={x for x in adj[v] if x//10==j}
                right={match[x] for x in adj[u] if x//10==i}
                overlap=sorted(left&right);overlap_hist[len(overlap)]+=1
                if len(overlap)>1:overlap_violations.append({'fibers':[i,j],'source':u,'matching_target':v,'overlap':overlap})
    defect_hist=Counter();row_deficits=Counter()
    for i in range(6):
        for j in range(i+1,6):
            for u in range(10*i,10*i+10):
                missing=0
                for v in range(10*j,10*j+10):
                    count=int(v in adj[u])+len(adj[u]&adj[v]);defect_hist[count]+=1
                    if count==0:missing+=1
                row_deficits[missing]+=1
    result={'n':n,'m':m,'simple':True,'degree_histogram':dict(sorted(degree_hist.items())),
      'distance_histogram':dict(sorted(distance_hist.items())),'valid_degree8_diameter2':not bad,
      'c5_automorphism_verified':True,'within_fiber_bad_pairs':len(within_bad),'uncovered_pair_count':len(bad),
      'bad_pairs_by_fiber_pair':dict(sorted(bad_by_fiber_pair.items())),
      'internal_neighbor_triple_overlap_histogram':dict(sorted(overlap_hist.items())),
      'internal_overlap_violations':overlap_violations,
      'cross_fiber_direct_plus_two_step_path_count_histogram':dict(sorted(defect_hist.items())),
      'cross_fiber_row_missing_count_histogram':dict(sorted(row_deficits.items())),
      'uncovered_pairs':bad}
    if args.params:
        params=json.loads(args.params.read_text());assert params['expected_uncovered_pairs']==len(bad)
        result['search_score_matches_independent_bfs']=True
    out=args.edges.with_suffix('.verification.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('uncovered_pairs','internal_overlap_violations')},indent=2))
if __name__=='__main__':main()
