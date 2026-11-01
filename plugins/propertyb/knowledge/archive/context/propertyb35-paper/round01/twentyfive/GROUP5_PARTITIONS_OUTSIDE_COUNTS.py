"""Short outside-degree and pair-budget checks on the 22 saved partition witnesses.
No outer-point labels or group labels are assigned. A passing witness is only
a necessary-condition witness, never a realization of the full hypergraph.
"""
from pathlib import Path
from itertools import combinations
from math import comb
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());dec=json.loads((P/'GROUP5_PARTITIONS.json').read_text());out=[]
def beta(q,m):
 a,b=divmod(q,m);return m*comb(a,2)+a*b
for r in dec['results']:
 if r['status']!='FEASIBLE':continue
 mu={int(t):c for t,c in cat['representatives'][r['id']]['counts'].items()};co=Counter();ky=Counter()
 for p in r['partition_multiset']:
  k=len(p['blocks']);ky[k]+=p['multiplicity']
  for t,u in combinations(p['blocks'],2):co[min(t,u),max(t,u)]+=p['multiplicity']
 lower=sum(beta(c,mu[t]*mu[u]) for (t,u),c in co.items())
 L=sum(c*comb(5-t.bit_count(),2) for t,c in mu.items() if t)
 empty=mu.get(0,0)
 assert L+10*empty==230
 ksum=sum(k*c for k,c in ky.items());assert 140-ksum==5*empty
 out.append(dict(id=r['id'],external_degree_identities_hold=True,partition_block_count_spectrum=dict(ky),repeated_external_pair_lower_bound_for_saved_witness=lower,repeat_budget=40))
summary=dict(scope=__doc__,saved_witnesses=22,all_22_degree_and_total_pair_identities_hold=True,witnesses_exceeding_repeat_budget=[r['id'] for r in out if r['repeated_external_pair_lower_bound_for_saved_witness']>40],maximum_repeat_lower_bound=max(r['repeated_external_pair_lower_bound_for_saved_witness'] for r in out),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_PARTITIONS_OUTSIDE_COUNTS.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2))
