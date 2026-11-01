"""Scalar arithmetic for the two disjoint three-star proof; no set-family generation."""
from fractions import Fraction as Q
from pathlib import Path
import json
alpha=Q(3125,13122);beta=Q(12005,131072)
assert Q(5,16)<=alpha+beta and Q(6,81)<=alpha and Q(6,256)<=beta
assert 3*alpha>=4*beta
low=(9*alpha+12*beta)/4+Q(5,9)**3
assert low==Q(31279645,31850496)<1
# Two core points use at most eight original negative incidences.
old_disjoint=max(16*t2+4*t1+t0+4*b2+b1
    for t2 in range(4) for t1 in range(4-t2) for t0 in range(4-t2-t1)
    for b2 in range(5) for b1 in range(9) if 2*t2+t1+2*b2+b1<=8)
assert old_disjoint==52
forbidden=[]
for n in range(4):
    exact=max(k+l for k in range(4-n) for l in range(5)
              if k+2*l<=8-2*n)
    assert exact==(11-3*n)//2
    forbidden.append(exact)
assert forbidden==[5,4,2,1]
unique_n0=max(4*k+3-k for k in range(4));assert unique_n0==12<36
unique_n1_c3=max(4*k+2-k for k in range(3));assert unique_n1_c3==8<12
n1_c4=[k for k in range(3) if 6-8+k>=0]
assert n1_c4==[2]
for M in range(2,5):
    exact=max(s*M+j*M+l+t0 for s in range(2) for j in range(3)
              for l in range(5) for t0 in range(2-s) if s+2*j+l<=4)
    assert exact==2*M+1<4*M
result=dict(PASS=True,scope=__doc__,six_mixed_low_bound=str(low),
            six_mixed_low_margin=str(1-low),old_disjoint_block=old_disjoint,
            forbidden_pair_bounds=forbidden,n0_unique_overlap_block=unique_n0,
            n1_unique_overlap_c3_block=unique_n1_c3,
            n1_c4_only_feasible_k=n1_c4,n2_disjoint_bound='2M+1<4M (M=2,3,4)',
            high_mixed_three_disjoint_comparison='8<27')
(Path(__file__).resolve().parent/'CHECK_TWO_THREE_STARS.json').write_text(json.dumps(result,indent=2)+'\n')
print(result)
