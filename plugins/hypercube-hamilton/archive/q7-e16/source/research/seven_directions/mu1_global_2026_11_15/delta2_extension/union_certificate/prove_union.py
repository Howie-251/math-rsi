"""Proof-log the joint 23-face query and independently check its exact DRUP."""

import argparse
import json
from pathlib import Path
from shutil import copyfileobj
import subprocess
from threading import Event, Thread
from time import monotonic, process_time, sleep

from build_union import HERE, digest
from fixed_face_probe import readback
from prove_edge import (
    CHECKER, CHECKER_DIR, CHECKER_SHA256, CHECKER_SOURCE_SHA256, CHECK_SECONDS,
    CNF, Glucose4, check_source_assignment, cp_model_pb2, pysolvers,
)

STEM = HERE / "a1_large_face_union"
PROOF = STEM.with_suffix(".drup")
HOLD_SECONDS = 180
FIRST_SECONDS = 300
CONTINUE = HERE / "union_continue_seconds.txt"


def validated_build():
    receipt = json.loads(STEM.with_suffix(".build.json").read_text(encoding="utf-8"))
    for suffix, key in ((".cnf", "cnf"), (".pb", "pb"), (".map.json", "map")):
        assert digest(STEM.with_suffix(suffix)) == receipt["sha256"][key]
    return receipt


def limited_solve(solver, seconds):
    done, interrupted = Event(), Event()
    start, cpu = monotonic(), process_time()

    def watchdog():
        while not done.wait(0.1):
            if max(monotonic()-start, process_time()-cpu) >= seconds:
                interrupted.set()
                solver.interrupt()
                return

    timer = Thread(target=watchdog, daemon=True)
    timer.start()
    try:
        answer = solver.solve_limited(expect_interrupt=True)
    finally:
        done.set()
        timer.join()
    summary = dict(status="SAT" if answer is True else "UNSAT" if answer is False else "UNKNOWN",
                   wall_seconds=monotonic()-start, cpu_seconds=process_time()-cpu,
                   interrupted_by_watchdog=interrupted.is_set(),
                   budget_seconds=seconds, solver_stats=solver.accum_stats())
    return answer, summary


def inspect_assignment(formula, model, record):
    assignment = set(model)
    assert len(assignment) == formula.nv and {abs(lit) for lit in assignment} == set(range(1, formula.nv+1))
    assert all(any(lit in assignment for lit in clause) for clause in formula.clauses)
    mapped = json.loads(STEM.with_suffix(".map.json").read_text(encoding="utf-8"))["original_variables"]
    proto = cp_model_pb2.CpModelProto.FromString(STEM.with_suffix(".pb").read_bytes())
    assert [name for name, *_ in mapped] == [v.name for v in proto.variables]
    values = [sum(lit in assignment for lit in row[1:]) for row in mapped]
    check_source_assignment(proto, values)
    H = {int(name[5:]) for (name, *_), v in zip(mapped, values) if v and name.startswith("hole_")}
    B = {v for v in H if v >= 64}
    row, = [row for row in record["source"]["declared_B_rows"]
            if B == set(row["B_alpha_odd"] + row["B_beta_even"])]
    witness = readback(H, row)
    path = STEM.with_suffix(".assignment.json")
    data = dict(row=row, witness=witness, dimacs_assignment=sorted(model, key=abs),
                source_constraints_checked=len(proto.constraints), cnf_clauses_checked=len(formula.clauses))
    path.write_text(json.dumps(data, separators=(",", ":"))+"\n", encoding="utf-8")
    return dict(witness=witness, fixed_B_row=row["index"], assignment_sha256=digest(path))


def wait_for_continuation(solver, steps):
    pysolvers.flushpr(solver.prfp)
    solver.prfile.seek(0, 2)
    checkpoint = STEM.with_suffix(".checkpoint.json")
    checkpoint.write_text(json.dumps(dict(status="AWAITING_CONTINUATION", last=steps[-1],
                                          trace_bytes=solver.prfile.tell(),
                                          hold_seconds=HOLD_SECONDS), indent=2)+"\n", encoding="utf-8")
    print(f"First window UNKNOWN; holding the same solver for {HOLD_SECONDS}s without running another window",
          flush=True)
    wait_start = monotonic()
    while monotonic() - wait_start < HOLD_SECONDS:
        if CONTINUE.exists():
            seconds = int(CONTINUE.read_text(encoding="ascii").strip())
            if seconds <= 0:
                raise ValueError("A continuation needs a positive explicit duration")
            return seconds
        sleep(0.5)
    return None


def solve():
    receipt = validated_build()
    path = STEM.with_suffix(".solve.json")
    if any(p.exists() for p in (path, PROOF, CONTINUE)):
        raise FileExistsError("Union solve artifacts or a stale continuation file already exist")
    formula = CNF(from_file=str(STEM.with_suffix(".cnf")))
    assert (formula.nv, len(formula.clauses)) == (receipt["cnf_variables"], receipt["cnf_clauses"])
    with Glucose4(with_proof=True) as solver:
        solver.append_formula(formula.clauses)
        print(f"23-face union Glucose4 started; initial {FIRST_SECONDS}s proof window", flush=True)
        answer, first = limited_solve(solver, FIRST_SECONDS)
        steps = [first]
        if answer is None and (seconds := wait_for_continuation(solver, steps)):
            solver.clear_interrupt()
            answer, step = limited_solve(solver, seconds)
            steps.append(step)
        result = dict(status=steps[-1]["status"], windows=steps, solver="PySAT Glucose4 with_proof",
                      cnf_sha256=receipt["sha256"]["cnf"], pb_sha256=receipt["sha256"]["pb"],
                      script_sha256=digest(Path(__file__)), imported_learned_clauses=0)
        print(f"23-face union: {result['status']}", flush=True)
        if answer is False or answer is None:
            pysolvers.flushpr(solver.prfp)
            solver.prfile.seek(0)
            target = PROOF if answer is False else STEM.with_suffix(".partial.drup")
            with target.open("xb") as stream:
                copyfileobj(solver.prfile, stream)
            result.update(trace_file=target.name, trace_sha256=digest(target), trace_bytes=target.stat().st_size)
        elif answer is True:
            result.update(inspect_assignment(formula, solver.get_model(), receipt))
    path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result), flush=True)


def verify():
    build = validated_build()
    solved = json.loads(STEM.with_suffix(".solve.json").read_text(encoding="utf-8"))
    assert solved["status"] == "UNSAT" and solved["cnf_sha256"] == build["sha256"]["cnf"]
    assert digest(PROOF) == solved["trace_sha256"] and PROOF.name == solved["trace_file"]
    assert digest(CHECKER) == CHECKER_SHA256 and digest(CHECKER_DIR/"drat-trim.c") == CHECKER_SOURCE_SHA256
    path = STEM.with_suffix(".verify.json")
    log = STEM.with_suffix(".verify.log")
    if path.exists() or log.exists():
        raise FileExistsError("Union verifier artifacts already exist")
    flags = ["-I", "-U", "-t", str(CHECK_SECONDS-10)]
    elapsed = monotonic()
    code, timeout = None, False
    print("Official DRAT-trim is verifying the full trace against the frozen union CNF", flush=True)
    with log.open("xb") as stream:
        try:
            command = [str(CHECKER), STEM.with_suffix(".cnf").name, PROOF.name, *flags]
            result = subprocess.run(command, cwd=HERE, stdout=stream, stderr=subprocess.STDOUT,
                                    timeout=CHECK_SECONDS, check=False)
            code = result.returncode
        except subprocess.TimeoutExpired:
            timeout = True
    lines = log.read_text(encoding="ascii", errors="replace").splitlines()
    statuses = [line.strip() for line in lines if line.startswith("s ")]
    accepted = not timeout and code == 0 and statuses == ["s VERIFIED"]
    result = dict(status="VERIFIED_RUP_UNSAT" if accepted else "VERIFY_INCOMPLETE",
                  official_checker_commit="2e3b2dc0ecf938addbd779d42877b6ed69d9a985",
                  checker_sha256=CHECKER_SHA256, checker_source_sha256=CHECKER_SOURCE_SHA256,
                  flags=flags, wall_seconds=monotonic()-elapsed, timeout=timeout,
                  exit_status=code, verifier_status=statuses, log_sha256=digest(log),
                  cnf_sha256=build["sha256"]["cnf"], pb_sha256=build["sha256"]["pb"],
                  proof_sha256=solved["trace_sha256"], proof_bytes=PROOF.stat().st_size,
                  script_sha256=digest(Path(__file__)),
                  core_rat_counts=[line for line in lines if "RAT lemmas in core" in line])
    path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=("solve", "verify"))
    args = p.parse_args()
    (solve if args.mode == "solve" else verify)()
