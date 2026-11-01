"""Fresh exact310 inclusive domain binding and all304 zero-quota strict certificates."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
saved=json.loads((P.parent/'RESULT.json').read_text());PP=(3,5,6,9,10,12);CR=(5,6,9,10);TM=(7,11,13,14)
keys=set()
for vv in product(range(1,5),repeat=6):
 I=dict(zip(PP,vv));cs=sum(I[p] for p in CR)
 if cs<13:continue
 for full in range(min(vv)+1):
  cap=(cs-13-4*full)//2
  if cap<0:continue
  assert cap<=1
  for tri in (0,*TM) if cap else (0,):
   mu=[0]*16;mu[15]=full
   if tri:mu[tri]=1
   for p in PP:mu[p]=I[p]-full-int(bool(tri) and tri&p==p)
   if min(mu)<0 or mu[3]<1 or mu[12]<1 or sum(mu[p] for p in CR)<13:continue
   for i in range(4):mu[1<<i]=10-sum(n for m,n in enumerate(mu) if m.bit_count()>=2 and m>>i&1)
   mu[0]=35-sum(mu)
   if min(mu)<0:continue
   keys.add(tuple(mu))
assert keys=={tuple(z['counts']) for z in saved['cases']} and len(keys)==310
strict=[z for z in saved['cases'] if z['strict']];assert len(strict)==304
cert=[];maximum=Fraction()
for z in strict:
 masks=[m for m,n in enumerate(z['counts']) for _ in range(n)];assert len(masks)==35
 types=[frozenset(i+1 for i in range(4) if m>>i&1) for m in masks]
 rows=independent_rows(21,tuple(z['positions']),types);U=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction())
 assert U==Fraction(z['bound'])<1;maximum=max(maximum,U)
 cert.append(dict(counts=z['counts'],expanded35_masks=masks,positions=z['positions'],bound=str(U),quota=0,rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rows]))
 assert time.process_time()-st<4.8,'5CPU audit cutoff'
out=dict(status='PASS_COMPLETE310_BINDING_AND304_STRICT_FIXED_REPLAYS',scope=__doc__,complete_domain=310,strict_certificates=304,remaining_six_types=len(saved['cases'])-len(strict),independent_domain_equal=True,all_strict_fixed_bounds_equal=True,maximum=str(maximum),replayed_rows=304*21,original_indices_per_case=35,ordered_distinct_pairs_per_case=1190,cases=cert,cpu_seconds=time.process_time()-st)
(P/'VERIFY_304.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='cases'})
