"""Only cached named formulas at cap17; no network, graph, source test, or solver."""
import time
START=time.process_time()
import json,math,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
D=Path(__file__).resolve().parent
assert not (D/'CACHED_DEGREE17_SCALAR.json').exists(), 'Single scalar batch already completed.'
CAP=17
prime=lambda n:n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
 if n<2:return False
 for p in range(2,n+1):
  if not prime(p):continue
  z=p
  while z<n:z*=p
  if z==n:return True
 return False
def best(rows):return max(rows,key=lambda z:z['n']) if rows else None
Q=[q for q in range(2,CAP) if pp(q)]
IQ=[];PAL=[];FOLD=[];DUAL=[];PRODUCT=[];OPP=[]
for q in Q:
 for d in range(CAP-q):
  if d%4 in (0,3):IQ.append(dict(q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+2)))
  if d%2==0 and pp(2*d+1):PAL.append(dict(q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+1)))
for exponent in range(1,5):
 q=2**exponent
 if exponent%2==1 and q+1<=CAP:FOLD.append(dict(q=q,source_degree=q+1,n=CAP*(q*q+1)))
 if 3*(q+1)<=CAP:DUAL.append(dict(q=q,source_degree=3*(q+1),n=4*CAP*(q*q+1)))
for q in [1,2,8]:
 for r in [1,2,8]:
  delta=(q+1)*(r+1)
  if delta<=CAP:PRODUCT.append(dict(type='GQpolarities',q=q,r=r,degree=delta,n=CAP*(q*q+1)*(r*r+1)))
 for r in [1]+Q:
  delta=(q+1)*(r+1)
  if delta<=CAP:
   base=(q+1)*(q*q+1)*(r*r+r+1);code=(q*q+1)*(r+1)
   PRODUCT.append(dict(type='GQpolarity_projectiveTriangle',q=q,r=r,degree=delta,n=base+(CAP-delta)*code))
# Generous upper envelope, NOT an existence/lower-bound assertion: allow
# every integer (s,t), full ovoid/spread and even the unresolved source fill.
for s in range(1,CAP):
 for t in range(s,CAP):
  delta=(s+1)*(t+1)
  if delta<=CAP:
   R=s*t+1
   OPP.append(dict(s=s,t=t,degree=delta,R=R,n=CAP*R*R+R,role='optimistic_fullO_spread_plus_fill_upper_not_public_guarantee'))
maxima=dict(PolarStarIQ=best(IQ),PolarStarPaley=best(PAL),Delorme_folded_replication=best(FOLD),Delorme_standard12_duality_replication=best(DUAL),Isham_composed_polarity_replication=best(PRODUCT),oppositeGQ_optimistic_upper=best(OPP))
result=dict(status='NO_CHECKED_CACHED_FAMILY_MEETS2016_GLOBAL17_THRESHOLD_STILL_UNKNOWN',Delta=17,candidate_order=2016,category_maxima=maxima,
 actual_Mizuno_monotone_guarantee=1920,best_located_guarantee_including_Mizuno=1920,all_category_maxima_below2016=all(z['n']<2016 for z in maxima.values()),
 no_named_cached_blocker=True,no_global_exhaustion_claim=True,current17_table_row=None,
 inputs=['public_baseline_audit/DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101.py (formulas read, not executed)',
 'public_baseline_audit/polarstar2024_primary_text.txt (cached primary)', 'public_baseline_audit/arxiv_2608_27253v2.txt (cached primary)'],
 exact_priority='UNKNOWN',new_queries=0,graph_BFS_field_rank_MIP_Lean_paidreview_runs=0,scalar_CPU_seconds=time.process_time()-START,CPU_budget_seconds=5)
(D/'CACHED_DEGREE17_SCALAR.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
