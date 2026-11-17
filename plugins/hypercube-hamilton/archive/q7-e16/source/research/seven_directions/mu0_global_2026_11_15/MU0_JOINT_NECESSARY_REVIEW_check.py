"""Check new MU0 base constraints and regenerate the bound source model without solving."""

from collections import Counter
from hashlib import file_digest
import json
from pathlib import Path

from google.protobuf import text_format
from ortools.sat import cp_model_pb2

import MU0_JOINT_NECESSARY as source


HERE = Path(__file__).resolve().parent
MIN_I64, MAX_I64 = -(1 << 63), (1 << 63) - 1
CODE_SHA = "c95b9ea0955f1c16ec06280b4288bd9a0bcc505de449f6e13cbc13d386dd35f0"
NOTE_SHA = "57dbeb457f8f31253a2181ae5e0f21a7a53860722deee62ae1858813075c8235"
MENU_DIGESTS = {
    "EDGE_MENU_PROBE.py": "b6547a3f18d663cb97a2ea6215963e9fc465e14db204e299da045fe9bc692d32",
    "EDGE_LOW_GAP_PROBE.py": "2a2725b2e22712d4ec1cd94cfbe36e13e3def79d6595fd0fd21c6770c85c8364",
    "EDGE_HIGH_GAP_PROBE.py": "c9fc0bd6ab0eb51cdea7e635ae445afdcd36e3321147e5ccddc54d7652ded9e4",
}


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def proto(model):
    return text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())


def line(terms, domain, guards=()):
    if domain == (0, 0) and terms and terms[min(terms)] < 0:
        terms = {i: -coefficient for i, coefficient in terms.items()}
    return ("linear", tuple(sorted(terms.items())), domain, tuple(sorted(guards)))


def row_record(row):
    kind = row.WhichOneof("constraint")
    guards = tuple(sorted(row.enforcement_literal))
    if kind == "linear":
        return line(dict(zip(row.linear.vars, row.linear.coeffs)), tuple(row.linear.domain), guards)
    if kind == "bool_or":
        return ("bool_or", tuple(sorted(row.bool_or.literals)), guards)
    if kind == "table":
        table = row.table
        assert not table.negated and not table.vars
        exprs = table.exprs
        assert all(len(e.vars) == 1 and tuple(e.coeffs) == (1,) and e.offset == 0 for e in exprs)
        n = len(exprs)
        assert len(table.values) % n == 0
        rows = tuple(tuple(table.values[i:i+n]) for i in range(0, len(table.values), n))
        return ("table", tuple(e.vars[0] for e in exprs), rows, guards)
    raise ValueError(kind)


def expected_base(ids):
    def count(pts, name):
        terms = {ids[f"hole_{v}"]: 1 for v in pts}
        terms[ids[name]] = -1
        return line(terms, (0, 0))

    holes = [ids[f"hole_{v}"] for v in range(128)]
    a, r = ids["small_face_holes_per_color"], ids["large_face_holes_per_color"]
    expected = [("table", (a, r), ((0, 8), (1, 7), (2, 6)), ())]
    for side, name in ((0, "small_face_holes_per_color"), (1, "large_face_holes_per_color")):
        for parity in (0, 1):
            expected.append(count([v for v in range(128) if v >> 6 == side and v.bit_count() % 2 == parity], name))
    for u in range(128):
        for j in range(7):
            v = u ^ (1 << j)
            if u < v:
                expected.append(line({holes[u]: 1, holes[v]: 1}, (MIN_I64, 1)))
        disj = [holes[u], *[-1 - holes[u ^ (1 << j)] for j in range(7)]]
        expected.append(("bool_or", tuple(sorted(disj)), ()))

    global_rows = tuple((x, y) for x in range(9) for y in range(9) if y - x >= 2)
    for j in range(7):
        x_name, y_name = f"global_alpha_{j}", f"global_beta_{j}"
        alpha = [v for v in range(128) if v.bit_count() % 2 and (v >> j) & 1]
        beta = [v for v in range(128) if not v.bit_count() % 2 and (v >> j) & 1]
        expected.append(count(alpha, x_name))
        expected.append(count(beta, y_name))
        if j == 6:
            continue
        expected.append(("table", (ids[x_name], ids[y_name]), global_rows, ()))
        p_name, q_name = f"large_alpha_{j}", f"large_beta_{j}"
        expected.append(count([u for u in alpha if u >= 64], p_name))
        expected.append(count([u for u in beta if u >= 64], q_name))
        p, q = ids[p_name], ids[q_name]
        flag = ids[f"large_delta_two_{j}"]
        expected.append(line({p: 1, q: -1}, (MIN_I64, -2)))
        expected.append(line({p: 1, q: -1}, (-2, -2), (flag,)))
        expected.append(line({p: 1, q: -1}, (MIN_I64, -3, -1, MAX_I64), (-1 - flag,)))
        expected.append(line({p: 1}, (2, MAX_I64), (flag,)))
        expected.append(line({p: 1, r: -1}, (MIN_I64, -4), (flag,)))
    return Counter(expected)


def main():
    assert digest(HERE / "MU0_JOINT_NECESSARY.py") == CODE_SHA
    assert digest(HERE / "MU0_JOINT_NECESSARY.md") == NOTE_SHA
    for file, expected in MENU_DIGESTS.items():
        assert digest(HERE.parent / "mu1_global_2026_11_15" / file) == expected
    metadata_file = HERE / "MU0_JOINT_NECESSARY.json"
    metadata = json.loads(metadata_file.read_bytes())
    assert metadata["status"] == "STATIC_BUILD_ONLY" and metadata["solver_calls"] == 0
    model_base, _, _ = source.build_base()
    base = proto(model_base)
    ids = {var.name: i for i, var in enumerate(base.variables)}
    assert len(ids) == len(base.variables)
    assert expected_base(ids) == Counter(map(row_record, base.constraints))
    for name, var in ids.items():
        if name.startswith(("hole_", "large_delta_two_")):
            assert tuple(base.variables[var].domain) == (0, 1)

    model, holes, stats = source.build()
    assert len(holes) == 128 and model.validate() == ""
    full = proto(model)
    assert sorted(field.name for field, _ in full.ListFields()) == ["constraints", "variables"]
    assert list(full.variables[:len(base.variables)]) == list(base.variables)
    assert list(full.constraints[:len(base.constraints)]) == list(base.constraints)

    def sorting(j):
        return line({ids[f"global_alpha_{j}"]: 1, ids[f"global_beta_{j}"]: -1,
                    ids[f"global_alpha_{j+1}"]: -1, ids[f"global_beta_{j+1}"]: 1}, (MIN_I64, 0))

    ordered = set(map(sorting, range(5)))
    assert len(ordered) == 5 and ordered <= {
        row_record(row) for row in full.constraints[len(base.constraints):]
        if row.WhichOneof("constraint") == "linear"
    }
    pb = HERE / "MU0_JOINT_NECESSARY.pb"
    assert full.SerializeToString(deterministic=True) == pb.read_bytes()
    assert digest(pb) == metadata["sha256"]["pb"]
    assert json.loads(json.dumps(stats)) == metadata["model_parameters"]
    assert metadata["variable_count"] == len(full.variables)
    assert metadata["constraint_count"] == len(full.constraints)

    record = {
        "verdict": "PASS",
        "scope": "All base rows independently recomputed, shared menus bound, exact full source PB re-created; no solve.",
        "base_constraints": len(base.constraints),
        "base_variables": len(base.variables),
        "inner_sort_constraints_checked": len(ordered),
        "full_constraints": len(full.constraints),
        "full_variables": len(full.variables),
        "pb_sha256": digest(pb),
        "producer_static_receipt_sha256": digest(metadata_file),
        "independent_checker_sha256": digest(Path(__file__)),
        "source_sha256": CODE_SHA,
        "note_sha256": NOTE_SHA,
    }
    with (HERE / "MU0_JOINT_NECESSARY_REVIEW_check.json").open("x", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2)
        handle.write("\n")
    print(json.dumps(record, indent=2), flush=True)


if __name__ == "__main__":
    main()
