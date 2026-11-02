"""Meaningful whole-input CNF versus independent integer semantics; no solver."""
import json
from itertools import combinations
from pathlib import Path
import random
import encode
import check

HERE=Path(__file__).resolve().parent

def structured():
    edges=set(model['fixed']); W=encode.W; C=encode.C
    perm=[2,5,1,4,0,3]
    edges.update((W[1][i],W[2][perm[i]]) for i in range(6))
    ports={W[0][1],W[1][3]}
    edges.update({(6,W[0][1]),(11,W[1][3])})
    # Complete parent/C degrees of every original U,V vertex.
    for parents,portparent in ((encode.U,6),(encode.V,11)):
        remaining=[]
        for p in parents:
            degree=sum(p in ab for ab in edges)
            remaining.extend([p]*(8-degree))
        assert len(remaining)==28
        if parents==encode.V: remaining=remaining[9:]+remaining[:9]
        edges.update(encode.pair(p,c) for p,c in zip(remaining,C))
    # Each group covers all 28 C points, then uses its exact extra incidences.
    for group in W:
        slots=[w for w in group for _ in range(5-int(w in ports))]
        first=slots[:28]
        edges.update((w,c) for w,c in zip(first,C))
        for w in slots[28:]:
            c=next(c for c in C if (w,c) not in edges and sum((z,c) in edges for z in encode.WW)<4)
            edges.add((w,c))
    # Havel-Hakimi on the required C degrees, producing an actual undirected T.
    residual={c:8-sum(c in ab for ab in edges) for c in C}
    while any(residual.values()):
        c=max(residual,key=lambda x:(residual[x],x)); degree=residual[c];residual[c]=0
        neighbors=sorted((d for d in C if d!=c and residual[d]>0 and encode.pair(c,d) not in edges),key=lambda d:(-residual[d],d))[:degree]
        assert len(neighbors)==degree
        for d in neighbors: edges.add(encode.pair(c,d));residual[d]-=1
    # Sort C only. W matchings/port coordinates are transported unchanged.
    order=sorted(C,key=lambda c:tuple(int(encode.pair(p,c) in edges) for p in encode.U+encode.V),reverse=True)
    move={old:new for old,new in zip(order,C)}
    return {encode.pair(move.get(a,a),move.get(b,b)) for a,b in edges}

model=encode.build()
rng=random.Random(61)
samples=[('fixed_only',set(model['fixed'])),('all_free',model['fixed']|set(model['free'])),('random_sparse',model['fixed']|{ab for ab in model['free'] if rng.random()<.12}),('regular_frontend',structured())]
reports=[]
for name,edges in samples:
    data=dict(n=61,edges=[list(ab) for ab in sorted(edges)])
    direct=check.inspect(data,include_bfs=(name=='regular_frontend'))
    values=encode.assignment(model,data)
    rejected=encode.rejected_groups(model,values)
    expected=sorted(group for group,valid in direct['groups'].items() if not valid)
    assert rejected==expected,(name,rejected,expected)
    assert direct['fixed_branch_structure']
    for ab,terms in model['common_terms'].items():
        count=sum(encode.truth(t,values) for t in terms)
        assert count==direct['common'][ab]
        assert all(encode.truth(t,values)==(count>=j) for j,t in enumerate(model['thresholds'][ab]))
        assert encode.truth(model['covered'][ab],values)==direct['covered'][ab]
    if name=='regular_frontend':
        assert direct['groups']['all_original_degrees_8'] and direct['groups']['complete_h6_frontend']
        assert direct['groups']['C_parent_vectors_nonincreasing_lex']
        assert not direct['target61_verified']
        (HERE/'semantic_regular_fixture.json').write_text(json.dumps(data,indent=2)+'\n')
    reports.append(dict(name=name,edges=len(edges),rejected_groups=rejected,original_pairs_checked=1830,target61_verified=direct['target61_verified']))
result=dict(status='PASSED',solver_calls=0,variables=model['em'].nv,clauses=len(model['em'].clauses),primary_edge_variables=model['primary_count'],samples=reports,regular_fixture_is_target=False)
(HERE/'sanity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
