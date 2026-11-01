"""Replay one MILP witness without importing its coefficient/generator code."""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
from time import process_time
import json

start=process_time()
P=Path(__file__).parent
data=json.loads((P/'MILP_RESULT.json').read_text())
entries=data['nonzero']
assert sum(v['count'] for v in entries)==29
cols=[sum(v['count']*v['occupancy'][i] for v in entries) for i in range(6)]
cross=[sum(v['count']*v['occupancy'][i]*v['occupancy'][j] for v in entries)
       for i,j in combinations(range(6),2)]
assert min(cols)>=20 and min(cross)>=16
W=sum(v['count']*sum(comb(n,2) for n in v['occupancy']) for v in entries)
assert W==40
fixed=[]
checks=0
for pair in combinations(range(6),2):
    remaining=[i for i in range(6) if i not in pair]
    base=sum(15 << (4*i) for i in pair)
    count=0
    for v in entries:
        edge=sum(1 << (4*i+j) for i,n in enumerate(v['occupancy']) for j in range(n))
        for selected in product(range(4),repeat=4):
            blue=base | sum(1 << (4*i+j) for i,j in zip(remaining,selected))
            count+=v['count']*int(not(edge&blue) or (edge&blue)==edge)
            checks+=1
    fixed.append(Q(count,256))
assert all(v>=1 for v in fixed)
assert [str(v) for v in fixed]==[v['bound'] for v in data['fixed_A_bounds']]

# These six type probabilities were independently sampled in CHECK.py.
parts=[(1,1,1,1,1,0),(2,1,1,1,0,0),(2,2,1,0,0,0),
       (3,1,1,0,0,0),(3,2,0,0,0,0),(4,1,0,0,0,0)]
B=[Q(1,16),Q(1,24),Q(1,36),Q(0),Q(0),Q(0)]
C=[Q(11,256),Q(7,96),Q(3,32),Q(31,384),Q(1,12),Q(1,24)]
bytype={p:0 for p in parts}
for row in entries:
    p=tuple(sorted(row['occupancy'],reverse=True))
    bytype[p]+=row['count']
b=sum(bytype[p]*v for p,v in zip(parts,B))
c=sum(bytype[p]*v for p,v in zip(parts,C))
assert b==Q(data['B_bound'])>=1 and c==Q(data['C_bound'])>=1
result=dict(status='PASS',scope='one saved 246-profile MILP witness only',
            original_H_claim=False,nonzero_profiles=len(entries),
            independent_fixed_pair_edge_sample_checks=checks,
            type_counts=[bytype[p] for p in parts],W=W,
            all_fifteen_A_bounds=[str(v) for v in fixed],
            minimum_A=str(min(fixed)),B=str(b),C=str(c),
            cpu_seconds=process_time()-start)
(P/'VERIFY_MILP_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
