"""Small exact formulas for the retrospective; no hypergraph/position search."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

cases=[]
for v,m,cap in [(19,33,1003),(19,34,None),(20,34,None)]:
    if cap is None:
        excess=10*m-choose(v,2)
        cap=m*(m-1)-2*max(0,(excess+5)//6)
    rows=[]
    for k in range(1,v+1):
        a=F(m*choose(k-1,4),choose(v,5))
        b=F(m*choose(v-k,4),choose(v,5))
        c=F(cap*choose(k-1,4)*choose(v-k,4),v*choose(v-1,4)*choose(v-5,4))
        rows.append(dict(k=k,A=str(a),B=str(b),C=str(c),bound=str(min(a,b,c))))
    cases.append(dict(v=v,edge_count=m,ordered_singleton_cap=cap,
                      bound=str(sum((F(r['bound']) for r in rows),F(0))),rows=rows))
overlaps=[]
for v in (17,18):
    red=v//2
    counts=[]
    for t in range(5):
        u=10-t
        count=(2*choose(v-10,red-5) if t==0 else
               choose(v-u,red-u)+choose(v-u,red))
        counts.append(count)
    overlap=F(min(counts),choose(v,red))
    overlaps.append(dict(v=v,red=red,sample_count=choose(v,red),
                         counts_by_intersection_size=counts,
                         least_overlap=str(overlap),union_bound=str(1-overlap)))
threshold_rows=[]
for cap in range(964,1065):
    v=19; m=34
    bound=sum((min(F(m*choose(k-1,4),choose(v,5)),
                   F(m*choose(v-k,4),choose(v,5)),
                   F(cap*choose(k-1,4)*choose(v-k,4),v*choose(v-1,4)*choose(v-5,4)))
               for k in range(1,v+1)),F(0))
    assert bound==F(170170+63*cap,230945)
    threshold_rows.append((cap,str(bound)))
result=dict(scope='Exact formula diagnostics; no T34 formal proof and no hypergraph search.',
            no_lock_cases=cases,small_vertex_overlap=overlaps,
            nineteen_cap_threshold=dict(checked_integer_range=[964,1064],
                formula='(170170+63*cap)/230945',
                strict_caps_in_checked_range=[c for c,b in threshold_rows if F(b)<1],
                boundary_values=threshold_rows[:2]))
Path(__file__).with_name('NO_LOCK_BOUNDARY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'no_lock':[(r['v'],r['edge_count'],r['ordered_singleton_cap'],r['bound']) for r in cases],
                  'overlap':[(r['v'],r['least_overlap'],r['union_bound']) for r in overlaps]}))
