"""Two bounded D1 diagnostics using proved canonical necessary conditions.

No historical symmetry breakers are added. UNKNOWN is not an exclusion;
even RAW UNSAT would still require certificate and original-graph bridges.
Use --prepare-only to emit inputs without starting a solver.
"""
from pathlib import Path
import argparse
import importlib.util
import itertools
import json
import os
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = ROOT / "context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929"
OUT = ROOT / "computations/dd82/n62/d1_hard_diagnostic"
SOURCE = ROOT / "proofs/dd82/n62/d1_match_canonical_diagnostic_constraints_20261011.json"


def load_encoder():
    spec = importlib.util.spec_from_file_location("n62_ab_cnf", ARCHIVE / "code/n62/n62_ab_cnf.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (128 * 1024**2, 128 * 1024**2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    OUT.mkdir(exist_ok=True)
    module = load_encoder()
    manifest = module.load_manifest(ARCHIVE / "theory/n62/n62_root_templates.json")
    template = next(t for t in manifest["templates"] if t["id"] == "D1_MATCH")
    base = OUT / "cnf/D1_MATCH.cnf"
    if not base.exists():
        module.generate_case(template, OUT, write_cnf=True)
    encoder = module.ABEncoder(template, module.CNFEmitter(None))
    mapping = json.loads((OUT / "maps/D1_MATCH.map.json").read_text())
    # Initial variable allocation is deterministic and checked against the map.
    for key, actual in (("edge_variables", encoder.edge_vars),
                        ("b1_variables", encoder.b1_vars),
                        ("b2_variables", encoder.b2_vars)):
        assert {(u, v): v_id for u, v, v_id in mapping[key]} == actual
    base_units = {v: bool(value) for v, value, _ in mapping["unit_assignments"]}
    data = json.loads(SOURCE.read_text())
    classes = {int(k): v for k, v in data["canonical_classes"].items()}
    reports = []
    for case in data["cases"]:
        if case["status"] != "NECESSARY_CONSTRAINTS_ONLY":
            continue
        units, clauses = {}, []

        def unit(var, value):
            value = bool(value)
            assert var not in base_units or base_units[var] == value, (var, "base conflict")
            assert var not in units or units[var] == value, (var, "added conflict")
            units[var] = value

        def a(u, v, value):
            if u == v:
                assert value == 0
                return
            fixed = encoder.fixed_A(u, v)
            if fixed is not None:
                assert fixed == value, ("A", u, v, fixed, value)
            else:
                unit(encoder.edge_vars[module.pair(u, v)], value)

        def b(u, v, value):
            if u == v:
                assert value == 0
                return
            pair = module.pair(u, v)
            if pair in encoder.fixed_B_values:
                assert encoder.fixed_B_values[pair] == value, ("B", u, v, value)
            else:
                unit(encoder.b1_vars[pair], value == 1)
                unit(encoder.b2_vars[pair], value == 2)

        def exactly_one(variables):
            assert variables
            clauses.append(list(variables))
            clauses.extend([-x, -y] for x, y in itertools.combinations(variables, 2))

        for u_text, neighbors in data["A_complete_rows"].items():
            u = int(u_text)
            for v in range(62):
                a(u, v, int(v in neighbors))
        for u, v, value in case["A_fixed_entries"]:
            a(u, v, value)
        for intersection in case["A_row_16_exact_intersections"]:
            for v in intersection["set"]:
                a(16, v, int(v in intersection["neighbors"]))
        for label, count in data["A_row_16_class_counts"].items():
            vertices = [v for v in classes[int(label)] if v != 16]
            if count == 0:
                for v in vertices:
                    a(16, v, 0)
            else:
                assert count == 1
                exactly_one([encoder.edge_vars[module.pair(16, v)] for v in vertices])
        for u_text, values in case["B_complete_rows"].items():
            u = int(u_text)
            for v in range(62):
                b(u, v, values.get(str(v), 0))
        for u in (4, 16):
            partial = case[f"B_row_{u}"]
            fixed = {int(v): val for v, val in partial["fixed"].items()}
            groups = partial["unit_endpoint_groups"]
            allowed = set().union(*map(set, groups))
            for v in range(62):
                if v in fixed:
                    b(u, v, fixed[v])
                elif v not in allowed:
                    b(u, v, 0)
                else:
                    unit(encoder.b2_vars[module.pair(u, v)], False)
            for group in groups:
                exactly_one([encoder.b1_vars[module.pair(u, v)] for v in group])

        # Proved structural zero entries from the hard-D1 and C4 papers.
        for u in classes[1]:
            for v in range(62):
                if v not in classes[2] + classes[3] + classes[4]:
                    b(u, v, 0)
        for u, v in itertools.combinations(classes[2], 2):
            b(u, v, 0)
        for u in classes[3]:
            for v in classes[4]:
                b(u, v, 0)
        for label in (1, 2, 3, 4):
            for u, v in itertools.combinations(classes[label], 2):
                a(u, v, 0)
        # Only distinguished vertices known to be triangle-free are set here.
        for v in {0, 1, 2, 3, 4, 9, 10, 16, 22, 29, case["b"], 35}:
            unit(encoder.tau_vars[v], False)

        name = case["id"]
        target = OUT / f"{name}.cnf"
        with base.open() as source, target.open("w") as dest:
            for line in source:
                if line.startswith("p cnf "):
                    _, _, nv, nc = line.split()
                    dest.write(f"p cnf {nv} {int(nc) + len(units) + len(clauses)}\n")
                else:
                    dest.write(line)
            for var, value in sorted(units.items()):
                dest.write(f"{var if value else -var} 0\n")
            for clause in clauses:
                dest.write(" ".join(map(str, clause)) + " 0\n")
        (OUT / f"{name}.constraints.json").write_text(json.dumps({
            "case": name, "b": case["b"],
            "source": str(SOURCE.relative_to(ROOT)),
            "literals": [v if value else -v for v, value in sorted(units.items())],
            "extra_clauses": clauses,
            "unit_count": len(units), "extra_clause_count": len(clauses),
            "scope": "canonical necessary conditions; no complete exclusion claim"
        }, indent=2) + "\n")
        if args.prepare_only:
            print(json.dumps({"case": name, "prepared": True,
                              "units": len(units), "extra_clauses": len(clauses)}), flush=True)
            continue
        proof = OUT / f"{name}.lrat"
        cmd = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"),
               "--lrat", "-t", "10", str(target), str(proof)]
        start = time.monotonic()
        with (OUT / f"{name}.log").open("w") as log:
            try:
                process = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT,
                                         timeout=25, preexec_fn=limits)
                code = process.returncode
                status = {10: "SAT_CANDIDATE", 20: "RAW_UNSAT_WITH_UNCHECKED_LRAT",
                          0: "UNKNOWN"}.get(code, "PROCESS_FAILURE")
            except subprocess.TimeoutExpired:
                code, status = None, "OUTER_WALL_TIMEOUT"
        report = dict(case=name, status=status, exit_code=code,
                      seconds=time.monotonic() - start, cpu_count=1, cold_start=True,
                      solver_seconds_budget=10, unit_count=len(units),
                      extra_clause_count=len(clauses),
                      proof_bytes=proof.stat().st_size if proof.exists() else 0,
                      proof_checked=False, lean_graph_bridge=False, command=cmd)
        reports.append(report)
        (OUT / "results.json").write_text(json.dumps(reports, indent=2) + "\n")
        print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
