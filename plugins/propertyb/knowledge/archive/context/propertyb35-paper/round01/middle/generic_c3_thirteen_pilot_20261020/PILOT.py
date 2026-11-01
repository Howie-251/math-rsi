"""Only the selected degree10^4 c13 necessary domain, fixed3 old layouts."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));sys.path.insert(0,str(ROOT/'computations'))
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
CROSS=(5,6,9,10);TM=(7,11,13,14);PP=(3,5,6,9,10,12)
MENU=((8,9,20,21),(9,10,20,21),(9,20,10,21))
def fixed(e,pos):
 lock={k:1<<v for v,k in enumerate(pos)};left=0;val=0
 for k in range(1,22):p=lock.get(k,0);val+=e.value(k,left,p);left|=p
 return Fraction(val,e.D)
domain=set()
# Sum cross-inclusive <=16 = exactcross +2*triplemass +4*fullmass.
# exactcross>=13 therefore fullmass=0, triplemass<=1.
for tri in (0,*TM):
 cap={p:4-int(bool(tri) and tri&p==p) for p in PP}
 for cross in product(*(range(cap[p]+1) for p in CROSS)):
  if sum(cross)<13:continue
  for A,B in product(range(1,cap[3]+1),range(1,cap[12]+1)):
   ns=[0]*16;ns[3]=A;ns[12]=B
   if tri:ns[tri]=1
   for p,n in zip(CROSS,cross):ns[p]=n
   for i in range(4):ns[1<<i]=10-sum(n for m,n in enumerate(ns) if m>>i&1)
   ns[0]=35-sum(ns)
   if min(ns)<0:continue
   assert sum(ns)==35 and all(sum(n for m,n in enumerate(ns) if m>>i&1)==10 for i in range(4))
   assert all(1<=sum(n for m,n in enumerate(ns) if m&p==p)<=4 for p in PP)
   domain.add(tuple(ns))
out=[]
for ns in sorted(domain):
 e=SubsetEngine(21,4,{m:n for m,n in enumerate(ns) if n});e.inv={p:(0,0,[]) for p in e.inv}
 vals=[(fixed(e,pos),pos) for pos in MENU];U,pos=min(vals)
 out.append(dict(counts=ns,degrees=[10]*4,exact_cross=sum(ns[p] for p in CROSS),triple_mass=sum(ns[t] for t in TM),positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]))
 assert time.process_time()-st<2.5,'primary cutoff reserves worst-input replay'
worst=max(out,key=lambda z:Fraction(z['bound']));ns=worst['counts'];masks=[m for m,n in enumerate(ns) for _ in range(n)]
types=[frozenset(i+1 for i in range(4) if m>>i&1) for m in masks]
ir=independent_rows(21,tuple(worst['positions']),types);own=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction());assert own==Fraction(worst['bound'])
res=dict(status='COMPLETE_SELECTED10POW4_PILOT',scope=__doc__,complete_for_this_quad=True,full_generic_c13_gate_proved=False,domain_size=len(domain),strict_count=sum(z['strict'] for z in out),nonstrict_count=sum(not z['strict'] for z in out),by_cross=dict(Counter(z['exact_cross'] for z in out)),by_triples=dict(Counter(z['triple_mass'] for z in out)),menu=MENU,worst=worst,worst_independent_replay=dict(expanded35_masks=masks,bound=str(own),rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in ir]),cases=out,cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ('cases','worst_independent_replay')})
