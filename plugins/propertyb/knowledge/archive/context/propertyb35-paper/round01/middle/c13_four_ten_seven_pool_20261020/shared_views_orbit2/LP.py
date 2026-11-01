"""Nonnegative failed-view marginal LP; exact rational witness checked separately."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import json,time
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent;st=time.process_time();d=json.loads((P/'TABLES.json').read_text());v=d['failed_views']
A=[list(row) for row in zip(*(z['c']+[int(z['r']==7),int(z['r']==9)] for z in v))]
b=d['target_columns']+[9,8]
pr=linprog(np.zeros(len(v)),A_eq=np.array(A,dtype=float),b_eq=b,bounds=(0,None),method='highs',options={'time_limit':4})
def exactsolve(matrix,rhs):
 M=[[F(x) for x in row]+[F(y)] for row,y in zip(matrix,rhs)];n=len(M);k=len(M[0])-1;r=0;piv=[]
 for c in range(k):
  found=next((i for i in range(r,n) if M[i][c]),None)
  if found is None:continue
  M[r],M[found]=M[found],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
  for i in range(n):
   if i!=r and M[i][c]:q=M[i][c];M[i]=[a-q*z for a,z in zip(M[i],M[r])]
  piv.append(c);r+=1
 for row in M:assert any(row[:k]) or not row[k]
 x=[F() for _ in range(k)]
 for i,c in enumerate(piv):x[c]=M[i][k]
 return x
out=dict(scope=__doc__,primal_status=int(pr.status),primal_message=str(pr.message),variables=len(v),constraints=len(b),T=d['T'],rhs=b)
if pr.success:
 support=[i for i,x in enumerate(pr.x) if x>1e-8];small=[[row[i] for i in support] for row in A];xx=exactsolve(small,b)
 assert all(x>=0 for x in xx) and all(sum(F(a)*x for a,x in zip(row,xx))==rhs for row,rhs in zip(small,b))
 witness=[dict(failed_index=i,view_index=v[i]['index'],weight=str(x),r=v[i]['r'],c=v[i]['c'],pure_quota=v[i]['pure_quota'],positions=v[i]['positions'],bound=v[i]['bound']) for i,x in zip(support,xx) if x]
 out.update(status='EXACT_FEASIBLE_FAILED_VIEW_MARGINAL',witness=witness,all_equalities_exact=True)
elif pr.status==2:
 dual=linprog(np.array(b,dtype=float),A_ub=-np.array(A,dtype=float).T,b_ub=np.zeros(len(v)),bounds=[(-1,1)]*len(b),method='highs',options={'time_limit':4})
 assert dual.success and dual.fun<0
 y=[F(float(t)).limit_denominator(1000000) for t in dual.x]
 den=lcm(*(t.denominator for t in y));yy=[int(t*den) for t in y]
 values=[sum(yy[j]*A[j][i] for j in range(len(b))) for i in range(len(v))];rhs=sum(a*z for a,z in zip(b,yy))
 assert min(values)>=0 and rhs<0
 out.update(status='EXACT_FARKAS_DUAL_FAILED_VIEWS_IMPOSSIBLE',dual_integer=yy,minimum_failed_column=min(values),weighted_rhs=rhs,all_failed_columns_exact=True,failed_columns=len(v))
else:out.update(status='LP_NOT_DECIDED_NO_CLAIM')
out['cpu_seconds']=time.process_time()-st
(P/'LP_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
