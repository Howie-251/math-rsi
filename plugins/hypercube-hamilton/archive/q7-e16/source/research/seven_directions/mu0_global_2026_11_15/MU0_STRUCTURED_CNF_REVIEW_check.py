"""Audit the new table clauses and recreate the frozen joint DIMACS in memory."""
import hashlib
import json
import os
import sys
import tempfile
from collections import Counter
from pathlib import Path

from ortools.sat import cp_model_pb2

HERE = Path(__file__).resolve().parent
CERT = HERE / "certificates"
KEY = CERT / "mu0_structured_joint"
PB = HERE / "MU0_STRUCTURED_JOINT.pb"
EDGE = HERE.parent / "mu1_global_2026_11_15" / "certificates"
SHARED = HERE.parent / "mu3_hard_first_2026_11_15" / "PROOF_TOOLS"


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def check_added_table(proto, encoder):
    constraint = proto.constraints[-1]
    assert constraint.name == "joint_a0_a1_a2_large_face_hole_basis"
    table = constraint.table
    assert not table.vars and not table.negated and not constraint.enforcement_literal
    width = len(table.exprs)
    assert width == 64 and len(table.values) == 189 * width
    rows = [
        tuple(table.values[start:start + width])
        for start in range(0, len(table.values), width)
    ]
    hole_literals = []
    for v, expression in enumerate(table.exprs, 64):
        assert len(expression.vars) == 1
        assert tuple(expression.coeffs) == (1,) and not expression.offset
        i = expression.vars[0]
        assert proto.variables[i].name == f"hole_{v}"
        assert list(proto.variables[i].domain) == [0, 1]
        lit, = encoder.thresholds[i]
        hole_literals.append(lit)

    first_selector = encoder.num_vars - len(rows) + 1
    selectors = list(range(first_selector, encoder.num_vars + 1))
    assert max(hole_literals) < first_selector
    expected = []
    for selector, row in zip(selectors, rows):
        assert set(row) <= {0, 1}
        expected.extend([-selector, lit if val else -lit] for lit, val in zip(hole_literals, row))
    expected.append(selectors)
    assert encoder.clauses[-len(expected):] == expected
    assert all(abs(lit) < first_selector for clause in encoder.clauses[:-len(expected)] for lit in clause)
    return len(expected)


def main():
    manifest = json.loads(KEY.with_suffix(".build.json").read_bytes())
    paths = dict(pb=PB, source_manifest=HERE / "MU0_STRUCTURED_JOINT.json",
                 cnf=KEY.with_suffix(".cnf"), map=KEY.with_suffix(".map.json"),
                 driver=HERE / "MU0_STRUCTURED_CNF.py", encoder=EDGE / "edge_cnf.py",
                 even_encoder=SHARED / "even_cnf.py", odd_encoder=SHARED / "odd_cnf.py")
    assert manifest["sha256"] == {role: digest(path) for role, path in paths.items()}
    assert manifest["sha256"]["pb"] == "6e37bc98707b75beb29f9d37aa0c8f9a2e72acfa2672dc8bd263763185734d30"
    assert manifest["sha256"]["encoder"] == "f5b169f4a72935e47447b3e07960fda6d83027631e8c71144322496022f7459e"
    proto = cp_model_pb2.CpModelProto.FromString(PB.read_bytes())
    assert not proto.HasField("objective") and not proto.HasField("floating_point_objective")
    assert not proto.assumptions
    sys.path.insert(0, str(EDGE))
    from edge_cnf import encode
    for key in ("TMP", "TEMP", "TMPDIR"):
        os.environ[key] = str(CERT)
    tempfile.tempdir = str(CERT)
    encoder = encode(proto)
    assert check_added_table(proto, encoder) == 189 * 64 + 1
    assert len(proto.variables) == manifest["source_variables"]
    assert len(proto.constraints) == manifest["source_constraints"]
    assert encoder.num_vars == manifest["cnf_variables"]
    assert len(encoder.clauses) == manifest["cnf_clauses"]
    assert encoder.new_union_constraints == manifest["wide_union_constraints"]

    mapped = json.loads(paths["map"].read_bytes())
    assert mapped["original_variables"] == [
        [var.name, *encoder.thresholds[i]]
        for i, var in enumerate(proto.variables)
    ]
    assert mapped["extra_equalities"] == [
        [cp_index, value, literal]
        for (cp_index, value), literal in encoder.equalities.items()
    ]
    with paths["cnf"].open("rb") as actual:
        assert actual.readline() == f"p cnf {encoder.num_vars} {len(encoder.clauses)}\n".encode("ascii")
        for clause in encoder.clauses:
            assert actual.readline() == (" ".join(map(str, (*clause, 0))) + "\n").encode("ascii")
        assert actual.readline() == b""
    assert paths["cnf"].stat().st_size == manifest["cnf_bytes"]
    receipt = {
        "verdict": "PASS",
        "scope": "Independent exact PB-to-DIMACS replay and direct table-clause check. No SAT call.",
        "inputs_sha256": manifest["sha256"],
        "build_receipt_sha256": digest(KEY.with_suffix(".build.json")),
        "audit_source_sha256": digest(Path(__file__).resolve()),
        "source_constraints_by_type": dict(Counter(c.WhichOneof("constraint") for c in proto.constraints)),
        "cnf_variables": encoder.num_vars,
        "cnf_clauses": len(encoder.clauses),
        "table_rows": 189,
        "table_clauses": 189 * 64 + 1,
    }
    (HERE / "MU0_STRUCTURED_CNF_REVIEW_check.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    print(f"DIMACS and map reconstructed exactly: {encoder.num_vars} variables, {len(encoder.clauses)} clauses.")


if __name__ == "__main__":
    main()

