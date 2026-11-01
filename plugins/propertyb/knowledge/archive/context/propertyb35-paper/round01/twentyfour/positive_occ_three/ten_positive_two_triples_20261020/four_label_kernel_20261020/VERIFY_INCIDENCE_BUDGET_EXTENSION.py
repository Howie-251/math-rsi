"""Replay only changed resource costs for the unchanged 1333 exact column certificates.

The full column/domain check is VERIFY_CERTIFICATES.py / VERIFY_DOMAIN.py.
This file neither discovers certificates nor changes their column inequalities.
"""
from fractions import Fraction as F
from pathlib import Path
import json

base = Path(__file__).resolve().parent
data = json.loads((base / 'ALL_LP.json').read_text())
assert data['complete'] and len(data['rows']) == 1333
seen = set()
profiles = []
for row in data['rows']:
    n = row['n']
    key = (n, tuple(row['capacities']), tuple(row['graph']))
    assert key not in seen
    seen.add(key)
    certificate = row['dual_certificate']
    weights = list(map(F, certificate['budget_weights']))
    assert all(w >= 0 for w in weights)
    assert not certificate['upper_bound_weights']
    assert row['budgets'][:3] == [2-n, 18, 8-2*n]
    assert len(weights) == len(row['budgets'])
    old = sum(F(b)*w for b, w in zip(row['budgets'], weights))
    assert old == F(certificate['bound']) < 1
    # t is the total number of original negative triples, before fixing Z.
    # 40 positive incidences + 3t + 4b <= 7*18 implies b <= floor((86-3t)/4).
    for t in range(n, 3):
        b = (86-3*t)//4
        budgets = list(row['budgets'])
        budgets[0] = t-n
        budgets[1] = b
        cost = sum(F(a)*w for a, w in zip(budgets, weights))
        assert cost == old + (t-2)*weights[0] + (b-18)*weights[1]
        assert cost < 1
        profiles.append(dict(n=n, capacities=row['capacities'], graph=row['graph'],
                             original_t=t, original_b_upper=b, exact_cost=str(cost)))
assert len(profiles) == 1813
assert max(F(row['exact_cost']) for row in profiles) == F(10, 11)
result = dict(PASS=True, unchanged_certificate_keys=len(seen),
              original_budget_profiles=len(profiles), max_exact_cost='10/11',
              original_t_b_upper=[[t, (86-3*t)//4] for t in range(3)],
              unchanged_columns='See VERIFY_CERTIFICATES.py / VERIFICATION.json',
              profiles=profiles)
(base / 'INCIDENCE_BUDGET_EXTENSION.json').write_text(json.dumps(result, indent=2)+'\n')
print('PASS 1333 unchanged certificates, 1813 original (t,b) budget profiles, max 10/11')
