"""Small necessary-parameter filter; no generator sets or graphs are searched."""
import json
import math
import time
from pathlib import Path

BASELINES = {4:364, 5:650, 6:1518, 7:2810, 8:5334, 9:9020,
             10:33397, 11:37628, 12:42342}

def prime(n):
    return n >= 2 and all(n % t for t in range(2, math.isqrt(n)+1))

def characteristic(q):
    for p in range(2, q+1):
        if q % p == 0 and prime(p):
            remaining = q
            while remaining % p == 0:
                remaining //= p
            return p if remaining == 1 else None

def main():
    start = time.process_time()
    degrees = []
    for d, lower in BASELINES.items():
        h, k = d-1, (d-1)*(d-2)
        moore = 1+d*sum((d-1)**i for i in range(5))
        low, high = lower//(3*h*h)+1, moore//(3*h*h)
        survivors = []
        fields = 0
        for q in range(low, high+1):
            p = characteristic(q)
            if p is None:
                continue
            fields += 1
            common = math.gcd(k, q-1)
            for m in range(1, common+1):
                if k % m or (q-1) % m:
                    continue
                colors = (q-1)//m
                if p == 2 or (m % 2 == 0 and (k//m) % 2 == 1):
                    internal = colors+(h-colors) % 2
                    case = 'nonzero_involutions'
                elif m % 2:
                    internal = colors+h % 2
                    case = 'inverse_pairs_exchange_two_colors'
                else:
                    internal = 2*colors+h % 2
                    case = 'inverse_pairs_stay_in_one_color'
                slots = 2*colors+internal
                if slots <= h:
                    survivors.append(dict(q=q, characteristic=p, action_order=m,
                        colors=colors, n=3*q*h*h, minimum_slots=slots, case=case))
        degrees.append(dict(degree=d, saved_lower_bound=lower, moore_bound=moore,
            field_size_interval=[low, high], prime_powers_checked=fields,
            survivors=survivors))
    result = dict(status='COMPLETE_NECESSARY_PARAMETER_FILTER_ONLY',
        baseline_snapshot='2026-10-26, not a new public-source check',
        scope='A=F_q x C3, K=C_((d-1)(d-2)) acting by one field scalar, H=<k^(d-2)>',
        degrees=degrees, CPU_seconds=time.process_time()-start,
        generator_sets_enumerated=0, graphs_generated=0)
    path = Path(__file__).with_name('CYCLIC_TRIANGLE_PARAMETER_FILTER.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
