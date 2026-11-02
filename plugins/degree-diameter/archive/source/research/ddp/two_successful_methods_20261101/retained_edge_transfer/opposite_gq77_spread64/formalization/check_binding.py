"""Literal readback and streamed formula equality only; no distance traversal."""
import ast
import json
import time
from pathlib import Path

D = Path(__file__).resolve().parent
P = D.parent
R = Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
F = R / 'formal/DegreeDiameter/Portfolio'
t0 = time.process_time()
x = json.loads((P / 'PARAMETERS.json').read_text())
lp = [r['points'] for r in x['lines']]
pl = x['point_incident_lines']
sp = x['spread_line_labels']
owner = x['point_spread_owner']

def literal(path, name):
    line = next(s for s in path.read_text().splitlines() if s.startswith('def ' + name + ' '))
    return ast.literal_eval(line.split(' := ', 1)[1].replace('![', '['))

def flat(a):
    assert len(a) == 20 and all(len(b) == 20 for b in a)
    return [r for b in a for r in b]

defs = F / 'OppositeGQ77SpreadDefinitions.lean'
assert flat(literal(defs, 'linePointBlocks')) == lp
assert flat(literal(defs, 'pointLineBlocks')) == pl
assert literal(defs, 'spread') == sp
assert flat(literal(defs, 'spreadOwnerBlocks')) == owner
assert all(0 <= v < 400 for row in lp + pl for v in row)
assert all(0 <= v < 400 for v in sp) and all(0 <= v < 50 for v in owner)
assert sorted(p for j in range(50) for p in lp[sp[j]]) == list(range(400))
assert all([j for j in range(50) if p in lp[sp[j]]] == [owner[p]] for p in range(400))
ix = json.loads((P / 'PROJECTION_INDEX_INPUTS.json').read_text())['point_rows']
for p in range(400):
    actual = flat(literal(F / f'OppositeGQ77SpreadInputRow{p:03}.lean', f'projectionIndicesBlocks{p:03}'))
    assert [list(t) for t in actual] == ix[p]
    assert all(0 <= v < 8 for t in actual for v in t)

steps = json.loads((P / 'EXTENSION_STEPS.json').read_text())['steps']
assert len(steps) == 50
for j, step in enumerate(steps):
    pins = [400*p+l for p in lp[sp[j]] for l in pl[p]]
    assert len(pins) == len(set(pins)) == 64
    assert step['step'] == j and step['spread_line'] == sp[j]
    assert step['new_vertex'] == 160000+j and step['pins'] == pins

edgepath = P / 'graph_d64_D3_n160050.edges'
count = old_count = bonus_count = 0
previous = (-1, -1)
with edgepath.open() as f:
    assert tuple(map(int, next(f).split())) == (160050, 5121600)
    for u in range(160000):
        p, l = divmod(u, 400)
        neighbors = [400*q+m for q in lp[l] for m in pl[p] if 400*q+m != u]
        if p in lp[l]:
            neighbors.append(160000+owner[p])
        assert len(neighbors) == len(set(neighbors)) == 64
        for v in sorted(neighbors):
            if v <= u:
                continue
            actual = tuple(map(int, next(f).split()))
            assert actual == (u, v) and previous < actual
            previous = actual
            count += 1
            if v < 160000:
                old_count += 1
            else:
                bonus_count += 1
    assert next(f, None) is None
assert (count, old_count, bonus_count) == (5121600, 5118400, 3200)
result = {
    'status': 'PASS_EXACT_LITERAL_READBACK_ORDERED_PINS_AND_STREAMED_EDGE_FORMULA',
    'linePoint_entries_exact': 3200, 'pointLine_entries_exact': 3200,
    'ordered_spread_labels_exact': 50, 'spreadOwner_entries_exact': 400,
    'owner_lookup_equals_actual_spread_membership_at_every_point': True,
    'ordered_projection_triples_exact': 160000,
    'all_Fin_literals_within_intended_bounds': True,
    'lookup_layout': 'row-major 20x20, original Fin400 index unchanged',
    'ordered_new_vertices': 'j=0..49, literal label160000+j',
    'ordered_pins': 'all50 rows, each64 entries equals actual step pins at same index',
    'actual_graph_carrier': 'Fin160000 sum Fin50, with explicit equivalence to Fin160050',
    'literal_edges_compared_one_by_one': count,
    'old_formula_edges': old_count, 'new_formula_edges': bonus_count, 'new_new_edges': 0,
    'ASCII_parser_formalized': False,
    'BFS_or_solver_runs': 0, 'independent_acceptance_claim': False,
    'CPU_seconds': time.process_time()-t0
}
(D / 'INPUT_BINDING_CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
