"""Only arithmetic on one pre-existing Q7 matching; no solver or family search."""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
source = BASE / "R7_ODD_MARGIN_RESIDUAL_WITNESS.json"
data = json.loads(source.read_text(encoding="utf-8"))
edges = [tuple(e) for e in data["edges"]]
assert len(edges) == 56
used = [v for e in edges for v in e]
assert len(set(used)) == 112
counts = [0] * 7
for a, b in edges:
    assert 0 <= a < 128 and 0 <= b < 128
    diff = a ^ b
    assert diff and diff & (diff - 1) == 0
    counts[diff.bit_length() - 1] += 1
assert counts == [4, 4, 6, 10, 10, 20, 2]
holes = set(range(128)) - set(used)
assert holes == set(data["holes"])
t, outer_i, inner_k = 67, 5, 2
assert t.bit_count() == 3
assert t & ((1 << outer_i) | (1 << inner_k)) == 0
assert {v ^ t for v in holes} == holes
blocks = []
for outer_bit in (0, 1):
    for inner_bit in (0, 1):
        h = sorted(v for v in holes
                   if (v >> outer_i) & 1 == outer_bit
                   and (v >> inner_k) & 1 == inner_bit)
        even = [v for v in h if v.bit_count() % 2 == 0]
        odd = [v for v in h if v.bit_count() % 2 == 1]
        assert len(even) == len(odd)
        blocks.append({"outer_bit": outer_bit, "inner_bit": inner_bit,
                       "holes": h, "even_holes": even, "odd_holes": odd,
                       "per_color": len(even)})
outer_edges = [list(e) for e in edges if (e[0] ^ e[1]) == 1 << outer_i]
assert len(outer_edges) == 20
out = {
    "status": "PASS_FIXED_INPUT_ARITHMETIC_ONLY",
    "caller": "/root", "worker": "/root/r7_blocks_write_retry",
    "input": source.name,
    "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "matching_count": 1, "solver_calls": 0, "family_enumeration": False,
    "edge_count": len(edges), "direction_counts": counts,
    "holes": sorted(holes), "xor_symmetry_t": t,
    "xor_symmetry_support": [0, 1, 6],
    "outer_i": outer_i, "inner_k_A": inner_k, "inner_k_B": inner_k,
    "blocks": blocks, "original_outer_cross_edges": outer_edges,
    "original_outer_cross_count": len(outer_edges),
    "scope": "Only the one existing matching and its fixed split; universal theorem is proved in prose."
}
target = BASE / "r7_balanced_q5_blocks_fixed_check.json"
target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": out["status"], "blocks": blocks,
                  "outer_cross_count": len(outer_edges)}, ensure_ascii=False))
