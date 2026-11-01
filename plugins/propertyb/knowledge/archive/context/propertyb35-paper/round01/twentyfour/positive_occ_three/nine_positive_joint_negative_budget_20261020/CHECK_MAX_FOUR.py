"""Reconstruct the unchanged seven E=3 types; exact distinct-target bounds for max-positive-occurrence four."""
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
old=json.loads((HERE.parent/'eighteen_one_triple/THREE_EDGE_CHECK.json').read_text())
edge_order=tuple(combinations(range(5),2))
parameters=[(u,v,t,b) for t in range(4) for b in range(21-t)
            for u in range(t+1) for v in range(min(b,3-u)+1)]
assert max(46*u+13*(t-u)+13*v+b-v for u,v,t,b in parameters)==155
assert max(16*u+4*(t-u)+4*v+b-v for u,v,t,b in parameters)==65
assert max(4*u+(t-u)+v for u,v,t,b in parameters)==12
rows=[]
for source in old['results']:
    masks=[];degree=[0]*5
    for (i,j),m in zip(edge_order,source['vector']):
        masks.extend([(1<<i)|(1<<j)]*m);degree[i]+=m;degree[j]+=m
    for i in range(5):masks.extend([1<<i]*(4-degree[i]))
    assert len(masks)==17 and len(masks)-sum(degree)//2==14
    candidates=[]
    for ids in combinations(range(17),4):
        coverage=0
        for p in ids:coverage|=masks[p]
        if coverage==31:candidates.append(ids)
    ie=sum((-1)**s.bit_count()*comb(sum(not m&s for m in masks),4)
           for s in range(32) if sum(not m&s for m in masks)>=4)
    assert len(candidates)==ie==source['C4_direct']
    pairs=Counter();triples=Counter()
    for ids in candidates:
        pairs.update(combinations(ids,2));triples.update(combinations(ids,3))
    highest=sorted((pairs[p] for p in combinations(range(17),2)),reverse=True)
    sums=[sum(highest[:u]) for u in range(4)]
    h3=max(triples.values(),default=0)
    cases=[dict(u=u,v=v,t=t,b=b,blocked=sums[u]+(t-u+v)*h3+b-v)
           for u,v,t,b in parameters]
    worst=max(cases,key=lambda c:c['blocked'])
    assert worst['blocked']<ie
    rows.append(dict(vector=source['vector'],graph_edges=source['graph_edges'],
                     orbit_size=source['orbit_size'],C4=ie,
                     top_three_pair_extensions=highest[:3],pair_top_sums=sums,h3=h3,
                     worst_case=worst,margin=ie-worst['blocked'],all_parameter_cases=cases))
assert len(rows)==7 and sum(row['orbit_size'] for row in rows)==220
result=dict(PASS=True,scope=__doc__,old_complete_domain_labels=220,orbits=7,
            parameter_cases_per_type=len(parameters),
            wide_E4_block_bound=155,no_matching_block_bound=65,C3_block_bound=12,
            rows=rows,minimum_E3_margin=min(r['margin'] for r in rows),
            minimum_margin_in_E_ge_4_branches=min(178-155,80-65,14-12))
(HERE/'CHECK_MAX_FOUR.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items() if k!='rows'})
for row in rows:print(row['graph_edges'],row['C4'],row['top_three_pair_extensions'],row['h3'],row['worst_case'],row['margin'])
