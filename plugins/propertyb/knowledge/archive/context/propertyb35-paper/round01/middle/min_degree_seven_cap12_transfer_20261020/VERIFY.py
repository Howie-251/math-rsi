"""Separate inclusive/Mobius8888 domain, original35-index replay, and n1-first full moment enumeration with capacity-layer scalar formula."""
from pathlib import Path
from itertools import product,combinations_with_replacement
from collections import Counter
from math import comb
from fractions import Fraction
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
st=time.process_time();q=json.loads((P/'QUAD8888_RESULT.json').read_text());r=json.loads((P/'RESULT.json').read_text());proj=json.loads((P/'PROJECTION.json').read_text())
# Full actual quad domain by degree counts, not selecting4 among21 indices.
for j in proj:
 ds=Counter(j['degrees']);qs=[v for v in combinations_with_replacement(range(7,14),4) if not (Counter(v)-ds)]
 assert qs==list(map(tuple,j['all_actual_selected_quads']))
# Alternative domain uses inclusive6pair variables; exactly1 triple or0; Mobius recovery.
pairs=(3,5,6,9,10,12);cross=(5,6,9,10);tris=(7,11,13,14);keys=set()
for cv in product(range(1,5),repeat=4):
 if sum(cv)<13:continue
 for A,B in product(range(1,5),repeat=2):
  inc={3:A,12:B,**dict(zip(cross,cv))}
  for tri in (0,*tris):
   ns=[0]*16
   if tri:ns[tri]=1
   for pair,n in inc.items():ns[pair]=n-int(bool(tri) and tri&pair==pair)
   if min(ns)<0 or ns[3]<1 or ns[12]<1 or sum(ns[m] for m in cross)<13:continue
   for i in range(4):ns[1<<i]=8-sum(n for m,n in inc.items() if m>>i&1)+int(bool(tri) and tri>>i&1)
   ns[0]=35-32+sum(inc.values())-int(bool(tri))
   if min(ns)>=0:keys.add(tuple(ns))
assert keys==set(map(tuple,q['labeled_keys'])) and len(keys)==10
rows=[]
for z in q['cases']:
 masks=[m for m,n in enumerate(z['counts']) for _ in range(n)];assert len(masks)==35
 types=[frozenset(i+1 for i in range(4) if m>>i&1) for m in masks]
 rr=independent_rows(21,tuple(z['best']['positions']),types);v=sum((min(x['A'],x['B'],x['C']) for x in rr),Fraction());assert v==Fraction(z['best']['bound'])<1
 rows.append({'counts':z['counts'],'expanded35_masks':masks,'positions':z['best']['positions'],'bound':str(v),'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in x.items()} for x in rr]})
(P/'QUAD8888_VERIFY_ROWS.json').write_text(json.dumps(rows,indent=2)+'\n')
quadcpu=time.process_time()-st
results=[]
for j in r['jobs']:
 ds=j['degrees'];W=sum(d*(d-1)//2 for d in ds);lo_tau=max(0,4*(max(ds)-10));coef=(sum(sorted(ds,reverse=True)[:6])-6)//2
 # Cost independently formed as a sorted multiset of every actual pointpair incidence.
 costs=sorted(d for d in ds for _ in range(comb(d,2)));prefix=[0]
 for d in costs:prefix.append(prefix[-1]+d)
 count=0;fails=[];maximum=-1
 for n1 in range(397,526):
  b,rem=divmod(2*n1,30);fparts=[rem//5+int(i<rem%5) for i in range(5)];Pbox=360*b+sum(fparts[i]*fparts[k] for i in range(5) for k in range(i))
  for t in range((W-n1)//4+1):
   lo=max(0,-((-2*lo_tau+W-280+8*t-n1)//3),W+n1-1190-2*t)
   hi=min((560-W-8*t+n1)//3,(W-n1-4*t)//3)
   if (lo-W+n1)%2:lo+=1
   for m in range(lo,hi+1,2):
    tau=(W-280+3*m+8*t-n1)//2;n2=(W-n1-3*m-4*t)//2;n0=595-(W+n1-m-2*t)//2
    assert min(n0,n2,m,t)>=0 and lo_tau<=tau<=140 and n0+n1+n2+m+t==595
    caps=(33*n0,35*n1-prefix[n1],coef*n2,12*m,4*t)
    # Layer-cake identity for optimal allocation; no greedy filling reused.
    v=6864*n1+sum(dw*min(Pbox,sum(caps[k:])) for k,dw in enumerate((36,84,210,462,924)))
    count+=1;maximum=max(maximum,v)
    if v>=5445440:fails.append({'n':[n0,n1,n2,m,t],'tau':tau,'twice_L':v})
 assert count==j['complete_domain'] and maximum==j['maximum_twice_L']
 assert sorted(fails,key=str)==sorted(j['survivors'],key=str)
 results.append({'spectrum_id':j['spectrum_id'],'complete_keys':count,'maximum_twice_L':maximum,'survivors':fails})
 assert time.process_time()-st<16
out={'status':'PASS','scope':__doc__,'all81_actual_quad_projections_independently_checked':True,'quad8888_labeled_domain':len(keys),'quad8888_original35_fixed_certificates':len(rows),'quad8888_independent_rows':21*len(rows),'quad8888_maximum':str(max(Fraction(x['bound']) for x in rows)),'quad_verify_cpu_seconds':quadcpu,'scalar_jobs':results,'total_scalar_keys':sum(j['complete_keys'] for j in results),'scalar_domains_and_maxima_and_full_survivor_lists_equal':True,'cpu_seconds':time.process_time()-st}
(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
