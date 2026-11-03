"""Prepared bounded joint-quotient profile; root-managed review before launch.

Input: all 65 saved norm-screen survivors; profile the seven c=5/7 inputs,
or process only the other 58 in the separately selected remaining mode.
The new unresolved mode removes already completed sizes and applies only
the proved stabilizer column sorting to the 18 unfinished inputs.
Generate complete integer rows
online; enforce shared balanced interfaces, trace, and every matrix entry
of Q^2+Q-11I=1*n^T. A Q is an abstract quotient, not an actual graph.
The old profile/remaining modes enumerate labelled Q without symmetry. No n62
input or search is executed; its general row-compatibility idea is reused.
"""
import argparse
from functools import lru_cache
from itertools import permutations
from math import gcd
from pathlib import Path
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
EXPECTED = {5: 4, 7: 3, 9: 10, 11: 11, 13: 18, 15: 10, 17: 9}


class BudgetExpired(Exception):
    pass


class Budget:
    def __init__(self, cpu_seconds, wall_seconds):
        self.cpu0, self.wall0 = time.process_time(), time.monotonic()
        self.cpu_seconds, self.wall_seconds = cpu_seconds, wall_seconds
        self.ticks = 0

    def check(self, force=False):
        self.ticks += 1
        if force or self.ticks % 256 == 0:
            if time.process_time()-self.cpu0 >= self.cpu_seconds:
                raise BudgetExpired('cpu')
            if time.monotonic()-self.wall0 >= self.wall_seconds:
                raise BudgetExpired('wall')


def interface_options(ni, nj):
    g = gcd(ni, nj)
    a, b = nj//g, ni//g
    return tuple((a*t, b*t) for t in range(min(g, 8//a, 8//b)+1))


def new_stats():
    return dict(search_nodes=0, row_plans=0, suffix_states=0,
                row_generation_nodes=0, compatible_complete_rows=0)


class RowPlan:
    """Exact row moment count for MRV; stream rows with assigned-row tests."""
    def __init__(self, sizes, i, diagonal_domain, assigned, budget, stats,
                 canonical=False, all_domains=None):
        stats['row_plans'] += 1
        self.sizes, self.i = sizes, i
        self.budget, self.stats = budget, stats
        # An assigned row j also fixes column j by detailed balance.
        self.fixed = [(j, col[i], row[i]) for j, (row, col) in assigned.items()]
        self.constraints = [(j, tuple(row), tuple(col))
                            for j, (row, col) in assigned.items()]
        self.unknown = [(j, interface_options(sizes[i], sizes[j]))
                        for j in range(len(sizes)) if j != i and j not in assigned]
        self.unknown.sort(key=lambda item: (len(item[1]), item[0]))
        self.canonical_previous = {}
        if canonical:
            assert all_domains is not None
            last = {}
            fixed_order = sorted(assigned)
            for j, opts in self.unknown:
                key = (sizes[j], tuple(all_domains[j]),
                       tuple(assigned[k][0][j] for k in fixed_order))
                if key in last:
                    self.canonical_previous[j] = last[key]
                last[key] = j
            # Within one key, size and option count coincide. Thus the
            # existing unknown order visits its column indices increasingly.
        fixed_sum = sum(r for j, r, c in self.fixed)
        fixed_moment = sum(r*c for j, r, c in self.fixed)

        @lru_cache(maxsize=None)
        def ways(pos, left_sum, left_moment):
            stats['suffix_states'] += 1
            budget.check()
            if left_sum < 0 or left_moment < 0:
                return 0
            if pos == len(self.unknown):
                return int(left_sum == 0 and left_moment == 0)
            return sum(ways(pos+1, left_sum-r, left_moment-r*c)
                       for r, c in self.unknown[pos][1]
                       if r <= left_sum and r*c <= left_moment)

        self.ways = ways
        self.choices = []
        self.count = 0
        for d in diagonal_domain:
            s = 8-d-fixed_sum
            m = sizes[i]+11-d-d*d-fixed_moment
            count = ways(0, s, m)
            if count:
                self.choices.append((d, s, m))
                self.count += count

    def generate(self):
        n, i = len(self.sizes), self.i
        row, col = [0]*n, [0]*n
        for j, r, c in self.fixed:
            row[j], col[j] = r, c
        targets = tuple(self.sizes[j]-row[j] for j, rj, cj in self.constraints)
        for d, left_sum, left_moment in self.choices:
            row[i] = col[i] = d
            dots = tuple(d*cj[i]+sum(r*cj[k] for k, r, c in self.fixed)
                         for j, rj, cj in self.constraints)
            if any(x > target for x, target in zip(dots, targets)):
                continue

            def visit(pos, s, m, partial):
                self.stats['row_generation_nodes'] += 1
                self.budget.check()
                if not self.ways(pos, s, m):
                    return
                if pos == len(self.unknown):
                    if partial != targets:
                        return
                    # The reverse entries are mathematically redundant under
                    # balance, but this direct integer check clarifies direction.
                    for j, rj, cj in self.constraints:
                        if sum(rj[k]*col[k] for k in range(n))+rj[i] != self.sizes[i]:
                            return
                    self.stats['compatible_complete_rows'] += 1
                    yield tuple(row), tuple(col)
                    return
                j, options = self.unknown[pos]
                for r, c in options:
                    previous = self.canonical_previous.get(j)
                    if previous is not None and r < row[previous]:
                        self.stats['canonical_pruned_options'] = self.stats.get('canonical_pruned_options', 0)+1
                        continue
                    if r > s or r*c > m:
                        continue
                    updated = tuple(x+r*cj[j] for x, (a, rj, cj)
                                    in zip(partial, self.constraints))
                    if any(x > target for x, target in zip(updated, targets)):
                        continue
                    row[j], col[j] = r, c
                    yield from visit(pos+1, s-r, m-r*c, updated)
                row[j] = col[j] = 0

            yield from visit(0, left_sum, left_moment, dots)


def verify_q(sizes, domains, q):
    """Direct full-matrix arithmetic, separate from search/row recurrences."""
    n = len(sizes)
    assert all(len(row) == n and sum(row) == 8 for row in q)
    assert sum(q[i][i] for i in range(n)) == 8-(n-1)//2
    for i in range(n):
        assert q[i][i] in domains[i] and q[i][i] < sizes[i]
        assert sizes[i]*q[i][i] % 2 == 0
        for j in range(n):
            assert isinstance(q[i][j], int) and q[i][j] >= 0
            if i != j:
                assert q[i][j] <= sizes[j]
            assert sizes[i]*q[i][j] == sizes[j]*q[j][i]
            assert sum(q[i][k]*q[k][j] for k in range(n))+q[i][j]-11*(i == j) == sizes[j]


def matching_edge_marks(q):
    """Post-solution marks only; this lifting obstruction never prunes Q."""
    n = len(q)
    return [[i, j] for i in range(n) for j in range(i+1, n)
            if q[i][i] == q[j][j] == 1 and q[i][j] > 0 and
            all(q[i][k]*q[k][j] == 0 for k in range(n) if k not in (i, j))]


def enumerate_quotients(sizes, domains, budget, out, canonical=False):
    assigned, stats = {}, out['stats']
    trace = 8-(len(sizes)-1)//2

    def search(used_trace):
        stats['search_nodes'] += 1
        budget.check()
        if len(assigned) == len(sizes):
            if used_trace != trace:
                return
            q = [list(assigned[i][0]) for i in range(len(sizes))]
            verify_q(sizes, domains, q)
            out['models'].append(dict(Q=q, matching_edge_obstruction_pairs=matching_edge_marks(q)))
            return
        plans = []
        for i in range(len(sizes)):
            if i in assigned:
                continue
            plan = RowPlan(sizes, i, domains[i], assigned, budget, stats,
                           canonical=canonical, all_domains=domains)
            if plan.count == 0:
                return
            plans.append(plan)
        remaining_trace = trace-used_trace
        if remaining_trace < 0:
            return
        bits, mask = 1, (1 << (remaining_trace+1))-1
        for plan in plans:
            updated = 0
            for d, s, m in plan.choices:
                updated |= bits << d
            bits = updated & mask
        if not (bits >> remaining_trace) & 1:
            return
        chosen = min(plans, key=lambda p: (p.count, p.i))
        for row, col in chosen.generate():
            if used_trace+row[chosen.i] > trace:
                continue
            assigned[chosen.i] = (row, col)
            search(used_trace+row[chosen.i])
            del assigned[chosen.i]

    search(0)


def sanity(budget):
    # Check only these given models and their row generation; no old
    # classification or new input-domain enumeration is run here.
    cases = [((12, 21, 28), [[1, 0, 7], [0, 4, 4], [3, 3, 2]]),
             ((6, 25, 30), [[3, 0, 5], [0, 2, 6], [1, 5, 2]]),
             ((2, 5, 6, 18, 30), [[0, 5, 3, 0, 0], [2, 0, 0, 0, 6],
               [1, 0, 1, 6, 0], [0, 0, 2, 1, 5], [0, 1, 0, 3, 4]]),
             ((3, 3, 15, 15, 25), [[0, 3, 5, 0, 0], [3, 0, 0, 5, 0],
               [1, 0, 2, 0, 5], [0, 1, 0, 2, 5], [0, 0, 3, 3, 2]])]
    generated_rows = 0
    for sizes, q in cases:
        domains = [[q[i][i]] for i in range(len(sizes))]
        verify_q(sizes, domains, q)
        assigned = {}
        for i in range(len(sizes)):
            plan = RowPlan(sizes, i, domains[i], assigned, budget, new_stats())
            rows = list(plan.generate())
            generated_rows += len(rows)
            target = (tuple(q[i]), tuple(q[j][i] for j in range(len(sizes))))
            assert target in rows
            assigned[i] = target
    return dict(status='SANITY_PASS', given_quotients=len(cases),
                actual_generated_rows=generated_rows,
                checked='full integer identity and known-row retention through shared-interface/offdiagonal tests')


def symmetry_sanity(budget):
    """Only the two known c=5 size domains, now using the canonical search."""
    cases = [((2, 5, 6, 18, 30), [[0, 5, 3, 0, 0], [2, 0, 0, 0, 6],
               [1, 0, 1, 6, 0], [0, 0, 2, 1, 5], [0, 1, 0, 3, 4]]),
             ((3, 3, 15, 15, 25), [[0, 3, 5, 0, 0], [3, 0, 0, 5, 0],
               [1, 0, 2, 0, 5], [0, 1, 0, 2, 5], [0, 0, 3, 3, 2]])]
    records = []
    for sizes, target in cases:
        domains = [[target[i][i]] for i in range(len(sizes))]
        verify_q(sizes, domains, target)
        out = dict(stats=new_stats(), models=[])
        enumerate_quotients(sizes, domains, budget, out, canonical=True)
        allowed = [p for p in permutations(range(len(sizes)))
                   if all(sizes[p[i]] == sizes[i] and domains[p[i]] == domains[i]
                          for i in range(len(sizes)))]
        matched = []
        for model in out['models']:
            q = model['Q']
            if any(all(q[i][j] == target[p[i]][p[j]]
                       for i in range(len(sizes)) for j in range(len(sizes)))
                   for p in allowed):
                matched.append(q)
        assert matched, sizes
        records.append(dict(sizes=sizes, representative_models=len(out['models']),
                            known_isomorphism_class_retained=True,
                            matching_representative=matched[0], stats=out['stats']))
    return dict(status='SYMMETRY_SANITY_PASS', cases=records,
                scope='Two known c5 examples; no old c3 enumeration')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode', choices=('sanity', 'profile', 'remaining',
                                      'symmetry-sanity', 'unresolved'), required=True)
    ap.add_argument('--input', type=Path, default=HERE/'component_norm_screen.result.json')
    ap.add_argument('--cpu', type=int, default=1)
    args = ap.parse_args()
    os.sched_setaffinity(0, {args.cpu})
    cap = {'sanity': 2, 'symmetry-sanity': 2, 'profile': 10,
           'remaining': 60, 'unresolved': 60}[args.mode]
    resource.setrlimit(resource.RLIMIT_CPU, (cap, cap))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
    budget = Budget(cap-(3 if args.mode in ('remaining', 'unresolved') else 1),
                    {'sanity': 4, 'symmetry-sanity': 4, 'profile': 18,
                     'remaining': 73, 'unresolved': 73}[args.mode])
    if args.mode in ('sanity', 'symmetry-sanity'):
        result = sanity(budget) if args.mode == 'sanity' else symmetry_sanity(budget)
        result.update(cpu_seconds=time.process_time()-budget.cpu0,
                      wall_seconds=time.monotonic()-budget.wall0)
        print(json.dumps(result, indent=2))
        return
    source = json.loads(args.input.read_text())
    assert source['complete'] and source['status'] == 'COMPLETE_NECESSARY_NORM_SCREEN'
    assert source['surviving_sizes'] == 65
    assert {row['c']: len(row['survivors']) for row in source['rows']} == EXPECTED
    canonical = args.mode == 'unresolved'
    previous_complete, previous_sources = set(), []
    if canonical:
        all_sizes = {tuple(item['sizes']) for row in source['rows'] for item in row['survivors']}
        for name, expected_complete in (('profile', 7), ('remaining', 40)):
            path = Path(__file__).with_suffix('.'+name+'.json')
            report = json.loads(path.read_text())
            complete = {tuple(item['sizes']) for item in report['items']
                        if item['enumeration_complete']}
            assert len(complete) == expected_complete and complete <= all_sizes
            previous_complete.update(complete)
            previous_sources.append(str(path))
        assert len(previous_complete) == 47 and len(all_sizes-previous_complete) == 18
    selected_components = [5, 7] if args.mode == 'profile' else [9, 11, 13, 15, 17]
    selected_count = 7 if args.mode == 'profile' else 58
    items = [dict(c=row['c'], selected_for_run=(tuple(item['sizes']) not in previous_complete)
                  if canonical else row['c'] in selected_components,
                  source_index=item['source_index'], sizes=item['sizes'],
                  diagonal_domains=item['diagonal_domains'], status='NOT_STARTED',
                  enumeration_complete=False, models=[], stats=new_stats(), cpu_seconds=0)
             for row in source['rows'] for item in row['survivors']]
    if canonical:
        selected_count = 18
        selected_components = sorted({item['c'] for item in items if item['selected_for_run']})
        assert sum(item['selected_for_run'] for item in items) == selected_count
    stopped = None
    for item in items:
        if not item['selected_for_run']:
            continue
        start = time.process_time()
        try:
            budget.check(force=True)
            enumerate_quotients(tuple(item['sizes']), item['diagonal_domains'], budget, item,
                               canonical=canonical)
            item['enumeration_complete'] = True
            item['status'] = 'MODEL' if item['models'] else 'EXHAUSTED_NO_MODEL'
        except BudgetExpired as exc:
            stopped = str(exc)
            item['status'] = 'MODEL' if item['models'] else 'UNKNOWN_BUDGET'
        finally:
            item['cpu_seconds'] = time.process_time()-start
        if stopped:
            break
    completed = sum(x['enumeration_complete'] for x in items)
    models = sum(len(x['models']) for x in items)
    unmarked = sum(not model['matching_edge_obstruction_pairs']
                   for item in items for model in item['models'])
    complete_status = ('COMPLETE_SELECTED_PROFILE' if args.mode == 'profile'
                       else 'COMPLETE_REMAINING_QUOTIENT_ENUMERATION')
    if canonical:
        complete_status = 'COMPLETE_UNRESOLVED_UP_TO_STABILIZER_SYMMETRY'
    result = dict(status=complete_status if completed == selected_count else 'BOUNDED_ENUMERATION_PARTIAL',
                  mode=args.mode, input_sizes=65, selected_sizes=selected_count,
                  selected_components=selected_components,
                  selected_input_complete=completed == selected_count, full_input_complete=False,
                  input_path=str(args.input), sizes_completed=completed,
                  models_without_matching_edge_mark=unmarked,
                  stopped=stopped, items=items,
                  scope='Only the selected component counts; abstract Q, not an adjacency/defect lift or isomorphism classification',
                  model_status_mean='At least one model; enumeration_complete separately states whether all models for these sizes were exhausted',
                  matching_marks='Post-model diagnostic only, never a search pruning rule',
                  cpu_seconds=time.process_time()-budget.cpu0,
                  wall_seconds=time.monotonic()-budget.wall0,
                  cpu_affinity=[args.cpu], os_cpu_limit_seconds=cap,
                  voluntary_cpu_limit_seconds=budget.cpu_seconds,
                  voluntary_wall_limit_seconds=budget.wall_seconds,
                  prescribed_external_wall_limit_seconds=20 if args.mode == 'profile' else 75)
    model_count_key = 'representative_models' if canonical else 'labelled_models'
    result[model_count_key] = models
    if canonical:
        result.update(canonical=True, previous_complete_sizes=47,
                      previous_completion_sources=previous_sources,
                      combined_input_coverage_complete=completed == 18,
                      scope='Exactly 18 previously unfinished size domains, retaining at least one representative of each size/domain-preserving isomorphism class; abstract Q only',
                      symmetry='Nondecreasing current-row entries only within equal size, full diagonal domain and assigned-row column signature',
                      enumeration_count_scope='Representatives may still contain isomorphic duplicates; counts are neither labelled totals nor isomorphism-class totals')
    suffix = {'profile': '.profile.json', 'remaining': '.remaining.json',
              'unresolved': '.unresolved.json'}[args.mode]
    Path(__file__).with_suffix(suffix).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'sizes_completed', model_count_key,
          'models_without_matching_edge_mark', 'cpu_seconds', 'wall_seconds')}, indent=2))


if __name__ == '__main__':
    main()
