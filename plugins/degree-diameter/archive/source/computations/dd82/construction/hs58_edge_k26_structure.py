#!/usr/bin/env python3
"""Verify the actual HS edge grid and all pairwise color incompatibilities."""
from pathlib import Path
from collections import Counter,deque
from itertools import combinations
import json,time
from twin59_to_58_deflation_verify import read_edges
HERE=Path(__file__).resolve().parent
OUT=HERE/'hs58_edge_k26_structure_run'
def main():
    start=time.process_time();OUT.mkdir(exist_ok=True)
    source=HERE/'petersen_all_matchings_run/candidate.best.edges'
    _,original=read_edges(source)
    vertices=sorted(set(range(40))|set(range(50,60)));old=set(vertices)
    edges={e for e in original if set(e)<=old};adj={u:set() for u in vertices}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    assert len(vertices)==50 and len(edges)==175 and Counter(map(len,adj.values()))=={7:50}
    distances=Counter();hscommon=Counter()
    for u in vertices:
        dist={u:0};queue=deque([u])
        while queue:
            a=queue.popleft()
            for v in adj[a]:
                if v not in dist:
                    dist[v]=dist[a]+1
                    queue.append(v)
        assert len(dist)==50
        for v in vertices:
            if u>=v:continue
            distances[dist[v]]+=1
            common=len(adj[u]&adj[v]);hscommon[common]+=1
            assert common==(0 if v in adj[u] else 1)
    assert distances=={1:175,2:1050}
    u,v=min(edges);X=sorted(adj[u]-{v});Y=sorted(adj[v]-{u})
    assert len(X)==len(Y)==6 and not set(X)&set(Y)
    R=sorted(old-{u,v}-set(X)-set(Y));rs=set(R)
    assert len(R)==36 and Counter(len(adj[w]&rs) for w in R)=={5:36}
    row={};column={};grid={}
    for w in R:
        nx=adj[w]&set(X);ny=adj[w]&set(Y)
        assert len(nx)==len(ny)==1
        row[w]=X.index(next(iter(nx)));column[w]=Y.index(next(iter(ny)))
        assert (row[w],column[w]) not in grid
        grid[row[w],column[w]]=w
    assert len(grid)==36
    pair_checks=[];reasons=Counter();compatible=[]
    for a,b in combinations(R,2):
        common=adj[a]&adj[b]
        common_r=sorted(common&rs)
        same_row=row[a]==row[b];same_column=column[a]==column[b]
        in_r_edge=b in adj[a]
        allowed=not(in_r_edge or common_r or same_row or same_column)
        if allowed:compatible.append([a,b])
        if in_r_edge:
            assert not common and not same_row and not same_column
            reason='adjacent_in_R';witness=[]
        else:
            assert len(common)==1
            witness=sorted(common);w=witness[0]
            assert w not in (u,v)
            if w in rs:
                assert not same_row and not same_column
                reason='common_neighbor_in_R'
            elif w in X:
                assert same_row and not same_column
                reason='same_X_row'
            else:
                assert w in Y and same_column and not same_row
                reason='same_Y_column'
        reasons[reason]+=1
        pair_checks.append({'vertices': [a,b],'reason':reason,'common_neighbor_witness':witness,'compatible_for_one_color':allowed})
    assert len(pair_checks)==630 and not compatible
    assert reasons=={'adjacent_in_R':90,'common_neighbor_in_R':360,'same_X_row':90,'same_Y_column':90}
    relabel={w:i for i,w in enumerate(vertices)}
    with (OUT/'hs50.edges').open('w') as out:
        out.write('50 175\n')
        for a,b in sorted(edges):out.write(f'{relabel[a]} {relabel[b]}\n')
    result={'source':str(source),'label_convention':'Original order60 labels unless explicitly relabelled',
      'hs50_edge_file':'hs50.edges','hs50_edge_file_vertex_to_original60':vertices,
      'hs50_degrees':{7:50},'hs50_distance_histogram':dict(distances),
      'hs50_common_neighbor_histogram':dict(hscommon),'selected_edge':[u,v],'X':X,'Y':Y,'R':R,
      'R_internal_degree_histogram':{5:36},'grid_rows_X_columns_Y':[[grid[i,j] for j in range(6)] for i in range(6)],
      'R_vertices_with_unique_X_and_Y_neighbor':36,
      'pair_count':len(pair_checks),'pair_obstruction_counts':dict(reasons),
      'allowed_color_class_compatibility_edges':compatible,'maximum_allowed_class_size':1,
      'six_vertex_color_classes':[],'six_class_partition_exists':False,
      'clique_enumeration_run':False,'exact_cover_search_run':False,
      'reason_searches_omitted':'All 630 pairs have a direct incompatibility witness, so the allowed-class graph is empty',
      'cpu_seconds':time.process_time()-start,'pair_checks':pair_checks}
    (OUT/'structure.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('pair_checks','R','grid_rows_X_columns_Y','hs50_edge_file_vertex_to_original60')},indent=2))
if __name__=='__main__':main()
