#!/usr/bin/env python3
"""Compile and execute both 128-bit C++20 verifiers for T3 and T4 (m=1024) in a scratch directory."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SRC = HERE / "source"
FA = SRC / "asymptotic_05912_flag_algebra"
RES = SRC / "research_asymptotic_20261031"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--work-dir", type=Path, required=True, help="New scratch output directory")
    ap.add_argument("--compiler", default="g++")
    args = ap.parse_args()
    out = args.work_dir.resolve()
    if out.exists():
        ap.error("--work-dir must not already exist")
    out.mkdir(parents=True)

    t0 = time.monotonic()
    data_dir = out / "qm_data"
    data_dir.mkdir()
    os.symlink(RES / "baseline" / "full_masks.bin", data_dir / "full_masks.bin")
    for f in (RES / "vendor" / "data").iterdir():
        if f.is_file():
            os.symlink(f, data_dir / f.name)

    exe_t3 = out / "independent_verify_track1"
    exe_t4 = out / "verify_qm_degree_potential"
    subprocess.run([args.compiler, "-std=c++20", "-O3", f"-I{FA}", str(FA / "independent_verify_track1.cpp"), "-o", str(exe_t3)], check=True)
    subprocess.run([args.compiler, "-std=c++20", "-O3", str(FA / "verify_qm_degree_potential.cpp"), "-o", str(exe_t4)], check=True)

    r_t3 = subprocess.run(
        [str(exe_t3), str(RES / "baseline" / "full_masks.bin"), str(FA / "q_int64.bin"),
         str(FA / "factors_int64.bin"), "62", str(FA / "cop_terms_general.txt"), str(FA / "cubic_terms.txt")],
        capture_output=True, text=True, check=True,
    )
    t3_json = json.loads(r_t3.stdout.strip())
    assert t3_json["status"] == "PASS" and t3_json["graphs_checked"] == 3212821
    assert t3_json["maximum_numerator"] == "523510268530411454208"
    assert t3_json["common_denominator"] == "885443715538058477568"

    pot = json.loads((FA / "track1_v1_qm_exact_potentials.json").read_text(encoding="utf-8"))[-1]
    assert pot["m"] == 1024
    r_t4 = subprocess.run(
        [str(exe_t4), str(data_dir), str(FA / "q_int64.bin"), "62",
         str(pot["U"]), str(pot["m"]), str(pot["S"]), str(pot["a_int"]),
         *[str(x) for x in pot["b_int"]]],
        capture_output=True, text=True, check=True,
    )
    t4_json = json.loads(r_t4.stdout.strip())
    assert t4_json["status"] == "PASS_EXACT_128BIT_POTENTIAL"
    assert t4_json["minimum_Q4_slack"] == "0"
    assert t4_json["deficit_numerator"] == "1606145007833500875963671347200"
    assert t4_json["deficit_denominator"] == "45545029376000000000"

    receipt_py = subprocess.run([sys.executable, "-B", str(FA / "verify_05912.py")], capture_output=True, text=True, check=True)
    summary = {
        "status": "PASS",
        "seconds": round(time.monotonic() - t0, 4),
        "T3_exact": "681653995482306581/1152921504606846976",
        "T4_exact": "9701859764505653085708308080340303/16409326186106551516455239680000000",
        "track1_cpp": t3_json,
        "potential_m1024_cpp": t4_json,
        "receipt_script_exit": receipt_py.returncode,
    }
    (out / "REPLAY_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
