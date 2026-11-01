"""Independent exact pair/triple extension counts on the unchanged seven E3 types."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
old=json.loads((HERE.parent/'eighteen_one_triple/THREE_EDGE_CHECK.json').read_text())
edges=tuple(combinations(range(5),2));rows=[]
for row in old['results']:
    g=row['vector'];degree=[0]*5;masks=[]
    for (u,v),count in zip(edges,g):
        masks.extend([(1<<u)|(1<<v)]*count)
        degree[u]+=count;degree[v]+=count
    for v,d in enumerate(degree):masks.extend([1<<v]*(4-d))
    assert len(masks)==17
    candidates=[]
    for ids in combinations(range(17),4):
        cover=0
        for i in ids:cover|=masks[i]
        if cover==31:candidates.append(ids)
    ie=0
    for selected in range(32):
        left=sum(not mask&selected for mask in masks)
        ie+=(-1)**selected.bit_count()*(comb(left,4) if left>=4 else 0)
    assert len(candidates)==ie==row['C4_direct']==row['C4_IE']
    pairs=Counter();triples=Counter()
    for ids in candidates:
        pairs.update(combinations(ids,2));triples.update(combinations(ids,3))
    h2=max(pairs.values(),default=0);h3=max(triples.values(),default=0)
    cases=[{'r':r,'b':b,'blocked_upper_bound':h2*r+h3*(2-r)+h3*b+(18-b)}
           for r in range(3) for b in range(5-r)]
    worst=max(cases,key=lambda z:z['blocked_upper_bound'])
    margin=ie-worst['blocked_upper_bound']
    assert margin>0
    rows.append({'vector':g,'graph_edges':row['graph_edges'],'old_orbit_size':row['orbit_size'],
                 'C4':ie,'maximum_pair_extension':h2,'maximum_triple_extension':h3,
                 'worst_case':worst,'margin':margin,'all_cases':cases})
p=F(7,16)
low=2*p**3+18*p**4
assert low==F(27097,32768)<1
assert len(rows)==7 and sum(r['old_orbit_size'] for r in rows)==220
assert max(44+33*r+12*b for r in range(3) for b in range(5-r))==134<178
assert max(26+12*r+3*b for r in range(3) for b in range(5-r))==56<80
result={'scope':__doc__,'reused_complete_old_domain_labels':220,'old_orbits':7,
        'low_occurrence_bound':str(low),'rows':rows,'minimum_margin':min(r['margin'] for r in rows),
        'status':'PASS'}
(HERE/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
