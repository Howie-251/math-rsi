"""Independent Fraction check of scalar sparse-positive profiles; no set-system enumeration."""
from fractions import Fraction as Q
from pathlib import Path
import json

q,p,r,s=Q(1,4),Q(7,16),Q(37,64),Q(175,256)
base=4*q*q+q**3+22*q**4
A2=(p*p-q*q)/2;A3=(p**3-q**3)/3;A4=(p**3*q-q**4)/3
assert A2>A3>A4>0
allocation=max(i*A2+j*A3+k*A4 for i in range(9) for j in range(4)
               for k in range(16) if i+j+k<=15)
assert allocation==8*A2+3*A3+4*A4
cross=max(i+j*q+k*q*q for i in range(2) for j in range(2)
          for k in range(5) if i+j+k<=4)
assert cross==1+q+2*q*q
five=[base,4*p*q+p*q*q+22*p*q**3,4*r*q+r*q*q+22*r*q**3,
      p*p+3*p*q+p*p*q+22*p*p*q*q,3*s*q+q*q+s*q*q+22*s*q**3,
      base+allocation,base+4*q*(r-q)+5*q*(p-q)+(r-q)*(p-q)*cross]
expected_five=list(map(Q,['45/128','315/512','1665/2048','1701/2048','6987/8192','981/1024','8181/8192']))
four=[4*q*q+23*q**4,4*p*q+23*p*q**3,4*r*q+23*r*q**3,p*p+3*p*q+23*p*p*q*q]
expected_four=list(map(Q,['87/256','609/1024','3219/4096','3255/4096']))
assert five==expected_five and four==expected_four and max(five+four)<1
base_three=3*q*q+3*q**3+21*q**4
allocation_three=max(i*A2+j*A3+k*A4 for i in range(7) for j in range(10)
                     for k in range(16) if i+j+k<=15)
assert allocation_three==6*A2+9*A3
cross_three=max(i+j*q+k*q*q for i in range(2) for j in range(4)
                for k in range(5) if i+j+k<=4)
assert cross_three==1+3*q
five_three=[base_three,3*p*q+3*p*q*q+21*p*q**3,
            3*r*q+3*r*q*q+21*r*q**3,p*p+2*p*q+3*p*p*q+21*p*p*q*q,
            3*s*q+3*s*q*q+21*s*q**3,base_three+allocation_three,
            base_three+4*q*(r-q)+5*q*(p-q)+(r-q)*(p-q)*cross_three]
four_three=[3*q*q+2*q**3+22*q**4,3*p*q+2*p*q*q+22*p*q**3,
            3*r*q+2*r*q*q+22*r*q**3,p*p+2*p*q+2*p*p*q+22*p*p*q*q]
three_three=[3*q*q+q**3+23*q**4,3*p*q+p*q*q+23*p*q**3]
assert five_three==list(map(Q,['81/256','567/1024','2997/4096','3297/4096','14175/16384','3717/4096','4041/4096']))
assert four_three==list(map(Q,['39/128','273/512','1443/2048','1575/2048']))
assert three_three==list(map(Q,['75/256','525/1024']))
assert max(five_three+four_three+three_three)<1 and 16>3
result=dict(PASS=True,five_profiles=list(map(str,five)),four_profiles=list(map(str,four)),
            chord_slopes=list(map(str,[A2,A3,A4])),max_joint_cross_weight=str(cross),
            worst_five=str(max(five)),worst_four=str(max(four)),
            three_negative_pair_five_profiles=list(map(str,five_three)),
            three_negative_pair_four_profiles=list(map(str,four_three)),
            three_negative_pair_three_profiles=list(map(str,three_three)),
            three_negative_pair_joint_cross_weight=str(cross_three),
            two_positive_disjoint_candidates=16,negative_pair_blockers=3,
            scope=__doc__)
(Path(__file__).resolve().parent/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(result)
