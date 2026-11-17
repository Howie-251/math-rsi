"""Bind independent model regeneration to finished proof-checker artifacts."""

import argparse
from hashlib import file_digest
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOOL = HERE.parents[1] / "mu3_hard_first_2026_11_15" / "PROOF_TOOLS" / "drat_trim_official_2e3b2dc"
DRAT_SHA = "4c37fb793037739ab5ef9019fa7bc579368a6db23a6076c4bd77952149c7391f"
DRAT_SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
DRAT_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
DRIVER_SHA = "c745ccb6d4fdaca0ff94fa2fc2c4f150d45b83f722add57b8f0db750c2855175"


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def bind(a):
    stem = f"edge_a{a}"
    build = HERE / f"{stem}.build.json"
    audit = HERE / f"audit_{stem}_rebuild.json"
    solve = HERE / f"{stem}.solve.json"
    verify = HERE / f"{stem}.verify.json"
    proof = HERE / f"{stem}.drup"
    log = HERE / f"{stem}.verify.log"

    rec = read(audit)
    assert rec["verdict"] == "PASS" and a == rec["a"]
    assert digest(build) == rec["producer_build_receipt_sha256"]
    assert digest(HERE / "audit_rebuild.py") == rec["independent_rebuild_script_sha256"]
    assert digest(HERE / "prove_edge.py") == DRIVER_SHA
    assert digest(TOOL / "drat-trim.exe") == DRAT_SHA
    assert digest(TOOL / "drat-trim.c") == DRAT_SOURCE_SHA
    for suffix, role in ((".cnf", "cnf"), (".pb", "pb"), (".map.json", "map")):
        assert digest(HERE / f"{stem}{suffix}") == rec["output_sha256"][role]
    hashes = {"build": digest(build), "independent_rebuild": digest(audit), **rec["output_sha256"]}
    if not solve.exists():
        return {"a": a, "status": "AWAITING_SOLVER", "sha256": hashes}
    result = read(solve)
    assert result["a"] == a and result["script_sha256"] == DRIVER_SHA
    assert result["cnf_sha256"] == hashes["cnf"] and result["pb_sha256"] == hashes["pb"]
    hashes["solver_receipt"] = digest(solve)
    if result["status"] == "UNKNOWN":
        return {"a": a, "status": "UNKNOWN", "sha256": hashes}
    if result["status"] == "SAT":
        assignment = HERE / f"{stem}.assignment.json"
        assert assignment.name == result["assignment_file"]
        hashes["assignment"] = digest(assignment)
        assert hashes["assignment"] == result["assignment_sha256"]
        return {
            "a": a, "status": "SOLVER_REPORTED_SAT",
            "realized_by_short_matching": result["realized_by_short_matching"],
            "sha256": hashes,
        }
    assert result["status"] == "UNSAT"
    hashes["proof"] = digest(proof)
    assert proof.name == result["proof_file"]
    assert hashes["proof"] == result["proof_sha256"]
    assert proof.stat().st_size == result["proof_bytes"] > 0
    if not verify.exists():
        return {"a": a, "status": "AWAITING_INDEPENDENT_VERIFIER", "sha256": hashes}
    check = read(verify)
    assert check["a"] == a and check["script_sha256"] == DRIVER_SHA
    assert check["checker_commit"] == DRAT_COMMIT
    assert check["checker_sha256"] == DRAT_SHA
    assert check["checker_source_sha256"] == DRAT_SOURCE_SHA
    assert check["options"] == ["-I", "-U", "-t", "590"]
    assert check["cnf_sha256"] == hashes["cnf"] and check["pb_sha256"] == hashes["pb"]
    assert check["proof_sha256"] == hashes["proof"] and check["proof_bytes"] == result["proof_bytes"]
    assert digest(log) == check["log_sha256"]
    hashes["verifier_receipt"] = digest(verify)
    hashes["verifier_log"] = digest(log)
    lines = log.read_text(encoding="ascii", errors="strict").splitlines()
    status_lines = [line.strip() for line in lines if line.strip().startswith("s ")]
    assert status_lines == check["verifier_status"]
    if check["status"] != "VERIFIED_RUP_UNSAT":
        return {"a": a, "status": "VERIFY_INCOMPLETE", "sha256": hashes}
    assert status_lines == ["s VERIFIED"] and check["exit_status"] == 0 and not check["timeout"]
    return {
        "a": a, "status": "VERIFIED_RUP_UNSAT", "sha256": hashes,
        "proof_bytes": result["proof_bytes"],
        "verifier_seconds": check["wall_seconds"],
        "verifier_log": log.name,
    }


def bind_source_audits():
    audits = {
        "EDGE_MODEL_REVIEW.json": "53bf1dd12ba0fb06aa5adb3b96dd7d91988c21a6cc515512d3ec1fc32385bf15",
        "EDGE_HIGH_GAP_MODEL_REVIEW.json": "c95284871d54d90eb4816062287434e60dd4a257a66fdf96609d6871dfd69f1d",
    }
    for name, expected in audits.items():
        receipt = HERE.parent / name
        assert digest(receipt) == expected
        record = read(receipt)
        assert record["verdict"] == "PASS"
        for rel, value in record["audited_input_hashes"].items():
            assert value == "sha256:" + digest(HERE.parent / rel), rel
    return audits

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", choices=("initial", "final"), help="Save the dated audit stage without overwriting previous stages.")
    args = parser.parse_args()
    outcomes = [bind(a) for a in (0, 1)]
    result = {
        "scope": "Independent hash and status binding only; proof truth is checked by fixed official DRAT-trim.",
        "branches": outcomes,
        "source_necessity_audits": bind_source_audits(),
        "both_verified_rup_unsat": all(row["status"] == "VERIFIED_RUP_UNSAT" for row in outcomes),
        "verifier": {"commit": DRAT_COMMIT, "binary_sha256": DRAT_SHA, "source_sha256": DRAT_SOURCE_SHA},
        "driver_sha256": DRIVER_SHA,
        "audit_script_sha256": digest(Path(__file__)),
    }
    output = json.dumps(result, indent=2) + "\n"
    if args.record:
        with (HERE / f"audit_edge_certificate_binding_{args.record}.json").open("x", encoding="utf-8") as stream:
            stream.write(output)
    print(output, end="", flush=True)


if __name__ == "__main__":
    main()
