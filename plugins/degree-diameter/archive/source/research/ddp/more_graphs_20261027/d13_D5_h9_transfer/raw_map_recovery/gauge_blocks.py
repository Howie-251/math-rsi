"""One finite block-invariant test, not a graph-distance or pool search."""
from collections import Counter, defaultdict
from pathlib import Path
import json
import lzma
import resource
import time

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
ROOT = BASE.parents[3]
OLD = ROOT / 'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout'
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (120, 121))


def main():
    assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_GAUGE_WITNESS_TEST'
    data = json.loads((BASE / 'fold13_classes.json').read_text())
    classes = data['classes']
    representatives = data['point_representatives']
    class_of = [-1] * 50554
    for f, vertices in enumerate(classes):
        for v in vertices:
            class_of[v] = f
    old_blocks, current_blocks = defaultdict(list), defaultdict(list)
    with lzma.open(OLD / 'partial_fold_source/graph_d13k5_n50750.edges.xz', 'rt') as f:
        assert int(next(f).split()[0]) == 50750
        for line in f:
            u, v = map(int, line.split())
            if u < 50554 and v < 50554:
                key = tuple(sorted((class_of[u], class_of[v])))
                old_blocks[key].append([u, v])
    with (BASE / 'source51417.edges').open() as f:
        assert tuple(map(int, next(f).split())) == (51417, 324451)
        for line in f:
            u, v = map(int, line.split())
            if u < 50554 and v < 50554:
                key = tuple(sorted((class_of[u], class_of[v])))
                current_blocks[key].append([u, v])
    assert set(old_blocks) == set(current_blocks)
    changed_counts = [[u, v, len(old_blocks[u, v]), len(current_blocks[u, v])]
                      for u, v in sorted(old_blocks)
                      if len(old_blocks[u, v]) != len(current_blocks[u, v])]
    count_types = Counter((a, b) for _, _, a, b in changed_counts)
    witness_key = next((u, v) for u, v, a, b in changed_counts if a == 4 and b == 2)
    with lzma.open(OLD / 'partial_fold_source/tau.txt.xz', 'rt') as f:
        source_duality = list(map(int, f.read().split()))
    def info(key):
        u, v = key
        return {'F_edge': [u, v], 'current_class_vertices': [classes[u], classes[v]],
                'raw_point_pair_classes': [[representatives[k], source_duality[source_duality[representatives[k]]]]
                                          for k in key],
                'old_core_edges': sorted(old_blocks[key]),
                'current_core_edges': sorted(current_blocks[key]),
                'old_block_edges': len(old_blocks[key]), 'current_block_edges': len(current_blocks[key])}
    reverse_key = next((u, v) for u, v, a, b in changed_counts if a == 2 and b == 4)
    same_count_changed = [key for key in sorted(old_blocks)
                          if len(old_blocks[key]) == len(current_blocks[key])
                          and sorted(old_blocks[key]) != sorted(current_blocks[key])]
    result = {
        'status': 'PAIR_FLIP_GAUGE_REFUTED_BY_BLOCK_CARDINALITY',
        'source_core_n': 50554, 'quotient_edges_examined': len(old_blocks),
        'old_core_edges': sum(map(len, old_blocks.values())),
        'current_core_edges': sum(map(len, current_blocks.values())),
        'block_edge_count_mismatches': len(changed_counts),
        'block_edge_count_change_histogram': [{'old': a, 'current': b, 'F_edges': n}
                                             for (a, b), n in sorted(count_types.items())],
        'same_count_but_changed_edge_blocks': len(same_count_changed),
        'old4_current2_witness': info(witness_key),
        'old2_current4_example': info(reverse_key),
        'reason': 'A permutation preserving each Fclass setwise is a bijection on each bipartite edgeblock. It preserves its edgecount. The old4/current2 block forbids equality and even oldedge homomorphism under any such pairflips.',
        'P_GAUGE': 'SUPPORTED_NO_GAUGE',
        'orientation_correct_mapping_exported': False,
        'scope': 'No classpreserving pairflip can transfer the fixed old13partialfold graph. This is not an exclusion of every possible colourdependent rawH9 realization.',
        'BFS': 0, 'Baer_pools_generated': 0, 'CPU_seconds': time.process_time() - START,
    }
    (OUT / 'block_count_changes.json').write_text(json.dumps(changed_counts, separators=(',', ':')) + '\n')
    (OUT / 'GAUGE_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
