"""Bounded numerical profile; lower bound on Grill's actual finite-position sum.

The quadrature is high-precision exploratory arithmetic, not a formal interval proof.
The discrete lower comparison in discrete_lower is an analytic inequality proved
in REPORT.md; it avoids enumerating exponentially many vertex positions.
"""
import argparse
import json
import time
from pathlib import Path

import mpmath as mp


def integral(k, p):
    return mp.betainc(mp.mpf('0.5'), k, 0, p*p) / 2


def rs_log_ratio(k, kap, p):
    m = kap * mp.power(2, k-1)
    q = kap*kap*(1-1/m)
    a = -mp.expm1(k*mp.log1p(-p))
    return mp.log(q*integral(k, p)) - kap*mp.log(a)


def minimize(fun, lo, hi, iterations=220):
    phi = (mp.sqrt(5)-1)/2
    c, d = hi-phi*(hi-lo), lo+phi*(hi-lo)
    fc, fd = fun(c), fun(d)
    for _ in range(iterations):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi-phi*(hi-lo)
            fc = fun(c)
        else:
            lo, c, fc = c, d, fd
            d = lo+phi*(hi-lo)
            fd = fun(d)
    p = (lo+hi)/2
    return fun(p), p


def rs_threshold(k):
    lo, hi = mp.mpf(1), mp.mpf(k)
    for _ in range(210):
        mid = (lo+hi)/2
        val, _ = minimize(lambda p: rs_log_ratio(k, mid, p),
                          mp.mpf('1e-20'), mp.mpf('.95'))
        if val < 0:
            lo = mid
        else:
            hi = mid
    root = (lo+hi)/2*mp.power(2,k-1)
    m0 = int(mp.floor(root))
    val, p = minimize(lambda p: rs_log_ratio(k, mp.mpf(m0)/mp.power(2,k-1), p),
                      mp.mpf('1e-20'), mp.mpf('.95'))
    return m0, root, val, p


def continuous(k, m, gamma):
    kap = mp.mpf(m)/mp.power(2,k-1)
    q = mp.mpf(gamma)/mp.power(4,k-1)
    # Exact minimizer of the linear-endpoint continuous criterion.
    p = mp.expm1(mp.log(kap*k/q)/(k-1))
    p = max(mp.mpf(0), min(mp.mpf(1), p))
    val = kap*mp.power(1-p,k) + q*integral(k,p)
    peak = min(kap*k, q)  # density maximum at x=1/2
    return val, p, peak


def discrete_lower(k, v, m, gamma):
    c, p, peak = continuous(k,m,gamma)
    # For N=v-2k+3 and s=N/v, prove D >= s^(2k-1)*C - 2*s^(2k-2)*peak/v.
    s = mp.mpf(v-2*k+3)/v
    low = mp.power(s,2*k-1)*c - 2*mp.power(s,2*k-2)*peak/v
    return low, c, p


def profile(k):
    start = time.process_time()
    m0, root, rsval, prs = rs_threshold(k)
    m = m0+1
    v = int(mp.floor((k-2)*mp.sqrt(m)))
    # Formal old degree/codegree relaxation: one universal center, balanced
    # outside degrees, r_outside=d_outside, r_center=max outside degree.
    r = ((k-1)*m + (v-2))//(v-1)
    gamma = m*(m-1)-r*(r-1)
    lower, cont, pc = discrete_lower(k,v,m,gamma)
    vmax = (1+mp.sqrt(1+4*k*(k-1)*m))/2
    balanced = mp.mpf(m)*2*mp.fprod((mp.mpf(v//2)-j)/(v-j) for j in range(k))
    # Odd v balanced expectation has a second slightly larger class term.
    if v%2:
        balanced = mp.mpf(m)*sum(mp.fprod((mp.mpf(t)-j)/(v-j) for j in range(k))
                                  for t in (v//2,v//2+1))
    dmin = ((k-1)*m)//(v-1)
    return dict(k=k,m0=m0,comparison_budget=m,rs_real_root=str(root),
                rs_m0_log_ratio=str(rsval),rs_m0_p=str(prs),v=v,
                sqrt_vertex_upper=str(vmax),outside_dmin=dmin,
                global_min_degree=(v+k-3)//(k-1),
                outside_pair_capacity=(k-2)*dmin,required_outside_pairs=v-2,
                old_gamma=gamma,old_gamma_deficit=m*(m-1)-gamma,
                continuous_linear=str(cont),continuous_p=str(pc),
                discrete_lower=str(lower),balanced_union=str(balanced),
                cpu_seconds=time.process_time()-start)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--k',type=int,nargs='+',default=[32,48,64,128])
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('PROFILE.json'))
    args=parser.parse_args()
    mp.mp.dps=90
    results=[]
    for k in args.k:
        row=profile(k)
        results.append(row)
        print(json.dumps(row),flush=True)
        args.output.write_text(json.dumps(results,indent=2)+'\n')
