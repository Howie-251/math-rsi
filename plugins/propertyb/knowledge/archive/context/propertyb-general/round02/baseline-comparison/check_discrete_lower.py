"""Exact rational evaluation of finite-position formula versus analytic lower bound."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path

import mpmath as mp

from profile import discrete_lower


def choose(n,r):
    return comb(n,r) if n>=r>=0 else 0


def exact_discrete(k,v,m,gamma):
    total=Fraction(0)
    d1=comb(v-1,k-1)
    d2=comb(v-k,k-1)
    for h in range(1,v+1):
        left,right=choose(h-1,k-1),choose(v-h,k-1)
        total += min(Fraction(m*k*left,v*d1),
                     Fraction(m*k*right,v*d1),
                     Fraction(gamma*left*right,v*d1*d2))
    return total


mp.mp.dps=90
rows=[]
for k in range(2,9):
    for v in [2*k-1,3*k+2,7*k+3]:
        m=2**k+3
        gamma=m*(m-1)-(m//3)*(m//3-1)
        exact=exact_discrete(k,v,m,gamma)
        low,_,_=discrete_lower(k,v,m,gamma)
        actual=mp.mpf(exact.numerator)/exact.denominator
        assert low<=actual+mp.mpf('1e-75'),(k,v,low,actual)
        rows.append(dict(k=k,v=v,m=m,gamma=gamma,
                         exact_D=str(exact),D_minus_lower=str(actual-low)))
receipt=dict(status='PASS',cases=len(rows),
             min_margin=str(min(mp.mpf(x['D_minus_lower']) for x in rows)),
             scope='Exact rational D; 90-digit evaluation of derived lower bound',
             rows=rows)
Path(__file__).with_name('DISCRETE_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='rows'}))
