#!/usr/bin/env python3
"""Finite k=12..16 diagnostic. Generation uses mpmath; replay is stdlib only.

Import the existing outward-interval arithmetic. Do not modify its data or code.
Old maxima are over the natural extension of Definition B.1 to these five k.
"""
from __future__ import annotations
import argparse
from decimal import ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
import importlib.util
import json
from math import isqrt
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'bound-figure-20261021' / 'general_data.py'
spec = importlib.util.spec_from_file_location('general_data', SOURCE)
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
DEST = HERE / 'numeric_bridge.json'


def pair(q):
    return [str(q.numerator), str(q.denominator)]


def unpair(q):
    return F(int(q[0]), int(q[1]))


def geometry(k, n):
    v = (1 + isqrt(1 + 4*k*(k-1)*n)) // 2
    assert v*(v-1) <= k*(k-1)*n < v*(v+1)
    r = min(v, max(k*k-k+1, (v-1)//(k-1)))
    g = min(F(n*(n-1)), F(n*n*(r-1), r))
    return v, r, g


def log_gap(k, n, p, improved=False):
    d = 2**(k-1)
    j = iv.exact_integral(k, p)
    a = 1-(1-p)**k
    g = geometry(k, n)[2] if improved else F(n*(n-1))
    lq = iv.ln_interval(g*j/(d*d))
    la = iv.interval_times_positive(iv.ln_interval(a), F(n,d))
    return (iv.rounded(lambda: lq[0]-la[1], ROUND_FLOOR),
            iv.rounded(lambda: lq[1]-la[0], ROUND_CEILING))


def feasible(k, n, p, improved=False):
    lo, hi = log_gap(k, n, p, improved)
    assert hi < 0, (k,n,hi)
    v,r,g = geometry(k,n)
    return dict(k=k, budget=n, p=pair(p), criterion='clique_C2' if improved else 'old_RS',
                log_gap_lower=str(lo), log_gap_upper=str(hi),
                v=v,r=r,g=pair(g), strict_acceptance=True)


def global_rejection(k, n, improved=False):
    """Reject every p in [0,1]; no assumption about the optimizer's globality.

    For p<=eps, J>=p(1-eps^2)^(k-1), a<=kp, hence
    Q/a^(n/d)>=C*(1-eps^2)^(k-1)/(k^(n/d)*eps^(n/d-1)).
    For each positive closed cell [l,h], J(p)>=J(l), a(p)<=a(h).
    """
    d=2**(k-1)
    kap=F(n,d)
    assert kap>1
    g=geometry(k,n)[2] if improved else F(n*(n-1))
    c=g/(d*d)
    eps=F(1,100*k)
    first=iv.ln_interval(c*(1-eps*eps)**(k-1))[0]
    second=iv.interval_times_positive(iv.ln_interval(k),kap)[1]
    third=iv.interval_times_positive(iv.ln_interval(eps),kap-1)[1]
    small=iv.rounded(lambda:first-second-third,ROUND_FLOOR)
    assert small>0
    cache={}
    def endpoint(p):
        if p not in cache:
            cache[p]=(iv.ln_interval(c*iv.exact_integral(k,p)),
                      iv.interval_times_positive(iv.ln_interval(1-(1-p)**k),kap))
        return cache[p]
    stack=[(eps,F(1))]
    cells=[]
    attempts=0
    while stack:
        l,h=stack.pop()
        attempts+=1
        assert attempts<=200000, 'bounded diagnostic exhausted'
        lower=iv.rounded(lambda:endpoint(l)[0][0]-endpoint(h)[1][1],ROUND_FLOOR)
        if lower>0:
            cells.append(dict(left=pair(l),right=pair(h),log_gap_lower=str(lower)))
        else:
            mid=(l+h)/2
            stack.extend(((mid,h),(l,mid)))
    cells.sort(key=lambda x:unpair(x['left']))
    assert unpair(cells[0]['left'])==eps
    assert unpair(cells[-1]['right'])==1
    assert all(unpair(a['right'])==unpair(b['left']) for a,b in zip(cells,cells[1:]))
    return dict(k=k,budget=n,criterion='clique_C2' if improved else 'old_RS',
                p_zero='0 < 0 is false',small_interval_right=pair(eps),
                small_interval_log_gap_lower=str(small),cells=cells,
                cell_count=len(cells),split_attempts=attempts,
                minimum_cell_lower=str(min(F(x['log_gap_lower']) for x in cells)),
                all_p_rejected=True)


def propose(k):
    import mpmath as mp
    mp.mp.dps=65
    d=mp.mpf(2)**(k-1)
    def sys(m,p,r=None):
        j=mp.betainc(mp.mpf('.5'),k,0,p*p)/2
        a=-mp.expm1(k*mp.log1p(-p))
        g=m*(m-1) if r is None else m*m*(1-mp.mpf(1)/r)
        f=mp.log(g*j/(d*d))-m/d*mp.log(a)
        deriv=(1-p*p)**(k-1)/j-m/d*k*(1-p)**(k-1)/a
        return f,deriv
    m,p=mp.findroot(lambda m,p:sys(m,p),(d*mp.sqrt(mp.mpf(k)/mp.log(k)),mp.log(k)/k*.6))
    oldn=int(mp.floor(m))
    old=feasible(k,oldn,F(int(mp.nint(p*10**35)),10**35))
    old['local_real_threshold']=mp.nstr(m,55)
    # Recalculate r after each continuous root; r is always exact at integer N.
    r=geometry(k,oldn)[1]
    for _ in range(10):
        nn,pp=mp.findroot(lambda m,p:sys(m,p,r),(m,p))
        n=int(mp.floor(nn))
        rr=geometry(k,n)[1]
        if rr==r:
            break
        r=rr
    else:
        raise AssertionError('r did not stabilize')
    new=feasible(k,n,F(int(mp.nint(pp*10**35)),10**35),True)
    new['local_real_threshold']=mp.nstr(nn,55)
    return old,new


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    start=time.perf_counter()
    if args.verify:
        doc=json.loads(DEST.read_text())
        assert [r['k'] for r in doc['rows']]==list(range(12,17))
        for row in doc['rows']:
            for name in ('old_feasible','new_feasible','uniform_gain_feasible'):
                q=row[name]
                got=feasible(q['k'],q['budget'],unpair(q['p']),name!='old_feasible')
                assert all(q[key]==value for key,value in got.items())
            gain,loglo,loghi,sq=iv.certified_gain(row['k'],row['old_budget_maximum'])
            assert row['uniform_gain_certificate']==dict(gain=gain,ln_k_lower=loglo,
                        ln_k_upper=loghi,isqrt_M=sq)
            assert row['old_budget_maximum']==row['old_feasible']['budget']
            assert row['new_budget_maximum']==row['new_feasible']['budget']
            assert row['old_lower_bound']==row['old_budget_maximum']+1
            assert row['new_lower_bound']==row['new_budget_maximum']+1
            assert row['delta']==row['new_budget_maximum']-row['old_budget_maximum']
            assert row['uniform_gain_feasible']['budget']==row['old_budget_maximum']+gain
            assert row['uniform_gain_feasible']['p']==row['old_feasible']['p']
            assert row['old_next_rejection']['budget']==row['old_budget_maximum']+1
            assert row['new_next_rejection']['budget']==row['new_budget_maximum']+1
            for name in ('old_next_rejection','new_next_rejection'):
                q=row[name]
                got=global_rejection(q['k'],q['budget'],name=='new_next_rejection')
                assert q==got
        q=doc['k12_seed']
        assert q==feasible(12,4423,F(1,12))
        print('PASS: five exact old/new feasible certificates; ten complete all-p exclusions; k12 seed')
        print('Replay seconds:',time.perf_counter()-start)
        return
    rows=[]
    for k in range(12,17):
        old,new=propose(k)
        gain,loglo,loghi,sq=iv.certified_gain(k,old['budget'])
        uniform=feasible(k,old['budget']+gain,unpair(old['p']),True)
        rej=global_rejection(k,old['budget']+1)
        newrej=global_rejection(k,new['budget']+1,True)
        rows.append(dict(k=k,old_feasible=old,old_next_rejection=rej,
                         new_feasible=new,new_next_rejection=newrej,
                         uniform_gain_feasible=uniform,
                         uniform_gain_certificate=dict(gain=gain,ln_k_lower=loglo,
                                        ln_k_upper=loghi,isqrt_M=sq),
                         old_budget_maximum=old['budget'],new_budget_maximum=new['budget'],
                         old_lower_bound=old['budget']+1,new_lower_bound=new['budget']+1,
                         delta=new['budget']-old['budget']))
        print(k,old['budget'],new['budget'],rows[-1]['delta'],
              rej['cell_count'],newrej['cell_count'],flush=True)
    doc=dict(scope='k=12..16; exact rational witnesses and all-p parameter exclusions, no hypergraph enumeration',
             old_definition='natural extension of Definition B.1 (formally stated there only for k>=17)',
             new_definition='largest accepted integer N in Corollary C.2',
             maximality='At rejected M+1, all p in [0,1] are excluded; for larger budgets both Q and exponent n/d make acceptance harder (0<a<=1; old g and new g are nondecreasing).',
             verification='Exact rational polynomial integral; existing 90-digit outward Decimal log intervals; parameter interval coverage verified.',
             rows=rows,k12_seed=feasible(12,4423,F(1,12)),
             elapsed_seconds=time.perf_counter()-start)
    DEST.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n')
    print('Generation seconds:',time.perf_counter()-start)


if __name__=='__main__':
    main()
