"""One authorized 120-CPU-second attempt on the prepared full false-twin CNF.

No repeated solver launches, extra inputs or resumable internal state are managed.
UNSAT is retained as RAW until the existing independent LRAT checker passes.
"""
from pathlib import Path
import json
import os
import resource
import subprocess
import sys
import time

from hs_augmentation import ROOT, dump

BASE = ROOT / "computations/dd82/construction"
OUT = BASE / "full_matching58_run"
CPU_SECONDS = 120
MEMORY_BYTES = 4 * 1024**3
PROOF_BYTES = 256 * 1024**2


def bounded(command, logfile, seconds, wall_seconds, cap_output=False):
    pin = min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0, {pin})
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds+1))
        resource.setrlimit(resource.RLIMIT_AS, (MEMORY_BYTES, MEMORY_BYTES))
        if cap_output:
            resource.setrlimit(resource.RLIMIT_FSIZE, (PROOF_BYTES, PROOF_BYTES))

    before, start = resource.getrusage(resource.RUSAGE_CHILDREN), time.monotonic()
    with logfile.open("w") as stream:
        try:
            rc = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                preexec_fn=limits, timeout=wall_seconds).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command, exit_code=rc, cpu_budget_seconds=seconds,
        wall_budget_seconds=wall_seconds, pinned_cpu=pin, threads=1,
        cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-start)


def main():
    enc = json.loads((OUT / "encoding.json").read_text())
    assert not (OUT / "launch.json").exists(), "Only one authorized solver attempt"
    solver = ROOT / ".tools/lean-4.24.0-linux/bin/cadical"
    command = [str(solver), "--lrat", "-t", str(CPU_SECONDS),
               str(OUT / "input.cnf"), str(OUT / "proof.lrat")]
    dump(OUT / "launch.json", dict(parent_run_id=enc["parent_run_id"], command=command,
         scope=enc["scope"], cpu_budget_seconds=CPU_SECONDS, threads=1,
         memory_limit_bytes=MEMORY_BYTES, proof_output_limit_bytes=PROOF_BYTES,
         solver_calls=1, retained_internal_solver_state=False,
         prior_solver_profile_calls=0, preparation_profile="encoding plus seed/CNF consistency only"))
    result = bounded(command, OUT / "solver.log", CPU_SECONDS, CPU_SECONDS+30, True)
    rc = result["exit_code"]
    result.update(parent_run_id=enc["parent_run_id"], scope=enc["scope"], solver_calls=1,
        variables=enc["variables"], clauses=enc["clauses"], proof_checked=False,
        retained_internal_solver_state=False,
        proof_bytes=(OUT / "proof.lrat").stat().st_size if (OUT / "proof.lrat").exists() else 0,
        status={10:"SAT_CANDIDATE", 20:"RAW_UNSAT", 0:"UNKNOWN", None:"WALL_LIMIT_UNKNOWN",
                -9:"CPU_LIMIT_UNKNOWN", -24:"CPU_LIMIT_UNKNOWN", -25:"OUTPUT_LIMIT_UNKNOWN"}
                .get(rc, "PROCESS_FAILURE_UNKNOWN"))
    dump(OUT / "result.json", result)
    print(json.dumps(result), flush=True)
    if rc == 10:
        decode = [sys.executable, str(BASE / "full_matching58_prepare.py"),
                  "decode", "--log", str(OUT / "solver.log")]
        result["model_decode"] = bounded(decode, OUT / "decode.log", 10, 20)
        assert result["model_decode"]["exit_code"] == 0
        verify = [sys.executable, str(BASE / "verify_hs_candidate.py"), str(OUT / "candidate.json")]
        result["independent_bfs_process"] = bounded(verify, OUT / "bfs.log", 10, 20)
        assert result["independent_bfs_process"]["exit_code"] == 0
        result["independent_graph_check"] = json.loads((OUT / "candidate.verification.json").read_text())
        if result["independent_graph_check"]["valid_target"]:
            result["status"] = "VERIFIED_TARGET"
    elif rc == 20:
        checker = [str(ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"),
                   "--no-trim", str(OUT / "input.cnf"), str(OUT / "proof.lrat")]
        check = bounded(checker, OUT / "certificate_check.log", 120, 150)
        check["verified"] = check["exit_code"] == 20 and "s VERIFIED" in (OUT / "certificate_check.log").read_text().splitlines()
        result["certificate_check"] = check
        result["proof_checked"] = check["verified"]
        if check["verified"]:
            result["status"] = "CHECKED_UNSAT"
    dump(OUT / "result.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
