from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()

def f(d,t):
 q,r=divmod(2*t,d);return (d-r)*q*q+r*(q+1)**2

def bound(ds,ns,tau,oldP):
 n1,n2,n4=ns[1],ns[2],ns[4];basecost=0;required=0;forcedextra=0;freebase=[];freeextra=[];bounds=[]
 for d in ds:
  b=comb(d,2)-2*d+10;rowtau=max(0,4*d-40)
  lo=max(0,b-(tau+n2)//2)
  hi=min(comb(d,2)-max(0,(4*d-20+rowtau+2)//3),b+(n4-rowtau)//2)
  bounds.append([lo,hi])
  if lo>hi:return -1,{'impossible':'pointinterval','bounds':bounds}
  basecost+=f(d,lo);required+=lo;forcedextra+=max(0,lo-b)
  for t in range(lo+1,hi+1):
   (freeextra if t>b else freebase).append(f(d,t)-f(d,t-1))
 budget=2*n4-forcedextra;need=n1-required
 if budget<0 or need<0:return -1,{'impossible':'budgetorlower','bounds':bounds}
 free=sorted(freebase+sorted(freeextra)[:budget])
 if need>len(free):return -1,{'impossible':'totalcapacity','bounds':bounds}
 B=basecost+sum(free[:need]);q,r=divmod(2*n1,30);p=min(oldP,(900*q+r*r-B)//2)
 return p,{'B':B,'bounds':bounds,'forced_extra':forcedextra,'free_extra_budget':budget}

def value(ns,caps,p):
 if p<0:return -1
 out=6864*ns[1]
 for cap,w in zip(reversed(caps),reversed((36,120,330,792,1716))):x=min(cap,p);p-=x;out+=x*w
 return out

j4=json.loads((P/'RESULT.json').read_text())['jobs'];j5=json.loads((P/'LAMBDA5_RESULT.json').read_text())['jobs'];outputs=[]
for role,jobs in [('lambda4',j4),('lambda5',j5)]:
 for j in jobs:
  ds=j['degrees'];res=[]
  for k in j.get('keys',j.get('cases',[])):
   # Retain all archived keys, including those already excluded by previous smaller P.
   p,cert=bound(ds,k['n'],k['tau'],k.get('newP',k.get('vertex_P',k.get('P'))));caps=k.get('caps',k.get('new_caps'))
   v=value(k['n'],caps,p)
   res.append({'n':k['n'],'tau':k['tau'],'P':p,'caps':caps,'twice_L':v,'strict':v<5445440,'certificate':cert})
  outputs.append({'role':role,'spectrum_id':j['spectrum_id'],'degrees':ds,'strict':all(k['strict'] for k in res),'keys':res})
out={'status':'COMPLETE_ARCHIVED_RESIDUAL_FILTER','jobs':outputs,'cpu_seconds':time.process_time()-st}
(P/'COUPLED_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
for role in ['lambda4','lambda5']:
 print(role,'strictids',[j['spectrum_id'] for j in outputs if j['role']==role and j['strict']])
 for j in outputs:
  if j['role']==role and not j['strict']: print(j['spectrum_id'],'remaining',sum(not k['strict'] for k in j['keys']),'max',max(k['twice_L'] for k in j['keys']))
print('CPU',out['cpu_seconds'])
