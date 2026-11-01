#!/usr/bin/env python3
"""Scalar source-transfer check plus a signed obstruction, never an H census."""
from itertools import product
from pathlib import Path
from fractions import Fraction
import json
sizes=[]
# Allow equal group sizes; all surviving disjoint three-group possibilities.
for a in range(2,5):
 for b in range(a,5):
  for c in range(b,5):
   if a+b+c<8: continue
   n=a*b*c; cap=7*a+1
   assert n>=8*a and n>cap
   sizes.append(dict(group_sizes=[a,b,c],candidates=n,blocker_incidence_cap=cap,margin=n-cap))
assert sizes
A=[{'f','g','a0','a1'},{'f','g','b0','b1'},{'h','c0','c1','c2'}]
small=[{'f'},{'g'},{'h'}]
triples=[set(q) for q in product(['a0','a1'],['b0','b1'],['c0','c1','c2'])]
N=small+triples
U=sorted(set.union(*A))
freq={x:sum(x in a for a in A)+sum(x in n for n in N) for x in U}
assert max(freq.values())==7
assert sum(map(len,A))-len(set.union(*A))==2
allowed=[]
for mask in range(1<<len(U)):
 R={U[i] for i in range(len(U)) if mask>>i&1}
 if all(R&a for a in A) and not any(n<=R for n in N):allowed.append(sorted(R))
assert not allowed
assert len(N)==15 and len(triples)==12
assert Fraction(3*(9-1),3*3**2)==Fraction(8,9)
out={'status':'PASS','scope':'scalar inequalities and one signed obstruction only',
 'two_forbidden_points_three_disjoint_groups':sizes,'three_positive_s3_D9_probability_bound':'8/9',
 'tau3_obstruction':{'positive_sets':[sorted(x) for x in A],
  'negative_singletons':[sorted(x) for x in small],'negative_triples':[sorted(x) for x in triples],
  'indexed_occurrence':freq,'max_occurrence':max(freq.values()),'ground_size':len(U),
  'checked_red_subsets':1<<len(U),'successful_red_sets':allowed,
  'positive_repeated_incidence_excess':2,
  'claims_not_made':['actual 23-point H realization','non-Property-B H','failure of existential source selection']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','scalar_group_types':len(sizes),
 'min_margin':min(x['margin'] for x in sizes),
 'signed_obstruction_ground_size':len(U),'signed_obstruction_subsets_checked':1<<len(U)},indent=2))
