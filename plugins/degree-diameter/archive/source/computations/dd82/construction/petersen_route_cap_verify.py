#!/usr/bin/env python3
"""Independently verify saved radius-two candidates from edge files by BFS.
Replays the saved changes from the seed with ordinary adjacency sets; does
not import search code or reuse bitsets/cached path counts.
"""
from pathlib import Path
from collections import Counter,deque
import json
HERE=Path(__file__).resolve().parent

def read(path):
    lines=[list(map(int,line.split())) for line in path.read_text().splitlines() if line.strip()]
    n,m=lines[0];assert n==60 and m==240 and len(lines)==m+1
    adj=[set() for _ in range(n)];seen=set()
    for u,v in lines[1:]:
        assert 0<=u<v<n and (u,v) not in seen;seen.add((u,v));adj[u].add(v);adj[v].add(u)
    assert Counter(map(len,adj))=={8:60}
    assert all(sum(v//10==f for v in adj[u])==(3 if u//10==f else 1) for u in range(n) for f in range(6))
    return adj

def check(path,moves,expected,seed):
    adj=read(path);replay=[set(row) for row in seed]
    for move in moves:
        i,j=move['fibers'];a,b=move['source_coordinates'];u,v=10*i+a,10*i+b
        x=next(x for x in replay[u] if x//10==j);y=next(y for y in replay[v] if y//10==j)
        for s,t in ((u,x),(v,y)):replay[s].remove(t);replay[t].remove(s)
        for s,t in ((u,y),(v,x)):replay[s].add(t);replay[t].add(s)
    assert replay==adj and adj!=seed
    assert all({v for v in adj[u] if v//10==u//10}=={v for v in seed[u] if v//10==u//10} for u in range(60))
    hist=Counter();bad=[]
    for u in range(60):
        ds=[-1]*60;ds[u]=0;queue=deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if ds[w]<0:ds[w]=ds[v]+1;queue.append(w)
        for v in range(u+1,60):
            hist[ds[v]]+=1
            if ds[v]<0 or ds[v]>2:
                bad.append({'u':u,'v':v,'distance':ds[v],'common_neighbors':sorted(adj[u]&adj[v]),'neighbors_u':sorted(adj[u]),'neighbors_v':sorted(adj[v])})
    route_hist=Counter();cap_violations=[]
    for u in range(60):
        for v in range(u+1,60):
            if u//10==v//10:continue
            route=int(v in adj[u])+len(adj[u]&adj[v]);route_hist[route]+=1
            if route>2:cap_violations.append([u,v,route])
    assert len(bad)==expected and not cap_violations
    result={'source':str(path),'n':60,'m':240,'simple':True,'degree_histogram':{8:60},
      'distance_histogram':dict(sorted(hist.items())),'cross_fiber_route_count_histogram':dict(sorted(route_hist.items())),
      'cross_fiber_route_cap_verified':2,'uncovered_pair_count':len(bad),'uncovered_pairs':bad,
      'saved_switch_replay_matches':True,'different_from_seed':True,'valid_degree8_diameter2':not bad}
    path.with_suffix('.verification.json').write_text(json.dumps(result,indent=2)+'\n')
    return {k:v for k,v in result.items() if k!='uncovered_pairs'}

def main():
    report=json.loads((HERE/'petersen_route_cap_two_switches.json').read_text())
    seed=read(HERE/'petersen_six_fibers.best.edges')
    checks=[check(HERE/'petersen_route_cap_two_switches.best.edges',report['best_path'],report['minimum_bad_pairs_among_distinct_neighbors'],seed),
            check(HERE/'petersen_route_cap_two_switches.best_double.edges',report['best_double_path'],report['minimum_bad_pairs_among_distinct_double_neighbors'],seed)]
    old=json.loads((HERE/'petersen_route_cap_neighborhood.json').read_text())
    oldset={(tuple(x['fibers']),tuple(x['swapped_sources']),x['bad_pairs']) for x in old['feasible']}
    newset={(tuple(x['move']['fibers']),tuple(x['move']['source_vertices']),x['bad_pairs']) for x in report['single_feasible_moves']}
    assert oldset==newset and len(oldset)==50
    result={'single_switch_list_matches_previous_root_enumeration':True,'candidate_checks':checks}
    (HERE/'petersen_route_cap_two_switches.verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
