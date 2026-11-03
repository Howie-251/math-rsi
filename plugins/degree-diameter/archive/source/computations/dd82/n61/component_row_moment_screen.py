"""Exact necessary row-moment screen; sanity/profile/full completed once.

For a row of size n and another component of size h, write g=gcd(n,h),
a=h/g, b=n/g. Detailed balance and simplicity give q_ij=a*t,
q_ji=b*t, 0<=t<=min(g,8//a,8//b). The row and diagonal polynomial
conditions are sum(a*t)=8-d and sum(a*b*t*t)=n+11-d-d*d.
Rows are solved separately; their t choices need not be compatible.
"""
import argparse
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
import json
import os
import resource
import signal
import time

from component_large_size_screen import trace_supported

EXPECTED = {5: 327, 7: 2310, 9: 5587, 11: 6588,
            13: 5378, 15: 3247, 17: 1759}
HERE = Path(__file__).resolve().parent


@lru_cache(maxsize=None)
def options(n, h):
    g = gcd(n, h)
    a, b = h//g, n//g
    return tuple((a*t, a*b*t*t)
                 for t in range(min(g, 8//a, 8//b)+1))


@lru_cache(maxsize=65536)
def row_moments(n, others):
    """dp[s] has bit k iff (sum q_ij, sum q_ij*q_ji)=(s,k)."""
    # Every future contribution is nonnegative, and all requested moments
    # n+11-d-d^2 are <=n+11. Thus these truncations cannot lose a solution.
    mask = (1 << (n+12))-1
    dp = [1]+[0]*8
    for h in others:
        nxt = [0]*9
        for add_sum, add_moment in options(n, h):
            if add_moment > n+11:
                continue
            for s in range(9-add_sum):
                nxt[s+add_sum] |= (dp[s] << add_moment) & mask
        dp = nxt
    return tuple(dp)


def row_domains(sizes, domains, budget_check):
    result = []
    for i, (n, ds) in enumerate(zip(sizes, domains)):
        budget_check()
        moments = row_moments(n, sizes[:i]+sizes[i+1:])
        result.append([d for d in ds if 0 <= n+11-d-d*d and
                       (moments[8-d] >> (n+11-d-d*d)) & 1])
    return result


def sanity():
    """Tiny independent products, not the previous c=3 enumeration."""
    cases = [(2, (2, 2, 3)), (3, (2, 3, 6)), (4, (2, 4, 6)),
             (6, (2, 3, 4)), (5, (2, 5, 5))]
    total_assignments = 0
    for n, others in cases:
        ratios = [(h//gcd(n, h), n//gcd(n, h), gcd(n, h)) for h in others]
        domains = [range(min(g, 8//a, 8//b)+1) for a, b, g in ratios]
        exact = [0]*9
        for ts in product(*domains):
            total_assignments += 1
            s = sum(a*t for (a, b, g), t in zip(ratios, ts))
            k = sum(a*b*t*t for (a, b, g), t in zip(ratios, ts))
            if s <= 8 and k <= n+11:
                exact[s] |= 1 << k
        assert row_moments(n, others) == tuple(exact), (n, others)
    return dict(status='SANITY_PASS', artificial_row_cases=len(cases),
                complete_small_assignments=total_assignments,
                comparison='all reachable (row_sum,moment) pairs, not only selected diagonals')


class BudgetExpired(Exception):
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode', choices=('sanity', 'profile', 'full'), required=True)
    ap.add_argument('--input', type=Path, default=HERE/'component_large_size_screen.result.json')
    ap.add_argument('--cpu', type=int, default=1)
    ap.add_argument('--profile-per-c', type=int, default=32)
    args = ap.parse_args()
    assert args.profile_per_c > 0
    cpu0, wall0 = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {args.cpu})
    cpu_limit, wall_limit = {'sanity': (2, 5), 'profile': (5, 15), 'full': (60, 90)}[args.mode]
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
    if args.mode == 'sanity':
        result = sanity()
        result.update(cpu_seconds=time.process_time()-cpu0,
                      wall_seconds=time.monotonic()-wall0)
        print(json.dumps(result, indent=2))
        return

    def budget_check():
        reserve = min(3, cpu_limit/5)
        if time.process_time()-cpu0 >= cpu_limit-reserve:
            raise BudgetExpired('cpu')
        if time.monotonic()-wall0 >= wall_limit-3:
            raise BudgetExpired('wall')

    def wall_timeout(signum, frame):
        raise BudgetExpired('wall_hard')

    signal.signal(signal.SIGALRM, wall_timeout)
    signal.setitimer(signal.ITIMER_REAL, wall_limit)
    source = json.loads(args.input.read_text())
    assert source['complete'] and source['status'] == 'COMPLETE_NECESSARY_SIZE_SCREEN'
    assert source['totals']['capacity_trace'] == 25196
    assert {r['c']: len(r['survivors']) for r in source['rows']} == EXPECTED
    rows = []
    for input_row in source['rows']:
        c = input_row['c']
        selected = EXPECTED[c] if args.mode == 'full' else min(EXPECTED[c], args.profile_per_c)
        rows.append(dict(c=c, source_size_count=EXPECTED[c], selected_size_count=selected,
                         processed_sizes=0, row_moment_nonempty=0, trace_survivors=0,
                         input_diagonal_values=0, row_feasible_diagonal_values=0,
                         final_diagonal_values=0, cpu_seconds=0, survivors=[]))
    stopped = None
    try:
        for input_row, out in zip(source['rows'], rows):
            stage_cpu = time.process_time()
            try:
                for index, item in enumerate(input_row['survivors'][:out['selected_size_count']]):
                    budget_check()
                    sizes = tuple(item['sizes'])
                    domains = row_domains(sizes, item['diagonal_domains'], budget_check)
                    out['processed_sizes'] += 1
                    out['input_diagonal_values'] += sum(map(len, item['diagonal_domains']))
                    out['row_feasible_diagonal_values'] += sum(map(len, domains))
                    if not all(domains):
                        continue
                    out['row_moment_nonempty'] += 1
                    domains = trace_supported(domains, 8-(out['c']-1)//2)
                    if domains is None:
                        continue
                    out['trace_survivors'] += 1
                    out['final_diagonal_values'] += sum(map(len, domains))
                    out['survivors'].append(dict(source_index=index, sizes=sizes,
                                                diagonal_domains=domains))
            finally:
                out['cpu_seconds'] = time.process_time()-stage_cpu
    except BudgetExpired as exc:
        stopped = str(exc)
    totals = {k: sum(r[k] for r in rows) for k in
              ('source_size_count', 'selected_size_count', 'processed_sizes',
               'row_moment_nonempty', 'trace_survivors', 'input_diagonal_values',
               'row_feasible_diagonal_values', 'final_diagonal_values')}
    complete = stopped is None and totals['processed_sizes'] == totals['selected_size_count']
    if args.mode == 'full' and complete:
        assert totals['processed_sizes'] == 25196
    result = dict(
        status=('COMPLETE_NECESSARY_ROW_SCREEN' if args.mode == 'full' else 'COMPLETE_PROFILE')
               if complete else 'RESOURCE_LIMIT_PARTIAL',
        mode=args.mode, selected_input_complete=complete,
        full_input_complete=complete and args.mode == 'full', stopped=stopped,
        input_path=str(args.input), totals=totals, rows=rows,
        scope='Necessary individual-row and trace conditions only, not jointly compatible Q rows',
        diagonal_domains_mean='Each retained value has an individual row solution and participates in a retained trace assignment',
        not_checked=['shared t_ij compatibility between different rows',
                     'off-diagonal entries of Q^2+Q-11I=1*n^T',
                     'realization by adjacency and defect blocks'],
        row_cache=row_moments.cache_info()._asdict(),
        cpu_seconds=time.process_time()-cpu0, wall_seconds=time.monotonic()-wall0,
        resource_limits=dict(cpu_seconds=cpu_limit, wall_seconds=wall_limit,
                             cpu_affinity=[args.cpu], memory_bytes=4*1024**3))
    suffix = '.result.json' if args.mode == 'full' else '.profile.json'
    output = Path(__file__).with_suffix(suffix)
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    signal.setitimer(signal.ITIMER_REAL, 0)
    print(json.dumps({k: result[k] for k in ('status', 'totals', 'cpu_seconds', 'wall_seconds')}, indent=2))


if __name__ == '__main__':
    main()
