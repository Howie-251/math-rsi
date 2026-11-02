#!/usr/bin/env python3
"""Independent BFS and replay of saved unrestricted graph switches."""
from collections import Counter,deque
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin_seed_unrestricted_switch_run'

def read(path):
    rows=[list(map(int,line.split())) for line in path.read_text().splitlines() if line.strip()]
    n,m=rows[0];assert m==4*n and len(rows)==m+1
    adj=[set() for _ in range(n)];edges=set()
    for u,v in rows[1:]:
        assert 0<=u<v<n and (u,v) not in edges;edges.add((u,v));adj[u].add(v);adj[v].add(u)
    assert Counter(map(len,adj))=={8:n}
    return adj,edges

def verify(path,expected,reference,change,deleted):
    adj,edges=read(path);n=len(adj)
    replay={e for e in reference}
    for e in change['removed']:assert tuple(e) in replay;replay.remove(tuple(e))
    for e in change['added']:assert tuple(e) not in replay;replay.add(tuple(e))
    assert replay==edges
    dh=Counter();bad=[]
    for u in range(n):
        ds=[-1]*n;ds[u]=0;queue=deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if ds[w]<0:ds[w]=ds[v]+1;queue.append(w)
        for v in range(u+1,n):
            dh[ds[v]]+=1
            if ds[v]<0 or ds[v]>2:bad.append({'u':u,'v':v,'distance':ds[v],'common_neighbors':sorted(adj[u]&adj[v]),'neighbors_u':sorted(adj[u]),'neighbors_v':sorted(adj[v])})
    assert len(bad)==expected
    def original(v):return v if deleted is None or v<deleted else v+1
    def mapped(e):return [original(e[0]),original(e[1])]
    before=[Counter() for _ in range(n)];after=[Counter() for _ in range(n)]
    for target,es in ((before,reference),(after,edges)):
        for u,v in es:target[u][original(v)//10]+=1;target[v][original(u)//10]+=1
    changed_profile=[original(v) for v in range(n) if before[v]!=after[v]]
    original_change={k:[mapped(e) for e in change[k]] for k in ('removed','added')}
    changed_edges=original_change['removed']+original_change['added']
    blocks={tuple(sorted((u//10,v//10))) for u,v in changed_edges}
    matching_move=len(blocks)==1 and all(i!=j for i,j in blocks)
    trace={'change_in_current_labels':change,'change_in_original_60_labels':original_change,
           'single_interfiber_matching_transposition':matching_move,
           'vertices_with_changed_neighbor_counts_by_original_fiber':changed_profile,
           'changed_original_internal_edges':{k:[e for e in es if e[0]//10==e[1]//10] for k,es in original_change.items()}}
    result={'source':str(path),'n':n,'m':len(edges),'simple':True,'degree_histogram':{8:n},
      'distance_histogram':dict(sorted(dh.items())),'uncovered_pair_count':len(bad),
      'valid_degree8_diameter2':not bad,'switch_replay_matches':True,'trace':trace,'uncovered_pairs':bad}
    path.with_suffix('.verification.json').write_text(json.dumps(result,indent=2)+'\n')
    path.with_suffix('.json').write_text(json.dumps({'n':n,'edges':[list(e) for e in sorted(edges)]},indent=2)+'\n')
    return {k:v for k,v in result.items() if k!='uncovered_pairs'},edges

def main():
    allchecks=[]
    deleted=json.loads((HERE/'twin60_deflate59_run/candidate.json').read_text())['best_deleted_original_vertex']
    for name in ('deflated59','twin60'):
        report=json.loads((OUT/f'{name}.json').read_text());_,reference=read(Path(report['source']))
        n=report['n'];local=[]
        for idx,scan in enumerate(report['neighborhoods']):
            # Independent formula for the number of disjoint pairs of edges in
            # an 8-regular simple graph; rejected alternatives are then counted
            # explicitly by the enumerator.
            m=4*n;assert scan['unordered_edge_pairs']==m*(m-1)//2
            assert scan['disjoint_edge_pairs']==m*(m-1)//2-n*28
            assert scan['valid_distinct_switches']+scan['existing_edge_rejections']==2*scan['disjoint_edge_pairs']
            assert sum(scan['bad_pair_histogram'].values())==scan['valid_distinct_switches']
            improved=scan['best_distinct_neighbor_bad_pairs']<scan['seed_bad_pairs']
            path=OUT/(f'{name}.step{idx+1}.edges' if improved else f'{name}.best_distinct_neighbor.edges')
            checked,newedges=verify(path,scan['best_distinct_neighbor_bad_pairs'],reference,scan['best_change'],deleted if n==59 else None)
            local.append(checked)
            if improved:reference=newedges
        allchecks.append({'name':name,'complete_neighborhood_counts_consistent':True,'candidates':local})
    output={'independent_implementation':'ordinary adjacency sets and all-source BFS, no search bitset reuse','deleted_original_vertex_for_n59':deleted,'checks':allchecks}
    (OUT/'verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
