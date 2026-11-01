"""Independent short-dual/slack check, then ONE integer aggregate face pilot.
Not an original-H search: G vertices and five low identities remain aggregated.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from collections import defaultdict
import json,time
import numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds

P=Path(__file__).resolve().parent;R=json.loads((P/'RESULT.json').read_text())
start=time.process_time();types=[tuple(t) for t in R['all_types']]
A=R['integer_matrix_rows'];b=R['integer_rhs'];cost=R['integer_objective']
slacks=[];orbits={}
for ell,a,bb,c,mask in types:
    j=mask.bit_count();U=comb(a,2)+comb(bb,2)+comb(c,2)
    gap=U+j*(j+ell-2)+3*int(ell==2)-ell*(U+j*(j-1))
    assert gap>=0
    slacks.append(gap)
    orbits[(ell,j,tuple(sorted((a,bb,c),reverse=True)))]=gap
# Direct exact check of the rational primal against the saved INTEGER system.
idx={t:i for i,t in enumerate(types)};x=[Q(0) for t in types]
for z in R['support']:
    x[idx[(z['ell'],z['a'],z['b'],z['c'],z['Y_mask'])]]=Q(z['weight'])
assert [sum((v*w for v,w in zip(row,x)),Q()) for row in A]==list(map(Q,b))
assert sum((v*w for v,w in zip(cost,x)),Q())==135
assert sum((v*w for v,w in zip(slacks,x)),Q())==0
# Independently check a simple fully symmetric rational witness, eight orbit
# totals, uniform among every labeled type in each orbit.
totals={(0,1,(2,1,1)):9,(0,2,(1,1,1)):6,
        (1,0,(4,0,0)):2,(1,0,(3,1,0)):4,
        (1,1,(3,0,0)):1,(1,4,(0,0,0)):3,
        (2,0,(3,0,0)):8,(2,3,(0,0,0)):2}
groups=defaultdict(list)
for i,(ell,a,bb,c,mask) in enumerate(types):groups[(ell,mask.bit_count(),tuple(sorted((a,bb,c),reverse=True)))].append(i)
sx=[Q(0) for t in types]
for key,total in totals.items():
    for i in groups[key]:sx[i]=Q(total,len(groups[key]))
assert [sum((v*w for v,w in zip(row,sx)),Q()) for row in A]==list(map(Q,b))
assert sum((v*w for v,w in zip(cost,sx)),Q())==135

# S>=130 implies total gap<=5. Four zero-gap F2 classes each at most2
# (their three high points are inside a fixed five-set), so all four exactly2.
zero_classes=[]
for g in range(3):
    zero_classes.append([int(t[0]==2 and t[g+1]==3) for t in types])
zero_classes.append([int(t[0]==2 and t[4].bit_count()==3) for t in types])
AA=A+zero_classes+[slacks]
lb=b+[2]*4+[-np.inf];ub=b+[2]*4+[5]
result=milp(-np.asarray(cost,dtype=float),integrality=np.ones(len(types)),bounds=Bounds(np.zeros(len(types)),np.full(len(types),np.inf)),
    constraints=LinearConstraint(np.asarray(AA,dtype=float),np.asarray(lb,dtype=float),np.asarray(ub,dtype=float)),
    options={'time_limit':10,'mip_rel_gap':0})
out={'scope':__doc__,'pointwise_short_dual_all512_checked':True,'first_LP_exact_primal_and_upper135_checked':True,
     'symmetric_rational_witness_orbit_totals':[{'ell':key[0],'Y_size':key[1],'G_sizes':key[2],'total':n} for key,n in totals.items()],
     'slack_orbits':[{'ell':key[0],'Y_size':key[1],'G_sizes':key[2],'slack':v} for key,v in sorted(orbits.items())],
     'actual_uniform_Y_bound_from_four_matching_classes':131,'integer_face_solver_status':int(result.status),
     'integer_face_solver_message':result.message,'integer_face_success':bool(result.success),'CPU_seconds':time.process_time()-start}
if result.x is not None:
    xx=[round(v) for v in result.x]
    assert max(abs(v-w) for v,w in zip(result.x,xx))<1e-6
    assert min(xx)>=0
    assert [sum(v*w for v,w in zip(row,xx)) for row in A]==b
    assert [sum(v*w for v,w in zip(row,xx)) for row in zero_classes]==[2]*4
    gap=sum(v*w for v,w in zip(slacks,xx));objective=sum(v*w for v,w in zip(cost,xx))
    assert gap<=5 and objective==135-gap>=130
    out.update(exact_integer_primal_feasible=True,integer_objective=objective,total_slack=gap,
       objective_by_low_count={str(e):sum(cost[i]*xx[i] for i,t in enumerate(types) if t[0]==e) for e in range(3)},
       positive_types=[{'ell':t[0],'a':t[1],'b':t[2],'c':t[3],'Y_mask':t[4],'weight':n,'slack':slacks[i]} for i,(t,n) in enumerate(zip(types,xx)) if n],
       equality_receipts=[{'name':name,'rhs':rhs,'exact_lhs':sum(v*w for v,w in zip(row,xx))} for name,rhs,row in zip([z['name'] for z in R['constraint_receipts']],b,A)],
       conclusion='Integer shared type budgets plus four actual F2 matching-class caps still admit S>=130; not an H construction.')
else:
    out['conclusion']='No integer witness returned within this one bounded pilot; no exact infeasibility claim.'
(P/'FACE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['slack_orbits','positive_types','equality_receipts']},indent=2))
if result.x is not None:print('positive_types',json.dumps(out['positive_types'],indent=2))
