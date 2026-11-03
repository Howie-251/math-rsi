#!/usr/bin/env python3
"""Post-authored reproducer for the two already completed cache probes.

This is not a snapshot of the original exec heredocs. It has been saved without
execution. It never writes into either frozen experiment directory.

Example, to run separately if explicitly requested later:
  python CACHE_PROBE_REPRODUCER.py --output-dir /tmp/d15-cache-reproduction

Only cached balls are read. No source adjacency, new ball, BFS, solver or graph
construction is used. All subset ordering is lexicographic in controller IDs.
"""
from pathlib import Path
import argparse
import itertools
import json
import math
import struct
import time


HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def load_json(path):
    return json.loads(path.read_text())


def write_json(path, value):
    # The containing output directory is newly created by main().
    with path.open('x') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def first_set_bit(bits):
    return (bits & -bits).bit_length() - 1 if bits else None


def derive_selection(table):
    """Use the certified relation, not a stored RESULT or hard-coded ports."""
    assert table['complete']
    q, k = table['bin_size'], table['dimension']
    # Both frozen PREDICTION files explicitly use the homogeneous realization.
    assert all(all(c == 0 for c in arc['c']) for arc in table['arcs'])
    self_arcs = sorted((a for a in table['arcs'] if a['from'] == a['to']),
                       key=lambda a: a['from'])
    assert len({arc['from'] for arc in self_arcs}) == len(self_arcs)
    ports = []
    triangles = []
    for arc in self_arcs:
        a = arc['from']
        v = arc['v']
        assert len(v) == k and v[arc['pivot']] == 1
        offsets = sorted({sum(((t*v[i]) % 3) * 3**i for i in range(k))
                          for t in range(3)})
        assert len(offsets) == 3 and offsets[0] == 0
        ports.append(a*q)
        triangles.append({'controller': a,
                          'old_triangle': [a*q+x for x in offsets]})
    return ports, triangles


def read_selected_cached_balls(n, wanted):
    """Return int bitsets with original target labels as bit indices."""
    wanted = set(wanted)
    full = (1 << n) - 1
    balls = {}
    if n == 15552:
        path = BASE/'d15_D4_current15552/single_vertex_R3_cover/R3_MASKS.bin'
        raw = memoryview(path.read_bytes())
        count, stored_n, words = struct.unpack_from('<III', raw, 0)
        assert (count, stored_n, words) == (648, n, 243)
        stride = 4 + 8*words
        assert len(raw) == 12 + count*stride
        for i in range(count):
            at = 12 + i*stride
            vertex = struct.unpack_from('<I', raw, at)[0]
            if vertex in wanted:
                balls[vertex] = int.from_bytes(raw[at+4:at+stride], 'little') & full
        info = {'path': str(path), 'candidate_rows': count,
                'words_per_ball': words, 'radius': 3,
                'row_labels': 'uint32 label stored before each ball'}
    elif n == 102060:
        folder = BASE/'d15_D5_current102060_source/monotone_R4_cover'
        eligible = [int(x) for x in (folder/'eligible.txt').read_text().split()]
        assert len(eligible) == len(set(eligible)) == 810
        preflight = load_json(folder/'PREFLIGHT.json')
        assert eligible == preflight['eligible_labels']
        words = 1595
        path = folder/'radius4.u64le.bin'
        raw = memoryview(path.read_bytes())
        stride = 8*words
        assert len(raw) == len(eligible)*stride
        for i, vertex in enumerate(eligible):
            if vertex in wanted:
                balls[vertex] = int.from_bytes(raw[i*stride:(i+1)*stride], 'little') & full
        info = {'path': str(path), 'candidate_rows': len(eligible),
                'words_per_ball': words, 'radius': 4,
                'row_labels': str(folder/'eligible.txt')}
    else:
        raise ValueError(f'No frozen cache interface for n={n}')
    assert set(balls) == wanted
    info['selected_rows_loaded'] = len(balls)
    return balls, info


def union_of(pins, balls):
    result = 0
    for pin in pins:
        result |= balls[pin]
    return result


def zero_probe(n, diameter, ports, balls):
    full = (1 << n) - 1
    covered = union_of(ports, balls)
    missing = full & ~covered
    return {'source_n': n, 'D': diameter, 'zero_ports': ports,
            'port_count': len(ports), 'all_zero_ports_actual_free': True,
            'free_binding': 'Every selected label occurs in the frozen original-free ball cache.',
            'cached_balls_loaded': len(ports), 'radius': diameter-1,
            'covered': covered.bit_count(), 'missing': missing.bit_count(),
            'first_missing': first_set_bit(missing), 'union_full': not missing,
            'actual_candidate_n': None, 'actual_candidate_D': None,
            'ordinary_bad_unordered_pairs': None}


def triangle_probe(n, diameter, triangles, balls, deadline_cpu):
    full = (1 << n) - 1
    masks = [union_of(t['old_triangle'], balls) for t in triangles]
    all_union = 0
    for mask in masks:
        all_union |= mask
    missing = full & ~all_union
    planned = math.comb(len(triangles), 5)
    tested = 0
    hit = None
    cursor = None
    last = None
    budget_cut = False
    all_union_gate_rejected = bool(missing)
    if not missing:
        iterator = itertools.combinations(range(len(triangles)), 5)
        for indices in iterator:
            # This tuple is the exact first unattempted object on a cutoff.
            if time.process_time() >= deadline_cpu:
                cursor = indices
                budget_cut = True
                break
            i, j, k, ell, r = indices
            covered = masks[i] | masks[j] | masks[k] | masks[ell] | masks[r]
            tested += 1
            last = indices
            if covered == full:
                pins = sorted({p for t in indices for p in triangles[t]['old_triangle']})
                assert len(pins) == 15
                hit = {'triangle_indices': indices,
                       'controllers': [triangles[t]['controller'] for t in indices],
                       'pins': pins, 'complete_cached_union_covered': n,
                       'scope': 'A necessary helper-zero cover only; no helper graph was built.'}
                cursor = next(iterator, None)
                break
    return {'source_n': n, 'D': diameter,
            'zero_self_triangles': len(triangles),
            'all_triangle_union_missing': missing.bit_count(),
            'all_triangle_union_first_missing': first_set_bit(missing),
            'five_subsets_planned': planned, 'five_subsets_tested': tested,
            'hit': hit, 'budget_cut': budget_cut,
            'all_union_gate_rejected': all_union_gate_rejected,
            'last_tested_triangle_indices': last,
            'next_unattempted_triangle_indices': cursor,
            'next_unattempted_controllers': None if cursor is None else
                [triangles[t]['controller'] for t in cursor],
            'full_fixed_rule_closed': bool(missing) or (tested == planned and hit is None),
            'new_graphs': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True,
                        help='A new directory, separate from the frozen experiments.')
    parser.add_argument('--mode', choices=['zero', 'triangles', 'both'], default='both')
    parser.add_argument('--subset-cpu-seconds', type=float, default=8,
                        help='Aggregate process-CPU deadline for the lex subset stage, including setup; default8.')
    args = parser.parse_args()
    if args.subset_cpu_seconds <= 0:
        parser.error('--subset-cpu-seconds must be positive')
    output = args.output_dir.resolve()
    frozen_dirs = [HERE/'canonical_zero_port_probe', HERE/'selfline_helper9_probe']
    if any(output == d.resolve() or d.resolve() in output.parents for d in frozen_dirs):
        parser.error('Output must be outside both frozen experiment directories.')
    if output.exists():
        parser.error('Output directory must not already exist; no existing results are overwritten.')
    output.mkdir(parents=True)
    start = time.process_time()
    deadline = start + args.subset_cpu_seconds
    zero_pred = load_json(frozen_dirs[0]/'PREDICTION.json')
    triangle_pred = load_json(frozen_dirs[1]/'PREDICTION.json')
    zero_expected = {s['source_n']: s for s in zero_pred['sources']}
    triangle_expected = {s['source_n']: s for s in triangle_pred['sources']}
    zero_results, triangle_results, receipts = [], [], []
    for label, n, diameter in [('source15552', 15552, 4), ('source102060', 102060, 5)]:
        table_path = HERE/'affine_relation_recovery'/f'{label}_AFFINE_RELATIONS.json'
        table = load_json(table_path)
        assert table['n'] == n
        ports, triangles = derive_selection(table)
        assert ports == zero_expected[n]['zero_ports']
        assert triangles == triangle_expected[n]['zero_self_triangles']
        needed = ports if args.mode == 'zero' else [p for t in triangles for p in t['old_triangle']]
        balls, cache_info = read_selected_cached_balls(n, needed)
        receipt = {'source_n': n, 'affine_relation_table': str(table_path),
                   'derived_zero_ports': ports, 'derived_zero_self_triangles': triangles,
                   'cache': cache_info}
        receipts.append(receipt)
        if args.mode in ('zero', 'both'):
            zero_results.append(zero_probe(n, diameter, ports, balls))
        if args.mode in ('triangles', 'both'):
            triangle_results.append(triangle_probe(n, diameter, triangles, balls, deadline))
        # Completed sources are persisted, so an explicit cutoff retains its cursor.
        if zero_results:
            write_or_replace_new_output(output/'canonical_zero_port_RESULT.json', {
                'status': 'REPRODUCED_CANONICAL_ZERO_PORT_UNIONS', 'sources': zero_results})
        if triangle_results:
            write_or_replace_new_output(output/'selfline_helper9_RESULT.json', {
                'status': 'REPRODUCED_COMPLETE_OR_RECORDED_CURSOR', 'sources': triangle_results})
    write_json(output/'REPRODUCTION_RECEIPT.json', {
        'source_code_status': 'Post-authored reproducer, not the original exec heredoc snapshot.',
        'mode': args.mode, 'frozen_inputs_modified': False,
        'frozen_predictions': [str(d/'PREDICTION.json') for d in frozen_dirs],
        'inputs': receipts, 'CPU_seconds': time.process_time()-start,
        'subset_stage_CPU_deadline_seconds': args.subset_cpu_seconds,
        'new_balls': 0, 'BFS': 0, 'solver_calls': 0, 'new_graphs': 0})
    print(output)


def write_or_replace_new_output(path, value):
    # These files live only in the newly created, explicitly selected output dir.
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


if __name__ == '__main__':
    main()
