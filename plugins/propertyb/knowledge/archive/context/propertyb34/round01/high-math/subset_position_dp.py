"""Exact labelled-subset position DP: all lock orders and positions in one pass.

Coefficients scaled by (v-s)!; final witnesses replayed using independent rows.
Only total and nested pure quotas are used by this proposal engine.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial,comb
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,link_q_lower
from pure_quota import certificate
from independent_structure_bounds import independent_rows

def fall(n,k):
 if k<0 or n<k:return 0
 z=1
 for j in range(k):z*=n-j
 return z

class SubsetEngine:
 def __init__(self,v,s,ns):
  self.v=v;self.s=s;self.ns={int(t):c for t,c in ns.items() if c};self.N=v-s;self.D=factorial(self.N);self.full=(1<<s)-1
  self.fact=[factorial(i) for i in range(self.N+1)]
  self.fl=[[fall(a,r) for r in range(10)] for a in range(self.N+1)]
  # zeta[pivot][left mask][outside size]: edge counts whose nonpivot trace lies in left.
  self.zeta={};self.inv={}
  for p in [0]+[1<<i for i in range(s)]:
   arr=[[0]*6 for _ in range(1<<s)]
   for t,c in self.ns.items():
    if p and not t&p:continue
    arr[t^p if p else t][5-t.bit_count()]+=c
   for i in range(s):
    b=1<<i
    for m in range(1<<s):
     if m&b:
      for r in range(6):arr[m][r]+=arr[m^b][r]
   self.zeta[p]=arr
   if not p:continue
   ts=sorted(t for t in self.ns if t&p);degree=sum(self.ns[t] for t in ts)
   q=link_q_lower(v,5,degree);pure=max(0,(4*self.ns.get(p,0)-self.N+2)//3)
   slots=[]
   for j,t in enumerate(ts):
    for u in ts[j:]:
     cap=comb(self.ns[t],2) if t==u else self.ns[t]*self.ns[u]
     if t==u==p:cap-=pure
     if cap:slots.append((t,u,cap))
   self.inv[p]=(q,pure,slots)

 def pair(self,t,u,left,p,a,b):
  right=self.full^left^p;r=5-t.bit_count();q=5-u.bit_count()
  if p:
   if t&u!=p or (t^p)&~left or (u^p)&~right or r+q>self.N:return 0
   return self.fl[a][r]*self.fl[b][q]*self.fact[self.N-r-q]
  if not r or not q or t&u or t&~left or u&~right or r+q-1>self.N:return 0
  return self.fl[a][r-1]*self.fl[b][q-1]*self.fact[self.N-r-q+1]

 def value(self,k,left,p,actual=None):
  right=self.full^left^p;a=k-1-left.bit_count();b=self.v-k-right.bit_count()
  if a<0 or b<0 or a+b+int(not p)!=self.N:return None
  ls=self.zeta[p][left];rs=self.zeta[p][right];A=B=C=0
  ran=range(6) if p else range(1,6)
  for r in ran:
   aa=self.fl[a][r if p else r-1]*self.fact[self.N-r]*(1 if p else r)
   bb=self.fl[b][r if p else r-1]*self.fact[self.N-r]*(1 if p else r)
   A+=ls[r]*aa;B+=rs[r]*bb
  base=min(A,B)
  if not base:return 0
  for r in ran:
   for q in ran:
    n=r+q-int(not p)
    if n<=self.N:C+=ls[r]*rs[q]*self.fl[a][r-int(not p)]*self.fl[b][q-int(not p)]*self.fact[self.N-n]
  C-=self.ns.get(p,0)*self.pair(p,p,left,p,a,b)
  if p:
   if actual and p in actual:
    t,u=actual[p];loss=self.pair(t,u,left,p,a,b)+self.pair(u,t,left,p,a,b)
   else:
    q,pure,slots=self.inv[p];loss=2*pure*self.pair(p,p,left,p,a,b);rem=max(0,q-pure)
    if rem:
     for w,cap in sorted((self.pair(t,u,left,p,a,b)+self.pair(u,t,left,p,a,b),cap) for t,u,cap in slots):
      take=min(rem,cap);rem-=take;loss+=take*w
      if not rem:break
     assert rem==0
   C-=loss
  assert C>=0
  return min(base,C)

 def solve(self,actual=None):
  dp={0:(0,())}
  for k in range(1,self.v+1):
   nxt={}
   for left,(prev,hist) in dp.items():
    for p in [0]+[1<<i for i in range(self.s) if not left&(1<<i)]:
     value=self.value(k,left,p,actual)
     if value is None:continue
     target=left|p;val=prev+value
     if target not in nxt or val<nxt[target][0]:nxt[target]=(val,hist+((p,k),)*int(bool(p)))
   dp=nxt
  val,hist=dp[self.full];pos=[0]*self.s
  for p,k in hist:pos[p.bit_length()-1]=k
  return dict(bound=Fraction(val,self.D),positions=pos,counts=self.ns)

 def verify(self,z):
  p=Profile(self.v,5,z['positions'],self.ns);cs=[certificate(p,i) for i in range(self.s)]
  rr=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(self.s)})
  stubs=[frozenset(i+1 for i in range(self.s) if t&(1<<i)) for t,c in self.ns.items() for _ in range(c)]
  ir=independent_rows(self.v,p.positions,stubs)
  for a,b in zip(rr,ir):
   assert a['A']==b['A'] and a['B']==b['B'] and a['C']==b['C']
   assert a['corrected_C']==b['C']-a['deduction']
  assert total_bound(rr)==z['bound']
  z['certificates']=cs;z['rows']=rr;z['independent_ABC']=True
  return z
