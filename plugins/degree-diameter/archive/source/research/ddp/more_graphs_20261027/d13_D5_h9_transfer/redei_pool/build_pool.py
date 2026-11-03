"""Reuse the fixed Redei15/plane caches on the actual degree13 host; no cover search."""
from array import array
from collections import Counter
from pathlib import Path
import json
import resource
import time

P = Path(__file__).resolve().parent
ROOT = P.parents[4]
HOST = P.parent
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (60, 61))


def cpu():
    return time.process_time() - START


def save(name, value):
    (P / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


assert json.loads((P / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_D13_POOL_QUERY'
orbit_path = ROOT / 'research/ddp/more_graphs_20261027/h9_redei15/pool/orbit.json'
orbit = json.loads(orbit_path.read_text())
ids15 = orbit['point_indices15']
masks = [int(a) + (int(b) << 64) for a, b in orbit['mask_words_u64_decimal']]
assert orbit['orbit_size'] == len(masks) == len(ids15) == 702
flatdir = ROOT / 'research/ddp/more_graphs_20261027/h9_baer_plane_pool'
nonflatdir = ROOT / 'research/ddp/more_graphs_20261027/h9_baer_nonflat_F3_pool'
cached_sources = json.loads((nonflatdir / 'sources.json').read_text())
coeff = list(map(int, (nonflatdir / 'coefficient_points91.txt').read_text().split()))
assert coeff[0] == 91
assert [coeff[1 + 3*j:4 + 3*j] for j in range(91)] == orbit['coefficient_points_PG2F9']
coords = (ROOT / cached_sources['coords']).read_bytes()
assert len(coords) == 66430 * 7
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

# One actual-adjacency read for degree production; source geometry and D5 are inherited.
degree = bytearray()
source = HOST / 'source51417.adjlist.txt'
with source.open() as f:
    for line in f:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        row = list(map(int, line.split()))
        assert row[0] == len(degree)
        degree.append(len(row) - 1)
n, m = len(degree), sum(degree) // 2
assert (n, m, max(degree)) == (51417, 324451, 13)
(P / 'degree13.u8.bin').write_bytes(degree)
fold = array('H')
fold.frombytes((HOST / 'point_to_core13.u16.bin').read_bytes())
assert len(fold) == 66430 and max(fold) == 50553
binding = {'source_file': str(source.relative_to(ROOT)), 'source_format': 'zero_based_adjacency_rows_with_vertex_first_and_comment_lines',
           'source_n': n, 'source_m': m, 'core_n': 50554,
           'degree_cache': str((P / 'degree13.u8.bin').relative_to(ROOT)),
           'point_to_actual_pin_cache': str((HOST / 'point_to_core13.u16.bin').relative_to(ROOT)),
           'degree_cache_reused_without_recomputation': False,
           'source_adjacency_reads_for_degrees': 1,
           'within_class_orientation_needed_for_stable_pinsets': False}
save('sources.json', {'bases': {'13': binding}, 'raw_point_coordinates': cached_sources['coords'],
                      'orbit_cache': str(orbit_path.relative_to(ROOT)),
                      'flat_plane_cache': str((flatdir / 'planes.json').relative_to(ROOT)),
                      'nonflat_plane_cache': str((nonflatdir / 'nonflat_planes.json').relative_to(ROOT)),
                      'source_degree_histogram': dict(sorted(Counter(degree).items())),
                      'free_vertices': sum(d < 13 for d in degree),
                      'free_slots': sum(13 - d for d in degree),
                      'source_D5_scope': 'Inherited source and orientation-free class coverage; no source BFS here.'})

classes = {}
hist_allowed = Counter()
kind_stats = {'flat': Counter(), 'nonflat': Counter()}
degree_allowed = feasible = under15 = processed = 0
prep_cpu = cpu()
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
    st['raw_occurrences'] += 702
    if allowed.bit_count() < 15:
        under15 += 1
    else:
        for oi, mask in enumerate(masks):
            if mask & ~allowed:
                continue
            degree_allowed += 1
            st['degree_allowed_occurrences'] += 1
            pins = tuple(sorted({actual[j] for j in ids15[oi]}))
            assert 10 <= len(pins) <= 15
            hist_allowed[len(pins)] += 1
            if len(pins) > 13:
                continue
            feasible += 1
            st['pin_count_feasible_occurrences'] += 1
            ref = [plane['global_index'], oi]
            if pins in classes:
                rec = classes[pins]
                rec['witness_multiplicity'] += 1
                rec['all_witness_plane_orbit_refs'].append(ref)
                continue
            rawids = [raw91[j] for j in ids15[oi]]
            witness = {'plane_kind': plane['kind'], 'plane_global_index': plane['global_index'],
                       'plane_local_index': plane['local_index'], 'plane_basis': plane['basis'],
                       'orbit_index': oi, 'Redei_orbit_index': oi,
                       'coefficient_point_indices15': ids15[oi], 'original_point_ids15': rawids,
                       'original_point_coordinates15': [list(coords[7*j:7*j+7]) for j in rawids],
                       'mask_words_u64_decimal': orbit['mask_words_u64_decimal'][oi]}
            if 'center_original_label' in plane:
                witness['center_original_label'] = plane['center_original_label']
            deg = [degree[v] for v in pins]
            classes[pins] = {'pins': list(pins), 'anchor_cap': 13-len(pins),
                             'mandatory_pin_count': len(pins), 'pin_current_degrees': deg,
                             'pin_free_slots': [13-d for d in deg], 'raw_point_count': 15,
                             'witness_multiplicity': 1, 'all_witness_plane_orbit_refs': [ref],
                             'witness': witness}
    processed += 1
    if processed == 10:
        elapsed = cpu() - loop_start
        projected = prep_cpu + elapsed * 1120 / 10
        profile = {'planes_processed_once': 10, 'shape_occurrences_covered': 7020,
                   'preparation_CPU_seconds': prep_cpu, 'loop_CPU_seconds': elapsed,
                   'projected_full1120_CPU_seconds': projected,
                   'distinct_pool13_sofar': len(classes), 'continue_complete_scope': projected <= 60,
                   'profile_not_replayed': True}
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
        'delta': 13, **binding, 'shape': 'Redei15 x^5 graphplus6 directions; fixedPGL3F3 orbit',
        'raw_point_count': 15, 'orbit_size': 702, 'planes_expected': 1120,
        'planes_processed': processed, 'complete1120plane_scope': complete,
        'source_binding': 'Frozen actual degree13 base; producer rechecks current degrees after acceptance. No R4 completion here.',
        'pin_count_histogram': dict(sorted(hist.items())), 'records': records}
save('pool13.json', pool)
result = {'status': 'COMPLETE_702_F3_ORBIT_X1120_PLANES_D13_DEGREE_POOL' if complete else 'PARTIAL_PROFILE_OVER_BUDGET' if profile_stopped else 'PARTIAL_CPU_WINDOW',
          'prediction_id': 'P_REDEI15_D13_DEGREE_POOL',
          'prediction_verdict': 'SUPPORTED' if records else 'REFUTED' if complete else 'UNRESOLVED',
          'delta': 13, 'D': 5, 'public_savedL': 51417, **binding,
          'orbit_size': 702, 'flat_planes_reused': 364, 'nonflat_planes_reused': 756,
          'planes_expected': 1120, 'planes_processed': processed, 'complete1120plane_scope': complete,
          'raw_shape_occurrences_covered': 702*processed,
          'raw_degree_allowed_occurrences': degree_allowed,
          'degree_and_pincount_feasible_occurrences': feasible,
          'distinct_folded_pinsets': len(records), 'duplicate_feasible_occurrences': feasible-len(records),
          'degree_allowed_fold_size_histogram': dict(sorted(hist_allowed.items())),
          'distinct_pin_count_histogram': dict(sorted(hist.items())),
          'maximum_anchor_cap': max((r['anchor_cap'] for r in records), default=None),
          'planes_with_under15_allowed_raw_points': under15, 'by_plane_kind': kind_stats,
          'CPU_seconds': cpu(), 'CPU_budget_seconds': 60, 'workers': 1,
          'old_Baer_masks_enumerated_or_read': False, 'old_candidate_pool_retested': False,
          'orbit_regenerated': False, 'planes_regenerated': False, 'profile10_replayed': False,
          'old_pi12_used': False, 'source_BFS': 0, 'R4_evaluations': 0, 'anchor_tests': 0,
          'graphs_generated': 0, 'actual_n': None, 'actual_D': None, 'ordinary_bad_unordered_pairs': None,
          'new_lower_bounds': 0, 'pending': [],
          'scope': 'Only the fixed702 PGL3(F3) orbit in the1120 saved F3-defined singular planes on current51417 base.',
          'handoff': 'Pool only; exact current-base coverage and anchors belong to separate degree13 producer.'}
save('RESULT.json', result)
save('terminal.json', {**result, 'running': False})
print('FINAL', json.dumps(result), flush=True)
