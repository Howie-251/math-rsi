#!/usr/bin/env python3
"""Check the finite-choice counts and independently BFS every retained graph."""
from pathlib import Path
from collections import Counter,deque
import bisect,json
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin59_to_58_deflation_run'
def read_edges(path):
    values=list(map(int,path.read_text().split()));n,m=values[:2]
    edges=[tuple(values[k:k+2]) for k in range(2,len(values),2)]
    assert len(edges)==m and len(set(edges))==m
    assert all(0<=u<v<n for u,v in edges)
    return n,set(edges)
def bfs(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        assert 0<=u<v<n
        adj[u].add(v);adj[v].add(u)
    assert len(edges)==4*n and Counter(map(len,adj))=={8:n}
    hist=Counter();bad=[]
    for u in range(n):
        dist=[-1]*n;dist[u]=0;q=deque([u])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if dist[w]<0:dist[w]=dist[v]+1;q.append(w)
        for v in range(u+1,n):
            hist[dist[v]]+=1
            if dist[v]<0 or dist[v]>2:
                bad.append({'u':u,'v':v,'distance':dist[v],
                  'common_neighbors':sorted(adj[u]&adj[v]),
                  'neighbors_u':sorted(adj[u]),'neighbors_v':sorted(adj[v])})
    return {'n':n,'m':len(edges),'simple':True,'degree_histogram':dict(Counter(map(len,adj))),
      'distance_histogram':dict(sorted(hist.items())),'bad_pair_count':len(bad),
      'valid_degree8_diameter2':not bad,'bad_pairs':bad}
def matchings(points):
    if not points:
        yield ()
        return
    a=points[0]
    for k in range(1,len(points)):
        b=points[k]
        for rest in matchings(points[1:k]+points[k+1:]):yield ((a,b),)+rest
def write(path,value):path.write_text(json.dumps(value,indent=2)+'\n')
def main():
    source=json.loads((HERE/'twin59_nonworsening_levels_run/expanded_states.json').read_text())
    report=json.loads((OUT/'deflation.json').read_text())
    assert source['n']==59 and len(source['states'])==24
    patterns=list(matchings(tuple(range(8))));assert len(patterns)==105
    counts=[]
    for s,r in zip(source['states'],report['per_state']):
        assert s['node']==r['node']
        edges={tuple(e) for e in s['edges']};adj=[set() for _ in range(59)]
        for u,v in edges:adj[u].add(v);adj[v].add(u)
        assert len(edges)==236 and Counter(map(len,adj))=={8:59}
        rejected=0
        for deleted in range(59):
            neighbors=sorted(adj[deleted])
            for pattern in patterns:
                rejected+=any(neighbors[b] in adj[neighbors[a]] for a,b in pattern)
        valid=59*105-rejected
        assert r['choices']==59*105 and r['rejected_existing_edges']==rejected and r['valid_choices']==valid
        assert sum(r['bad_pair_histogram'].values())==valid
        assert min(map(int,r['bad_pair_histogram']))==r['minimum_bad_pairs']
        counts.append({'node':s['node'],'choices':59*105,'rejected':rejected,'valid':valid})
    assert sum(r['valid'] for r in counts)==report['valid_choices']
    assert sum(r['rejected'] for r in counts)==report['rejected_existing_edges']
    assert report['choices']==24*59*105
    totalhist=Counter()
    for r in report['per_state']:totalhist.update(r['bad_pair_histogram'])
    assert dict(totalhist)==report['bad_pair_histogram']
    origin=next(s for s in source['states'] if s['node']==report['best_source_node'])
    deleted=report['best_deleted_vertex_order59'];old={tuple(e) for e in origin['edges']}
    neighbors={v if u==deleted else u for u,v in old if deleted in (u,v)}
    repair=[tuple(e) for e in report['best_repair_edges_order59']]
    assert len(repair)==4 and Counter(v for e in repair for v in e)=={v:1 for v in neighbors}
    assert all(e not in old for e in repair)
    repaired={e for e in old if deleted not in e}|set(repair)
    expected={(u-(u>deleted),v-(v>deleted)) for u,v in repaired}
    n,seed=read_edges(OUT/'deflation.best.edges');assert n==58 and seed==expected
    seedjson=json.loads((OUT/'deflation.best.json').read_text())
    assert {tuple(e) for e in seedjson['edges']}==seed
    seedcheck=bfs(n,seed);assert seedcheck['bad_pair_count']==report['minimum_bad_pairs']
    write(OUT/'deflation.best.verification.json',seedcheck)
    result={'all_148680_choices_accounted_for':True,'existing_edge_rejections_independently_counted':True,
      'best_deflation_exact_origin_reconstructed':True,'source_counts':counts,'deflation_check':seedcheck}
    if seedcheck['bad_pair_count']:
        episode=json.loads((OUT/'component.json').read_text())
        states=[seed];ordered=[tuple(sorted(seed))]
        for node in episode['stored_states'][1:]:
            g=states[node['parent']].copy()
            for e in node['change']['removed']:assert tuple(e) in g;g.remove(tuple(e))
            for e in node['change']['added']:assert tuple(e) not in g;g.add(tuple(e))
            key=tuple(sorted(g));pos=bisect.bisect_left(ordered,key)
            assert pos==len(ordered) or ordered[pos]!=key
            ordered.insert(pos,key);states.append(g)
        assert len(states)==episode['distinct_stored_states']<=100
        statechecks=[bfs(58,g) for g in states]
        assert all(c['bad_pair_count']==r['bad_pairs'] for c,r in zip(statechecks,episode['stored_states']))
        assert sum(e['valid_switches_evaluated'] for e in episode['expansions'])==episode['candidate_switches_evaluated']
        for e in episode['expansions']:assert sum(e['bad_pair_histogram'].values())==e['valid_switches_evaluated']
        for step in episode['path']:
            path=Path(step['file']);nn,g=read_edges(path);assert nn==58 and g==states[step['node']]
            check=statechecks[step['node']];assert check['bad_pair_count']==step['bad_pairs']
            check['change_order58']=step['change']
            check['change_order59']={k:[[u+(u>=deleted),v+(v>=deleted)] for u,v in es] for k,es in step['change'].items()}
            write(path.with_suffix('.verification.json'),check)
            write(path.with_suffix('.json'),{'n':58,'edges':[list(e) for e in sorted(g)],
              'deflation_origin':{'source_state_node':report['best_source_node'],'deleted_vertex_order59':deleted,'repair_edges_order59':repair},
              'path_node':step['node'],'change_order58':step['change']})
        result.update({'all_retained_episode_states_replayed_distinct_and_bfs_checked':True,
          'episode_state_checks':statechecks,'component_completely_closed':episode['component_completely_closed'],
          'episode_stop_reason':episode['stop_reason'],'final_bad_pair_count':episode['endpoint_bad_pairs']})
        write(OUT/'episode.expanded_states.json',{'n':58,'states':[{'node':i,'edges':[list(e) for e in sorted(g)]} for i,g in enumerate(states)]})
    write(OUT/'verification.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_counts','deflation_check','episode_state_checks')},indent=2))
    print('deflation BFS',seedcheck['distance_histogram'])
    if 'statechecks' in locals():print('last saved BFS',statechecks[-1]['distance_histogram'])
if __name__=='__main__':main()
