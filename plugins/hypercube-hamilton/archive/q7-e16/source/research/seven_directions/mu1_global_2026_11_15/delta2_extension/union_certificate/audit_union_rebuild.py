"""Regenerate the frozen 23-branch union PB and DIMACS without solving."""

from collections import Counter
from hashlib import file_digest
import json
from pathlib import Path

from google.protobuf import text_format
from ortools.sat import cp_model_pb2

import build_union
import edge_cnf
import fixed_face_probe


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "pb": "7777048fc33fba6884e5e511c58bae9f27f9ed4b822406843521d1809e652926",
    "cnf": "9b5e81061611d53223349d4a338a155661a4092a28009129eeb20f1f52f2e0f1",
    "map": "2d520be51aad329b65c23d16bb001900dd5f25eea4aecbeb0bd811f5871bd157",
    "driver": "0d16a9b4df66054f45dc729817e2372cf7c462a7c63aaf69dcd2c3d471922783",
    "compiler": "f5b169f4a72935e47447b3e07960fda6d83027631e8c71144322496022f7459e",
    "fixed_face_model": "de25c43af33834243296aea1deee8cdaba4f188b4007f2d967613dd1c5c58bd6",
    "delta2_coverage_helper": "204bfb299883bef7be32ac3844a42a673f54be24a210df75c30d105fcb9f5de0",
}


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def main():
    basename = HERE / "a1_large_face_union"
    pb, cnf, mapping, receipt_path = (basename.with_suffix(s) for s in (".pb", ".cnf", ".map.json", ".build.json"))
    artifacts = {
        "pb": pb, "cnf": cnf, "map": mapping,
        "driver": HERE / "build_union.py", "compiler": Path(edge_cnf.__file__),
        "fixed_face_model": Path(fixed_face_probe.__file__),
        "delta2_coverage_helper": HERE.parent / "probe.py",
    }
    digests = {role: digest(file) for role, file in artifacts.items()}
    assert digests == EXPECTED
    receipt = read(receipt_path)
    assert receipt["status"] == "CNF_BUILT" and receipt["sha256"] == EXPECTED
    source_audit_path = HERE.parent / "STRUCTURE_FIXED_B_REVIEW_check.json"
    source_audit = read(source_audit_path)
    assert source_audit["verdict"] == "PASS"
    assert source_audit["sha256"]["fixed_face_probe.py"] == EXPECTED["fixed_face_model"]
    assert source_audit["sha256"]["probe.py"] == EXPECTED["delta2_coverage_helper"]

    model, holes, info = fixed_face_probe.build(tuple(range(23)))
    assert len(holes) == 128 and model.validate() == ""
    assert json.loads(json.dumps(info)) == receipt["source"]
    proto = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    assert sorted(field.name for field, _ in proto.ListFields()) == ["constraints", "variables"]
    assert len(proto.variables) == 29416 and len(proto.constraints) == 100033
    assert proto.SerializeToString(deterministic=True) == pb.read_bytes()
    native_file = HERE / "audit_union_native_rebuild.pb"
    assert Path.cwd().resolve() == HERE and not native_file.exists()
    try:
        assert model.export_to_file(native_file.name)
        assert cp_model_pb2.CpModelProto.FromString(native_file.read_bytes()) == proto
    finally:
        if native_file.exists():
            native_file.unlink()

    enc = edge_cnf.encode(proto)
    with cnf.open("rb") as stream:
        assert stream.readline() == f"p cnf {enc.num_vars} {len(enc.clauses)}\n".encode("ascii")
        for number, clause in enumerate(enc.clauses, 1):
            line = (" ".join(map(str, (*clause, 0))) + "\n").encode("ascii")
            assert stream.readline() == line, number
        assert stream.read(1) == b""
    map_data = read(mapping)
    assert map_data["original_variables"] == [[v.name, *enc.thresholds[i]] for i, v in enumerate(proto.variables)]
    assert map_data["extra_equalities"] == [
        [i, value, literal] for (i, value), literal in enc.equalities.items()
    ]
    assert (enc.num_vars, len(enc.clauses)) == (receipt["cnf_variables"], receipt["cnf_clauses"])
    assert enc.new_union_constraints == receipt["wide_union_constraints"]
    assert cnf.stat().st_size == receipt["cnf_bytes"]
    classifications = Counter(c.WhichOneof("constraint") for c in proto.constraints)
    assert classifications == receipt["constraint_types"]
    result = {
        "verdict": "PASS",
        "scope": "Fresh audited fixed-face model build; native CP export, canonical PB, complete DIMACS and variable-map comparison. No solving.",
        "source_constraints": len(proto.constraints),
        "source_variables": len(proto.variables),
        "constraint_types": classifications,
        "cnf_variables": enc.num_vars,
        "cnf_clauses": len(enc.clauses),
        "sha256": digests,
        "build_receipt_sha256": digest(receipt_path),
        "fixed_face_source_audit_sha256": digest(source_audit_path),
        "independent_script_sha256": digest(Path(__file__)),
    }
    with (HERE / "audit_union_rebuild.json").open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()

