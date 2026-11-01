"""Complete bounded clean-star domain, fixed five-point layout plus six old slots."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,time,sys
P=Path(__file__).resolve().parent;st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(P))
from FIVE import SubsetEngine
def comps(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for tail in comps(n-a,k-1):yield(a,)+tail
def fixed(e,pos):
 lock={k:1<<v for v,k in enumerate(pos)};left=0;value=0
 for k in range(1,22):p=lock.get(k,0);value+=e.value(k,left,p);left|=p
 return Fraction(value,e.D)
source=json.loads((P/'FIVE_RESULT.json').read_text());domain=[];stats=[]
for sid,row in enumerate(source['nonstrict']):
 assert row['BF'] is not None and row['clean_degree_max']>=7
 counts=Counter()
 for r in range(7,row['clean_degree_max']+1):
  for inc in comps(r-5,5):
   s=tuple(a+1 for a in inc)
   if any(a>b for a,b in zip(s,row['attachments'])):continue
   ns=Counter({int(m)<<1:n for m,n in row['counts'].items()})
   for v,n in enumerate(s):ns[1<<(v+1)]-=n;ns[(1<<(v+1))|1]+=n
   assert min(ns.values())>=0 and sum(ns.values())==35
   dd=[sum(n for m,n in ns.items() if m>>v&1) for v in range(6)]
   assert dd==[r]+row['degrees']
   positions=[(k,)+tuple(row['positions']) for k in (1,9,10,11,20,21) if k not in row['positions']]
   domain.append(dict(source=sid,r=r,s=s,counts=dict(ns),degrees=dd,five_positions=row['positions'],fixed_positions=positions));counts[r]+=1
 stats.append(dict(source=sid,traces=row['traces'],D_F=row['F_degree_sum'],BF=row['BF'],rmax=row['clean_degree_max'],counts_by_r=dict(counts),total=sum(counts.values())))
(P/'STAR_DOMAIN.json').write_text(json.dumps(dict(scope=__doc__,sources=stats,inputs=domain),indent=2)+'\n')
out=[];first_failure=None
for i,z in enumerate(domain):
 e=SubsetEngine(21,6,z['counts']);e.inv={p:(0,0,[]) for p in e.inv}
 vals=[(fixed(e,pos),pos) for pos in z['fixed_positions']];U,pos=min(vals)
 rr=dict(**z,positions=pos,bound=str(U),strict=U<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]);out.append(rr)
 if i==0:
  pilot=dict(status='SINGLE_CASE_PILOT',case=rr,complete_domain=len(domain),cpu_seconds=time.process_time()-st)
  (P/'STAR_PILOT.json').write_text(json.dumps(pilot,indent=2)+'\n');print('PILOT',rr['source'],rr['r'],rr['s'],rr['bound'],'CPU',pilot['cpu_seconds'],flush=True)
 if U>=1 and first_failure is None:first_failure=rr;print('FIRST_FAILURE',rr['source'],rr['r'],rr['s'],rr['bound'],flush=True)
 assert time.process_time()-st<9,'9CPU primary cutoff leaves independent replay budget'
res=dict(status='COMPLETE_FIXED_CLEAN_STAR_DOMAIN',scope=__doc__,sources=stats,domain_size=len(domain),strict_count=sum(z['strict'] for z in out),nonstrict=[z for z in out if not z['strict']],cases=out,cpu_seconds=time.process_time()-st)
(P/'STAR_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print('FINAL',{k:v for k,v in res.items() if k not in ('cases','nonstrict')});print('NONSTRICT_TOTAL',len(res['nonstrict']))
