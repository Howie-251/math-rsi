"""One bounded internal-Petersen assembly, with saved complete candidates."""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

from hs_augmentation import dump, verify
from petersen_four_fiber_reassembly import diagnostic

HERE=Path(__file__).resolve().parent
OUT=HERE/"petersen_internal_reassembly_run"
SOURCE=HERE/"petersen_four_fiber_reassembly_run/seed.edges"
OUT.mkdir(exist_ok=True)
assert not (OUT/"resources.json").exists(), "No unchanged rerun"
start=time.monotonic()
parent=time.process_time()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
command=[str(HERE/"petersen_internal_reassembly.bin"),str(SOURCE),str(OUT)]
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(7,7))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
r=subprocess.run(command,capture_output=True,text=True,preexec_fn=limits,timeout=8)
(OUT/"search.log").write_text(r.stdout+r.stderr)
after_search=resource.getrusage(resource.RUSAGE_CHILDREN)
assert r.returncode==0
search=json.loads((OUT/"search.json").read_text())
source_rows=[list(map(int,line.split())) for line in SOURCE.read_text().splitlines()]
assert source_rows[0]==[60,240]
original={tuple(e) for e in source_rows[1:]}
checked=[]
unique=[]
for path in sorted(OUT.glob("*.json")):
    data=json.loads(path.read_text())
    if "edges" not in data or not isinstance(data["edges"],list):continue
    edges=[tuple(e) for e in data["edges"]]
    identical=next((entry for entry in unique if entry[0]==edges),None)
    if identical is None:
        brief=json.loads(verify(path))
        full=json.loads(path.with_suffix(".verification.json").read_text())
        diag=diagnostic(edges)
        unique.append((edges,path.name,full,diag))
        method="independent BFS of expanded edges"
    else:
        _,name,full,diag=identical
        dump(path.with_suffix(".verification.json"),full)
        brief={k:v for k,v in full.items() if k not in ("degrees","bad_pairs")}
        method=f"same full edge list as {name}; reuse its independent BFS"
    assert full["n"]==60 and full["edges"]==240 and full["degrees"]==[8]*60
    dump(path.with_suffix(".diagnostic.json"),diag)
    edit=dict(source=str(SOURCE),removed_edges=sorted(original-set(edges)),added_edges=sorted(set(edges)-original),
              internal_fibers_changed=sorted({u//10 for u,v in original^set(edges)}),
              external_matching_edges_unchanged=all(u//10==v//10 for u,v in original^set(edges)))
    assert edit["external_matching_edges_unchanged"]
    dump(path.with_suffix(".edits.json"),edit)
    checked.append(dict(file=path.name,method=method,result=brief))
after=resource.getrusage(resource.RUSAGE_CHILDREN)
result=dict(source=str(SOURCE),scope="Fixed 97-bad seed's fifteen matching interfaces and P2/P3; screen all labeled P0/P1 against both fixed boundary fibers, then coupled P4/P5 preserving exact45 only if both first domains survive",
            command=command,exit_code=r.returncode,search=search,
            search_child_cpu_seconds=after_search.ru_utime+after_search.ru_stime-before.ru_utime-before.ru_stime,
            verification_child_cpu_seconds=after.ru_utime+after.ru_stime-after_search.ru_utime-after_search.ru_stime,
            parent_cpu_seconds=time.process_time()-parent,wall_seconds=time.monotonic()-start,
            total_cpu_budget_seconds=10,solver_runs=0,unique_expanded_graphs_checked=len(unique),checks=checked,
            skipped_initial_proposal="P4/P5-only was not run: it leaves existing 02/03/12/13 bad blocks unchanged")
result["p1_boundary_screen_started"]=any(json.loads(line)["fiber"]==1 for line in (OUT/"boundary_domains.jsonl").read_text().splitlines())
result["coupled45_stage_started"]="boundary_domain" not in search["stop_reason"]
dump(OUT/"resources.json",result)
print(json.dumps(result))
