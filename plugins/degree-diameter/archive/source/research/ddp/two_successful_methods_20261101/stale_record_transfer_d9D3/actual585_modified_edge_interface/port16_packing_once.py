#!/usr/bin/env python3
"""Owner-avoiding p0 prototype: one unrestricted port16 packing gate."""
import time
START = time.process_time()
import csv
import json
import os
from pathlib import Path
import resource
import traceback

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
OLD = REPO / 'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction'
PRIOR = .800336324
PREP = .2
LIMIT = 17.5
resource.setrlimit(resource.RLIMIT_CPU, (18, 18))


def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')


write('PORT16_HANDLE.json', {'status': 'RUNNING', 'pid': os.getpid(), 'single_worker': True,
    'stage': 'source/cache model binding then eligible mask exactcover',
    'prior_read_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'process_hard_CPU_seconds': 18, 'wholecase_CPU_cap_seconds': 20})
try:
    design = json.loads((OLD / 'BLOCKS.json').read_text())
    ports = design['ports']
    p0 = ports[0]
    assert p0 == 0
    portset = set(ports)
    otherports = [p for p in ports if p != p0]
    portbit = {p: i for i, p in enumerate(otherports)}
    blocks = {row['vertex']: set(row['ports']) for row in design['nonport_blocks']}
    core = set(blocks)
    adj = [set(map(int, line.split())) for line in
           (REPO / 'research/ddp/polarity585_replication/source585.implicit_adj.txt').read_text().splitlines()
           if line.strip()]
    assert len(adj) == 585 and len(core) == 520 and len(ports) == 65
    owner = {}
    for u in core:
        own = adj[u] & portset
        assert len(own) == 1
        owner[u] = next(iter(own))
    coreedges = [(u, v) for u in sorted(core) for v in sorted(adj[u] & core) if u < v]
    assert len(coreedges) == 2080
    oldsigma = {tuple(row['edge']) for row in json.loads((OLD / 'sigma_edge_spread/SIGMA_EDGES.json').read_text())}
    assert len(oldsigma) == 32

    eligible = []
    eligible_degree = {}
    owner_p0_edges = 0
    block_p0_edges = 0
    with (HERE / 'PORT16_ALL2080_CORE_EDGE_BINDINGS.tsv').open('w', newline='') as stream:
        out = csv.writer(stream, delimiter='\t')
        out.writerow(['source_core_edge_id', 'u', 'v', 'owner_u', 'owner_v',
            'C_intersection_size', 'C_union_size', 'p0_in_union', 'owner_p0', 'eligible',
            'legacy_sigma_edge', 'mask64_hex', 'union_actual_port_labels'])
        for eid, (u, v) in enumerate(coreedges):
            intersection = blocks[u] & blocks[v]
            union = blocks[u] | blocks[v]
            assert owner[u] != owner[v]
            assert {owner[u], owner[v]} <= intersection
            assert len(intersection) == 2 and len(union) == 16
            has_p0 = p0 in union
            has_p0_owner = owner[u] == p0 or owner[v] == p0
            owner_p0_edges += has_p0_owner
            block_p0_edges += has_p0
            mask = sum(1 << portbit[p] for p in union if p != p0)
            old = (u, v) in oldsigma
            if not has_p0:
                assert not has_p0_owner
                eligible.append({'id': len(eligible), 'source_core_edge_id': eid,
                    'u': u, 'v': v, 'owners': [owner[u], owner[v]], 'mask': mask,
                    'legacy_sigma': old, 'vertices_mask': (1 << u) | (1 << v)})
                eligible_degree[u] = eligible_degree.get(u, 0) + 1
                eligible_degree[v] = eligible_degree.get(v, 0) + 1
            out.writerow([eid, u, v, owner[u], owner[v], len(intersection), len(union),
                int(has_p0), int(has_p0_owner), int(not has_p0), int(old), hex(mask),
                ','.join(map(str, sorted(union)))])
    assert oldsigma <= {(r['u'], r['v']) for r in eligible}
    write('PORT16_ELIGIBLE_EDGES.json', {
        'p0_actual_vertex_label': p0, 'p0_cached_port_index': 0,
        'mask_bit_to_actual_port': otherports,
        'edges': [{k: v for k, v in r.items() if k not in ('mask', 'vertices_mask')}
                  | {'mask64_hex': hex(r['mask'])} for r in eligible],
        'all32_legacy_edges_retained_for_mixed_packings': True,
    })

    membership = [[] for _ in range(64)]
    for edge in eligible:
        mask = edge['mask']
        while mask:
            bit = (mask & -mask).bit_length() - 1
            mask &= mask - 1
            membership[bit].append(edge['id'])
    full = (1 << 64) - 1
    nodes = 0
    max_depth = 0
    old_only_lastchoices_skipped = 0
    incompatible_vertex_edges = 0
    timeout = False
    solution = None
    first_unfinished_prefix = None
    failed_states = set()
    memo_hits = 0

    def dfs(uncovered, used_vertices, selected, used_non_sigma):
        global nodes, max_depth, old_only_lastchoices_skipped, incompatible_vertex_edges
        global timeout, solution, first_unfinished_prefix, memo_hits
        nodes += 1
        max_depth = max(max_depth, len(selected))
        if time.process_time() - START > LIMIT:
            timeout = True
            first_unfinished_prefix = selected.copy()
            return False
        if uncovered == 0:
            assert len(selected) == 4 and used_non_sigma
            solution = selected.copy()
            return True
        state = (uncovered, used_vertices, used_non_sigma)
        if state in failed_states:
            memo_hits += 1
            return False
        last = len(selected) == 3
        best = None
        pending = uncovered
        while pending:
            bit = (pending & -pending).bit_length() - 1
            pending &= pending - 1
            options = []
            for eid in membership[bit]:
                edge = eligible[eid]
                if last and not used_non_sigma and edge['legacy_sigma']:
                    # Only all-four-old configurations are removed, by their saved complete NO.
                    old_only_lastchoices_skipped += 1
                    continue
                if edge['mask'] & uncovered != edge['mask']:
                    continue
                if edge['vertices_mask'] & used_vertices:
                    incompatible_vertex_edges += 1
                    continue
                options.append(eid)
            if not options:
                failed_states.add(state)
                return False
            if best is None or len(options) < len(best):
                best = options
                if len(best) == 1:
                    break
        for eid in best:
            edge = eligible[eid]
            selected.append(eid)
            if dfs(uncovered ^ edge['mask'], used_vertices | edge['vertices_mask'],
                   selected, used_non_sigma or not edge['legacy_sigma']):
                return True
            selected.pop()
            if timeout:
                return False
        failed_states.add(state)
        return False

    dfs(full, 0, [], False)
    hit = solution is not None
    if hit:
        selected = [eligible[i] for i in solution]
        vertices = [x for e in selected for x in (e['u'], e['v'])]
        assert len(set(vertices)) == 8
        masks = [e['mask'] for e in selected]
        union = 0
        for mask in masks:
            assert not union & mask
            union |= mask
        assert union == full
        write('PORT16_FIRST_PACKING.json', {
            'status': 'NECESSARY_PORT_PACKING_ONLY_NO_GRAPH',
            'p0_actual_vertex_label': p0,
            'cut_edges': [[e['u'], e['v']] for e in selected],
            'core_star_pins': vertices, 'owners': [e['owners'] for e in selected],
            'all_owner_labels_avoid_p0': True, 'eight_actual_core_labels_distinct': True,
            'masks_pairwise_disjoint': True, 'union_actual_ports': otherports,
            'eligible_edge_ids': solution,
            'legacy_sigma_flags': [e['legacy_sigma'] for e in selected],
            'no_core_R2_newroot_or_oldold_D3_claim': True,
        })
    degree_hist = {}
    for value in eligible_degree.values():
        degree_hist[str(value)] = degree_hist.get(str(value), 0) + 1
    complete = not timeout and not hit
    result = {
        'status': ('NECESSARY_PORT16_PACKING_HIT_FULL_GRAPH_UNTESTED' if hit else
                   'UNKNOWN_OWNER_AVOIDING_P0_PORT16_PACKING_CPU_CAP' if timeout else
                   'COMPLETE_NO_FIXED_P0_OWNER_AVOIDING_FOURCUT_STARPORT_PROTOTYPE'),
        'p0_actual_vertex_label': p0, 'p0_cached_port_index': 0,
        'source_core_edges_considered': len(coreedges),
        'source_core_edges_with_p0_owner': owner_p0_edges,
        'source_core_edges_with_p0_in_Cunion': block_p0_edges,
        'eligible_unrestricted_core_edges': len(eligible),
        'eligible_core_vertices': len(eligible_degree), 'eligible_degree_histogram': degree_hist,
        'domain_count_prediction_1568_supported': len(eligible) == 1568,
        'domain_vertex_prediction_448_supported': len(eligible_degree) == 448,
        'domain_degree_prediction7_supported': degree_hist == {'7': 448},
        'old_sigma_edges_retained_for_mixed_domain': len(oldsigma),
        'all_four_old_sigma_subdomain': 'INHERITED_COMPLETE_NO_NOT_REEXECUTED',
        'complete_all_four_old_candidate_evaluations': 0,
        'old_only_lastchoice_filter_visits': old_only_lastchoices_skipped,
        'dfs_nodes': nodes, 'failed_states_saved': len(failed_states), 'memo_hits': memo_hits,
        'maximum_visited_partial_packing_depth': max_depth,
        'explicit_vertex_overlap_rejections': incompatible_vertex_edges,
        'mixed_new_domain_exhausted': complete, 'packing_hit': hit,
        'CPU_cap_stop': timeout, 'first_unfinished_prefix': first_unfinished_prefix,
        'source_literal_parses': 1, 'new_BFS_field_GQ_coreR2_matching_graph_solver_count': 0,
        'scope': 'fixed actual585, p0 actualvertex0, four disjoint corecuts whose endpoint owners all avoidp0, star on8core endpoints+p0, arbitrary perfectmatching other64A; excludes p0-ownercuts and otherp0 choices from conclusion',
        'next': 'STOP; necessary packing hit is not a graph or D3, no p1/seed/matching/candidate continuation',
    }
except Exception as exc:
    result = {'status': 'UNKNOWN_PORT16_INPUT_OR_PROCESS_FAILURE', 'error': str(exc),
        'traceback': traceback.format_exc(), 'scope': 'no mathematical prototype NO from a failure',
        'next': 'STOP preserve failure and budget'}

actual = time.process_time() - START
total = PRIOR + PREP + actual
result.update({'prior_read_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'actual_process_CPU_seconds': actual, 'wholecase_CPU_seconds': total,
    'wholecase_CPU_cap_seconds': 20})
write('PORT16_RESULT.json', result)
write('PORT16_TERMINAL.json', {**result, 'terminal': True, 'active_processes': 0})
write('PORT16_HANDLE.json', {'status': result['status'], 'pid': os.getpid(), 'terminal': True,
    'active_processes': 0, 'wholecase_CPU_seconds': total})
print(json.dumps({k: result[k] for k in ('status', 'eligible_unrestricted_core_edges',
    'eligible_core_vertices', 'eligible_degree_histogram', 'dfs_nodes',
    'packing_hit', 'mixed_new_domain_exhausted', 'wholecase_CPU_seconds', 'error') if k in result}))
