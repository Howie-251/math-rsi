"""Bind the actual official RUP checking result to the independently audited CNF."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "certificates" / "mu0_structured_joint"
CHECKER = HERE.parent / "mu3_hard_first_2026_11_15" / "PROOF_TOOLS" / "drat_trim_official_2e3b2dc"


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    files = {
        "pb": HERE / "MU0_STRUCTURED_JOINT.pb",
        "cnf": CERT.with_suffix(".cnf"),
        "map": CERT.with_suffix(".map.json"),
        "build": CERT.with_suffix(".build.json"),
        "solve": CERT.with_suffix(".solve.json"),
        "proof": CERT.with_suffix(".drup"),
        "verify": CERT.with_suffix(".verify.json"),
        "log": CERT.with_suffix(".verify.log"),
        "verify_driver": HERE / "MU0_STRUCTURED_PROOF.py",
        "checker_exe": CHECKER / "drat-trim.exe",
        "checker_source": CHECKER / "drat-trim.c",
        "independent_cnf_reconstruction": HERE / "MU0_STRUCTURED_CNF_REVIEW_check.json",
        "independent_pb_reconstruction": HERE / "MU0_STRUCTURED_SOURCE_REVIEW_check.json",
    }
    hashes = {role: digest(path) for role, path in files.items()}
    read_json = lambda role: json.loads(files[role].read_bytes())
    build, solve, verify = (read_json(role) for role in ("build", "solve", "verify"))
    cnf_review, pb_review = (
        read_json(role) for role in ("independent_cnf_reconstruction", "independent_pb_reconstruction")
    )
    assert cnf_review["verdict"] == pb_review["verdict"] == "PASS"
    assert pb_review["structured_pb_sha256"] == hashes["pb"]
    assert cnf_review["build_receipt_sha256"] == hashes["build"]
    for role in ("pb", "cnf", "map"):
        assert build["sha256"][role] == cnf_review["inputs_sha256"][role] == hashes[role]
    for receipt in (solve, verify):
        assert receipt["pb_sha256"] == hashes["pb"]
        assert receipt["cnf_sha256"] == hashes["cnf"]
        assert receipt["driver_sha256"] == hashes["verify_driver"]
    assert solve["status"] == "UNSAT" and not solve["interrupted_by_watchdog"]
    assert solve["imported_learned_clauses"] == 0
    assert solve["trace_file"] == files["proof"].name
    assert solve["trace_sha256"] == verify["proof_sha256"] == hashes["proof"]
    assert solve["trace_bytes"] == verify["proof_bytes"] == files["proof"].stat().st_size
    with files["proof"].open("rb") as proof:
        proof.seek(-512, 2)
        assert proof.read().splitlines()[-1].strip() == b"0"
    assert verify["checker_sha256"] == hashes["checker_exe"] == "4c37fb793037739ab5ef9019fa7bc579368a6db23a6076c4bd77952149c7391f"
    assert verify["checker_source_sha256"] == hashes["checker_source"] == "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
    assert verify["flags"] == ["-I", "-U", "-t", "590"]
    assert verify["exit_status"] == 0 and not verify["timeout"]
    assert verify["status"] == "VERIFIED_RUP_UNSAT"
    assert verify["log_sha256"] == hashes["log"]
    lines = files["log"].read_text(encoding="ascii").splitlines()
    statuses = [line.strip() for line in lines if line.startswith("s ")]
    assert statuses == verify["verifier_status"] == ["s VERIFIED"]
    rat_core = [line for line in lines if "RAT lemmas in core" in line]
    assert rat_core == verify["core_rat_counts"] and len(rat_core) == 1
    assert re.search(r"(?<!\d)0 RAT lemmas in core\b", rat_core[0])
    record = {
        "verdict": "PASS",
        "scope": "Binding of actual official RUP verification to byte-reconstructed frozen joint CNF and original PB.",
        "artifact_sha256": hashes,
        "audit_source_sha256": digest(Path(__file__).resolve()),
        "proof_bytes": solve["trace_bytes"],
        "solve_wall_seconds": solve["wall_seconds"],
        "official_rup_verification_wall_seconds": verify["wall_seconds"],
        "official_rup_logs": statuses + rat_core,
        "independent_solver_calls": 0,
    }
    (HERE / "MU0_STRUCTURED_PROOF_REVIEW_check.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{statuses[0]}; {rat_core[0]}; proof and CNF hashes match")


if __name__ == "__main__":
    main()

