"""Fixed8 old-layout pilot, then complete actual t0/pq domain if cheap."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(P))
from PAIRS import bound
# PAIRS is discovery code; only its deterministic arithmetic helper is used.
pairdata=json.loads((P/'PAIR_RESULT.json').read_text())
base=[(10,11,21),(1,11,12),(1,21,9),(11,1,21)]
menu=sorted(set(base+[tuple(22-k for k in pos) for pos in base]));assert len(menu)==8
strict_pairs={(tuple(z['degrees']),z['codegree']) for z in pairdata['cases'] if z['strict']}
domain=[]
for r in pairdata['nonstrict']:
 du,dv=r['degrees'];c=r['codegree'];assert c==5
 for p in range(1,9):
  for q in range(1,9-p):
   # Non-B permits rejecting only strong-pair gates already strict independently.
   if (tuple(sorted((8,du))),p) in strict_pairs or (tuple(sorted((8,dv))),q) in strict_pairs:continue
   ns={0:32-du-dv+p+q,1:8-p-q,2:du-5-p,4:dv-5-q,3:p,5:q,6:5,7:0}
   if min(ns.values())<0:continue
   assert sum(ns.values())==35
   dd=[sum(n for m,n in ns.items() if m>>v&1) for v in range(3)]
   assert dd==[8,du,dv]
   assert sum(n for m,n in ns.items() if m&3==3)==p
   assert sum(n for m,n in ns.items() if m&5==5)==q
   assert sum(n for m,n in ns.items() if m&6==6)==5 and ns[7]==0
   domain.append(dict(high_pair=[du,dv],p=p,q=q,counts=ns,spectrum_ids=r['spectrum_ids']))
assert len(domain)==64
out=[]
for idx,r in enumerate(domain):
 vals=[(bound(r['counts'],pos),pos) for pos in menu];value,pos=min(vals)
 z=dict(**r,positions=pos,bound=str(value),strict=value<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]);out.append(z)
 if idx==0:
  pilot=dict(scope='Single actual first t0 inventory, before full64 scan',case=z,menu=menu,cpu_seconds=time.process_time()-st)
  (P/'TRIPLE_PILOT.json').write_text(json.dumps(pilot,indent=2)+'\n');print('PILOT',z['high_pair'],r['p'],r['q'],z['bound'],flush=True)
 assert time.process_time()-st<8,'bounded triple arithmetic cutoff'
res=dict(status='COMPLETE_FIXED8_THREE_LOCK_DOMAIN',scope=__doc__,menu=menu,domain_size=len(domain),strict_count=sum(z['strict'] for z in out),nonstrict=[z for z in out if not z['strict']],cases=out,cpu_seconds=time.process_time()-st)
(P/'TRIPLE_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ('cases','nonstrict')});print('NONSTRICT',[(z['high_pair'],z['p'],z['q'],z['bound']) for z in res['nonstrict']])
