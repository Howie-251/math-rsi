"""Exact minimization over every increasing lock position, for fixed labelled types.
Weights depend only on current position, preceding lock count and pivot status.
No original hypergraphs are enumerated. Returned winner is independently replayed.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,edge_weight,pair_weight,json_value
from pure_quota import certificate as pure
from avoided_lock_quotas import certificate as avoided
from independent_structure_bounds import independent_rows

def solve(v,counts,s,actual,use_avoided=False):
 details={}
 for k in range(1,v+1):
  for j in range(s+1):
   if j>k-1:continue
   for pivot in (False,True):
    j2=j+int(pivot)
    if j2>s or s-j2>v-k:continue
    pos=tuple(range(1,j+1))+(k,)*int(pivot)+tuple(range(k+1,k+1+s-j2));p=Profile(v,5,pos,counts)
    A=sum((n*edge_weight(v,5,pos,t,k,True) for t,n in counts.items()),Fraction())
    B=sum((n*edge_weight(v,5,pos,t,k,False) for t,n in counts.items()),Fraction())
    C=sum((n*(m-int(t==u))*pair_weight(v,5,pos,t,u,k) for t,n in counts.items() for u,m in counts.items()),Fraction())
    cs=(avoided if use_avoided else pure)(p,j) if pivot else None
    loss=cs['loss'] if cs else Fraction()
    if pivot and j in actual:
     t,u=actual[j];loss=pair_weight(v,5,pos,t,u,k)+pair_weight(v,5,pos,u,t,k)
    details[k,j,pivot]=min(A,B,C-loss)
 dp={(0,0):(Fraction(),())}
 for k in range(1,v+1):
  for j in range(s+1):
   if (k-1,j) not in dp:continue
   old,pos=dp[k-1,j]
   for pivot in (False,True):
    key=k,j,pivot
    if key not in details:continue
    dst=k,j+int(pivot);b=old+details[key]
    if dst not in dp or b<dp[dst][0]:dp[dst]=(b,pos+(k,)*int(pivot))
 b,pos=dp[v,s];p=Profile(v,5,pos,counts);cs=[(avoided if use_avoided else pure)(p,i) for i in range(s)];losses={pos[i]:cs[i]['loss'] for i in range(s)}
 for i,(t,u) in actual.items():losses[pos[i]]=pair_weight(v,5,pos,t,u,pos[i])+pair_weight(v,5,pos,u,t,pos[i])
 rs=rows(p,deductions=losses)
 assert b==total_bound(rs)
 stubs=[frozenset(i+1 for i in range(s) if t&(1<<i)) for t,n in counts.items() for _ in range(n)]
 ir=independent_rows(v,pos,stubs)
 assert all(all(a[z]==c[z] for z in ('A','B','C')) for a,c in zip(rs,ir))
 return dict(bound=b,positions=pos,counts=counts,actual=actual,certificates=cs,rows=rs,independent_ABC=True)

