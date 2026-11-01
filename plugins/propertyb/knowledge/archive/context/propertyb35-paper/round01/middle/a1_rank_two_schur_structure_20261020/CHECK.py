from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import isqrt
import json,time
st=time.process_time()
P=Path(__file__).resolve().parent
source=P.parent/'a1_independent_set_degree_prefix_20261020/LOW19_RESULT.json'
old=json.loads(source.read_text())
profiles=[]
for rec in old['profiles']:
 if not any(mode['survives'] for mode in rec['modes']):continue
 n=rec['n'];E=sum(n)-n[1];Q=E+3*n[3]+8*n[4];t=n[4]
 values=[]
 for h in range(14,21):
  sigma=4*h+5*t;k=35-h;r=21-h
  raw=224*k-2*r*Q-(7+h)*sigma+F(sigma*sigma,16)
  polynomial=-48*h*h+(32*Q-4032-40*t)*h+125440-672*Q-560*t+25*t*t
  assert 16*raw==polynomial and polynomial>0
  values.append(polynomial)
 profiles.append({'original_n':n,'tau':rec['tau'],'E':E,'Q':Q,'t':t,
                  'sixteen_F_h14_through20':values,'low_nodes_upper':13})
assert {(p['Q'],p['t']) for p in profiles}=={(227,8),(229,7),(229,8)}
assert [p['sixteen_F_h14_through20'][::6] for p in profiles]==[[1376,9056],[1673,9977],[928,8992]]
diag=(F(15,4),F(3),F(7,4))
products=[x*y for x,y in combinations_with_replacement(diag,2)]
assert products==[F(225,16),F(45,4),F(105,16),F(9),F(21,4),F(49,16)]
assert [v for v in products if v.denominator==1 and isqrt(v.numerator)**2==v.numerator]==[F(9)]
assert (14*14+2*2)//4==50 and (12*12+3*3)//4==38
assert min(a*(a-1)//2+(7-a)*(6-a)//2 for a in range(8))==9
out={'status':'PASS','scope':'three frozen actual-moment profiles; no DP or H generation',
     'profiles':profiles,'rank_two_diag_products':[str(v) for v in products],
     'rank_two_seven_points_quad_minimum':9,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
