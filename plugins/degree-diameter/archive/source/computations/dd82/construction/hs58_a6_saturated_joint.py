"""One joint completion of all 56 saturated no-cross a6 old cores.

All 400 old-new incidences and all 28 auxiliary edges remain variable.
Only auxiliary degree sorting breaks new-label symmetry. No palette or
additional obstruction clauses are used. Prepare and solve are separate
so the exact input statistics can be reported before the sole solver run.
"""
from collections import Counter
from itertools import combinations, permutations, product
import argparse
import importlib.util
import json
import os
import resource
import subprocess
import sys
import time

from hs_augmentation import ROOT, ARCHIVE, base, dump, verify

OUT = ROOT / "computations/dd82/construction/hs58_a6_saturated_joint_run"
D = {(0, 1), (10, 11)}
P = {0, 1, 10, 11}
SECONDS = 180


def addition_domain(original, qn):
    halves = [([4, 36, 45, 46], [39, 12, 48, 49]),
              ([2, 30, 31, 40], [32, 33, 14, 42])]
    cells = {0: {4, 30, 40, 45}, 1: {2, 31, 36, 46},
             10: {14, 32, 39, 48}, 11: {12, 33, 42, 49}}
    forced = [(25, 26), (35, 41)]
    records = []
    for h0, h1 in product(range(2), repeat=2):
        selected = set(halves[0][h0]) | set(halves[1][h1])
        left0, right0 = sorted(selected & cells[0]), sorted(selected & cells[1])
        left1, right1 = sorted(selected & cells[10]), sorted(selected & cells[11])
        for order0, order1 in product(permutations(right0), permutations(right1)):
            additions = sorted(tuple(sorted(e)) for e in
                               forced + list(zip(left0, order0)) + list(zip(left1, order1)))
            records.append(dict(id=len(records), halves=[h0, h1], additions=additions,
                                zeros=sorted({v for e in additions for v in e})))

    # Independent property/count check, using actual Q-neighborhoods rather
    # than the generator's matching construction. Each permitted bijection
    # is represented once because uniqueness attains its factorial count.
    tau = {0: 1, 1: 0, 10: 11, 11: 10}
    canonical = {tuple(map(tuple, rec["additions"])) for rec in records}
    assert len(records) == len(canonical) == 56
    counts = Counter()
    zero_sets = set()
    for rec in records:
        A, Z = rec["additions"], set(rec["zeros"])
        assert len(A) == 6 and len(Z) == 12 and not (Z & P)
        assert all(tuple(e) not in original for e in A)
        assert all(not (qn[z] & Z) for z in Z)
        assert {25, 26, 35, 41} <= Z
        for q, partner in A:
            assert qn[q] & P
            assert qn[partner] & P == {tau[x] for x in qn[q] & P}
        choices = []
        for pair in halves:
            selected_half = [i for i, half in enumerate(pair) if set(half) <= Z]
            assert len(selected_half) == 1
            choices.extend(selected_half)
        assert len(Z - {25, 26, 35, 41}) == 8
        counts[tuple(choices)] += 1
        zero_sets.add(tuple(sorted(Z)))
    assert len(zero_sets) == 4
    assert counts == {(0, 0): 24, (0, 1): 4, (1, 0): 4, (1, 1): 24}
    dump(OUT / "addition_domain.json", dict(
        fixed_deletions=sorted(D), templates=records, distinct_templates=56,
        distinct_zero_sets=4,
        counts_by_halves={f"{a},{b}": n for (a, b), n in sorted(counts.items())},
        independent_properties_checked=["six-edge matching", "original nonedges",
            "D endpoint avoidance", "independent twelve-vertex zero set",
            "actual-Q tau-opposite cells", "distinctness and complete factorial counts"]))
    return records


def prepare():
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "input.cnf").exists(), "Do not replace an existing input"
    start_cpu, start_wall = time.process_time(), time.monotonic()
    original, qn = base()
    original = set(original)
    assert D <= original
    assert not any(y in qn[x] for x in (0, 1) for y in (10, 11))
    retained = original - D
    records = addition_domain(original, qn)
    spec = importlib.util.spec_from_file_location("hs58_a6_joint_cardinality", ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(OUT / "input.cnf")
    selectors = [em.new_var("old_core_selector") for _ in records]
    eligible = sorted({tuple(e) for rec in records for e in rec["additions"]})
    A = {e: em.new_var("selected_addition") for e in eligible}
    B = [[em.new_var("attachment") for _ in range(8)] for _ in range(50)]
    H = {e: em.new_var("auxiliary_edge") for e in combinations(range(8), 2)}
    mod.enforce_exact(em, selectors, 1, "one_old_core")
    for e, avar in A.items():
        supporting = [selectors[i] for i, rec in enumerate(records) if e in map(tuple, rec["additions"])]
        em.add_clause(-avar, *supporting)
        for selector in supporting:
            em.add_clause(-selector, avar)

    def edge(x, y):
        if x == y:
            return False
        x, y = min(x, y), max(x, y)
        if y < 50:
            return True if (x, y) in retained else A.get((x, y), False)
        if x < 50:
            return B[x][y-50]
        return H[x-50, y-50]

    for x in range(50):
        add_incident = [v for e, v in A.items() if x in e]
        retained_degree = len(qn[x]) - sum(x in e for e in D)
        mod.enforce_exact(em, add_incident+B[x], 8-retained_degree, f"old_degree_{x}")
    for a in range(8):
        incident_h = [v for e, v in H.items() if a in e]
        mod.enforce_exact(em, [B[x][a] for x in range(50)]+incident_h, 8, f"new_degree_{a}")
    # New labels may always be permuted to nonincreasing auxiliary degrees.
    degrees = [mod.unary_thresholds(em, [v for e, v in H.items() if a in e],
                                   7, f"aux_degree_{a}") for a in range(8)]
    for a in range(7):
        for k in range(7):
            em.add_clause(-degrees[a+1][k], degrees[a][k])

    and_cache = {}

    def conjunction(a, b):
        if a is False or b is False:
            return False
        if a is True:
            return b
        if b is True:
            return a
        pair = tuple(sorted((a, b)))
        if pair not in and_cache:
            out = em.new_var("two_step_path")
            mod.add_iff_and(em, out, *pair)
            and_cache[pair] = out
        return and_cache[pair]

    coverage = Counter()
    fixed_covered = []
    for x, y in combinations(range(58), 2):
        direct = edge(x, y)
        if direct is True or any(edge(x, z) is True and edge(z, y) is True for z in range(58)):
            fixed_covered.append([x, y])
            continue
        terms = [] if direct is False else [direct]
        for z in range(58):
            term = conjunction(edge(x, z), edge(z, y))
            if term is not False:
                assert term is not True
                terms.append(term)
        em.add_clause(*terms)
        kind = "old_old" if y < 50 else ("old_new" if x < 50 else "new_new")
        coverage[kind] += 1
    assert len(fixed_covered) + sum(coverage.values()) == 1653
    em.finish()
    record = dict(n=58, HS_edges=sorted(original), fixed_deletions=sorted(D),
        selectors=selectors, addition_variables={f"{x},{y}": v for (x,y),v in A.items()},
        attachment_variables=B, auxiliary_variables={f"{a},{b}": v for (a,b),v in H.items()},
        old_core_templates=56, old_additions=6, auxiliary_edges_implied=11,
        primary_variable_counts=dict(selectors=56, addition_indicators=len(A), attachments=400, auxiliary_edges=28),
        variables=em.variable_count, clauses=em.clause_count, variable_kind_counts=em.kind_counts,
        coverage_clauses=dict(coverage), fixed_covered_pairs=fixed_covered, total_pairs=1653,
        normalization="d_H(0)>=d_H(1)>=...>=d_H(7), with no further normalization",
        strengthening_clauses=[], prior_complete_seed="computations/dd82/construction/hs58_a6_saturated_seed_run/seed.json",
        scope="All 56 saturated a6 no-cross old-addition templates for D={(0,1),(10,11)}, all 400 ports and 28 H edges free, up to new-label degree sorting.",
        encoding_cpu_seconds=time.process_time()-start_cpu,
        encoding_wall_seconds=time.monotonic()-start_wall)
    dump(OUT / "encoding.json", record)
    print(json.dumps({k: v for k, v in record.items() if k in
                     ("variables", "clauses", "primary_variable_counts", "coverage_clauses", "total_pairs",
                      "encoding_cpu_seconds", "encoding_wall_seconds", "normalization", "scope")}))


def usage_delta(before):
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime


def solve():
    meta = json.loads((OUT / "encoding.json").read_text())
    assert not (OUT / "solver.log").exists(), "Only one solver attempt is authorized"
    command = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"), "--lrat", "-t", str(SECONDS),
               str(OUT / "input.cnf"), str(OUT / "proof.lrat")]

    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (SECONDS, SECONDS))
        resource.setrlimit(resource.RLIMIT_AS, (8*1024**3, 8*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE, (768*1024**2, 768*1024**2))

    before, start = resource.getrusage(resource.RUSAGE_CHILDREN), time.monotonic()
    with (OUT / "solver.log").open("w") as log:
        try:
            rc = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                timeout=SECONDS+30, preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:
            rc = None
    result = dict(status={10: "SAT_CANDIDATE", 20: "RAW_UNSAT", 0: "UNKNOWN",
                          -9: "CPU_LIMIT", -24: "CPU_LIMIT", -25: "OUTPUT_LIMIT",
                          None: "WALL_LIMIT"}.get(rc, "PROCESS_FAILURE"),
                  exit_code=rc, cpu_seconds=usage_delta(before), wall_seconds=time.monotonic()-start,
                  cpu_budget_seconds=SECONDS, memory_limit_bytes=8*1024**3,
                  proof_output_limit_bytes=768*1024**2, attempt=1, command=command,
                  variables=meta["variables"], clauses=meta["clauses"], proof_checked=False,
                  pinned_cpu=min(os.sched_getaffinity(0)), retained_solver_state=False)
    dump(OUT / "result.json", result)
    if rc == 10:
        values = {abs(q): q > 0 for line in (OUT / "solver.log").read_text().splitlines()
                  if line.startswith("v ") for q in map(int, line.split()[1:]) if q}
        domain = json.loads((OUT / "addition_domain.json").read_text())["templates"]
        chosen = [i for i, var in enumerate(meta["selectors"]) if values[var]]
        assert len(chosen) == 1
        additions = domain[chosen[0]]["additions"]
        ports = [[a for a, var in enumerate(row) if values[var]] for row in meta["attachment_variables"]]
        h = [tuple(map(int, key.split(","))) for key, var in meta["auxiliary_variables"].items() if values[var]]
        assert len(h) == 11
        original = {tuple(e) for e in meta["HS_edges"]}
        edges = sorted(list(original-D)+list(map(tuple, additions))+[(50+a,50+b) for a,b in h]
                       +[(x,50+a) for x,row in enumerate(ports) for a in row])
        assert len(edges) == len(set(edges)) == 232
        path = OUT / "candidate.json"
        dump(path, dict(n=58, edges=edges, old_deletions=sorted(D), old_additions=additions,
                        auxiliary_edges=h, old_new_ports=ports, selected_template=chosen[0]))
        path.with_suffix(".edges").write_text("58 232\n"+"".join(f"{x} {y}\n" for x,y in edges))
        result["independent_graph_check"] = json.loads(verify(path))
    elif rc == 20:
        check_command = [str(ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"),
                         "--no-trim", str(OUT / "input.cnf"), str(OUT / "proof.lrat")]
        before, start = resource.getrusage(resource.RUSAGE_CHILDREN), time.monotonic()
        with (OUT / "certificate_check.log").open("w") as log:
            try:
                checked_rc = subprocess.run(check_command, stdout=log, stderr=subprocess.STDOUT,
                                            timeout=180, preexec_fn=limits).returncode
            except subprocess.TimeoutExpired:
                checked_rc = None
        verified = checked_rc == 20 and "s VERIFIED" in (OUT / "certificate_check.log").read_text().splitlines()
        result["certificate_check"] = dict(command=check_command, exit_code=checked_rc,
            verified=verified, cpu_seconds=usage_delta(before), wall_seconds=time.monotonic()-start)
        result["proof_checked"] = verified
        if verified:
            result["status"] = "CHECKED_UNSAT"
    dump(OUT / "result.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["prepare", "solve"])
    args = parser.parse_args()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    (prepare if args.phase == "prepare" else solve)()
