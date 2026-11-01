"""Diagnostic only: integer negative-type budget for eight positive four-sets and max positive occurrence3."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
HERE=Path(__file__).parent

def main():
    start=time.time();out=[]
    p=[Q(0),Q(1,4),Q(7,16),Q(37,64)]
    for h in range(1,5):
      for z in range(4):
        ns=[z,h+2*z+2,15-2*h-3*z,h]
        if min(ns)<0:continue
        cs=[];val=[]
        for size in (3,4):
          for t in product(*(range(min(size,n)+1) for n in ns)):
            if sum(t)!=size:continue
            cs.append(t);q=Q(1)
            for j in range(4):q*=p[j]**t[j]
            val.append(q)
        mat=np.array([[int(sum(t)==s) for t in cs] for s in (3,4)]+[[t[j] for t in cs] for j in range(4)],dtype=float)
        cap=[(7-j)*ns[j] for j in range(4)]
        lower=[3,18]+[max(0,a-6) for a in cap];upper=[3,18]+cap
        res=milp(-np.array([float(q) for q in val]),integrality=np.ones(len(cs)),bounds=Bounds(0,np.inf),constraints=LinearConstraint(mat,lower,upper),options={'time_limit':10})
        assert res.success,res.message
        x=[round(t) for t in res.x];usage=[sum(t[j]*a for t,a in zip(cs,x)) for j in range(4)]
        assert sum(a for t,a in zip(cs,x) if sum(t)==3)==3
        assert sum(a for t,a in zip(cs,x) if sum(t)==4)==18
        assert all(max(0,c-6)<=u<=c for c,u in zip(cap,usage))
        exact=sum((q*a for q,a in zip(val,x)),Q())
        out.append(dict(positive_type_counts=ns,negative_capacities=cap,negative_usage=usage,value=str(exact),less_than_one=exact<1,compositions=[dict(type=t,count=a,product=str(q)) for t,a,q in zip(cs,x,val) if a],solver_optimal_status=int(res.status)))
    result=dict(scope=__doc__,status='DIAGNOSTIC_NOT_AN_EXACT_OPTIMALITY_CERTIFICATE',profiles=out,elapsed_seconds=time.time()-start)
    (HERE/'SELECTOR_BUDGET_PILOT.json').write_text(json.dumps(result,indent=2)+'\n')
    for r in out:print(r['positive_type_counts'],r['value'],r['less_than_one'])
if __name__=='__main__':main()
