"""Compile each frozen physical E16 edge model to DIMACS, without CP solving."""

import argparse
import json
import os
import sys
import tempfile
from collections import Counter
from hashlib import file_digest
from itertools import product
from pathlib import Path
from time import perf_counter
from unittest.mock import patch

from google.protobuf import text_format
from ortools.sat import cp_model_pb2

HERE = Path(__file__).resolve().parent
MU1 = HERE.parent
MU3_TOOLS = MU1.parent / "mu3_hard_first_2026_11_15" / "PROOF_TOOLS"
sys.path[:0] = [str(MU1), str(MU3_TOOLS)]

import odd_cnf

# The imported compiler sets its own scratch directory during import.
for name in ("TMP", "TEMP", "TMPDIR"):
    os.environ[name] = str(HERE)
tempfile.tempdir = str(HERE)

from EDGE_HIGH_GAP_PROBE import build as build_physical_model

MAX_CLAUSES = 5_000_000
MAX_BYTES = 500_000_000


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


class EdgeEncoder(odd_cnf.OddEncoder):
    def __init__(self, domains):
        self.new_union_constraints = 0
        super().__init__(tuple((0, 1) if domain == (1, 1) else domain for domain in domains))
        self.original_domains = domains
        for index, domain in enumerate(domains):
            if domain == (1, 1):
                self.add((self.cp_bool(index),))

    def add(self, literals, guards=()):
        super().add(literals, guards)
        if len(self.clauses) > MAX_CLAUSES:
            raise ValueError(f"CNF clause preflight exceeds {MAX_CLAUSES:,}")

    def linear(self, variables, coeffs, domain, guards):
        if len(variables) <= 6 or len(domain) <= 2:
            return super().linear(variables, coeffs, domain, guards)
        if (
            len(domain) % 2 or len(variables) != len(coeffs)
            or any(self.domains[i] != (0, 1) for i in variables)
            or set(coeffs) - {-1, 1}
        ):
            raise ValueError("unsupported wide multirange linear constraint")
        intervals = tuple(zip(domain[::2], domain[1::2]))
        if any(low > high for low, high in intervals):
            raise ValueError("invalid interval endpoints")

        # With all original guards true, at least one interval must be selected.
        # A selected interval enforces its bounds under those same original guards.
        # Any valid CP value lies in some interval and can choose its selector.
        self.new_union_constraints += 1
        choices = [self.new_var() for _ in intervals]
        self.add(choices, guards)
        for choice, interval in zip(choices, intervals):
            super().linear(variables, coeffs, interval, (*guards, choice))


def encode(proto):
    # Keep the audited constraint dispatcher and every inherited encoding rule.
    with patch.object(odd_cnf, "OddEncoder", EdgeEncoder):
        return odd_cnf.encode(proto)


def truth_table():
    from pysat.solvers import Minisat22

    tests = 0
    domains = ((0, 1),) * 10
    examples = (
        ((1,) * 8, (-8, -2, 3, 8)),
        ((1,) * 4 + (-1,) * 4, (-8, -2, 3, 8)),
        ((1, -1) * 4, (-4, -4, -1, 0, 2, 2)),
        ((-1,) * 8, (-2, -1, 4, 8)),
        ((1,) * 8, (-20, -10, 10, 20)),
    )
    for signed, domain in examples:
        intervals = tuple(zip(domain[::2], domain[1::2]))
        encoder = EdgeEncoder(domains)
        encoder.linear(list(range(8)), signed, domain,
                       (encoder.cp_bool(8), encoder.cp_bool(-10)))
        assert encoder.new_union_constraints == 1
        with Minisat22(bootstrap_with=encoder.clauses) as solver:
            for row in product((0, 1), repeat=len(domains)):
                amount = sum(c * x for c, x in zip(signed, row))
                expected = not (row[8] and not row[9]) or any(
                    low <= amount <= high for low, high in intervals
                )
                assumptions = [encoder.cp_bool(i if x else -1 - i) for i, x in enumerate(row)]
                assert solver.solve(assumptions=assumptions) == expected, (signed, domain, row)
                tests += 1
    encoder = EdgeEncoder(((0, 0), (1, 1)))
    with Minisat22(bootstrap_with=encoder.clauses) as solver:
        for zero, one in product((0, 1), repeat=2):
            assumptions = (encoder.cp_bool(0 if zero else -1),
                           encoder.cp_bool(1 if one else -2))
            assert solver.solve(assumptions=assumptions) == (not zero and bool(one))
            tests += 1
    return tests


def source_proto(a):
    model, _, stats = build_physical_model(a)
    proto = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    if len(proto.variables) != len(model.proto.variables) or len(proto.constraints) != len(model.proto.constraints):
        raise ValueError("model text round trip changed dimensions")
    return proto, stats


def build(a):
    start = perf_counter()
    stem = f"edge_a{a}"
    target = HERE / stem
    pb_path = target.with_suffix(".pb")
    cnf_path = target.with_suffix(".cnf")
    map_path = target.with_suffix(".map.json")
    receipt_path = target.with_suffix(".build.json")
    if any(path.exists() for path in (pb_path, cnf_path, map_path, receipt_path)):
        raise FileExistsError(f"existing build artifacts for {stem}")

    proto, gate_stats = source_proto(a)
    print(f"{stem}: {len(proto.variables):,} source variables, {len(proto.constraints):,} constraints", flush=True)
    enc = encode(proto)
    counts = len(enc.clauses)
    header = f"p cnf {enc.num_vars} {counts}\n"
    exact_dimacs_bytes = len(header) + sum(
        2 + sum(len(str(literal)) + 1 for literal in clause) for clause in enc.clauses
    )
    print(f"{stem}: {enc.num_vars:,} variables, {counts:,} clauses, {exact_dimacs_bytes:,} bytes", flush=True)
    if exact_dimacs_bytes > MAX_BYTES:
        raise ValueError(f"CNF byte preflight exceeds {MAX_BYTES:,}")

    pb_path.write_bytes(proto.SerializeToString(deterministic=True))
    with cnf_path.open("x", encoding="ascii", newline="\n") as stream:
        stream.write(header)
        for clause in enc.clauses:
            stream.write(" ".join(map(str, (*clause, 0))) + "\n")
    assert cnf_path.stat().st_size == exact_dimacs_bytes
    map_path.write_text(json.dumps({
        "threshold_meaning": "Each list is x>=1, x>=2, ... in source variable order.",
        "original_variables": [[v.name, *enc.thresholds[i]] for i, v in enumerate(proto.variables)],
        "extra_equalities": [[index, value, lit] for (index, value), lit in enc.equalities.items()],
    }, separators=(",", ":")) + "\n", encoding="utf-8")

    files = {
        "pb": pb_path, "cnf": cnf_path, "map": map_path, "compiler": Path(__file__),
        "physical_model": MU1 / "EDGE_HIGH_GAP_PROBE.py",
        "low_gap": MU1 / "EDGE_LOW_GAP_PROBE.py", "prior_menu": MU1 / "EDGE_MENU_PROBE.py",
        "original": MU1 / "EDGE_PROBE.py", "even_compiler": MU3_TOOLS / "even_cnf.py",
        "odd_compiler": MU3_TOOLS / "odd_cnf.py",
    }
    result = {
        "status": "CNF_BUILT", "a": a, "wall_seconds": perf_counter() - start,
        "source_variables": len(proto.variables), "source_constraints": len(proto.constraints),
        "constraint_types": Counter(c.WhichOneof("constraint") for c in proto.constraints),
        "gate_stats": gate_stats, "multirange_constraints": enc.new_union_constraints,
        "num_cnf_vars": enc.num_vars, "num_cnf_clauses": counts, "cnf_bytes": exact_dimacs_bytes,
        "sha256": {role: digest(path) for role, path in files.items()},
    }
    receipt_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("test", "build"))
    parser.add_argument("a", nargs="?", type=int, choices=(0, 1))
    args = parser.parse_args()
    if args.mode == "test":
        assert args.a is None
        print(f"PASS {truth_table():,} guarded multirange truth-table assignments")
    else:
        assert args.a is not None
        build(args.a)


if __name__ == "__main__":
    main()
