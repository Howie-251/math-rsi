#!/usr/bin/env python3
"""Generate feasible RS budgets; verify certificates with exact/interval arithmetic.

Candidate generation uses mpmath.  Certificate replay (--verify) needs only Python's
standard library and does not assume that the candidate optimizer is global.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from math import comb, isqrt
import json
from pathlib import Path
import platform
import time

PREC = 90
DEST = Path(__file__).with_name('general_data.json')


def rounded(op, rounding):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = rounding
        return +op()


def rational_interval(q):
    q = Fraction(q)
    return (rounded(lambda: Decimal(q.numerator)/Decimal(q.denominator), ROUND_FLOOR),
            rounded(lambda: Decimal(q.numerator)/Decimal(q.denominator), ROUND_CEILING))


def ln_interval(q):
    lo, hi = rational_interval(q)
    # Decimal.ln is correctly rounded, ROUND_HALF_EVEN independently of c.rounding.
    # One adjacent representable number on either side encloses each exact log.
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_HALF_EVEN
        return lo.ln().next_minus(), hi.ln().next_plus()


def interval_times_positive(iv, q):
    qlo, qhi = rational_interval(q)
    products_low = [rounded(lambda a=a, b=b: a*b, ROUND_FLOOR)
                    for a in iv for b in (qlo, qhi)]
    products_high = [rounded(lambda a=a, b=b: a*b, ROUND_CEILING)
                     for a in iv for b in (qlo, qhi)]
    return min(products_low), max(products_high)


def exact_integral(k, p):
    """Integral_0^p (1-y^2)^(k-1)dy, an exact rational polynomial."""
    return sum(((-1)**j*comb(k-1, j)*p**(2*j+1)/Fraction(2*j+1)
                for j in range(k)), Fraction(0))


def certified_gain(k, M):
    loglo, loghi = ln_interval(k)
    sqrt_lower = isqrt(M)
    # All operations below are exact rational arithmetic, including floor.
    gain = Fraction(sqrt_lower, 8)/(1+Fraction(loghi))
    return gain.numerator//gain.denominator, str(loglo), str(loghi), sqrt_lower


def certificate(k, M, p):
    assert 17 <= k <= 64 and M >= 2**k and 0 < p <= 1
    d = 2**(k-1)
    J = exact_integral(k, p)
    a = 1-(1-p)**k
    Q = Fraction(M*(M-1), d*d)*J
    assert J > 0 and 0 < a <= 1 and Q > 0
    lq = ln_interval(Q)
    la = interval_times_positive(ln_interval(a), Fraction(M, d))
    lo = rounded(lambda: lq[0]-la[1], ROUND_FLOOR)
    hi = rounded(lambda: lq[1]-la[0], ROUND_CEILING)
    assert hi < 0, f'non-strict or failed RS certificate: k={k}, M={M}, upper={hi}'
    gain, loglo, loghi, sq = certified_gain(k, M)
    base_gain, _, _, base_sq = certified_gain(k, 2**k)
    return dict(k=k, M_plot=M, p_numerator=str(p.numerator), p_denominator=str(p.denominator),
                p_decimal=str(Decimal(p.numerator)/Decimal(p.denominator)),
                baseline_lower=M+1, gain_certified=gain, improved_lower=M+1+gain,
                gain_from_2_to_k=base_gain,
                isqrt_M=sq, isqrt_2_to_k=base_sq,
                ln_k_lower=loglo, ln_k_upper=loghi,
                log_ratio_lower=str(lo), log_ratio_upper=str(hi),
                strict_log_margin_lower=str(rounded(lambda: -hi, ROUND_FLOOR)),
                integral_numerator=str(J.numerator), integral_denominator=str(J.denominator),
                verification='PASS_STRICT_RATIONAL_INTEGRAL_DECIMAL_INTERVAL')


def propose(k):
    import mpmath as mp
    mp.mp.dps = 75
    d = mp.mpf(2)**(k-1)

    def system(kap, p):
        J = mp.betainc(mp.mpf('.5'), k, 0, p*p)/2
        a = -mp.expm1(k*mp.log1p(-p))
        f = mp.log(kap*(kap-1/d)*J)-kap*mp.log(a)
        derivative = (1-p*p)**(k-1)/J-kap*k*(1-p)**(k-1)/a
        return f, derivative

    # A local stationary solution is a candidate, never a maximality certificate.
    kap, p = mp.findroot(system, (mp.sqrt(mp.mpf(k)/mp.log(k)), mp.log(k)/k*.6),
                         tol=mp.mpf('1e-65'), maxsteps=100)
    M = int(mp.floor(kap*d))
    p_rat = Fraction(int(mp.nint(p*10**30)), 10**30)
    # A rejected optimizer proposal cannot become a plotted point. A one-integer
    # retreat suffices for rounding ties; the loop is deliberately bounded.
    for retreat in range(5):
        try:
            row = certificate(k, M-retreat, p_rat)
            row['candidate_real_threshold'] = mp.nstr(kap*d, 65)
            row['candidate_method'] = 'local stationary root only; no maximality assertion'
            row['retreat_from_candidate_floor'] = retreat
            return row
        except AssertionError:
            if retreat == 4:
                raise


def verify(document):
    assert [r['k'] for r in document['rows']] == list(range(17, 65))
    fields = ('M_plot', 'p_numerator', 'p_denominator', 'baseline_lower',
              'gain_certified', 'improved_lower', 'gain_from_2_to_k',
              'isqrt_M', 'isqrt_2_to_k', 'ln_k_lower', 'ln_k_upper',
              'log_ratio_lower', 'log_ratio_upper', 'strict_log_margin_lower',
              'integral_numerator', 'integral_denominator', 'verification')
    for row in document['rows']:
        replay = certificate(row['k'], row['M_plot'],
                             Fraction(int(row['p_numerator']), int(row['p_denominator'])))
        assert all(row[f] == replay[f] for f in fields), row['k']
    print(f'PASS: {len(document["rows"])} strict feasible-budget and conservative-gain certificates')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--output', type=Path, default=DEST)
    args = parser.parse_args()
    if args.verify:
        verify(json.loads(args.output.read_text()))
        return
    start = time.perf_counter()
    rows = []
    for k in range(17, 65):
        rows.append(propose(k))
        print(k, rows[-1]['M_plot'], rows[-1]['gain_certified'], flush=True)
    import mpmath as mp
    doc = dict(scope='Certified feasible budgets M_plot(k) <= B_RS(k), not exact maxima; k=17..64',
               theorem='m(k) >= B_RS(k)+1+floor(sqrt(B_RS(k))/(8*(1+ln(k)))) for k>=17',
               plotted_corollary='m(k) >= M_plot(k)+1+gain_certified(k)',
               gain_definition='floor(isqrt(M_plot)/(8*(1+ln_k_upper))) <= theorem gain',
               base_gain_definition='same conservative formula with M=2^k',
               acceptance='ln(M*(M-1)*J/2^(2*k-2)) - M/2^(k-1)*ln(1-(1-p)^k) < 0',
               verifier='Exact Fraction polynomial J; 90-digit outward Decimal interval arithmetic',
               dependencies=dict(generation_mpmath=mp.__version__, replay='Python standard library only',
                                 python=platform.python_version()),
               elapsed_seconds=time.perf_counter()-start, rows=rows)
    verify(doc)
    args.output.write_text(json.dumps(doc, ensure_ascii=False, indent=2)+'\n')


if __name__ == '__main__':
    main()
