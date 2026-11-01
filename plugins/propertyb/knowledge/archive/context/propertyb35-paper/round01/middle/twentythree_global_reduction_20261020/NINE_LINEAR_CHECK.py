#!/usr/bin/env python3
"""Only the conditional pairwise-linear nine-red branch; no red-family enumeration."""
from math import comb
from itertools import product
from pathlib import Path
import json,time
p=Path(__file__).resolve().parent;st=time.process_time()
C=lambda n,k:comb(n,k) if 0<=k<=n else 0
for rho in range(10):assert comb(rho,2)>=2*rho-3
rows=[]
for i,j,k in product(range(2),repeat=3):
 for z in range(min(i,j,k)+1):
  u=12-i-j-k+z;n=C(17-u,10-u);assert n<=3*(i+j+k);rows.append([i,j,k,z,u,n])
D=comb(17,10);R=comb(13,6);B=comb(13,10);minpairs=2*36-3*17;deduction=comb(9,2)*36+(84-3*7)*minpairs;bound=9*R+22*B-deduction
assert (minpairs,deduction,bound,D-bound)==(21,2619,19117,331)
out={'status':'PASS_CONDITIONAL_LINEAR_NINE_RED','assumptions':['nine distinct outside four-sets on17points','every pair of those four-sets intersects in at most one point','22 indexed blue four-sets'],'D':D,'R':R,'B':B,'feasible_triple_parameter_rows':rows,'minimum_linear_pair_count':minpairs,'minimum_red_union_deduction':deduction,'failed_samples_upper':bound,'success_samples_lower':D-bound,'cpu_seconds':time.process_time()-st}
(p/'NINE_LINEAR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
