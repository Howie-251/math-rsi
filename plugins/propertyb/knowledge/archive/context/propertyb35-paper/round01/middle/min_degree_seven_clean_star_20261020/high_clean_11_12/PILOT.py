"""Exactly one feasible clean B-star of each degree11/12, four old slots only."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
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
out=[]
for r in (11,12):
 ss=[tuple(x+1 for x in inc) for inc in comp(r-5,5)]
 ss=[s for s in ss if all(a<=b for a,b in zip(s,base['attachments']))];s=ss[0]
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
 out.append(dict(r=r,s=s,complete_domain_size=len(ss),counts=dict(ns),degrees=[r]+base['degrees'],positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals],expanded35_masks=masks,independent_rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in z.items()} for z in ir]))
res=dict(status='BOTH_FIRST_PILOTS_STRICT' if all(z['strict'] for z in out) else 'FIRST_PILOT_FAILURE_PRESENT_STOP_FULL_DOMAIN',scope=__doc__,actual_clean_caller_not_proved_here=True,cases=out,cpu_seconds=time.process_time()-st)
(P/'PILOT_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print('STATUS',res['status'],'CPU',res['cpu_seconds'])
for z in out:print(z['r'],z['s'],z['bound'],z['positions'],z['complete_domain_size'],z['strict'])
