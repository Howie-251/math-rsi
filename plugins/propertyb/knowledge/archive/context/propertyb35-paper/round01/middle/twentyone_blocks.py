"""Fixed-pattern direct colour count for the actual degree5 five-four-block link.
Verifies two elementary colour ensembles; no full hypergraph enumeration.
"""
from itertools import combinations,product
from fractions import Fraction as Q
from pathlib import Path
import json,time
HERE=Path(__file__).parent
PATTERNS=[(1,1,1,1,1),(2,1,1,1,0),(2,2,1,0,0),(3,1,1,0,0),(3,2,0,0,0),(4,1,0,0,0)]
def masks(parts):return [sum(1<<(4*i+j) for i,a in enumerate(parts) for j in range(a))]
def mono(edge,red):return edge&red==edge or not edge&red
states2=[sum(sum(1<<(4*i+j) for j in p) for i,p in enumerate(ps)) for ps in product(list(combinations(range(4),2)),repeat=5)]
states3=[sum(sum(1<<(4*i+j) for j in range(4) if j!=excluded) for i,excluded in zip(groups,blues)) for groups in combinations(range(5),3) for blues in product(range(4),repeat=3)]
assert len(states2)==7776 and len(states3)==640
rows=[]
for p in PATTERNS:
 e=masks(p)[0];a=sum(mono(e,r) for r in states2);b=sum(mono(e,r) for r in states3)
 rows.append(dict(pattern=p,balanced_count=a,balanced_probability=str(Q(a,len(states2))),three_red_count=b,three_red_probability=str(Q(b,len(states3)))))
assert [r['three_red_count'] for r in rows]==[10,13,28,49,88,112]
assert [r['balanced_count'] for r in rows]==[486,324,216,0,0,0]
witness=dict(counts=[8,0,22,0,0,0],balanced_bound=str(8*Q(1,16)+22*Q(1,36)),three_red_bound=str(Q(8*10+22*28,640)),scope='necessary count-vector relaxation only; no actual hypergraph claimed')
result=dict(status='PASS',scope=__doc__,balanced_states=len(states2),three_red_states=len(states3),rows=rows,remaining_relaxation=witness)
(HERE/'TWENTYONE_BLOCK_COUNTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
