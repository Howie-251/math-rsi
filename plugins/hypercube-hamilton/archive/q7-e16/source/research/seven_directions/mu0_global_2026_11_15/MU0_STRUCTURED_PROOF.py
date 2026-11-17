"""Produce and independently check a bounded RUP proof for the structured mu=0 CNF."""

import argparse
import json
import os
import subprocess
import tempfile
from pathlib import Path
from shutil import copyfileobj
from threading import Event, Thread
from time import monotonic, process_time

from MU0_STRUCTURED_CNF import HERE, STEM, digest
from MU0_STRUCTURED_DIAGNOSTIC import inspect_witness

from prove_edge import (
    CHECK_SECONDS, CHECKER, CHECKER_DIR, CHECKER_SHA256, CHECKER_SOURCE_SHA256,
    CNF, Glucose4, cp_model_pb2, pysolvers,
)


SAT_SECONDS = 300
PB = HERE / "MU0_STRUCTURED_JOINT.pb"
CNF_PATH = STEM.with_suffix(".cnf")
MAP = STEM.with_suffix(".map.json")
SOLVE_RECEIPT = STEM.with_suffix(".solve.json")
PROOF = STEM.with_suffix(".drup")


def write_json(path, doc):
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(doc, indent=2) + "\n")


def validated_build():
    record = json.loads(STEM.with_suffix(".build.json").read_bytes())
    for role, path in (("pb", PB), ("cnf", CNF_PATH), ("map", MAP)):
        if digest(path) != record["sha256"][role]:
            raise ValueError(f"The CNF build no longer matches its {role}")
    return record


def inspect_assignment(formula, model):
    true = set(model)
    if len(true) != formula.nv or {abs(lit) for lit in true} != set(range(1, formula.nv + 1)):
        raise ValueError("Incomplete DIMACS assignment")
    if not all(any(lit in true for lit in clause) for clause in formula.clauses):
        raise ValueError("DIMACS assignment violates an original clause")
    rows = json.loads(MAP.read_bytes())["original_variables"]
    proto = cp_model_pb2.CpModelProto.FromString(PB.read_bytes())
    if [row[0] for row in rows] != [v.name for v in proto.variables]:
        raise ValueError("Threshold map and source variable order differ")
    source_values = [sum(lit in true for lit in row[1:]) for row in rows]
    witness = inspect_witness(proto, source_values)
    assignment = STEM.with_suffix(".assignment.json")
    write_json(assignment, dict(dimacs_assignment=sorted(true, key=abs),
                                source_assignment=source_values, witness=witness))
    return dict(witness=witness, assignment_sha256=digest(assignment))


def limited_solve(solver):
    finished, interrupted = Event(), Event()
    start, cpu_start = monotonic(), process_time()

    def interrupt_at_limit():
        while not finished.wait(0.1):
            if max(monotonic()-start, process_time()-cpu_start) >= SAT_SECONDS:
                interrupted.set()
                solver.interrupt()
                return

    watchdog = Thread(target=interrupt_at_limit, daemon=True)
    watchdog.start()
    try:
        answer = solver.solve_limited(expect_interrupt=True)
    finally:
        finished.set()
        watchdog.join()
    return answer, dict(wall_seconds=monotonic()-start, cpu_seconds=process_time()-cpu_start,
                        interrupted_by_watchdog=interrupted.is_set(), limit_seconds=SAT_SECONDS,
                        solver_stats=solver.accum_stats())


def solve():
    build = validated_build()
    partial = STEM.with_suffix(".partial.drup")
    outputs = (SOLVE_RECEIPT, PROOF, partial, STEM.with_suffix(".assignment.json"))
    if any(path.exists() for path in outputs):
        raise FileExistsError("The authorized structured query already has solver artifacts")
    for key in ("TMP", "TEMP", "TMPDIR"):
        os.environ[key] = str(STEM.parent)
    tempfile.tempdir = str(STEM.parent)
    formula = CNF(from_file=str(CNF_PATH))
    if (formula.nv, len(formula.clauses)) != (build["cnf_variables"], build["cnf_clauses"]):
        raise ValueError("Unexpected DIMACS size")
    with Glucose4(with_proof=True) as solver:
        solver.append_formula(formula.clauses)
        print(f"Structured joint Glucose4, one {SAT_SECONDS}s proof window", flush=True)
        answer, timing = limited_solve(solver)
        status = "UNSAT" if answer is False else "SAT" if answer is True else "UNKNOWN"
        result = dict(status=status, solver="PySAT Glucose4 with proof logging",
                      pb_sha256=build["sha256"]["pb"], cnf_sha256=build["sha256"]["cnf"],
                      driver_sha256=digest(Path(__file__)), imported_learned_clauses=0, **timing)
        if answer is True:
            result.update(inspect_assignment(formula, solver.get_model()))
        else:
            trace = PROOF if answer is False else partial
            pysolvers.flushpr(solver.prfp)
            solver.prfile.seek(0)
            with trace.open("xb") as stream:
                copyfileobj(solver.prfile, stream)
            result.update(trace_file=trace.name, trace_sha256=digest(trace),
                          trace_bytes=trace.stat().st_size)
    write_json(SOLVE_RECEIPT, result)
    print(json.dumps(result), flush=True)


def verify():
    build = validated_build()
    solved = json.loads(SOLVE_RECEIPT.read_bytes())
    if (solved["status"] != "UNSAT" or solved["cnf_sha256"] != build["sha256"]["cnf"]
            or solved["trace_file"] != PROOF.name or solved["trace_sha256"] != digest(PROOF)):
        raise ValueError("Solver receipt does not bind a complete proof for this CNF")
    if (digest(CHECKER) != CHECKER_SHA256 or
            digest(CHECKER_DIR / "drat-trim.c") != CHECKER_SOURCE_SHA256):
        raise ValueError("Official checker hash mismatch")
    receipt = STEM.with_suffix(".verify.json")
    log = STEM.with_suffix(".verify.log")
    if receipt.exists() or log.exists():
        raise FileExistsError("Verifier artifacts already exist")

    flags = ["-I", "-U", "-t", str(CHECK_SECONDS - 10)]
    start = monotonic()
    code, timeout = None, False
    print("Official drat-trim is checking the complete RUP proof", flush=True)
    with log.open("xb") as stream:
        try:
            checked = subprocess.run([str(CHECKER), CNF_PATH.name, PROOF.name, *flags],
                                     cwd=STEM.parent, stdout=stream, stderr=subprocess.STDOUT,
                                     timeout=CHECK_SECONDS, check=False)
            code = checked.returncode
        except subprocess.TimeoutExpired:
            timeout = True
    lines = log.read_text(encoding="ascii", errors="replace").splitlines()
    statuses = [line.strip() for line in lines if line.startswith("s ")]
    accepted = not timeout and code == 0 and statuses == ["s VERIFIED"]
    result = dict(status="VERIFIED_RUP_UNSAT" if accepted else "VERIFY_INCOMPLETE",
                  checker_sha256=CHECKER_SHA256, checker_source_sha256=CHECKER_SOURCE_SHA256,
                  driver_sha256=digest(Path(__file__)), flags=flags, exit_status=code,
                  timeout=timeout, verifier_status=statuses, wall_seconds=monotonic()-start,
                  cnf_sha256=build["sha256"]["cnf"], pb_sha256=build["sha256"]["pb"],
                  proof_sha256=solved["trace_sha256"], proof_bytes=PROOF.stat().st_size,
                  log_sha256=digest(log), core_rat_counts=[s for s in lines if "RAT lemmas in core" in s])
    write_json(receipt, result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("solve", "verify"))
    (solve if parser.parse_args().mode == "solve" else verify)()
