"""Independently reconstruct the structured mu=0 PB and audit its physical table."""
import hashlib
import json
from collections import Counter
from pathlib import Path

from ortools.sat import cp_model_pb2

HERE = Path(__file__).resolve().parent
OLD = "MU0_JOINT_NECESSARY.pb"
NEW = "MU0_STRUCTURED_JOINT.pb"
NAME = "joint_a0_a1_a2_large_face_hole_basis"
LABELS = tuple(range(64, 128))


def read(name):
    return (HERE / name).read_bytes()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def decode(name):
    raw = read(name)
    proto = cp_model_pb2.CpModelProto()
    proto.ParseFromString(raw)
    return raw, proto


def physical_groups():
    empty = json.loads(read("MU0_A0_BASIS_REVIEW_check.json"))
    rest = json.loads(read("MU0_A12_BASIS_REVIEW_check.json"))
    assert empty["verdict"] == rest["verdict"] == "PASS"
    groups = {0: [(row["alpha"], row["beta"]) for row in empty["physical_hole_sets"]]}
    assert [row["basis_index"] for row in empty["physical_hole_sets"]] == list(range(19))
    for a in (1, 2):
        group = rest["cases"][str(a)]["physical_large_face_rows"]
        assert [row["index"] for row in group] == list(range(len(group)))
        groups[a] = [(row["H_alpha"], row["H_beta"]) for row in group]
    assert {a: len(rows) for a, rows in groups.items()} == {0: 19, 1: 98, 2: 72}
    physical = []
    for a, group in sorted(groups.items()):
        for alphas, betas in group:
            assert len(set(alphas)) == len(set(betas)) == 8 - a
            assert set(alphas + betas) <= set(LABELS)
            assert all(x.bit_count() % 2 == 1 for x in alphas)
            assert all(x.bit_count() % 2 == 0 for x in betas)
            assert all((x ^ y).bit_count() != 1 for x in alphas for y in betas)
            physical.append(tuple(int(v in alphas or v in betas) for v in LABELS))
    assert len(set(physical)) == 189
    return physical


def removed_rows(proto):
    destinations = {}
    for i in range(5):
        coefficients = tuple(sorted((
            (f"global_alpha_{i}", 1), (f"global_beta_{i}", -1),
            (f"global_alpha_{i + 1}", -1), (f"global_beta_{i + 1}", 1),
        )))
        destinations[coefficients] = i
    found = {}
    for n, constraint in enumerate(proto.constraints):
        if constraint.WhichOneof("constraint") != "linear":
            continue
        equation = constraint.linear
        coefficients = tuple(sorted(
            (proto.variables[k].name, c) for k, c in zip(equation.vars, equation.coeffs)
        ))
        if coefficients not in destinations:
            continue
        assert len(equation.vars) == len(equation.coeffs) == 4
        assert list(equation.domain) == [-(1 << 63), 0]
        assert not constraint.name and not constraint.enforcement_literal
        i = destinations[coefficients]
        assert i not in found
        found[i] = n
    assert found == {i: 1140 + i for i in range(5)}
    return sorted(found.values())


def main():
    old_bytes, old = decode(OLD)
    new_bytes, new = decode(NEW)
    assert digest(old_bytes) == "c3922789fddf1ec764ea5a9260bd0cfc315b068e783c1fac6f7d989b8d2839f4"
    assert len(old.variables) == len(new.variables) == 29_424
    assert len(old.constraints) == 100_055 and len(new.constraints) == 100_051
    assert old.variables == new.variables
    order = removed_rows(old)
    transported = [c for i, c in enumerate(old.constraints) if i not in order]
    assert list(new.constraints[:-1]) == transported

    hole_map = {}
    for i, var in enumerate(old.variables):
        if var.name.startswith("hole_"):
            label = int(var.name.removeprefix("hole_"))
            assert label not in hole_map and list(var.domain) == [0, 1]
            hole_map[label] = i
    assert set(hole_map) == set(range(128))
    rows = physical_groups()
    table = cp_model_pb2.ConstraintProto(name=NAME)
    for v in LABELS:
        table.table.exprs.add(vars=[hole_map[v]], coeffs=[1])
    for bits in rows:
        table.table.values.extend(bits)
    assert new.constraints[-1] == table
    assert not table.table.negated and not table.enforcement_literal
    assert not set(hole_map[v] for v in range(64)).intersection(
        e.vars[0] for e in table.table.exprs
    )

    rebuilt = cp_model_pb2.CpModelProto()
    rebuilt.CopyFrom(old)
    rebuilt.ClearField("constraints")
    rebuilt.constraints.extend(transported)
    rebuilt.constraints.add().CopyFrom(table)
    assert rebuilt.SerializeToString(deterministic=True) == new_bytes

    # The production caller is read-only when invoked through build().
    import MU0_STRUCTURED_JOINT as actual
    regenerated, audit = actual.build()
    assert regenerated.SerializeToString(deterministic=True) == new_bytes
    manifest = json.loads(read("MU0_STRUCTURED_JOINT.json"))
    assert manifest["structured_pb_sha256"] == digest(new_bytes)
    assert manifest["source_pb_sha256"] == digest(old_bytes)
    assert audit["allowed_table"]["row_bits_sha256"] == digest(b"".join(bytes(row) for row in rows))
    assert manifest["allowed_table"] == audit["allowed_table"]
    result = {
        "verdict": "PASS",
        "scope": "Original-domain necessity and byte-exact static PB reconstruction. No solving.",
        "frozen_previous_pb_sha256": digest(old_bytes),
        "structured_pb_sha256": digest(new_bytes),
        "structured_builder_sha256": digest(read("MU0_STRUCTURED_JOINT.py")),
        "structured_manifest_sha256": digest(read("MU0_STRUCTURED_JOINT.json")),
        "audit_source_sha256": digest(Path(__file__).read_bytes()),
        "basis_a0_independent_census_sha256": digest(read("MU0_A0_BASIS_REVIEW_check.json")),
        "basis_a1_a2_independent_census_sha256": digest(read("MU0_A12_BASIS_REVIEW_check.json")),
        "removed_solely_signed_order": order,
        "new_physical_table_columns": [f"hole_{v}" for v in LABELS],
        "new_physical_table_rows": len(rows),
        "new_physical_table_row_popcounts": dict(sorted(Counter(map(sum, rows)).items())),
        "variables": len(new.variables),
        "constraints": len(new.constraints),
    }
    (HERE / "MU0_STRUCTURED_SOURCE_REVIEW_check.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(digest(new_bytes), len(new.variables), len(new.constraints), "189 exact physical rows")


if __name__ == "__main__":
    main()

