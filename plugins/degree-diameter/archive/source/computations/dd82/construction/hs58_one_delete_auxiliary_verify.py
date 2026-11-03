#!/usr/bin/env python3
"""Recover saved-example symmetry orbits and independently BFS every recovered H."""
from pathlib import Path
from itertools import permutations
from collections import Counter,deque
import bisect,json,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'hs58_one_delete_auxiliary_run'
def key(edges):return tuple(sorted(tuple(sorted(e)) for e in edges))
def contains(ordered,value):
    pos=bisect.bisect_left(ordered,value)
    return pos<len(ordered) and ordered[pos]==value
def check(edges,case):
    assert len(edges)==case['edge_count'] and len(set(edges))==len(edges)
    adj=[set() for _ in range(8)]
    for u,v in edges:
        assert 0<=u<v<8
        adj[u].add(v);adj[v].add(u)
    assert all(len(adj[u])<=case['degree_upper_bounds'][u] for u in range(8))
    allowed={tuple(case['U']),tuple(case['V'])};bad=[];hist=Counter()
    for u in range(8):
        distance=[-1]*8;distance[u]=0;queue=deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if distance[w]<0:distance[w]=distance[v]+1;queue.append(w)
        for v in range(u+1,8):
            hist[distance[v]]+=1
            if distance[v]<0 or distance[v]>2:
                assert (u,v) in allowed
                bad.append([u,v])
    return {'degrees':[len(adj[u]) for u in range(8)],'degree_histogram':dict(Counter(map(len,adj))),
      'distance_histogram':dict(sorted(hist.items())),'bad_pairs':bad}
def main():
    start=time.process_time();report=json.loads((OUT/'enumeration.json').read_text())
    assert not report['timed_out'] and all(c['complete'] for c in report['cases'])
    results=[];allcases=[]
    for case in report['cases']:
        examples=[key(s['edges']) for s in case['saved_survivors']]
        assert len(examples)==len(set(examples))
        graphs=sorted(examples);orbits=[]
        if case['m']==5 and case['U']==case['V'] and examples:
            graphs=[]
            for example in examples:
                if contains(graphs,example):continue
                before=len(graphs)
                for flip in (False,True):
                    for rest in permutations(range(2,8)):
                        mapping=((1,0) if flip else (0,1))+rest
                        transformed=key((mapping[u],mapping[v]) for u,v in example)
                        pos=bisect.bisect_left(graphs,transformed)
                        if pos==len(graphs) or graphs[pos]!=transformed:graphs.insert(pos,transformed)
                orbits.append({'representative_edges':example,'orbit_size':len(graphs)-before,
                  'action':'arbitrary permutation of labels2..7 and optional interchange0,1'})
        checks=[check(g,case) for g in graphs]
        assert len(graphs)<=case['survivor_count']
        complete=len(graphs)==case['survivor_count']
        results.append({'m':case['m'],'U':case['U'],'V':case['V'],
          'enumerated_survivor_count':case['survivor_count'],'originally_saved_examples':len(examples),
          'distinct_recovered_and_bfs_verified':len(graphs),'all_enumerated_survivors_recovered':complete,
          'orbit_recovery':orbits,'checks':checks})
        allcases.append({'m':case['m'],'U':case['U'],'V':case['V'],'complete_survivor_list':complete,
          'survivor_count':case['survivor_count'],'survivors':[{'edges':g} for g in graphs]})
    result={'all_four_enumerations_complete':True,
      'no_28_edge_enumeration_rerun':True,
      'completeness_basis':'Recovered valid labelled graphs are exactly distinct; equality with the completed enumeration count proves the list complete',
      'all_survivors_independently_bfs_verified':all(r['all_enumerated_survivors_recovered'] for r in results),
      'cpu_seconds':time.process_time()-start,'cases':results}
    (OUT/'all_survivors.json').write_text(json.dumps({'n':8,'cases':allcases},separators=(',',':'))+'\n')
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    filtered=[]
    for s in allcases[2]['survivors']:
        degrees=Counter(v for e in s['edges'] for v in e)
        if degrees[0]+degrees[1] in (9,10):
            filtered.append({'edges':s['edges'],'common_degrees':[degrees[0],degrees[1]]})
    subset={'necessary_condition':'m5 U=V={0,1}: dH(0)+dH(1) in {9,10}',
      'scope':'Filter of recovered510 graphs only; global filtering completeness not yet established',
      'survivors':filtered}
    (OUT/'common_degree_filtered_examples.json').write_text(json.dumps(subset,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
    for c in results:print(json.dumps({k:v for k,v in c.items() if k!='checks'},indent=2))
if __name__=='__main__':main()
