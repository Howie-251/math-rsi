#!/usr/bin/env python3
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
out=[]
for n in (21,22):
 N=n-5;r=10;b=N-r;D=C(N,r);red=C(N-4,r-4);blue=C(N-4,r);joint=C(N-8,r-8)
 isolated=max(c*red+(34-c)*blue-max(c-1,0)*joint for c in range(7))
 disjoint=max(c*red+(33-c)*blue-max(c-1,0)*joint for c in range(7))+C(N-5,r-5)+C(N-5,r)
 assert isolated<D and disjoint<D
 assert F(isolated,D)==({21:F(259,286),22:F(4531,4862)}[n])
 assert F(disjoint,D)==({21:F(7659,8008),22:F(2337,2431)}[n])
 # The common-low-point branch uses9R7B at21,10R7B at22.
 cr=9 if n==21 else 10;cD=C(N,cr);cR=C(N-4,cr-4);cB=C(N-4,cr);cj=C(N-8,cr-8)
 common=max(c*cR+(33-c)*cB-max(c-1,0)*cj for c in range(8))
 assert common<cD
 if n==21:assert max(c*cR+(33-c)*cB for c in range(8))<cD
 if n==22:
  assert 7*cR+26*cB==cD and 6*cj==216 and common==19232
 cases=[]
 expected={21:[6754,6611,6039],22:[17589,18161,18876]}[n]
 for j in (2,3,4):
  degree_cap=(38-9*j)//(5-j);cmax=degree_cap-1
  assert degree_cap=={2:6,3:5,4:2}[j]
  G=C(N-5+j,r)
  value=cmax*red+(33-cmax)*blue+G
  assert value==expected[j-2]<D
  assert value==max(c*red+(33-c)*blue+G for c in range(cmax+1))
  cases.append(dict(intersection=j,nonshared_red_degree_cap=degree_cap,red_attachment_cap=cmax,G_bad_count=G,union_bad_count=value,sample_count=D,strict_margin=D-value,bound=str(F(value,D))))
 out.append(dict(n=n,outside=[r,b],sample_count=D,singleton_red_count=red,singleton_blue_count=blue,isolated_bound=str(F(isolated,D)),disjoint_exception_bound=str(F(disjoint,D)),common_degree_at_most9=dict(outside_red=cr,sample_count=cD,bound=str(F(common,cD)),strict_margin=cD-common),all_common_degrees_at_least10=cases))
result=dict(status='PASS',claim='Any simple five-uniform H on21 or22 points with35 edges and a degree<=1 vertex of the non-one-intersection graph is Property B',scope='independent exact scalar check, no H enumeration',uses_G_degree_assumption=False,uses_min_degree=False,uses_max_degree=False,uses_paircover=False,rows=out,cpu_seconds=time.process_time()-start)
P.joinpath('MIN_DEGREE_FREE_REPAIR_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
