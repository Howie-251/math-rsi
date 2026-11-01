"""Stdlib fulltarget exact verifier, independent of LP build/solver code."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from collections import defaultdict
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
old=json.loads((HERE.parent/'positive_occ_three/eight_mixed_eighteen/SMALL_GRAPH_CHECK.json').read_text())['rows']
new=json.loads((HERE/'SOLVE_TWO_E2.json').read_text())
expected={'old59_%d_E2'%i:r for i,r in enumerate(old) if r['E']==2}
assert len(expected)==2 and {r['name'] for r in new['rows']}==set(expected)
checked=0;bounds=[]
for r in new['rows']:
 A=list(map(set,expected[r['name']]['sets']));assert [sorted(a) for a in A]==r['sets']
 U=sorted(set.union(*A));assert U==list(range(len(U)))
 reds={frozenset(q) for k in (3,4) for q in combinations(U,k) if all(set(q)&a for a in A)}
 assert reds==set(map(frozenset,r['candidate_red_sets']))
 c=r['dual_certificate'];w={frozenset(p['red_set']):F(p['weight']) for p in c['coverage_weights']}
 assert set(w)<=reds and all(x>=0 for x in w.values()) and sum(w.values())==1
 beta=list(map(F,c['budget_weights']));assert len(beta)==3+len(U) and all(x>=0 for x in beta)
 assert not c['upper_bound_weights']
 lhs={k:defaultdict(F) for k in (2,3,4)}
 for red,x in w.items():
  for k in lhs:
   for q in combinations(red,k):lhs[k][frozenset(q)]+=x
 for k,types in ((2,('N2',)),(3,('T3','Bx3')),(4,('N4',))):
  for q in combinations(U,k):
   common=beta[2]+sum(beta[3+v] for v in q)
   for typ in types:
    rhs=common+int(typ in ('N2','T3'))*beta[0]+int(typ in ('N2','Bx3'))*beta[1]
    assert lhs[k][frozenset(q)]<=rhs;checked+=1
 B=[2,4,21]+[7-sum(v in a for a in A) for v in U]
 assert B==r['budgets'];bound=sum(x*y for x,y in zip(B,beta))
 assert bound==F(c['coverage_upper_bound']) and bound<1;bounds.append(str(bound))
out={'status':'PASS','old59_E2_domain_keys_exact':True,'typed_target_columns_checked':checked,'exact_bounds':bounds,'upper_weights_empty':True,'no_scipy_or_discovery_import':True,'cpu_seconds':time.process_time()-start}
(HERE/'VERIFY_TWO_E2.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
