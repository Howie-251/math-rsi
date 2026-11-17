"""One fixed witness and imported-version checks; no family enumeration."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_witness(base, d, e, f):
    forbidden = {0, 3, d, d ^ e, d ^ e ^ f}
    edges = {tuple(sorted((x, x ^ base))) for x in range(64)
             if not x & base and x not in forbidden}
    edges.update([tuple(sorted((d, d ^ e))),
                  tuple(sorted(((d ^ e) ^ base, (d ^ e ^ f) ^ base)))])
    used = set(forbidden)
    squares = []
    for q in [1 << i for i in range(6) if 1 << i != base]:
        x = next(x for x in range(64) if not x & base and x < x ^ q
                 and x not in used and x ^ q not in used)
        y = x ^ q
        for a in (x, y):
            edges.remove(tuple(sorted((a, a ^ base))))
        edges.update([tuple(sorted((x, y))), tuple(sorted((x ^ base, y ^ base)))])
        squares.append([q, x, y])
        used.update([x, y])
    endpoints = [v for edge in edges for v in edge]
    assert len(edges) == 29 and len(set(endpoints)) == 58
    assert all((a ^ b).bit_count() == 1 for a, b in edges)
    counts = [sum((a ^ b) == 1 << i for a, b in edges) for i in range(6)]
    assert min(counts) >= 2
    return {"parameters": [base, d, e, f], "square_switches_q_x_y": squares,
            "edges": sorted(map(list, edges)),
            "holes": sorted(set(range(64)) - set(endpoints)),
            "direction_counts": counts}


def create_artifacts():
    a = local_witness(32, 12, 1, 2)
    b = local_witness(16, 6, 8, 2)
    assert a["holes"] == [0, 3, 15, 32, 35, 44]
    assert b["holes"] == [0, 3, 12, 16, 19, 22]
    edges = a["edges"] + [[x + 64, y + 64] for x, y in b["edges"]]
    edges += [[0, 64], [3, 67]]
    endpoints = [v for edge in edges for v in edge]
    assert len(edges) == 60 and len(set(endpoints)) == 120
    assert all((x ^ y).bit_count() == 1 for x, y in edges)
    holes = sorted(set(range(128)) - set(endpoints))
    assert holes == [15, 32, 35, 44, 76, 80, 83, 86]
    assert not any((x ^ y).bit_count() == 1 for x in holes for y in holes)
    counts = [sum((x ^ y) == 1 << i for x, y in edges) for i in range(7)]
    assert min(counts) == 2 and [i for i, c in enumerate(counts) if c == 2] == [6]
    witness = {"scope": "single fixed input, no matching family search",
               "A": a, "B_local": b, "M": edges, "holes": holes,
               "direction_counts": counts, "m": 2, "maximal_short_matching": True,
               "T_U_V_W_excluded": "only two-edge direction is j=6; both faces have >=2 edges in each internal direction"}
    witness_path = ROOT / "R7_EIGHT_HOLE_M2_WITNESS.json"
    witness_path.write_text(json.dumps(witness, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit = json.loads((ROOT / "Q7_EIGHT_NINE_CUTS_REVIEW.json").read_text(encoding="utf-8"))
    checked = {}
    for field in ("audited_input_hashes", "imported_dependency_hashes"):
        for name, expected in audit[field].items():
            actual = digest(ROOT / name)
            assert actual == expected.removeprefix("sha256:"), name
            checked[name] = actual
    assert audit["verdict"] == "PASS"
    paths = [
        "R7_EIGHT_HOLE_CYCLE_PROJECTION.md", "R7_EIGHT_HOLE_M2_WITNESS.json",
        "check_r7_eight_hole_cycle.py", "Q7_EIGHT_NINE_CUTS_REVIEW.json",
        "Q7_EIGHT_NINE_CUTS_REVIEW.md", "Q7_SIX_HOLE_CLOSURE.md",
        "Q7_SIX_HOLE_REVIEW.json", "A4_DIMENSIONAL_INDUCTION.md",
        "A4_DIMENSIONAL_REVIEW.json", "PROOF_PACKAGE.md",
        "R7_TWO_CROSS_SEPARATING_FACE.md", "R7_TWO_CROSS_SINGLE_INTERNAL.md",
        "R7_SINGLE_I_FLEXIBLE_EAR.md", "R7_SINGLE_I_SOURCE_CUT.md",
    ]
    manifest = {"status": "author deterministic checks; not independent mathematical review",
                "bound_files": {name: digest(ROOT / name) for name in paths},
                "nine_cut_audit_declared_inputs_verified": checked,
                "main_theorem_import": "Q7_EIGHT_NINE_CUTS exact claim item4",
                "additional_imports_scope": "at-least-60 extension corollary only: previously accepted six/four/two-hole path and perfect matching circle inputs",
                "fixed_witness_check": "PASS", "fixed_witness_direction_counts": counts,
                "family_enumeration": False, "RUN_STATE_modified": False}
    (ROOT / "R7_EIGHT_HOLE_CYCLE_INPUTS.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": "PASS", "proof_sha256": digest(ROOT / paths[0]),
                      "witness_direction_counts": counts,
                      "A_counts": a["direction_counts"], "B_counts": b["direction_counts"],
                      "A_squares": a["square_switches_q_x_y"],
                      "B_squares": b["square_switches_q_x_y"],
                      "nine_cut_bound_inputs_checked": len(checked)}, ensure_ascii=False))


if __name__ == "__main__":
    create_artifacts()
