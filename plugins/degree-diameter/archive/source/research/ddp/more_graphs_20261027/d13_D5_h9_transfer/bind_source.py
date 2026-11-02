"""Bind only the new degree13 source to its saved H9 split-coordinate data."""
from array import array
from collections import Counter, defaultdict
from pathlib import Path
import json
import lzma
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
OLD = ROOT / 'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout'
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (120, 121))


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + '\n')


def main():
    assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_D13_SOURCE_BINDING'
    adj = []
    for line in (OUT / 'source51417.adjlist.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        row = list(map(int, line.split()))
        assert row[0] == len(adj)
        assert len(row[1:]) == len(set(row[1:])) and row[0] not in row[1:]
        adj.append(set(row[1:]))
    n = len(adj)
    assert n == 51417
    assert all(0 <= v < n and u in adj[v] for u, row in enumerate(adj) for v in row)
    degree = [len(x) for x in adj]
    assert max(degree) == 13
    m = sum(degree) // 2
    witness_path = OLD / 'partial_fold_source/witnesses/pf_d13_k5_n50750.json'
    witness = json.loads(witness_path.read_text())
    bits = [(b >> j) & 1 for b in bytes.fromhex(witness['split']) for j in range(7, -1, -1)][:33033]
    assert sum(bits) == witness['counts']['split_fibers'] == 17157
    qdata = json.loads((OLD / 'Q_data.json').read_text())
    with lzma.open(OLD / 'partial_fold_source/tau.txt.xz', 'rt') as f:
        tau = list(map(int, f.read().split()))
    phi = [tau[tau[p]] for p in range(66430)]
    representatives = [None] * 33397
    raw_labels = [-1] * 66430
    split_fold_ids = []
    for f, p, split in zip(qdata['generic_fold_ids'], qdata['generic_point_representatives'], bits):
        q = phi[p]
        representatives[f] = p
        assert p < q
        raw_labels[p] = p
        raw_labels[q] = q if split else p
        if split:
            split_fold_ids.append(f)
    for f, p in zip(qdata['H3_fold_ids'], qdata['H3_point_representatives']):
        assert phi[p] == p
        representatives[f] = p
        raw_labels[p] = p
    assert min(raw_labels) >= 0
    labels = sorted(set(raw_labels))
    label_index = {p: i for i, p in enumerate(labels)}
    fold = [label_index[p] for p in raw_labels]
    core_n = len(labels)
    assert core_n == 50554
    classes = [sorted({fold[p], fold[phi[p]]}) for p in representatives]
    class_of, swap = [-1] * core_n, list(range(core_n))
    for f, vertices in enumerate(classes):
        for v in vertices:
            assert class_of[v] < 0
            class_of[v] = f
        if len(vertices) == 2:
            swap[vertices[0]], swap[vertices[1]] = vertices[1], vertices[0]
    assert min(class_of) >= 0
    core = [{v for v in adj[u] if v < core_n} for u in range(core_n)]
    core_edges = {(u, v) for u, row in enumerate(core) for v in row if u < v}
    phi_automorphism = all({swap[v] for v in core[u]} == core[swap[u]] for u in range(core_n))
    quotient = {tuple(sorted((class_of[u], class_of[v]))) for u, v in core_edges}
    F = set()
    with lzma.open(OLD / 'duality_source/graph_d10k5_n33397.edges.xz', 'rt') as f:
        assert tuple(map(int, next(f).split())) == (33397, 166425)
        F = {tuple(map(int, line.split())) for line in f if line.strip()}
    quotient_equal = quotient == F
    old_core_edges = set()
    with lzma.open(OLD / 'partial_fold_source/graph_d13k5_n50750.edges.xz', 'rt') as f:
        old_n, old_m = map(int, next(f).split())
        assert old_n == 50750
        for line in f:
            u, v = map(int, line.split())
            if u < core_n and v < core_n:
                old_core_edges.add((u, v))
    constraints = defaultdict(list)
    multiplicity_bad = []
    for u, v in F:
        count = sum(b in core[a] for a in classes[u] for b in classes[v])
        if len(classes[u]) == len(classes[v]) == 2:
            if count not in (2, 4):
                multiplicity_bad.append((u, v, count))
                continue
            parity = int(count == 2)
            constraints[u].append((v, parity))
            constraints[v].append((u, parity))
        elif count != len(classes[u]) * len(classes[v]):
            multiplicity_bad.append((u, v, count))
    colors, consistent, components = {}, True, 0
    for start in split_fold_ids:
        if start in colors:
            continue
        components += 1
        colors[start] = 0
        todo = [start]
        for u in todo:
            for v, parity in constraints[u]:
                if v in colors:
                    consistent &= colors[v] == colors[u] ^ parity
                else:
                    colors[v] = colors[u] ^ parity
                    todo.append(v)
    old_color = [(b >> j) & 1 for b in bytes.fromhex(witness['colour']) for j in range(7, -1, -1)][:33033]
    old_by_fold = {f: c for f, c in zip(qdata['generic_fold_ids'], old_color)}
    old_color_edge_parity_mismatches = sum((old_by_fold[u] ^ old_by_fold[v]) != p
                                           for u, row in constraints.items() for v, p in row if u < v)
    h3vertices = [fold[p] for p in qdata['H3_point_representatives']]
    h3_signatures = defaultdict(list)
    for v in h3vertices:
        h3_signatures[tuple(sorted(core[v]))].append(v)
    extra_rows = []
    initial_h3_copy_prefix = 0
    for v in range(core_n, n):
        pins = tuple(sorted(w for w in adj[v] if w < core_n))
        parents = h3_signatures.get(pins, [])
        if v == core_n + initial_h3_copy_prefix and parents:
            initial_h3_copy_prefix += 1
        extra_rows.append({'vertex': v, 'core_pin_count': len(pins),
                           'extra_neighbor_count': sum(w >= core_n for w in adj[v]),
                           'H3_core_star_signature_parents': parents})
    binding_ok = quotient_equal and phi_automorphism and not multiplicity_bad and consistent
    result = {
        'status': 'D13_CORE_PARTITION_BOUND' if binding_ok else 'D13_BINDING_GAP',
        'target_Delta': 13, 'target_D': 5, 'public_savedL': 51417,
        'source_n': n, 'source_m': m, 'source_simple_symmetric': True,
        'source_degree_histogram': dict(sorted(Counter(degree).items())),
        'source_D5_status': 'Public reported D5 inherited; no allsource BFS in this task.',
        'old_author_witness': str(witness_path.relative_to(ROOT)),
        'old_author_split_fibers': sum(bits), 'core_n': core_n, 'extras': n - core_n,
        'core_edges': len(core_edges), 'core_degree_histogram': dict(sorted(Counter(map(len, core)).items())),
        'class_size_histogram': dict(Counter(map(len, classes))),
        'candidate_same_old_split_set': True, 'old_pi12_reused': False,
        'label_rule': 'Oldauthor rawpoint labels, mergedpair leastpoint, splitpoint separate; numbered by sortedlabels.',
        'exact_quotient_F33397_edges_match': quotient_equal,
        'simultaneous_pair_swap_is_core_automorphism': phi_automorphism,
        'core_edges_equal_old_author_core': core_edges == old_core_edges,
        'old_core_edges_missing': len(old_core_edges - core_edges),
        'new_core_edges_not_in_old': len(core_edges - old_core_edges),
        'first_old_core_edges_missing': sorted(old_core_edges - core_edges)[:10],
        'first_new_core_edges_not_in_old': sorted(core_edges - old_core_edges)[:10],
        'edge_multiplicity_model_errors': multiplicity_bad[:10],
        'split_color_parity_consistent': consistent, 'split_color_components': components,
        'old_colour_edge_parity_mismatches': old_color_edge_parity_mismatches,
        'initial_H3_core_star_signature_prefix': initial_h3_copy_prefix,
        'extras_with_H3_core_star_signature': sum(bool(x['H3_core_star_signature_parents']) for x in extra_rows),
        'core_vertices_with_free_slot': sum(degree[v] < 13 for v in range(core_n)),
        'extra_vertices_with_free_slot': sum(degree[v] < 13 for v in range(core_n, n)),
        'all_free_slots': sum(13 - d for d in degree),
        'core_free_slots': sum(13 - degree[v] for v in range(core_n)),
        'extra_free_slots': sum(13 - degree[v] for v in range(core_n, n)),
        'Redei15_budget': 'F3stable placement has10+s mandatorypins; Delta13 allows0<=s<=3 and atmost3-s distinctoldanchors.',
        'mapping_restored_for_tau_stable_pinsets': binding_ok,
        'full_raw_orientation_binding': core_edges == old_core_edges,
        'point_map_binding_scope': 'Exactcurrent coreclass supports over labelled F33397. Within each splitpair the deterministic saved numbering suffices for tau-stable pinsets; a full raw H9 orientation is not asserted.',
        'uniform_core_transfer': 'Every Fedge block is complete or a perfectmatching by checked multiplicities and simultaneousswap. Hence Fwalks lift from every currentcorevertex. Tau-stable raw B selects wholeclasses, proving its currentcore R4 coverage from the inherited Fpolar theorem.',
        'point_to_core_file': 'point_to_core13.u16.bin' if binding_ok else None,
        'pool_generated': False, 'coverage_search': False, 'BFS_count': 0,
        'CPU_seconds': time.process_time() - START,
    }
    if binding_ok:
        (OUT / 'point_to_core13.u16.bin').write_bytes(array('H', fold).tobytes())
        save('fold13_classes.json', {'classes': classes, 'point_representatives': representatives,
                                    'split_fold_ids': split_fold_ids,
                                    'recovered_color_parity': [{'fold': k, 'color': colors[k]} for k in sorted(colors)]})
    save('source_degrees.json', {'n': n, 'm': m, 'degrees': degree,
                                 'available_vertices': [v for v in range(n) if degree[v] < 13]})
    (OUT / 'degree13.u8.bin').write_bytes(bytes(degree))
    with (OUT / 'source51417.edges').open('w') as f:
        f.write(f'{n} {m}\n')
        for u, row in enumerate(adj):
            for v in sorted(row):
                if u < v:
                    f.write(f'{u} {v}\n')
    save('extras_profile.json', {'core_n': core_n, 'source_n': n, 'records': extra_rows})
    save('RESULT.json', result)
    save('terminal.json', {**result, 'running': False})
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
