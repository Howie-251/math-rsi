"""Append only global triangle-freeness and d <= 9 to old canonical D1 CNFs.

Stages: --prepare-only; --profile (b=28, 5 seconds); --run (one 120-second
cold start for each case). Existing solver outputs are never overwritten.
The complete graph-to-CNF Lean bridge remains absent.
"""
from pathlib import Path
import argparse
import importlib.util
import itertools
import json
import os
import re
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
ARCHIVE = ROOT / "context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929"
OLD = ROOT / "computations/dd82/n62/d1_hard_diagnostic"
OUT = ROOT / "computations/dd82/n62/d1_connected_diagnostic"
CASES = ("D1_HARD_b_28", "D1_HARD_b_41")


def dump(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def load():
    spec = importlib.util.spec_from_file_location(
        "connected_archive_encoder", ARCHIVE / "code/n62/n62_ab_cnf.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    manifest = module.load_manifest(ARCHIVE / "theory/n62/n62_root_templates.json")
    template = next(t for t in manifest["templates"] if t["id"] == "D1_MATCH")
    encoder = module.ABEncoder(template, module.CNFEmitter(None))
    return module, template, encoder


def header(path):
    with path.open() as src:
        for line in src:
            if line.startswith("p cnf "):
                return tuple(map(int, line.split()[2:]))
    raise ValueError(f"No DIMACS header: {path}")


def prepare():
    start = time.monotonic()
    OUT.mkdir(exist_ok=True)
    if (OUT / "preparation.json").exists():
        return json.loads((OUT / "preparation.json").read_text())
    module, template, encoder = load()
    # Regenerate the full allocation and compare all maps, including tau and
    # template units. This is a count-only encoding, not a solver call.
    encoder.encode()
    mapping = json.loads((OLD / "maps/D1_MATCH.map.json").read_text())
    assert encoder.mapping() == mapping
    assert header(OLD / "cnf/D1_MATCH.cnf") == (
        encoder.emitter.variable_count, encoder.emitter.clause_count)
    pairs = set(itertools.combinations(range(62), 2))
    fixed = set(encoder.fixed_B_values)
    dynamic = set(encoder.b2_vars)
    assert not fixed & dynamic and fixed | dynamic == pairs
    fixed_doubles = [list(uv) for uv, value in sorted(encoder.fixed_B_values.items())
                     if value == 2]
    assert fixed_doubles == [[0, 9]]
    maximum_dynamic = 9 - len(fixed_doubles)
    inputs = [var for uv, var in sorted(encoder.b2_vars.items())]
    assert len(inputs) == len(set(inputs)) == 1802
    primitive_audit = module.audit_unary_threshold_encoder()
    reports = []
    for case in CASES:
        source = OLD / f"{case}.cnf"
        nv, nc = header(source)
        assert nv == encoder.emitter.variable_count
        old_constraints = json.loads((OLD / f"{case}.constraints.json").read_text())
        assert nc == encoder.emitter.clause_count + old_constraints["unit_count"] + old_constraints["extra_clause_count"]
        units = dict(encoder.unit_values)
        for literal in old_constraints["literals"]:
            assert abs(literal) not in units or units[abs(literal)] == (literal > 0)
            units[abs(literal)] = literal > 0
        tau_literals = [-encoder.tau_vars[u] for u in range(62)]
        assert all(units.get(-literal, False) is False for literal in tau_literals)
        target = OUT / f"{case}.cnf"
        added = OUT / f"{case}.added.cnf"
        assert not target.exists() and not added.exists()
        emitter = module.CNFEmitter(added)
        emitter.variable_count = nv
        for literal in tau_literals:
            emitter.add_clause(literal)
        thresholds = module.unary_thresholds(
            emitter, inputs, maximum_dynamic + 1, "global_double_pair_threshold")
        assert thresholds[maximum_dynamic] is not None
        emitter.add_clause(-thresholds[maximum_dynamic])
        emitter.finish()
        # Preserve every old clause and its order, updating just the header.
        old_clause_count = 0
        with source.open() as src, target.open("x") as dest:
            for line in src:
                if line.startswith("p cnf "):
                    dest.write(f"p cnf {emitter.variable_count} {nc + emitter.clause_count}\n")
                else:
                    dest.write(line)
                    if line.strip() and not line.startswith("c"):
                        assert line.rstrip().endswith(" 0") or line.strip() == "0"
                        old_clause_count += 1
            with added.open() as extra:
                for line in extra:
                    if not line.startswith("p cnf "):
                        dest.write(line)
        assert old_clause_count == nc
        report = dict(case=case, source=str(source.relative_to(ROOT)),
            old_variables=nv, old_clauses=nc,
            variables=emitter.variable_count, clauses=nc + emitter.clause_count,
            added_variables=emitter.variable_count-nv, added_clauses=emitter.clause_count,
            tau_negative_literals=tau_literals,
            tau_units_already_present=sum(-x in units for x in tau_literals),
            fixed_double_pairs=fixed_doubles, dynamic_b2_selector_count=len(inputs),
            dynamic_b2_at_most=maximum_dynamic, threshold_false=thresholds[maximum_dynamic],
            dynamic_b2_inputs=inputs,
            auxiliary_range=[nv+1, emitter.variable_count],
            dynamic_b2_already_fixed_true=[var for var in inputs if units.get(var) is True],
            dynamic_b2_already_fixed_false_count=sum(units.get(var) is False for var in inputs),
            added_clause_file=str(added.relative_to(ROOT)))
        dump(OUT / f"{case}.constraints.json", report)
        reports.append({k: v for k, v in report.items() if k not in ("dynamic_b2_inputs", "tau_negative_literals")})
    report = dict(status="PREPARED", seconds=time.monotonic()-start,
        pinned_cpu=next(iter(os.sched_getaffinity(0))),
        mapping_equal_to_full_encoder=True, fixed_pair_count=len(fixed),
        dynamic_pair_count=len(dynamic), all_unordered_pairs=len(pairs),
        primitive_counter_audit=primitive_audit, cases=reports,
        new_conditions=["all actual triangle membership tau variables false", "total unordered actual B=2 pairs at most 9"],
        lean_graph_bridge=False)
    dump(OUT / "preparation.json", report)
    return report


def verify_sat(log, case):
    """Reconstruct adjacency directly and check graph properties by enumeration."""
    _, template, _ = load()
    mapping = json.loads((OLD / "maps/D1_MATCH.map.json").read_text())
    assignment = {}
    for line in log.read_text().splitlines():
        if line.startswith("v "):
            for literal in map(int, line.split()[1:]):
                if literal:
                    assignment[abs(literal)] = literal > 0
    A = [[0] * 62 for _ in range(62)]
    edges = {(0, x) for x in range(1, 9)}
    edges.update(tuple(sorted(edge)) for edge in template["H_edges"])
    edges.update((x, int(y)) for y, parents in template["parent_map"].items() for x in parents)
    edges.update((u, v) for u, v, var in mapping["edge_variables"] if assignment[var])
    for u, v in edges:
        A[u][v] = A[v][u] = 1
    neighbors = [{v for v in range(62) if A[u][v]} for u in range(62)]
    assert all(len(ns) == 8 for ns in neighbors)
    B = [[0]*62 for _ in range(62)]
    for u, v in itertools.combinations(range(62), 2):
        common = len(neighbors[u] & neighbors[v])
        assert A[u][v] or common > 0
        assert not A[u][v] or common == 0
        value = common + A[u][v] - 1
        assert value in (0, 1, 2)
        B[u][v] = B[v][u] = value
    assert all(sum(row) == 3 for row in B)
    doubles = [[u,v] for u,v in itertools.combinations(range(62),2) if B[u][v] == 2]
    assert len(doubles) <= 9
    for key, value in (("b1_variables",1), ("b2_variables",2)):
        assert all(assignment[var] == (B[u][v] == value) for u,v,var in mapping[key])
    assert all(not assignment[var] for u,var in mapping["tau_variables"])
    result = dict(status="INDEPENDENTLY_VERIFIED_ACTUAL_GRAPH", n=62,
                  degree=8, diameter_at_most=2, triangle_free=True,
                  double_pairs=doubles, adjacency=A, repeat_matrix=B)
    dump(OUT / f"{case}.verified_graph.json", result)
    return result["status"]


def run(case, seconds, stage):
    stem = OUT / f"{case}.{stage}"
    result_path = stem.with_suffix(stem.suffix + ".json")
    log = stem.with_suffix(stem.suffix + ".log")
    proof = stem.with_suffix(stem.suffix + ".lrat")
    assert not any(p.exists() for p in (result_path, log, proof)), "No retries/overwrites"
    cmd = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"), "--lrat",
           "-t", str(seconds), str(OUT / f"{case}.cnf"), str(proof)]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds+1))
        resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE, (512*1024**2, 512*1024**2))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with log.open("x") as stream:
        try:
            process = subprocess.run(cmd, stdout=stream, stderr=subprocess.STDOUT,
                timeout=seconds+5, preexec_fn=limits)
            code = process.returncode
            status = {10:"SAT_CANDIDATE", 20:"RAW_UNSAT_WITH_UNCHECKED_LRAT", 0:"UNKNOWN",
                      -24:"CPU_LIMIT", -25:"OUTPUT_FILE_LIMIT"}.get(code,"PROCESS_FAILURE")
        except subprocess.TimeoutExpired:
            code, status = None, "OUTER_WALL_TIMEOUT"
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(case=case, stage=stage, status=status, exit_code=code,
        wall_seconds=time.monotonic()-start,
        cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        solver_seconds_budget=seconds, outer_wall_limit_seconds=seconds+5,
        cpu_soft_limit_seconds=seconds, cpu_hard_limit_seconds=seconds+1,
        pinned_cpu=next(iter(os.sched_getaffinity(0))), cpu_count=1,
        memory_limit_bytes=4*1024**3, output_file_limit_bytes=512*1024**2,
        proof_bytes=proof.stat().st_size if proof.exists() else 0,
        proof_checked=False, lean_graph_bridge=False, cold_start=True,
        command=cmd)
    text = log.read_text()
    for field, pattern in (
        ("max_rss_mb", r"maximum resident set size of process:\s+([0-9.]+)"),
        ("conflicts", r"c conflicts:\s+(\d+)"),
        ("decisions", r"c decisions:\s+(\d+)")):
        match = re.search(pattern, text)
        if match:
            report[field] = float(match.group(1)) if field == "max_rss_mb" else int(match.group(1))
    if status == "SAT_CANDIDATE":
        report["graph_verification"] = verify_sat(log, case)
    if code == 20:
        # Local search found Lean's internal LRAT library, but no standalone
        # CLI checker. Preserve RAW status; an unchecked trace is no theorem.
        report["checker_availability"] = "No existing standalone LRAT checker found"
    dump(result_path, report)
    print(json.dumps(report), flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prepare-only", action="store_true")
    group.add_argument("--profile", action="store_true")
    group.add_argument("--run", action="store_true")
    args = parser.parse_args()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    report = prepare()
    if args.prepare_only:
        print(json.dumps(report), flush=True)
    elif args.profile:
        run(CASES[0], 5, "profile5")
    else:
        profile = json.loads((OUT / f"{CASES[0]}.profile5.json").read_text())
        assert profile["status"] in ("UNKNOWN", "CPU_LIMIT"), "Review decisive or failed profile before longer work"
        used_cpu = profile["cpu_seconds"]
        reports = []
        for case in CASES:
            # Leave half a second for the observed coarse OS CPU-limit signal.
            seconds = min(120, int(244.5-used_cpu))
            assert seconds > 0
            result = run(case, seconds, "bounded120")
            used_cpu += result["cpu_seconds"]
            reports.append(result)
            dump(OUT / "results.json", dict(profile=profile, bounded_runs=reports,
                total_cpu_seconds=used_cpu, total_solver_budget_seconds=5+sum(
                    r["solver_seconds_budget"] for r in reports)))


if __name__ == "__main__":
    main()
