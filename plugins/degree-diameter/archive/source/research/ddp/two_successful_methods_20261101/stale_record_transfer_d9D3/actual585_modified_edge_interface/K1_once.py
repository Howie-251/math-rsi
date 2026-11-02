#!/usr/bin/env python3
"""One owner-p0 mask plus three far masks; optional new-root core support."""
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
PRIOR = 1.881081201
PREP = .20
READER = .30
LIMIT = 16.8
resource.setrlimit(resource.RLIMIT_CPU, (17, 17))


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + '\n')


write('K1_HANDLE.json', {'status': 'RUNNING', 'pid': os.getpid(), 'single_worker': True,
    'stage': 'reuse saved owner64/far1568 mask domain', 'prior_case_CPU_seconds': PRIOR,
    'new_preparation_charge_CPU_seconds': PREP, 'independent_reader_charge_CPU_seconds': READER,
    'wholecase_CPU_cap_seconds': 20, 'process_hard_CPU_seconds': 17})
result = None
try:
    saved_far = json.loads((HERE / 'PORT16_ELIGIBLE_EDGES.json').read_text())
    assert saved_far['p0_actual_vertex_label'] == saved_far['p0_cached_port_index'] == 0
    ports = [0] + saved_far['mask_bit_to_actual_port']
    assert len(ports) == len(set(ports)) == 65
    port_index = {p: i for i, p in enumerate(ports)}
    owner_edges = []
    all_core = set()
    with (HERE / 'PORT16_ALL2080_CORE_EDGE_BINDINGS.tsv').open() as stream:
        for row in csv.DictReader(stream, delimiter='\t'):
            u, v = int(row['u']), int(row['v'])
            all_core.update((u, v))
            if int(row['owner_p0']):
                ou, ov = int(row['owner_u']), int(row['owner_v'])
                free_owner = ov if ou == 0 else ou
                assert free_owner != 0 and (ou == 0) != (ov == 0)
                mask = (int(row['mask64_hex'], 16) << 1) | 1
                assert mask.bit_count() == 16
                owner_edges.append({'source_core_edge_id': int(row['source_core_edge_id']),
                    'u': u, 'v': v, 'owners': [ou, ov], 'free_owner': free_owner,
                    'mask': mask, 'vertices': (1 << u) | (1 << v)})
    far_edges = []
    for row in saved_far['edges']:
        mask = int(row['mask64_hex'], 16) << 1
        assert mask.bit_count() == 16 and mask & 1 == 0
        far_edges.append({**row, 'mask': mask, 'vertices': (1 << row['u']) | (1 << row['v'])})
    assert len(owner_edges) == 64 and len(far_edges) == 1568 and len(all_core) == 520
    membership = [[] for _ in range(65)]
    for eid, edge in enumerate(far_edges):
        mask = edge['mask']
        while mask:
            bit = (mask & -mask).bit_length() - 1
            mask &= mask - 1
            membership[bit].append(eid)
    write('K1_DOMAIN.json', {
        'p0_actual_vertex_label': 0, 'p0_cached_port_index': 0,
        'mask_bit_to_actual_vertex': ports,
        'owner64': [{k: v for k, v in e.items() if k not in ('mask', 'vertices')}
                    | {'mask65_hex': hex(e['mask'])} for e in owner_edges],
        'far1568_reference': 'PORT16_ELIGIBLE_EDGES.json; shift each saved mask left by1',
        'legacy_sigma_far_edges_retained': True,
        'no_k0_or_sigma_search_reexecuted': True,
    })
    full = (1 << 65) - 1
    nodes = 0
    port_packings = 0
    core_fail = 0
    allnew_pass = False
    timeout = False
    completed_owners = 0
    current_owner_id = -1
    old_adj = None
    support = None
    core_vertices = sorted(all_core)
    core_index = {v: i for i, v in enumerate(core_vertices)}
    core_full = (1 << 520) - 1
    source_parses = 0
    support_builds = 0
    first_port_packing = None
    first_core_missing = None
    first_unfinished = None
    packing_stages = (HERE / 'K1_ALL_PACKING_CORE_STAGES.tsv').open('w', newline='')
    out = csv.writer(packing_stages, delimiter='\t')
    out.writerow(['packing_id', 'owner_domain_id', 'owner_source_edge_id', 'far0', 'far1', 'far2',
        'core_pin_labels', 'free_owner_a', 'omitted_actual_port_t', 'forced4_matching_pairs',
        'core_targets_covered', 'first_missing_core', 'missing_core_mask_hex', 'stage'])
    owner_stage = (HERE / 'K1_OWNER_DOMAIN_STAGES.tsv').open('w', newline='')
    owner_out = csv.writer(owner_stage, delimiter='\t')
    owner_out.writerow(['owner_domain_id', 'source_core_edge_id', 'DFS_nodes_in_domain',
        'port_packings_in_domain', 'status'])

    def build_core_support():
        global old_adj, support, source_parses, support_builds
        if support is not None:
            return
        old_adj = [set(map(int, line.split())) for line in
            (REPO / 'research/ddp/polarity585_replication/source585.implicit_adj.txt').read_text().splitlines()
            if line.strip()]
        assert len(old_adj) == 585
        source_parses += 1
        support = {}
        with (HERE / 'K1_CORE_TARGET_R2_SUPPORTS.tsv').open('w', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t')
            writer.writerow(['old_pin_vertex_label', 'core_target_support_hex'])
            for root in sorted(all_core | {0}):
                ball = {root} | old_adj[root]
                for neighbor in old_adj[root]:
                    ball.update(old_adj[neighbor])
                mask = sum(1 << core_index[v] for v in ball if v in all_core)
                support[root] = mask
                writer.writerow([root, hex(mask)])
        write('K1_CORE_TARGET_SUPPORT_SCHEMA.json', {
            'core_bit_to_actual_vertex': core_vertices,
            'support_root_count': len(support), 'scope': 'new k1 new-root core-target R2 support, direct0/1/2 old-edge composition',
            'source_D3_validity_BFS': 0, 'ordinary_BFS': 0,
        })
        support_builds += 1

    def packing_test(owner, selected_far, omitted_bit):
        global port_packings, core_fail, allnew_pass, first_port_packing, first_core_missing
        edges = [owner] + [far_edges[i] for i in selected_far]
        vertices = [x for e in edges for x in (e['u'], e['v'])]
        assert len(set(vertices)) == 8
        union = 0
        for edge in edges:
            assert not union & edge['mask']
            union |= edge['mask']
        assert union.bit_count() == 64 and full ^ union == (1 << omitted_bit)
        omitted = ports[omitted_bit]
        a = owner['free_owner']
        assert omitted != 0 and omitted != a
        pairs = [sorted(e['owners']) for e in edges[1:]] + [sorted([a, omitted])]
        assert len({x for pair in pairs for x in pair}) == 8
        star_pins = sorted([0] + vertices)
        build_core_support()
        coverage = 0
        for pin in star_pins:
            coverage |= support[pin]
        missing = core_full ^ coverage
        missed = [core_vertices[i] for i in range(520) if missing & (1 << i)]
        status = 'CORE_FAIL' if missed else 'ALL_NEWROOT_PASS_OLDOLD_UNTESTED'
        pid = port_packings
        port_packings += 1
        record = {
            'packing_id': pid, 'owner_domain_id': current_owner_id,
            'p0_actual_vertex_label': 0, 'p0_port_index': 0,
            'cut_edges': [sorted([e['u'], e['v']]) for e in edges],
            'mask65_hex': [hex(e['mask']) for e in edges],
            'source_core_edge_ids': [e['source_core_edge_id'] for e in edges],
            'far_ids': selected_far.copy(), 'eight_core_labels': vertices,
            'star_pins': star_pins, 'free_owner_a': a, 'omitted_actual_port_t': omitted,
            'forced4_matching_pairs': pairs, 'remaining_absolute_vertices_to_match': 56,
            'core_targets_covered': coverage.bit_count(), 'missing_core_targets': missed,
            'core_support_for_each_pin': [{'actual_pin': pin, 'core_mask_hex': hex(support[pin])} for pin in star_pins],
            'stage': status, 'full_graph_generated': False, 'oldold_D3_tested': False,
        }
        out.writerow([pid, current_owner_id, owner['source_core_edge_id'], *selected_far,
            ','.join(map(str, vertices)), a, omitted, json.dumps(pairs), coverage.bit_count(),
            missed[0] if missed else -1, hex(missing), status])
        if first_port_packing is None:
            first_port_packing = pid
            first_core_missing = missed[0] if missed else None
            write('K1_FIRST_PORT_PACKING.json', record)
        if missed:
            core_fail += 1
            return False

        # Explicit <=3 paths for this new-root obligation only. No graph or BFS.
        cuts = {tuple(sorted([e['u'], e['v']])) for e in edges}

        def old_pin_route(target):
            if target in star_pins:
                return [585, target]
            for pin in star_pins:
                if target in old_adj[pin] and tuple(sorted((pin, target))) not in cuts:
                    return [585, pin, target]
            for pin in star_pins:
                for mid in sorted(old_adj[pin]):
                    if tuple(sorted((pin, mid))) in cuts:
                        continue
                    if target in old_adj[mid] and tuple(sorted((mid, target))) not in cuts:
                        return [585, pin, mid, target]
            return None

        a_pin = owner['u'] if owner['owners'][0] == a else owner['v']
        with (HERE / 'K1_ALL_NEWROOT_PASS_ROUTES.tsv').open('w', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t')
            writer.writerow(['actual_target_vertex', 'type', 'actual_route', 'uses_forced_matching_edge'])
            for target in range(585):
                route = old_pin_route(target)
                forced = False
                if route is None and target == omitted:
                    route = [585, a_pin, a, omitted]
                    forced = True
                assert route is not None and len(route) - 1 <= 3
                assert len(set(route)) == len(route)
                writer.writerow([target, 'core' if target in all_core else 'absolute',
                    ','.join(map(str, route)), int(forced)])
        write('K1_FIRST_ALL_NEWROOT_PASS.json', record)
        allnew_pass = True
        return True

    def dfs(owner, uncovered, used_vertices, selected, omitted_bit):
        global nodes, timeout, first_unfinished
        nodes += 1
        if time.process_time() - START >= LIMIT:
            timeout = True
            first_unfinished = {'owner_domain_id': current_owner_id, 'far_prefix': selected.copy(),
                'omitted_bit': omitted_bit, 'remaining_mask65_hex': hex(uncovered)}
            return False
        if len(selected) == 3:
            if omitted_bit is None:
                assert uncovered.bit_count() == 1
                omitted_bit = (uncovered & -uncovered).bit_length() - 1
            else:
                assert uncovered == 0
            return packing_test(owner, selected, omitted_bit)
        best = None
        chosen_bit = None
        pending = uncovered
        while pending:
            bit = (pending & -pending).bit_length() - 1
            pending &= pending - 1
            options = []
            for eid in membership[bit]:
                edge = far_edges[eid]
                if edge['mask'] & uncovered != edge['mask'] or edge['vertices'] & used_vertices:
                    continue
                options.append(eid)
            if best is None or len(options) < len(best):
                best, chosen_bit = options, bit
                if not best:
                    break
        if not best:
            if omitted_bit is None:
                return dfs(owner, uncovered ^ (1 << chosen_bit), used_vertices, selected, chosen_bit)
            return False
        for eid in best:
            edge = far_edges[eid]
            selected.append(eid)
            if dfs(owner, uncovered ^ edge['mask'], used_vertices | edge['vertices'], selected, omitted_bit):
                return True
            selected.pop()
            if timeout:
                return False
        if omitted_bit is None:
            return dfs(owner, uncovered ^ (1 << chosen_bit), used_vertices, selected, chosen_bit)
        return False

    # No failure memo: core support depends on actual selected pin labels.
    for oid, owner in enumerate(owner_edges):
        current_owner_id = oid
        before_nodes, before_pack = nodes, port_packings
        dfs(owner, full ^ owner['mask'], owner['vertices'], [], None)
        owner_out.writerow([oid, owner['source_core_edge_id'], nodes - before_nodes,
            port_packings - before_pack, 'ALL_NEWROOT_PASS' if allnew_pass else 'CPU_CAP' if timeout else 'COMPLETE'])
        if allnew_pass or timeout:
            break
        completed_owners += 1
    packing_stages.close()
    owner_stage.close()
    complete = completed_owners == 64 and not timeout and not allnew_pass
    result = {
        'status': ('K1_ALL_NEWROOT_COVER_PASS_FULL_GRAPH_OLDOLD_MATCHING_PENDING' if allnew_pass else
                   'COMPLETE_NO_FIXED_P0_K1_PROTOTYPE_BY_NEWROOT_OBLIGATION' if complete else
                   'UNKNOWN_FIXED_P0_K1_PROTOTYPE_CPU_CAP'),
        'owner_edge_domain': len(owner_edges), 'far_edge_domain': len(far_edges),
        'completed_owner_domains': completed_owners, 'current_owner_domain_id': current_owner_id,
        'full_k1_domain_exhausted': complete, 'DFS_nodes': nodes,
        'necessary_port_packings': port_packings, 'core_failed_packings': core_fail,
        'all_newroot_cover_pass': allnew_pass, 'first_port_packing_id': first_port_packing,
        'first_packing_first_missing_core': first_core_missing,
        'first_unfinished_prefix': first_unfinished, 'CPU_cap_stop': timeout,
        'source_literal_parse_count': source_parses, 'new_question_core_R2_support_builds': support_builds,
        'source_D3_field_ordinaryBFS_remaining56matching_fullgraph_solver_Lean_or_reviews': 0,
        'p0_actual_vertex_label': 0, 'p0_cached_port_index': 0,
        'scope': 'fixedactual585, p0actual0, exactlyoneownerp0 corecut plus3far cuts, one8core+p0star andperfectmatchingother64A; portpacking plus allnewroot obligation only',
        'next': 'STOP; any remaining56 matching or oldoldD3/full586 graph requires root authorization',
    }
except Exception as exc:
    result = {'status': 'UNKNOWN_K1_PROCESS_OR_INPUT_FAILURE', 'error': str(exc),
        'traceback': traceback.format_exc(), 'scope': 'no uncompleted domain NO from failure',
        'next': 'STOP preserve costs and failure'}

actual = time.process_time() - START
total = PRIOR + PREP + READER + actual
result.update({'prior_case_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'independent_reader_charge_CPU_seconds': READER, 'actual_process_CPU_seconds': actual,
    'wholecase_CPU_seconds': total, 'wholecase_CPU_cap_seconds': 20})
write('K1_RESULT.json', result)
write('K1_TERMINAL.json', {**result, 'terminal': True, 'active_processes': 0})
write('K1_HANDLE.json', {'status': result['status'], 'pid': os.getpid(), 'terminal': True,
    'active_processes': 0, 'wholecase_CPU_seconds': total})
print(json.dumps(result))
