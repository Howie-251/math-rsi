"""Bounded budget profile on the old remaining E7 cores; no new positive domain.
Uniform minimal-C4 candidate only. Stops at first nonstrict relaxation; does not
call a nonstrict probability bound a counterexample.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json,time
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent;start=time.process_time();rows=[]
old=json.load(open(P/'OLD_CORE_SCALAR_PROFILE.json'))['residual']
for idx,r in enumerate(old):
 if idx in (0,1,7):continue # two isolates and common-point case separately analytic
 A=[set(B) for B in r['sets']];U=sorted(set.union(*A));N=len(U)
 C3=[frozenset(R) for R in combinations(U,3) if all(set(R)&B for B in A)]
 C4=[frozenset(R) for R in combinations(U,4) if all(set(R)&B for B in A) and not any(S<=set(R) for S in C3)]
 targets=[(k,frozenset(Fset)) for k in (3,4) for Fset in combinations(U,k) if any(set(Fset)<=R for R in C4)]
 budgets=[15-len(C3),27-len(C3)]+[7-sum(v in B for B in A)-sum(v in S for S in C3) for v in U]
 assert min(budgets)>=0
 mat=np.array([[int(k==3),1]+[int(v in S) for v in U] for k,S in targets],dtype=float).T
 probs=[F(sum(S<=R for R in C4),len(C4)) for k,S in targets]
 sol=linprog(-np.array(list(map(float,probs))),A_ub=mat,b_ub=budgets,bounds=(0,1),method='highs')
 record={'old_residual_index':idx,'old_vector':r['old_vector'],'sets':r['sets'],'C3':len(C3),'minimal_C4':len(C4),'targets':len(targets),'budgets':budgets,'solver_status':sol.status,'uniform_coverage_max':None if sol.fun is None else -sol.fun}
 if sol.status!=0:record['status']='NO_CONCLUSION';rows.append(record);break
 beta=[F(max(0,-x)).limit_denominator(1000000) for x in sol.ineqlin.marginals]
 gamma=[F(max(0,-x)).limit_denominator(1000000) for x in sol.upper.marginals]
 repair=F(0)
 for (k,S),q,ga in zip(targets,probs,gamma):
  rhs=beta[0]*int(k==3)+beta[1]+sum(beta[2+i] for i,v in enumerate(U) if v in S)+ga
  repair=max(repair,q-rhs)
 beta[1]+=repair
 cost=sum(b*v for b,v in zip(beta,budgets))+sum(gamma)
 assert all(q<=beta[0]*int(k==3)+beta[1]+sum(beta[2+i] for i,v in enumerate(U) if v in S)+ga for (k,S),q,ga in zip(targets,probs,gamma))
 record.update({'exact_cost':str(cost),'beta':list(map(str,beta)),'upper_weights':[{'size':k,'target':sorted(S),'weight':str(ga)} for (k,S),ga in zip(targets,gamma) if ga],'status':'STRICT_FIXED_UNIFORM_CERTIFICATE' if cost<1 else 'NONSTRICT_RELAXATION_ONLY'})
 rows.append(record)
 if cost>=1:break
out={'scope':__doc__,'rows':rows,'checked':len(rows),'all_processed_strict':all(r['status']=='STRICT_FIXED_UNIFORM_CERTIFICATE' for r in rows),'completed_all_twelve':len(rows)==12,'cpu_seconds':time.process_time()-start}
(P/'RESIDUAL_UNIFORM_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2));print([(r['old_residual_index'],r.get('exact_cost')) for r in rows])
