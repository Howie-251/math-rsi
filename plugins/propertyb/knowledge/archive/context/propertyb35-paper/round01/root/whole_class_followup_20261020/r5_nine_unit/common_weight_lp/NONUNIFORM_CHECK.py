"""Shared original-edge LP for the FIVE nonuniform row8 Y graphs with w<=3.
Use the newly actual-proved q_xy<=1 for every w_xy=3 pair.
No new graph enumeration, layout search, MILP or H search.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json,sys,time
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
base=json.loads((P/'RESULT.json').read_text())
old=json.loads((P.parent/'K5_EXCEPTION_RESULT.json').read_text())['integer_Y_graphs']
edges=list(combinations(range(5),2));types=[tuple(t) for t in base['all_types']]
A=base['integer_matrix_rows'];names=[z['name'] for z in base['constraint_receipts']]
graphs=[z for z in old['all_representatives'] if max(z['w'])<=3]
assert len(graphs)==6 and sum(all(w==2 for w in z['w']) for z in graphs)==1
graphs=sorted([z for z in graphs if not all(w==2 for w in z['w'])],key=lambda z:(z['sum_cost'],z['w']))
start=time.process_time();results=[]
for g in graphs[:1] if 'profile' in sys.argv else graphs:
    tm=time.process_time();weights=dict(zip(edges,g['w']));b=list(base['integer_rhs'])
    assert [sum(w for (i,j),w in weights.items() if v in (i,j)) for v in range(5)]==[8]*5
    for k,name in enumerate(names):
        for (i,j),w in weights.items():
            if name==f'Y{i}_Y{j}_pair_incidence':b[k]=1+w
    costs=[ell*(comb(a,2)+comb(bb,2)+comb(c,2)+sum(w for (i,j),w in weights.items() if mask>>i&1 and mask>>j&1)) for ell,a,bb,c,mask in types]
    high_pairs=[e for e,w in weights.items() if w==3]
    C=[[ell*int(mask>>i&1 and mask>>j&1) for ell,a,bb,c,mask in types] for i,j in high_pairs]
    d=[1]*len(C)
    r=linprog(-np.asarray(costs,dtype=float),A_eq=np.asarray(A,dtype=float),b_eq=np.asarray(b,dtype=float),
              A_ub=np.asarray(C,dtype=float),b_ub=np.asarray(d,dtype=float),bounds=(0,None),method='highs')
    rec={'Y_edge_order':edges,'w':g['w'],'high_pairs_q_cap1':high_pairs,'solver_status':int(r.status),'message':r.message}
    if not r.success:
        # One common nonnegative violation v supplies an explicit rational
        # Farkas certificate, rather than trusting a float infeasible status.
        ae=np.column_stack((np.asarray(A,dtype=float),np.zeros(len(A))))
        cu=np.column_stack((np.asarray(C,dtype=float),-np.ones(len(C))))
        phase=linprog(np.array([0.0]*len(types)+[1.0]),A_eq=ae,b_eq=np.asarray(b,dtype=float),
                      A_ub=cu,b_ub=np.asarray(d,dtype=float),bounds=(0,None),method='highs')
        assert phase.success and phase.fun>1e-8
        h=[Q(-float(v)).limit_denominator(1000000) for v in phase.eqlin.marginals]
        k=[Q(-float(v)).limit_denominator(1000000) for v in phase.ineqlin.marginals]
        assert min(k)>=0
        coeff=[sum((Q(A[i][j])*h[i] for i in range(len(A))),Q())+sum((Q(C[i][j])*k[i] for i in range(len(C))),Q()) for j in range(len(types))]
        contradiction=sum((v*q for v,q in zip(b,h)),Q())+sum((v*q for v,q in zip(d,k)),Q())
        assert min(coeff)>=0 and contradiction<0
        rec.update(excluded_by_exact_Farkas=True,exact_farkas_rhs=str(contradiction),exact_farkas_minimum_coefficient=str(min(coeff)),
                   exact_equality_dual=[{'name':n,'rhs':rhs,'coefficient':str(q)} for n,rhs,q in zip(names,b,h) if q],
                   exact_inequality_dual=[{'Y_pair':e,'rhs':rhs,'coefficient':str(q)} for e,rhs,q in zip(high_pairs,d,k) if q],
                   equality_rhs=b,inequality_matrix=C,inequality_rhs=d,integer_objective=costs,
                   conclusion='Exact Farkas sum has all512 variable coefficients nonnegative and strictly negative RHS; necessary domain impossible.')
    else:
        x=[Q(float(v)).limit_denominator(1000000) if v>1e-9 else Q(0) for v in r.x]
        y=[Q(-float(v)).limit_denominator(1000000) for v in r.eqlin.marginals]
        z=[Q(-float(v)).limit_denominator(1000000) for v in r.ineqlin.marginals]
        assert min(x)>=0 and min(z)>=0
        assert [sum((Q(v)*q for v,q in zip(row,x)),Q()) for row in A]==list(map(Q,b))
        primal_ub=[sum((Q(v)*q for v,q in zip(row,x)),Q()) for row in C]
        assert all(u<=v for u,v in zip(primal_ub,d))
        slack=[sum((Q(A[i][k])*y[i] for i in range(len(A))),Q())+sum((Q(C[i][k])*z[i] for i in range(len(C))),Q())-costs[k] for k in range(len(types))]
        assert min(slack)>=0
        primal=sum((Q(v)*q for v,q in zip(costs,x)),Q())
        upper=sum((v*q for v,q in zip(b,y)),Q())+sum((v*q for v,q in zip(d,z)),Q())
        assert primal==upper
        rec.update(exact_primal_feasible=True,exact_dual_feasible=True,exact_optimum=str(upper),strict_below130=upper<130,
                   primal_support=[{'type':t,'weight':str(q)} for t,q in zip(types,x) if q],
                   exact_equality_dual=[{'name':n,'rhs':rhs,'coefficient':str(q)} for n,rhs,q in zip(names,b,y) if q],
                   exact_inequality_dual=[{'Y_pair':e,'rhs':rhs,'coefficient':str(q)} for e,rhs,q in zip(high_pairs,d,z) if q],
                   equality_rhs=b,inequality_matrix=C,inequality_rhs=d,integer_objective=costs,
                   dual_minimum_slack=str(min(slack)),all_primal_q_values=[str(v) for v in primal_ub])
    rec['CPU_seconds']=time.process_time()-tm;results.append(rec)
out={'scope':__doc__,'uniform_already_proved_analytically':True,'complete_nonuniform_row8_wcap3_domain':len(results)==5,
     'graph_representatives':len(results),'all_exact_strict':len(results)==5 and all(z.get('strict_below130',False) or z.get('excluded_by_exact_Farkas',False) for z in results),
     'CPU_seconds':time.process_time()-start,'records':results}
(P/('NONUNIFORM_PROFILE.json' if 'profile' in sys.argv else 'NONUNIFORM_RESULT.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
print([(z['w'],z.get('exact_optimum'),z.get('strict_below130')) for z in results])
