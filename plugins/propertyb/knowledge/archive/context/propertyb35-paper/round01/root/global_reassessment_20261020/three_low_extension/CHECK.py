"""One authorized row/column partition prototype, not a hypergraph search."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
from time import process_time
import json

t0 = process_time()
points = [(i,j) for i in range(5) for j in range(5) if i != j]
rows = [sum(1 << k for k,(i,j) in enumerate(points) if i == a) for a in range(5)]
cols = [sum(1 << k for k,(i,j) in enumerate(points) if j == a) for a in range(5)]
assert all(x.bit_count() == 4 for x in rows+cols)
counts = Counter()
joint_sources = Counter()
for chosen in combinations(range(20),10):
    blue = sum(1 << x for x in chosen)
    row_blue = [i for i,m in enumerate(rows) if blue & m == m]
    row_red = [i for i,m in enumerate(rows) if blue & m == 0]
    col_blue = [i for i,m in enumerate(cols) if blue & m == m]
    col_red = [i for i,m in enumerate(cols) if blue & m == 0]
    row_bad = bool(row_blue and row_red)
    col_bad = bool(col_blue and col_red)
    counts[(row_bad,col_bad)] += 1
    if row_bad and col_bad:
        assert len(row_blue) == len(row_red) == len(col_blue) == len(col_red) == 1
        assert col_blue == row_red and col_red == row_blue
        joint_sources[(row_red[0],row_blue[0])] += 1

N = comb(20,10)
C_num = 20*comb(12,6)-60*comb(8,2)+30*comb(4,2)
p1,p0 = F(comb(10,4),comb(20,4)),F(2*comb(10,5),comb(20,5))
assert N == 184756 and C_num == 16980
assert sum(v for (r,c),v in counts.items() if r) == C_num
assert sum(v for (r,c),v in counts.items() if c) == C_num
assert counts[(True,True)] == 400
assert set(joint_sources.values()) == {20} and len(joint_sources) == 20
assert p1*N == 8008 and p0*N == 6006
assert 3*C_num-2*8008+21*6006 == 161050
base12 = F(161050+2002*12,N)
corrected12 = base12 - F(400,N)
assert base12 == F(92537,92378) > 1
assert corrected12 == F(92337,92378) < 1
assert corrected12 == 1-F(82,N)
result = {
    'status':'PASS',
    'scope':'one off-diagonal 5x5 row/column pair on 20 points',
    'points':points,
    'samples_checked':N,
    'single_conflict_count':C_num,
    'single_conflict_probability':str(F(C_num,N)),
    'row_column_joint_count':400,
    'row_column_joint_probability':str(F(400,N)),
    'ordered_red_blue_row_sources':len(joint_sources),
    'joint_samples_per_ordered_source':20,
    'p1':str(p1),'p0':str(p0),
    'p1_count_over_N':8008,'p0_count_over_N':6006,
    'original_bound_numerator':'161050+2002*(D-5*alpha)',
    'original_strict_integer_threshold':'D-5*alpha <= 11',
    'corrected_prototype_bound_numerator':'160650+2002*(D-5*alpha)',
    'corrected_prototype_strict_integer_threshold':'D-5*alpha <= 12',
    'D12_alpha0_uncorrected':str(base12),
    'D12_alpha0_corrected':str(corrected12),
    'D12_alpha0_margin':str(1-corrected12),
    'general_partition_joint_lower_bound_proved':False,
    'original_Hs_enumerated':0,
    'cpu_seconds':process_time()-t0
}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'points'},indent=2))
