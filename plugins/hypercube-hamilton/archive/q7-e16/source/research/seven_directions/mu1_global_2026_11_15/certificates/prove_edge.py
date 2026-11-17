"""Run a bounded proof-logging SAT check, then optionally verify a DRUP proof."""

import argparse
import json
import subprocess
from pathlib import Path
from shutil import copyfileobj
from threading import Event, Thread
from time import monotonic, process_time

from edge_cnf import HERE, MU3_TOOLS, digest

from ortools.sat import cp_model_pb2
import pysolvers
from pysat.formula import CNF
from pysat.solvers import Glucose4

from EDGE_HIGH_GAP_PROBE import validate_high_geometry
from EDGE_LOW_GAP_PROBE import (
    ALPHA, AXES, BETA, VERTICES, check_matching, short_maximum_matching, validate_sat,
)

SAT_SECONDS = 300
CHECK_SECONDS = 600
CHECKER_DIR = MU3_TOOLS / "drat_trim_official_2e3b2dc"
CHECKER = CHECKER_DIR / "drat-trim.exe"
CHECKER_SHA256 = "4c37fb793037739ab5ef9019fa7bc579368a6db23a6076c4bd77952149c7391f"
CHECKER_SOURCE_SHA256 = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"


def validated_build(a):
    stem = HERE / f"edge_a{a}"
    receipt = json.loads(stem.with_suffix(".build.json").read_text(encoding="utf-8"))
    for suffix, role in ((".cnf", "cnf"), (".pb", "pb"), (".map.json", "map")):
        assert digest(stem.with_suffix(suffix)) == receipt["sha256"][role]
    return stem, receipt


def check_source_assignment(proto, values):
    def true_ref(ref):
        return values[ref] == 1 if ref >= 0 else values[-1 - ref] == 0

    def allowed(value, domain):
        return any(low <= value <= high for low, high in zip(domain[::2], domain[1::2]))

    assert len(values) == len(proto.variables)
    assert all(allowed(value, var.domain) for value, var in zip(values, proto.variables))
    for idx, constraint in enumerate(proto.constraints):
        if not all(true_ref(ref) for ref in constraint.enforcement_literal):
            continue
        kind = constraint.WhichOneof("constraint")
        if kind == "bool_or":
            assert any(true_ref(ref) for ref in constraint.bool_or.literals), idx
        elif kind == "linear":
            row = constraint.linear
            amount = sum(coeff * values[var] for var, coeff in zip(row.vars, row.coeffs))
            assert allowed(amount, row.domain), idx
        elif kind == "table":
            row = constraint.table
            width = len(row.exprs)
            point = [values[expr.vars[0]] for expr in row.exprs]
            present = any(row.values[k:k + width] == point
                          for k in range(0, len(row.values), width))
            assert present != row.negated, idx
        else:
            raise ValueError((idx, kind))


def save_assignment(a, stem, formula, model):
    assignment = set(model)
    assert len(assignment) == formula.nv and {abs(lit) for lit in assignment} == set(range(1, formula.nv + 1))
    assert all(any(lit in assignment for lit in clause) for clause in formula.clauses)
    mapped = json.loads(stem.with_suffix(".map.json").read_text(encoding="utf-8"))["original_variables"]
    cp_proto = cp_model_pb2.CpModelProto.FromString(stem.with_suffix(".pb").read_bytes())
    assert [row[0] for row in mapped] == [v.name for v in cp_proto.variables]
    values = [sum(threshold in assignment for threshold in row[1:]) for row in mapped]
    check_source_assignment(cp_proto, values)

    H = {int(name[5:]) for (name, *_), value in zip(mapped, values) if name.startswith("hole_") and value}
    axes = validate_sat(a, H)
    assert [row["delta"] for row in axes[:6]] == sorted(row["delta"] for row in axes[:6])
    assert not any(validate_high_geometry(H).values())
    assert all(any(v ^ (1 << j) not in H for j in AXES) for v in VERTICES if v not in H)
    matching = short_maximum_matching(H)
    realized = check_matching(H, matching)
    path = stem.with_suffix(".assignment.json")
    record = dict(
        axes=axes, realized_by_short_matching=realized, matching_size=len(matching), short_matching=matching,
        holes_alpha_odd=sorted(H.intersection(ALPHA)), holes_beta_even=sorted(H.intersection(BETA)),
        all_source_constraints_checked=len(cp_proto.constraints), all_cnf_clauses_checked=len(formula.clauses),
        dimacs_assignment=sorted(model, key=abs),
    )
    path.write_text(json.dumps(record, separators=(",", ":")) + "\n", encoding="utf-8")
    return dict(assignment_file=path.name, assignment_sha256=digest(path),
                realized_by_short_matching=realized, matching_size=len(matching),
                holes_alpha_odd=record["holes_alpha_odd"], holes_beta_even=record["holes_beta_even"],
                axes=axes)


def solve(a):
    stem, building = validated_build(a)
    receipt_path = stem.with_suffix(".solve.json")
    proof_path = stem.with_suffix(".drup")
    if any(path.exists() for path in (receipt_path, proof_path, stem.with_suffix(".assignment.json"))):
        raise FileExistsError(f"Existing solver artifacts for a={a}")
    formula = CNF(from_file=str(stem.with_suffix(".cnf")))
    assert (formula.nv, len(formula.clauses)) == (building["num_cnf_vars"], building["num_cnf_clauses"])

    with Glucose4(with_proof=True) as solver:
        solver.append_formula(formula.clauses)
        finished, interrupted = Event(), Event()
        started, cpu_start = monotonic(), process_time()

        def interrupt_at_budget():
            while not finished.wait(0.1):
                if max(monotonic() - started, process_time() - cpu_start) >= SAT_SECONDS:
                    interrupted.set()
                    solver.interrupt()
                    return

        thread = Thread(target=interrupt_at_budget, daemon=True)
        thread.start()
        print(f"a={a}: proof-logging SAT solver started with {SAT_SECONDS}s limit", flush=True)
        try:
            decided = solver.solve_limited(expect_interrupt=True)
        finally:
            finished.set()
            thread.join()
        status = "SAT" if decided is True else "UNSAT" if decided is False else "UNKNOWN"
        result = dict(a=a, status=status, solver="PySAT Glucose4 with proof logging",
                      script_sha256=digest(Path(__file__)), cnf_sha256=building["sha256"]["cnf"],
                      pb_sha256=building["sha256"]["pb"], budget_seconds=SAT_SECONDS,
                      interrupted_by_watchdog=interrupted.is_set(), wall_seconds=monotonic() - started,
                      cpu_seconds=process_time() - cpu_start, solver_stats=solver.accum_stats())
        print(f"a={a}: {status} after {result['wall_seconds']:.3f}s", flush=True)
        if decided is False:
            pysolvers.flushpr(solver.prfp)
            solver.prfile.seek(0)
            with proof_path.open("xb") as handle:
                copyfileobj(solver.prfile, handle)
            result.update(proof_file=proof_path.name, proof_sha256=digest(proof_path),
                          proof_bytes=proof_path.stat().st_size)
        elif decided is True:
            result.update(save_assignment(a, stem, formula, solver.get_model()))
    receipt_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result), flush=True)


def verify(a):
    stem, building = validated_build(a)
    solve_record = json.loads(stem.with_suffix(".solve.json").read_text(encoding="utf-8"))
    proof = stem.with_suffix(".drup")
    assert solve_record["status"] == "UNSAT"
    assert solve_record["cnf_sha256"] == building["sha256"]["cnf"]
    assert solve_record["proof_sha256"] == digest(proof)
    assert digest(CHECKER) == CHECKER_SHA256
    assert digest(CHECKER_DIR / "drat-trim.c") == CHECKER_SOURCE_SHA256
    log = stem.with_suffix(".verify.log")
    receipt = stem.with_suffix(".verify.json")
    if log.exists() or receipt.exists():
        raise FileExistsError(f"Existing official verifier artifacts for a={a}")
    options = ["-I", "-U", "-t", str(CHECK_SECONDS - 10)]
    started = monotonic()
    timed_out = False
    exit_status = None
    with log.open("xb") as stream:
        try:
            done = subprocess.run([str(CHECKER), stem.with_suffix(".cnf").name, proof.name, *options],
                                  cwd=HERE, stdout=stream, stderr=subprocess.STDOUT,
                                  timeout=CHECK_SECONDS, check=False)
            exit_status = done.returncode
        except subprocess.TimeoutExpired:
            timed_out = True
    statuses = [line.strip() for line in log.read_text(encoding="ascii", errors="replace").splitlines()
                if line.startswith("s ")]
    accepted = not timed_out and exit_status == 0 and statuses == ["s VERIFIED"]
    result = dict(a=a, status="VERIFIED_RUP_UNSAT" if accepted else "VERIFY_INCOMPLETE",
                  verifier="official drat-trim", checker_commit="2e3b2dc0ecf938addbd779d42877b6ed69d9a985",
                  checker_sha256=CHECKER_SHA256, checker_source_sha256=CHECKER_SOURCE_SHA256,
                  script_sha256=digest(Path(__file__)), cnf_sha256=building["sha256"]["cnf"],
                  pb_sha256=building["sha256"]["pb"], proof_sha256=solve_record["proof_sha256"],
                  proof_bytes=proof.stat().st_size, log_sha256=digest(log), options=options,
                  wall_seconds=monotonic() - started, timeout=timed_out, exit_status=exit_status,
                  verifier_status=statuses)
    receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("solve", "verify"))
    parser.add_argument("a", type=int, choices=(0, 1))
    args = parser.parse_args()
    (solve if args.mode == "solve" else verify)(args.a)


if __name__ == "__main__":
    main()
