from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

types = [(x,p,b,v) for x,p in product(range(2), repeat=2)
         for b in range(6) for v in range(6)
         if x+p+b+v == 5 and 6*x+7*p+8*b+9*v == 39]
assert set(types) == {(1,0,3,1),(0,1,4,0),(1,1,1,2)}
# Coordinates: constant, n3, n4, tau.
n1 = (368,3,8,-2)
n2 = (140,-3,-6,1)
lhs = [5016*n1[i]+2520*n2[i] for i in range(4)]
lhs[0] += 2376
lhs[1] += 4368
lhs[2] += 3192
assert lhs == [2201064,11856,28200,-7512]
threshold = F(2722720-lhs[0],24)
assert threshold == F(65207,3)
integer_threshold = -(-threshold.numerator // threshold.denominator)
assert integer_threshold == 21736
out = {"status":"PASS", "degree_sum_39_types_x_p_eight_nine":types,
       "N34_upper":3,"P_constant_numerator":198,
       "expanded_L":lhs,"unrounded_threshold":str(threshold),
       "integer_necessary":[494,1175,-313,integer_threshold]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
