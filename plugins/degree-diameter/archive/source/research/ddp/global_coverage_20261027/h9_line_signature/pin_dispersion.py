"""One structural witness, without distances or geometric reconstruction."""
import json
import time
from itertools import combinations
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
start = time.process_time()
screen = json.loads((OUT / 'necessary_filter.json').read_text())
witness = screen['first_pre165_failure']
assert witness['vertex'] == 41502
pins = witness['A_i']
K = 41356
core = []
source = ROOT / 'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
with source.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):
            continue
        row = list(map(int, line.split()))
        if row[0] >= K:
            break
        assert row[0] == len(core)
        core.append(set(v for v in row[1:] if v < K))
pairs = []
for a, b in combinations(pins, 2):
    pairs.append(dict(a=a, b=b, adjacent=b in core[a],
                      common_core_neighbors=sorted(core[a] & core[b]),
                      closed_neighborhood_intersection=sorted((core[a] | {a}) & (core[b] | {b}))))
assert len(pairs) == 45
assert not any(p['adjacent'] or p['common_core_neighbors'] for p in pairs)
signature_path = ROOT / 'research/ddp/global_coverage_20261027/h9_relation/current_extra_signatures.json'
signature = next(r for r in json.loads(signature_path.read_text())['records'] if r['vertex'] == 41502)
assert signature['current_extra_neighbors'] == []
result = dict(vertex=41502, pins=pins, pin_core_degrees=[len(core[a]) for a in pins],
              unordered_pin_pairs=45, adjacent_pairs=0, pairs_with_common_core_neighbor=0,
              all_pair_core_distance_lower_bound=3, exact_core_distances_computed=False,
              all_closed_radius1_neighborhoods_disjoint=True, pair_evidence=pairs,
              earlier_extra_neighbors=[], later_extra_neighbors=[],
              new_vertex_connects_all_45_pin_pairs_by_two_edges=True,
              BFS_performed=False, geometric_incidence_rebuilt=False,
              CPU_seconds=time.process_time() - start)
(OUT / 'first41502_dispersion.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'pair_evidence'}, indent=2))
