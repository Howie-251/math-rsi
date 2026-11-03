"""Count size multisets only; no quotient matrix is generated or tested.

Necessary domain for c=5,7,...,17 defect components of an order-61 graph:
sum(n)=61, n>=2; each n is 7-smooth, v_3(n)<=2, and
n <= floor(8*(65-2*c)/9).  The last bound uses a positive quotient
neighbor of size at least ceil(n/8), plus c-2 other sizes at least two.

This exact integer DP does not impose diagonal spectral bounds, trace,
handshake, interface capacity, or the matrix polynomial.  Its counts are
not counts of feasible quotients or graphs.  One authorized <=1 CPU
second run, with no search for Q and no automatic follow-up queue.
"""
from pathlib import Path
import json
import os
import resource
import time


def allowed_size(n):
    if n % 27 == 0:
        return False
    for p in (2, 3, 5, 7):
        while n % p == 0:
            n //= p
    return n == 1


def count_multisets(c, values):
    # Each denomination is processed once. Increasing k permits repeated
    # copies of that denomination; order among parts is not counted.
    dp = [[0] * 62 for _ in range(c + 1)]
    dp[0][0] = 1
    for n in values:
        for k in range(1, c + 1):
            for total in range(n, 62):
                dp[k][total] += dp[k - 1][total - n]
    return dp[c][61]


def main():
    cpu0, wall0 = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {1})
    resource.setrlimit(resource.RLIMIT_CPU, (1, 2))
    rows = []
    for c in range(5, 18, 2):
        maximum = 8 * (65 - 2 * c) // 9
        values = [n for n in range(2, maximum + 1) if allowed_size(n)]
        rows.append(dict(c=c, m=(c - 1)//2, maximum_size=maximum,
                         allowed_sizes=values,
                         size_multiset_count=count_multisets(c, values)))
    result = dict(
        status='COMPLETE_SIZE_DOMAIN_COUNT_ONLY',
        scope='Sorted component-size multisets; no Q search or feasibility decision',
        total_vertices=61,
        constraints=['c odd, 5<=c<=17', 'all n>=2', 'sum(n)=61',
                     'all prime factors of n <=7', 'v_3(n)<=2',
                     'n<=floor(8*(65-2*c)/9)'],
        not_tested=['diagonal spectral bounds', 'trace', 'handshake',
                    'positive interface capacity', 'Q^2+Q-11I=1*n^T'],
        rows=rows,
        total_size_multisets=sum(row['size_multiset_count'] for row in rows),
        algorithm_cpu_seconds=time.process_time()-cpu0,
        algorithm_wall_seconds=time.monotonic()-wall0,
        cpu_affinity=[1], cpu_soft_limit_seconds=1)
    out = Path(__file__).with_suffix('.result.json')
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
