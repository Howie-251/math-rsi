"""Candidate new bound for the all-pair local profile: random lock ordering.
The full type multiset is invariant under every lock permutation. At each locked
position, average the exact weight of each FIXED actual bad pair over all lock
orders; categories are pure/pure, pure/pair, pair/pair. Then use the proved total
and pure bad-pair quotas. Concavity gives E[min(A,B,C-loss)] <= min(A,B,C-E[loss]).
Dynamic programming finds the exact best positional pattern for this averaged
bound; states are (position, number of preceding locks), not whole hypergraphs.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import comb
import json,sys,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,edge_weight,pair_weight,link_q_lower,json_value,rows,total_bound

def averaged_loss(v,s,d,positions,j):
 bit=1<<j;k=positions[j];single=d-s+1
 def w(t,u):return pair_weight(v,5,positions,t,u,k)+pair_weight(v,5,positions,u,t,k)
 others=[1<<h for h in range(s) if h!=j]
 slots=[dict(category='pure-pure',weight=w(bit,bit),capacity=comb(single,2)),
  dict(category='pure-pair',weight=sum((w(bit,bit|h) for h in others),Fraction(0))/(s-1),capacity=single*(s-1)),
  dict(category='pair-pair',weight=sum((w(bit|h,bit|g) for h,g in combinations(others,2)),Fraction(0))/comb(s-1,2),capacity=comb(s-1,2))]
 q=link_q_lower(v,5,d);r=max(0,(4*single-(v-s)+2)//3)
 assert r<=slots[0]['capacity']
 loss=r*slots[0]['weight'];slots[0]['capacity']-=r;rem=max(0,q-r)
 for x in sorted(slots,key=lambda x:x['weight']):
  take=min(rem,x['capacity']);rem-=take;loss+=take*x['weight']
 assert rem==0
 return loss,dict(q_total=q,q_pure=r,slots=slots)

def solve(v,s,d):
 ns={sum(1<<i for i in ij):1 for ij in combinations(range(s),2)}
 for i in range(s):ns[1<<i]=d-s+1
 ns[0]=34-sum(ns.values());ns={t:c for t,c in ns.items() if c}
 assert min(ns.values())>0
 states={};details={}
 for k in range(1,v+1):
  for j in range(s+1):
   if j>k-1:continue
   for pivot in (False,True):
    nextj=j+int(pivot)
    if nextj>s or s-nextj>v-k:continue
    pos=tuple(range(1,j+1))+(k,)*int(pivot)+tuple(range(k+1,k+1+s-nextj))
    p=(v,5,pos);A=sum((c*edge_weight(*p,t,k,True) for t,c in ns.items()),Fraction(0));B=sum((c*edge_weight(*p,t,k,False) for t,c in ns.items()),Fraction(0))
    C=sum((c*(ns.get(u,0)-int(t==u))*pair_weight(*p,t,u,k) for t,c in ns.items() for u in ns),Fraction(0))
    loss,cert=averaged_loss(v,s,d,pos,j) if pivot else (Fraction(0),None)
    value=min(A,B,C-loss)
    details[k,j,pivot]=dict(A=A,B=B,C=C,averaged_loss=loss,bound=value,certificate=cert)
 dp={(0,0):(Fraction(0),())}
 for k in range(1,v+1):
  for j in range(s+1):
   if (k-1,j) not in dp:continue
   previous,positions=dp[k-1,j]
   for pivot in (False,True):
    key=(k,j,pivot)
    if key not in details:continue
    nxt=(k,j+int(pivot));value=previous+details[key]['bound'];pos=positions+(k,)*int(pivot)
    if nxt not in dp or value<dp[nxt][0]:dp[nxt]=(value,pos)
 best,pos=dp[v,s];p=Profile(v,5,pos,ns);outrows=[]
 for k in range(1,v+1):outrows.append(dict(k=k,**details[k,sum(x<k for x in pos),k in pos]))
 assert sum(r['bound'] for r in outrows)==best
 return dict(v=v,s=s,degree=d,counts=ns,bound=best,positions=pos,rows=outrows)

if __name__=='__main__':
 start=time.perf_counter();r=solve(24,5,7)
 out=dict(scope=__doc__,elapsed_seconds=time.perf_counter()-start,result=r)
 Path(__file__).with_name('SYMMETRIC_K5.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
 print(r['positions'],r['bound'],float(r['bound']))
