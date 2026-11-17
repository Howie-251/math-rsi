"""Compile the frozen joint mu=0 PB using the audited E16 DIMACS encoder."""

import json
import sys
from pathlib import Path
from time import perf_counter

from ortools.sat import cp_model_pb2

from MU0_STRUCTURED_JOINT import HERE, checked_bytes

OLD_ENCODER = HERE.parent / "mu1_global_2026_11_15" / "certificates"
CERTIFICATE = HERE / "certificates"
STEM = CERTIFICATE / "mu0_structured_joint"
sys.path.insert(0, str(OLD_ENCODER))

from edge_cnf import MAX_BYTES, MU3_TOOLS, digest, encode


def main():
    start = perf_counter()
    CERTIFICATE.mkdir(exist_ok=True)
    cnf, mapping, receipt = (STEM.with_suffix(s) for s in (".cnf", ".map.json", ".build.json"))
    if any(path.exists() for path in (cnf, mapping, receipt)):
        raise FileExistsError("Structured CNF artifacts already exist")
    source = HERE / "MU0_STRUCTURED_JOINT.pb"
    source_manifest = HERE / "MU0_STRUCTURED_JOINT.json"
    record = json.loads(source_manifest.read_bytes())
    proto = cp_model_pb2.CpModelProto.FromString(checked_bytes(source, record["structured_pb_sha256"]))
    encoder = encode(proto)
    count = len(encoder.clauses)
    header = f"p cnf {encoder.num_vars} {count}\n"
    exact_bytes = len(header) + sum(2 + sum(len(str(lit)) + 1 for lit in clause)
                                    for clause in encoder.clauses)
    print(f"{encoder.num_vars:,} variables, {count:,} clauses, {exact_bytes:,} bytes", flush=True)
    if exact_bytes > MAX_BYTES:
        raise ValueError(f"CNF preflight exceeds {MAX_BYTES:,} bytes")
    with cnf.open("x", encoding="ascii", newline="\n") as stream:
        stream.write(header)
        for clause in encoder.clauses:
            stream.write(" ".join(map(str, (*clause, 0))) + "\n")
    if cnf.stat().st_size != exact_bytes:
        raise ValueError("Unexpected serialized DIMACS size")

    thresholds = {
        "threshold_meaning": "Each list is x>=1, x>=2, ... in source variable order.",
        "original_variables": [[v.name, *encoder.thresholds[i]]
                               for i, v in enumerate(proto.variables)],
        "extra_equalities": [[i, value, lit] for (i, value), lit in encoder.equalities.items()],
    }
    with mapping.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(thresholds, separators=(",", ":")) + "\n")

    files = dict(pb=source, source_manifest=source_manifest, cnf=cnf, map=mapping, driver=Path(__file__),
                 encoder=OLD_ENCODER / "edge_cnf.py", even_encoder=MU3_TOOLS / "even_cnf.py",
                 odd_encoder=MU3_TOOLS / "odd_cnf.py")
    result = dict(status="CNF_BUILT", source_variables=len(proto.variables),
                  source_constraints=len(proto.constraints), cnf_variables=encoder.num_vars,
                  cnf_clauses=count, cnf_bytes=exact_bytes, wall_seconds=perf_counter()-start,
                  wide_union_constraints=encoder.new_union_constraints,
                  sha256={role: digest(path) for role, path in files.items()})
    with receipt.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
