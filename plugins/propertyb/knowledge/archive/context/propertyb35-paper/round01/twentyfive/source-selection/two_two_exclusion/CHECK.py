"""Exact scalar and local recoloring checks for the two-two source exclusion.
No hypergraph or source-coloring enumeration.
"""
from itertools import combinations,product
from pathlib import Path
import json,time
D=Path(__file__).resolve().parent;t0=time.process_time()
rows=[]
for e in range(4):
 for m in range(e+1):
  q=e-m
  for mu in range(m+1):
   for b in range(q+1):
    private_at_multi=b+q
    assert private_at_multi<=2*q
    meetU=m+private_at_multi+(13-e)
    assert meetU==13+b<=13+e-m
    gap=16*(8-mu)-6*(13+e-m)
    assert gap==50-16*mu-6*e+6*m
    assert gap>=50-10*m-6*e>=50-16*e>=2
    rows.append(dict(e=e,m=m,mu=mu,q=q,b=b,
                     private_at_multi=private_at_multi,meet_U_exact_bound=meetU,
                     meet_U_coarse_bound=13+e-m,pair_gap=gap))
assert len(rows)==35
maxpair=max(u*p for u in range(6) for p in range(6-u));assert maxpair==6
# x=0,y=1 have opposite initial colors; five other points have all possible colors.
# For every five-edge type, verify the complete classification of new monochromatic edges.
checked=0;new_bad=0
for bits in product((0,1),repeat=5):
 color=[0,1]+list(bits);after=[1,0]+list(bits)
 for edge in combinations(range(7),5):
  checked+=1
  proper=len({color[v] for v in edge})==2
  bad=len({after[v] for v in edge})==1
  if proper and bad:
   new_bad+=1
   moved=set(edge)&{0,1};assert len(moved)==1
   v=next(iter(moved))
   assert sum(color[w]==color[v] for w in edge)==1
assert checked==672
out=dict(scope=__doc__,status='PASS',scalar_domain='all 0<=e<=3, 0<=m<=e, 0<=mu<=m, 0<=b<=e-m; safe overapprox',
 scalar_rows=rows,scalar_row_count=len(rows),minimum_pair_gap=min(r['pair_gap'] for r in rows),
 maximum_U_P_pairs_per_five_edge=maxpair,
 local_swap_patterns=checked,new_bad_patterns=new_bad,
 every_new_bad_edge_has_unique_moved_minority=True,
 cpu_seconds=time.process_time()-t0)
(D/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='scalar_rows'},indent=2))
