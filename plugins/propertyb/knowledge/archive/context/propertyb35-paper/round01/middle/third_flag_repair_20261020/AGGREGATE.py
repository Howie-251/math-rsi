import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from itertools import combinations_with_replacement
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json,time
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
beta=[84,210,462,924,1716]
patterns=[]
# Pair intersections sorted; the central triple intersection determines all seven Venn atoms.
for js in combinations_with_replacement(range(5),3):
 for t in range(min(js)+1):
  a,b,c=js
  if any(v<0 for v in (5-a-b+t,5-a-c+t,5-b-c+t)):continue
  flag=sum(beta[js[k]] for k in range(3) if t==0 and all(js[l]==1 for l in range(3) if l!=k))
  flags=[sum(1 for k in range(3) if js[k]==j and t==0 and all(js[l]==1 for l in range(3) if l!=k)) for j in range(5)]
  patterns.append({'pair_intersections':js,'triple_intersection':t,'weighted_flags':flag,'flags_by_outer_intersection':flags})
# Variables n0..n4, tau, then triple-pattern counts.
CBASE=6+len(patterns);N=CBASE+9;eq=[];rhs=[];ub=[];ubr=[]
def row():return np.zeros(N)
a=row();a[:5]=1;eq.append(a);rhs.append(595)
a=row();a[:5]=range(5);eq.append(a);rhs.append(648)
a=row();a[:5]=[comb(j,2) for j in range(5)];a[5]=-1;eq.append(a);rhs.append(140)
for j in range(5):
 a=row();a[j]=-33
 for i,p in enumerate(patterns):a[6+i]=p['pair_intersections'].count(j)
 eq.append(a);rhs.append(0)
a=row()
for i,p in enumerate(patterns):a[6+i]=p['triple_intersection']
eq.append(a);rhs.append(1399)
# Actual point-pair triple moment is between tau and 3tau because lambda<=9.
a=row();a[5]=1
for i,p in enumerate(patterns):a[6+i]=-comb(p['triple_intersection'],2)
ub.append(a);ubr.append(0)
a=-a.copy();a[5]=-3;ub.append(a);ubr.append(0)
# For a fixed outer pair F,H with intersection j, each flag G uses
# two exclusive-point occurrences. Each exclusive point has at most8
# third edges after its own outer edge: flags<=8(5-j), and <=33.
for j in range(5):
 a=row();a[j]=-min(33,8*(5-j))
 for i,p in enumerate(patterns):a[6+i]=p['flags_by_outer_intersection'][j]
 ub.append(a);ubr.append(0)
# A covered cross point-pair contributes at most2 unless lambda>=3.
# For j4, common-four matching multiplicity <=9-lambda;
# for j2/3 the crude ordered-exclusive-edge multiplicity <=(9-lambda)^2.
for j,base,price in ((2,18,36),(3,8,36),(4,2,6)):
 a=row();a[j]=-base;a[5]=-price
 for i,p in enumerate(patterns):a[6+i]=p['flags_by_outer_intersection'][j]
 ub.append(a);ubr.append(0)
# Preserve the same codegree distribution in both triple-common moment
# and flag-capacity constraints, rather than optimizing tau uses independently.
for coeff,target in (([1]*9,210),(list(range(1,10)),350)):
 a=row();a[CBASE:]=coeff;eq.append(a);rhs.append(target)
a=row();a[5]=-1
for l in range(1,10):a[CBASE+l-1]=comb(l-1,2)
eq.append(a);rhs.append(0)
a=row()
for i,p in enumerate(patterns):a[6+i]=comb(p['triple_intersection'],2)
for l in range(1,10):a[CBASE+l-1]=-comb(l,3)
eq.append(a);rhs.append(0)
for j,base in ((2,18),(3,8),(4,2)):
 a=row();a[j]=-base
 for i,p in enumerate(patterns):a[6+i]=p['flags_by_outer_intersection'][j]
 for l in range(3,10):a[CBASE+l-1]=-(9-l)**(1 if j==4 else 2)*(l-2)
 ub.append(a);ubr.append(0)
obj=row()
for i,p in enumerate(patterns):obj[6+i]=p['weighted_flags']
bounds=[(0,None)]*N;bounds[1]=(397,None)
st=time.process_time();r=linprog(-obj,A_eq=eq,b_eq=rhs,A_ub=ub,b_ub=ubr,bounds=bounds,method='highs')
out={'patterns':len(patterns),'status':r.message,'cpu_seconds':time.process_time()-st,'threshold_numerator':2722720,'denominator':352716}
if r.success:
 z=[F(float(x)).limit_denominator(1000000) for x in r.x]
 # independent exact constraints written explicitly rather than reusing float matrices.
 n=z[:5];tau=z[5];p=z[6:CBASE];lam=z[CBASE:]
 assert sum(n)==595 and sum(j*n[j] for j in range(5))==648 and sum(comb(j,2)*n[j] for j in range(5))==140+tau and n[1]>=397
 assert all(x>=0 for x in z)
 for j in range(5):assert sum(v*q['pair_intersections'].count(j) for v,q in zip(p,patterns))==33*n[j]
 assert sum(v*q['triple_intersection'] for v,q in zip(p,patterns))==1399
 m2=sum(v*comb(q['triple_intersection'],2) for v,q in zip(p,patterns));assert tau<=m2<=3*tau
 for j in range(5):assert sum(v*q['flags_by_outer_intersection'][j] for v,q in zip(p,patterns))<=min(33,8*(5-j))*n[j]
 for j,base,price in ((2,18,36),(3,8,36),(4,2,6)):
  assert sum(v*q['flags_by_outer_intersection'][j] for v,q in zip(p,patterns))<=base*n[j]+price*tau
 assert sum(lam)==210 and sum(l*v for l,v in enumerate(lam,1))==350
 assert sum(comb(l-1,2)*v for l,v in enumerate(lam,1))==tau
 assert sum(comb(l,3)*v for l,v in enumerate(lam,1))==m2
 for j,base in ((2,18),(3,8),(4,2)):
  assert sum(v*q['flags_by_outer_intersection'][j] for v,q in zip(p,patterns))<=base*n[j]+sum((9-l)**(1 if j==4 else 2)*max(l-2,0)*v for l,v in enumerate(lam,1))
 val=sum(v*q['weighted_flags'] for v,q in zip(p,patterns));out.update(exact_objective=str(val),EU=str(val/F(352716)),n=[str(v) for v in n],tau=str(tau),pointpair_codegree_counts=[str(v) for v in lam],pointpair_third_moment=str(m2),exact_constraints='PASS',witness=[dict(q,count=str(v)) for q,v in zip(patterns,p) if v])
(P/'AGGREGATE.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='witness'})
