"""Second S4 orbit representative only, complete degree7/9 views, same pure quota/layouts."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
original=json.loads((P.parents[1]/'generic_c3_thirteen_pilot_20261020/RESULT.json').read_text())
mu=[z['counts'] for z in original['cases'] if not z['strict']][2]
T=tuple(m for m,n in enumerate(mu) if n);assert T==(0,2,3,4,5,6,9,10,12)
pairsource=json.loads((P.parents[1]/'two_six_transfer_20261020/PAIR_RESULT.json').read_text())
gates=[z for z in pairsource['cases'] if z['degrees'] in ([7,10],[9,10])]
assert {(tuple(z['degrees']),z['codegree']) for z in gates}=={((r,10),c) for r in (7,9) for c in range(5,r+1)}
assert all(z['strict'] for z in gates)
MENU=[(s,8,9,20,21) for s in (1,10,11,12)];domain=[]
for nonempty in product(*(range(mu[m]+1) for m in T[1:])):
 row=tuple(sum(c for m,c in zip(T[1:],nonempty) if m>>i&1) for i in range(4))
 if any(not 1<=c<=4 for c in row):continue
 n=sum(nonempty)
 for r in (7,9):
  c0=r-n
  if not 0<=c0<=mu[0]:continue
  c=(c0,)+nonempty
  ns={}
  for m,count in zip(T,c):ns[2*m]=mu[m]-count;ns[2*m+1]=count
  assert min(ns.values())>=0 and sum(ns.values())==35
  assert [sum(n for m,n in ns.items() if m>>i&1) for i in range(5)]==[r,10,10,10,10]
  domain.append(dict(r=r,c=c,row=row,pure_quota=max(0,(4*c0-16+2)//3),counts=ns))
views=[]
for i,z in enumerate(domain):
 e=SubsetEngine(21,5,z['counts']);e.inv={p:(0,0,[]) for p in e.inv};e.inv[1]=(0,z['pure_quota'],[])
 vals=[]
 for pos in MENU:
  lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
  for at in range(1,22):p=lock.get(at,0);U+=e.value(at,left,p);left|=p
  vals.append((Fraction(U,e.D),pos))
 U,pos=min(vals);views.append(dict(index=i,**z,positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]))
 if i==0:print('PILOT',z['r'],z['c'],'bound',str(U),'CPU',time.process_time()-st,flush=True)
 if time.process_time()-st>14:raise RuntimeError('14CPU table cutoff; do not use partial domain as complete')
clean=[z for z in views if z['r']==7 and all(z['c'][j]==0 for j,m in enumerate(T) if m.bit_count()==1)]
assert len(clean)>0
failed=[z for z in views if not z['strict']]
target=[mu[m]*(5-m.bit_count()) for m in T];assert sum(target)==9*7+8*9
out=dict(status='COMPLETE_WORST_SOURCE_ACTUAL_VIEWS',scope=__doc__,T=T,source_counts=mu,target_columns=target,target_degree_counts={'7':9,'9':8},imported_pair_gates=[dict(degrees=z['degrees'],codegree=z['codegree'],bound=z['bound']) for z in gates],Nfree=16,menu=MENU,domain_size=len(views),by_degree=dict(Counter(z['r'] for z in views)),strict_count=sum(z['strict'] for z in views),failed_count=len(failed),failed_by_degree=dict(Counter(z['r'] for z in failed)),complete_clean7_domain=len(clean),clean7_strict=sum(z['strict'] for z in clean),clean7_nonstrict=[z for z in clean if not z['strict']],views=views,failed_views=failed,cpu_seconds=time.process_time()-st)
(P/'TABLES.json').write_text(json.dumps(out,indent=2)+'\n');print('FINAL',{k:v for k,v in out.items() if k not in ('views','failed_views','clean7_nonstrict','imported_pair_gates','source_counts')})
