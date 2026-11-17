"""Compile one joint CNF for the audited 23 large-face representatives."""

import json
import os
import sys
import tempfile
from collections import Counter
from pathlib import Path
from time import perf_counter

from google.protobuf import text_format
from ortools.sat import cp_model_pb2

HERE = Path(__file__).resolve().parent
DELTA2 = HERE.parent
CERT = DELTA2.parent / "certificates"
sys.path[:0] = [str(DELTA2), str(CERT)]

from edge_cnf import MAX_BYTES, digest, encode

for key in ("TMP", "TEMP", "TMPDIR"):
    os.environ[key] = str(HERE)
tempfile.tempdir = str(HERE)

from fixed_face_probe import build, read_basis


def source_proto():
    indices = tuple(range(len(read_basis())))
    assert indices == tuple(range(23))
    model, _, source_record = build(indices)
    proto = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    assert len(proto.variables) == len(model.proto.variables)
    assert len(proto.constraints) == len(model.proto.constraints)
    return proto, source_record


def build_cnf():
    start = perf_counter()
    stem = HERE / "a1_large_face_union"
    pb, cnf, mapping, receipt = (stem.with_suffix(suffix) for suffix in
                                  (".pb", ".cnf", ".map.json", ".build.json"))
    if any(path.exists() for path in (pb, cnf, mapping, receipt)):
        raise FileExistsError("The union model has already been built")
    proto, record = source_proto()
    print(f"Union PB: {len(proto.variables):,} variables / {len(proto.constraints):,} constraints", flush=True)
    enc = encode(proto)
    header = f"p cnf {enc.num_vars} {len(enc.clauses)}\n"
    total = len(header) + sum(2 + sum(len(str(lit)) + 1 for lit in clause) for clause in enc.clauses)
    if total > MAX_BYTES:
        raise ValueError(f"CNF preflight {total:,} bytes exceeds {MAX_BYTES:,}")
    pb.write_bytes(proto.SerializeToString(deterministic=True))
    with cnf.open("x", encoding="ascii", newline="\n") as stream:
        stream.write(header)
        for clause in enc.clauses:
            stream.write(" ".join(map(str, (*clause, 0))) + "\n")
    assert cnf.stat().st_size == total
    mapping.write_text(json.dumps({
        "threshold_meaning": "Each list is x>=1, x>=2, ... in source variable order.",
        "original_variables": [[v.name, *enc.thresholds[i]] for i, v in enumerate(proto.variables)],
        "extra_equalities": [[i, value, lit] for (i, value), lit in enc.equalities.items()],
    }, separators=(",", ":")) + "\n", encoding="utf-8")
    paths = {
        "pb": pb, "cnf": cnf, "map": mapping, "driver": Path(__file__),
        "compiler": CERT / "edge_cnf.py",
        "fixed_face_model": DELTA2 / "fixed_face_probe.py",
        "delta2_coverage_helper": DELTA2 / "probe.py",
    }
    result = dict(status="CNF_BUILT", source=record,
                  source_variables=len(proto.variables), source_constraints=len(proto.constraints),
                  constraint_types=Counter(row.WhichOneof("constraint") for row in proto.constraints),
                  wide_union_constraints=enc.new_union_constraints,
                  cnf_variables=enc.num_vars, cnf_clauses=len(enc.clauses), cnf_bytes=total,
                  wall_seconds=perf_counter()-start,
                  sha256={key: digest(path) for key, path in paths.items()})
    receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print({key: value for key, value in result.items() if key != "source"}, flush=True)


if __name__ == "__main__":
    build_cnf()
