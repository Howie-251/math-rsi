#!/usr/bin/env python3
"""Verify the in-repo Q7 E16 bundle, 290 baseline imports, S6 large-face bases, and Q6 A8 census."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
SRC = HERE / "source"
PKG = SRC / "archive_inventory" / "E16_PACKAGE.json"
INV = HERE / "INVENTORY.json"


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def verify_mu0_basis_rows(mu0_dir: Path) -> dict:
    meta = json.loads((mu0_dir / "MU0_STRUCTURED_JOINT.json").read_text(encoding="utf-8"))
    assert meta["source_variables"] == meta["variables"] == 29424
    assert meta["source_constraints"] == 100055 and meta["constraints"] == 100051
    assert len(meta["removed_signed_order"]) == 5
    assert sha256(mu0_dir / "MU0_JOINT_NECESSARY.pb") == meta["source_pb_sha256"]
    assert sha256(mu0_dir / "MU0_STRUCTURED_JOINT.pb") == meta["structured_pb_sha256"]

    rows = []
    for spec in meta["basis_files"]:
        a = spec["a"]
        bf = mu0_dir / spec["file"]
        assert sha256(bf) == spec["sha256"]
        rep = json.loads(bf.read_text(encoding="utf-8"))
        assert rep["status"] == "COMPLETE" and len(rep["representatives"]) == spec["row_count"]
        r = 8 - a
        for item in rep["representatives"]:
            L, V = item["L"], item["V"]
            assert len(L) == len(set(L)) == r and len(V) == len(set(V)) == r
            assert all(isinstance(v, int) and 0 <= v < 64 and v.bit_count() % 2 == 0 for v in L)
            assert all(isinstance(v, int) and 0 <= v < 64 and v.bit_count() % 2 == 1 for v in V)
            odd = {64 + v for v in L}
            even = {64 + (63 ^ v) for v in V}
            assert all((x ^ y).bit_count() != 1 for x in odd for y in even)
            holes = odd | even
            rows.append(tuple(int(v in holes) for v in range(64, 128)))
    assert len(rows) == len(set(rows)) == 189
    row_bits_sha = hashlib.sha256(b"".join(bytes(row) for row in rows)).hexdigest()
    assert row_bits_sha == meta["allowed_table"]["row_bits_sha256"]
    return {
        "rows_verified": len(rows),
        "row_bits_sha256": row_bits_sha,
        "structured_pb_sha256": meta["structured_pb_sha256"],
    }


def main() -> int:
    pkg = json.loads(PKG.read_text(encoding="utf-8"))
    inv = json.loads(INV.read_text(encoding="utf-8"))
    omitted_paths = {row["path"] for row in inv["omitted_files"]}

    verified_payload = 0
    for rec in pkg["payload"]:
        if rec["path"] in omitted_paths:
            continue
        fp = SRC / rec["path"]
        assert fp.is_file() and fp.stat().st_size == rec["size"], rec["path"]
        assert sha256(fp) == rec["sha256"], rec["path"]
        verified_payload += 1

    verified_imports = 0
    for rec in pkg["baseline_imports"]:
        fp = SRC / rec["path"]
        assert fp.is_file() and sha256(fp) == rec["sha256"], rec["path"]
        verified_imports += 1

    mu0_dir = SRC / "research" / "seven_directions" / "mu0_global_2026_11_15"
    q6_a8_dir = SRC / "research" / "seven_directions" / "mu1_global_2026_11_15" / "q6_a8"
    basis_summary = verify_mu0_basis_rows(mu0_dir)

    ortools_rebuilt = False
    with tempfile.TemporaryDirectory(prefix="q7-e16-checks-") as tmp:
        tmp_p = Path(tmp)
        work_mu0 = tmp_p / "mu0"
        shutil.copytree(mu0_dir, work_mu0)
        for out_json in ("MU0_A0_BASIS_REVIEW_check.json", "MU0_A0_PLANS_REVIEW_check.json", "MU0_A12_BASIS_REVIEW_check.json"):
            (work_mu0 / out_json).unlink()
        for script in ("MU0_A0_BASIS_REVIEW_check.py", "MU0_A0_PLANS_REVIEW_check.py", "MU0_A12_BASIS_REVIEW_check.py"):
            subprocess.run([sys.executable, "-B", str(work_mu0 / script)], cwd=str(work_mu0), capture_output=True, text=True, check=True)

        work_a8 = tmp_p / "q6_a8"
        shutil.copytree(q6_a8_dir, work_a8)
        (work_a8 / "Q6_A8_FULL_REVIEW_check.json").unlink()
        subprocess.run([sys.executable, "-B", str(work_a8 / "Q6_A8_FULL_REVIEW_check.py")], cwd=str(work_a8), capture_output=True, text=True, check=True)

        if importlib.util.find_spec("ortools") is not None:
            expected_pb_sha = basis_summary["structured_pb_sha256"]
            (work_mu0 / "MU0_STRUCTURED_JOINT.pb").unlink()
            (work_mu0 / "MU0_STRUCTURED_JOINT.json").unlink()
            subprocess.run([sys.executable, "-B", str(work_mu0 / "MU0_STRUCTURED_JOINT.py")], cwd=str(work_mu0), capture_output=True, text=True, check=True)
            assert sha256(work_mu0 / "MU0_STRUCTURED_JOINT.pb") == expected_pb_sha
            ortools_rebuilt = True

    out = {
        "status": "PASS",
        "verified_in_repo_payload_files": verified_payload,
        "verified_bundled_baseline_imports": verified_imports,
        "omitted_large_cnf_drup_exe_count": len(omitted_paths),
        "mu0_large_face_basis": basis_summary,
        "stdlib_independent_checks_passed": [
            "MU0_A0_BASIS_REVIEW_check.py (4950 labeled -> 19 S6 orbits)",
            "MU0_A0_PLANS_REVIEW_check.py (19 a=0 plans)",
            "MU0_A12_BASIS_REVIEW_check.py (98 + 72 S6 orbits)",
            "Q6_A8_FULL_REVIEW_check.py (41-orbit Q6 A8 geometry + odd fibers)",
        ],
        "ortools_pb_rebuilt_in_this_env": ortools_rebuilt,
        "scope": "Verifies all 261 in-repo E16 payload files, all 290 bundled baseline imports, the 189-row S6 large-face table, and stdlib independent orbit/plan checkers for MU0 and Q6 A8. Replaying the 10 omitted .cnf/.drup certificates requires the external R-S-n=7(2).rar archive and drat-trim.",
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
