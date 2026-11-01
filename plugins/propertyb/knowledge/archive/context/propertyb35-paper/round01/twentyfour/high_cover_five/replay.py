"""Independent weighted-excess recursion and true degree-preserving orbit/transport audit.
Replays RAW ABC from35 expanded edge stubs, with no link quotas, DP, LP or position search.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
from collections import Counter
from math import factorial
import json,time,sys
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(32))
def main():
 st=time.time();masks=[t for t in range(32) if 2<=t.bit_count()<=4];patterns=[]
 def recover_patterns(j,budget,multi):
  if j==len(masks):
   if budget==0:patterns.append(dict(multi))
   return
  t=masks[j];weight=t.bit_count()-1
  for n in range(budget//weight+1):
   if n:multi[t]=n
   else:multi.pop(t,None)
   recover_patterns(j+1,budget-n*weight,multi)
  multi.pop(t,None)
 recover_patterns(0,3,{})
 assert len(patterns)==325;categories=Counter(tuple(sorted(t.bit_count() for t,n in p.items() for _ in range(n))) for p in patterns);assert categories=={(2,2,2):220,(2,3):100,(4,):5}
 expected=set();groups={};expected_orbit_counts={};dom=json.loads((HERE/'DOMAIN.json').read_text())
 for ds in ((10,8,8,8,8),(9,9,8,8,8)):
  group=[p for p in permutations(range(5)) if all(ds[i]==ds[p[i]] for i in range(5))];groups[ds]=group;reps=set()
  for multi in patterns:
   ns={t:0 for t in range(32)};ns[31]=1;ns.update(multi)
   for i,d in enumerate(ds):ns[1<<i]=d-1-sum(n for t,n in multi.items() if t>>i&1)
   assert sum(ns.values())==35 and ns[0]==0 and ns[31]==1 and min(ns.values())>=0;expected.add((ds,key(ns)));images=[]
   for p in group:
    move=lambda t:sum(1<<p[i] for i in range(5) if t>>i&1);images.append(key({move(t):n for t,n in ns.items()}))
   reps.add(min(images))
  expected_orbit_counts[str(ds)]=len(reps)
 assert len(expected)==650 and expected=={(tuple(r['degrees']),key(r['counts'])) for r in dom['labelled']};assert expected_orbit_counts=={'(10, 8, 8, 8, 8)':31,'(9, 9, 8, 8, 8)':50}
 assert len(dom['orbits'])==81
 orbit_canons=set()
 for r in dom['orbits']:
  ns={int(t):n for t,n in r['counts'].items()};ds=tuple(r['degrees']);images=[]
  for p in groups[ds]:
   move=lambda t:sum(1<<p[i] for i in range(5) if t>>i&1);images.append(key({move(t):n for t,n in ns.items()}))
  orbit_canons.add((ds,min(images)))
 assert len(orbit_canons)==81
 for r in dom['labelled']:
  rep=dom['orbits'][r['orbit']];p=r['from_representative_permutation'];ds=tuple(r['degrees']);assert p in [list(v) for v in groups[ds]];assert tuple(rep['degrees'])==ds
  move=lambda t:sum(1<<p[i] for i in range(5) if t>>i&1);assert key({move(int(t)):n for t,n in rep['counts'].items()})==key(r['counts'])
 fixed=json.loads((HERE/'FIXED.json').read_text());assert fixed['complete'] and len(fixed['cases'])==81;vals=[];by_degree={}
 for r in fixed['cases']:
  rep=dom['orbits'][r['id']];assert key(rep['counts'])==key(r['counts']) and rep['degrees']==r['degrees'];ns={int(t):n for t,n in r['counts'].items()};stubs=[frozenset(i+1 for i in range(5) if t>>i&1) for t,n in ns.items() for _ in range(n)];rows=independent_rows(24,tuple(r['positions']),stubs);assert len(stubs)==35 and len(rows)==24
  for a,b in zip(rows,r['rows']):assert (a['A'],a['B'],a['C'])==(Q(b['A']),Q(b['B']),Q(b['C']))
  value=sum(min(z['A'],z['B'],z['C']) for z in rows);assert value==Q(r['raw_ABC_bound']) and value<1;vals.append(value);by_degree.setdefault(str(tuple(r['degrees'])),[]).append(value)
 result=dict(status='PASS',scope=__doc__,independent_excess_solutions=325,category_counts={str(k):n for k,n in categories.items()},independent_labelled_count=650,true_degree_preserving_orbits=81,orbits_by_degree=expected_orbit_counts,transport_checks=650,raw_ABC_certificates=81,expanded_stubs_per_certificate=35,independent_ABC_rows=24*81,link_quota_deductions_used=0,common_denominator=str(factorial(19)),max_raw_ABC_bound=str(max(vals)),maxima_by_degree={d:str(max(v)) for d,v in by_degree.items()},elapsed_seconds=time.time()-st);(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
