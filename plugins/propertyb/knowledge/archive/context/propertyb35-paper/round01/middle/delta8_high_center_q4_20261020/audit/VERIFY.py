"""Independent local q4 domain and old fixed-16-menu replay; CPU cap ten seconds."""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import Counter
from fractions import Fraction
from math import comb
import json, sys, time

P = Path(__file__).resolve().parent
ROOT = P.parents[5]
BASE = P.parent
START = time.process_time()
sys.dont_write_bytecode = True
sys.path[:0] = [str(ROOT/'context/propertyb34/round01/high-math'), str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows

def budget():
    assert time.process_time()-START < 10, 'ten CPU-second cutoff'

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

# Rebuild every threshold from the mathematical one-red/tree formula, not fails.
types = ('P', 0, 2, 3, 4)
threshold = {}
for sig in combinations_with_replacement(types, 4):
    fail = set()
    for a in range(31):
        values = []
        for r in range(17):
            exceptional = sum(0 if t == 'P' else C(11, r-5)+C(11, r)
                              if t == 0 else C(11+t, r) for t in sig)
            u = a*C(12, r-4)+(30-a)*C(12, r)-max(a-1, 0)*C(8, r-8)+exceptional
            values.append((Fraction(u, C(16, r)), r, u))
        if min(values)[0] >= 1:
            fail.add(a)
    threshold[sig] = fail
saved_threshold = json.loads((BASE.parent/'four_nonunit_degree_six_center_20261020/RESULT.json').read_text())
assert len(threshold) == 70
for z in saved_threshold['thresholds']:
    assert threshold[tuple(z['types'])] == set(z['fails'])
threshold_cpu = time.process_time()-START
budget()

# Incidence signatures recover the singleton attachments uniquely. Unlike root,
# enumerate all three degree roles for each common labeled trace multiset.
roles = [(14, 8, 8, 8, 8), (14, 9, 8, 8, 8), (15, 8, 8, 8, 8)]
jobs = {ds: {'degrees': ds, 'counts': Counter(), 'residual': []} for ds in roles}
allowed = [m for m in range(32) if m.bit_count() not in (1, 5)]
all_traces = list(combinations_with_replacement(allowed, 4))
assert len(allowed) == 26 and len(all_traces) == 23751
for tr in all_traces:
    h = tuple(sum(bool(m & (1 << v)) for m in tr) for v in range(5))
    cap = max(sum(bool(m & (1 << u)) and bool(m & (1 << v)) for m in tr)
              for u in range(5) for v in range(u))
    for ds, job in jobs.items():
        job['counts']['full_trace_labels'] += 1
        a = tuple(d-1-i for d, i in zip(ds, h))
        if sum(a) != 30 or min(a) < 0:
            continue
        job['counts']['exact_degree_sum'] += 1
        if cap > 3:
            continue
        job['counts']['pair_cap'] += 1
        signatures = [tuple(sorted(('P' if m & (1 << v) else m.bit_count() for m in tr),
                                   key=types.index)) for v in range(5)]
        if any(a[v] not in threshold[signatures[v]] for v in range(5)):
            job['counts']['anchor_strict'] += 1
        else:
            job['residual'].append({'traces': tr, 'attachments': a, 'degrees': ds})
for job in jobs.values():
    job['counts']['nonstrict'] = len(job['residual'])
saved = json.loads((BASE/'RESULT.json').read_text())
for job in jobs.values():
    rootjob = next(j for j in saved['jobs'] if tuple(j['degrees']) == job['degrees'])
    assert job['counts'] == rootjob['counts']
    assert {(tuple(r['traces']), tuple(r['attachments'])) for r in job['residual']} == {
        (tuple(r['traces']), tuple(r['attachments'])) for r in rootjob['residual']}
domain_cpu = time.process_time()-START-threshold_cpu
budget()

# Exactly the menu in FIVE_LOCK_FULL83.py; no new orders, permutations or grid.
old = json.loads((BASE.parent/'generic_quad_core_multiplicity_three_20261020/ACTUAL_A3_PARTITIONS.json').read_text())
end = sorted({tuple(z['positions']) for z in old['cases']})
central = [tuple(x for x in range(9, 15) if x != omit) for omit in range(9, 15)]
menu = sorted(set(central+end+[tuple(22-x for x in pos) for pos in end]))
assert len(end) == 5 and len(menu) == 16

cases = []
profile = None
for job in jobs.values():
    for z in job['residual']:
        ns = Counter({31: 1})
        ns.update(z['traces'])
        for v, a in enumerate(z['attachments']):
            ns[1 << v] += a
        assert sum(ns.values()) == 35
        assert tuple(sum(n for m, n in ns.items() if m & (1 << v)) for v in range(5)) == z['degrees']
        engine = SubsetEngine(21, 5, dict(ns))
        engine.inv = {pivot: (0, 0, []) for pivot in engine.inv}
        layouts = []
        first_start = time.process_time()
        primary_row_cache = {}
        for pos in menu:
            bypos = {k: 1 << v for v, k in enumerate(pos)}
            left = 0
            row_values = []
            for k in range(1, 22):
                pivot = bypos.get(k, 0)
                row_values.append(engine.value(k, left, pivot))
                left |= pivot
            value = Fraction(sum(row_values), engine.D)
            layouts.append({'positions': pos, 'bound': str(value), 'strict': value < 1})
            primary_row_cache[pos] = row_values
        if profile is None:
            profile = {'first_inventory_all16_primary_cpu': time.process_time()-first_start,
                       'remaining_inventory_count': 11}
        best = min(layouts, key=lambda x: Fraction(x['bound']))
        # Every best, strict or nonstrict, is independently expanded and replayed.
        masks = [m for m, n in ns.items() for _ in range(n)]
        stubs = [frozenset(v+1 for v in range(5) if m & (1 << v)) for m in masks]
        rows = independent_rows(21, tuple(best['positions']), stubs)
        replay = sum((min(r['A'], r['B'], r['C']) for r in rows), Fraction())
        assert replay == Fraction(best['bound'])
        for prim, row in zip(primary_row_cache[tuple(best['positions'])], rows):
            assert Fraction(prim, engine.D) == min(row['A'], row['B'], row['C'])
        cases.append(dict(**z, counts=dict(ns), all_35_masks=masks, all_layouts=layouts,
                          best=best, zero_quota=True, replay_bound=str(replay),
                          rows=[{k: str(v) if isinstance(v, Fraction) else v for k, v in r.items()} for r in rows]))
        budget()

result = {'status': 'COMPLETE_LOCAL_Q4_CHECK',
          'scope': 'H21/35 distinct5, actual edge F with Gamma degree4, specified F degrees, internal pair codegrees<=4. No other degree assumptions.',
          'review_independence': 'same-family', 'acceptance_status': 'provisional',
          'threshold_groups_independently_recomputed': 70, 'threshold_a': [0, 30], 'threshold_r': [0, 16],
          'full_trace_labels': 23751, 'jobs': [{**j, 'counts': dict(j['counts'])} for j in jobs.values()],
          'menu_source': 'three_nonunit_direct_repair_20261020/FIVE_LOCK_FULL83.py', 'menu': menu,
          'new_layouts_tested': 0, 'primary_profile': profile, 'cases': cases,
          'strict_tail_count': sum(z['best']['strict'] for z in cases),
          'remaining_tails': [z for z in cases if not z['best']['strict']],
          'replayed_original_edge_indices_per_inventory': 35, 'ordered_distinct_pairs_per_inventory': 1190,
          'replayed_position_rows': len(cases)*21, 'threshold_cpu': threshold_cpu, 'domain_cpu': domain_cpu,
          'cpu_seconds': time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k not in ('jobs', 'cases', 'remaining_tails', 'menu')}))
for z in cases:
    print(z['degrees'], z['traces'], z['attachments'], z['best'])
