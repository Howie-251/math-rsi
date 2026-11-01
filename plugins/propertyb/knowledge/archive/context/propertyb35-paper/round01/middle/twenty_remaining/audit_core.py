"""Independent exact expanded-stub replay of all small M35 v20 input certificates.
No SciPy, DP, or position search; nested/avoided losses reconstructed exactly.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math')]
from independent_structure_bounds import independent_rows
from verify_joint_layout import weight

def deduction(ns,pos,i,c):
 s=len(pos);bit=1<<i;ts=sorted(t for t,n in ns.items() if n and t&bit);inv=[]
 for j,t in enumerate(ts):
  for u in ts[j:]:
   cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
   if cap:inv.append([weight(20,pos,t,u,i)+weight(20,pos,u,t,i),cap,t==u==bit,t,u])
 if 'q_total' in c:
  degree=sum(ns[t] for t in ts);qt=max(0,(4*degree-19+2)//3);qp=max(0,(4*ns.get(bit,0)-(20-s)+2)//3)
  assert qt==c['q_total'] and qp==c['q_pure'];remaining=qp;loss=Q()
  for z in sorted(inv):
   if z[2]:
    n=min(remaining,z[1]);remaining-=n;z[1]-=n;loss+=n*z[0]
  assert remaining==0;remaining=max(0,qt-qp)
  for z in sorted(inv):
   n=min(remaining,z[1]);remaining-=n;loss+=n*z[0]
  assert remaining==0
 else:
  alphas=[]
  for z in c['dual']:
   R=z['avoid'];a=Q(z['alpha']);assert a>=0 and not R&bit
   f=sum(n for t,n in ns.items() if t&bit and not t&R);q=max(0,(4*f-(19-R.bit_count())+2)//3)
   assert f==z['edge_count'] and q==z['q'];alphas.append((R,q,a))
  main=sum((q*a for R,q,a in alphas),Q())
  pen=sum((cap*max(Q(),sum((a for R,q,a in alphas if not (t|u)&R),Q())-w) for w,cap,pure,t,u in inv),Q())
  loss=max(Q(),main-pen)
  if 'main' in c:assert main==Q(c['main']) and pen==Q(c['penalty'])
 assert loss==Q(c['loss']);return loss

def verify(r):
 ns={int(t):n for t,n in r['counts'].items() if n};pos=tuple(r['positions']);s=len(pos)
 assert sum(ns.values())==35 and all(n>0 and t.bit_count()<=5 for t,n in ns.items())
 stubs=[frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
 rr=independent_rows(20,pos,stubs);losses={pos[i]:deduction(ns,pos,i,c) for i,c in enumerate(r['quotas'])}
 value=sum((min(z['A'],z['B'],z['C']-losses.get(z['k'],Q())) for z in rr),Q())
 assert value==Q(r['bound']);return value

def main():
 start=time.time();out=[]
 for filename in ['PAIRS.json','UNIT_PAIRS.json','STAR_THREE_REFINED.json','EXCEPTION_TRIPLES.json','FOUR_SEVENS.json']:
  records=json.loads((HERE/filename).read_text())['cases']
  if filename=='PAIRS.json':records=[r for r in records if r['degrees']==[6,6] or (r['degrees']==[6,7] and r['codegree']==1)]
  vals=[verify(r) for r in records]
  out.append(dict(file=filename,cases=len(vals),strict=sum(v<1 for v in vals),max_strict=str(max((v for v in vals if v<1),default=Q()))));print(out[-1],flush=True)
 result=dict(status='PASS',scope=__doc__,results=out,elapsed_seconds=time.time()-start)
 (HERE/'CORE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print('seconds',time.time()-start)
if __name__=='__main__':main()
