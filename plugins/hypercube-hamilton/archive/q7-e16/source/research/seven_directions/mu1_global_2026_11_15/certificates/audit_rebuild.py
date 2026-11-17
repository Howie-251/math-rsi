"""Rebuild only the two frozen models and compare PB/CNF without solving."""

import argparse
from collections import Counter
from hashlib import file_digest, sha256
import json
from pathlib import Path

import edge_cnf
from EDGE_HIGH_GAP_PROBE import build as build_physical
from google.protobuf import text_format
from ortools.sat import cp_model_pb2


HERE = Path(__file__).resolve().parent
SOURCE_HASHES = {
    "compiler": "f5b169f4a72935e47447b3e07960fda6d83027631e8c71144322496022f7459e",
    "physical_model": "c9fc0bd6ab0eb51cdea7e635ae445afdcd36e3321147e5ccddc54d7652ded9e4",
    "low_gap": "2a2725b2e22712d4ec1cd94cfbe36e13e3def79d6595fd0fd21c6770c85c8364",
    "prior_menu": "b6547a3f18d663cb97a2ea6215963e9fc465e14db204e299da045fe9bc692d32",
    "original": "ea9544b66e4dd85e4fd0117d94060768333c4c7be472fbc830afb8925bd1efdd",
    "even_compiler": "ddd6c61b2c73e32a33d37604cc3b6482898ba5f4484c059412cf251fd756e944",
    "odd_compiler": "7e5d68afc45e193314edb70ed590bcdfc08ec6c604d66cd66d5fe11bba53942f",
}
SOURCE_PATHS = {
    "compiler": HERE / "edge_cnf.py",
    "physical_model": HERE.parent / "EDGE_HIGH_GAP_PROBE.py",
    "low_gap": HERE.parent / "EDGE_LOW_GAP_PROBE.py",
    "prior_menu": HERE.parent / "EDGE_MENU_PROBE.py",
    "original": HERE.parent / "EDGE_PROBE.py",
    "even_compiler": edge_cnf.MU3_TOOLS / "even_cnf.py",
    "odd_compiler": edge_cnf.MU3_TOOLS / "odd_cnf.py",
}


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def read_json(path):
    return json.loads(path.read_bytes())


def audit_build(a):
    stem = f"edge_a{a}"
    audited = {role: digest(path) for role, path in SOURCE_PATHS.items()}
    assert audited == SOURCE_HASHES
    metadata_path = HERE / f"{stem}.build.json"
    metadata = read_json(metadata_path)
    assert metadata["status"] == "CNF_BUILT" and metadata["a"] == a
    assert all(metadata["sha256"][role] == h for role, h in audited.items())
    model, holes, build_stats = build_physical(a)
    assert len(holes) == 128 and model.validate() == ""
    fresh = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    names = [field.name for field, _ in fresh.ListFields()]
    assert sorted(names) == ["constraints", "variables"]
    assert json.loads(json.dumps(build_stats)) == metadata["gate_stats"]

    p = HERE / f"{stem}.pb"
    pb_bytes = p.read_bytes()
    native = cp_model_pb2.CpModelProto()
    # Check the independent C++ model-helper export route as well.
    tmp_name = f"audit_{stem}_native_rebuild.pb"
    tmp_path = HERE / tmp_name
    assert Path.cwd().resolve() == HERE and not tmp_path.exists()
    try:
        assert model.export_to_file(tmp_name)
        native.ParseFromString(tmp_path.read_bytes())
        assert native == fresh
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    assert fresh.SerializeToString(deterministic=True) == pb_bytes

    cnf = HERE / f"{stem}.cnf"
    encoded = edge_cnf.encode(fresh)
    with cnf.open("rb") as stream:
        assert stream.readline() == f"p cnf {encoded.num_vars} {len(encoded.clauses)}\n".encode("ascii")
        for i, clause in enumerate(encoded.clauses, 1):
            regenerated = (" ".join(map(str, (*clause, 0))) + "\n").encode("ascii")
            assert stream.readline() == regenerated, i
        assert stream.read(1) == b""
    mapping = HERE / f"{stem}.map.json"
    mapping_data = read_json(mapping)
    assert mapping_data["original_variables"] == [
        [v.name, *levels] for v, levels in zip(fresh.variables, encoded.thresholds)
    ]
    assert mapping_data["extra_equalities"] == [
        [i, value, literal] for (i, value), literal in encoded.equalities.items()
    ]
    output_hashes = {"pb": sha256(pb_bytes).hexdigest(), "cnf": digest(cnf), "map": digest(mapping)}
    assert all(metadata["sha256"][role] == h for role, h in output_hashes.items())
    assert encoded.num_vars == metadata["num_cnf_vars"]
    assert len(encoded.clauses) == metadata["num_cnf_clauses"]
    assert encoded.new_union_constraints == metadata["multirange_constraints"]
    assert cnf.stat().st_size == metadata["cnf_bytes"]

    kinds = Counter(c.WhichOneof("constraint") for c in fresh.constraints)
    domains = Counter(str(tuple(v.domain)) for v in fresh.variables)
    record = {
        "a": a,
        "verdict": "PASS",
        "scope": "Fresh CP source reconstruction; native PB and exact DIMACS comparison; no solving.",
        "source_variables": len(fresh.variables),
        "source_constraints": len(fresh.constraints),
        "constraint_types": kinds,
        "variable_domains": domains,
        "wide_multirange_constraints": encoded.new_union_constraints,
        "cnf_variables": encoded.num_vars,
        "cnf_clauses": len(encoded.clauses),
        "cnf_bytes": cnf.stat().st_size,
        "source_sha256": audited,
        "output_sha256": output_hashes,
        "producer_build_receipt_sha256": digest(metadata_path),
        "independent_rebuild_script_sha256": digest(Path(__file__)),
    }
    path = HERE / f"audit_{stem}_rebuild.json"
    with path.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, indent=2)
        stream.write("\n")
    print(json.dumps(record), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", nargs="+", type=int, choices=(0, 1))
    for choice in parser.parse_args().a:
        audit_build(choice)
