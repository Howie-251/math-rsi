"""Exact arithmetic for the seven possible repeated-positive point profiles."""
from fractions import Fraction as F
from pathlib import Path
import json

q=F(1,4); p=F(7,16); r=F(37,64); s=F(175,256)
base=4*q*q+q**3+22*q**4
a2=(p*p-q*q)/2
a3=(p**3-q**3)/3
a4=(p**3*q-q**4)/3
assert a2>a3>a4>0
resource_max=max(j2*a2+j3*a3+j4*a4
                 for j2 in range(9) for j3 in range(4) for j4 in range(16)
                 if j2+j3+j4<=15)
assert resource_max==8*a2+3*a3+4*a4
dx=r-q;dy=p-q
bounds={
 'none':base,
 'one_occ2':4*p*q+p*q*q+22*p*q**3,
 'one_occ3':4*r*q+r*q*q+22*r*q**3,
 'two_occ2':p*p+3*p*q+p*p*q+22*p*p*q*q,
 'one_occ4':3*s*q+q*q+s*q*q+22*s*q**3,
 'three_occ2':base+resource_max,
 'occ3_and_occ2':base+4*q*dx+5*q*dy+dx*dy*(1+q+2*q*q),
}
assert all(v<1 for v in bounds.values())
assert max(bounds.values())==F(8181,8192)
out={'complete':True,'method':'seven positive-occurrence profiles; exact rational inequalities, no set-layout search',
     'bounds':{k:str(v) for k,v in bounds.items()},'maximum':str(max(bounds.values())),
     'chord_slopes':list(map(str,(a2,a3,a4))),
     'three_double_resource_maximum':str(resource_max)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
