"""Tiny fraction arithmetic only; no original-H or coloring sample enumeration."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json
import time

t0 = time.process_time()
parts = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1)]
w = [sum(comb(x,2) for x in p) for p in parts]
p = []
for part in parts:
    occupancy = part + (0,)*(6-len(part))
    value = F(0)
    for chosen in combinations(range(6),4):
        blue, red = F(1), F(1)
        for i,n in enumerate(occupancy):
            if i in chosen:
                blue *= F(1,4) if n == 1 else int(n == 0)
                red *= F(4-n,4)
            elif n:
                red = F(0)
        value += blue + red
    p.append(value / 15)
numerators = [int(x*15360) for x in p]
assert numerators == [180,440,832,1136,1792,2048]
corrections = [numerators[i] - 180 - 326*w[i] for i in range(6)]
assert corrections == [0,-66,0,-22,308,-88]
coarse = [180 + 326*x + (308 if part == (3,2) else 0)
          for part,x in zip(parts,w)]
assert all(a <= b for a,b in zip(numerators,coarse))
assert 29*180 == 5220
assert 5220+10139 == 15359 < 15360
assert all(x % 4 == 0 for x in numerators)

alpha_rows = []
for tu in range(4):
    for tv in range(4-tu):
        bound = min(6+tu,6+tv,4*(tu+1),4*(tv+1))
        for alpha in range(bound+1):
            alpha_rows.append((tu,tv,alpha,alpha-tu-tv))
assert max(r[3] for r in alpha_rows) == 5
assert max(50+4*r[3]-8 for r in alpha_rows) == 62
g = [a*comb(5-a,2) for a in range(6)]
deficit = [6*a-3*comb(a,2)-g[a] for a in range(6)]
assert deficit == [0,0,3,6,6,0]
result = {
    'status':'PASS',
    'scope':'tiny conditional probability formula and algebra; no H enumeration',
    'probabilities':[str(x) for x in p],
    'numerators_over_15360':numerators,
    'weights':w,
    'corrections_from_180_plus_326w':corrections,
    'coarse_numerators':coarse,
    'exact_strict_integer_numerator_maximum':15356,
    'coarse_gate_maximum':10139,
    'r3_alpha_necessary_rows_checked':len(alpha_rows),
    'r3_max_alpha_minus_tau':5,
    'r3_T_flat_sumW_upper':62,
    'r4_G_flat_sumW_upper':46,
    'r5_G_flat_sumW_upper':50,
    'low_incidence_deficits':deficit,
    'selector_proved':False,
    'r6_r7_full_low_trace_geometry_checked':False,
    'original_Hs_enumerated':0,
    'original_coloring_samples_replayed':0,
    'cpu_seconds':time.process_time()-t0
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
