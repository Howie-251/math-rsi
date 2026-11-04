"""Stdlib-only verification of the extremal 18-hole rooted-maximal witness."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raw = (ROOT/'rooted_23_matching.json').read_bytes()
d = json.loads(raw)
assert d['status'] == 'FOUND'
m = {tuple(sorted(e)) for e in d['matching']}
assert len(m) == len(d['matching']) == 23
covered = [v for e in m for v in e]
assert len(set(covered)) == 46 and 0 not in covered
assert all((a ^ b).bit_count() == 1 for a, b in m)
holes = set(range(64))-set(covered)
assert holes == set(d['holes']) and len(holes) == 18
edges = {(a, a ^ (1 << j)) for a in range(64) for j in range(6) if a < (a ^ (1 << j))}
rooted_edges = {e for e in edges if 0 not in e}
assert len(rooted_edges) == 186
assert all(a in covered or b in covered for a, b in rooted_edges)
addable = [e for e in sorted(edges) if not set(e) & set(covered)]
assert addable and all(0 in e for e in addable)
for e in addable:
    cp = set(covered) | set(e)
    assert all(a in cp or b in cp for a, b in edges)
out = dict(status='PASS', matching_edges=23, holes=18, maximal_avoiding_root=True,
           addable_full_cube_edges=addable, all_one_edge_completions_globally_maximal=True,
           directions=sorted({(a ^ b).bit_length()-1 for a, b in m}),
           input_sha256=hashlib.sha256(raw).hexdigest(),
           significance='Together with Havel-Krivanek bound, exact maximum rooted-maximal hole count is 18',
           hamilton_path_claim=False, full_p6_proved=False)
(ROOT/'rooted_23_verification.json').write_text(json.dumps(out, indent=2), encoding='utf8')
print(json.dumps(out, indent=2))
