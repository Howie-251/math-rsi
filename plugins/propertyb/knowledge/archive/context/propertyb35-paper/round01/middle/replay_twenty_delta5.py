"""Independent expanded-stub replay of all 438 M35 v20 delta5 triples.
No layout search, SciPy, or floating arithmetic. Validates all saved exact duals.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from itertools import combinations
import sys,json,time
ROOT=Path(__file__).resolve().parents[4]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
HERE=Path(__file__).parent

def weight(v,pos,t,u,k):
 N=v-len(pos);pivot=sum(1<<i for i,p in enumerate(pos) if p==k)
 left=sum(1<<i for i,p in enumerate(pos) if p<k);right=sum(1<<i for i,p in enumerate(pos) if p>k)
 if t&u!=pivot or (t^pivot)&~left or (u^pivot)&~right:return Q()
 a=k-1-left.bit_count();b=v-k-right.bit_count()
 return injection_probability(N,a,b,5-t.bit_count(),5-u.bit_count(),False)

def slots(ns,pos,i):
 bit=1<<i;ts=sorted(t for t,n in ns.items() if n and t&bit);ans=[]
 for j,t in enumerate(ts):
  for u in ts[j:]:
   cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
   if cap:ans.append(dict(t=t,u=u,capacity=cap,weight=weight(20,pos,t,u,pos[i])+weight(20,pos,u,t,pos[i])))
 return ans

def loss(ns,pos,i,c):
 inv=slots(ns,pos,i);bit=1<<i
 d=sum(n for t,n in ns.items() if t&bit)
 if 'q_total' in c:
  qt=max(0,(4*d-19+2)//3);qp=max(0,(4*ns.get(bit,0)-17+2)//3)
  assert (qt,qp)==(c['q_total'],c['q_pure'])
  entries=[[x['weight'],x['capacity'],x['t']==x['u']==bit,x['t'],x['u']] for x in inv]
  answer=Q();remaining=qp
  for x in sorted(entries):
   if x[2]:
    take=min(remaining,x[1]);x[1]-=take;remaining-=take;answer+=take*x[0]
  assert remaining==0
  remaining=max(0,qt-qp)
  for x in sorted(entries):
   take=min(remaining,x[1]);remaining-=take;answer+=take*x[0]
  assert remaining==0
 else:
  alphas=[]
  for z in c['dual']:
   R=z['avoid'];alpha=Q(z['alpha']);assert alpha>=0 and not R&bit
   f=sum(n for t,n in ns.items() if t&bit and not t&R)
   q=max(0,(4*f-(19-R.bit_count())+2)//3)
   assert f==z['edge_count'] and q==z['q'];alphas.append((R,q,alpha))
  main=sum((a*q for R,q,a in alphas),Q())
  penalty=sum((z['capacity']*max(Q(),sum((a for R,q,a in alphas if not (z['t']|z['u'])&R),Q())-z['weight']) for z in inv),Q())
  answer=max(Q(),main-penalty)
  assert main==Q(c['main']) and penalty==Q(c['penalty'])
 assert answer==Q(c['loss'])
 return answer

def main():
 start=time.time();cases=json.loads((HERE/'TWENTY_DELTA5_AVOIDED.json').read_text())['cases']
 actual=set();strict=0;maxstrict=Q();residual=[];allrows=0
 for idx,r in enumerate(cases):
  ns={int(t):n for t,n in r['counts'].items() if n};pos=tuple(r['positions'])
  assert sum(ns.values())==35 and min(ns.values())>0
  ds=tuple(sum(n for t,n in ns.items() if t&(1<<i)) for i in range(3))
  ps=tuple(sum(n for t,n in ns.items() if t&m==m) for m in (3,5,6));t=ns.get(7,0)
  assert ds==tuple(r['degrees']) and ps==tuple(r['codegrees']) and t==r['triple']
  actual.add((ds[1],ds[2],*ps,t))
  stubs=[frozenset(i+1 for i in range(3) if t&(1<<i)) for t,n in ns.items() for _ in range(n)]
  rr=independent_rows(20,pos,stubs)
  losses={pos[i]:loss(ns,pos,i,c) for i,c in enumerate(r['quotas'])}
  total=Q()
  for own,saved in zip(rr,r['rows']):
   assert all(own[k]==Q(saved[k]) for k in ('A','B','C'))
   assert 0<=losses.get(own['k'],Q())<=own['C']
   val=min(own['A'],own['B'],own['C']-losses.get(own['k'],Q()))
   assert val==Q(saved['bound']);total+=val;allrows+=1
  assert total==Q(r['bound']) and (total<1)==r['strict']
  if total<1:strict+=1;maxstrict=max(maxstrict,total)
  else:residual.append(dict(index=idx,degrees=ds,codegrees=ps,triple=t,bound=str(total)))
 expected=set()
 for a in range(5,9):
  for b in range(a,10):
   if a+18*b>170:continue
   for xy,xz in ((1,1),(1,2),(2,1)):
    for yz in range(1,a+1):
     for t in range(min(xy,xz,yz)+1):
      ns=[35-5-a-b+xy+xz+yz-t,5-xy-xz+t,a-xy-yz+t,b-xz-yz+t,xy-t,xz-t,yz-t,t]
      if min(ns)>=0:expected.add((a,b,xy,xz,yz,t))
 assert expected==actual and len(actual)==len(cases)==438
 wanted={(8,8,1,1,1,0),(8,8,1,1,2,0),(8,9,1,1,1,0),(8,9,1,1,2,0),(8,9,2,1,2,0),(8,9,2,1,2,1)}
 assert {(z['degrees'][1],z['degrees'][2],*z['codegrees'],z['triple']) for z in residual}==wanted
 result=dict(status='PASS',scope=__doc__,cases=438,strict=strict,max_strict=str(maxstrict),residual=residual,rows=allrows,expected_domain_exact=True,all_dual_arithmetic_exact=True,elapsed_seconds=time.time()-start)
 (HERE/'TWENTY_DELTA5_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
