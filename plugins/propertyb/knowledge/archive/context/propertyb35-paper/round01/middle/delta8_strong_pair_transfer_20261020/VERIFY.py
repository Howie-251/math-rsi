"""Independent full pair/triple domain reconstruction and all164 fixed bound replays."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
pairdata=json.loads((P/'PAIR_RESULT.json').read_text());tripledata=json.loads((P/'TRIPLE_RESULT.json').read_text())
source=json.loads((P.parent/'min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_RESULT.json').read_text())['jobs']
expected={}
for s in source:
 dd=Counter(s['degrees'])
 for x in sorted(dd):
  for y in sorted(dd):
   if x>y or x==y and dd[x]<2:continue
   for c in range(5,x+1):expected.setdefault((x,y,c),set()).add(s['spectrum_id'])
actual={(z['degrees'][0],z['degrees'][1],z['codegree']):set(z['spectrum_ids']) for z in pairdata['cases']}
assert expected==actual and len(actual)==100
tails={(tuple(z['degrees']),z['codegree']) for z in pairdata['nonstrict']}
assert tails=={((10,12),5),((10,13),5),((11,11),5),((11,12),5)}
expected3={}
for (du,dv),c in tails:
 ids=expected[(du,dv,c)]
 for sid in ids:
  s=next(r for r in source if r['spectrum_id']==sid);b=s['degrees'].count(8)
  assert du>8 and dv>8 and b>3*c
 # Without invoking a global lambda bound, the already strict pair instances
 # for8/du and8/dv exclude p/q>=5 for this actual original H.
 for d in (du,dv):
  for lam in range(5,9):
   z=next(z for z in pairdata['cases'] if z['degrees']==[8,d] and z['codegree']==lam)
   assert z['strict']
 for p in range(1,5):
  for q in range(1,5):
   ns={0:32-du-dv+p+q,1:8-p-q,2:du-5-p,4:dv-5-q,3:p,5:q,6:5,7:0}
   assert min(ns.values())>=0
   expected3[(du,dv,p,q)]={str(m):n for m,n in ns.items()}
actual3={(z['high_pair'][0],z['high_pair'][1],z['p'],z['q']):z['counts'] for z in tripledata['cases']}
assert expected3==actual3 and len(actual3)==64
certs=[];failed=[];rowcount=0
for kind,data,s in [('pair',pairdata['cases'],2),('triple',tripledata['cases'],3)]:
 for z in data:
  ns={int(m):n for m,n in z['counts'].items()};masks=[m for m,n in ns.items() for _ in range(n)];assert len(masks)==35
  types=[frozenset(v+1 for v in range(s) if m>>v&1) for m in masks]
  rr=independent_rows(21,tuple(z['positions']),types);U=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction())
  assert U==Fraction(z['bound']) and (U<1)==z['strict'];rowcount+=21
  key=dict(degrees=z['degrees'],codegree=z['codegree']) if kind=='pair' else dict(high_pair=z['high_pair'],p=z['p'],q=z['q'])
  if U<1:
   certs.append(dict(kind=kind,key=key,expanded35_masks=masks,positions=z['positions'],counts=ns,bound=str(U),quota=0,rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rr]))
  else:failed.append(dict(kind=kind,key=key,bound=str(U)))
 assert time.process_time()-st<12,'independent12CPU cutoff'
out=dict(status='PASS',scope=__doc__,spectra=15,pair_keys=100,triple_keys=64,strict_pair_certificates=96,strict_triple_certificates=40,all164_best_bounds_equal=True,all_replayed_rows=rowcount,ordered_distinct_pairs_per_input=1190,independent_actual_domain_equal=True,actual_clean_z_pool_valid_for_all_four_sources=True,strict_certificates=certs,nonstrict=failed,cpu_seconds=time.process_time()-st)
(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('strict_certificates','nonstrict')})
