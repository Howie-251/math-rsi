"""Exact Fraction checks for the double-positive-point negative-incidence budget.
Only the max-positive-occurrence<=2 branch is claimed.
"""
from fractions import Fraction as F
from pathlib import Path
import json
P=Path(__file__).resolve().parent;p=F(7,16);q=F(1,4)
alpha={s:(p**s-q**s)/s for s in range(1,9)}
assert all(alpha[s]>alpha[s+1]>0 for s in range(1,8))
chord_cases=0
for s in range(1,9):
 for j in range(s+1):
  assert p**j*q**(s-j)<=q**s+alpha[s]*j;chord_cases+=1
rows=[];expected={6:F(13331,16384),7:F(117373,131072),8:F(64049,65536)}
for m in [6,7,8]:
 B=2*m*(7-2);t=4;b=22
 J3=min(3*t,B);J4=min(4*b,max(0,B-3*t));bound=t*q**3+b*q**4+alpha[3]*J3+alpha[4]*J4
 # Independent exhaustive integer budget allocation, tiny two-arity domain.
 best=max(alpha[3]*j3+alpha[4]*j4 for j3 in range(3*t+1) for j4 in range(4*b+1) if j3+j4<=B)
 assert best==alpha[3]*J3+alpha[4]*J4
 assert bound==expected[m]<1
 rows.append(dict(m=m,D_upper=2*m,B=B,J3=J3,J4=J4,bad_bound=str(bound),gap=str(1-bound)))
out=dict(passed=True,scope=__doc__,alpha3=str(alpha[3]),alpha4=str(alpha[4]),exact_chord_cases=chord_cases,numerical_cases=rows)
(P/'DOUBLE_BUDGET_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
