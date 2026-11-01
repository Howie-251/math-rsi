"""Nine-type exact certificate for v34, minimum degree eleven."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import importlib.util
import json
import signal
import time
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
START=time.process_time()
spec=importlib.util.spec_from_file_location('independent_component_injection',BASE/'independent31_33/check.py')
a=importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)  # guarded main does not run
signal.setitimer(signal.ITIMER_PROF,45)
signal.alarm(120)
used_quotas=set()


def deletion(v,slots,ell,j):
    """Maximum of individual avoided-subfamily quota costs; never their sum."""
    types=[t for t in ell if t>>j&1]
    cells=[]
    for index,t in enumerate(types):
        for u in types[index:]:
            cap=comb(ell[t],2) if t==u else ell[t]*ell[u]
            if cap:
                weight=a.prob(v,slots,slots[j],t,u)+a.prob(v,slots,slots[j],u,t)
                cells.append((weight,cap,t|u))
    costs=[]
    for R in range(1<<len(slots)):
        if R>>j&1:
            continue
        f=sum(n for t,n in ell.items() if t>>j&1 and not t&R)
        N=v-1-R.bit_count()
        need=a.quota(f,N)
        used_quotas.add((f,N,need))
        cost=Q(0)
        for w,cap,union in sorted(cells):
            if not union&R:
                take=min(cap,need)
                cost+=take*w
                need-=take
        assert need==0
        costs.append(cost)
    return max(costs)


a.deletion=deletion


def main():
    rows=[]
    def add(kind,degrees,ell,pos,**params):
        assert min(ell.values())>=0 and sum(ell.values())==66
        assert all(sum(n for t,n in ell.items() if t>>j&1)==d for j,d in enumerate(degrees))
        value=a.bound(34,pos,ell)
        assert value<1,(kind,params,value)
        rows.append(dict(kind=kind,degrees=degrees,ell=ell,positions=pos,U=str(value),strict=True,**params))
    add('unit_pair',[11,11],a.two(11,11,1),[17,18])
    for center in (12,13):
        for tau in (0,1):
            add('low_center_wedge',[center,11,11],a.triple((center,11,11),2,tau),[16,17,18],endpoint_codegree=2,tau=tau)
    for tau in range(4):
        ell={7:tau,3:3-tau,5:3-tau,6:3-tau,9:1,10:1,12:1,1:4+tau,2:4+tau,4:4+tau,8:9}
        ell[0]=66-sum(ell.values())
        ell={t:n for t,n in ell.items() if n}
        add('rigid_special_four',[11,11,11,12],ell,[16,17,19,18],tau=tau)
    assert len(rows)==9
    # Independent short integer check of the analytic cardinality conclusion.
    relaxed=[]
    for r in range(12,35):
        b=34-r
        for c in range(b+1):
            aa=b-c
            if aa>0 and aa+3*c<=22 and b>=11 and b-10>=r:
                relaxed.append((r,aa,c))
    assert relaxed==[(12,22,0)]
    result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',
                scope='v34, exactly66 edges, paircover, minimum degree11: complete nine-type local certificate',
                probability_method='Pre-existing independent falling-factorial uniform-injection kernel',
                quota_method='Independently reconstructed component quota; maximum of single-R cheapest-cell deductions',
                profiles=len(rows),maximum=str(max(Q(r['U']) for r in rows)),
                harmonic_cardinality_relaxation=relaxed,
                quotas=[dict(f=f,N=N,q=q) for f,N,q in sorted(used_quotas)],
                cpu_seconds=time.process_time()-START,rows=rows)
    (HERE/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','quotas')},indent=2))
    for row in rows:
        print(row['kind'],row['degrees'],row.get('tau'),row['U'])


if __name__=='__main__':
    main()
