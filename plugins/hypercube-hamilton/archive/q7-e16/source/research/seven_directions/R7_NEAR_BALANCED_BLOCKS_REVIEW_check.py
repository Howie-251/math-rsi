"""Independent arithmetic on exactly one supplied matching; no search/solver."""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'R7_NEAR_BALANCED_FIXED_WITNESS.json'
data = json.loads(SOURCE.read_text(encoding='utf-8'))
edges = data['edges']
used = set()
counts = [0] * 7
for u, v in edges:
    assert 0 <= u < 128 and 0 <= v < 128 and u != v
    assert u not in used and v not in used
    used.update((u, v))
    d = u ^ v
    assert d > 0 and d & (d - 1) == 0
    counts[d.bit_length() - 1] += 1
holes = sorted(set(range(128)) - used)
parity = lambda v: v.bit_count() % 2
colors = lambda vertices: [sum(parity(v) == c for v in vertices) for c in (0, 1)]
adjacent = [(u, v) for u in holes for v in holes if u < v and (u ^ v).bit_count() == 1]
balanced_outer = []
old_passing = []
new_passing = []
fixed_gate = []
tested = 0
for i in range(7):
    faces = [[v for v in holes if (v >> i) & 1 == s] for s in (0, 1)]
    if all(colors(face)[0] == colors(face)[1] for face in faces):
        balanced_outer.append(i)
    for ka in range(7):
        if ka == i:
            continue
        for kb in range(7):
            if kb == i:
                continue
            tested += 1
            blocks = [colors([v for v in face if (v >> k) & 1 == s])
                      for face, k in zip(faces, (ka, kb)) for s in (0, 1)]
            outer_ok = all(colors(face)[0] == colors(face)[1] for face in faces)
            if all(e == o for e, o in blocks):
                old_passing.append([i, ka, kb])
            if outer_ok and all(abs(e - o) <= 1 for e, o in blocks):
                new_passing.append([i, ka, kb])
            if (i, ka, kb) == (6, 0, 0):
                fixed_gate = blocks
assert len(edges) == 56 and counts == [4, 6, 4, 4, 18, 16, 4]
assert holes == [0, 3, 5, 9, 47, 55, 59, 61, 66, 68, 72, 80, 118, 122, 124, 127]
assert colors(holes) == [8, 8] and not adjacent
assert balanced_outer == [6] and tested == 252 and not old_passing
assert new_passing == [[6, 0, 0]]
assert fixed_gate == [[1, 0], [3, 4], [4, 3], [0, 1]]
result = dict(status='PASS', matching_count=1, solver_calls=0,
              producer_script_executed=False, source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              edge_count=len(edges), direction_counts=counts, holes=holes,
              color_counts=colors(holes), inclusion_maximal=not adjacent,
              balanced_outer_coordinates=balanced_outer, old_Q_gates_checked=tested,
              old_Q_passing=old_passing, Qplus_passing=new_passing,
              fixed_gate=fixed_gate, exact_outer_bridge_count=counts[6],
              exclusions=dict(two_edge_direction_rules=2 not in counts,
                              B_max12_holes=len(holes)>12,
                              E8_completion=not adjacent and len(edges)<60,
                              old_Q=not old_passing),
              hamilton_certificate_produced=False)
output = BASE / 'R7_NEAR_BALANCED_BLOCKS_REVIEW_check.json'
output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
