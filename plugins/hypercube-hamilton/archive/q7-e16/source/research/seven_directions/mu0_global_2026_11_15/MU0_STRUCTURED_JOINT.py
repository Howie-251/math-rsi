"""Build the joint mu=0 source from the frozen necessary model and B bases."""

import json
from hashlib import sha256
from pathlib import Path

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model


HERE = Path(__file__).resolve().parent
FROZEN_SOURCE = HERE / "MU0_JOINT_NECESSARY.pb"
FROZEN_SOURCE_SHA256 = "c3922789fddf1ec764ea5a9260bd0cfc315b068e783c1fac6f7d989b8d2839f4"
BASIS_SPECS = (
    (0, 19, "db2f7a47c191a4d6b7c39584d08071f3b8f1bb2d60b87dd6252b0f6a29cb26ab"),
    (1, 98, "052d703172b57b365016ad70a598b5ad9241d8171cfab54484b7553319307306"),
    (2, 72, "5b8d596fd2f8f32ebb4162f5adb47bd2c8f7c8eac9ce1038d0d7d5705871e11b"),
)
B_VERTICES = tuple(range(64, 128))
INT64_MIN = -(1 << 63)
TABLE_NAME = "joint_a0_a1_a2_large_face_hole_basis"


def checked_bytes(path, expected):
    data = path.read_bytes()
    if sha256(data).hexdigest() != expected:
        raise ValueError(f"Unexpected SHA-256 for {path}")
    return data


def signature(left):
    right = left + 1
    return tuple(sorted((
        (f"global_alpha_{left}", 1), (f"global_beta_{left}", -1),
        (f"global_alpha_{right}", -1), (f"global_beta_{right}", 1),
    )))


def remove_inner_order(proto):
    expected = {signature(left) for left in range(5)}
    removed = {}
    for index, constraint in enumerate(proto.constraints):
        if constraint.WhichOneof("constraint") != "linear":
            continue
        linear = constraint.linear
        if len(linear.vars) != 4 or len(linear.coeffs) != 4:
            continue
        terms = tuple(sorted(
            (proto.variables[var].name, coefficient)
            for var, coefficient in zip(linear.vars, linear.coeffs)
        ))
        if terms not in expected:
            continue
        if (terms in removed or tuple(linear.domain) != (INT64_MIN, 0)
                or constraint.enforcement_literal or constraint.name):
            raise ValueError("Unexpected declaration of a global imbalance order")
        removed[terms] = index
    if set(removed) != expected:
        raise ValueError("All five signed order constraints are required")
    for index in sorted(removed.values(), reverse=True):
        del proto.constraints[index]
    return [dict(source_index=removed[terms], terms=terms, domain=[INT64_MIN, 0])
            for terms in map(signature, range(5))]


def read_B_rows():
    rows, files = [], []
    for a, expected_count, expected_sha in BASIS_SPECS:
        path = HERE / f"MU0_A{a}_BASIS_PREFLIGHT.json"
        report = json.loads(checked_bytes(path, expected_sha))
        representatives = report["representatives"]
        if (report["status"] != "COMPLETE" or
                len(representatives) != report["stored_representatives"] or
                len(representatives) != expected_count):
            raise ValueError(f"Incomplete a={a} basis")
        files.append(dict(a=a, file=path.name, sha256=expected_sha, row_count=expected_count))
        r = 8 - a
        for item in representatives:
            L, V = item["L"], item["V"]
            if any(len(group) != r or len(set(group)) != r
                   or any(not isinstance(v, int) or not 0 <= v < 64
                          or v.bit_count() % 2 != parity for v in group)
                   for group, parity in ((L, 0), (V, 1))):
                raise ValueError(f"Invalid six-bit support in the a={a} basis")
            odd = {64 + v for v in L}
            even = {64 + (63 ^ v) for v in V}
            if any((x ^ y).bit_count() == 1 for x in odd for y in even):
                raise ValueError(f"Non-independent B holes in the a={a} basis")
            holes = odd | even
            rows.append(tuple(int(v in holes) for v in B_VERTICES))
    if len(set(rows)) != len(rows):
        raise ValueError("Duplicate B rows")
    return rows, files


def build():
    proto = cp_model_pb2.CpModelProto()
    proto.ParseFromString(checked_bytes(FROZEN_SOURCE, FROZEN_SOURCE_SHA256))
    source_variables, source_constraints = len(proto.variables), len(proto.constraints)
    removed = remove_inner_order(proto)

    names = {variable.name: index for index, variable in enumerate(proto.variables)
             if variable.name.startswith("hole_")}
    if set(names) != {f"hole_{v}" for v in range(128)}:
        raise ValueError("Expected 128 physical hole variables, each with its own name")
    indices = [names[f"hole_{v}"] for v in B_VERTICES]
    if any(tuple(proto.variables[index].domain) != (0, 1) for index in indices):
        raise ValueError("The B table requires Boolean hole variables")
    rows, basis_files = read_B_rows()

    constraint = proto.constraints.add(name=TABLE_NAME)
    table = constraint.table
    for index in indices:
        table.exprs.add(vars=[index], coeffs=[1])
    for row in rows:
        table.values.extend(row)

    model = cp_model.CpModel()
    if not model.proto.parse_text_format(text_format.MessageToString(proto)):
        raise ValueError("CP-SAT rejected the structured source proto")
    if error := model.validate():
        raise ValueError(error)
    if len(proto.variables) != source_variables or len(proto.constraints) != source_constraints - 4:
        raise ValueError("Unexpected structured source size")
    report = dict(
        status="STATIC_BUILD_ONLY", solver_calls=0, matching_enumerations=0,
        small_face_geometry_enumerations=0, small_face_anchor=False,
        source_pb=FROZEN_SOURCE.name, source_pb_sha256=FROZEN_SOURCE_SHA256,
        builder_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        source_variables=source_variables, source_constraints=source_constraints,
        variables=len(proto.variables), constraints=len(proto.constraints),
        removed_signed_order=removed, basis_files=basis_files,
        allowed_table=dict(name=TABLE_NAME, columns=[f"hole_{v}" for v in B_VERTICES],
                           variable_indices=indices, rows=len(rows), negated=False,
                           row_order="a ascending, then each frozen JSON representative order",
                           row_bits_sha256=sha256(b"".join(bytes(row) for row in rows)).hexdigest()),
    )
    return proto, report


def main():
    pb_path = HERE / "MU0_STRUCTURED_JOINT.pb"
    report_path = HERE / "MU0_STRUCTURED_JOINT.json"
    if pb_path.exists() or report_path.exists():
        raise FileExistsError("Structured source artifacts already exist")
    proto, report = build()
    data = proto.SerializeToString(deterministic=True)
    report["structured_pb_sha256"] = sha256(data).hexdigest()
    pb_path.write_bytes(data)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "status", "variables", "constraints", "structured_pb_sha256",
    )}), flush=True)


if __name__ == "__main__":
    main()
