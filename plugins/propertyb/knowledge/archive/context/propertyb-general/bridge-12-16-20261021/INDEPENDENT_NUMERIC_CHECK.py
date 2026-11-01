#!/usr/bin/env python3
"""Independent replay: exact recurrence for J, mpmath.iv outward logarithms.

Reads numeric_bridge.json only. Does not import either original verifier.
All assertions concern exact rationals or interval endpoints, never binary floats.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json
import platform
import time

import mpmath as mp

HERE = Path(__file__).resolve().parent
mp.iv.dps = 120


def rational(pair):
    return Q(int(pair[0]), int(pair[1]))


def interval(q):
    q = Q(q)
    return mp.iv.mpf(q.numerator) / mp.iv.mpf(q.denominator)


def endpoint_q(t):
    """Exact rational decoding of a finite mpmath binary endpoint."""
    sign, mantissa, exponent, _ = t
    assert isinstance(mantissa, int)
    return Q((-1 if sign else 1) * mantissa) * Q(2) ** exponent


def bounds(x):
    return tuple(endpoint_q(t) for t in x._mpi_)


def display_bounds(x):
    # Human-readable display only; all decisions use exact bounds above.
    return str(x)


def integral(k, p):
    # Integration by parts: (2k-1)J_k = p(1-p²)^(k-1)+(2k-2)J_(k-1).
    # This does not reuse the source's alternating-binomial summation.
    value = p
    for n in range(2, k + 1):
        value = (p * (1 - p*p)**(n-1) + (2*n-2)*value) / (2*n-1)
    assert value > 0
    return value


def geometry(k, n):
    # Find v by an integer binary search, independent of source's isqrt formula.
    target = k * (k-1) * n
    lo, hi = 1, target + 1
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid*(mid-1) <= target:
            lo = mid
        else:
            hi = mid
    v = lo
    assert v*(v-1) <= target < v*(v+1)
    r = min(v, max(k*k-k+1, (v-1)//(k-1)))
    assert k <= r <= v
    return v, r, min(Q(n*(n-1)), Q(n*n*(r-1), r))


def coefficient(k, n, improved):
    g = geometry(k, n)[2] if improved else Q(n*(n-1))
    return g / 2**(2*k-2)


def accept(q):
    k, n = q['k'], q['budget']
    p = rational(q['p'])
    assert 0 < p <= 1
    improved = q['criterion'] == 'clique_C2'
    assert q['criterion'] in ('clique_C2', 'old_RS')
    j, a = integral(k, p), 1-(1-p)**k
    f = mp.iv.ln(interval(coefficient(k,n,improved)*j))
    f -= interval(Q(n,2**(k-1))) * mp.iv.ln(interval(a))
    low, high = bounds(f)
    assert high < 0
    assert Q(q['log_gap_lower']) <= low <= high <= Q(q['log_gap_upper'])
    v,r,g = geometry(k,n)
    assert (q['v'], q['r'], rational(q['g'])) == (v,r,g)
    assert q['strict_acceptance'] is True
    return dict(k=k,budget=n,criterion=q['criterion'],v=v,r=r,
                independent_log_gap=display_bounds(f),status='PASS')


def reject(q):
    k,n = q['k'],q['budget']
    improved = q['criterion']=='clique_C2'
    c = coefficient(k,n,improved)
    kap = Q(n,2**(k-1))
    eps = rational(q['small_interval_right'])
    assert kap > 1 and eps == Q(1,100*k)
    # p=0 in the original strict criterion gives 0<0 and hence is excluded.
    assert q['p_zero']=='0 < 0 is false'
    small = mp.iv.ln(interval(c*(1-eps*eps)**(k-1)))
    small -= interval(kap)*mp.iv.ln(interval(k))
    small -= interval(kap-1)*mp.iv.ln(interval(eps))
    assert bounds(small)[0] > 0
    assert Q(q['small_interval_log_gap_lower']) <= bounds(small)[0]
    cells=q['cells']
    assert len(cells)==q['cell_count'] and len(cells)>0
    assert rational(cells[0]['left'])==eps
    assert rational(cells[-1]['right'])==1
    cache={}
    def ep(p):
        if p not in cache:
            cache[p]=(mp.iv.ln(interval(c*integral(k,p))),
                      interval(kap)*mp.iv.ln(interval(1-(1-p)**k)))
        return cache[p]
    previous=eps
    minimum=None
    for cell in cells:
        l,h=rational(cell['left']),rational(cell['right'])
        assert previous==l and eps<=l<h<=1
        f=ep(l)[0]-ep(h)[1]
        low=bounds(f)[0]
        assert low>0
        assert Q(cell['log_gap_lower'])<=low
        minimum=low if minimum is None else min(minimum,low)
        previous=h
    assert previous==1
    assert Q(q['minimum_cell_lower'])==min(Q(t['log_gap_lower']) for t in cells)
    assert q['all_p_rejected'] is True
    assert q['split_attempts']==2*len(cells)-1
    return dict(k=k,budget=n,criterion=q['criterion'],cell_count=len(cells),
                small_interval=display_bounds(small),
                minimum_cell_lower_rational=[str(minimum.numerator),str(minimum.denominator)],
                full_parameter_coverage='p=0, (0,eps], [eps,1]',status='PASS')


def main():
    start=time.perf_counter()
    doc=json.loads((HERE/'numeric_bridge.json').read_text())
    assert [row['k'] for row in doc['rows']]==list(range(12,17))
    expected_old=[4632,9538,19601,40214,82376]
    expected_new=[4646,9563,19646,40293,82492]
    accepted=[]
    rejected=[]
    gains=[]
    for i,row in enumerate(doc['rows']):
        k=row['k']
        old,new=row['old_budget_maximum'],row['new_budget_maximum']
        assert (old,new)==(expected_old[i],expected_new[i])
        assert row['old_lower_bound']==old+1 and row['new_lower_bound']==new+1
        assert row['delta']==new-old
        for name in ('old_feasible','new_feasible','uniform_gain_feasible'):
            q=row[name]
            assert q['k']==k
            assert q['criterion']==('old_RS' if name=='old_feasible' else 'clique_C2')
            accepted.append(accept(q))
        assert row['old_feasible']['budget']==old
        assert row['new_feasible']['budget']==new
        gc=row['uniform_gain_certificate']
        ln=mp.iv.ln(interval(k))
        assert Q(gc['ln_k_lower'])<=bounds(ln)[0]
        assert bounds(ln)[1]<=Q(gc['ln_k_upper'])
        sq=isqrt(old)
        assert sq*sq<=old<(sq+1)**2 and gc['isqrt_M']==sq
        conservative=Q(sq,8)/(1+Q(gc['ln_k_upper']))
        gain=conservative.numerator//conservative.denominator
        assert gain==gc['gain']
        assert row['uniform_gain_feasible']['budget']==old+gain
        assert row['uniform_gain_feasible']['p']==row['old_feasible']['p']
        gains.append(dict(k=k,gain= gain,status='PASS'))
        for name,base,criterion in (('old_next_rejection',old,'old_RS'),
                                   ('new_next_rejection',new,'clique_C2')):
            q=row[name]
            assert (q['k'],q['budget'],q['criterion'])==(k,base+1,criterion)
            rejected.append(reject(q))
    assert (doc['k12_seed']['k'],doc['k12_seed']['budget'],rational(doc['k12_seed']['p']))==(12,4423,Q(1,12))
    seed=accept(doc['k12_seed'])
    result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',
                deterministic_recomputation='PASS: independent exact recurrence plus mpmath.iv logarithms',
                scope='Only the saved k=12..16 numeric certificates; no global hypergraph proof or Lean verification.',
                python=platform.python_version(),mpmath_version=mp.__version__,interval_decimal_precision=mp.iv.dps,
                accepted=accepted,rejected=rejected,gains=gains,seed=seed,
                accepted_main_count=len(accepted),all_parameter_exclusion_count=len(rejected),
                total_rejection_cells=sum(x['cell_count'] for x in rejected),
                elapsed_seconds=time.perf_counter()-start,
                software_trust='Python exact integer/Fraction arithmetic and mpmath.iv outward interval logarithms; not a proof-kernel artifact.')
    (HERE/'INDEPENDENT_NUMERIC_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','accepted_main_count','all_parameter_exclusion_count','total_rejection_cells','elapsed_seconds')},ensure_ascii=False))


if __name__=='__main__':
    main()
