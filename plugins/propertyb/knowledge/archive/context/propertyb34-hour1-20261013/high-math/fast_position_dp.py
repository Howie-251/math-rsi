"""Integer-scaled exact position DP. Final winners must be replayed with Fraction rows."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import factorial,comb
import sys,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import edge_weight,pair_weight,link_q_lower,position_context

class Engine:
 def __init__(self,v,s):
  self.v=v;self.s=s;self.D=factorial(v-s);self.states={};self.valid=[t for t in range(1<<s) if t.bit_count()<=5]
  for k in range(1,v+1):
   for j in range(s+1):
    if j>k-1:continue
    for pivot in (False,True):
     j2=j+int(pivot)
     if j2>s or s-j2>v-k:continue
     pos=tuple(range(1,j+1))+(k,)*int(pivot)+tuple(range(k+1,k+1+s-j2))
     aa={t:int(self.D*edge_weight(v,5,pos,t,k,True)) for t in self.valid};bb={t:int(self.D*edge_weight(v,5,pos,t,k,False)) for t in self.valid}
     cc={(t,u):int(self.D*pair_weight(v,5,pos,t,u,k)) for t in self.valid for u in self.valid};cc={p:w for p,w in cc.items() if w}
     self.states[k,j,pivot]=(aa,bb,cc)
  edge_weight.cache_clear();pair_weight.cache_clear();position_context.cache_clear()
 def solve(self,ns,actual=None):
  s=self.s;v=self.v;actual=actual or {};static={}
  for j in range(s):
   bit=1<<j;ts=sorted(t for t in ns if t&bit);degree=sum(ns[t] for t in ts);q=link_q_lower(v,5,degree);r=max(0,(4*ns.get(bit,0)-(v-s)+2)//3)
   slots=[]
   for i,t in enumerate(ts):
    for u in ts[i:]:
     cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
     if t==u==bit:cap-=r
     if cap:slots.append((t,u,cap))
   static[j]=(bit,q,r,slots)
  dp={(0,0):(0,())}
  for k in range(1,v+1):
   for j in range(s+1):
    if (k-1,j) not in dp:continue
    previous,oldpos=dp[k-1,j]
    for pivot in (False,True):
     key=k,j,pivot
     if key not in self.states:continue
     aa,bb,cc=self.states[key];A=sum(n*aa[t] for t,n in ns.items());B=sum(n*bb[t] for t,n in ns.items())
     value=min(A,B)
     if value:
      C=sum(ns.get(t,0)*(ns.get(u,0)-int(t==u))*w for (t,u),w in cc.items())
      if pivot:
       if j in actual:
        t,u=actual[j];loss=cc.get((t,u),0)+cc.get((u,t),0)
       else:
        bit,q,r,inv=static[j];loss=2*r*cc.get((bit,bit),0);rem=max(0,q-r)
        for w,cap in sorted((cc.get((t,u),0)+cc.get((u,t),0),cap) for t,u,cap in inv):
         take=min(rem,cap);rem-=take;loss+=take*w
        assert rem==0
       C-=loss
      value=min(value,C)
     nxt=k,j+int(pivot);val=previous+value
     if nxt not in dp or val<dp[nxt][0]:dp[nxt]=(val,oldpos+(k,)*int(pivot))
  total,pos=dp[v,s];return dict(bound=Fraction(total,self.D),positions=pos)
