"""Bounded independent backward checks of the two frozen E16 certificates."""
from hashlib import file_digest
import json
from pathlib import Path
import subprocess
from time import monotonic

HERE = Path(__file__).resolve().parent
PROOF = HERE.parent
COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
TOOL_SHA = "4c37fb793037739ab5ef9019fa7bc579368a6db23a6076c4bd77952149c7391f"
BUDGET = 600
OPTIONS = ["-I", "-U", "-t", "590"]
SPECS = (
    ("even", "build.json", "prove_900.json"),
    ("odd", "build_odd.json", "prove_odd.json"),
)


def sha(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def check(branch, build_name, proof_name, checker):
    cnf = PROOF / f"{branch}.cnf"
    proof = PROOF / f"{branch}.drup"
    build = read(PROOF / build_name)
    production = read(PROOF / proof_name)
    cnf_hash, proof_hash = sha(cnf), sha(proof)
    assert cnf_hash == build["sha256"][cnf.name] == production["cnf_sha256"]
    assert proof_hash == production["proof_sha256"]
    assert proof.stat().st_size == production["proof_bytes"]
    assert production["status"] == "UNSAT"
    args = [str(checker), cnf.name, proof.name, *OPTIONS]
    log = HERE / f"{branch}_official_drat_trim.log"
    out = HERE / f"{branch}_official_drat_trim.json"
    start = monotonic()
    print(f"{branch}: starting official DRAT-trim in backward RUP mode", flush=True)
    timed_out = False
    exit_status = None
    with log.open("xb") as stream:
        try:
            result = subprocess.run(
                args, cwd=PROOF, stdin=subprocess.DEVNULL, stdout=stream,
                stderr=subprocess.STDOUT, timeout=BUDGET,
            )
            exit_status = result.returncode
        except subprocess.TimeoutExpired:
            timed_out = True
    seconds = monotonic() - start
    lines = log.read_bytes().decode("ascii", errors="replace").splitlines()
    statuses = [line.strip() for line in lines if line.strip().startswith("s ")]
    verified = exit_status == 0 and not timed_out and statuses == ["s VERIFIED"]
    receipt = dict(
        branch=branch, checker="official DRAT-trim", checker_commit=COMMIT,
        checker_source_url=f"https://raw.githubusercontent.com/marijnheule/drat-trim/{COMMIT}/drat-trim.c",
        source_sha256=SOURCE_SHA, checker_sha256=TOOL_SHA, driver_sha256=sha(Path(__file__)),
        compile_flags=["-std=gnu99", "-O2", "-Dgetc_unlocked=getc"],
        cnf_sha256=cnf_hash, proof_sha256=proof_hash, proof_bytes=proof.stat().st_size,
        cnf_file=cnf.name, proof_file=proof.name, options=OPTIONS,
        budget_wall_seconds=BUDGET, wall_seconds=seconds, timeout=timed_out,
        exit_status=exit_status, verifier_status= statuses, log_sha256=sha(log),
        status="VERIFIED_RUP_UNSAT" if verified else "NOT_VERIFIED",
    )
    with out.open("x", encoding="utf-8") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    print(f"{branch}: {receipt['status']} {statuses} exit={exit_status} {seconds:.3f}s", flush=True)
    return verified


def main():
    checker = HERE / "drat-trim.exe"
    assert sha(HERE / "drat-trim.c") == SOURCE_SHA and sha(checker) == TOOL_SHA
    verified = [check(*spec, checker) for spec in SPECS]
    return 0 if all(verified) else 1


if __name__ == "__main__":
    raise SystemExit(main())
