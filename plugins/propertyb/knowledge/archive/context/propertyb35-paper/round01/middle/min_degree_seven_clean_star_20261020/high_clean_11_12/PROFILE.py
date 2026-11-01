"""Complete194/287 clean-star domains, same four fixed slots and zero quotas."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
from itertools import combinations
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));sys.path.insert(0,str(ROOT/'computations'))
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
base=json.loads((P.parent/'FIVE_RESULT.json').read_text())['nonstrict'][1]
def comp(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for rest in comp(n-a,k-1):yield(a,)+rest
domain={}
for r in (11,12):
 first={tuple(x+1 for x in inc) for inc in comp(r-5,5) if all(x+1<=a for x,a in zip(inc,base['attachments']))}
 second=set()
 for cut in combinations(range(1,r),4):
  edges=(0,)+cut+(r,);s=tuple(edges[i+1]-edges[i] for i in range(5))
  if all(x<=a for x,a in zip(s,base['attachments'])):second.add(s)
 assert first==second and len(first)==(194 if r==11 else 287);domain[r]=sorted(first)
out=[];stop=False
for r,star in domain.items():
 for s in star:
  ns=Counter({int(m)<<1:n for m,n in base['counts'].items()})
  for v,n in enumerate(s):ns[1<<(v+1)]-=n;ns[(1<<(v+1))|1]+=n
  assert sum(ns.values())==35 and min(ns.values())>=0
  e=SubsetEngine(21,6,ns);e.inv={p:(0,0,[]) for p in e.inv};vals=[]
  for slot in (9,10,20,21):
   pos=(slot,)+tuple(base['positions']);lock={k:1<<v for v,k in enumerate(pos)};left=0;val=0
   for at in range(1,22):p=lock.get(at,0);val+=e.value(at,left,p);left|=p
   vals.append((Fraction(val,e.D),pos))
  U,pos=min(vals);masks=[m for m,n in ns.items() for _ in range(n)];ts=[frozenset(i+1 for i in range(6) if m>>i&1) for m in masks]
  ir=independent_rows(21,pos,ts);own=sum((min(z['A'],z['B'],z['C']) for z in ir),Fraction());assert own==U
  row=dict(r=r,s=s,counts=dict(ns),degrees=[r]+base['degrees'],positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals],expanded35_masks=masks,independent_rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in z.items()} for z in ir]);out.append(row)
  if U>=1:print('FIRST_NONSTRICT',r,s,str(U),flush=True);stop=True;break
  if time.process_time()-st>8:print('8CPU_STOP',flush=True);stop=True;break
 if stop:break
complete=len(out)==481
res=dict(status='COMPLETE481_STRICT' if complete and all(z['strict'] for z in out) else 'STOPPED_ON_NONSTRICT' if out and not out[-1]['strict'] else 'BOUNDED_PREFIX',scope=__doc__,actual_clean_caller_not_proved_here=True,independent_cut_domain_equal=True,domain_sizes={str(r):len(s) for r,s in domain.items()},checked=len(out),strict_count=sum(z['strict'] for z in out),maximum=str(max(Fraction(z['bound']) for z in out)),replayed_rows=21*len(out),cases=out,nonstrict=[z for z in out if not z['strict']],cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ('cases','nonstrict')})
