#!/usr/bin/env python3
"""Independently verify all four 682-edge C4-free spanning subgraphs of Q8."""
from __future__ import annotations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SEEDS = HERE / "research" / "ex_qn_c4" / "proofs" / "q8_seed_isometries_cycle011"


def check_q8_graph(path: Path) -> dict:
    edges = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.replace(",", " ").split()
        u, v = int(parts[0]), int(parts[1])
        if u > v:
            u, v = v, u
        assert 0 <= u < 256 and 0 <= v < 256
        diff = u ^ v
        assert diff > 0 and (diff & (diff - 1)) == 0
        assert (u, v) not in edges
        edges.add((u, v))
    c4 = 0
    for i in range(8):
        for j in range(i + 1, 8):
            for x in range(256):
                if (x & (1 << i)) == 0 and (x & (1 << j)) == 0:
                    a, b, c = x ^ (1 << i), x ^ (1 << j), x ^ (1 << i) ^ (1 << j)
                    sq = [(min(x, a), max(x, a)), (min(x, b), max(x, b)),
                          (min(a, c), max(a, c)), (min(b, c), max(b, c))]
                    if all(e in edges for e in sq):
                        c4 += 1
    assert len(edges) == 682 and c4 == 0
    return {"file": path.name, "vertices": 256, "edges": len(edges), "c4_count": c4}


def main() -> int:
    rows = [check_q8_graph(SEEDS / f"seed{k}.edges") for k in (1, 2, 3, 4)]
    print(json.dumps({"status": "PASS", "lower_bound_verified": 682, "seeds": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
