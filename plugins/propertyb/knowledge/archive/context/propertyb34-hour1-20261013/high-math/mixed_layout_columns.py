"""Bounded LP column proposal using weighted actual-slot position DP, exact final mixture."""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
import numpy as np
from scipy.optimize import linprog
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from mixed_layout_lp import inventory,vector
from fast_position_dp import Engine
from multilock import json_value


def oracle(eng,ns,slots,alphas):
 s=eng.s;v=eng.v;best=None;offs=[];n=0
 for ss in slots:offs.append(n);n+=len(ss)
 for perm in permutations(range(s)):
  move=lambda t:sum(1<<perm[i] for i in range(s) if t&(1<<i));mp={t:move(t) for t in ns};counts={mp[t]:c for t,c in ns.items()};inv=[perm.index(j) for j in range(s)];dp={(0,0):(0.,())}
  for k in range(1,v+1):
   for j in range(s+1):
    if (k-1,j) not in dp:continue
    previous,oldpos=dp[k-1,j]
    for pivot in (False,True):
     key=k,j,pivot
     if key not in eng.states:continue
     aa,bb,cc=eng.states[key];A=sum(c*aa[t] for t,c in counts.items());B=sum(c*bb[t] for t,c in counts.items());base=min(A,B);C=sum(counts.get(t,0)*(counts.get(u,0)-int(t==u))*w for (t,u),w in cc.items()) if base else 0
     if not pivot:value=float(min(base,C))
     else:
      i=inv[j];value=0.
      for z,(t,u) in enumerate(slots[i]):
       alpha=alphas[offs[i]+z]
       if alpha<1e-12:continue
       mt,mu=mp[t],mp[u];loss=cc.get((mt,mu),0)+cc.get((mu,mt),0);value+=alpha*min(base,C-loss)
     nxt=k,j+int(pivot);val=previous+value
     if nxt not in dp or val<dp[nxt][0]:dp[nxt]=(val,oldpos+(k,)*int(pivot))
  val,pos=dp[v,s]
  if best is None or val<best['value']:best=dict(value=val,positions=pos,perm=perm)
 return best

def solve(eng,x,max_rounds=10):
 ns={int(t):n for t,n in x['counts'].items()};slots=inventory(ns,eng.s,eng.v);cols=[];seen=set();idx=[i for i,ss in enumerate(slots) for _ in ss];m=len(idx)
 layouts=[tuple(range(a,a+6)) for a in (10,9)]+[(10,11,12,13,14,24),(10,11,12,13,23,24),(8,9,10,11,12,14)]
 def add(pos,perm):
  f,g=vector(eng,ns,slots,pos,perm);key=f,tuple(g)
  if key in seen:return False
  seen.add(key);cols.append(dict(free=f,values=g,positions=tuple(pos[perm[i]] for i in range(eng.s))));return True
 for pos in layouts:
  for perm in permutations(range(eng.s)):add(pos,perm)
 hist=[]
 for rr in range(max_rounds+1):
  n=len(cols);mat=np.zeros((m,n+eng.s));mat[:,:n]=np.asarray([z['values'] for z in cols],dtype=float).T/eng.D
  for row,i in enumerate(idx):mat[row,n+i]=-1
  c=np.asarray([z['free']/eng.D for z in cols]+[1]*eng.s);eq=np.asarray([[1]*n+[0]*eng.s],dtype=float);r=linprog(c,A_ub=mat,b_ub=np.zeros(m),A_eq=eq,b_eq=[1],bounds=(0,None),method='highs');assert r.success
  ps=[Fraction(round(float(p)*100000),100000) if p>1e-9 else Fraction() for p in r.x[:n]];tot=sum(ps,Fraction());ps=[p/tot for p in ps]
  free=sum((p*Fraction(z['free'],eng.D) for p,z in zip(ps,cols)),Fraction());av=[sum((p*Fraction(z['values'][j],eng.D) for p,z in zip(ps,cols)),Fraction()) for j in range(m)];centers=[];off=0
  for i,ss in enumerate(slots):vv=av[off:off+len(ss)];off+=len(ss);centers.append(dict(center=i,slots=ss,averages=vv,maximum=max(vv)))
  bound=free+sum(z['maximum'] for z in centers);hist.append(dict(round=rr,columns=n,LP=float(r.fun),exact_bound=bound));print('group',x['group'],'round',rr,'cols',n,'bound',bound,float(bound),flush=True)
  out=dict(group=x['group'],counts=ns,bound=bound,free_average=free,centers=centers,witnesses=[dict(probability=p,positions=z['positions']) for p,z in zip(ps,cols) if p],history=hist)
  if bound<1 or rr==max_rounds:break
  pick=oracle(eng,ns,slots,-r.ineqlin.marginals)
  if not add(pick['positions'],pick['perm']):hist[-1]['no_new_column']=True;break
 return out
if __name__=='__main__':
 start=time.perf_counter();eng=Engine(24,6);source=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low6_badnone.json').read_text());out=[]
 for x in source['results']:
  if x['group'] not in (1,3,5,8):continue
  out.append(solve(eng,x,12));Path(__file__).with_name('MIXED_LAYOUT_COLUMNS.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>180:print('BUDGET_STOP',flush=True);break
