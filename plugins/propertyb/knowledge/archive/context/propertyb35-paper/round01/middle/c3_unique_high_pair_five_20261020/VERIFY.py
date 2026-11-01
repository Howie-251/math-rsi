"""Independent inclusive-pair/Mobius generation and425 original-index fixed replays."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
dom=json.loads((P/'DOMAIN.json').read_text());saved=json.loads((P/'RESULT.json').read_text())
PP=(3,5,6,9,10,12);CROSS=(5,6,9,10);TM=(7,11,13,14)
keys={};family_counts=Counter();high_mass=Counter()
for fid,fam in enumerate(dom['profile']['families']):
 mark=fam['marked_pair'];ds=fam['degrees'];other=[p for p in PP if p!=mark]
 for values in product(range(1,5),repeat=5):
  inclusive={mark:5,**dict(zip(other,values))}
  crosssum=sum(inclusive[p] for p in CROSS)
  if crosssum<14:continue
  for full in range(min(inclusive.values())+1):
   tri_max=(crosssum-14-4*full)//2
   if tri_max<0:continue
   # The actual inclusive identity itself implies tri_max<=1.
   assert tri_max<=1
   choices=[(0,0,0,0)]
   if tri_max==1:choices += [tuple(int(i==j) for i in range(4)) for j in range(4)]
   for triples in choices:
    mu=[0]*16;mu[15]=full
    for m,n in zip(TM,triples):mu[m]=n
    for p in PP:mu[p]=inclusive[p]-full-sum(n for m,n in zip(TM,triples) if m&p==p)
    if min(mu)<0 or mu[3]<1 or mu[12]<1 or sum(mu[p] for p in CROSS)<14:continue
    for v,d in enumerate(ds):mu[1<<v]=d-sum(n for m,n in enumerate(mu) if m.bit_count()>=2 and m>>v&1)
    mu[0]=35-sum(mu)
    if min(mu)<0:continue
    for p in PP:assert sum(n for m,n in enumerate(mu) if m&p==p)==inclusive[p]
    key=tuple(mu);keys.setdefault(key,[]).append(fid);family_counts[fid]+=1;high_mass[(full,sum(triples))]+=1
expected={tuple(z['counts']):z['families'] for z in dom['keys']}
assert keys==expected and len(keys)==425
assert saved['complete'] and saved['strict_count']==425 and saved['checked']==425
assert set(keys)=={tuple(z['counts']) for z in saved['cases']}
certs=[];maximum=Fraction()
for z in saved['cases']:
 mu=z['counts'];masks=[m for m,n in enumerate(mu) for _ in range(n)];assert len(masks)==35
 types=[frozenset(v+1 for v in range(4) if m>>v&1) for m in masks]
 rows=independent_rows(21,tuple(z['positions']),types);U=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction())
 assert U==Fraction(z['bound'])<1;maximum=max(maximum,U)
 certs.append(dict(counts=mu,families=z['families'],degrees=z['degrees'],expanded35_masks=masks,positions=z['positions'],bound=str(U),quota=0,rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rows]))
 assert time.process_time()-st<12,'12CPU independent replay budget'
out=dict(status='PASS_COMPLETE_DOMAIN_AND425_STRICT_FIXED_CERTIFICATES',scope=__doc__,families=14,domain_size=425,inclusive_to_exact_domain_equal=True,family_counts=dict(family_counts),high_mass={str(k):v for k,v in high_mass.items()},strict_certificates=425,maximum=str(maximum),replayed_rows=425*21,ordered_distinct_pairs_per_case=1190,cases=certs,cpu_seconds=time.process_time()-st)
(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='cases'})
