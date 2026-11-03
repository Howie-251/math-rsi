#!/usr/bin/env python3
"""Exact diagnostic of the four-label covering charge; not a graph search."""
import itertools
import json
from pathlib import Path

rows = []
base_edges = {(0, 1), (1, 2), (2, 3), (0, 3)}
for diagonals in itertools.product((0, 1), repeat=2):
    edges = base_edges | ({(0, 2)} if diagonals[0] else set()) | ({(1, 3)} if diagonals[1] else set())
    accepted = 0
    minimum = 20
    equality = set()
    for counts in itertools.product(range(4), repeat=4):
        d_x = sum(counts)
        if d_x > 8:
            continue
        for private_mask in range(16):
            private = {i for i in range(4) if private_mask & (1 << i)}
            if d_x + len(private) > 8:
                continue
            cover = [counts[(i-1)%4] + counts[i] + (i in private) for i in range(4)]
            if min(cover) < 1:
                continue
            h = sum(i in private and j in private for i, j in edges)
            accepted += 1
            minimum = min(minimum, d_x + h)
            assert d_x + h >= 2, (diagonals, counts, sorted(private))
            if d_x + h == 2:
                equality.add((d_x, h))
    rows.append({'private_diagonals':list(diagonals), 'covering_patterns':accepted,
                 'minimum_dX_plus_private_edges':minimum, 'equality_pairs':sorted(equality)})
report = {
    'question':'Four-cycle private graph covering charge d_X(w)+h(w)>=2',
    'arithmetic':'exact integers', 'cpu_limit':'one process; no solver',
    'scope':'All four X-type counts from 0 through 3 and all 16 private-neighbor masks, total degree<=8; not complete 59-vertex graphs',
    'results':rows,
    'global_counts':{'outside_W':39,'X_W_edges':72,'minimum_private_edge_W_triangles':2*39-72,
                     'minimum_triangle_incidence_at_private_vertices':2*(2*39-72),
                     'maximum_if_private_C4':4*2},
    'mathematical_proof':'proofs/dd82/n59/h5_zero_r2_c4_interface_20261011.md'
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
