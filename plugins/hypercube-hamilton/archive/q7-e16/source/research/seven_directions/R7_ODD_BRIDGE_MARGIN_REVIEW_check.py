"""Independent fixed-input arithmetic only; no producer imports or solver."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8-sig'))
def digest(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
def canon(edges):
    return sorted(tuple(sorted(e)) for e in edges)
def parity(x):
    return x.bit_count() % 2
def short(a, b):
    return (a ^ b).bit_count() == 1
def matching(edges, n):
    flat = [x for e in edges for x in e]
    assert len(flat) == len(set(flat))
    assert all(0 <= x < 2**n for x in flat)
    assert all(short(a, b) for a, b in edges)
    return set(range(2**n)) - set(flat)
def directions(edges, n):
    return [sum(a ^ b == 1 << k for a, b in edges) for k in range(n)]

inputs = read('R7_ODD_BRIDGE_MARGIN_INPUTS.json')
assert digest('R7_ODD_BRIDGE_MARGIN.md') == '0708043bf9d11a6a38d1ac48f62e1391ee4b1af2ec49b34cafa195c001c08ce6'
assert digest('R7_ODD_BRIDGE_MARGIN_INPUTS.json') == 'd6f942963e533c048875391229a295b8a1d2e4c4b15d572e45cacfa0fada3e8d'
bindings = {}
for section in ('direct_import_hashes', 'comparison_and_fixed_witness_hashes', 'author_artifact_hashes'):
    for name, expected in inputs[section].items():
        actual = digest(name)
        assert actual == expected, name
        bindings[name] = actual

newB = [(1,33),(2,6),(4,12),(7,39),(8,40),(10,42),(11,43),
        (13,45),(14,15),(16,24),(17,49),(19,23),(20,52),(21,29),
        (22,54),(25,27),(26,58),(28,30),(32,48),(34,50),(35,51),
        (36,44),(37,53),(38,46),(41,57),(56,60),(62,63)]
newA = [(a ^ 3, b ^ 3) for a, b in newB]
new = read('R7_ODD_MARGIN_RESIDUAL_WITNESS.json')
old = read('R7_MARGIN_GATE_RESIDUAL_WITNESS.json')

def verify(data, A, B):
    assert canon(A) == canon(data['faces']['A']['edges'])
    assert canon(B) == canon(data['faces']['B']['edges'])
    assert canon(A) == canon([(a ^ 3, b ^ 3) for a,b in B])
    faces = {}
    gates = []
    for face, edges in [('A', A), ('B', B)]:
        internal = matching(edges, 6)
        assert {0,3} <= internal and len(edges) == 27
        H = internal - {0,3}
        O = {x for x in H if parity(x)}
        E = H - O
        assert sorted(O) == data['faces'][face].get('O', data['faces'][face].get('local_odd_holes'))
        assert sorted(E) == data['faces'][face].get('E', data['faces'][face].get('local_even_holes'))
        dc = directions(edges, 6)
        assert min(dc) >= 2
        assert all(not short(x, d) for x in O for d in (0,3))
        faces[face] = dict(O=sorted(O), E=sorted(E), internal_free=sorted(internal), directions=dc)
        for d in (0,3):
            row = []
            for k in range(6):
                X = {x for x in range(64) if (x ^ d) & (1 << k)}
                delta = len(O & X) - len(E & X)
                EY = sorted(E - X)
                gates.append(dict(response=face, d=d, k=k, delta=delta,
                                  EY=EY, original_cross_edges=dc[k],
                                  M_pass=delta in (0,1), N_pass=delta == 2 and bool(EY) and dc[k]>=3))
                row.append(delta)
            faces[face][str(d)] = row
    global_edges = A + [(a+64,b+64) for a,b in B] + [(0,64),(3,67)]
    assert canon(global_edges) == canon(data['edges'])
    holes = matching(global_edges, 7)
    assert len(global_edges) == 56 and len(holes) == 16
    assert sorted(holes) == data['holes']
    assert not any(short(a,b) for a in holes for b in holes)
    assert sum(parity(x)==0 for x in holes)==8
    assert set(faces['A']['internal_free']) & set(faces['B']['internal_free']) == {0,3}
    dc = directions(global_edges, 7)
    assert dc == data['direction_counts']
    assert [k for k,x in enumerate(dc) if x == 2] == [6]
    for actual, recorded in zip(gates, data['margin_gates']):
        aliases = dict(response='response_face',d='anchor',k='coordinate',delta='delta')
        for key in ('response','d','k','delta'):
            assert actual[key] == recorded.get(key,recorded.get(aliases[key]))
    assert len(data['margin_gates']) == 24
    return dict(faces=faces, direction_counts=dc, gates=gates, maximal=True,
                size=56, holes=sorted(holes), global_parity_holes=[8,8])

oldB = [tuple(e) for e in old['faces']['B']['edges']]
oldA = [(a^3,b^3) for a,b in oldB]
oldcheck = verify(old, oldA, oldB)
newcheck = verify(new, newA, newB)
gate = next(g for g in oldcheck['gates'] if (g['response'],g['d'],g['k'])==('B',0,2))
assert gate['delta']==2 and gate['EY']==[40] and gate['original_cross_edges']==8 and gate['N_pass']
OB, EB = map(set, (oldcheck['faces']['B']['O'],oldcheck['faces']['B']['E']))
X = {x for x in range(64) if x & 4}
assert sorted(OB & X)==[31,47,55,61] and sorted(EB & X)==[12,20]
assert newcheck['direction_counts']==[4,4,6,10,10,20,2]
assert {g['delta'] for g in newcheck['gates']}=={-1,3,4}
assert all(not g['M_pass'] and not g['N_pass'] for g in newcheck['gates'])
for name in ('R7_ODD_BRIDGE_MARGIN_INPUTS.json','R7_ODD_MARGIN_RESIDUAL_WITNESS.md',
             'R7_ODD_MARGIN_RESIDUAL_WITNESS.json'):
    bindings[name] = digest(name)

# Verify immediate accepted source/report bindings, without replaying their certificates.
report_bindings = []
for report, source in [('../six_directions/P6_FULL_REVIEW.json','../six_directions/P6_FULL_CLOSURE.md'),
                       ('../six_directions/Q5_A10_FULL_REVIEW.json','../six_directions/Q5_A10_FULL_CLOSURE.md'),
                       ('R7_SIGNED_HOLE_MARGIN_REVIEW.json','R7_SIGNED_HOLE_MARGIN.md'),
                       ('PERFECT_MATCHING_SPLICE_REVIEW.json','PERFECT_MATCHING_SPLICE.md'),
                       ('R7_THREE_FREE_PAIRINGS_REVIEW.json','R7_THREE_FREE_PAIRINGS.md')]:
    obj = read(report)
    assert obj['verdict']=='PASS'
    # Existing schemas differ; require the digest to occur in that report.
    expected = digest(source)
    assert expected in json.dumps(obj)
    report_bindings.append(dict(report=report,source=source,sha256=expected,match=True))

result = dict(status='PASS', no_producer_imports=True, no_solver_calls=True,
              no_matching_family_or_high_hole_enumeration=True,
              bindings=bindings, immediate_accepted_bindings=report_bindings,
              old56=oldcheck, new56=newcheck,
              old56_N_gate=gate, old_large_certificates_rerun=False)
out = ROOT/'R7_ODD_BRIDGE_MARGIN_REVIEW_check.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS',bindings=len(bindings),old_N_gate=gate,
                     new_direction_counts=newcheck['direction_counts'],new_deltas=[-1,3,4]),ensure_ascii=False))
