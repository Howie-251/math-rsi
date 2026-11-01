#!/usr/bin/env python3
"""Derive five uniform-curve rows from the saved exact numeric certificates."""
import json
from decimal import Decimal, localcontext, ROUND_FLOOR
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = json.loads((HERE / 'numeric_bridge.json').read_text())
check = json.loads((HERE / 'INDEPENDENT_NUMERIC_CHECK.json').read_text())
assert check['status'] == 'PASS'
rows = []
for r in raw['rows']:
    c = r['uniform_gain_certificate']
    M, g = r['old_budget_maximum'], c['gain']
    with localcontext() as ctx:
        ctx.prec = 110
        derived = int((Decimal(c['isqrt_M']) / (8 * (1 + Decimal(c['ln_k_upper'])))).to_integral_value(rounding=ROUND_FLOOR))
    assert derived == g
    assert r['old_feasible']['budget'] == M and r['old_feasible']['strict_acceptance']
    assert r['uniform_gain_feasible']['budget'] == M + g and r['uniform_gain_feasible']['strict_acceptance']
    assert any(x['k'] == r['k'] and x['gain'] == g and x['status'] == 'PASS' for x in check['gains'])
    rows.append(dict(k=r['k'], M_plot=M, baseline_lower=M+1, gain_certified=g,
                     improved_lower=M+1+g, isqrt_M=c['isqrt_M'],
                     ln_k_lower=c['ln_k_lower'], ln_k_upper=c['ln_k_upper'],
                     old_feasible=r['old_feasible'], uniform_gain_feasible=r['uniform_gain_feasible'],
                     proof_status='Lean uniform theorem; numeric values independently computed', verification='PASS_SAVED_CERTIFICATES_AND_INDEPENDENT_NUMERIC_CHECK'))
assert [r['k'] for r in rows] == list(range(12,17))
out = dict(scope='Five new plot rows only; same uniform theorem gain, not optimized C.2 gain',
           theorem='m(k) >= B_RS(k)+1+floor(sqrt(B_RS(k))/(8*(1+ln(k)))) for all k>=12',
           source='numeric_bridge.json', independent_check='INDEPENDENT_NUMERIC_CHECK.json',
           gain_definition='floor(isqrt(M_plot)/(8*(1+ln_k_upper))) <= theorem gain', rows=rows)
(HERE / 'bridge_plot_data.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print([(r['k'], r['baseline_lower'], r['gain_certified'], r['improved_lower']) for r in rows])
