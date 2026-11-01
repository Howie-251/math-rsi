"""Exact caller check; no solver, no external package, no historical data."""
from fractions import Fraction as F
import json

# Direct feasible objective: interval upper bound plus either quota fixes z=1.
c = F(1)
lower_from_each_quota = [F(1), F(1)]
feasible_lower = max(F(0), *lower_from_each_quota)
assert feasible_lower == c
z = feasible_lower
w = F(1)
cost = w*z
assert all(z >= b for b in lower_from_each_quota)

# Evaluate the imported bound independently of the direct objective computation.
delta = [F(1), F(1)]
a = [F(1), F(1)]
unrepaired = sum(d*b for d,b in zip(delta, lower_from_each_quota))
combined_coefficient = sum(d*x for d,x in zip(delta,a))
capacity_penalty = c*max(F(0), combined_coefficient-w)
repaired = unrepaired-capacity_penalty
assert cost == 1 and unrepaired == 2 and capacity_penalty == 1
assert repaired == cost and not cost >= unrepaired

# Signed-coefficient spot checks exercise both branches of the only inequality
# used in the general proof. They are diagnostic, not a real-domain proof.
checks = 0
for e in map(F, [-2, -1, 0, 1, 2]):
    for capacity in map(F, [0, 1, 2]):
        for value in [F(0), capacity/2, capacity]:
            assert e*value <= capacity*max(F(0), e)
            checks += 1

print(json.dumps({
    'scope': 'one-slot two-quota exact caller; signed scalar diagnostics',
    'feasible_z': str(z), 'actual_cost': str(cost),
    'two_individual_bounds': ['1', '1'],
    'incorrect_same_cost_sum': str(unrepaired),
    'incorrect_bound_refuted': cost < unrepaired,
    'capacity_penalty': str(capacity_penalty),
    'repaired_bound': str(repaired), 'repaired_bound_valid_and_tight': repaired == cost,
    'signed_scalar_checks': checks,
    'general_real_theorem_proved_by': 'finite algebra in PROOF_DRAFT.md, not these samples'
}, indent=2))
