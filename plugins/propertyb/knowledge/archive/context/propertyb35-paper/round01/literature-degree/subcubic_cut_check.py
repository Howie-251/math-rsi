from fractions import Fraction
from pathlib import Path
import json
H=Path(__file__).parent
rows={}
for n in (24,25):
 B=175-6*n;rs=[]
 for u in range(n+1):
  general=Fraction(u*u+(24-n)*u+4*B,10)
  if u<=3:upper=0;method='r<=3'
  elif u==4:upper=(4*(6*u+B)-u*(n-u))//12;method='12m4 <= 4D-cross'
  elif u==5:
   X=4*(6*u+B)-u*(n-u)
   upper=max((X-20*q)//12+2*q for q in (0,1));method='m5 in {0,1};12m4+20m5<=4D-cross'
  else:upper=general.numerator//general.denominator;method='root fractional bound'
  assert upper<=3*u
  if u>0:assert upper<=3*u-(1 if n==24 else 3)
  if n==24 and u not in (0,4):assert upper<=3*u-2
  rs.append(dict(u=u,general_upper=str(general),integer_upper=upper,slack=3*u-upper,method=method))
 rows[str(n)]=rs
out=dict(result='PASS',pointwise_r_check=[dict(r=r,lhs=max(0,r-3),rhs=str(Fraction(2*r,5)-Fraction(r*(5-r),10))) for r in range(6)],ranges=rows)
assert all(Fraction(z['rhs'])>=z['lhs'] for z in out['pointwise_r_check'])
(H/'SUBCUBIC_CUT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({n:[(r['u'],r['integer_upper'],r['slack']) for r in rs] for n,rs in rows.items()})
