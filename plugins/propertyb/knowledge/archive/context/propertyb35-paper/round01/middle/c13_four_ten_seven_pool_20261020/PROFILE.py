"""First complete worst source, expand other five only if it is all strict."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
tails=[z for z in json.loads((P.parent/'generic_c3_thirteen_pilot_20261020/RESULT.json').read_text())['cases'] if not z['strict']]
PP=(3,5,6,9,10,12);MENU=[(slot,8,9,20,21) for slot in (1,10,11,12)]
def domain(mu):
 out=[]
 for cp in product(*(range(mu[p]+1) for p in PP)):
  tot=sum(cp)
  if tot>7:continue
  rows=[sum(n for p,n in zip(PP,cp) if p>>v&1) for v in range(4)]
  if any(not 1<=n<=4 for n in rows):continue
  c0=7-tot
  if not 0<=c0<=mu[0]:continue
  ns={m<<1:n for m,n in enumerate(mu) if n};ns[0]-=c0;ns[1]=c0
  for p,n in zip(PP,cp):ns[p<<1]-=n;ns[(p<<1)|1]=n
  assert min(ns.values())>=0 and sum(ns.values())==35
  out.append(dict(c_pair=cp,c0=c0,inclusive_z_to_K=rows,counts=ns))
 return out
def fixed(e,pos):
 lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
 for at in range(1,22):p=lock.get(at,0);U+=e.value(at,left,p);left|=p
 return Fraction(U,e.D)
cases=[];sources=[];stop=False
for sid,tail in enumerate(tails):
 dd=domain(tail['counts']);own=[]
 for z in dd:
  e=SubsetEngine(21,5,z['counts']);e.inv={p:(0,0,[]) for p in e.inv}
  vals=[(fixed(e,pos),pos) for pos in MENU];U,pos=min(vals)
  row=dict(source=sid,**z,positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]);cases.append(row);own.append(row)
  if U>=1:print('FIRST_NONSTRICT',row,flush=True);stop=True;break
  if time.process_time()-st>8:print('8CPU_STOP',flush=True);stop=True;break
 sources.append(dict(source=sid,source_counts=tail['counts'],complete=len(own)==len(dd),domain_size=len(dd),checked=len(own),strict=sum(z['strict'] for z in own),maximum=str(max(Fraction(z['bound']) for z in own))))
 print('SOURCE',sources[-1],'CPU',time.process_time()-st,flush=True)
 if stop:break
out=dict(status='COMPLETE_SIX_S2_SOURCES' if len(sources)==6 and all(s['complete'] for s in sources) and all(z['strict'] for z in cases) else 'STOPPED_ON_NONSTRICT' if any(not z['strict'] for z in cases) else 'BOUNDED_PREFIX',scope=__doc__,menu=MENU,sources=sources,case_count=len(cases),cases=cases,nonstrict=[z for z in cases if not z['strict']],cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print('FINAL',{k:v for k,v in out.items() if k not in ('cases','sources','nonstrict')})
