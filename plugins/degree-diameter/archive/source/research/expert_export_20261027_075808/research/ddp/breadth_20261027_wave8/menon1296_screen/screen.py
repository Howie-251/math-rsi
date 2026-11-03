"""Finite design/group checks only. No incidence-color CSP or full graph is built."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
started = time.process_time()
out = Path(__file__).resolve().parent

def q(x):
    return (((x >> 0) & 1) * ((x >> 1) & 1) +
            ((x >> 2) & 1) * ((x >> 3) & 1)) % 2

D = tuple(x for x in range(16) if q(x) == 1)
blocks = [tuple(sorted(x ^ t for x in D)) for t in range(16)]
assert len(D) == 6 and len(set(blocks)) == 16
assert all(len(b) == 6 for b in blocks)
replications = [sum(p in b for b in blocks) for p in range(16)]
common_blocks = { (u, v): [t for t, b in enumerate(blocks) if u in b and v in b]
                  for u, v in combinations(range(16), 2) }
assert set(replications) == {6}
assert all(len(ts) == 2 for ts in common_blocks.values())
assert all(len(set(a) & set(b)) == 2 for a, b in combinations(blocks, 2))

# Four directions in AG(2,3); the three lines in each direction are
# parametrized consistently by an origin plus t*direction, t=0,1,2.
points = [(x, y) for x in range(3) for y in range(3)]
directions = [(1, 0), (0, 1), (1, 1), (1, 2)]
all_edges = set(combinations(points, 2))
groups = []
edge_class = {}
for c, d in enumerate(directions):
    lines = set()
    for x in points:
        line = tuple(sorted(((x[0] + t*d[0]) % 3, (x[1] + t*d[1]) % 3)
                            for t in range(3)))
        lines.add(line)
    assert len(lines) == 3
    ordered_lines = []
    for line in sorted(lines):
        x = min(line)
        ordered_lines.append([((x[0]+t*d[0]) % 3, (x[1]+t*d[1]) % 3)
                              for t in range(3)])
    for g in range(3):
        edges = [tuple(sorted(line[t] for t in range(3) if t != g))
                 for line in ordered_lines]
        covered = {v for e in edges for v in e}
        assert len(edges) == 3 and len(covered) == 6
        groups.append(dict(c=c, direction=d, g=g, edges=edges,
                           covered_vertices=sorted(covered)))
        for e in edges:
            assert e not in edge_class
            edge_class[e] = c
    for g, h in combinations(range(3), 2):
        a, b = groups[3*c+g], groups[3*c+h]
        assert len(set(map(tuple, a['covered_vertices'])) |
                   set(map(tuple, b['covered_vertices']))) == 9
assert set(edge_class) == all_edges

# Enumerate layer words including backtracking: proving an obstruction for
# all walks suffices for paths. B-B stays in the same design block.
allowed = {'A': ['C'], 'C': ['A', 'B'], 'B': ['B', 'C']}
words_with_A = []
def layer_words(word):
    if len(word) > 1 and word[-1] == 'C' and 'A' in word:
        words_with_A.append(word)
    if len(word)-1 < 4:
        for t in allowed[word[-1]]:
            layer_words(word+t)
layer_words('B')
assert sorted(words_with_A) == ['BB C A C'.replace(' ', ''), 'BCAC']

# The optional translation-invariant color rule already fails: all 15
# pairs of D elements yield different nonzero differences.
diffs = [d ^ e for d, e in combinations(D, 2)]
assert set(diffs) == set(range(1, 16)) and len(diffs) == len(set(diffs))

coordinates = dict(D=D, blocks=[dict(id=t, points=b) for t, b in enumerate(blocks)],
                   AG_points=points, directions=directions, edge_groups=groups,
                   common_block_constraints=[dict(points=[u,v], blocks=ts)
                                             for (u,v),ts in common_blocks.items()])
(out/'design_and_groups.json').write_text(json.dumps(coordinates, indent=2)+'\n')
result = dict(
    status='CLASS_PRESERVING_INCIDENCE_PERMUTATIONS_CANNOT_HAVE_DIAMETER_4',
    design=dict(v=16,b=16,k=6,r=6,lambda_=2,incidences=96),
    proposed_graph=dict(A=144,C=576,B=576,n=1296,m=5184,degree=8,
                        AC_edges=1152,CB_edges=3456,BB_edges=576),
    connected_for_any_incidence_permutations=True,
    local_AC_distance_at_most=3,local_CC_distance_at_most=4,
    AG_groups=dict(groups=12,edges_per_group=3,total_edges=36,
                   same_class_two_different_groups_cover_all9=True),
    B_to_C_layer_words_le4_containing_A=sorted(words_with_A),
    explicit_obstruction=dict(start_B=dict(block_translate=0,block_points=D,
                                          c=0,direction=directions[0],g=0,line=0),
                              end_C=dict(point=0,edge=[[0,0],[0,1]],c=1,
                                         direction=directions[1]),
                              point_not_in_start_block=True,distance_at_least=5),
    forced_bad_unordered_BC_pairs=576*10*27,
    forced_bad_ordered_BC_and_CB_pairs=2*576*10*27,
    general_incidence_color_constraint=dict(variables=96,nonzero_forms=120,
                                            gauge_free_dimensions=65,
                                            feasibility='NOT_SOLVED_NOT_NEEDED_FOR_STRUCTURED_OBSTRUCTION'),
    translation_invariant_color_rule='IMPOSSIBLE_REQUIRES_6_DISTINCT_COLORS',
    unrestricted36_permutation_pi='NOT_EXCLUDED',
    incidence_color_CSP_run=False,full_graph_generated=False,BFS_performed=False,
    CPU_seconds=time.process_time()-started)
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
