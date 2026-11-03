#!/usr/bin/env python3
"""Independent reconstruction/BFS and neutral adjacency check of the closed component."""
from pathlib import Path
from collections import Counter,deque
from itertools import combinations
import bisect,json
from twin_seed_unrestricted_switch_verify import read
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin59_nonworsening_levels_run'
def bfs(edges,n=59):
    adj=[set() for _ in range(n)]
    for u,v in edges:assert 0<=u<v<n;adj[u].add(v);adj[v].add(u)
    assert len(edges)==236 and Counter(map(len,adj))=={8:59}
    histogram=Counter();bad=[]
    for u in range(n):
        distance=[-1]*n;distance[u]=0;queue=deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if distance[w]<0:distance[w]=distance[v]+1;queue.append(w)
        for v in range(u+1,n):
            histogram[distance[v]]+=1
            if distance[v]<0 or distance[v]>2:
                bad.append({'u':u,'v':v,'distance':distance[v],'common_neighbors':sorted(adj[u]&adj[v]),'neighbors_u':sorted(adj[u]),'neighbors_v':sorted(adj[v])})
    valid=0
    for (a,b),(c,d) in combinations(sorted(edges),2):
        if len({a,b,c,d})<4:continue
        valid+=(c not in adj[a] and d not in adj[b])
        valid+=(d not in adj[a] and c not in adj[b])
    return {'n':59,'m':236,'simple':True,'degree_histogram':{8:59},'distance_histogram':dict(sorted(histogram.items())),
            'uncovered_pair_count':len(bad),'valid_degree8_diameter2':not bad,
            'independent_valid_switch_count':valid,'uncovered_pairs':bad}
def main():
    report=json.loads((OUT/'episode.json').read_text())
    assert report['terminal_neutral_component_closed'] and report['strict_improvements']==0
    _,seed=read(Path(report['source']));states=[seed];ordered=[tuple(sorted(seed))]
    for node in report['stored_states'][1:]:
        edges=states[node['parent']].copy()
        for e in node['change']['removed']:assert tuple(e) in edges;edges.remove(tuple(e))
        for e in node['change']['added']:assert tuple(e) not in edges;edges.add(tuple(e))
        encoded=tuple(sorted(edges));pos=bisect.bisect_left(ordered,encoded)
        assert pos==len(ordered) or ordered[pos]!=encoded
        ordered.insert(pos,encoded);states.append(edges)
    assert len(states)==report['distinct_stored_states']==24
    checks=[bfs(edges) for edges in states]
    assert all(r['uncovered_pair_count']==26 for r in checks)
    neutral=[set() for _ in states]
    for i,j in combinations(range(len(states)),2):
        removed=states[i]-states[j];added=states[j]-states[i]
        if len(removed)==len(added)==2 and len({v for e in removed for v in e})==4:
            neutral[i].add(j);neutral[j].add(i)
    done={0};queue=deque([0])
    while queue:
        for v in neutral[queue.popleft()]:
            if v not in done:done.add(v);queue.append(v)
    assert len(done)==len(states)
    expansions={e['node']:e for e in report['expansions']}
    assert len(expansions)==len(states) and all(e['complete'] for e in expansions.values())
    for i in range(len(states)):
        e=expansions[i]
        assert e['valid_switches_evaluated']==checks[i]['independent_valid_switch_count']
        assert sum(e['bad_pair_histogram'].values())==e['valid_switches_evaluated']
        assert min(map(int,e['bad_pair_histogram']))==26
        assert e['bad_pair_histogram']['26']==len(neutral[i])
    assert sum(e['valid_switches_evaluated'] for e in expansions.values())==report['candidate_switches_evaluated']
    result={'all_stored_graphs_replayed_and_distinct':True,'all_24_graphs_independently_bfs_verified':True,
      'independent_valid_switch_counts_match':True,'neutral_adjacency_matches_enumerated_energy26_counts':True,
      'neutral_component_connected':True,'neutral_state_count':len(states),'neutral_edge_count':sum(map(len,neutral))//2,
      'neutral_degree_histogram':dict(Counter(map(len,neutral))),
      'scope':'Complete nonincreasing two-edge-switch component of the fixed labelled 26-bad-pair seed only',
      'no_lower_exit_in_all_complete_enumerated_neighborhoods':True,
      'neutral_adjacency':[sorted(v) for v in neutral],'state_checks':checks}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    graphs={'n':59,'states':[{'node':i,'edges':[list(e) for e in sorted(s)]} for i,s in enumerate(states)]}
    (OUT/'expanded_states.json').write_text(json.dumps(graphs,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('state_checks','neutral_adjacency')},indent=2))
if __name__=='__main__':main()
