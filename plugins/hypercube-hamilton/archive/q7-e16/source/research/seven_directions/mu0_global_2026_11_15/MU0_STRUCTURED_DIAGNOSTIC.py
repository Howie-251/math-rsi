"""Run the one bounded diagnostic on the frozen 189-row joint mu=0 source."""

import json
from pathlib import Path

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model

from MU0_JOINT_DIAGNOSTIC import (
    ALPHA, AXES, B_ALPHA, B_BETA, BETA, INNER_AXES, OUTER, SEED, VERTICES,
    check_matching, counts, digest, hall_certificate, short_maximum_matching,
)
from MU0_STRUCTURED_JOINT import B_VERTICES, BASIS_SPECS, HERE, checked_bytes, read_B_rows


SECONDS = 60.0
WORKERS = 8


def affine(expression, assignment):
    return expression.offset + sum(c * assignment[v] for v, c in
                                   zip(expression.vars, expression.coeffs))


def literal_value(literal, assignment):
    return bool(assignment[literal]) if literal >= 0 else not assignment[-1 - literal]


def in_domain(value, domain):
    return any(low <= value <= high for low, high in zip(domain[::2], domain[1::2]))


def check_assignment(proto, assignment):
    """Re-evaluate all frozen source constraints on the returned assignment."""
    if len(assignment) != len(proto.variables):
        raise ValueError("Unexpected assignment length")
    for index, (variable, value) in enumerate(zip(proto.variables, assignment)):
        if not in_domain(value, variable.domain):
            raise ValueError(f"Out-of-domain returned value at variable {index}")
    for index, constraint in enumerate(proto.constraints):
        if not all(literal_value(lit, assignment) for lit in constraint.enforcement_literal):
            continue
        kind = constraint.WhichOneof("constraint")
        if kind == "linear":
            linear = constraint.linear
            value = sum(c * assignment[v] for v, c in zip(linear.vars, linear.coeffs))
            valid = in_domain(value, linear.domain)
        elif kind == "bool_or":
            valid = any(literal_value(lit, assignment) for lit in constraint.bool_or.literals)
        elif kind == "table":
            table = constraint.table
            if table.vars or not table.exprs:
                raise ValueError("Expected the frozen table expression format")
            value = tuple(affine(expr, assignment) for expr in table.exprs)
            width = len(value)
            listed = any(value == tuple(table.values[i:i + width])
                         for i in range(0, len(table.values), width))
            valid = listed != table.negated
        else:
            raise ValueError(f"Unexpected source constraint {kind}")
        if not valid:
            raise ValueError(f"Returned assignment violates constraint {index} ({kind})")


def inspect_witness(proto, assignment):
    check_assignment(proto, assignment)
    values = {var.name: value for var, value in zip(proto.variables, assignment)}
    a = values["small_face_holes_per_color"]
    holes = {v for v in VERTICES if values[f"hole_{v}"]}
    rows, _ = read_B_rows()
    row = rows.index(tuple(int(v in holes) for v in B_VERTICES))
    basis_index = row - sum(size for size_a, size, _ in BASIS_SPECS if size_a < a)

    matching = short_maximum_matching(holes)
    realized = check_matching(holes, matching)
    witness = dict(a=a, global_basis_row=row, basis_index_for_a=basis_index,
                   source_assignment_verified=True, H_odd=sorted(holes.intersection(ALPHA)),
                   H_even=sorted(holes.intersection(BETA)),
                   maximum_matching_size=len(matching), realized_by_short_matching=realized,
                   short_matching=matching)
    if not realized:
        witness["hall_certificate"] = hall_certificate(holes, matching)

    witness["axis_table"] = []
    for j in AXES:
        alpha, beta = counts(holes, ALPHA, j), counts(holes, BETA, j)
        record = dict(axis=j, global_alpha=alpha, global_beta=beta, global_odd_minus_even=alpha-beta)
        if j in INNER_AXES:
            p, q = counts(holes, B_ALPHA, j), counts(holes, B_BETA, j)
            record.update(B_alpha=p, B_beta=q, B_deficit=q-p)
        if realized:
            record["original_matching_edges"] = sum((u ^ v) == (1 << j) for u, v in matching)
        witness["axis_table"].append(record)
    return witness


def main():
    receipt_path = HERE / "MU0_STRUCTURED_JOINT.json"
    pb = HERE / "MU0_STRUCTURED_JOINT.pb"
    output = HERE / "MU0_STRUCTURED_DIAGNOSTIC.json"
    if output.exists():
        raise FileExistsError("The one structured diagnostic receipt already exists")

    receipt = json.loads(receipt_path.read_bytes())
    expected_sha = receipt["structured_pb_sha256"]
    data = cp_model_pb2.CpModelProto.FromString(checked_bytes(pb, expected_sha))
    model = cp_model.CpModel()
    if not model.proto.parse_text_format(text_format.MessageToString(data)):
        raise ValueError("Unable to load the audited structured proto")
    if error := model.validate():
        raise ValueError(error)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_search_workers = WORKERS
    solver.parameters.random_seed = SEED
    print("Joint 189-row mu=0 diagnostic: one 60s CP-SAT call", flush=True)
    status = solver.solve(model)
    result = dict(status=solver.status_name(status), scope="joint a=0,1,2 diagnostic only",
                  diagnostic_solver_calls=1, budget_seconds=SECONDS, workers=WORKERS, seed=SEED,
                  solver_wall_seconds=solver.wall_time, solver_statistics=solver.response_stats(),
                  source_pb_sha256=expected_sha, source_receipt_sha256=digest(receipt_path),
                  diagnostic_sha256=digest(Path(__file__)), matching_calls=0, matching_enumerations=0)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result.update(matching_calls=1, witness=inspect_witness(data, solver.response_proto.solution))
    with output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")
    print(f"Result: {result['status']} after {result['solver_wall_seconds']:.3f}s", flush=True)


if __name__ == "__main__":
    main()
