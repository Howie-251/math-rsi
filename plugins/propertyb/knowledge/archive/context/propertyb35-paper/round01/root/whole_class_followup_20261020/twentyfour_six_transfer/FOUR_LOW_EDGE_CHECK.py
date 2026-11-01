"""Exact fixed-binomial and branch arithmetic; no set-family enumeration."""
from math import comb
from pathlib import Path
from time import process_time
import json

t0 = process_time()
N = comb(19, 9)
weak = 18*comb(11,5) - (3*comb(8,2)+21*comb(7,1)) - (
    3*comb(8,5)+21*comb(7,5)) + (
    12*comb(3,1)+3*comb(4,1)+3*comb(4,2))
A = 12*comb(11,5)-12*comb(7,1)-12*comb(7,5)+6*comb(3,1)
BR = 4*comb(12,5)-6*comb(8,1)
BB = 4*comb(12,6)-6*comb(8,6)
AR = 12*comb(8,5)-12*comb(4,1)
AB = 12*comb(8,2)-12*comb(4,2)
red_pinned = A+BR-AR
blue_pinned = A+BB-AB
pair = 2*A+BR+BB-AR-AB
assert (N,weak,A,red_pinned,blue_pinned,pair)==(92378,7542,5226,7722,8490,16212)
spokes = []
for p in (0,1):
    for s in range(4-2*p):
        free = (3-2*p-s)*weak+p*pair+s*blue_pinned
        fixed = 4*5005+(14+p)*3003
        bound = free+fixed
        assert bound==84688+4131*p+948*s < N
        spokes.append(dict(p=p,s=s,fixed=fixed,free=free,bound=bound,margin=N-bound))
no_spokes = [
    5*5005+14*3003+3*weak,
    4*5005+15*3003+red_pinned+2*weak,
    16*3003+4*5005+red_pinned+pair,
]
assert no_spokes == [89693,87871,92002] and max(no_spokes)<N
assert comb(13,2)==6*13==78
assert 26*2==52 < 11*5==55
out=dict(status="PASS",scope="exact binomial and finite branch arithmetic; no hypergraphs enumerated",
         sample_space=N,weak=weak,single_conflict=A,
         red_pinned=red_pinned,blue_pinned=blue_pinned,free_pair=pair,
         spoke_branches=spokes,
         no_spoke_branches=[dict(matching=c,bound=b,margin=N-b) for c,b in enumerate(no_spokes)],
         r13=dict(low_incidence=78,triple_edges=26,available_high_incidence=52,required_high_incidence=55),
         cpu_seconds=process_time()-t0)
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
