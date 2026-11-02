"""Only quotient/formal-path capacities for the three specified reflection families.

No translation assignment is evaluated.  The entire run has a 30 CPU second
hard limit and stops starting new skeletons at 28 CPU seconds.
"""
from pathlib import Path
from math import gcd
from collections import Counter
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
CASES = [(13, 28, 5), (17, 24, 2), (29, 12, 12)]


def canonical(beta, s, t, m, units, both):
    images = []
    for k in units:
        b = (k * beta) % m
        b = min(b, (-b) % m)
        for sign in ([1, -1] if both else [1]):
            for anchor in (0, s, t):
                cross = sorted((sign * k * (q - anchor)) % m for q in (0, s, t))
                cross.remove(0)
                images.append((b, *cross))
    return min(images)


def capacities(p, m, r, kind, beta, sigma, tau):
    h = m // 2
    power = [pow(r, k, p) for k in range(m)]
    variables = 3 if kind == 'mixed' else 4
    zero = (0,) * (variables + 1)
    def basis(i):
        return tuple(int(k == i) for k in range(variables + 1))
    def inverse(form, q):
        return tuple((-power[-q % m] * z) % p for z in form), (-q) % m
    # Dart, inverse dart, destination layer, quotient, affine translation form.
    steps = [[('a0', 'a0', 0, h, zero), ('a1', 'a1', 0, h, basis(0))], []]
    if kind == 'mixed':
        b = basis(1)
        bi, qi = inverse(b, beta)
        steps[1] = [('bp', 'bm', 1, beta, b), ('bm', 'bp', 1, qi, bi)]
        cross = [(zero, 0), (basis(2), sigma), (basis(3), tau)]
    else:
        steps[1] = [('b0', 'b0', 1, h, basis(1)), ('b1', 'b1', 1, h, basis(2))]
        cross = [(zero, 0), (basis(3), sigma), (basis(4), tau)]
    for i, (form, q) in enumerate(cross):
        inv, qi = inverse(form, q)
        name = f'c{i}'
        steps[0].append((name, name, 1, q, form))
        steps[1].append((name, name, 0, qi, inv))
    roots = []
    for root in (0, 1):
        forms = [[set() for _ in range(m)] for _ in range(2)]
        walks = [[0] * m for _ in range(2)]
        def visit(layer, q, form, forbidden, depth):
            forms[layer][q].add(form)
            walks[layer][q] += 1
            if depth == 5:
                return
            for name, reverse, dest, voltage, linear in steps[layer]:
                if name == forbidden:
                    continue
                newform = tuple((a + power[q] * b) % p for a, b in zip(form, linear))
                visit(dest, (q + voltage) % m, newform, reverse, depth + 1)
        visit(root, 0, zero, None, 0)
        assert sum(map(sum, walks)) == 1706
        distinct = [[len(cell) for cell in row] for row in forms]
        roots.append(dict(root=root, nonbacktracking_walk_counts=walks,
                          distinct_affine_forms=distinct,
                          minimum_walks=min(map(min, walks)),
                          minimum_distinct=min(map(min, distinct)),
                          deficient_cells=[[side, q, distinct[side][q]]
                                           for side in range(2) for q in range(m)
                                           if distinct[side][q] < p]))
    cross = ((p - 1) * (p - 2) if sigma == tau == 0 else
             p * (p - 1) if sigma == 0 or sigma == tau else p * p)
    internal = ((p - 1 if beta == 0 else p) if kind == 'mixed' else p * (p - 1))
    return dict(kind=kind, quotient=[beta, sigma, tau], roots=roots,
                passes_walk_capacity=all(row['minimum_walks'] >= p for row in roots),
                passes_form_capacity=all(row['minimum_distinct'] >= p for row in roots),
                minimum_distinct=min(row['minimum_distinct'] for row in roots),
                raw_translation_assignments=p ** variables,
                legal_translation_assignments=cross * internal)


def main():
    started = time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    if hasattr(os, 'sched_getaffinity'):
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    cases = []
    for p, m, r in CASES:
        order = next(d for d in range(1, m + 1) if pow(r, d, p) == 1)
        h = m // 2
        assert m % order == 0 and pow(r, h, p) == p - 1
        units = [k for k in range(1, m) if gcd(k, m) == 1 and pow(r, k, p) == r]
        assert all(k % order == 1 and (k * h) % m == h for k in units)
        case = dict(p=p, m=m, r=r, h=h, action_order=order, n=2*p*m,
                    compatible_quotient_units=units, branches={})
        for kind in ('mixed', 'both'):
            raw = []
            for beta in (range(h) if kind == 'mixed' else [h]):
                for s in range(m):
                    for t in range(s, m):
                        if gcd(gcd(gcd(m, h), beta), gcd(s, t)) == 1:
                            raw.append((beta, s, t))
            anchored = sorted({canonical(*q, m, [1], False) for q in raw})
            sided = sorted({canonical(*q, m, [1], kind == 'both') for q in raw})
            rows = sorted({canonical(*q, m, units, kind == 'both') for q in raw})
            # Each canonical image still satisfies the declared raw contract;
            # these checks do not evaluate a translation assignment.
            raw_set = set(raw)
            assert all(q in raw_set for q in rows)
            assert all(canonical(*q, m, units, kind == 'both') == q for q in rows)
            case['branches'][kind] = dict(raw_connected_quotients=[list(q) for q in raw],
                after_cross_anchoring=len(anchored), after_allowed_side_swap=len(sided),
                canonical_quotients=[list(q) for q in rows], records=[],
                translation_variables=3 if kind == 'mixed' else 4)
        cases.append(case)
    exhausted = False
    cursor = None
    for case_index, case in enumerate(cases):
        for kind in ('mixed', 'both'):
            branch = case['branches'][kind]
            for row_index, q in enumerate(branch['canonical_quotients']):
                if time.process_time() - started >= 28.0:
                    exhausted = True
                    cursor = dict(case_index=case_index, kind=kind, canonical_row_index=row_index,
                                  quotient=q)
                    break
                branch['records'].append(capacities(case['p'], case['m'], case['r'], kind, *q))
            if exhausted:
                break
        if exhausted:
            break
    compact = []
    for case in cases:
        summary = {k: case[k] for k in ('p', 'm', 'r', 'n', 'action_order', 'compatible_quotient_units')}
        summary['branches'] = {}
        for kind, branch in case['branches'].items():
            records = branch['records']
            survivors = [row for row in records if row['passes_form_capacity']]
            branch['status'] = ('COMPLETE' if len(records) == len(branch['canonical_quotients'])
                                else 'PARTIAL' if records else 'NOT_STARTED')
            branch['summary'] = dict(status=branch['status'],
                raw_connected_quotients=len(branch['raw_connected_quotients']),
                after_cross_anchoring=branch['after_cross_anchoring'],
                after_allowed_side_swap=branch['after_allowed_side_swap'],
                canonical_quotients=len(branch['canonical_quotients']), processed_quotients=len(records),
                walk_capacity_survivors=sum(row['passes_walk_capacity'] for row in records),
                affine_form_capacity_survivors=len(survivors),
                survivor_quotients=[row['quotient'] for row in survivors],
                minimum_distinct_histogram=dict(sorted(Counter(row['minimum_distinct'] for row in records).items())),
                raw_assignments_per_quotient=case['p'] ** branch['translation_variables'],
                survivor_raw_translation_assignments=sum(row['raw_translation_assignments'] for row in survivors),
                survivor_legal_translation_assignments=sum(row['legal_translation_assignments'] for row in survivors))
            summary['branches'][kind] = branch['summary']
            if branch['status'] == 'COMPLETE':
                name = f"p{case['p']}_m{case['m']}_r{case['r']}_{kind}_skeletons.txt"
                (HERE / name).write_text(str(len(survivors)) + '\n' +
                    ''.join(' '.join(map(str, row['quotient'])) + '\n' for row in survivors))
        compact.append(summary)
    result = dict(scope='Only three specified groups; quotient and formal-path capacity, no translation search',
                  status='PARTIAL_BUDGET' if exhausted else 'COMPLETE', cursor=cursor,
                  cpu_seconds=time.process_time()-started, summary=compact, cases=cases)
    (HERE / 'capacity_results.json').write_text(json.dumps(result, indent=2) + '\n')
    terminal = dict(status=result['status'], cursor=cursor, summary=compact,
                    cpu_seconds_before_serialization=result['cpu_seconds'],
                    total_cpu_seconds=time.process_time()-started)
    (HERE / 'terminal.json').write_text(json.dumps(terminal, indent=2) + '\n')
    print(json.dumps(terminal, indent=2))


if __name__ == '__main__':
    main()
