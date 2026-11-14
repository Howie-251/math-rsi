"""Check the frozen strong-column central basis through accepted seven-axis gates."""

from pathlib import Path
import json
from time import process_time
from unittest.mock import patch

from R7_E16_MU3_CENTRAL_S2_PREFLIGHT import INPUTS, S3_REVIEW, accepted_central_s3_cuts
import R7_E16_MU3_CENTRAL_S3_FIXED_PLANS as earlier


BASE = Path(__file__).with_name("R7_E16_MU3_CENTRAL_S2_STRONG_BASE.json")
BASE_SHA256 = "dace8049caf39bef4192d576a109ac6cb4cd3b59de0e8c5e21f451b7b7124c5d"
EXPECTED = 19_718
CPU_LIMIT = 90
COMPUTE_LIMIT = 88
ACCEPTED = {name: digest for name, digest in earlier.ACCEPTED.items()
            if name != "R7_E16_MU3_CENTRAL_M3_REVIEW.json"}
ACCEPTED[S3_REVIEW] = INPUTS[S3_REVIEW]
EARLIER_CUTS = earlier.accepted_cut_witness


def accepted_cut_witness(colors):
    s3 = accepted_central_s3_cuts(colors)
    if not s3:
        witness = EARLIER_CUTS(colors)
        assert witness is None or "accepted_central_m_ge3" not in witness
        return witness

    outer, side, alpha, sparse = s3[0]
    gates = earlier.previous_pass.gates
    cut = next(row for row in gates.directed_cuts(colors) if row[:3] == (outer, side, alpha))
    _, _, _, donor, receiver = cut
    major, minor = receiver
    loads = tuple((i, (len(gates.face(major, i, 1)), len(gates.face(minor, i, 1))))
                  for i in gates.AXES if i != outer)
    assert tuple(i for i, (c, d) in loads if c - d in (1, 2)) == sparse
    return {"accepted_central_s_ge3": gates.previous.witness(
        outer, side, alpha, donor, receiver, inner_loads=loads, sparse_axes=sparse)}


def run(start):
    with (patch.object(earlier, "BASE", BASE),
          patch.object(earlier, "BASE_SHA256", BASE_SHA256),
          patch.object(earlier, "EXPECTED", EXPECTED),
          patch.object(earlier, "CPU_LIMIT", CPU_LIMIT),
          patch.object(earlier, "COMPUTE_LIMIT", COMPUTE_LIMIT),
          patch.object(earlier, "ACCEPTED", ACCEPTED),
          patch.object(earlier, "accepted_cut_witness", accepted_cut_witness)):
        return earlier.run(start)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as out:
        out.write(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "positives"}))
