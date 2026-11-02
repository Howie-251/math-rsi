"""Exact <=2-anchor completion of the frozen7 Q-lines; no new graph generated."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
BASE = OUT.parent
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
assert json.loads((OUT / 'PREDICTION.json').read_text())['frozen_before_exact_anchor_completion']
rows = json.loads((BASE / 'quadric_extension/RESULT.json').read_text())['rows']
pool = json.loads((BASE / 'h9_quadric_line_extension_pool/pool.json').read_text())['records']
assert len(rows) == len(pool) == 7
for i, row in enumerate(rows):
    assert row['candidate'] == i and row['pins'] == pool[i]['pins']
    assert len(row['pins']) == 10 and row['missing_count'] == len(row['missing_vertices'])

source = ROOT / 'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
adj = []
with source.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):
            continue
        z = list(map(int, line.split()))
        assert z[0] == len(adj)
        adj.append(z[1:])
N = len(adj)
assert N == 42342 and sum(map(len, adj)) == 2*245217 and max(map(len, adj)) == 12
available = [v for v in range(N) if len(adj[v]) < 12]
assert len(available) == 14396
anchor_index = {v: i for i, v in enumerate(available)}
all_anchors = (1 << len(available))-1
targets = sorted({t for row in rows for t in row['missing_vertices']})
coverers = {}
distances = {}
target_counts = {}
unknown = False

for t in targets:
    if time.process_time()-START > 54:
        unknown = True
        break
    dist = bytearray([255])*N
    dist[t] = 0
    queue = [t]
    for u in queue:
        d = dist[u]+1
        if d > 4:
            break
        for v in adj[u]:
            if dist[v] == 255:
                dist[v] = d
                queue.append(v)
    bitbytes = bytearray((len(available)+7)//8)
    for i, v in enumerate(available):
        if dist[v] <= 4:
            bitbytes[i >> 3] |= 1 << (i & 7)
    coverers[t] = int.from_bytes(bitbytes, 'little')
    distances[t] = bytes(dist)
    target_counts[t] = coverers[t].bit_count()

def path_to_target(anchor, target):
    ds = distances[target]
    assert ds[anchor] <= 4
    path = [anchor]
    while path[-1] != target:
        u = path[-1]
        path.append(min(v for v in adj[u] if ds[v]+1 == ds[u]))
    return path

def certify(row, anchors):
    missing = row['missing_vertices']
    evidence = []
    for t in missing:
        chosen = next(a for a in anchors if distances[t][a] <= 4)
        path = path_to_target(chosen, t)
        evidence.append(dict(target=t, covering_anchor=chosen,
                             old_base_distance=distances[t][chosen], path=path))
    pins = sorted(row['pins']+anchors)
    assert len(pins) == len(set(pins)) <= 12
    assert all(len(adj[v]) < 12 for v in pins)
    return dict(candidate=row['candidate'], mandatory_pins=row['pins'], anchors=anchors,
                complete_new_neighbor_set=pins, new_vertex_label=N, new_vertex_degree=len(pins),
                neighbor_current_degrees=[len(adj[v]) for v in pins],
                saved_missing_targets=missing, exact_missing_targets_covered=len(evidence),
                coverage_paths_for_saved_missing_targets=evidence,
                other_targets_covered_by_saved_mandatory_certificate=True,
                alloldtargets_radius4_covered=True, predicted_new_n=N+1,
                predicted_maximum_degree=12, predicted_D_at_most=5,
                actual_new_graph_generated=False, actual_new_graph_D=None)

candidate_results = []
success = None
if not unknown:
    for row in rows:
        excluded = sum(1 << anchor_index[v] for v in row['pins'])
        allowed = all_anchors & ~excluded
        missing = sorted(row['missing_vertices'], key=lambda t: (target_counts[t], t))
        one = allowed
        for t in missing:
            one &= coverers[t]
        if one:
            a = available[(one & -one).bit_length()-1]
            success = certify(row, [a])
            candidate_results.append(dict(candidate=row['candidate'],status='ONE_ANCHOR_EXISTS',
                                           first_anchors_tested=0, allowed_anchor_count=allowed.bit_count()))
            break
        cursor = allowed
        tested = 0
        while cursor:
            if tested % 128 == 0 and time.process_time()-START > 54:
                unknown = True
                break
            first_bit = cursor & -cursor
            cursor -= first_bit
            first_index = first_bit.bit_length()-1
            second = allowed & ~first_bit
            for t in missing:
                if not (coverers[t] & first_bit):
                    second &= coverers[t]
                    if not second:
                        break
            tested += 1
            if second:
                second_index = (second & -second).bit_length()-1
                anchors = [available[first_index], available[second_index]]
                success = certify(row, anchors)
                candidate_results.append(dict(candidate=row['candidate'],status='TWO_ANCHORS_EXIST',
                                               first_anchors_tested=tested, allowed_anchor_count=allowed.bit_count()))
                break
        if success:
            break
        candidate_results.append(dict(candidate=row['candidate'],
                                      status='UNKNOWN_CPU_LIMIT' if unknown else 'NO_AT_MOST_TWO_ANCHORS',
                                      first_anchors_tested=tested, allowed_anchor_count=allowed.bit_count(),
                                      one_anchor_intersection_empty=True))
        if unknown:
            break

status = 'FOUND_FULL_CANDIDATE_PENDING_ROOT' if success else ('UNKNOWN_CPU_LIMIT' if unknown else 'NO_AT_MOST_TWO_ANCHORS_ALL_FIXED7')
result = dict(prediction_id='P10',status=status,
              existential_answer=True if success else (None if unknown else False),
              input_candidates=7, candidate_rows_completed=len(candidate_results),
              remaining_candidates_not_needed_for_existential=bool(success and len(candidate_results)<7),
              available_anchor_vertices=len(available), source_n=N, source_m=245217,
              saved_missing_union_size=len(targets), reverse_R4_BFS_executed=len(coverers),
              mandatory_R4_recomputed=0, full_allsource_BFS=False,
              candidate_results=candidate_results, full_candidate=success,
              target_available_coverer_counts=target_counts, new_graphs_generated=0,
              actual_new_lower_bounds=0, CPU_seconds=time.process_time()-START,
              pending=['root generation and independent acceptance'] if success else [],
              scope='Exactly the fixed7 mandatory10-pin sets and every allowed choice of at most2 distinct degree-feasible anchors; no line changes or third anchor')
if success:
    (OUT / 'first_success.json').write_text(json.dumps(success,indent=2)+'\n')
(OUT / 'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
# Keep precise reverse coverage for reuse; this is a bitset/data cache, not a checksum.
covered_targets = sorted(coverers)
(OUT / 'reverse_R4_distances.u8.bin').write_bytes(b''.join(distances[t] for t in covered_targets))
(OUT / 'reverse_coverers.u8.bin').write_bytes(b''.join(coverers[t].to_bytes((len(available)+7)//8,'little') for t in covered_targets))
(OUT / 'coverage_cache.json').write_text(json.dumps(dict(targets=covered_targets,
    available_anchors=available, graph_n=N, distances_row_bytes=N,
    coverers_row_bytes=(len(available)+7)//8, bit_order='little-endian anchor-index bits'),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['target_available_coverer_counts','full_candidate']},indent=2),flush=True)
if success:
    print('FULL_CANDIDATE',json.dumps(success),flush=True)
