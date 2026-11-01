"""One shared original-edge-type LP for the r5 three-K5 exception.
Only uniform Y excess w=2; continuous necessary relaxation, not an H search.
The objective pays ell=2 twice. Rational primal receipts checked exactly.
"""
from pathlib import Path
from itertools import combinations
from math import comb
from fractions import Fraction as Q
import json,time
import numpy as np
from scipy.optimize import linprog

P=Path(__file__).resolve().parent
start=time.process_time()
types=[]
for ell in range(3):
    for mask in range(32):
        j=mask.bit_count();m=5-ell-j
        if m<0:continue
        for a in range(m+1):
            for b in range(m-a+1):
                c=m-a-b
                types.append((ell,a,b,c,mask))
assert len(types)==512
names=[];A=[];B=[]
def add(name,fun,rhs):
    names.append(name);A.append([fun(t) for t in types]);B.append(rhs)
for ell,n in enumerate([15,10,10]):
    add(f'edge_low_count_{ell}',lambda t,e=ell:int(t[0]==e),n)
for g in range(3):
    add(f'G{g}_degree_total',lambda t,g=g:t[g+1],35)
for y in range(5):
    add(f'Y{y}_degree',lambda t,y=y:int(t[4]>>y&1),8)
for g in range(3):
    add(f'G{g}_internal_pair_incidence',lambda t,g=g:comb(t[g+1],2),20)
for g,h in combinations(range(3),2):
    add(f'G{g}_G{h}_cross_pair_incidence',lambda t,g=g,h=h:t[g+1]*t[h+1],25)
for g in range(3):
    for y in range(5):
        add(f'G{g}_Y{y}_cross_pair_incidence',lambda t,g=g,y=y:t[g+1]*int(t[4]>>y&1),5)
for y,z in combinations(range(5),2):
    add(f'Y{y}_Y{z}_pair_incidence',lambda t,y=y,z=z:int(t[4]>>y&1 and t[4]>>z&1),3)
for g in range(3):
    add(f'low_G{g}_pair_incidence',lambda t,g=g:t[0]*t[g+1],25)
for y in range(5):
    add(f'low_Y{y}_pair_incidence',lambda t,y=y:t[0]*int(t[4]>>y&1),5)
cost=[ell*(comb(a,2)+comb(b,2)+comb(c,2)+2*comb(mask.bit_count(),2)) for ell,a,b,c,mask in types]
assert len(names)==50
sol=linprog(-np.array(cost,dtype=float),A_eq=np.array(A,dtype=float),b_eq=np.array(B,dtype=float),bounds=(0,None),method='highs')
out={'scope':__doc__,'uniform_Y_w':2,'edge_types':len(types),'equality_constraints':len(names),'simple_edge_capacities_added':False,
     'solver_status':sol.status,'solver_message':sol.message,'success':bool(sol.success),'solver':'scipy.optimize.linprog(method=highs)',
     'CPU_seconds':time.process_time()-start}
if sol.success:
    xx=[Q(float(x)).limit_denominator(1000000) if x>1e-9 else Q(0) for x in sol.x]
    exact=[sum((Q(a)*x for a,x in zip(row,xx)),Q()) for row in A]
    assert exact==[Q(b) for b in B]
    assert min(xx)>=0
    obj=sum((Q(c)*x for c,x in zip(cost,xx)),Q())
    assert abs(float(obj)+sol.fun)<1e-7
    out.update(exact_primal_feasible=True,objective_exact=str(obj),objective_float=-sol.fun,
       support=[{'ell':t[0],'a':t[1],'b':t[2],'c':t[3],'Y_mask':t[4],'Y_subset':[y for y in range(5) if t[4]>>y&1],
                 'weight':str(x),'objective_coefficient':cc} for t,x,cc in zip(types,xx,cost) if x],
       constraint_receipts=[{'name':n,'rhs':b,'exact_lhs':str(v),'float_residual':float(r)} for n,b,v,r in zip(names,B,exact,sol.eqlin.residual)],
       floating_dual=[{'name':n,'marginal_for_min_negative_objective':float(v)} for n,v in zip(names,sol.eqlin.marginals)],
       zero_variable_count=sum(not x for x in xx),positive_variable_count=sum(bool(x) for x in xx),
       all_primal_weights_integer=all(x.denominator==1 for x in xx))
    # No optimization claim is based on this reconstruction alone. Check a
    # candidate dual exactly when HiGHS returns small rational multipliers.
    yy=[Q(-float(x)).limit_denominator(1000000) for x in sol.eqlin.marginals]
    slacks=[sum((Q(A[i][j])*yy[i] for i in range(len(B))),Q())-cost[j] for j in range(len(types))]
    dual_obj=sum((y*b for y,b in zip(yy,B)),Q())
    out['exact_dual']={'feasible':min(slacks)>=0,'objective':str(dual_obj),'minimum_slack':str(min(slacks)),
       'terms':[{'name':n,'coefficient':str(y),'rhs':b} for n,y,b in zip(names,yy,B) if y]}
    if min(slacks)>=0 and dual_obj==obj:out['exact_LP_optimum_certified']=True
    if obj>=130:
        out['conclusion']='This necessary shared-edge relaxation cannot force S<130, even at uniform Y weights. Stop before other17 Y spectra.'
    else:
        out['conclusion']='Candidate S<130 bound requires exact feasible dual before theorem use.'
    # Store the complete finite input as well, not only solver log/support.
    out['all_types']=[list(t) for t in types]
    out['integer_matrix_rows']=A;out['integer_rhs']=B;out['integer_objective']=cost
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['support','constraint_receipts','floating_dual','all_types','integer_matrix_rows','integer_rhs','integer_objective']},indent=2))
if sol.success:print('support',json.dumps(out['support'],indent=2))
