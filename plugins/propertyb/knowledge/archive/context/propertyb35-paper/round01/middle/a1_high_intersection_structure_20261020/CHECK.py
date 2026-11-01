#!/usr/bin/env python3
"""Scalar capacity check and one six-point partial-pattern audit; no H search."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,time
HERE=Path(__file__).resolve().parent

def main():
 st=time.process_time();maximum=-1;at=[];feasible=0
 for A in range(37):
  for B in range(37-A):
   for t in range(16):
    if 2*t>A or 3*t>A+3*B:continue
    feasible+=1;value=17826*t-5430*B
    if value>maximum:maximum=value;at=[(A,B,t)]
    elif value==maximum:at.append((A,B,t))
 assert maximum==240240 and all(t==15 and B==5 for A,B,t in at)
 assert max(t for A in range(37) for B in range(37-A) for t in range(37)
            if 2*t<=A and 3*t<=A+3*B)==15
 assert 259248-maximum==19008
 # Independent dual-style unrounded scalar bound.
 assert 2*2766+3*4098==17826
 assert -2766-4098+6864==0
 assert -3*4098+6864==-5430
 assert 36*6864==247104
 # The five-of-six top is a fixed partial edge pattern, not a completed H21.
 Q=set(range(6));edges=[Q-{i} for i in range(5)]
 deg=[sum(v in e for e in edges) for v in range(6)]
 lam={(u,v):sum({u,v}<=e for e in edges) for u,v in combinations(range(6),2)}
 assert sorted(deg)==[4,4,4,4,4,5] and max(lam.values())==4
 assert all(len(e&f)==4 and 5 in e&f for e,f in combinations(edges,2))
 assert len(edges)==5 and Q-{5} not in edges
 out=dict(status='PASS',scalar_domain='A,B,t integers; A+B<=36; 2t<=A; 3t<=A+3B',
          feasible_scalar_tuples=feasible,maximum_weighted_eight_core=maximum,attainers=at,
          exact_t_maximum=15,remaining_weight_required=19008,
          fixed_partial_top_edges=[sorted(e) for e in edges],partial_degrees=deg,
          partial_codegree_histogram={str(c):sum(v==c for v in lam.values()) for c in set(lam.values())},
          completed_A1_H_claim=False,CPU_seconds=time.process_time()-st)
 (HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
