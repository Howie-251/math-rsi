"""Current51417 Baer13 pool using whole point-involution classes; no cover search."""
from array import array
from collections import Counter
from pathlib import Path
import json
import resource
import time

P = Path(__file__).resolve().parent
ROOT = P.parents[4]
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (60, 61))


def cpu():
    return time.process_time() - START


def save(name, value):
    (P / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def members(mask):
    out = []
    while mask:
        bit = mask & -mask
        out.append(bit.bit_length() - 1)
        mask ^= bit
    return out


assert json.loads((P / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_BAER13_D13_POOL_QUERY'
base = P.parent
flatdir = ROOT / 'research/ddp/more_graphs_20261027/h9_baer_plane_pool'
nonflatdir = ROOT / 'research/ddp/more_graphs_20261027/h9_baer_nonflat_F3_pool'
orbit = json.loads((flatdir / 'orbit.json').read_text())
coeff = orbit['coefficient_points_PG2F9']
assert orbit['orbit_size'] == 7560 and len(coeff) == 91
words = array('Q')
words.frombytes((flatdir / 'baer_masks.u64.bin').read_bytes())
assert len(words) == 15120
masks = [int(words[2*j]) + (int(words[2*j+1]) << 64) for j in range(7560)]
ids13 = [members(m) for m in masks]
assert all(len(ids) == 13 for ids in ids13)

# The planes have F3 bases. The source point involution is coordinate Frobenius.
index = {tuple(v): i for i, v in enumerate(coeff)}
frob91 = [index[tuple(a % 3 + 3 * (-(a // 3) % 3) for a in v)] for v in coeff]
assert all(frob91[frob91[j]] == j for j in range(91))
closure_masks = [m | sum(1 << frob91[j] for j in ids) for m, ids in zip(masks, ids13)]
closure_ids = [members(m) for m in closure_masks]
closure_hist = Counter(map(len, closure_ids))
save('closure_shape_summary.json', {'source_Baer_masks_reused': 7560,
     'unique_whole_class_closure_masks': len(set(closure_masks)),
     'raw_closure_size_histogram': dict(sorted(closure_hist.items())),
     'Frobenius_coefficient_permutation': frob91,
     'notation': 'phi is the point involution; phi=tau^2 in bind_source.py author-file notation.'})

cache_binding = json.loads((base / 'redei_pool/sources.json').read_text())
binding = cache_binding['bases']['13'].copy()
assert (binding['source_n'], binding['source_m'], binding['core_n']) == (51417, 324451, 50554)
degree = (ROOT / binding['degree_cache']).read_bytes()
assert len(degree) == 51417 and max(degree) == 13
fold = array('H')
fold.frombytes((ROOT / binding['point_to_actual_pin_cache']).read_bytes())
assert len(fold) == 66430 and max(fold) == 50553
coords = (ROOT / cache_binding['raw_point_coordinates']).read_bytes()
assert len(coords) == 66430 * 7
binding['degree_cache_reused_without_recomputation'] = True
binding['source_adjacency_reads_in_this_task'] = 0
binding['whole_class_closure_required'] = True
binding['within_class_orientation_needed_for_stable_pinsets'] = False
flats = json.loads((flatdir / 'planes.json').read_text())['records']
nonflats = json.loads((nonflatdir / 'nonflat_planes.json').read_text())['records']
assert len(flats) == 364 and len(nonflats) == 756
planes = []
for x in flats:
    planes.append({'global_index': len(planes), 'kind': 'flat', 'local_index': x['plane_index'],
                   'basis': x['basis_y_x_z'], 'point_ids91': x['point_ids91'],
                   'center_original_label': x['center_original_label']})
for x in nonflats:
    planes.append({'global_index': len(planes), 'kind': 'nonflat', 'local_index': x['nonflat_plane_index'],
                   'basis': x['RREF_basis'], 'point_ids91': x['Q9_point_ids91']})
save('sources.json', {'bases': {'13': binding}, 'raw_point_coordinates': cache_binding['raw_point_coordinates'],
     'Baer_masks': str((flatdir / 'baer_masks.u64.bin').relative_to(ROOT)),
     'Baer_orbit': str((flatdir / 'orbit.json').relative_to(ROOT)),
     'flat_planes': str((flatdir / 'planes.json').relative_to(ROOT)),
     'nonflat_planes': str((nonflatdir / 'nonflat_planes.json').relative_to(ROOT)),
     'mapping_rule': 'pi13(B union phi(B)); includes every vertex of each touched current class. No raw orientation assumption.',
     'coverage_rule': 'Whole-class surjective quotient lifting preserves the inherited polar/Baer radius4 core guarantee; actual extra vertices are not checked here.'})

classes = {}
allowed_hist = Counter()
kind_stats = {'flat': Counter(), 'nonflat': Counter()}
degree_allowed = feasible = under13 = processed = 0
prep = cpu()
loop_start = cpu()
profile_stopped = False
for plane in planes:
    if cpu() > 58:
        break
    raw91 = plane['point_ids91']
    assert len(raw91) == 91
    actual = [fold[r] for r in raw91]
    allowed = sum(1 << j for j, v in enumerate(actual) if degree[v] < 13)
    st = kind_stats[plane['kind']]
    st['planes_processed'] += 1
    st['Baer_occurrences'] += 7560
    if allowed.bit_count() < 13:
        under13 += 1
    else:
        for oi, mask in enumerate(closure_masks):
            if mask & ~allowed:
                continue
            degree_allowed += 1
            st['degree_allowed_whole_closure_occurrences'] += 1
            pins = tuple(sorted({actual[j] for j in closure_ids[oi]}))
            allowed_hist[len(pins)] += 1
            if len(pins) > 13:
                continue
            feasible += 1
            st['degree_and_pincount_feasible_occurrences'] += 1
            ref = [plane['global_index'], oi]
            if pins in classes:
                rec = classes[pins]
                rec['witness_multiplicity'] += 1
                rec['all_witness_plane_baer_refs'].append(ref)
                continue
            rawids = [raw91[j] for j in ids13[oi]]
            closedids = [raw91[j] for j in closure_ids[oi]]
            witness = {'plane_kind': plane['kind'], 'plane_global_index': plane['global_index'],
                       'plane_local_index': plane['local_index'], 'plane_basis': plane['basis'],
                       'Baer_orbit_index': oi, 'Baer_point_indices13': ids13[oi],
                       'Baer_mask_words_u64': [str(words[2*oi]), str(words[2*oi+1])],
                       'original_point_ids13': rawids,
                       'original_point_coordinates13': [list(coords[7*j:7*j+7]) for j in rawids],
                       'closure_coefficient_point_indices': closure_ids[oi],
                       'closure_raw_point_ids': closedids,
                       'closure_raw_point_coordinates': [list(coords[7*j:7*j+7]) for j in closedids]}
            if 'center_original_label' in plane:
                witness['center_original_label'] = plane['center_original_label']
            deg = [degree[v] for v in pins]
            classes[pins] = {'pins': list(pins), 'anchor_cap': 13-len(pins),
                             'mandatory_pin_count': len(pins), 'pin_current_degrees': deg,
                             'pin_free_slots': [13-d for d in deg], 'raw_point_count': 13,
                             'raw_closure_point_count': len(closedids),
                             'whole_class_closure': True, 'witness_multiplicity': 1,
                             'all_witness_plane_baer_refs': [ref], 'witness': witness}
    processed += 1
    if processed == 10:
        elapsed = cpu() - loop_start
        projected = prep + elapsed * 1120 / 10
        profile = {'planes_processed_once': 10, 'Baer_occurrences_covered': 75600,
                   'preparation_CPU_seconds': prep, 'loop_CPU_seconds': elapsed,
                   'projected_full1120_CPU_seconds': projected, 'distinct_pool13_sofar': len(classes),
                   'continue_complete_scope': projected <= 60, 'profile_not_replayed': True}
        save('profile10planes.json', profile)
        print('PROFILE10', json.dumps(profile), flush=True)
        if projected > 60:
            profile_stopped = True
            break

complete = processed == 1120
records = [classes[pins] for pins in sorted(classes)]
for i, rec in enumerate(records):
    rec['pool_index'] = i
hist = Counter(len(r['pins']) for r in records)
pool = {'status': 'COMPLETE_DEGREE_ONLY_POOL' if complete else 'PARTIAL_DEGREE_ONLY_POOL',
        'delta': 13, **binding, 'shape': 'Baer13 whole point-involution class closure',
        'raw_point_count': 13, 'orbit_size': 7560, 'planes_expected': 1120,
        'planes_processed': processed, 'complete1120plane_scope': complete,
        'source_binding': 'Frozen51417 source; producer must recheck current degrees after additions.',
        'pin_count_histogram': dict(sorted(hist.items())), 'records': records}
save('pool13.json', pool)
result = {'status': 'COMPLETE_BAER13_WHOLE_CLASS_D13_DEGREE_POOL' if complete else 'PARTIAL_PROFILE_OVER_BUDGET' if profile_stopped else 'PARTIAL_CPU_WINDOW',
          'prediction_id': 'P_BAER13_D13_CURRENT51417_DEGREE_POOL',
          'prediction_verdict': 'SUPPORTED' if records else 'REFUTED' if complete else 'UNRESOLVED',
          'mode_executed': 'whole_phi_class_closure_only',
          'direct13raw_mode_executed': False,
          'direct_mode_reason': 'Source agent identifies edge-multiplicity changes that cannot be repaired by within-class gauge; no orientation-correct direct map supplied.',
          'delta': 13, 'D': 5, 'public_savedL': 51417, **binding,
          'orbit_size_reused': 7560, 'flat_planes_reused': 364, 'nonflat_planes_reused': 756,
          'planes_expected': 1120, 'planes_processed': processed, 'complete1120plane_scope': complete,
          'Baer_plane_occurrences_covered': 7560*processed,
          'degree_allowed_whole_closure_occurrences': degree_allowed,
          'degree_and_pincount_feasible_occurrences': feasible,
          'distinct_folded_pinsets': len(records), 'duplicate_feasible_occurrences': feasible-len(records),
          'degree_allowed_actual_pin_count_histogram': dict(sorted(allowed_hist.items())),
          'distinct_pin_count_histogram': dict(sorted(hist.items())),
          'maximum_anchor_cap': max((r['anchor_cap'] for r in records), default=None),
          'planes_with_under13_degree_allowed_raw_points': under13,
          'raw_closure_size_histogram': dict(sorted(closure_hist.items())), 'by_plane_kind': kind_stats,
          'CPU_seconds': cpu(), 'CPU_budget_seconds': 60, 'workers': 1,
          'orbit_regenerated': False, 'planes_regenerated': False, 'old_N12_pool_retested': False,
          'Redei_pool_repeated': False, 'source_BFS': 0, 'R4_evaluations': 0, 'anchor_tests': 0,
          'graphs_generated': 0, 'actual_n': None, 'actual_D': None, 'ordinary_bad_unordered_pairs': None,
          'new_lower_bounds': 0, 'pending': [],
          'scope': 'Fixed7560 Baer13 masks in1120 saved F3-defined singular planes, whole-point-involution classes, current51417 source only.',
          'handoff': 'Literal degree-legal pool only; current extras and full old-graph radius4 require separate producer.'}
save('RESULT.json', result)
save('terminal.json', {**result, 'running': False})
print('FINAL', json.dumps(result), flush=True)
