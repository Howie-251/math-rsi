"""Check the two saved binary LRAT traces with official lrat-trim 0.2.0.

No SAT solver is invoked. Historical solver reports remain unchanged.
This establishes the saved CNFs' unsatisfiability, not the Lean graph bridge.
"""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "computations/dd82/n62/d1_connected_diagnostic"
OUTPUT = INPUT / "certificate_checks"
TOOL = ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (512*1024**2, 512*1024**2))


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    OUTPUT.mkdir(exist_ok=True)
    version = subprocess.check_output([str(TOOL), "-V"], text=True).strip()
    assert version == "0.2.0"
    reports = []
    for b in (28, 41):
        name = f"D1_HARD_b_{b}"
        cnf = INPUT / f"{name}.cnf"
        proof = INPUT / f"{name}.bounded120.lrat"
        log = OUTPUT / f"{name}.log"
        result = OUTPUT / f"{name}.json"
        assert not any(p.exists() for p in (log, result)), "Preserve prior checks"
        # Supplying CNF enables checking. --no-trim checks all additions.
        # Release 0.2.0 reports backward checking in this observed mode.
        check_command = [str(TOOL), "--no-trim", str(cnf), str(proof)]
        command = check_command
        start = time.monotonic()
        with log.open("x") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       preexec_fn=limits, start_new_session=True)
            timeout = False
            while True:
                pid, wait_status, usage = os.wait4(process.pid, os.WNOHANG)
                if pid:
                    break
                if time.monotonic()-start >= 120:
                    timeout = True
                    os.killpg(process.pid, 9)
                    pid, wait_status, usage = os.wait4(process.pid, 0)
                    break
                time.sleep(0.05)
            code = os.waitstatus_to_exitcode(wait_status)
            process.returncode = code
        log_text = log.read_text()
        verified = code == 20 and "s VERIFIED" in log_text.splitlines()
        report = dict(case=name, status="CERTIFICATE_CHECKED_UNSAT" if verified else
                      ("CHECKER_WALL_TIMEOUT" if timeout else "CHECKER_DID_NOT_VERIFY"),
                      exit_code=code, checker="official arminbiere/lrat-trim",
                      checker_version=version, source_tag="rel-0.2.0",
                      source_record=".tools/dd82-lrat-check/source_and_build.json",
                      checker_command=check_command, invocation=command,
                      wall_seconds=time.monotonic()-start,
                      cpu_seconds=usage.ru_utime+usage.ru_stime,
                      max_rss_kib=usage.ru_maxrss,
                      cpu_limit_seconds=120, wall_limit_seconds=120,
                      memory_limit_bytes=4*1024**3, output_file_limit_bytes=512*1024**2,
                      pinned_cpu=next(iter(os.sched_getaffinity(0))), cpu_count=1,
                      cnf=str(cnf.relative_to(ROOT)), proof=str(proof.relative_to(ROOT)),
                      proof_bytes=proof.stat().st_size, proof_format="binary LRAT",
                      proof_checked=verified, all_proof_additions_checked=verified,
                      lean_graph_bridge=False, lean_kernel_checked=False,
                      solver_rerun=False)
        result.write_text(json.dumps(report, indent=2)+"\n")
        reports.append(report)
        (OUTPUT / "results.json").write_text(json.dumps(reports, indent=2)+"\n")
        print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
