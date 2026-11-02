import csv
import itertools
import json
import resource
import time
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
started = time.process_time()
preparation_charge = 0.1  # Conservative CPU allowance for creating this small batch.
HERE = Path(__file__).resolve().parent
CASE = HERE.parent
prior = json.loads((CASE / 'sector_matching_extension/TERMINAL.json').read_text())
data = json.loads((CASE / 'sector_matching_extension/ORDER7_GENERATOR_AND_ORBITS.json').read_text())
fixed = sorted(o[0] for o in data['orbits'] if len(o) == 1)
orbits = [set(o) for o in data['orbits'] if len(o) == 7]
adj = [set() for _ in range(106)]
lines = (CASE / 'source106.header.edges').read_text().splitlines()
for line in lines[1:]:
    a, b = map(int, line.split())
    adj[a].add(b)
    adj[b].add(a)

records = []
orbit_profiles = []
for orbit in orbits:
    r = {len(adj[u] & orbit) for u in orbit}
    k = {len(adj[u] & set(fixed)) for u in orbit}
    assert len(r) == len(k) == 1
    r, k = next(iter(r)), next(iter(k))
    orbit_profiles.append(dict(representative=min(orbit), vertices=sorted(orbit),
                               r=r, k=k,
                               closed_neighborhood=len(orbit.union(*(adj[u] for u in orbit)))))
    for q in (3, 4):
        for chosen in itertools.combinations(fixed, q):
            pins = orbit | set(chosen)
            closed = pins.union(*(adj[u] for u in pins))
            h_values = {len(adj[u] & set(chosen)) for u in orbit}
            assert len(h_values) == 1
            h = next(iter(h_values))
            row = dict(orbit=min(orbit), fixed=' '.join(map(str, chosen)),
                       pins=len(pins), r=r, k=k, h=h, covered=len(closed),
                       union_upper=92 + 7*q - 7*(r+k+h),
                       reason='', witness='')
            assert len(closed) <= row['union_upper']
            if len(closed) != 106:
                row.update(reason='NOT_CLOSED_DOMINATING',
                           witness=str(min(set(range(106)) - closed)))
            else:
                cross = {u: len(adj[u] - pins) for u in pins}
                over = [u for u in pins if cross[u] + 1 > 11]
                if over:
                    row.update(reason='FROZEN_CROSS_PLUS_Z_OVER11', witness=str(min(over)))
                else:
                    zero = {u for u in pins if cross[u] + 1 == 11}
                    impossible = [u for u in pins
                                  if cross[u] + 1 + len(pins - {u} - zero) < 10]
                    if impossible:
                        u = min(impossible)
                        row.update(reason='FORCED_ZERO_INTERNAL_NEIGHBORS_BELOW_MIN10',
                                   witness=f'{u};maxdegree={cross[u]+1+len(pins-{u}-zero)}')
                    else:
                        row.update(reason='UNRESOLVED_PASSES_NECESSARY_GATE')
            records.append(row)

with (HERE / 'ALL1764_PINSET_GATES.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=list(records[0]))
    writer.writeheader()
    writer.writerows(records)
counts = Counter(row['reason'] for row in records)
by_size = {n: dict(Counter(row['reason'] for row in records if row['pins'] == n))
           for n in (10, 11)}
elapsed = time.process_time() - started
assert elapsed + preparation_charge < 2
result = dict(status='PREDICTION_SUPPORTED_NO_INVARIANT_PINSET_PASSES_NECESSARY_GATES'
              if not counts['UNRESOLVED_PASSES_NECESSARY_GATE'] else 'PREDICTION_NOT_ESTABLISHED',
              pinsets=len(records), by_failure=dict(counts), by_size=by_size,
              orbit_profiles=orbit_profiles,
              unresolved=sum(row['reason'] == 'UNRESOLVED_PASSES_NECESSARY_GATE' for row in records),
              internal_rewiring_need_not_preserve_C7=True,
              prediction_test='closed domination plus fixed-edge/forced-zero degree conditions',
              source_diameter_or_common_neighbor_or_automorphism_rechecks=0,
              graph_BFS=0, solver=0, rewiring_enumeration=0,
              new_graph_or_Lean_count_increment=0,
              batch_CPU_seconds=elapsed,
              preparation_CPU_charge=preparation_charge,
              preparation_charge_is_conservative_not_a_measurement=True,
              prior_case_CPU_seconds=prior['case_CPU_seconds'],
              case_CPU_seconds=prior['case_CPU_seconds'] + preparation_charge + elapsed,
              batch_CPU_budget_seconds=2, case_CPU_budget_seconds=20)
(HERE / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
elapsed = time.process_time() - started
terminal = dict(status=result['status'], running=False,
                prior_case_CPU_seconds=prior['case_CPU_seconds'],
                batch_CPU_seconds=elapsed,
                preparation_CPU_charge=preparation_charge,
                case_CPU_seconds=prior['case_CPU_seconds'] + preparation_charge + elapsed,
                batch_CPU_budget_seconds=2, case_CPU_budget_seconds=20)
(HERE / 'TERMINAL.json').write_text(json.dumps(terminal, indent=2) + '\n')
print(json.dumps(dict(status=result['status'], pinsets=len(records),
                      by_failure=dict(counts), by_size=by_size,
                      batch_CPU_seconds=elapsed, case_CPU_seconds=terminal['case_CPU_seconds'])))
