"""Bind the independently reconstructed structured-union CNF to official RUP verdict."""

from hashlib import file_digest
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DELTA2 = HERE.parent
sys.path.insert(0, str(DELTA2.parent / "certificates"))

from audit_bind import DRAT_COMMIT, DRAT_SHA, DRAT_SOURCE_SHA, TOOL, bind, bind_source_audits


def digest(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def main():
    stem = HERE / "a1_large_face_union"
    pb, cnf, mapping, proof, log = (stem.with_suffix(s) for s in (
        ".pb", ".cnf", ".map.json", ".drup", ".verify.log"
    ))
    build_path, solve_path, check_path = (stem.with_suffix(s) for s in (
        ".build.json", ".solve.json", ".verify.json"
    ))
    rebuild_path = HERE / "audit_union_rebuild.json"
    source_audit_path = DELTA2 / "STRUCTURE_FIXED_B_REVIEW_check.json"
    build, solve, check, rebuild = map(read, (build_path, solve_path, check_path, rebuild_path))
    assert rebuild["verdict"] == "PASS"
    assert digest(build_path) == rebuild["build_receipt_sha256"]
    assert digest(source_audit_path) == rebuild["fixed_face_source_audit_sha256"]
    assert digest(HERE / "audit_union_rebuild.py") == rebuild["independent_script_sha256"]
    p_hash, c_hash, m_hash, proof_hash = map(digest, (pb, cnf, mapping, proof))
    for k, h in (("pb", p_hash), ("cnf", c_hash), ("map", m_hash)):
        assert build["sha256"][k] == rebuild["sha256"][k] == h
    assert digest(HERE / "prove_union.py") == solve["script_sha256"] == check["script_sha256"]
    assert solve["script_sha256"] == "d04b713a0436ae4339fda2f3d5ebcab89862c25ebb3e0edc502d0de405a48c9b"
    assert solve["status"] == "UNSAT" and solve["imported_learned_clauses"] == 0
    assert solve["trace_file"] == proof.name and solve["trace_bytes"] == proof.stat().st_size > 0
    assert solve["trace_sha256"] == check["proof_sha256"] == proof_hash
    assert check["proof_bytes"] == solve["trace_bytes"]
    assert solve["cnf_sha256"] == check["cnf_sha256"] == c_hash
    assert solve["pb_sha256"] == check["pb_sha256"] == p_hash

    assert check["official_checker_commit"] == DRAT_COMMIT
    assert check["checker_source_sha256"] == digest(TOOL / "drat-trim.c") == DRAT_SOURCE_SHA
    assert check["checker_sha256"] == digest(TOOL / "drat-trim.exe") == DRAT_SHA
    assert check["flags"] == ["-I", "-U", "-t", "590"]
    assert check["status"] == "VERIFIED_RUP_UNSAT" and not check["timeout"] and check["exit_status"] == 0
    assert check["log_sha256"] == digest(log)
    lines = log.read_text(encoding="ascii").splitlines()
    assert [line.strip() for line in lines if line.strip().startswith("s ")] == check["verifier_status"] == ["s VERIFIED"]
    rat_lines = [line for line in lines if "RAT lemmas in core" in line]
    assert rat_lines == check["core_rat_counts"] and len(rat_lines) == 1 and rat_lines[0].startswith("c 0 RAT")
    with proof.open("rb") as handle:
        handle.seek(max(0, proof.stat().st_size - 64))
        assert handle.read().splitlines()[-1].strip() == b"0"

    a0 = bind(0)
    assert a0["status"] == "VERIFIED_RUP_UNSAT"
    result = {
        "verdict": "PASS",
        "scope": "Actual RUP terminal certificates for a=0 and the full 23-row structured a=1 union; source-model necessity and CNF encoding audited separately.",
        "source_necessity_audits": bind_source_audits(),
        "a0": a0,
        "a1": {
            "status": check["status"],
            "cnf_variables": rebuild["cnf_variables"],
            "cnf_clauses": rebuild["cnf_clauses"],
            "proof_bytes": proof.stat().st_size,
            "verify_seconds": check["wall_seconds"],
            "core_rat_counts": rat_lines,
            "sha256": {x.name: digest(x) for x in (pb, cnf, mapping, proof, log,
                                                 build_path, solve_path, check_path, rebuild_path)},
        },
        "verifier": {"commit": DRAT_COMMIT, "source_sha256": DRAT_SOURCE_SHA, "binary_sha256": DRAT_SHA},
        "audit_script_sha256": digest(Path(__file__)),
    }
    with (HERE / "audit_union_certificate_binding.json").open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()

