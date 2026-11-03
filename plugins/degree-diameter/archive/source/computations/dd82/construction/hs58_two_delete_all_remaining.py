"""HS58 with two original deletions: all remaining addition counts together.

All old nonedges, all attachments, and all auxiliary edges are variables.
Exact degrees imply |H|=|A|+5; bounding |H| by 11..13 selects 6..8 additions.
Auxiliary degrees are ordered solely by independent new-vertex relabeling.
"""
from itertools import combinations
from pathlib import Path
import argparse
import importlib.util
import json
import os
import resource
import subprocess
import sys
import time

from hs_augmentation import ROOT, ARCHIVE, base, dump, verify

HERE = Path(__file__).resolve().parent
GEOMETRIES = {"adjacent": [(0, 1), (0, 4)], "cross": [(0, 1), (2, 3)], "no_cross": [(0, 1), (10, 11)]}


def prepare(geometry):
    out = HERE / "hs58_two_delete_all_remaining_run" / geometry
    out.mkdir(parents=True, exist_ok=True)
    assert not (out / "input.cnf").exists(), "No unchanged preparation"
    cpu, wall = time.process_time(), time.monotonic()
    original, ns = base()
    original = set(original)
    deleted = set(GEOMETRIES[geometry])
    assert deleted <= original
    retained = original - deleted
    fixed_neighbors = [set() for _ in range(58)]
    for x, y in retained:
        fixed_neighbors[x].add(y)
        fixed_neighbors[y].add(x)
    spec = importlib.util.spec_from_file_location("all_remaining_cardinality", ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(out / "input.cnf")
    added = {(x, y): em.new_var("old_addition") for x, y in combinations(range(50), 2)
             if (x, y) not in original}
    ports = [[em.new_var("old_new") for _ in range(8)] for _ in range(50)]
    hvars = {(a, b): em.new_var("new_new") for a, b in combinations(range(8), 2)}
    for x in range(50):
        incident = [q for e, q in added.items() if x in e]
        mod.enforce_exact(em, incident + ports[x], 8 - len(fixed_neighbors[x]), f"old_degree_{x}")
    for a in range(8):
        incident = [q for e, q in hvars.items() if a in e]
        mod.enforce_exact(em, [ports[x][a] for x in range(50)] + incident, 8, f"new_degree_{a}")
    hcount = mod.unary_thresholds(em, list(hvars.values()), 14, "auxiliary_edge_count")
    em.add_clause(hcount[10])
    em.add_clause(-hcount[13])
    hdegrees = [mod.unary_thresholds(em, [q for e, q in hvars.items() if a in e], 7,
                                    "auxiliary_degree") for a in range(8)]
    for a in range(7):
        for k in range(7):
            em.add_clause(-hdegrees[a+1][k], hdegrees[a][k])

    def edge(x, y):
        if x == y:
            return False
        if x > y:
            x, y = y, x
        if y < 50:
            return True if (x, y) in retained else added.get((x, y), False)
        if x < 50:
            return ports[x][y - 50]
        return hvars[x - 50, y - 50]

    ands = {}

    def conjunction(a, b):
        if a is False or b is False:
            return False
        if a is True:
            return b
        if b is True:
            return a
        key = tuple(sorted((a, b)))
        if key not in ands:
            q = em.new_var("two_edge_path")
            mod.add_iff_and(em, q, *key)
            ands[key] = q
        return ands[key]

    coverage = dict(old_old=0, old_new=0, new_new=0)
    fixed_count = 0
    for x, y in combinations(range(58), 2):
        if y in fixed_neighbors[x] or fixed_neighbors[x] & fixed_neighbors[y]:
            fixed_count += 1
            continue
        xy = edge(x, y)
        terms = set() if xy is False else {xy}
        for z in range(58):
            q = conjunction(edge(x, z), edge(z, y))
            if q is not False:
                assert q is not True
                terms.add(q)
        em.add_clause(*sorted(terms))
        coverage["old_old" if y < 50 else ("old_new" if x < 50 else "new_new")] += 1
    assert fixed_count + sum(coverage.values()) == 1653
    em.finish()
    report = dict(geometry=geometry, n=58, fixed_deletions=sorted(deleted),
        original_HS_edges=sorted(original),
        addition_variables=[[x, y, q] for (x, y), q in added.items()],
        attachment_variables=ports, auxiliary_edge_variables=[[a, b, q] for (a, b), q in hvars.items()],
        addition_count_range=[6, 8], auxiliary_edge_count_range=[11, 13],
        primary_variables=len(added) + 400 + 28,
        variables=em.variable_count, clauses=em.clause_count,
        conjunction_variables=len(ands), coverage_clauses=coverage,
        pairs_covered_by_fixed_old_edges=fixed_count,
        old_vertex_normalization=[], attachment_normalization=[],
        new_vertex_normalization="Nonincreasing H degrees. Any candidate admits this by independently permuting all eight new labels; every attachment column remains free.",
        scope="Every HS58 target with this fixed deletion pair and six, seven, or eight original nonedge additions; all additions, ports, and auxiliary edges are free. The pure two-deletion spectral bound and previous a<=5 exclusion cover counts outside this interval.",
        encoding_cpu_seconds=time.process_time()-cpu,
        encoding_wall_seconds=time.monotonic()-wall)
    dump(out / "encoding.json", report)
    print(json.dumps({k: report[k] for k in ["geometry", "variables", "clauses", "primary_variables", "conjunction_variables", "coverage_clauses", "pairs_covered_by_fixed_old_edges", "encoding_cpu_seconds", "encoding_wall_seconds"]}), flush=True)


def solve(geometry):
    out = HERE / "hs58_two_delete_all_remaining_run" / geometry
    assert not (out / "result.json").exists(), "One solve, no unchanged rerun"
    enc = json.loads((out / "encoding.json").read_text())
    budget = 180
    command = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"), "--lrat", "-t", str(budget),
               str(out / "input.cnf"), str(out / "proof.lrat")]

    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (budget, budget+1))
        resource.setrlimit(resource.RLIMIT_AS, (8*1024**3, 8*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE, (768*1024**2, 768*1024**2))

    wall = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with (out / "solver.log").open("w") as log:
        try:
            rc = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                timeout=budget+20, preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(geometry=geometry, status={10: "SAT_CANDIDATE", 20: "RAW_UNSAT", 0: "UNKNOWN",
        -9: "CPU_LIMIT", -24: "CPU_LIMIT", -25: "OUTPUT_LIMIT", None: "WALL_LIMIT"}.get(rc, "PROCESS_FAILURE"),
        exit_code=rc, command=command, cpu_budget_seconds=budget,
        cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-wall, proof_checked=False,
        attempt=1, retained_solver_state=False, variables=enc["variables"], clauses=enc["clauses"])
    if rc == 10:
        values = {abs(q): q > 0 for line in (out / "solver.log").read_text().splitlines()
                  if line.startswith("v ") for q in map(int, line.split()[1:]) if q}
        additions = [(x, y) for x, y, q in enc["addition_variables"] if values[q]]
        h = [(a, b) for a, b, q in enc["auxiliary_edge_variables"] if values[q]]
        b = [(x, 50+a) for x, row in enumerate(enc["attachment_variables"]) for a, q in enumerate(row) if values[q]]
        edges = sorted((set(map(tuple, enc["original_HS_edges"])) - set(map(tuple, enc["fixed_deletions"]))) | set(additions) | set(b) | {(50+a, 50+c) for a, c in h})
        path = out / "candidate.json"
        dump(path, dict(n=58, edges=edges, old_deletions=enc["fixed_deletions"], old_additions=additions,
                       auxiliary_edges=h, actual_addition_count=len(additions)))
        path.with_suffix(".edges").write_text("58 232\n"+"".join(f"{x} {y}\n" for x, y in edges))
        result["independent_graph_check"] = json.loads(verify(path))
    if rc == 20:
        check = [str(ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"), "--no-trim",
                 str(out / "input.cnf"), str(out / "proof.lrat")]
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        clock = time.monotonic()
        checked = subprocess.run(check, capture_output=True, text=True, timeout=120)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        (out / "certificate_check.log").write_text(checked.stdout+checked.stderr)
        valid = checked.returncode == 20 and "s VERIFIED" in checked.stdout.splitlines()
        result["certificate_check"] = dict(command=check, exit_code=checked.returncode, verified=valid,
            cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
            wall_seconds=time.monotonic()-clock)
        result["proof_checked"] = valid
        if valid:
            result["status"] = "CHECKED_UNSAT"
    dump(out / "result.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["prepare", "solve"])
    parser.add_argument("geometry", choices=sorted(GEOMETRIES))
    parser.add_argument("--cpu", type=int, default=None)
    args = parser.parse_args()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0)) if args.cpu is None else args.cpu})
    (prepare if args.phase == "prepare" else solve)(args.geometry)
