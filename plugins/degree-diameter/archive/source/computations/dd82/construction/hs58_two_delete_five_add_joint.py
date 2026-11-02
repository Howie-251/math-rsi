"""One joint a=5 construction attempt: all 1050 additions and 400 ports.

Only the two original deletions and the auxiliary H are fixed. No old
addition or attachment from the complete seed is frozen or normalized.
"""
from itertools import combinations
import importlib.util
import json
import os
import resource
import subprocess
import sys
import time

from hs_augmentation import ROOT, ARCHIVE, base, dump, verify

OUT = ROOT / "computations/dd82/construction/hs58_two_delete_five_add_joint_run"
SEED = ROOT / "computations/dd82/construction/hs58_two_delete_five_add_switch_run/type14.old_covered.json"


def main():
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "input.cnf").exists(), "One attempt, no unchanged rerun"
    prep_cpu, prep_wall = time.process_time(), time.monotonic()
    seed = json.loads(SEED.read_text())
    original, _ = base()
    original = set(original)
    deleted = {tuple(e) for e in seed["old_deletions"]}
    retained = original - deleted
    H = {tuple(e) for e in seed["auxiliary_edges"]}
    assert len(deleted) == 2 and len(H) == 10
    hns = [set() for _ in range(8)]
    oldns = [set() for _ in range(50)]
    for x, y in retained:
        oldns[x].add(y); oldns[y].add(x)
    for a, b in H:
        hns[a].add(b); hns[b].add(a)
    spec = importlib.util.spec_from_file_location("hs58_a5_cardinality", ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    em = mod.CNFEmitter(OUT / "input.cnf")
    additions = {(x, y): em.new_var("old_addition") for x, y in combinations(range(50), 2)
                 if (x, y) not in original}
    B = [[em.new_var("attachment") for a in range(8)] for x in range(50)]

    def edge(x, y):
        if x == y:
            return False
        if x > y:
            x, y = y, x
        if y < 50:
            if (x, y) in retained:
                return True
            return additions.get((x, y), False)
        if x < 50:
            return B[x][y-50]
        return (x-50, y-50) in H

    def conjunction(a, b):
        if a is False or b is False:
            return False
        if a is True:
            return b
        if b is True:
            return a
        q = em.new_var("two_path")
        mod.add_iff_and(em, q, a, b)
        return q

    for x in range(50):
        incident = [q for (u, v), q in additions.items() if x in (u, v)]
        mod.enforce_exact(em, incident + B[x], 8-len(oldns[x]), f"old_degree_{x}")
    for a in range(8):
        mod.enforce_exact(em, [B[x][a] for x in range(50)], 8-len(hns[a]), f"new_degree_{a}")
    mod.enforce_exact(em, list(additions.values()), 5, "total_additions")
    coverage = {"old_old": 0, "old_new": 0, "new_new": 0}
    fixed_covered = 0
    for x, y in combinations(range(58), 2):
        xy = edge(x, y)
        # Skip precisely pairs already covered using fixed edges alone.
        if xy is True or any(edge(x, z) is True and edge(z, y) is True for z in range(58)):
            fixed_covered += 1
            continue
        terms = [xy] if xy is not False else []
        for z in range(58):
            q = conjunction(edge(x, z), edge(z, y))
            if q is not False:
                assert q is not True
                terms.append(q)
        em.add_clause(*terms)
        key = "old_old" if y < 50 else ("old_new" if x < 50 else "new_new")
        coverage[key] += 1
    em.finish()
    dump(OUT / "encoding.json", dict(n=58, HS_edges=sorted(original),
         fixed_deletions=sorted(deleted), fixed_auxiliary_edges=sorted(H),
         auxiliary_catalog_type=14, seed=str(SEED),
         addition_variables={f"{x},{y}": q for (x,y),q in additions.items()},
         attachment_variables=B, addition_count=5, normalization=[],
         primary_variables=len(additions)+400, variables=em.variable_count,
         clauses=em.clause_count, coverage_clauses=coverage,
         pairs_covered_by_fixed_edges=fixed_covered,
         scope="Every 58-point target with this exact HS labeling, D={(0,1),(10,11)} and this labeled H of a5 catalog type14; all five old additions and all 400 attachments remain free.",
         encoding_cpu_seconds=time.process_time()-prep_cpu,
         encoding_wall_seconds=time.monotonic()-prep_wall))
    seconds = 20
    cmd = [str(ROOT / ".tools/lean-4.24.0-linux/bin/cadical"), "--lrat", "-t", str(seconds),
           str(OUT / "input.cnf"), str(OUT / "proof.lrat")]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds))
        resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE, (128*1024**2, 128*1024**2))
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with (OUT / "solver.log").open("w") as f:
        try:
            rc = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT,
                                timeout=seconds+5, preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(status={10:"SAT_CANDIDATE",20:"RAW_UNSAT",0:"UNKNOWN",-9:"CPU_LIMIT",-24:"CPU_LIMIT",-25:"OUTPUT_LIMIT",None:"WALL_LIMIT"}.get(rc,"PROCESS_FAILURE"),
                  exit_code=rc, cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-start, cpu_budget_seconds=seconds,
                  command=cmd, variables=em.variable_count, clauses=em.clause_count,
                  attempt=1, proof_checked=False, retained_solver_state=False)
    if rc == 10:
        vals = {abs(q):q > 0 for line in (OUT / "solver.log").read_text().splitlines()
                if line.startswith("v ") for q in map(int,line.split()[1:]) if q}
        chosen = [e for e,q in additions.items() if vals[q]]
        ports = [[a for a,q in enumerate(row) if vals[q]] for row in B]
        graph = sorted(list(retained)+chosen+[(50+a,50+b) for a,b in H]
                       +[(x,50+a) for x,row in enumerate(ports) for a in row])
        path = OUT / "candidate.json"
        dump(path,dict(n=58, edges=graph, old_deletions=sorted(deleted), old_additions=chosen,
                       auxiliary_edges=sorted(H), attachments=ports))
        path.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x,y in graph))
        result["independent_graph_check"] = json.loads(verify(path))
    if rc == 20:
        cmdcheck = [str(ROOT / ".tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim"), "--no-trim",
                    str(OUT / "input.cnf"), str(OUT / "proof.lrat")]
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        startcheck = time.monotonic()
        checked = subprocess.run(cmdcheck, capture_output=True, text=True, timeout=30)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        (OUT / "certificate_check.log").write_text(checked.stdout+checked.stderr)
        ok = checked.returncode == 20 and "s VERIFIED" in checked.stdout.splitlines()
        result["certificate_check"] = dict(command=cmdcheck, exit_code=checked.returncode, verified=ok,
            cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
            wall_seconds=time.monotonic()-startcheck)
        result["proof_checked"] = ok
        if ok:
            result["status"] = "CHECKED_UNSAT"
    dump(OUT / "result.json", result)
    print(json.dumps(result))


if __name__ == "__main__":
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    main()
