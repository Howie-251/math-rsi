"""One pass through the frozen53 unattempted star pinsets on the changing base."""
from collections import Counter
from pathlib import Path
import json
import resource
import subprocess
import time

OUT = Path(__file__).resolve().parent
PARENT = OUT.parent
BASE = PARENT.parent
ROOT = BASE.parents[3]
START = time.process_time()
CHILD = resource.getrusage(resource.RUSAGE_CHILDREN)
BUDGET = 20.0
CARRIED_CPU = 0.0


def cpu():
    c = resource.getrusage(resource.RUSAGE_CHILDREN)
    return CARRIED_CPU + time.process_time() - START + c.ru_utime + c.ru_stime - CHILD.ru_utime - CHILD.ru_stime


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + '\n')


def rel(path):
    return str(path.relative_to(ROOT))


def main():
    global CARRIED_CPU
    assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_REMAINING53_CURRENT_BASE_BATCH'
    previous = None
    if (OUT / 'RESULT.json').exists():
        previous = json.loads((OUT / 'RESULT.json').read_text())
        assert previous['status'] == 'ACCEPT16_LIMIT_STOP'
        assert (OUT / 'RESUME_SCOPE.json').exists()
        CARRIED_CPU = previous['additional_parent_children_CPU_seconds']
    frozen = json.loads((OUT / 'frozen_remaining53.json').read_text())['records']
    assert len(frozen) == 53 and [r['ordinal'] for r in frozen] == list(range(38, 91))
    receipt = json.loads((PARENT / 'independent_newroot51418.json').read_text())
    assert receipt['n'] == 51418 and receipt['maximum_degree'] == 13
    assert receipt['new_root_eccentricity'] == 5 and receipt['all_source_edges_retained']
    first = json.loads((PARENT / 'first_hit.json').read_text())
    degree = list((BASE / 'degree13.u8.bin').read_bytes())
    for p in first['full_neighbor_set']:
        degree[p] += 1
    degree.append(len(first['full_neighbor_set']))
    assert len(degree) == 51418 and max(degree) == 13
    native = PARENT / 'cover'
    assert native.exists() and (PARENT / 'cover.cpp').read_text().count('assert(DEG==13);') == 1
    current = PARENT / 'graph_d13_D5_n51418.edges'
    n, m = 51418, 324461
    (OUT / 'items').mkdir(exist_ok=True)
    (OUT / 'graphs').mkdir(exist_ok=True)
    rows, accepted, calls = [], [], 0
    if previous:
        rows = previous['rows']
        accepted = previous['records']
        calls = previous['native_calls']
        assert [r['ordinal'] for r in rows] == list(range(38, 38 + len(rows)))
        for oldstep in accepted:
            assert oldstep['actual_base_n'] == n and oldstep['actual_base_m'] == m
            assert oldstep['actual_complete_current_R4_missing'] == 0
            for p in oldstep['full_neighbor_set']:
                degree[p] += 1
            degree.append(len(oldstep['full_neighbor_set']))
            n, m = oldstep['new_n'], oldstep['new_m']
            current = ROOT / oldstep['graph_file']
        assert n == previous['final_n'] and m == previous['final_m']
        frozen = frozen[len(rows):]
    status = 'ALL53_FROZEN_ITEMS_TERMINAL'
    for item in frozen:
        pins = item['mandatory_pins']
        row = {**item, 'frozen_source_n': 51417, 'frozen_source_m': 324451,
               'source_n': n, 'source_m': m, 'actual_base_n': n, 'actual_base_m': m,
               'actual_source_graph': rel(current),
               'prior_continuation_acceptances': len(accepted)}
        blocked = [p for p in pins if degree[p] >= 13]
        if blocked:
            row.update(status='CURRENT_DEGREE_BLOCKED', saturated_mandatory_pins=blocked)
            rows.append(row)
            continue
        if BUDGET - cpu() < 7.5:
            status = 'ADDITIONAL_CPU_RESERVE_STOP'
            break
        prefix = OUT / 'items' / f'ord{item["ordinal"]:03d}_v{item["prototype"]}_n{n}'
        pinfile = Path(str(prefix) + '.pins.txt')
        pinfile.write_text(' '.join(map(str, pins)) + '\n')
        with Path(str(prefix) + '.log').open('w') as log:
            ret = subprocess.run([str(native), 'prepare', str(current), str(pinfile), str(prefix), '13'], stdout=log, stderr=log, timeout=15)
        calls += 1
        if ret.returncode:
            row.update(status='UNKNOWN_NATIVE_PROCESS_LIMIT', returncode=ret.returncode)
            rows.append(row)
            continue
        check = json.loads(Path(str(prefix) + '.json').read_text())
        assert (check['source_n'], check['source_m']) == (n, m) and check['pins'] == pins
        if check['status'] == 'DEGREE_INFEASIBLE':
            row.update(status='CURRENT_DEGREE_BLOCKED_NATIVE', saturated_mandatory_pins=check['blocked'])
            rows.append(row)
            continue
        missing = check['missing']
        row.update(mandatory_R4_file=rel(Path(str(prefix) + '.json')),
                   mandatory_R4_missing=len(missing),
                   core_R4_missing=sum(v < 50554 for v in missing),
                   extra_R4_missing=sum(v >= 50554 for v in missing),
                   native_CPU_seconds=check['CPU_seconds'])
        guards = [] if not missing else check.get('exact_anchors') if check.get('exact_one_or_two_found') else None
        if guards is not None and len(guards) > min(item['anchor_cap'], 2):
            guards = None
        if guards is None:
            row.update(status='EXACT_NO_ONE_GUARD' if item['anchor_cap'] == 1 else
                       'EXACT_NO_AT_MOST_TWO_GUARDS' if check.get('exact_two_complete') else 'UNKNOWN_EXACT_TWO_LIMIT',
                       larger_actual_guard_budget_open=item['anchor_cap'] > 2)
            rows.append(row)
            continue
        selected = sorted(pins + guards)
        assert len(selected) == len(set(selected)) <= 13
        assert item['deleted_saturated_pin'] not in selected
        assert all(degree[p] < 13 for p in selected)
        good, selected_prefix = check, prefix
        if guards:
            if BUDGET - cpu() < 0.5:
                row.update(status='COMPLETE_MASK_CANDIDATE_VERIFY_UNATTEMPTED_BUDGET', guards=guards)
                rows.append(row)
                status = 'ADDITIONAL_CPU_RESERVE_STOP'
                break
            pinfile.write_text(' '.join(map(str, selected)) + '\n')
            selected_prefix = Path(str(prefix) + '_selected')
            with Path(str(selected_prefix) + '.log').open('w') as log:
                ret = subprocess.run([str(native), 'verify', str(current), str(pinfile), str(selected_prefix), '13'], stdout=log, stderr=log, timeout=15)
            calls += 1
            assert ret.returncode == 0
            good = json.loads(Path(str(selected_prefix) + '.json').read_text())
        assert good['missing_count'] == 0 and good['covered_count'] == n
        assert good['pin_current_degrees'] == [degree[p] for p in selected]
        graph = OUT / 'graphs' / f'graph_d13_D5_n{n+1}.edges'
        with current.open() as old, graph.open('w') as new:
            assert tuple(map(int, next(old).split())) == (n, m)
            new.write(f'{n+1} {m+len(selected)}\n')
            for line in old:
                new.write(line)
            for p in selected:
                new.write(f'{p} {n}\n')
        row.update(status='ACCEPTED_PRODUCTION_COMPLETE_CURRENT_R4_INDUCTION',
                   guards=guards, full_neighbor_set=selected,
                   selected_old_degrees=good['pin_current_degrees'],
                   new_vertex=n, new_n=n+1, new_m=m+len(selected), new_degree=len(selected),
                   actual_complete_current_R4_covered=n, actual_complete_current_R4_missing=0,
                   selected_R4_evidence=rel(Path(str(selected_prefix) + '.json')),
                   graph_file=rel(graph), all_old_edges_retained=True,
                   acceptance_scope='CompleteactualcurrentR4+degrees fromprecedingacceptedD5source.',
                   parent_verification_pending=False, rawmap_used=False)
        rows.append(row)
        accepted.append(row)
        save('accepted_sequence.json', {'initial_n': 51418, 'records': accepted})
        print('ACCEPTED ' + json.dumps({k: row[k] for k in ['prototype', 'deleted_saturated_pin', 'guards', 'full_neighbor_set', 'new_n', 'new_m']}), flush=True)
        for p in selected:
            degree[p] += 1
        degree.append(len(selected))
        n, m, current = n + 1, m + len(selected), graph
        assert max(degree) <= 13
    original_cpu = json.loads((PARENT / 'RESULT.json').read_text())['total_parent_children_CPU_seconds']
    result = {'status': status, 'running': False, 'initial_n': 51418, 'initial_m': 324461,
              'final_n': n, 'final_m': m, 'final_graph': rel(current),
              'frozen_items': 53, 'visited': len(rows), 'unattempted': 53 - len(rows),
              'accepted_extensions': len(accepted), 'rows': rows, 'records': accepted,
              'row_status_counts': dict(Counter(r['status'] for r in rows)),
              'native_calls': calls, 'additional_parent_children_CPU_seconds': cpu(),
              'additional_CPU_budget_seconds': BUDGET,
              'original_producer_CPU_seconds': original_cpu,
              'combined_producer_CPU_seconds': original_cpu + cpu(),
              'maximum_degree': max(degree), 'D5_scope': 'Rootaccepted51418thencompleteperstepcurrentR4/degreeinduction.',
              'old37_failed_prototypes_retested': False,
              'fresh_currentdegree_and_currentR4_used': True,
              'source_BFS': 0, 'all_source_BFS': 0, 'per_graph_root_BFS': 0,
              'external_review': 0, 'Lean': 0, 'shared_family_modified': False,
              'pending': []}
    save('RESULT.json', result)
    save('terminal.json', {k: v for k, v in result.items() if k not in ['rows', 'records']})
    print('TERMINAL ' + json.dumps({k: v for k, v in result.items() if k not in ['rows', 'records']}), flush=True)


if __name__ == '__main__':
    main()
