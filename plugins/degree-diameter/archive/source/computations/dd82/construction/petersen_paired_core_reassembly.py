"""New boundary modification: dualize interfaces 01 and 23 simultaneously.

The unique nonoriginal M23 preserving M+PM+MP is already saved by the
paired-core domain computation. Compute the analogous small M01 domain,
build an actual two-channel seed, then one 25-CPU exact assembly call.
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

from hs_augmentation import ROOT, ARCHIVE, dump, verify
from petersen_four_fiber_reassembly import SOURCE, RELEASED, adjacency, matching, diagnostic

HERE = Path(__file__).resolve().parent
OUT = HERE/"petersen_paired_core_reassembly_run"


def prepare():
    cpu,wall = time.process_time(),time.monotonic()
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"encoding.json").exists(), "No unchanged rerun"
    original = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    ns = adjacency(original)
    f = {(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i!=j}
    old01 = [v-10 for v in f[0,1]]
    old23 = [v-30 for v in f[2,3]]
    domain23 = json.loads((HERE/"petersen_paired_core_exchange_run/domain.json").read_text())
    assert domain23["complete"] and domain23["solution_count"] == 2
    new23 = next(p for p in domain23["solutions"] if p != old23)
    # Exact cover of the unchanged direct/internal 7-route support in 01.
    p0 = [ns[u]&set(range(10)) for u in range(10)]
    p1 = [{v-10 for v in ns[10+u] if 10<=v<20} for u in range(10)]
    support = set()
    for u,v in enumerate(old01):
        cells = {(u,v)}|{(w,v) for w in p0[u]}|{(u,w) for w in p1[v]}
        assert len(cells) == 7 and support.isdisjoint(cells)
        support |= cells
    domains,placements = [],{}
    for u in range(10):
        row = []
        for v in range(10):
            cells = {(u,v)}|{(w,v) for w in p0[u]}|{(u,w) for w in p1[v]}
            if cells <= support:
                row.append(v)
                placements[u,v] = sum(1<<(10*x+y) for x,y in cells)
        domains.append(row)
    solutions,state,nodes = [],[-1]*10,0
    def visit(u,used,cells):
        nonlocal nodes
        nodes += 1
        if u == 10:
            assert cells.bit_count() == 70
            solutions.append(state[:])
            return
        for v in domains[u]:
            placement = placements[u,v]
            if not (used>>v&1) and not (cells&placement):
                state[u] = v
                visit(u+1,used|(1<<v),cells|placement)
    visit(0,0,0)
    assert old01 in solutions
    assert len(solutions) == 2
    new01 = next(p for p in solutions if p!=old01)
    dump(OUT/"core_domains.json",dict(domain01=dict(complete=True,allowed_arrows=domains,
         nodes=nodes,solutions=solutions,original=old01,selected=new01),
         domain23_source="../petersen_paired_core_exchange_run/domain.json",
         selected23=new23,old23=old23))

    # Reuse the already constructed exact Q0/Q1 partition, not its old core.
    prior = json.loads((HERE/"petersen_four_fiber_reassembly_run/seed.json").read_text())
    seed = {tuple(e) for e in prior["edges"] if (e[0]//10,e[1]//10) not in {(0,1),(2,3)}}
    seed |= {(u,10+v) for u,v in enumerate(new01)}
    seed |= {(20+u,30+v) for u,v in enumerate(new23)}
    assert len(seed) == 240 and all(len(s)==8 for s in adjacency(seed))
    dump(OUT/"seed.json",dict(n=60,edges=sorted(seed),source=str(SOURCE),
         mechanism="Preserve both 7-slot direct/internal matrices while dualizing core matchings 01 and 23; retain the exact two-channel 45 partition",
         selected_core01=new01,selected_core23=new23,
         removed_edges=sorted(original-seed),added_edges=sorted(seed-original)))
    (OUT/"seed.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(seed)))
    checked = json.loads(verify(OUT/"seed.json"))
    diag = diagnostic(seed)
    assert all(b["energy"] == 0 for b in diag["blocks"] if b["fibers"] in ([2,3],[4,5]))
    assert not diag["omitted_fibers_giving_induced_HS50"]
    dump(OUT/"seed.diagnostic.json",diag)

    # New fixed boundary: all old fixed edges except 23, which is replaced
    # by its unique nonoriginal exact-local solution. Six module interfaces
    # remain arbitrary; 01 must differ from the original seed interface.
    fixed = {e for e in original if (e[0]//10,e[1]//10) not in RELEASED|{(2,3)}}
    fixed |= {(20+u,30+v) for u,v in enumerate(new23)}
    adj = adjacency(fixed)
    phi = prior["phi_4_to_5"]
    spec = importlib.util.spec_from_file_location("paired_core_cardinality",ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(OUT/"input.cnf")
    variables = {(u,v):em.new_var("edge") for i,j in sorted(RELEASED)
                 for u in range(10*i,10*i+10) for v in range(10*j,10*j+10)}
    def var(u,v):
        return variables.get(tuple(sorted((u,v))))
    def exactly_one(lits):
        em.add_clause(*lits)
        for a,b in combinations(lits,2):
            em.add_clause(-a,-b)
    for i,j in sorted(RELEASED):
        for u in range(10*i,10*i+10):
            exactly_one([var(u,v) for v in range(10*j,10*j+10)])
        for v in range(10*j,10*j+10):
            exactly_one([var(u,v) for u in range(10*i,10*i+10)])
    em.add_clause(*[-var(u,10+old01[u]) for u in range(10)])
    conjunctions = {}
    def paths(u,v):
        terms = set()
        if var(u,v):
            terms.add(var(u,v))
        for w in range(60):
            if w in (u,v):
                continue
            a,b = var(u,w),var(v,w)
            if w in adj[u] and b:
                terms.add(b)
            elif w in adj[v] and a:
                terms.add(a)
            elif a and b:
                key = tuple(sorted((a,b)))
                if key not in conjunctions:
                    z = em.new_var("route")
                    mod.add_iff_and(em,z,*key)
                    conjunctions[key] = z
                terms.add(conjunctions[key])
        return sorted(terms)
    coverage = 0
    for u,v in combinations(range(60),2):
        if v not in adj[u] and not (adj[u]&adj[v]):
            em.add_clause(*paths(u,v))
            coverage += 1
    before_special = em.clause_count
    for u in range(40,50):
        for v in range(50,60):
            row = paths(u,v)
            assert len(row) == 27
            if v == phi[u-40]:
                for z in row:
                    em.add_clause(-z)
            else:
                exactly_one(row)
    special = em.clause_count-before_special
    em.finish()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(n=60,source=str(SOURCE),fixed_edges=sorted(fixed),new_fixed_M23=new23,
         released_interfaces=sorted(RELEASED),require_original_M01_changed=True,
         edge_variables=[[u,v,z] for (u,v),z in variables.items()],
         variables=em.variable_count,clauses=em.clause_count,coverage_clauses=coverage,
         exact45_partition_clauses=special,conjunction_variables=len(conjunctions),
         scope="Fixed unique nonoriginal exact-local M23; free six interfaces 01,04,05,14,15,45 with original01 forbidden; eight other original matching interfaces fixed",
         seed_check=checked,preparation_parent_cpu_seconds=time.process_time()-cpu,
         preparation_bfs_child_cpu_seconds=after.ru_utime+after.ru_stime-child.ru_utime-child.ru_stime,
         preparation_wall_seconds=time.monotonic()-wall)
    dump(OUT/"encoding.json",report)
    print(json.dumps({k:v for k,v in report.items() if k not in ("fixed_edges","edge_variables")}))


def solve():
    assert not (OUT/"result.json").exists(), "No unchanged solve"
    enc = json.loads((OUT/"encoding.json").read_text())
    budget = 25
    command = [str(ROOT/".tools/lean-4.24.0-linux/bin/cadical"),"-t",str(budget),str(OUT/"input.cnf")]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(budget,budget+1))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with (OUT/"solver.log").open("w") as log:
        try:
            rc = subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=30).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(status={10:"SAT_CANDIDATE",20:"RAW_UNSAT",0:"UNKNOWN",-24:"CPU_LIMIT"}.get(rc,"PROCESS_FAILURE"),
         exit_code=rc,scope=enc["scope"],command=command,cpu_budget_seconds=budget,
         cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
         wall_seconds=time.monotonic()-start,threads=1,proof_written=False,proof_checked=False)
    if rc == 10:
        values = {abs(lit):lit>0 for line in (OUT/"solver.log").read_text().splitlines()
                  if line.startswith("v ") for lit in map(int,line.split()[1:]) if lit}
        edges = {tuple(e) for e in enc["fixed_edges"]} | {(u,v) for u,v,z in enc["edge_variables"] if values[z]}
        dump(OUT/"candidate.json",dict(n=60,edges=sorted(edges),scope=enc["scope"]))
        (OUT/"candidate.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(edges)))
        report["independent_graph_check"] = json.loads(verify(OUT/"candidate.json"))
        dump(OUT/"candidate.diagnostic.json",diagnostic(edges))
    dump(OUT/"result.json",report)
    print(json.dumps(report))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase",choices=["prepare","solve"])
    args = parser.parse_args()
    (prepare if args.phase == "prepare" else solve)()
