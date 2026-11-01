"""One bounded 246-profile integer-feasibility pilot, then exact readback."""
import json
import resource
import warnings
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
from time import process_time, monotonic
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

resource.setrlimit(resource.RLIMIT_CPU, (60,60))
start, wall = process_time(), monotonic()
P = Path(__file__).parent
profiles = [p for p in product(range(5),repeat=6) if sum(p)==5]
assert len(profiles)==246
pairs = list(combinations(range(6),2))

def conditional(p, allblue):
    blue, red = Q(1), Q(1)
    for i,n in enumerate(p):
        if i in allblue:
            if n:
                red = Q(0)
        else:
            blue *= Q(1,4) if n==1 else int(n==0)
            red *= Q(4-n,4)
    return blue+red

def balanced(p):
    ans=Q(2)
    for n in p:
        ans *= Q(comb(4-n,2-n),6) if n<=2 else 0
    return ans

def scaled(q, d):
    val=q*d
    assert val.denominator==1
    return val.numerator

fixed = [[scaled(conditional(p,pair),256) for p in profiles] for pair in pairs]
B = [scaled(balanced(p),46656) for p in profiles]
C = [scaled(sum((conditional(p,(i,)) for i in range(6)),Q(0))/6,6144)
     for p in profiles]
rows = [[1]*len(profiles)]
lower, upper = [29], [29]
for i in range(6):
    rows.append([p[i] for p in profiles]);lower.append(20);upper.append(np.inf)
for i,j in pairs:
    rows.append([p[i]*p[j] for p in profiles]);lower.append(16);upper.append(np.inf)
for row in fixed:
    rows.append(row);lower.append(256);upper.append(np.inf)
for row,denom in ((B,46656),(C,6144)):
    rows.append(row);lower.append(denom);upper.append(np.inf)
assert len(rows)==39
with warnings.catch_warnings(record=True) as warning_log:
    sol = milp(np.zeros(len(profiles)),integrality=np.ones(len(profiles)),
               bounds=Bounds(np.zeros(len(profiles)),np.full(len(profiles),29)),
               constraints=LinearConstraint(np.asarray(rows,dtype=float),lower,upper),
               options={'time_limit':50,'threads':1,'presolve':True,'mip_rel_gap':0.0})
result=dict(scope='one necessary six-block count MILP; not original-H enumeration',
            profiles=246, integer_variables=246,linear_rows=39,
            numerical_status=int(sol.status), numerical_message=str(sol.message),
            solver_warnings=[str(w.message) for w in warning_log],
            budget_cpu_seconds=60,solver_time_limit_seconds=50,threads_requested=1,
            whole_twentyfive_claim=False)
if sol.x is not None:
    x=[int(round(v)) for v in sol.x]
    integral=all(abs(v-w)<1e-6 for v,w in zip(sol.x,x))
    actual=[sum(v*n for v,n in zip(row,x)) for row in rows]
    exact=integral and all(v>=lo and (not np.isfinite(hi) or v<=hi)
                           for v,lo,hi in zip(actual,lower,upper))
    result['exact_integer_readback']=exact
    if exact:
        W=sum(n*sum(comb(a,2) for a in p) for p,n in zip(profiles,x))
        assert W<=50
        result.update(verdict='FEASIBLE_WITH_EXACT_RECEIPT',
                      nonzero=[dict(occupancy=list(p),count=n) for p,n in zip(profiles,x) if n],
                      total=sum(x),W=W,
                      column_incidence=actual[1:7],block_pair_cross_incidence=actual[7:22],
                      fixed_A_bounds=[dict(full_blue_blocks=list(pair),bound=str(Q(v,256)))
                                      for pair,v in zip(pairs,actual[22:37])],
                      B_bound=str(Q(actual[37],46656)),C_bound=str(Q(actual[38],6144)),
                      A_average_bound=str(sum((Q(v,256) for v in actual[22:37]),Q(0))/15),
                      minimum_fixed_A_bound=str(min(Q(v,256) for v in actual[22:37])),
                      all_exact_integer_rows=[dict(lhs=v,lower=int(lo),
                                                   upper=None if not np.isfinite(hi) else int(hi))
                                              for v,lo,hi in zip(actual,lower,upper)])
    else:
        result['verdict']='NUMERICAL_VECTOR_FAILED_EXACT_READBACK'
else:
    result['verdict']='NUMERICAL_ONLY_NO_EXACT_INFEASIBILITY_CERTIFICATE'
result.update(cpu_seconds=process_time()-start,wall_seconds=monotonic()-wall)
(P/'MILP_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('verdict','numerical_status','cpu_seconds','wall_seconds')}))
