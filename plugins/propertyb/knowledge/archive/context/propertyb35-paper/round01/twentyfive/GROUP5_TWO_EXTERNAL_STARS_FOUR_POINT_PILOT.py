"""Only inventories 1 and 9: four external points of one singleton-trace edge.
Cross-group pairs must be surviving seven-lock pairs. Forgetting within-group
conditions gives a necessary complete-bipartite cut on four partition copies.
No full twenty-point arrangement is searched.
"""
from pathlib import Path
from itertools import combinations_with_replacement,combinations
from collections import Counter
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();data=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_ALL_TRACES.json').read_text())['results'];six=json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text());cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());out=[]
for ident in [1,9]:
 mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};nu={t:(5-t.bit_count())*c for t,c in mu.items() if t};unique={t for t,c in mu.items() if t and c==1};zs=[z for z in data if z['id']==ident];Ts=sorted({z['T'] for z in zs});res={T:{frozenset([tuple(sorted(z['P'])),tuple(sorted(z['Q']))]) for z in zs if z['T']==T and Q(z['bound'])>=1} for T in Ts};initial={tuple(sorted(p)) for p in next(f['residual_partitions'] for f in six['families'] if f['id']==ident)};active=set(initial);rounds=[]
 while True:
  remove=set();stats=[]
  for T in Ts:
   pp=sorted(p for p in active if T in p);cap={p:min(min(nu[t] for t in p),1 if len(set(p)&unique)>=3 else 20) for p in pp};valid=[];checked=0
   for quadruple in combinations_with_replacement(pp,4):
    checked+=1;mult=Counter(quadruple)
    if any(n>cap[p] for p,n in mult.items()):continue
    if any(len(set(quadruple[i])&set(quadruple[j])&unique)>=3 for i,j in combinations(range(4),2)):continue
    cut=None
    for mask in range(1,8):
     side={i+1 for i in range(3) if mask>>i&1}
     if all(frozenset([quadruple[i],quadruple[j]]) in res[T] for i in side for j in set(range(4))-side):cut=mask;break
    if cut is not None:valid.append(dict(partitions=[list(p) for p in quadruple],cut_mask_on_vertices_1_2_3=cut))
   supported={tuple(p) for z in valid for p in z['partitions']};missing=set(pp)-supported;remove|=missing
   stats.append(dict(T=T,eligible_partitions=len(pp),quadruples_checked=checked,valid_multisets=valid,unsupported=[list(p) for p in sorted(missing)]))
  rounds.append(dict(active=len(active),by_trace=stats,removed=[list(p) for p in sorted(remove)]))
  if not remove:break
  active-=remove
 missing=[t for t,c in mu.items() if t and c and not any(t in p for p in active)]
 out.append(dict(id=ident,rounds=rounds,remaining_partitions=[list(p) for p in sorted(active)],missing_required_traces=missing,eliminated=bool(missing)))
summary=dict(scope=__doc__,inventories=[1,9],eliminated_ids=[r['id'] for r in out if r['eliminated']],elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_TWO_EXTERNAL_STARS_FOUR_POINT_PILOT.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2));print([(r['id'],len(r['remaining_partitions']),r['missing_required_traces'],[(z['active'],len(z['removed'])) for z in r['rounds']]) for r in out])
