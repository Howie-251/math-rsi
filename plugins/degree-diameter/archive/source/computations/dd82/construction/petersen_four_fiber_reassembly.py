"""One exact K4 interface reassembly, guided by the 4--5 cycle budget.

Release 01,04,05,14,15,45; require 01 to change.  The two fixed routes
4->2->5 and 4->3->5 coincide in Phi.  Complete target coverage forces
the remaining nine routes in every 4->5 row to partition J-Phi exactly.
First build a complete seed satisfying that partition, then one bounded SAT.
"""
from collections import Counter
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

HERE = Path(__file__).resolve().parent
OUT = HERE / "petersen_four_fiber_reassembly_run"
SOURCE = HERE / "petersen_all_matchings_run/candidate.best.json"
RELEASED = {(0, 1), (0, 4), (0, 5), (1, 4), (1, 5), (4, 5)}


def adjacency(edges):
    ns = [set() for _ in range(60)]
    for u, v in edges:
        ns[u].add(v)
        ns[v].add(u)
    return ns


def matching(ns, i, j):
    result = []
    for u in range(10*i, 10*i+10):
        choices = ns[u] & set(range(10*j, 10*j+10))
        assert len(choices) == 1
        result.append(next(iter(choices)))
    assert len(set(result)) == 10
    return result


def diagnostic(edges):
    ns = adjacency(edges)
    blocks = []
    for i, j in combinations(range(6), 2):
        hist = Counter()
        energy = 0
        for u in range(10*i, 10*i+10):
            for v in range(10*j, 10*j+10):
                routes = int(v in ns[u]) + len(ns[u] & ns[v])
                hist[routes] += 1
                b = routes - 1
                energy += b*(b-1)//2
        blocks.append(dict(fibers=[i,j], route_histogram=dict(sorted(hist.items())),
                           bad_pairs=hist[0], energy=energy))
    hs = []
    for omit in range(6):
        keep = [v for v in range(60) if v//10 != omit]
        keep_set = set(keep)
        sub = {v: ns[v] & keep_set for v in keep}
        if all(len(sub[u] & sub[v]) == (0 if v in sub[u] else 1)
               for u,v in combinations(keep,2)):
            hs.append(omit)
    return dict(blocks=blocks, energy=sum(b["energy"] for b in blocks),
                bad_pair_count=sum(b["bad_pairs"] for b in blocks),
                omitted_fibers_giving_induced_HS50=hs)


def prepare():
    start = time.monotonic()
    cpu = time.process_time()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "encoding.json").exists(), "No unchanged regeneration"
    original = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    ns = adjacency(original)
    f = {(i,j): matching(ns,i,j) for i in range(6) for j in range(6) if i != j}
    phi = [f[2,5][f[4,2][u]-20] for u in range(10)]
    assert phi == [f[3,5][f[4,3][u]-30] for u in range(10)]
    assert all(phi == [f[a,5][f[4,a][u]-10*a] for u in range(10)] for a in (0,1))

    # The original M45 has seven distinct internal/direct targets avoiding
    # Phi. Its remaining two targets form a 2-regular bipartite graph.
    residual = []
    for u in range(40,50):
        m = f[4,5][u-40]
        forbidden = {phi[u-40], m} | (ns[m] & set(range(50,60)))
        forbidden |= {f[4,5][w-40] for w in ns[u] if 40 <= w < 50}
        assert len(forbidden) == 8
        residual.append(set(range(50,60))-forbidden)
    assert all(sum(v in row for row in residual) == 2 for v in range(50,60))
    owner = {}
    def augment(u, seen):
        for v in sorted(residual[u]):
            if v in seen:
                continue
            seen.add(v)
            if v not in owner or augment(owner[v], seen):
                owner[v] = u
                return True
        return False
    assert all(augment(u,set()) for u in range(10))
    q0 = [next(v for v,u0 in owner.items() if u0 == u) for u in range(10)]
    q1 = [next(iter(residual[u]-{q0[u]})) for u in range(10)]
    assert len(set(q1)) == 10
    seed = set(original)
    # Keep 4->a for the seed and replace a->5 to realize Qa exactly.
    for a, q in ((0,q0),(1,q1)):
        seed -= {e for e in seed if e[0]//10 == a and e[1]//10 == 5}
        seed |= {(f[4,a][u],q[u]) for u in range(10)}
    # A genuine old-core change: transpose the first two outputs of M01.
    old_pair = {(0,f[0,1][0]), (1,f[0,1][1])}
    new_pair = {(0,f[0,1][1]), (1,f[0,1][0])}
    seed = (seed-old_pair) | new_pair
    assert len(seed) == 240 and all(len(s) == 8 for s in adjacency(seed))
    seed_data = dict(n=60, edges=sorted(seed), source=str(SOURCE),
                     released_interfaces=sorted(RELEASED), phi_4_to_5=phi,
                     reconstructed_routes_4_to_0_to_5=q0,
                     reconstructed_routes_4_to_1_to_5=q1,
                     removed_edges=sorted(original-seed), added_edges=sorted(seed-original),
                     mechanism="Decompose the two unused 4-to-5 targets into two matching routes; realize them through fibers 0 and 1, and change core interface 01.")
    dump(OUT/"seed.json",seed_data)
    (OUT/"seed.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(seed)))
    checked = json.loads(verify(OUT/"seed.json"))
    diag = diagnostic(seed)
    assert diag["blocks"][-1]["fibers"] == [4,5]
    assert diag["blocks"][-1]["energy"] == 0
    assert not diag["omitted_fibers_giving_induced_HS50"]
    dump(OUT/"seed.diagnostic.json",diag)

    fixed = {e for e in original if (e[0]//10,e[1]//10) not in RELEASED}
    adj = adjacency(fixed)
    spec = importlib.util.spec_from_file_location("four_fiber_cardinality",ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(OUT/"input.cnf")
    variables = {(u,v):em.new_var("matching_edge") for i,j in sorted(RELEASED)
                 for u in range(10*i,10*i+10) for v in range(10*j,10*j+10)}
    def var(u,v):
        return variables.get(tuple(sorted((u,v))))
    def exactly_one(lits):
        em.add_clause(*lits)
        for x,y in combinations(lits,2):
            em.add_clause(-x,-y)
    for i,j in sorted(RELEASED):
        for u in range(10*i,10*i+10):
            exactly_one([var(u,v) for v in range(10*j,10*j+10)])
        for v in range(10*j,10*j+10):
            exactly_one([var(u,v) for u in range(10*i,10*i+10)])
    # Every retained target in this explicitly new scope changes old core 01.
    em.add_clause(*[-var(u,f[0,1][u]) for u in range(10)])
    conjunctions = {}
    def conjunction(x,y):
        key = tuple(sorted((x,y)))
        if key not in conjunctions:
            z = em.new_var("two_edge_route")
            mod.add_iff_and(em,z,*key)
            conjunctions[key] = z
        return conjunctions[key]
    def variable_routes(u,v):
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
                terms.add(conjunction(a,b))
        return sorted(terms)
    coverage = 0
    for u,v in combinations(range(60),2):
        if v in adj[u] or adj[u]&adj[v]:
            continue
        em.add_clause(*variable_routes(u,v))
        coverage += 1
    before_special = em.clause_count
    for u in range(40,50):
        for v in range(50,60):
            terms = variable_routes(u,v)
            assert len(terms) == 27 # direct, six internal, twenty 2-variable paths
            if v == phi[u-40]:
                for t in terms:
                    em.add_clause(-t)
            else:
                exactly_one(terms)
    special = em.clause_count-before_special
    em.finish()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    encoding = dict(n=60, source=str(SOURCE), fixed_edges=sorted(fixed),
                    released_interfaces=sorted(RELEASED), require_core_01_changed=True,
                    phi_4_to_5=phi, edge_variables=[[u,v,z] for (u,v),z in variables.items()],
                    variables=em.variable_count, clauses=em.clause_count,
                    route_conjunction_variables=len(conjunctions), coverage_clauses=coverage,
                    exact_45_partition_clauses=special,
                    scope="Six independent matching interfaces of K4 on fibers 0,1,4,5; original nine other interfaces and all Petersen internal graphs fixed; 01 must change.",
                    candidate_preservation="All free interfaces are arbitrary permutations. Exact 45 partition follows from two identical fixed routes Phi plus the one-per-row defect budget. All remaining vertex-pair coverage is encoded directly.",
                    independent_seed_check=checked,
                    preparation_parent_cpu_seconds=time.process_time()-cpu,
                    preparation_bfs_child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                    preparation_wall_seconds=time.monotonic()-start)
    dump(OUT/"encoding.json",encoding)
    print(json.dumps({k:v for k,v in encoding.items() if k not in ("fixed_edges","edge_variables")}))


def solve():
    assert not (OUT/"result.json").exists(), "No unchanged solve"
    enc = json.loads((OUT/"encoding.json").read_text())
    budget = 45
    command = [str(ROOT/".tools/lean-4.24.0-linux/bin/cadical"),"-t",str(budget),str(OUT/"input.cnf")]
    # This is a construction call without a proof file. Any UNSAT remains RAW;
    # no second solver or automatic certificate run is authorized here.
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(budget,budget+1))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with (OUT/"solver.log").open("w") as log:
        try:
            rc = subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,
                                preexec_fn=limits,timeout=50).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    report = dict(status={10:"SAT_CANDIDATE",20:"RAW_UNSAT",0:"UNKNOWN",-24:"CPU_LIMIT"}.get(rc,"PROCESS_FAILURE"),
                  exit_code=rc, cpu_budget_seconds=budget,
                  cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-start,command=command,
                  proof_written=False,proof_checked=False,threads=1,
                  variables=enc["variables"],clauses=enc["clauses"],scope=enc["scope"])
    if rc == 10:
        values = {abs(lit):lit>0 for line in (OUT/"solver.log").read_text().splitlines()
                  if line.startswith("v ") for lit in map(int,line.split()[1:]) if lit}
        edges = {tuple(e) for e in enc["fixed_edges"]}
        edges |= {(u,v) for u,v,z in enc["edge_variables"] if values[z]}
        assert len(edges) == 240
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
