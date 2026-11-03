"""Export one small LP dual and an exact integer capacity certificate.

Only cached R2 sets are read; no MIP, source BFS or graph search is run.
"""
import json
import os
from pathlib import Path
import time
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
P=Path(__file__).resolve().parent;start=time.process_time()
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
r=json.loads((P/'radius2_sets.json').read_text())
balls=[set(x) for x in r['closed_R2']]
A=csc_matrix(np.array([[t in b for b in balls] for t in range(972)],dtype=float))
lp=linprog(np.ones(108),A_ub=-A,b_ub=-np.ones(972),bounds=(0,1),method='highs',options={'time_limit':2,'threads':1})
assert lp.success
dual=[max(0.0,-float(x)) for x in lp.ineqlin.marginals]
weights=[int(np.floor(1000000*x)) for x in dual]
column_sums=[sum(weights[t] for t in b) for b in balls]
W=sum(weights);C=max(column_sums)
assert W>13*C
out=dict(status='EXACT_INTEGER_ROW_CAPACITY_CERTIFICATE_EXPORTED_PENDING_INDEPENDENT_READ_CHECK',
    source_n=972,eligible_pin_count=108,cached_matrix='radius2_sets.json',LP_minimum=float(lp.fun),
    LP_row_dual_nonnegative=dual,integer_scale=1000000,row_weights=weights,
    W_total_target_weight=W,C_max_single_ball_weight=C,all_108_ball_weights=column_sums,
    W_minus_13C=W-13*C,exact_lower_bound_on_required_pins=(W+C-1)//C,
    proof='Every cover must cover total target weightW. Each chosen pin ball contributes at mostC; double counting can only increase the sum. Therefore k*C>=W, so W>13*C excludes every cover with at most13 pins.',
    independent_check_pending=True,source_BFS=0,MIP_repeated=0,cached_balls_recomputed=0,
    LP_repeated_for_dual_export=1,CPU_seconds=time.process_time()-start)
(P/'INTEGER_ROW_WEIGHTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['row_weights','LP_row_dual_nonnegative','all_108_ball_weights']}))
