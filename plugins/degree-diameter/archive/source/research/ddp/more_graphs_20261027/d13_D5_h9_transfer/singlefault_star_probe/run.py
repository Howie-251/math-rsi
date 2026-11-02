"""One fixed91-prototype current-source star deletion batch, at mosttwo guards."""
from collections import Counter
from pathlib import Path
import json
import resource
import subprocess
import time

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
ROOT = BASE.parents[3]
START = time.process_time()
CHILD = resource.getrusage(resource.RUSAGE_CHILDREN)
BUDGET = 30.0


def cpu():
    c = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() - START + c.ru_utime + c.ru_stime - CHILD.ru_utime - CHILD.ru_stime


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + '\n')


def rel(path):
    return str(path.relative_to(ROOT))


def main():
    assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_NATIVE_COVER'
    assert not (OUT / 'RESULT.json').exists()
    frozen = json.loads((OUT / 'frozen91.json').read_text())['records']
    assert len(frozen) == 91
    assert [(r['prototype_degree'], r['prototype']) for r in frozen] == sorted((r['prototype_degree'], r['prototype']) for r in frozen)
    source = BASE / 'source51417.edges'
    degree = (BASE / 'degree13.u8.bin').read_bytes()
    assert len(degree) == 51417
    native_source = (OUT / 'cover.cpp').read_text()
    assert native_source.count('assert(DEG==13);') == 1
    assert 'DEG==11||DEG==12' not in native_source
    subprocess.run(['g++', '-O3', '-std=c++17', str(OUT / 'cover.cpp'), '-o', str(OUT / 'cover')], check=True)
    compile_cpu = cpu()
    (OUT / 'items').mkdir(exist_ok=True)
    rows, hit, calls = [], None, 0
    status = 'ALL91_AT_MOST_TWO_GUARDS_TERMINAL'
    for item in frozen:
        if BUDGET - cpu() < 7.5:
            status = 'TOTAL_CPU_RESERVE_STOP'
            break
        pins = item['mandatory_pins']
        assert item['deleted_saturated_pin'] not in pins
        assert degree[item['deleted_saturated_pin']] == 13
        assert all(degree[p] < 13 for p in pins)
        prefix = OUT / 'items' / f'ord{item["ordinal"]:03d}_v{item["prototype"]}'
        pinfile = Path(str(prefix) + '.pins.txt')
        pinfile.write_text(' '.join(map(str, pins)) + '\n')
        row = dict(item)
        with Path(str(prefix) + '.log').open('w') as log:
            ret = subprocess.run([str(OUT / 'cover'), 'prepare', str(source), str(pinfile), str(prefix), '13'],
                                 stdout=log, stderr=log, timeout=15)
        calls += 1
        if ret.returncode:
            row.update(status='UNKNOWN_NATIVE_PROCESS_LIMIT', returncode=ret.returncode)
            rows.append(row)
            continue
        check = json.loads(Path(str(prefix) + '.json').read_text())
        assert check['source_n'] == 51417 and check['source_m'] == 324451 and check['pins'] == pins
        missing = check['missing']
        row.update(mandatory_R4_file=rel(Path(str(prefix) + '.json')),
                   mandatory_R4_missing=len(missing),
                   core_R4_missing=sum(v < 50554 for v in missing),
                   extra_R4_missing=sum(v >= 50554 for v in missing),
                   native_CPU_seconds=check['CPU_seconds'])
        if item['ordinal'] == 0:
            profile = {**row, 'compile_CPU_seconds': compile_cpu,
                       'total_CPU_seconds_so_far': cpu(),
                       'estimated_all91_CPU_seconds': compile_cpu + 91 * check['CPU_seconds'],
                       'at_most_two_guard_result': check.get('exact_one_or_two_found', not missing),
                       'source_BFS': 0}
            save('FIRST_PROFILE.json', profile)
            print('FIRST_PROFILE ' + json.dumps({k: profile[k] for k in ['prototype', 'mandatory_R4_missing', 'core_R4_missing', 'extra_R4_missing', 'native_CPU_seconds', 'estimated_all91_CPU_seconds', 'at_most_two_guard_result']}), flush=True)
        guards = [] if not missing else check.get('exact_anchors') if check.get('exact_one_or_two_found') else None
        if guards is not None and len(guards) > item['tested_guard_cap']:
            guards = None
        if guards is None:
            if item['tested_guard_cap'] == 1:
                row['status'] = 'EXACT_NO_ONE_GUARD'
            elif check.get('exact_two_complete'):
                row['status'] = 'EXACT_NO_AT_MOST_TWO_GUARDS'
            else:
                row['status'] = 'UNKNOWN_EXACT_TWO_LIMIT'
            row['larger_actual_guard_budget_open'] = item['anchor_cap'] > 2
            rows.append(row)
            continue
        selected = sorted(pins + guards)
        assert len(selected) == len(set(selected)) <= 13
        assert item['deleted_saturated_pin'] not in selected
        assert all(degree[p] < 13 for p in selected)
        good, selected_prefix = check, prefix
        if guards:
            if BUDGET - cpu() < 0.5:
                row.update(status='COMPLETE_MASK_CANDIDATE_SELECTED_VERIFY_UNATTEMPTED_BUDGET', guards=guards)
                rows.append(row)
                status = 'TOTAL_CPU_RESERVE_STOP'
                break
            pinfile.write_text(' '.join(map(str, selected)) + '\n')
            selected_prefix = Path(str(prefix) + '_selected')
            with Path(str(selected_prefix) + '.log').open('w') as log:
                verify = subprocess.run([str(OUT / 'cover'), 'verify', str(source), str(pinfile), str(selected_prefix), '13'], stdout=log, stderr=log, timeout=15)
            calls += 1
            assert verify.returncode == 0
            good = json.loads(Path(str(selected_prefix) + '.json').read_text())
        assert good['missing_count'] == 0 and good['covered_count'] == 51417
        assert max(good['pin_current_degrees']) < 13
        graph = OUT / 'graph_d13_D5_n51418.edges'
        with source.open() as old, graph.open('w') as new:
            assert tuple(map(int, next(old).split())) == (51417, 324451)
            new.write(f'51418 {324451 + len(selected)}\n')
            for line in old:
                new.write(line)
            for p in selected:
                new.write(f'{p} 51417\n')
        row.update(status='PRODUCER_COMPLETE51418_PENDING_ROOT',
                   guards=guards, full_neighbor_set=selected,
                   new_n=51418, new_m=324451 + len(selected), new_vertex=51417,
                   new_vertex_degree=len(selected),
                   selected_old_degrees=good['pin_current_degrees'],
                   actual_complete_current_R4_missing=0,
                   actual_complete_current_R4_covered=51417,
                   selected_R4_evidence=rel(Path(str(selected_prefix) + '.json')),
                   graph_file=rel(graph), all_old_edges_retained=True,
                   rawmap_or_geometric_core_assumption=False,
                   independent_root_check_pending=True)
        hit = row
        rows.append(row)
        save('first_hit.json', hit)
        status = 'FIRST_COMPLETE_GRAPH_STOP'
        print('FIRST_HIT ' + json.dumps({k: row[k] for k in ['prototype', 'deleted_saturated_pin', 'mandatory_pins', 'guards', 'full_neighbor_set', 'new_n', 'new_m', 'graph_file']}), flush=True)
        break
    result = {
        'status': status, 'running': False, 'source_n': 51417, 'source_m': 324451,
        'target_Delta': 13, 'target_D': 5, 'public_savedL': 51417,
        'frozen_items': 91, 'items_visited': len(rows), 'unattempted': 91 - len(rows),
        'native_calls': calls, 'rows': rows,
        'row_status_counts': dict(Counter(r['status'] for r in rows)),
        'complete_extensions': int(hit is not None),
        'compile_CPU_seconds': compile_cpu, 'total_parent_children_CPU_seconds': cpu(),
        'CPU_budget_seconds': BUDGET,
        'actual_n': 51418 if hit else None, 'actual_D': None,
        'ordinary_bad_unordered_pairs': None,
        'source_BFS': 0, 'old_source_allBFS': 0, 'raw_geometry_used': False,
        'prediction_exists': 'SUPPORTED' if hit else 'UNRESOLVED' if len(rows) < 91 or any(r['status'].startswith('UNKNOWN') for r in rows) else 'REFUTED_FOR_FIXED_AT_MOST_TWO_GUARD_SCOPE',
        'full_actual_guard_budget_excluded': False,
        'pending': ['Rootindependentfirstnewparametergraphcheck'] if hit else [],
    }
    save('RESULT.json', result)
    save('terminal.json', {k: v for k, v in result.items() if k != 'rows'})
    print('TERMINAL ' + json.dumps({k: v for k, v in result.items() if k != 'rows'}), flush=True)


if __name__ == '__main__':
    main()
