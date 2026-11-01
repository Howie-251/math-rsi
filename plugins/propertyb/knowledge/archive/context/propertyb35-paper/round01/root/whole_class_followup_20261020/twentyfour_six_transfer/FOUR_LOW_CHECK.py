"""Only fixed binomial arithmetic for the analytic two-pair repair."""
from fractions import Fraction
from math import comb
from pathlib import Path
from time import process_time
import json

t0=process_time()
N=comb(19,9)
individual=12*comb(11,5)-12*comb(7,1)-12*comb(7,5)+6*comb(3,1)
core_red=4*comb(12,5)-6*comb(8,1)
core_blue=4*comb(12,6)-6*comb(8,6)
assert individual==5226 and core_red==3120 and core_blue==3528
pair=2*individual+core_red+core_blue
weak=7542
fixed_pair=4*5005+4*3003
six=fixed_pair+11*3003+pair+weak
seven=fixed_pair+10*3003+pair+13*924
eight=fixed_pair+9*3003+pair+18*924-comb(10,4)-comb(10,5)
assert (pair,six,seven,eight)==(17100,89707,91174,92329)
assert max(six,seven,eight)<N
out={'status':'PASS','scope':'fixed exact binomial arithmetic; no hypergraph or set-family enumeration',
     'sample_space':N,'four_disjoint_blocks_conflict':individual,
     'pair_extra_core_red_bound':core_red,'pair_extra_core_blue_bound':core_blue,
     'free_pair_failure_bound':pair,
     'fifth_degree_6_failure_bound':six,'fifth_degree_7_failure_bound':seven,
     'fifth_degree_8_failure_bound':eight,
     'strict_margins':[N-six,N-seven,N-eight],
     'probabilities':[str(Fraction(v,N)) for v in (six,seven,eight)],
     'cpu_seconds':process_time()-t0}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
