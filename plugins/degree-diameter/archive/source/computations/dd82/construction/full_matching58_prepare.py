"""Exact full false-twin58 CNF preparation; this program never runs a solver.

All 28 six-by-six matching blocks are represented. The seven root blocks
are identity only by a coordinate gauge, leaving 21 arbitrary permutations.
No group action, triangle condition or prior f9 parameters constrain CNF.
"""
from itertools import combinations
from pathlib import Path
import argparse
import importlib.util
import json
import os
import sys
import time

from hs_augmentation import ROOT, ARCHIVE, dump

BASE = ROOT / "computations/dd82/construction"
OUT = BASE / "full_matching58_run"
SOURCE = BASE / "false_twins58_f9_coverage_run/candidate.best.edges"
SOURCE_BFS = BASE / "false_twins58_f9_coverage_run/independent_bfs.json"
PARENT_RUN_ID = "dd82-v3-f9-c7-20261013-0749"
FIBRES = [list(range(10+6*i, 16+6*i)) for i in range(8)]
PARENTS = list(range(2, 10))


def scaffold():
    return {(u, p) for u in (0, 1) for p in PARENTS} | {
        (PARENTS[i], x) for i, fibre in enumerate(FIBRES) for x in fibre}


def read_edges(path):
    rows = [tuple(map(int, line.split())) for line in path.read_text().splitlines() if line.strip()]
    assert rows[0] == (58, 232)
    edges = {tuple(sorted(e)) for e in rows[1:]}
    assert len(edges) == len(rows)-1 == 232
    assert all(0 <= u < v < 58 for u, v in edges)
    return edges


def interfaces_from_edges(edges):
    adj = [set() for _ in range(58)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(row) == 8 for row in adj)
    assert scaffold() <= edges
    interfaces = []
    rebuilt = scaffold()
    for i, j in combinations(range(8), 2):
        image = []
        for u in FIBRES[i]:
            targets = adj[u] & set(FIBRES[j])
            assert len(targets) == 1
            v = next(iter(targets))
            image.append(FIBRES[j].index(v))
            rebuilt.add((u, v))
        assert sorted(image) == list(range(6))
        if i == 0:
            assert image == list(range(6))
        interfaces.append(dict(i=i, j=j, permutation=image))
    assert rebuilt == edges
    return interfaces


def evaluate_dimacs(path, values):
    false_ids = []
    count = 0
    for line in path.read_text().splitlines():
        if line.startswith("p "):
            _, _, variables, expected = line.split()
            assert len(values)-1 == int(variables)
        elif line and not line.startswith("c"):
            clause = list(map(int, line.split()))
            assert clause[-1] == 0
            count += 1
            if not any(values[abs(lit)] == (lit > 0) for lit in clause[:-1]):
                false_ids.append(count)
    assert count == int(expected)
    return false_ids


def prepare():
    cpu, wall = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "input.cnf").exists(), "Preserve the prepared input"
    edges = read_edges(SOURCE)
    interfaces = interfaces_from_edges(edges)
    dump(OUT / "seed.json", dict(n=58, edges=sorted(edges), source=str(SOURCE.relative_to(ROOT)),
         parent_run_id=PARENT_RUN_ID, role="failed seed only; no edges fixed from this seed"))
    (OUT / "seed.edges").write_text("58 232\n" + "".join(f"{u} {v}\n" for u, v in sorted(edges)))
    dump(OUT / "seed.interfaces.json", dict(fibres=FIBRES, parents=PARENTS,
         twins=[0, 1], interfaces=interfaces, root_identity=True,
         migration="Exact same labelled edge set as source; extracted all 28 interfaces independently of A/B/C."))

    # Reuse only the existing DIMACS emitter and exact three-clause AND helper.
    spec = importlib.util.spec_from_file_location("full_matching58_emitter", ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(OUT / "input.cnf")
    edge_vars = {}
    edge_records = []
    values = [False]
    for i, j in combinations(range(8), 2):
        for a in range(6):
            for b in range(6):
                q = em.new_var("matching_edge")
                u, v = FIBRES[i][a], FIBRES[j][b]
                edge_vars[i, a, j, b] = q
                edge_records.append([i, a, j, b, u, v, q])
                values.append((u, v) in edges)

    def edge(i, a, j, b):
        assert i != j
        return edge_vars[i, a, j, b] if i < j else edge_vars[j, b, i, a]

    def exactly_one(row):
        em.add_clause(*row)
        for x, y in combinations(row, 2):
            em.add_clause(-x, -y)

    for i, j in combinations(range(8), 2):
        for a in range(6):
            exactly_one([edge(i, a, j, b) for b in range(6)])
        for b in range(6):
            exactly_one([edge(i, a, j, b) for a in range(6)])
    matching_end = em.clause_count
    for j in range(1, 8):
        for a in range(6):
            for b in range(6):
                q = edge(0, a, j, b)
                em.add_clause(q if a == b else -q)
    gauge_end = em.clause_count

    and_records, coverage = [], []
    for i, j in combinations(range(8), 2):
        for a in range(6):
            for b in range(6):
                terms = [edge(i, a, j, b)]
                for k in range(8):
                    if k in (i, j):
                        continue
                    for c in range(6):
                        left, right = edge(i, a, k, c), edge(k, c, j, b)
                        q = em.new_var("two_step_path")
                        mod.add_iff_and(em, q, left, right)
                        and_records.append([q, left, right])
                        values.append(values[left] and values[right])
                        assert len(values)-1 == q
                        terms.append(q)
                assert len(terms) == 37
                em.add_clause(*terms)
                coverage.append(dict(clause_id=em.clause_count,
                    coordinates=[i, a, j, b], pair=[FIBRES[i][a], FIBRES[j][b]],
                    direct=terms[0], paths=terms[1:]))
    em.finish()
    assert (em.variable_count, em.clause_count) == (37296, 115500)
    assert (matching_end, gauge_end) == (5376, 5628)
    assert len(and_records) == 36288 and len(coverage) == 1008
    dump(OUT / "variables.json", dict(edge_record_format=["i", "a", "j", "b", "u", "v", "variable"],
        edge_variables=edge_records, and_record_format=["output", "left", "right"], and_variables=and_records))
    dump(OUT / "coverage.json", coverage)
    assignment = [q if values[q] else -q for q in range(1, len(values))]
    (OUT / "seed.assignment.txt").write_text("v " + " ".join(map(str, assignment)) + " 0\n")
    false_ids = evaluate_dimacs(OUT / "input.cnf", values)
    by_id = {row["clause_id"]: row for row in coverage}
    assert all(q in by_id for q in false_ids)
    false_pairs = [by_id[q]["pair"] for q in false_ids]
    prior = json.loads(SOURCE_BFS.read_text())
    bfs_pairs = sorted(row["pair"] for row in prior["bad_pairs"])
    assert sorted(false_pairs) == bfs_pairs and len(false_ids) == 105
    dump(OUT / "seed.cnf_check.json", dict(false_clause_count=len(false_ids),
        false_clause_ids=false_ids, false_pairs=false_pairs, all_false_clauses_are_coverage=True,
        matching_gauge_and_tseitin_clauses_all_satisfied=True,
        agrees_with_existing_independent_bfs=True, independent_bfs_source=str(SOURCE_BFS.relative_to(ROOT)),
        new_bfs_runs=0, solver_calls=0))

    solver = ROOT / ".tools/lean-4.24.0-linux/bin/cadical"
    checker = ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"
    assert os.access(solver, os.X_OK) and os.access(checker, os.X_OK)
    dump(OUT / "interfaces.json", dict(status="PREPARED_NOT_RUN", solver_calls=0,
        solver_command_template=[str(solver), "--lrat", "-t", "{cpu_seconds}", str(OUT / "input.cnf"), str(OUT / "proof.lrat")],
        checker_command=[str(checker), "--no-trim", str(OUT / "input.cnf"), str(OUT / "proof.lrat")],
        sat_decode_command=[sys.executable, str(Path(__file__).resolve()), "decode", "--log", str(OUT / "solver.log")],
        independent_bfs_command=[sys.executable, str(BASE / "verify_hs_candidate.py"), str(OUT / "candidate.json")],
        suggested_profile=dict(cpu_seconds=30, wall_seconds=40, threads=1, memory_bytes=4*1024**3,
                               proof_output_limit_bytes=256*1024**2),
        status_semantics=dict(sat="Decode full graph and independently BFS before accepting it",
            unsat="RAW until exact-input LRAT verifies", unknown="No exclusion or feasibility conclusion")))
    record = dict(parent_run_id=PARENT_RUN_ID, status="PREPARED_NOT_RUN", solver_calls=0,
        scope="All false-twin58 graphs up to choice of twins, fibre labels and root-matching coordinate gauge; no group action imposed",
        fibres=FIBRES, parents=PARENTS, twins=[0, 1], fixed_scaffold_edges=sorted(scaffold()),
        represented_matching_blocks=28, independent_matching_blocks_after_gauge=21,
        variables=em.variable_count, primary_edge_variables=1008, tseitin_variables=len(and_records),
        clauses=em.clause_count, clause_groups=dict(perfect_matching=5376, root_gauge=252,
                                                   tseitin_and=108864, cross_coverage=1008),
        normalization="Q_0j = I for j=1,...,7; no further normalization or additional cuts",
        cnf_bytes=(OUT / "input.cnf").stat().st_size,
        seed_is_exact_source_graph=True, seed_false_coverage_clauses=105,
        helper_reuse="CNFEmitter and add_iff_and only; no historical n62 branch or constraints executed",
        preparation_cpu_seconds=time.process_time()-cpu,
        preparation_wall_seconds=time.monotonic()-wall)
    dump(OUT / "encoding.json", record)
    print(json.dumps({k:v for k,v in record.items() if k not in ("fixed_scaffold_edges", "fibres")}))


def decode(log_path):
    """Decode an already produced SAT model; no process launch is performed."""
    text = log_path.read_text()
    assert "s SATISFIABLE" in text.splitlines()
    meta = json.loads((OUT / "encoding.json").read_text())
    mapped = {abs(lit): lit > 0 for line in text.splitlines() if line.startswith("v ")
              for lit in map(int, line.split()[1:]) if lit}
    assert set(mapped) == set(range(1, meta["variables"]+1))
    values = [False] + [mapped[q] for q in range(1, meta["variables"]+1)]
    assert not evaluate_dimacs(OUT / "input.cnf", values)
    variables = json.loads((OUT / "variables.json").read_text())["edge_variables"]
    edges = scaffold() | {(u,v) for i,a,j,b,u,v,q in variables if values[q]}
    assert len(edges) == 232
    interfaces = interfaces_from_edges(edges)
    dump(OUT / "candidate.json", dict(n=58, edges=sorted(edges), interfaces=interfaces,
         parent_run_id=PARENT_RUN_ID, source_solver_log=str(log_path)))
    (OUT / "candidate.edges").write_text("58 232\n" + "".join(f"{u} {v}\n" for u,v in sorted(edges)))
    print(json.dumps(dict(status="SAT_CANDIDATE_PENDING_INDEPENDENT_BFS", n=58, edges=232)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "decode"])
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    if args.action == "prepare":
        prepare()
    else:
        assert args.log is not None
        decode(args.log)
