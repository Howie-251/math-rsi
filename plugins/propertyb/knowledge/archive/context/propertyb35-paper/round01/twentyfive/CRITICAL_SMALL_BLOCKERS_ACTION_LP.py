"""Bounded fourteen-type moment LP for all-j critical low-edge actions.
A feasible LP point is a relaxation witness, never an actual hypergraph.
Odd-order balance ties of difference1 receive no unproved singleton constraint.
"""
from pathlib import Path
from itertools import product
from math import comb
from fractions import Fraction as Q
import json,time
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent;st=time.perf_counter();C=lambda n,k:comb(n,k) if 0<=k<=n else 0

def model(n,M,DG,a):
 b=n-5-a;types=[(r,s,5-r-s) for r in range(5) for s in range(a+1) if 1<=5-r-s<=min(4,b)];eq=[[1]*len(types),[r for r,s,t in types]];rhs=[M-1,DG-5];ge=[];bounds=[];names=[]
 def add(row,bd,name):ge.append(row);bounds.append(bd);names.append(name)
 add([s for r,s,t in types],7*a,'degree_red_outside');add([t for r,s,t in types],7*b,'degree_blue_outside')
 add([r*s for r,s,t in types],5*a,'cover_G_red');add([r*t for r,s,t in types],5*b,'cover_G_blue');add([C(s,2) for r,s,t in types],C(a,2),'cover_red_red');add([s*t for r,s,t in types],a*b,'cover_red_blue');add([C(t,2) for r,s,t in types],C(b,2),'cover_blue_blue')
 for j in range(b+1):add([int((r,s,t)==(1,0,4))*C(b-4,j)+(5-r)*C(b-t,j-t) for r,s,t in types],5*C(b,j),f'action_j{j}')
 R=5+a
 if b-R>=2:add([int(t==1) for r,s,t in types],b,'balanced_blue_majority_singletons')
 if R-b>=2:add([int((r,s,t)==(0,1,4)) for r,s,t in types],a,'balanced_red_majority_zero_G_blue_critical')
 return dict(n=n,M=M,DG=DG,a=a,b=b,types=types,equalities=eq,equality_rhs=rhs,ge=ge,ge_rhs=bounds,ge_names=names)

def solve_exact(A,y):
 a=[[Q(v) for v in row]+[Q(vv)] for row,vv in zip(A,y)];m=len(a);n=len(a[0])-1;piv=[];rr=0
 for col in range(n):
  k=next((k for k in range(rr,m) if a[k][col]),None)
  if k is None:continue
  a[rr],a[k]=a[k],a[rr];v=a[rr][col];a[rr]=[x/v for x in a[rr]]
  for j in range(m):
   if j!=rr and a[j][col]:v=a[j][col];a[j]=[x-v*z for x,z in zip(a[j],a[rr])]
  piv.append(col);rr+=1
  if rr==m:break
 if any(not any(row[:n]) and row[n] for row in a):return None
 if len(piv)!=n:return None
 x=[Q(0)]*n
 for j,col in enumerate(piv):x[col]=a[j][-1]
 return x

def rational(m,x):
 k=len(x);A=list(m['equalities']);y=list(m['equality_rhs'])
 for row,bd in zip(m['ge'],m['ge_rhs']):
  if abs(sum(v*z for v,z in zip(row,x))-bd)<1e-6:A.append(row);y.append(bd)
 for j,v in enumerate(x):
  if abs(v)<1e-7:A.append([int(i==j) for i in range(k)]);y.append(0)
 xx=solve_exact(A,y)
 if xx is None:return None
 if any(v<0 for v in xx):return None
 if any(sum(Q(v)*z for v,z in zip(row,xx))!=bd for row,bd in zip(m['equalities'],m['equality_rhs'])):return None
 if any(sum(Q(v)*z for v,z in zip(row,xx))<bd for row,bd in zip(m['ge'],m['ge_rhs'])):return None
 return xx

results=[];witness=None
for n,M,maxDG in [(24,34,35),(24,35,36),(23,34,37),(23,35,38)]:
 for DG in range(35,maxDG+1):
  for a in range(1,n-5):
   m=model(n,M,DG,a);t=time.perf_counter();res=linprog(np.zeros(len(m['types'])),A_ub=-np.array(m['ge'],dtype=float),b_ub=-np.array(m['ge_rhs'],dtype=float),A_eq=np.array(m['equalities'],dtype=float),b_eq=m['equality_rhs'],bounds=(0,None),method='highs',options={'time_limit':2});r=dict(n=n,M=M,DG=DG,a=a,b=m['b'],status=int(res.status),elapsed_seconds=time.perf_counter()-t);results.append(r)
   if res.success and witness is None:
    xx=rational(m,res.x)
    if xx is not None:
     witness=dict(**m,values=[str(v) for v in xx],support=[dict(r=rr,s=ss,t=tt,N=str(v)) for (rr,ss,tt),v in zip(m['types'],xx) if v],ge_slacks=[dict(name=name,value=str(sum(Q(v)*z for v,z in zip(row,xx))-bd)) for name,row,bd in zip(m['ge_names'],m['ge'],m['ge_rhs'])],exact_passed=True)
summary=dict(scope=__doc__,models=len(results),feasible=sum(z['status']==0 for z in results),reported_infeasible=sum(z['status']==2 for z in results),other=sum(z['status'] not in [0,2] for z in results),elapsed_seconds=time.perf_counter()-st,by_branch=[dict(n=n,M=M,models=sum(z['n']==n and z['M']==M for z in results),feasible=sum(z['n']==n and z['M']==M and z['status']==0 for z in results)) for n,M in [(24,34),(24,35),(23,34),(23,35)]])
(P/'CRITICAL_SMALL_BLOCKERS_ACTION_LP.json').write_text(json.dumps(dict(summary=summary,exact_relaxation_witness=witness,results=results),indent=2)+'\n');print(json.dumps(summary,indent=2));print('witness',json.dumps(None if witness is None else {k:witness[k] for k in ['n','M','DG','a','b','support','exact_passed']},indent=2))
