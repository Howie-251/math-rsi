"""Actual exclusive2+2 quadruples with one marked inclusive pair5, others<=4."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
PAIRS=(3,5,6,9,10,12);CROSS=(5,6,9,10);TRIPLES=(7,11,13,14)
QUADS=[(10,12,9,8),(10,12,8,8),(11,11,9,8),(11,11,8,8),(10,13,8,8),(11,12,8,8)]
MENU=((8,9,20,21),(9,10,20,21),(9,20,10,21))
def degrees(ns):return tuple(sum(n for m,n in enumerate(ns) if m>>v&1) for v in range(4))
def fixed(e,pos):
 lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
 for k in range(1,22):p=lock.get(k,0);U+=e.value(k,left,p);left|=p
 return Fraction(U,e.D)
families=[];keys={};full_high_shapes=Counter()
for qid,(du,dv,da,db) in enumerate(QUADS):
 for role in ('same','cross'):
  orders=[(da,db)] if role=='same' or da==db else [(da,db),(db,da)]
  for oa,ob in orders:
   mark=3 if role=='same' else 5
   ds=(du,dv,oa,ob) if role=='same' else (du,oa,dv,ob)
   fam=dict(qid=qid,role=role,degrees=ds,marked_pair=mark);fid=len(families);families.append(fam)
   caps={p:5 if p==mark else 4 for p in PAIRS};cross_budget=sum(caps[p] for p in CROSS)
   # General inclusive budget: exact cross mass +2*triple mass+4*full mass.
   for full in range(5):
    max_tri=(cross_budget-14-4*full)//2
    if max_tri<0:continue
    for tv in product(range(max_tri+1),repeat=4):
     if sum(tv)>max_tri:continue
     remainder={p:caps[p]-full-sum(v for m,v in zip(TRIPLES,tv) if m&p==p) for p in PAIRS}
     if min(remainder.values())<0:continue
     cross_ranges=[(remainder[p],) if p==mark else range(remainder[p]+1) for p in CROSS]
     for aa in product(*cross_ranges):
      if sum(aa)<14:continue
      side_ranges=[(remainder[p],) if p==mark else range(1,remainder[p]+1) for p in (3,12)]
      for side in product(*side_ranges):
       ns=[0]*16;ns[15]=full
       for m,v in zip(TRIPLES,tv):ns[m]=v
       for m,v in zip(CROSS,aa):ns[m]=v
       ns[3],ns[12]=side
       hi=degrees(ns)
       for i,d in enumerate(ds):ns[1<<i]=d-hi[i]
       ns[0]=35-sum(ns)
       if min(ns)<0:continue
       inc={p:sum(n for m,n in enumerate(ns) if m&p==p) for p in PAIRS}
       assert inc[mark]==5 and all(1<=v<=4 for p,v in inc.items() if p!=mark)
       assert degrees(ns)==ds and ns[3]>=1 and ns[12]>=1 and sum(ns)==35
       key=tuple(ns);keys.setdefault(key,[]).append(fid);full_high_shapes[(full,sum(tv))]+=1
profile=dict(families=families,family_count=len(families),labeled_inventory_count=len(keys),high_mass_cases={str(k):v for k,v in full_high_shapes.items()},by_exact_cross=dict(Counter(sum(ns[m] for m in CROSS) for ns in keys)),generation_cpu=time.process_time()-st)
(P/'DOMAIN.json').write_text(json.dumps(dict(profile=profile,keys=[dict(counts=k,families=v) for k,v in sorted(keys.items())]),indent=2)+'\n');print('DOMAIN',profile,flush=True)
out=[];first_failure=None
for i,(ns,fids) in enumerate(sorted(keys.items())):
 e=SubsetEngine(21,4,{m:n for m,n in enumerate(ns) if n});e.inv={p:(0,0,[]) for p in e.inv}
 vals=[(fixed(e,pos),pos) for pos in MENU];U,pos=min(vals)
 z=dict(counts=ns,families=fids,degrees=degrees(ns),positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]);out.append(z)
 if i==0:
  (P/'SINGLE_CASE_PILOT.json').write_text(json.dumps(dict(case=z,cpu_seconds=time.process_time()-st),indent=2)+'\n');print('PILOT',z,flush=True)
 if U>=1:
  first_failure=z;print('FIRST_NONSTRICT',z,flush=True);break
 if time.process_time()-st>8:print('CPU_PREFIX_STOP',flush=True);break
res=dict(status='COMPLETE' if len(out)==len(keys) else 'STOPPED_ON_NONSTRICT' if first_failure else 'CPU_BOUNDED_PREFIX',scope=__doc__,profile=profile,menu=MENU,complete=len(out)==len(keys),checked=len(out),strict_count=sum(z['strict'] for z in out),first_nonstrict=first_failure,cases=out,cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print('FINAL',{k:v for k,v in res.items() if k not in ('cases','profile')},flush=True)
