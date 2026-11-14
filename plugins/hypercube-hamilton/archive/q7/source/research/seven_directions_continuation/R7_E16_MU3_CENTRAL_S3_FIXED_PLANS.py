"""Check one frozen central s=3 basis using earlier accepted all-axis gates."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

import R7_E16_MU3_CENTRAL_M3_FIXED_PLANS as previous_pass


HERE = Path(__file__).resolve().parent
BASE = HERE / "R7_E16_MU3_CENTRAL_S3_BASE.json"
BASE_SHA256 = "b6a54f6354ec3c9c3b979c15ca05371ae8f68c7860bdb5e41f942b893fe5e973"
EXPECTED = 18_049
CPU_LIMIT = 90
COMPUTE_LIMIT = 88
ACCEPTED = {
    "R41_FULL_REVIEW.json": "3bbd1bae12da13e05fae0ea651e1fed4cdf97372dd99b7062bb424db06489f55",
    "R7_E16_MU3_CENTRAL_M3_REVIEW.json": "31d0009e8a40c65c2c2db6585c47f372d00a7f946950930459582550c247aeec",
    "R7_E16_MU3_CENTRAL_ANTIPODAL_REVIEW.json": "93f2cab6e97679b41f5ac403d060421a113711c8b346240e56073cbe4febb665",
}


def accepted_cut_witness(colors):
    gates = previous_pass.gates
    previous = gates.previous
    antipodal = central = None
    for outer, side, alpha, donor, receiver in gates.directed_cuts(colors):
        major, minor = receiver
        shape = tuple(tuple(map(len, groups)) for groups in (donor, receiver))
        if shape == ((4, 7), (4, 1)):
            return {"accepted_R41_full": previous.witness(outer, side, alpha, donor, receiver, root=minor[0])}
        if shape != ((3, 6), (5, 2)):
            continue
        if antipodal is None and (minor[0] ^ minor[1]).bit_count() == 6:
            antipodal = {"accepted_central_antipodal_h6": previous.witness(outer, side, alpha, donor, receiver, h=6)}
        if antipodal is not None or central is not None:
            continue
        loads = tuple((i, (len(gates.face(major, i, 1)), len(gates.face(minor, i, 1))))
                      for i in gates.AXES if i != outer)
        usable = tuple(i for i, load in loads if load in previous.R32_LOADS)
        if len(usable) >= 3:
            central = {"accepted_central_m_ge3": previous.witness(outer, side, alpha, donor, receiver,
                                                                 inner_loads=loads, usable=usable)}
    return antipodal or central


def run(start):
    for name, expected in ACCEPTED.items():
        raw = (HERE / name).read_bytes()
        assert sha256(raw).hexdigest() == expected and json.loads(raw)["verdict"] == "PASS"
    with (patch.object(previous_pass, "BASE", BASE),
          patch.object(previous_pass, "BASE_SHA256", BASE_SHA256),
          patch.object(previous_pass, "EXPECTED", EXPECTED),
          patch.object(previous_pass, "CPU_LIMIT", COMPUTE_LIMIT),
          patch.object(previous_pass.gates.previous, "high_m_witnesses", accepted_cut_witness)):
        result = previous_pass.run(start)
    for row in result["positives"]:
        plan = row["plan"]
        if plan["gate"] != "accepted_high_m":
            continue
        ((gate, witness),) = plan["witnesses"].items()
        row["plan"] = (dict(gate=gate, **witness) if gate == "accepted_central_antipodal_h6"
                       else dict(gate=gate, witness=witness))
    result["plan_counts"] = Counter(row["plan"]["gate"] for row in result["positives"])
    result["accepted_receipts_sha256"] = ACCEPTED
    result["cpu_limit_seconds"] = CPU_LIMIT
    result["compute_cutoff_cpu_seconds"] = COMPUTE_LIMIT
    return result


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "positives"}))
