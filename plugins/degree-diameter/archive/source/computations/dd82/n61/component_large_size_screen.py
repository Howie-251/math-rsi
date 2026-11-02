"""Exact necessary size screen; its complete result is saved alongside this source.

Generate the previously counted 36,143 sorted size multisets. Check
integer spectral diagonal bounds and handshake; exact trace feasibility;
connected diameter-two possible interface support; and row capacity.
Interface caps include q_ij<=n_j and q_ji<=n_i, equivalently t_ij<=gcd(n_i,n_j).
Survivors have only necessary conditions, not a realized quotient.
Completed once; do not rerun merely to recover its saved result.
"""
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path
import json
import os
import resource
import time

from component_large_size_domain import allowed_size

EXPECTED = {5: 1026, 7: 4443, 9: 8331, 11: 9070,
            13: 6918, 15: 4188, 17: 2167}
STAGES = ('input_sizes', 'nonempty_spectral_diagonals', 'spectral_trace',
          'possible_support_connected', 'possible_support_diameter_two',
          'nonempty_capacity_diagonals', 'capacity_trace')


def size_tuples(values, c):
    """Sorted tuples, each once, using only sum/minimum/maximum pruning."""
    def visit(start, left, total, prefix):
        if left == 0:
            if total == 0:
                yield prefix
            return
        if total < left*values[start] or total > left*values[-1]:
            return
        for j in range(start, len(values)):
            n = values[j]
            if left*n > total:
                break
            if total-n <= (left-1)*values[-1]:
                yield from visit(j, left-1, total-n, prefix+(n,))
    yield from visit(0, c, 61, ())


def trace_supported(domains, target):
    """Keep exactly values participating in some allowed trace assignment."""
    mask = (1 << (target+1))-1
    prefix = [1]
    for domain in domains:
        v = 0
        for d in domain:
            v |= prefix[-1] << d
        prefix.append(v & mask)
    if not (prefix[-1] >> target) & 1:
        return None
    suffix = [0]*(len(domains)+1)
    suffix[-1] = 1
    for i in range(len(domains)-1, -1, -1):
        for d in domains[i]:
            suffix[i] |= suffix[i+1] << d
        suffix[i] &= mask
    return [[d for d in domain if any(
        ((prefix[i] >> a) & 1) and
        ((suffix[i+1] >> (target-d-a)) & 1)
        for a in range(target-d+1))]
        for i, domain in enumerate(domains)]


def support_checks(adj):
    """Return connected, diameter<=2 for a bitset simple supergraph."""
    allbits = (1 << len(adj))-1
    seen, todo = 1, 1
    while todo:
        bit = todo & -todo
        todo ^= bit
        new = adj[bit.bit_length()-1] & ~seen
        seen |= new
        todo |= new
    if seen != allbits:
        return False, False
    for i, neighbors in enumerate(adj):
        covered, todo = neighbors | (1 << i), neighbors
        while todo:
            bit = todo & -todo
            todo ^= bit
            covered |= adj[bit.bit_length()-1]
        if covered != allbits:
            return True, False
    return True, True


def main():
    cpu0, wall0 = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {1})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
    values_all = [n for n in range(2, 49) if allowed_size(n)]
    diagonal = {n: [d for d in range(min(8, n-1)+1)
                    if n*d % 2 == 0 and
                    (122*d-17*n+61)**2 <= 45*(61-n)**2]
                for n in values_all}
    cap, cap_records = {}, []
    for a, b in combinations_with_replacement(values_all, 2):
        g = gcd(a, b)
        # Balance gives q_ab=(b/g)*t, q_ba=(a/g)*t. Simplicity
        # gives t<=g; both row-eight bounds give the other two caps.
        tmax = min(g, 8*g//a, 8*g//b)
        ab, ba = b//g*tmax, a//g*tmax
        cap[a, b], cap[b, a] = (tmax, ab, ba), (tmax, ba, ab)
        cap_records.append([a, b, tmax, ab, ba])
    rows, complete = [], True
    for c, expected in EXPECTED.items():
        trace = 8-(c-1)//2
        maximum = 8*(65-2*c)//9
        values = [n for n in values_all if n <= maximum]
        counts = dict.fromkeys(STAGES, 0)
        survivors = []
        row = dict(c=c, expected_input_sizes=expected, counts=counts,
                   trace=trace, maximum_size=maximum, complete=False,
                   survivors=survivors)
        rows.append(row)
        for sizes in size_tuples(values, c):
            if counts['input_sizes'] % 64 == 0 and time.process_time()-cpu0 >= 9:
                complete = False
                break
            counts['input_sizes'] += 1
            domains = [diagonal[n] for n in sizes]
            if not all(domains):
                continue
            counts['nonempty_spectral_diagonals'] += 1
            domains = trace_supported(domains, trace)
            if domains is None:
                continue
            counts['spectral_trace'] += 1
            adj, capacity = [0]*c, [0]*c
            for i in range(c):
                for j in range(i+1, c):
                    tmax, ij, ji = cap[sizes[i], sizes[j]]
                    capacity[i] += ij
                    capacity[j] += ji
                    if tmax:
                        adj[i] |= 1 << j
                        adj[j] |= 1 << i
            connected, diameter_two = support_checks(adj)
            if not connected:
                continue
            counts['possible_support_connected'] += 1
            if not diameter_two:
                continue
            counts['possible_support_diameter_two'] += 1
            domains = [[d for d in ds if 8-d <= capacity[i]]
                       for i, ds in enumerate(domains)]
            if not all(domains):
                continue
            counts['nonempty_capacity_diagonals'] += 1
            domains = trace_supported(domains, trace)
            if domains is None:
                continue
            counts['capacity_trace'] += 1
            survivors.append(dict(sizes=sizes, diagonal_domains=domains,
                                   row_off_capacity=capacity))
        if not complete:
            break
        assert counts['input_sizes'] == expected, (c, counts)
        row['complete'] = True
    totals = {stage: sum(r['counts'][stage] for r in rows) for stage in STAGES}
    if complete:
        assert totals['input_sizes'] == 36143
    result = dict(
        status='COMPLETE_NECESSARY_SIZE_SCREEN' if complete else 'CPU_LIMIT_PARTIAL',
        complete=complete, expected_total_input_sizes=36143,
        scope='Necessary size/diagonal domains only; no Q matrix search or graph realization',
        stage_counts_are_cumulative=True, totals=totals, rows=rows,
        interface_caps_format=['size_a', 'size_b', 'tmax', 'q_ab_max', 'q_ba_max'],
        interface_caps_by_sizes=cap_records,
        diagonal_domains_mean='Each value participates in some trace assignment after row-capacity filtering',
        not_checked=['joint interface choices or row sums',
                     'matrix polynomial Q^2+Q-11I=1*n^T', 'graph realization'],
        algorithm_cpu_seconds=time.process_time()-cpu0,
        algorithm_wall_seconds=time.monotonic()-wall0,
        cpu_affinity=[1], cpu_soft_limit_seconds=10, voluntary_stop_cpu_seconds=9)
    Path(__file__).with_suffix('.result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'totals',
          'algorithm_cpu_seconds', 'algorithm_wall_seconds')}, indent=2))


if __name__ == '__main__':
    main()
