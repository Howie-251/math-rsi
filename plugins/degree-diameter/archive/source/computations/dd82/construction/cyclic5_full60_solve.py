"""One bounded discovery call on the already prepared full-C5 order-60 CNF.

No input modification, seed fixing, restart, proof output or UNSAT claim.
SAT is accepted only after all actual clauses and an independent BFS pass.
"""
from pathlib import Path
import argparse
import json
import os
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "computations/dd82/construction"
OUT = BASE / "cyclic5_full60_run"
CPU_SECONDS = 120
SOLVER_TIME_SECONDS = 120
WALL_SECONDS = 180
MEMORY_BYTES = 4 * 1024**3


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def bounded(command, log, seconds, wall_seconds, cpu):
    assert cpu in os.sched_getaffinity(0)

    def limits():
        os.sched_setaffinity(0, {cpu})
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds+1))
        resource.setrlimit(resource.RLIMIT_AS, (MEMORY_BYTES, MEMORY_BYTES))

    before, start = resource.getrusage(resource.RUSAGE_CHILDREN), time.monotonic()
    with log.open("w") as stream:
        try:
            rc = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                preexec_fn=limits, timeout=wall_seconds).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command, exit_code=rc, cpu_budget_seconds=seconds,
        wall_budget_seconds=wall_seconds, threads=1, pinned_cpu=cpu,
        cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-start)


def decode(log):
    enc = json.loads((OUT / "encoding.json").read_text())
    lines = log.read_text().splitlines()
    assert "s SATISFIABLE" in lines
    values = {}
    for line in lines:
        if not line.startswith("v "):
            continue
        for q in map(int, line.split()[1:]):
            if q:
                assert abs(q) not in values or values[abs(q)] == (q > 0)
                values[abs(q)] = q > 0
    assert set(values) == set(range(1, enc["variables"]+1))
    false_ids, count = [], 0
    with (OUT / "input.cnf").open() as source:
        for line in source:
            if not line.strip() or line.startswith("c"):
                continue
            if line.startswith("p "):
                assert line.split() == ["p", "cnf", str(enc["variables"]), str(enc["clauses"])]
                continue
            clause = list(map(int, line.split()))
            assert clause[-1] == 0
            count += 1
            if not any(values[abs(q)] == (q > 0) for q in clause[:-1]):
                false_ids.append(count)
    assert count == enc["clauses"]
    save(OUT / "model_check.json", dict(run_id=enc["run_id"],
        assigned_variables=len(values), checked_clauses=count,
        false_clause_count=len(false_ids), false_clause_ids=false_ids,
        all_actual_clauses_satisfied=not false_ids))
    assert not false_ids

    palette = json.loads((OUT / "palette.json").read_text())["orbits"]
    assert len(palette) == 354
    assert {item["variable"] for item in palette} == set(range(1, 355))
    selected, edges = [], set()
    for item in palette:
        if not values[item["variable"]]:
            continue
        a, b, shift = item["a"], item["b"], item["shift"]
        expanded = {tuple(sorted((5*a+t, 5*b+(t+shift) % 5))) for t in range(5)}
        assert len(expanded) == 5 and all(u < v for u, v in expanded)
        assert expanded == {tuple(uv) for uv in item["edges"]}
        assert not edges.intersection(expanded)
        edges.update(expanded)
        selected.append({k: item[k] for k in ["index", "variable", "a", "b", "shift"]})
    assert len(selected) == 48 and len(edges) == 240
    parameters = dict(run_id=enc["run_id"], coordinates="vertex 5*a+t, t in Z5",
        selected_orbit_indices=[item["index"] for item in selected], selected_orbits=selected)
    save(OUT / "candidate.parameters.json", parameters)
    save(OUT / "candidate.json", dict(n=60, edges=sorted(edges),
        run_id=enc["run_id"], source_solver_log=str(log), parameters=parameters,
        status="SAT_CANDIDATE_PENDING_INDEPENDENT_BFS"))
    (OUT / "candidate.edges").write_text("60 240\n" + "".join(f"{u} {v}\n" for u, v in sorted(edges)))
    print(json.dumps(dict(status="SAT_CANDIDATE_PENDING_INDEPENDENT_BFS",
                          n=60, edges=240, selected_orbits=48)))


def solve(cpu):
    assert not (OUT / "launch.json").exists(), "Only one authorized discovery call"
    enc = json.loads((OUT / "encoding.json").read_text())
    assert enc["status"] == "PREPARED_NOT_RUN" and enc["primary_variables"] == 354
    assert cpu in os.sched_getaffinity(0)
    solver = ROOT / ".tools/lean-4.24.0-linux/bin/cadical"
    command = [str(solver), "-t", str(SOLVER_TIME_SECONDS), str(OUT / "input.cnf")]
    save(OUT / "launch.json", dict(run_id=enc["run_id"], command=command,
        scope=enc["scope"], cpu_budget_seconds=CPU_SECONDS,
        solver_soft_time_limit_seconds=SOLVER_TIME_SECONDS, wall_budget_seconds=WALL_SECONDS,
        pinned_cpu=cpu, threads=1, memory_limit_bytes=MEMORY_BYTES,
        proof_output_enabled=False, solver_calls=1, input_modified=False,
        fixed_seed_literals=False, retained_internal_solver_state=False))
    result = bounded(command, OUT / "solver.log", CPU_SECONDS, WALL_SECONDS, cpu)
    rc = result["exit_code"]
    result.update(run_id=enc["run_id"], scope=enc["scope"],
        variables=enc["variables"], clauses=enc["clauses"], primary_variables=354,
        solver_calls=1, proof_output_enabled=False, proof_checked=False,
        retained_internal_solver_state=False, input_modified=False,
        status={10: "SAT_CANDIDATE", 20: "RAW_UNSAT", 0: "UNKNOWN",
                None: "WALL_LIMIT_UNKNOWN", -9: "KILLED_UNKNOWN", -24: "CPU_LIMIT_UNKNOWN"}
                .get(rc, "PROCESS_FAILURE_UNKNOWN"))
    save(OUT / "result.json", result)
    print(json.dumps(result), flush=True)
    if rc == 10:
        result["decode_process"] = bounded(
            [sys.executable, str(Path(__file__).resolve()), "decode", "--log", str(OUT / "solver.log")],
            OUT / "decode.log", 10, 20, cpu)
        if result["decode_process"]["exit_code"] != 0:
            result["status"] = "SAT_MODEL_OR_DECODE_CHECK_FAILED"
        else:
            result["independent_bfs_process"] = bounded(
                [sys.executable, str(BASE / "verify_hs_candidate.py"), str(OUT / "candidate.json")],
                OUT / "independent_bfs.log", 10, 20, cpu)
            if result["independent_bfs_process"]["exit_code"] != 0:
                result["status"] = "SAT_INDEPENDENT_CHECK_FAILED"
            else:
                checked = json.loads((OUT / "candidate.verification.json").read_text())
                result["independent_graph_check"] = checked
                exact_target = (checked["valid_target"] and checked["n"] == 60
                    and checked["edges"] == 240 and checked["degrees"] == [8]*60
                    and checked["diameter"] is not None and checked["diameter"] <= 2
                    and checked["bad_pair_count"] == 0)
                result["status"] = "VERIFIED_TARGET" if exact_target else "SAT_FAILED_TARGET_CHECK"
        result["mathematical_conclusion"] = (
            "An independently verified order-60 target was found"
            if result["status"] == "VERIFIED_TARGET" else "No accepted target; inspect the saved model/check output")
    elif rc == 20:
        result["mathematical_conclusion"] = "None: RAW_UNSAT has no proof certificate and excludes no family"
    else:
        result["mathematical_conclusion"] = "None: UNKNOWN does not decide the free-C5 family"
    save(OUT / "result.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["solve", "decode"])
    parser.add_argument("--cpu", type=int, default=0)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    if args.action == "solve":
        solve(args.cpu)
    else:
        assert args.log is not None
        decode(args.log)
