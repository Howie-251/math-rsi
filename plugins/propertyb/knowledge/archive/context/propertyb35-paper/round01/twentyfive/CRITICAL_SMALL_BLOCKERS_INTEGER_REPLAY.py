"""Independent standard-library exact replay of count witnesses and small-set identities.
No LP/model/construction source is imported. Count witnesses are not actual H.
"""
from pathlib import Path
from itertools import combinations
from math import comb
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def verify(w):
 n,M,D,a,b=(w[k] for k in ['n','M','DG','a','b']);support=[(z['r'],z['s'],z['t'],Q(z['N'])) for z in w['support']]
 assert a+b==n-5 and all(r+s+t==5 and 0<=r<=4 and 0<=s<=a and 1<=t<=min(4,b) and v>0 for r,s,t,v in support)
 def S(f):return sum(v*f(r,s,t) for r,s,t,v in support)
 assert S(lambda r,s,t:1)==M-1 and S(lambda r,s,t:r)==D-5
 checks={'degree_red':(S(lambda r,s,t:s),7*a),'degree_blue':(S(lambda r,s,t:t),7*b),'G_red':(S(lambda r,s,t:r*s),5*a),'G_blue':(S(lambda r,s,t:r*t),5*b),'red_red':(S(lambda r,s,t:C(s,2)),C(a,2)),'red_blue':(S(lambda r,s,t:s*t),a*b),'blue_blue':(S(lambda r,s,t:C(t,2)),C(b,2))}
 for label,idx,k in [('G',0,5),('red',1,a),('blue',2,b)]:
  checks['even_cut_'+label]=(S(lambda r,s,t:(r,s,t)[idx]*(5-(r,s,t)[idx])),2*((k*(n-k)+1)//2))
 c=S(lambda r,s,t:int((r,s,t)==(1,0,4)))
 for j in range(b+1):checks['action_'+str(j)]=(c*C(b-4,j)+S(lambda r,s,t:(5-r)*C(b-t,j-t)),5*C(b,j))
 if b-(5+a)>=2:checks['balance']=(S(lambda r,s,t:int(t==1)),b)
 if (5+a)-b>=2:checks['balance']=(S(lambda r,s,t:int((r,s,t)==(0,1,4))),a)
 assert all(x>=y for x,y in checks.values())
 return dict(n=n,M=M,DG=D,a=a,b=b,c=str(c),t1=str(S(lambda r,s,t:int(t==1))),checks={k:dict(lhs=str(x),rhs=str(y),slack=str(x-y)) for k,(x,y) in checks.items()})
old=json.loads((P/'CRITICAL_SMALL_BLOCKERS_INTEGER_RELAXATION.json').read_text());out=[dict(source='INTEGER_RELAXATION',**verify(old))]
rat=json.loads((P/'CRITICAL_SMALL_BLOCKERS_ACTION_PARITY_LP.json').read_text())['exact_relaxation_witness'];out.append(dict(source='ACTION_PARITY_LP',**verify(rat)))
branches=json.loads((P/'CRITICAL_SMALL_BLOCKERS_CENTER_BRANCH.json').read_text())['results']
for row in branches:
 if row.get('exact_passed'):
  w=dict(n=24,M=34,DG=35,**row);rr=verify(w)
  assert Q(rr['c'])>=10 if row['branch']=='many_positive' else Q(rr['c'])<=9 and Q(rr['t1'])>=4
  out.append(dict(source='CENTER_BRANCH_'+row['branch'],**rr))
# Independent characterization of minimal free transversals of two four-sets.
patterns=0
for intersection in range(5):
 A=set(range(4));B=set(range(intersection))|set(range(4,8-intersection));U=A|B;uu=sorted(U)
 for bits in range(1<<len(uu)):
  F={v for j,v in enumerate(uu) if bits>>j&1};AA=A-F;BB=B-F;free=U-F
  candidates=[frozenset(z) for k in [1,2] for z in combinations(sorted(free),k) if set(z)&AA and set(z)&BB]
  actual={z for z in candidates if not any(w<z for w in candidates)}
  predicted={frozenset([v]) for v in AA&BB}|{frozenset([x,y]) for x in AA-BB for y in BB-AA}
  assert actual==predicted
  if not AA or not BB:assert not actual
  elif AA&BB:assert any(len(z)==1 for z in actual)
  else:assert actual=={frozenset([x,y]) for x in AA for y in BB}
  patterns+=1
# Parameterized k-uniform local cost comparison, followed by the k=5 costs.
general_local_cases=0
for edge_size in range(2,11):
 for blue_size in range(1,edge_size):
  for epsilon in [0,1]:
   h=edge_size-blue_size-epsilon
   assert h*(h-1)+h*epsilon >= (edge_size-blue_size-1)**2
   general_local_cases+=1
# The a=1, n=24 common-row blocker budget: exact local coefficients.
coefficients={}
for t in [1,2,3]:
 values=[k*(k-1)+k*ss for k in range(5) for ss in [0,1] if k+ss==5-t]
 coefficients[t]=min(values)
assert coefficients=={1:9,2:4,3:1}
assert (28-9*3)//4==0 and 28-9*3==1 and 3*(3-1)>5
q_costs=[9*q+4*(4-q)**2 for q in range(4)]
assert q_costs==[64,45,34,31] and min(q_costs)>28
result=dict(passed=True,scope=__doc__,parameterized_cost_cases=general_local_cases,one_red_exterior_coefficients=coefficients,one_red_exterior_q_costs=q_costs,count_witnesses=len(out),witnesses=out,canonical_two_positive_singleton_deletion_patterns=patterns,elapsed_seconds=time.perf_counter()-st)
(P/'CRITICAL_SMALL_BLOCKERS_INTEGER_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='witnesses'},indent=2))
