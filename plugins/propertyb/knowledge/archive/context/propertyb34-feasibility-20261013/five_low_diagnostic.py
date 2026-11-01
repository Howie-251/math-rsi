"""Grok-suggested small T34 diagnostic; exact formulas, no hypergraph search."""
from pathlib import Path
from fractions import Fraction
import sys,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,rows,total_bound,json_value
from independent_structure_bounds import independent_rows
from enumerate_pair_partitions import enumerate_partitions,canonical_large_blocks,exact_types

data={}
for part in enumerate_partitions(5):
    canon=canonical_large_blocks(part,5)
    counts=exact_types(part,5,degree=6,edges=34)['counts_by_mask']
    for start in range(7,16):
        pos=tuple(range(start,start+5))
        p=Profile(25,5,pos,counts)
        value=total_bound(rows(p))
        if canon not in data or value<data[canon]['bound']:
            data[canon]=dict(large_blocks=canon,positions=pos,counts=counts,bound=value)
for r in data.values():
    p=Profile(25,5,r['positions'],r['counts'])
    stubs=[frozenset(i+1 for i in range(5) if t&(1<<i)) for t,n in r['counts'].items() for _ in range(n)]
    other=independent_rows(25,r['positions'],stubs)
    for a,b in zip(rows(p),other):
        assert all(a[k]==b[k] for k in ['k','A','B','C','bound'])
    r['independent_rows_agree']=True
vectors=[(e3,e4,e5) for e3 in range(13) for e4 in range(5) for e5 in range(3)
         if e3+3*e4+6*e5<=12 and 3*e3+8*e4+15*e5>=14]
out=dict(scope='32 labelled K5 decompositions, nine contiguous windows, no deductions since six-degree link has no bad pairs; no optimality beyond this window.',
         five_low_profiles=list(data.values()),
         grok_aggregate_type_counts=dict(feasible_integer_vectors=len(vectors),edge_saturated=sum(a+3*b+6*c==12 for a,b,c in vectors),
                                        equality14=[x for x in vectors if 3*x[0]+8*x[1]+15*x[2]==14]))
Path(__file__).with_name('FIVE_LOW_DIAGNOSTIC.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
print(json.dumps(json_value(out),ensure_ascii=False))

