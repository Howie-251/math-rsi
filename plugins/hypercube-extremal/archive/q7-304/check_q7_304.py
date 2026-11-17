#!/usr/bin/env python3
"""Verify the two 304-edge C4-free Q7 constructions and run bundled orbit/encoding audits."""
from __future__ import annotations
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def check_q7_graph(path: Path) -> dict:
    edges = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.replace(",", " ").split()
        u, v = int(parts[0]), int(parts[1])
        if u > v:
            u, v = v, u
        assert 0 <= u < 128 and 0 <= v < 128, (u, v)
        diff = u ^ v
        assert diff > 0 and (diff & (diff - 1)) == 0, f"Non-cube edge {(u, v)}"
        assert (u, v) not in edges, f"Duplicate edge {(u, v)}"
        edges.add((u, v))
    c4 = 0
    for i in range(7):
        for j in range(i + 1, 7):
            for x in range(128):
                if (x & (1 << i)) == 0 and (x & (1 << j)) == 0:
                    a, b, c = x ^ (1 << i), x ^ (1 << j), x ^ (1 << i) ^ (1 << j)
                    sq = [(min(x, a), max(x, a)), (min(x, b), max(x, b)),
                          (min(a, c), max(a, c)), (min(b, c), max(b, c))]
                    if all(e in edges for e in sq):
                        c4 += 1
    assert len(edges) == 304 and c4 == 0, (path.name, len(edges), c4)
    return {"file": path.name, "vertices": 128, "edges": len(edges), "c4_count": c4}


def main() -> int:
    w_res = [check_q7_graph(HERE / "witnesses" / name) for name in ("A.edges", "B.edges")]
    p304 = HERE / "source" / "sources" / "agents" / "generation" / "research" / "problem_001_304"
    orbit_run = subprocess.run([sys.executable, "-B", str(p304 / "six_profiles_independent_audit.py")],
                               cwd=str(p304), capture_output=True, text=True, check=True)
    manifest = json.loads((p304 / "star_rigidity_certificate_manifest.json").read_text(encoding="utf-8"))
    out = {
        "status": "PASS_LOWER_WITNESSES_AND_ORBIT_AUDIT",
        "lower_bound_verified": 304,
        "witnesses": w_res,
        "six_profiles_orbit_audit_exit": orbit_run.returncode,
        "upper_bound_scope": "304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass (21 raw .cnf/.drup traces were omitted upstream).",
        "manifest_entries_recorded": len(manifest) if isinstance(manifest, list) else len(manifest.get("certificates", manifest)),
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
