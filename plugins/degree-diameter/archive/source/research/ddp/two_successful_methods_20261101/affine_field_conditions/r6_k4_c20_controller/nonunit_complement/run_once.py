#!/usr/bin/env python3
"""Only the disjoint anchor5/nonunit domain; at most five additional CPU seconds."""
import csv
import json
import os
from pathlib import Path
import resource
import subprocess
import time

here = Path(__file__).resolve().parent
os.chdir(here)
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
start_self = time.process_time()
start_children = resource.getrusage(resource.RUSAGE_CHILDREN)
def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime - start_children.ru_utime - start_children.ru_stime

compiled = subprocess.run(["g++", "-std=c++17", "-O3", "-o", "search", "search.cpp"], capture_output=True, text=True)
(here / "COMPILE.log").write_text(compiled.stdout + compiled.stderr)
compile_cpu = child_cpu()
if compiled.returncode:
    raise SystemExit(compiled.returncode)
remaining = 4.8 - child_cpu() - (time.process_time() - start_self)
if remaining <= 0:
    raise SystemExit("Compilation exhausted the new five-second allowance")
run = subprocess.run(["./search", str(remaining)], capture_output=True, text=True)
(here / "SEARCH.log").write_text(run.stdout + run.stderr)
if run.returncode:
    raise SystemExit(run.returncode)
result = json.loads((here / "RAW_RESULT.json").read_text())
if result["status"] == "PASS":
    shifts = dict(zip([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], result["last_considered_shifts"]))
    def step(v, p):
        i, z = divmod(v, 20)
        j = i ^ (p % 3 + 1)
        if p >= 3:
            z = (z + (1 if i < j else -1) * shifts[tuple(sorted((i,j)))]) % 20
        return 20 * j + z
    ports = [[step(u,p) for p in range(6)] for u in range(80)]
    with (here / "PORT_TABLE.tsv").open("w") as f:
        f.write("vertex\tbase\tdeck\tp0\tp1\tp2\tp3\tp4\tp5\n")
        for u,row in enumerate(ports):
            assert len(set(row)) == 6
            f.write("\t".join(map(str,[u,u//20,u%20,*row]))+"\n")
    with (here / "controller.edges").open("w") as f:
        for u,row in enumerate(ports):
            for p,v in enumerate(row):
                assert ports[v][p] == u
                if u < v:
                    f.write(f"{u} {v}\n")
    with (here / "TRIANGLES.tsv").open("w") as f:
        f.write("a\tb\tc\n")
        for a in range(80):
            for b in ports[a]:
                if b <= a:
                    continue
                for c in ports[b]:
                    if c > b and c in ports[a]:
                        f.write(f"{a}\t{b}\t{c}\n")
    count = 0
    with (here / "NB3_WITNESSES.tsv").open("w") as f:
        f.write("source\ttarget\tp1\tp2\tp3\tv1\tv2\tv3\n")
        for row in csv.DictReader((here / "CLASS_WITNESSES.tsv").open(), delimiter="\t"):
            i,j,r = (int(row[k]) for k in ("root_base","target_base","residue"))
            ps = [int(row[f"p{k}"]) for k in (1,2,3)]
            assert ps[0]!=ps[1] and ps[1]!=ps[2]
            for z in range(20):
                u,v = 20*i+z,20*j+(z+r)%20
                w1=ports[u][ps[0]]
                w2=ports[w1][ps[1]]
                w3=ports[w2][ps[2]]
                assert w3==v and (u==v or v not in ports[u])
                f.write("\t".join(map(str,[u,v,*ps,w1,w2,w3]))+"\n")
                count += 1
    assert count==5920
result.update({"compile_CPU_seconds": compile_cpu,
               "additional_total_CPU_seconds": child_cpu()+time.process_time()-start_self,
               "additional_CPU_limit_seconds":5,
               "original_total_CPU_limit_seconds":30,
               "inherited_prior_CPU_seconds":1.094645045,
               "workers":1,"original_anchor1_search_rerun":False,
               "word_coefficient_source":"../WORD_COEFFICIENTS.tsv",
               "fiber_generated":False,"BFS_calls":0,"solver_calls":0,"Lean_calls":0,
               "old_graphs_revalidated":0})
result["combined_measured_CPU_seconds"] = result["inherited_prior_CPU_seconds"]+result["additional_total_CPU_seconds"]
(here / "RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
