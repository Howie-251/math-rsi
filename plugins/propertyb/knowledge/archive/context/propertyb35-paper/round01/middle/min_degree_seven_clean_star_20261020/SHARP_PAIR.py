"""Two actual clean degree-seven stars in B: one fixed old-slot configuration."""
from pathlib import Path
from itertools import combinations_with_replacement,product
from fractions import Fraction
from collections import Counter
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
positive='--positive-F0' in sys.argv
prefix='SHARP_PAIR_POSITIVE' if positive else 'SHARP_PAIR'
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));sys.path.insert(0,str(ROOT/'computations'))
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
base=json.loads((P/'FIVE_RESULT.json').read_text())['nonstrict'][1]
assert base['traces']==[7,25,30] and base['attachments']==[4,7,7,7,6]
types=[]
for j in (1,2,4):
 s=[1]*5;s[0]+=1;s[j]+=1;types.append((j,tuple(s)))
domain=[]
for (j,s),(k,t) in combinations_with_replacement(types,2):
 for overlap in product(*(range(min(a,b)+1) for a,b in zip(s,t))):
  if sum(overlap)<1 or positive and overlap[0]<1:continue
  ns=Counter({int(m)<<2:n for m,n in base['counts'].items() if int(m).bit_count()!=1})
  for v,(a,b,c,d) in enumerate(zip(base['attachments'],s,t,overlap)):
   assert a-b-c+d>=0
   f=1<<(v+2);ns[f]=a-b-c+d;ns[f|1]=b-d;ns[f|2]=c-d;ns[f|3]=d
  assert sum(ns.values())==35 and min(ns.values())>=0
  ds=[sum(n for m,n in ns.items() if m>>v&1) for v in range(7)]
  assert ds==[7,7]+base['degrees']
  domain.append(dict(types=[j,k],s=s,t=t,overlap=overlap,pair_codegree=sum(overlap),counts=dict(ns),degrees=ds))
assert len(domain)==(240 if positive else 354)
pos=(20,21)+tuple(base['positions']);assert len(set(pos))==7
(P/(prefix+'_DOMAIN.json')).write_text(json.dumps(dict(scope=__doc__,positions=pos,domain_size=len(domain),cases=domain),indent=2)+'\n')
out=[]
for i,z in enumerate(domain):
 e=SubsetEngine(21,7,z['counts']);e.inv={p:(0,0,[]) for p in e.inv}
 lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
 for at in range(1,22):p=lock.get(at,0);U+=e.value(at,left,p);left|=p
 val=Fraction(U,e.D)
 masks=[m for m,n in z['counts'].items() for _ in range(n)];ts=[frozenset(v+1 for v in range(7) if m>>v&1) for m in masks]
 ir=independent_rows(21,pos,ts);own=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction());assert own==val
 rr=dict(**z,positions=pos,bound=str(val),strict=val<1,expanded35_masks=masks,independent_rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in ir]);out.append(rr)
 if i==0:print('PILOT',rr['types'],rr['overlap'],rr['bound'],'CPU',time.process_time()-st,flush=True)
 if val>=1:print('FIRST_NONSTRICT',rr['types'],rr['overlap'],rr['bound'],flush=True);break
 if time.process_time()-st>8:print('8CPU_STOP',flush=True);break
res=dict(status='COMPLETE_STRICT' if len(out)==len(domain) and all(z['strict'] for z in out) else 'STOPPED_ON_NONSTRICT' if out and not out[-1]['strict'] else 'BOUNDED_PREFIX',scope=__doc__,domain_size=len(domain),checked=len(out),positions=pos,cases=out,nonstrict=[z for z in out if not z['strict']],cpu_seconds=time.process_time()-st)
(P/(prefix+'_RESULT.json')).write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ('cases','nonstrict')})
