#!/usr/bin/env python3
"""One bounded symbolic preprocessing run; no assignments, graphs, or BFS."""
from pathlib import Path
from collections import Counter
import json
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
sys.path.insert(0, str(HERE.parent / 'fourpair_tight'))
from linear import kernel, project

Q, M, DIM, BUDGET = 17, 48, 6, 115.0


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


def compose(new, old):
    return [[sum(k * old[i][j] for i, k in enumerate(row)) % Q for j in range(DIM)]
            for row in new]


def reduce_mode(row, scalar, product, inverse):
    phases = row['pair_phases'] + [24, 24]
    anchor = next(i for i, phase in enumerate(phases) if scalar[phase] != 1)
    assert anchor == row['anchor_component']
    components = [{'phase': j, 'kind': 'pair'} for j in row['pair_phases']]
    components += [{'phase': 24, 'kind': 'involution'} for _ in range(2)]
    original = affine_word_forms(Q, product, inverse, scalar, components)
    assert original['form_counts'] == row['symbolic_capacity']
    anchored = [{c[:anchor] + c[anchor + 1:] for c in cell} for cell in original['forms']]
    assert list(map(len, anchored)) == original['form_counts']
    basis = [[int(i == j) for j in range(DIM)] for i in range(DIM)]
    forms, iterations = anchored, []
    for step in range(DIM + 1):
        counts = list(map(len, forms))
        if min(counts) < Q:
            status = 'REJECTED_RESTRICTED_CAPACITY'
            break
        tight = [j for j, n in enumerate(counts) if n == Q]
        dim = len(basis)
        matrix = [[sum(c[k] for c in forms[j]) % Q for k in range(dim)] for j in tight]
        rref, pivots, newbasis = kernel(matrix, dim)
        record = {'iteration': step, 'dimension_before': dim, 'counts_before': counts,
                  'exact_17_phases': tight, 'sum_matrix_current_coordinates': matrix,
                  'rref': rref, 'pivot_columns': pivots, 'rank': len(pivots),
                  'kernel_basis_in_current_coordinates': newbasis}
        if not pivots:
            record['status'] = 'STABLE_NO_NEW_LINEAR_CONSTRAINT'
            iterations.append(record)
            status = 'SURVIVES_STABLE_TIGHT_LINEAR_CLOSURE'
            break
        basis = compose(newbasis, basis)
        forms = project(forms, newbasis)
        assert forms == project(anchored, basis)
        record.update(dimension_after=len(basis), basis_in_original_anchored_coordinates=basis,
                      counts_after=list(map(len, forms)))
        iterations.append(record)
    else:
        raise AssertionError('More than six strict dimension drops')
    counts = list(map(len, forms))
    deficient = [j for j, n in enumerate(counts) if n < Q]
    result = {'source_cursor': row['cursor'], 'pair_phases': row['pair_phases'],
              'anchor_component': anchor, 'iterations': iterations, 'status': status,
              'final_dimension': len(basis), 'basis_in_original_anchored_coordinates': basis,
              'final_form_counts': counts, 'deficient_phases': deficient,
              'remaining_projective_inputs': 0 if deficient else (Q ** len(basis) - 1) // (Q - 1)}
    if deficient:
        witness = min(deficient, key=lambda j: counts[j])
        result.update(witness_phase=witness, witness_restricted_forms=sorted(forms[witness]))
    return result


def main():
    start = time.process_time()
    assert not (HERE / 'terminal.json').exists(), 'No automatic rerun'
    rows = [json.loads(line) for line in (HERE.parent / 'survivors.jsonl').read_text().splitlines()]
    rows = [r for r in rows if r['pair_count'] == 5]
    assert len(rows) == 16375
    assert all(r['involution_count'] == 2 and r['field_variables'] == 7 and
               r['projective_marked_inputs'] == 1508598 for r in rows)
    byphase = {tuple(r['pair_phases']): r for r in rows}
    assert len(byphase) == len(rows)
    old_inputs = json.loads((HERE.parent / 'maximin_production/inputs.json').read_text())
    old_terminal = json.loads((HERE.parent / 'maximin_production/terminal.json').read_text())
    assert old_terminal['status'] == 'COMPLETE_MAXIMIN_SCOPE_NO_SOLUTION'
    completed = {r['source_cursor']: r for r in old_terminal['per_pattern']}
    checked = set()
    for item in old_inputs:
        if item['pairs'] != 5:
            continue
        old = completed[item['source_cursor']]
        row = byphase[tuple(item['pair_phases'])]
        assert row['cursor'] == item['source_cursor']
        assert old['scope'] == old['counts']['processed_marked_inputs'] == item['projective_scope'] == 1508598
        assert old['counts']['full_root_BFS'] == 0 and old['counts']['fiber_passes_in_test_order'][-1] == 0
        checked.add(row['cursor'])
    assert len(checked) == 28
    scalar = [pow(3, j, Q) for j in range(M)]
    assert pow(17, 2, 48) == 1 and all(scalar[17*j % M] == scalar[j] for j in range(M))
    product = [[(i + j) % M for j in range(M)] for i in range(M)]
    inverse = [(-j) % M for j in range(M)]
    maps, orbit_members = [], {}
    for row in rows:
        transformed = []
        for slot, phase in enumerate(row['pair_phases']):
            target = 17 * phase % M
            inverted = target > M // 2
            canonical = M - target if inverted else target
            factor = -scalar[-phase % M] % Q if inverted else 1
            transformed.append((canonical, slot, factor, inverted, target))
        transformed.sort()
        target_key = tuple(t[0] for t in transformed)
        target_row = byphase[target_key]
        assert all(target_row['symbolic_capacity'][17*j % M] == row['symbolic_capacity'][j] for j in range(M))
        rep = min(tuple(row['pair_phases']), target_key)
        orbit_members.setdefault(rep, []).append(row['cursor'])
        maps.append({'source_cursor': row['cursor'], 'source_pair_phases': row['pair_phases'],
                     'target_cursor': target_row['cursor'], 'target_pair_phases': list(target_key),
                     'representative_cursor': byphase[rep]['cursor'],
                     'target_pair_slots': [{'new_slot': k, 'old_slot': x[1], 'field_factor': x[2],
                                            'inverse_taken': x[3], 'phase_before_canonical_inverse': x[4]}
                                           for k, x in enumerate(transformed)],
                     'reflection_slot_map': [5, 6], 'reflection_field_factors': [1, 1]})
    mapping_by_cursor = {x['source_cursor']: x for x in maps}
    assert all(mapping_by_cursor[x['target_cursor']]['target_cursor'] == x['source_cursor'] for x in maps)
    orbits = []
    for key, members in sorted(orbit_members.items()):
        assert len(members) in (1, 2)
        old_members = sorted(checked.intersection(members))
        row = byphase[key]
        orbits.append({'representative_cursor': row['cursor'], 'pair_phases': list(key),
                       'member_cursors': sorted(members), 'orbit_size': len(members),
                       'checked_member_cursors': old_members,
                       'status': 'ALREADY_EXCLUDED_BY_COMPLETED_MODE' if old_members else 'UNSEARCHED',
                       'minimum_original_form_count': min(row['symbolic_capacity']),
                       'initial_exact_17_phases': [j for j, n in enumerate(row['symbolic_capacity']) if n == Q]})
    unsearched = [o for o in orbits if o['status'] == 'UNSEARCHED']
    todo = [o for o in unsearched if o['initial_exact_17_phases']]
    dump('phase17_mappings.json', maps)
    dump('orbits.json', orbits)
    preparation = {
        'input_modes': len(rows), 'actual_checked_modes': len(checked),
        'original_minimum_capacity_histogram': dict(Counter(min(r['symbolic_capacity']) for r in rows)),
        'phase17_orbits': len(orbits), 'orbit_size_histogram': dict(Counter(o['orbit_size'] for o in orbits)),
        'already_excluded_orbits': len(orbits) - len(unsearched),
        'already_excluded_modes_after_automorphism': sum(o['orbit_size'] for o in orbits if o['status'] != 'UNSEARCHED'),
        'unsearched_orbits': len(unsearched),
        'unsearched_modes': sum(o['orbit_size'] for o in unsearched),
        'tight_17_representatives_to_process': len(todo),
        'tight_17_original_modes_represented': sum(o['orbit_size'] for o in todo),
        'remaining_projective_inputs_before_automorphism': sum(o['orbit_size'] for o in unsearched) * 1508598,
        'remaining_projective_inputs_after_automorphism_before_linear': len(unsearched) * 1508598,
        'preparation_CPU_seconds': time.process_time() - start,
    }
    dump('preparation.json', preparation)
    print(json.dumps({'event': 'PREPARATION_COMPLETE', **preparation}), flush=True)
    results = {}
    with (HERE / 'tight_results.jsonl').open('w') as out:
        for index, orbit in enumerate(todo):
            if time.process_time() - start >= BUDGET:
                break
            result = reduce_mode(byphase[tuple(orbit['pair_phases'])], scalar, product, inverse)
            result['member_cursors'] = orbit['member_cursors']
            result['orbit_size'] = orbit['orbit_size']
            results[result['source_cursor']] = result
            out.write(json.dumps(result) + '\n')
            if (index + 1) % 100 == 0:
                out.flush()
                progress = {'tight_representatives_completed': index + 1,
                            'tight_representatives_total': len(todo),
                            'next_tight_index': index + 1,
                            'CPU_seconds': time.process_time() - start}
                dump('progress.json', progress)
                print(json.dumps({'event': 'PROGRESS', **progress}), flush=True)
    candidates = []
    for orbit in unsearched:
        source = byphase[tuple(orbit['pair_phases'])]
        result = results.get(source['cursor'])
        if result:
            item = {**orbit, **{k: result[k] for k in ['status', 'final_dimension',
                    'basis_in_original_anchored_coordinates', 'remaining_projective_inputs', 'final_form_counts']}}
            item['linear_result_source_cursor'] = source['cursor']
        else:
            item = {**orbit, 'status': 'TIGHT_PREPROCESSING_PENDING' if orbit['initial_exact_17_phases'] else 'NO_TIGHT_FIBER_UNCHANGED',
                    'final_dimension': DIM,
                    'basis_in_original_anchored_coordinates': [[int(i == j) for j in range(DIM)] for i in range(DIM)],
                    'remaining_projective_inputs': 1508598, 'final_form_counts': source['symbolic_capacity']}
        item.update(anchor_component=source['anchor_component'], source_cursor=source['cursor'])
        candidates.append(item)
    dump('remaining_representatives.json', candidates)
    rejected = [c for c in candidates if c['status'] == 'REJECTED_RESTRICTED_CAPACITY']
    live = [c for c in candidates if c['status'] != 'REJECTED_RESTRICTED_CAPACITY']
    summary = {**preparation,
        'status': 'COMPLETE_SYMBOLIC_PREPROCESSING' if len(results) == len(todo) else 'CPU_BUDGET_STOP_SYMBOLIC_PREFIX',
        'next_tight_index': len(results), 'tight_representatives_completed': len(results),
        'rejected_orbit_representatives': len(rejected),
        'rejected_original_modes': sum(c['orbit_size'] for c in rejected),
        'surviving_orbit_representatives': len(live),
        'surviving_original_modes': sum(c['orbit_size'] for c in live),
        'surviving_dimension_histogram': dict(Counter(c['final_dimension'] for c in live)),
        'surviving_representatives_by_original_minimum': dict(Counter(c['minimum_original_form_count'] for c in live)),
        'remaining_projective_inputs_after_automorphism_and_linear': sum(c['remaining_projective_inputs'] for c in live),
        'remaining_projective_inputs_with_original_mode_multiplicity': sum(c['remaining_projective_inputs'] * c['orbit_size'] for c in live),
        'CPU_seconds': time.process_time() - start, 'CPU_budget_seconds': 120, 'internal_stop_seconds': BUDGET,
        'worker_count': 1, 'actual_field_assignments': 0, 'graphs_generated': 0, 'BFS_runs': 0,
        'pending': [] if len(results) == len(todo) else ['Unprocessed tight orbit representatives'],
    }
    dump('terminal.json', summary)
    print(json.dumps({'event': 'TERMINAL', **summary}), flush=True)


if __name__ == '__main__':
    main()
