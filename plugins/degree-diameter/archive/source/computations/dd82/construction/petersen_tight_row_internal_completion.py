"""One exact all-six-internal completion after the tight-row degree repair.

270 internal-edge variables, no fixed internal edges and no symmetry cuts.
Degree-three clauses and triangle/C4 prohibitions characterize Petersen
graphs on ten vertices. Every remaining cross-pair constraint is binary.
"""
from itertools import combinations
from pathlib import Path
import argparse
import json
import os
import resource
import subprocess
import time

from hs_augmentation import ROOT, dump, verify
from petersen_four_fiber_reassembly import adjacency, diagnostic

OUT = ROOT / "computations/dd82/construction/petersen_tight_row_internal_completion_run"
SOURCE = ROOT / "computations/dd82/construction/petersen_tight_row_repair_run/candidate.json"


def prepare():
    start, cpu_start = time.monotonic(), time.process_time()
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "input.cnf").exists(), "Do not regenerate an unchanged input"
    seed = json.loads(SOURCE.read_text())
    edges = {tuple(e) for e in seed["edges"]}
    assert seed["n"] == 60 and len(edges) == 240
    ns = adjacency(edges)
    assert all(len(s) == 8 for s in ns)
    fixed = {e for e in edges if e[0]//10 != e[1]//10}
    external = adjacency(fixed)
    assert len(fixed) == 150
    match = {}
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for u in range(10*i,10*i+10):
                targets = [v for v in external[u] if v//10 == j]
                assert len(targets) == 1
                match[u,j] = targets[0]
    assert all(len(s) == 5 for s in external)
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for u in range(10*i,10*i+10):
                targets = {match[u,j]}
                targets.update(match[match[u,k],j] for k in range(6) if k not in (i,j))
                assert len(targets) >= 4

    variables = {}
    for i in range(6):
        for u,v in combinations(range(10*i,10*i+10),2):
            variables[u,v] = len(variables)+1
    assert len(variables) == 270

    def var(u,v):
        assert u != v and u//10 == v//10
        return variables[tuple(sorted((u,v)))]

    clauses, counts = [], {}
    for i in range(6):
        for u in range(10*i,10*i+10):
            incident = [var(u,v) for v in range(10*i,10*i+10) if v != u]
            # At most three: no four simultaneously true.
            clauses.extend(tuple(-x for x in subset) for subset in combinations(incident,4))
            # At least three: no seven simultaneously false.
            clauses.extend(tuple(subset) for subset in combinations(incident,7))
    counts["exact_cubic"] = len(clauses)
    before = len(clauses)
    for i in range(6):
        for a,b,c in combinations(range(10*i,10*i+10),3):
            clauses.append((-var(a,b),-var(a,c),-var(b,c)))
    counts["no_triangles"] = len(clauses)-before
    before = len(clauses)
    for i in range(6):
        for a,b,c,d in combinations(range(10*i,10*i+10),4):
            for cycle in ((a,b,c,d),(a,b,d,c),(a,c,b,d)):
                clauses.append(tuple(-var(cycle[k],cycle[(k+1)%4]) for k in range(4)))
    counts["no_four_cycles"] = len(clauses)-before

    coverage = []
    for i,j in combinations(range(6),2):
        for u in range(10*i,10*i+10):
            for v in range(10*j,10*j+10):
                if v in external[u] or external[u] & external[v]:
                    continue
                # Only routes left: u--internal--M_ji(v)--matching--v,
                # and u--matching--M_ij(u)--internal--v.
                a = var(u,match[v,i])
                b = var(match[u,j],v)
                assert a != b
                coverage.append(dict(pair=[u,v], variables=[a,b],
                    source_internal_edge=sorted((u,match[v,i])),
                    target_internal_edge=sorted((match[u,j],v))))
                clauses.append((a,b))
    counts["cross_coverage_binary"] = len(coverage)
    assert counts == dict(exact_cubic=9720,no_triangles=720,
                          no_four_cycles=3780,cross_coverage_binary=768)
    assert len(clauses) == 14988
    # For the already verified complete seed, exactly its BFS-bad pairs
    # falsify the coverage clauses. All local Petersen clauses hold.
    assignment = {q:edge in edges for edge,q in variables.items()}
    false_clauses = [c for c in clauses if not any(assignment[abs(x)] == (x>0) for x in c)]
    failed_pairs = {tuple(c["pair"]) for c in coverage
                    if not any(assignment[q] for q in c["variables"])}
    checked = json.loads(SOURCE.with_suffix(".verification.json").read_text())
    assert failed_pairs == {tuple(row["pair"]) for row in checked["bad_pairs"]}
    assert len(false_clauses) == len(failed_pairs) == 286

    with (OUT / "input.cnf").open("w") as stream:
        stream.write(f"p cnf {len(variables)} {len(clauses)}\n")
        for clause in clauses:
            stream.write(" ".join(map(str,clause))+" 0\n")
    dump(OUT / "coverage.json",coverage)
    encoding = dict(source=str(SOURCE.relative_to(ROOT)),
        scope="Exactly the saved repaired fifteen external matching interfaces; all six internal Petersen graphs independently free, with no internal edges fixed and no symmetry breaking.",
        n=60,variables=len(variables),clauses=len(clauses),clause_groups=counts,
        edge_variables=[[u,v,q] for (u,v),q in variables.items()],
        fixed_external_edges=sorted(fixed),
        free_internal_fibers=list(range(6)),fixed_internal_edges=[],
        symmetry_breaking_clauses=0,
        known_seed_falsified_clauses=286,known_seed_bfs_bad_pairs=286,
        known_seed_bad_pairs_equal_falsified_coverage_clauses=True,
        candidate_preservation="Every Petersen choice satisfies exact cubic and girth>=5. Conversely any local solution is cubic girth>=5 on ten vertices, so its 1+3+6 radius-two tree exhausts the fiber. The direct and four other-fiber routes are fixed; an uncovered cross pair has precisely the two encoded possible internal-edge routes.",
        preparation_cpu_seconds=time.process_time()-cpu_start,
        preparation_wall_seconds=time.monotonic()-start)
    dump(OUT / "encoding.json",encoding)
    print(json.dumps({k:v for k,v in encoding.items() if k not in ("edge_variables","fixed_external_edges")}))


def bounded(command, log_path, cpu_budget, wall_budget, proof_cap=False):
    pin = min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0,{pin})
        resource.setrlimit(resource.RLIMIT_CPU,(cpu_budget,cpu_budget+1))
        resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
        if proof_cap:
            resource.setrlimit(resource.RLIMIT_FSIZE,(768*1024**2,768*1024**2))

    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with log_path.open("w") as stream:
        try:
            rc = subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,
                                preexec_fn=limits,timeout=wall_budget).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command,exit_code=rc,
                cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                wall_seconds=time.monotonic()-start,cpu_budget_seconds=cpu_budget,
                wall_budget_seconds=wall_budget,pinned_cpu=pin,threads=1)


def solve():
    enc = json.loads((OUT / "encoding.json").read_text())
    assert not (OUT / "launch.json").exists(), "Only one solver launch is authorized"
    command = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"),
               "--lrat","-t","180",str(OUT / "input.cnf"),str(OUT / "proof.lrat")]
    dump(OUT / "launch.json",dict(command=command,solver_launches=1,
         cpu_budget_seconds=180,memory_limit_bytes=8*1024**3,proof_limit_bytes=768*1024**2))
    result = bounded(command,OUT / "solver.log",180,190,True)
    result.update(scope=enc["scope"],variables=enc["variables"],clauses=enc["clauses"],
                  solver_calls=1,proof_checked=False,
                  proof_bytes=(OUT / "proof.lrat").stat().st_size if (OUT / "proof.lrat").exists() else 0)
    rc = result["exit_code"]
    result["status"] = {10:"SAT_CANDIDATE",20:"RAW_UNSAT",0:"UNKNOWN",
                        -24:"CPU_LIMIT_UNKNOWN",-25:"OUTPUT_LIMIT_UNKNOWN"}.get(rc,"PROCESS_FAILURE_UNKNOWN")
    if rc == 10:
        values = {abs(lit):lit>0 for line in (OUT / "solver.log").read_text().splitlines()
                  if line.startswith("v ") for lit in map(int,line.split()[1:]) if lit}
        edges = {tuple(e) for e in enc["fixed_external_edges"]}
        edges.update((u,v) for u,v,q in enc["edge_variables"] if values[q])
        dump(OUT / "candidate.json",dict(n=60,edges=sorted(edges),source=str(SOURCE.relative_to(ROOT))))
        (OUT / "candidate.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(edges)))
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        result["independent_graph_check"] = json.loads(verify(OUT / "candidate.json"))
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        result["bfs_cpu_seconds"] = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
        dump(OUT / "candidate.diagnostic.json",diagnostic(edges))
    elif rc == 20:
        checker = [str(ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"),
                   "--no-trim",str(OUT / "input.cnf"),str(OUT / "proof.lrat")]
        check = bounded(checker,OUT / "certificate_check.log",180,190)
        check["verified"] = check["exit_code"] == 20 and "s VERIFIED" in (OUT / "certificate_check.log").read_text().splitlines()
        result["certificate_check"] = check
        result["proof_checked"] = check["verified"]
        if check["verified"]:
            result["status"] = "CHECKED_UNSAT"
    dump(OUT / "result.json",result)
    print(json.dumps(result),flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action",choices=["prepare","solve"])
    args = parser.parse_args()
    {"prepare":prepare,"solve":solve}[args.action]()
