"""Independent prime-power/divisor/slot audit; no graph or generator search."""
import json
import time
from math import isqrt
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
saved = json.loads((OUT/'CYCLIC_TRIANGLE_PARAMETER_FILTER.json').read_text())
BASELINES = {4:364,5:650,6:1518,7:2810,8:5334,9:9020,10:33397,11:37628,12:42342}


def moore_bound(degree):
    layer = degree
    total = 1
    for _ in range(5):
        total += layer
        layer *= degree-1
    return total


max_q = max(moore_bound(d)//(3*(d-1)**2) for d in BASELINES)
sieve = [True]*(max_q+1)
sieve[0] = sieve[1] = False
for p in range(2,isqrt(max_q)+1):
    if sieve[p]:
        for multiple in range(p*p,max_q+1,p):
            sieve[multiple] = False
prime_powers = {}
for p in range(2,max_q+1):
    if not sieve[p]:
        continue
    power, exponent = p, 1
    while power <= max_q:
        assert power not in prime_powers
        prime_powers[power] = (p,exponent)
        power *= p
        exponent += 1


def divisors(number):
    answer = set()
    for divisor in range(1,isqrt(number)+1):
        if number % divisor == 0:
            answer.add(divisor)
            answer.add(number//divisor)
    return sorted(answer)


degrees = []
all_survivors = []
for d,lower in BASELINES.items():
    h,k = d-1,(d-1)*(d-2)
    moore = moore_bound(d)
    # Check inequalities directly over independently generated prime powers.
    fields = [q for q in sorted(prime_powers) if lower < 3*q*h*h <= moore]
    survivors = []
    tested_actions = 0
    for q in fields:
        p,exponent = prime_powers[q]
        for m in divisors(k):
            if (q-1) % m:
                continue
            tested_actions += 1
            colors = (q-1)//m
            nonzero_involutions = p == 2 or (m % 2 == 0 and (k//m) % 2 == 1)
            inverse_exchanges_colors = p != 2 and m % 2 == 1
            if inverse_exchanges_colors:
                assert colors % 2 == 0
            # Independent abstract-slot minimization, not a copy of s_min formulas.
            minimum_internal = None
            for slots in range(2*colors+2):
                if slots % 2 != h % 2:
                    continue
                if nonzero_involutions:
                    color_capacity = slots
                elif inverse_exchanges_colors:
                    color_capacity = 2*(slots//2)
                else:
                    color_capacity = slots//2
                if color_capacity >= colors:
                    minimum_internal = slots
                    break
            assert minimum_internal is not None
            total_slots = 2*colors+minimum_internal
            if total_slots <= h:
                row = {'degree':d,'q':q,'characteristic':p,'field_exponent':exponent,
                       'action_order':m,'colors':colors,'n':3*q*h*h,
                       'minimum_internal_slots':minimum_internal,'minimum_total_slots':total_slots}
                survivors.append(row)
                all_survivors.append(row)
    original = next(entry for entry in saved['degrees'] if entry['degree']==d)
    exact_interval = [lower//(3*h*h)+1,moore//(3*h*h)]
    assert original['saved_lower_bound'] == lower
    assert original['moore_bound'] == moore
    assert original['field_size_interval'] == exact_interval
    assert original['prime_powers_checked'] == len(fields)
    expected = [(x['q'],x['action_order'],x['colors'],x['n'],x['minimum_slots']) for x in original['survivors']]
    actual = [(x['q'],x['action_order'],x['colors'],x['n'],x['minimum_total_slots']) for x in survivors]
    assert actual == expected
    degrees.append({'degree':d,'field_interval':exact_interval,'prime_powers':fields,
                    'prime_power_count':len(fields),'action_orders_tested':tested_actions,
                    'survivors':survivors,'all_saved_values_match':True})
assert len(all_survivors)==9
result = {
    'status':'COMPLETE_INDEPENDENT_NECESSARY_FILTER_CHECK',
    'baseline_scope':'Given saved snapshot only; no current public-source verification.',
    'independent_methods':[
        'Prime sieve followed by prime powers, instead of trial-factor recognition.',
        'Direct lower<n<=Moore tests, with independently accumulated BFS-layer Moore bound.',
        'Divisors of k via complementary factor pairs, then test divisibility of q-1.',
        'Integer slot minimization by parity and inverse-color capacity, not s_min formula reuse.',
    ],
    'maximum_q_from_Moore':max_q,'all_nine_tuples_match':True,
    'degrees':degrees,'survivors':all_survivors,
    'cpu_seconds':time.process_time()-START,
    'graphs_generated':0,'generator_sets_enumerated':0,
    'nonclaim':'This verifies the stated necessary parameter filter, not diameter-five existence or completeness outside its scalar triangle family.',
}
(OUT/'CYCLIC_TRIANGLE_PARAMETER_FILTER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'maximum_q':max_q,'survivors':all_survivors,
                  'prime_power_counts':[d['prime_power_count'] for d in degrees],
                  'cpu_seconds':result['cpu_seconds']},indent=2))
