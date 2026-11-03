"""One bounded complete palette run and independent BFS of all minima."""
from collections import Counter, deque
from pathlib import Path
import json
import os
import resource
import subprocess
import time

from hs_augmentation import dump

HERE=Path(__file__).resolve().parent
OUT=HERE/"petersen_binary_palette_run"
assert not (OUT/"resources.json").exists(), "No unchanged rerun"
wall=time.monotonic()
parent=time.process_time()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
command=[str(HERE/"petersen_binary_palette_search.bin"),str(OUT/"input.txt"),str(OUT)]
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(4,4))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
r=subprocess.run(command,capture_output=True,text=True,timeout=5,preexec_fn=limits)
(OUT/"search.log").write_text(r.stdout+r.stderr)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
assert r.returncode==0
search=json.loads((OUT/"search.json").read_text())
verify_cpu=time.process_time()
minima=OUT/"minima"
minima.mkdir(exist_ok=True)
checks=[]
with (OUT/"minimum_graphs.edges").open() as f:
    n,m,count=map(int,next(f).split())
    assert (n,m)==(60,240)
    for index in range(count):
        mask,claimed_bad,claimed_energy=map(int,next(f).split())
        raw=[tuple(map(int,next(f).split())) for _ in range(m)]
        assert len(set(raw))==m and all(0<=u<v<n for u,v in raw)
        ns=[set() for _ in range(n)]
        for u,v in raw:ns[u].add(v);ns[v].add(u)
        assert all(len(s)==8 for s in ns)
        bad=[]
        diameter=0
        for u in range(n):
            dist={u:0}
            queue=deque([u])
            while queue:
                x=queue.popleft()
                for y in ns[x]:
                    if y not in dist:
                        dist[y]=dist[x]+1
                        queue.append(y)
            for v in range(u+1,n):
                d=dist.get(v)
                if d is None or d>2:
                    bad.append(dict(pair=[u,v],distance=d,common_neighbors=sorted(ns[u]&ns[v])))
                if d is not None:diameter=max(diameter,d)
        assert len(bad)==claimed_bad
        energy=0
        for u in range(n):
            for v in range(u+1,n):
                b=len(ns[u]&ns[v])+int(v in ns[u])-1
                energy+=b*(b-1)//2
        assert energy==claimed_energy
        blocks=Counter(tuple(v//10 for v in row["pair"]) for row in bad)
        report=dict(mask=mask,n=n,edges=m,degrees=[8]*n,bad_pair_count=len(bad),
                    bad_pairs=bad,diameter=diameter,cycle_energy=energy,
                    bad_blocks=[dict(fibers=list(k),bad_pairs=v) for k,v in sorted(blocks.items())],
                    valid_target=not bad)
        dump(minima/f"mask{mask:05d}.json",dict(n=n,mask=mask,edges=raw))
        dump(minima/f"mask{mask:05d}.verification.json",report)
        checks.append({k:v for k,v in report.items() if k not in ("degrees","bad_pairs")})
    assert not f.read().strip()
assert len(checks)==search["saved_complete_graphs"]
dump(OUT/"independent_verification.json",dict(all_saved_graphs_checked=True,graphs=checks,
     bfs_cpu_seconds=time.process_time()-verify_cpu))
resources=dict(exit_code=r.returncode,command=command,complete=search["complete"],
               search_child_cpu_seconds=child_cpu,
               parent_and_bfs_cpu_seconds=time.process_time()-parent,
               wall_seconds=time.monotonic()-wall,
               computation_cpu_budget_seconds=5,
               actual_accounted_cpu_seconds=child_cpu+time.process_time()-parent,
               threads=1,solver_runs=0)
assert resources["actual_accounted_cpu_seconds"]<5
dump(OUT/"resources.json",resources)
print(json.dumps(dict(search_summary={k:v for k,v in search.items() if not k.endswith("histogram")},resources=resources)))
