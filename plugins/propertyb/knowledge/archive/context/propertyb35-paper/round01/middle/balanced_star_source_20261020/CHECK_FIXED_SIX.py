from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json
import time

start=time.process_time()
p=29*Fraction(21,646)+90*Fraction(70,comb(20,10))
assert p==Fraction(180474,184756)<1
stars=[]
for b,q in product(range(4,11),range(5)):
    for a1,a2,a3,a4 in product(range(6),repeat=4):
        if a1+a2+a3+a4!=5 or a1+2*a2+3*a3+4*a4!=b+q or a4<1:continue
        assert b+q>=8
        if a4==1:
            ap=(a3,a2,a1,1)
            bp,qp=20-b,4-q
            assert sum(ap)==5 and sum((i+1)*ap[i] for i in range(4))==bp+qp
            assert (ap[2],ap[1],ap[0],1)==(a1,a2,a3,a4)
            if b==10:
                assert a3-a1==q-2
                assert a3<=(q+2)//2
        stars.append([b,q,a1,a2,a3,a4])
rows10=[r for r in stars if r[0]==10 and r[-1]==1]
result={'status':'PASS','source_probability':str(p),'all_small_star_rows':stars,
        'b10_single_N4_rows':rows10,'cpu_seconds':time.process_time()-start,
        'scope':'Balanced-entry scalar and six-star integer types only; no hypergraph enumeration'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='all_small_star_rows'}))
