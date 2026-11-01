"""One 19-point weak-partition prototype; no hypergraph or matrix search."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from time import process_time
import json

t0=process_time()
merged={(0,1),(1,0)}
points=['x']+[(i,j) for i in range(5) for j in range(5)
              if i!=j and (i,j) not in merged]
def label(cell):
    return 0 if cell in merged else points.index(cell)
rows=[sum(1<<v for v in {label((i,j)) for j in range(5) if j!=i}) for i in range(5)]
cols=[sum(1<<v for v in {label((i,j)) for i in range(5) if i!=j}) for j in range(5)]
assert len(points)==19 and all(m.bit_count()==4 for m in rows+cols)
assert Counter(sum(bool(m>>i&1) for m in rows) for i in range(19))=={1:18,2:1}
tests={
    'shared_repeat_hits_all_blocks':['x',(2,3),(3,4),(4,2)],
    'no_repeat_common_four_transversal':[(0,2),(1,3),(2,0),(3,1)],
    'one_complete_row':[(4,0),(4,1),(4,2),(4,3)],
}
masks={name:sum(1<<points.index(p) for p in ps) for name,ps in tests.items()}
stats=Counter()
marked={name:Counter() for name in tests}
for blue_set in combinations(range(19),9):
    blue=sum(1<<i for i in blue_set)
    bp=any(blue&m==m for m in rows) and any(blue&m==0 for m in rows)
    bq=any(blue&m==m for m in cols) and any(blue&m==0 for m in cols)
    stats['P']+=bp;stats['Q']+=bq;stats['both']+=bp and bq
    for name,T in masks.items():
        if not blue&T:
            marked[name]['E']+=1
            marked[name]['E_and_P']+=bp
            marked[name]['E_and_Q']+=bq
            marked[name]['E_and_both']+=bp and bq
            marked[name]['E_and_union']+=bp or bq
N=comb(19,9)
assert N==92378 and stats['P']==stats['Q']==7542
assert marked['shared_repeat_hits_all_blocks']['E_and_union']==0
assert all(v['E']==5005 for v in marked.values())
assert comb(15,9)==5005 and comb(15,5)==3003
assert comb(14,9)+comb(14,4)==3003
assert 3*7542+20*3003-5005==77681
assert 77681+1001*14==91695<N
assert 77681+1001*15==92696>N
out={
    'status':'PASS','scope':'one shared-repeat weak row/column prototype',
    'points':points,'row_masks':rows,'column_masks':cols,
    'balanced_samples':N,'conflict_counts':dict(stats),
    'single_conflict_probability':str(Fraction(7542,N)),
    'marked_cases':{name:{'points':tests[name],**dict(v)} for name,v in marked.items()},
    'raw_actual_gate_numerator':'77681+1001*(2*min(d_u,d_v)-5*alpha)',
    'strict_integer_threshold':'2*min(d_u,d_v)-5*alpha <= 14',
    'uniform_positive_marked_overlap_false_in_this_prototype':True,
    'original_Hs_enumerated':0,'cpu_seconds':process_time()-t0,
}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('points','row_masks','column_masks')},indent=2))
