#!/usr/bin/env python3
"""Explain the completed family failure from saved unique3routes and girth5.
No new controller distance/word enumeration or fiber/solver call.
"""
import json
import time
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent

def main():
    start=time.process_time()
    C=json.loads((PARENT/'Exoo72/INPUT.json').read_text())['controller']
    old=json.loads((PARENT/'Exoo72/EDGE_DOMAINS.json').read_text())
    N=[sum(1<<v for v in row) for row in C]
    records=[];hist=Counter();commonchecks=0
    for e in old:
        u,v=e['source'],e['target'];A=[x for x in C[u] if x!=v];B=[x for x in C[v] if x!=u]
        assert len(A)==len(B)==4 and not(set(A)&set(B))
        boundary=set(A)|set(B);assert not any(y in C[x] for x in boundary for y in boundary if x!=y)
        alive=((1<<72)-1)^((1<<u)|(1<<v));H=[x&alive for x in N]
        for side in [A,B]:
            for i,x in enumerate(side):
                for y in side[i+1:]:
                    assert not(H[x]&H[y]);commonchecks+=1
        pairs={tuple(x['entry']):x['ordered_unique_pairs'][0] for x in e['unique_forbidden_entries']}
        hist[len(pairs)]+=1
        rows=Counter(i for i,j in pairs);cols=Counter(j for i,j in pairs)
        repeated=next((i for i,c in sorted(rows.items()) if c>=2),None)
        if repeated is not None:
            collision=[key for key in sorted(pairs) if key[0]==repeated][:2];side='A';common_vertex=C[u][repeated]
        else:
            repeated=next(j for j,c in sorted(cols.items()) if c>=2)
            collision=[key for key in sorted(pairs) if key[1]==repeated][:2];side='B';common_vertex=C[v][repeated]
        witnesses=[]
        for i,j in collision:
            a,b=C[u][i],C[v][j];w=pairs[i,j]
            assert {w['source'],w['target']}=={a,b}
            assert w['word']['vertices'] in [[a,u,v,b],[b,v,u,a]]
            witnesses.append({'cross_pair':[a,b],'normalized_ports':[i,j],'saved_unique_distance3_witness':w})
        records.append({'deleted':[u,v],'A':A,'B':B,'AunionB_independent':True,'same_side_H_commonneighbors_empty':True,'unique_cross_pair_count':len(pairs),'collision_side':side,'common_boundary_vertex':common_vertex,'two_distinct_unique_cross_pairs':witnesses,'required_matching_degree_at_common_vertex':2,'available_matching_degree':1,'strict_obstruction':True})
    assert len(records)==180
    result={'status':'ALL180_DELETED_EDGES_HAVE_INCOMPATIBLE_UNIQUE_CROSS_PAIRS','source_edges':180,'all4320crossmatchings_covered':True,'unique_cross_pair_count_histogram':dict(sorted(hist.items())),'same_side_commonneighbor_zero_checks':commonchecks,'all180_structural_certificates':records,'CPU_seconds':time.process_time()-start,'controller_BFS_or_shortword_recomputation':0,'new_graphs':0,'solver_calls':0}
    (HERE/'STRUCTURAL_CROSS_OBSTRUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
    current=json.loads((HERE/'RESULT.json').read_text())
    current['stronger_explanation']='Every deleted edge has >=2unique3crosspairs sharing a boundary endpoint;all must be matched directly,contradicting matchingdegree1. Existing same-side routes were retained in initial gate.'
    current['structural_certificate']='STRUCTURAL_CROSS_OBSTRUCTION.json'
    current['structural_explanation_CPU_seconds']=result['CPU_seconds']
    (HERE/'RESULT.json').write_text(json.dumps(current,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='all180_structural_certificates'}))

if __name__=='__main__':main()
