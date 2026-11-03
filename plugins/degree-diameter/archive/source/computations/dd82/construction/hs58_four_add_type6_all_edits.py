"""One bounded full type6 assembly: all deletions, additions and ports free."""
from itertools import combinations
import importlib.util
import json
import os
import resource
import subprocess
import sys
import time

import networkx as nx
from hs_augmentation import ROOT, ARCHIVE, base, dump, verify

OUT = ROOT / "computations/dd82/construction/hs58_four_add_type6_all_edits_run"
H = {(0,a) for a in range(1,8)} | {(1,4),(2,3)}


def main():
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "encoding.json").exists(), "One unchanged attempt only"
    prep_cpu, prep_wall = time.process_time(), time.monotonic()
    before_children = resource.getrusage(resource.RUSAGE_CHILDREN)
    original, original_ns = base()
    original = set(original)
    hn = [set() for _ in range(8)]
    for a,b in H:
        hn[a].add(b); hn[b].add(a)
    seed_source = ROOT / "computations/dd82/construction/hs58_two_delete_four_add_switch_run/parent3_h4_7.json"
    seed = json.loads(seed_source.read_text())
    old = [tuple(e) for e in seed["edges"] if e[1] < 50]
    deg = [0]*50
    for x,y in old:
        deg[x] += 1; deg[y] += 1
    flow = nx.DiGraph()
    for x in range(50):
        flow.add_edge("source",x,capacity=8-deg[x])
        for a in range(8):
            flow.add_edge(x,50+a,capacity=1)
    for a in range(8):
        flow.add_edge(50+a,"sink",capacity=8-len(hn[a]))
    value, assignment = nx.maximum_flow(flow,"source","sink")
    assert value == 46
    ports = [[a for a in range(8) if assignment[x][50+a]] for x in range(50)]
    graph = sorted(old+[(50+a,50+b) for a,b in H]+[(x,50+a) for x,row in enumerate(ports) for a in row])
    seedpath = OUT / "seed.json"
    dump(seedpath,dict(n=58,edges=graph,old_deletions=seed["old_deletions"],
         old_additions=seed["old_additions"],auxiliary_edges=sorted(H),attachments=ports,
         mechanism="Retain the explicit four-addition old core and assign all 46 ports by exact integral capacity flow to the remaining type6 auxiliary.",
         source=str(seed_source)))
    seedpath.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x,y in graph))
    seedcheck = json.loads(verify(seedpath))
    fullcheck = json.loads(seedpath.with_suffix(".verification.json").read_text())
    assert fullcheck["degrees"] == [8]*58 and fullcheck["edges"] == 232
    spec = importlib.util.spec_from_file_location("type6_full_cardinality",ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(OUT / "input.cnf")
    R = {e:em.new_var("retained_HS_edge") for e in sorted(original)}
    A = {e:em.new_var("added_original_nonedge") for e in combinations(range(50),2) if e not in original}
    B = [[em.new_var("attachment") for a in range(8)] for x in range(50)]
    def edge(x,y):
        if x == y:
            return False
        if x > y:
            x,y = y,x
        if y < 50:
            return R[(x,y)] if (x,y) in R else A[(x,y)]
        if x < 50:
            return B[x][y-50]
        return (x-50,y-50) in H
    for x in range(50):
        mod.enforce_exact(em,[edge(x,y) for y in range(50) if y != x]+B[x],8,f"degree_old_{x}")
    for a in range(8):
        mod.enforce_exact(em,[B[x][a] for x in range(50)],8-len(hn[a]),f"degree_new_{a}")
    mod.enforce_exact(em,[-r for r in R.values()],2,"deleted_count")
    mod.enforce_exact(em,list(A.values()),4,"added_count")
    coverage = {"old_old":0,"old_new":0,"new_new":0}
    for x,y in combinations(range(58),2):
        if edge(x,y) is True or any(edge(x,z) is True and edge(z,y) is True for z in range(58)):
            continue
        direct = edge(x,y)
        terms = [] if direct is False else [direct]
        for z in range(58):
            a,b = edge(x,z),edge(z,y)
            if a is False or b is False:
                continue
            if a is True:
                terms.append(b)
            elif b is True:
                terms.append(a)
            else:
                q = em.new_var("two_path")
                mod.add_iff_and(em,q,a,b)
                terms.append(q)
        assert not any(q is True or q is False for q in terms)
        em.add_clause(*terms)
        coverage["old_old" if y<50 else ("old_new" if x<50 else "new_new")] += 1
    em.finish()
    after_children = resource.getrusage(resource.RUSAGE_CHILDREN)
    dump(OUT / "encoding.json",dict(n=58,auxiliary_catalog_type=6,auxiliary_edges=sorted(H),
         retained_variables={f"{x},{y}":q for (x,y),q in R.items()},
         addition_variables={f"{x},{y}":q for (x,y),q in A.items()},attachment_variables=B,
         deleted_count=2,added_count=4,normalization=[],additional_structural_constraints=[],
         primary_variables=175+1050+400,variables=em.variable_count,clauses=em.clause_count,
         coverage_clauses=coverage,seed_independent_check=seedcheck,
         preparation_parent_cpu_seconds=time.process_time()-prep_cpu,
         preparation_BFS_child_cpu_seconds=after_children.ru_utime+after_children.ru_stime-before_children.ru_utime-before_children.ru_stime,
         preparation_wall_seconds=time.monotonic()-prep_wall,
         scope="All placements of two original HS deletions and four original-nonedge additions, with all 400 attachments free and H fixed to the type6 representative. No old labels are normalized."))
    seconds = 10
    cmd = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"),"--lrat","-t",str(seconds),str(OUT/"input.cnf"),str(OUT/"proof.lrat")]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE,(128*1024**2,128*1024**2))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = time.monotonic()
    with (OUT / "solver.log").open("w") as log:
        try:
            rc = subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=seconds+5,preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(status={10:"SAT_CANDIDATE",20:"RAW_UNSAT",0:"UNKNOWN",-9:"CPU_LIMIT",-24:"CPU_LIMIT",-25:"OUTPUT_LIMIT",None:"WALL_LIMIT"}.get(rc,"PROCESS_FAILURE"),
                  exit_code=rc,cpu_budget_seconds=seconds,
                  cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-started,command=cmd,
                  variables=em.variable_count,clauses=em.clause_count,attempt=1,
                  proof_checked=False,retained_solver_state=False)
    if rc == 10:
        vals = {abs(q):q>0 for line in (OUT/"solver.log").read_text().splitlines() if line.startswith("v ") for q in map(int,line.split()[1:]) if q}
        kept = [e for e,q in R.items() if vals[q]]
        added = [e for e,q in A.items() if vals[q]]
        attachments = [[a for a,q in enumerate(row) if vals[q]] for row in B]
        graph = sorted(kept+added+[(50+a,50+b) for a,b in H]+[(x,50+a) for x,row in enumerate(attachments) for a in row])
        path = OUT/"candidate.json"
        dump(path,dict(n=58,edges=graph,old_deletions=sorted(original-set(kept)),old_additions=added,auxiliary_edges=sorted(H),attachments=attachments))
        path.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x,y in graph))
        result["independent_graph_check"] = json.loads(verify(path))
    if rc == 20:
        checkcmd = [str(ROOT/".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"),"--no-trim",str(OUT/"input.cnf"),str(OUT/"proof.lrat")]
        checked = subprocess.run(checkcmd,capture_output=True,text=True,timeout=30)
        (OUT/"certificate_check.log").write_text(checked.stdout+checked.stderr)
        ok = checked.returncode == 20 and "s VERIFIED" in checked.stdout.splitlines()
        result["certificate_check"] = dict(command=checkcmd,exit_code=checked.returncode,verified=ok)
        result["proof_checked"] = ok
        if ok:
            result["status"] = "CHECKED_UNSAT"
    dump(OUT/"result.json",result)
    print(json.dumps(result))


if __name__ == "__main__":
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    main()
