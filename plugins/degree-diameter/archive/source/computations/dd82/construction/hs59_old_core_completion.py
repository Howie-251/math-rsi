#!/usr/bin/env python3
"""Run the single finite 10-CPU-second completion and independently BFS records."""
from collections import Counter, deque
from pathlib import Path
import json
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'hs59_old_core_repair_run'
PREFIX=OUT/'completion'


def read_edges(path):
    lines=path.read_text().splitlines()
    n,m=map(int,lines[0].split())
    edges=[tuple(map(int,line.split())) for line in lines[1:]]
    assert len(edges)==m==len(set(edges))
    return n,edges


def verify(path, expected, original_source_edges, record):
    n,edges=read_edges(path)
    assert n==59 and len(edges)==236
    neighbors=[set() for _ in range(n)]
    for u,v in edges:
        assert 0<=u<v<n
        neighbors[u].add(v);neighbors[v].add(u)
    assert all(len(s)==8 for s in neighbors)
    orig=lambda v:v+(v>=41)
    original_edges={tuple(sorted((orig(u),orig(v)))) for u,v in edges}
    removed={(9,14),tuple(record['second_deleted_old_edge'])}
    removed.update(map(tuple,record['removed_auxiliary_edges']))
    added=set(map(tuple,record['added_old_new_edges']))
    assert removed<=original_source_edges and not added&original_source_edges
    assert original_edges==original_source_edges-removed|added
    old=set(range(40))|set(range(50,60))
    bad=[];diameter=0;counts=Counter()
    for root in range(n):
        dist={root:0};queue=deque([root])
        while queue:
            v=queue.popleft()
            for w in neighbors[v]:
                if w not in dist:dist[w]=dist[v]+1;queue.append(w)
        assert len(dist)==n
        diameter=max(diameter,max(dist.values()))
        for other in range(root+1,n):
            if dist[other]>2:
                u,v=orig(root),orig(other)
                kind='old_old' if u in old and v in old else 'new_new' if u not in old and v not in old else 'old_new'
                counts[kind]+=1
                bad.append(dict(pair=[u,v],distance=dist[other],kind=kind,
                    common_neighbors=sorted(orig(x) for x in neighbors[root]&neighbors[other]),
                    neighbors_u=sorted(orig(x) for x in neighbors[root]),
                    neighbors_v=sorted(orig(x) for x in neighbors[other])))
    assert len(bad)==expected
    result=dict(n=n,edges=len(edges),degrees=[len(s) for s in neighbors],diameter=diameter,
        bad_pair_count=len(bad),bad_pair_type_counts=dict(counts),
        bad_pairs_original_60_labels=bad,change_replay_verified=True,
        complete_original_label_edges=sorted(original_edges))
    path.with_suffix('.verification.json').write_text(json.dumps(result,indent=2)+'\n')
    return dict(file=str(path),bad_pairs=len(bad),diameter=diameter,bad_pair_type_counts=dict(counts))


def limits():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(10,10))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))


def main():
    assert not PREFIX.with_suffix('.json').exists(),'Do not rerun the completed family.'
    source=HERE/'twin59_neutral_component_run/component.path2.edges'
    command=[str(HERE/'hs59_old_core_completion.bin'),str(source),str(OUT/'completion_input.txt'),str(PREFIX)]
    started=time.monotonic()
    with PREFIX.with_suffix('.log').open('w') as log:
        p=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    resources=dict(command=command,exit_code=p.returncode,wall_seconds=time.monotonic()-started,
        cpu_seconds=usage.ru_utime+usage.ru_stime,max_rss_kib=usage.ru_maxrss,
        cpu_limit_seconds=10,threads=1)
    PREFIX.with_suffix('.resources.json').write_text(json.dumps(resources,indent=2)+'\n')
    assert p.returncode==0
    report=json.loads(PREFIX.with_suffix('.json').read_text())
    _,edges=read_edges(source)
    orig=lambda v:v+(v>=41)
    original={tuple(sorted((orig(u),orig(v)))) for u,v in edges}
    checked=[verify(Path(r['file']),r['bad_pairs'],original,r) for r in report['strict_best_records']]
    PREFIX.with_suffix('.verification.json').write_text(json.dumps(checked,indent=2)+'\n')
    print(json.dumps(dict(resources=resources,complete=report['complete'],valid=report['valid_full_candidates'],
        best=report['best_bad_pairs'],best_assignment_count=report['best_assignment_count'],checked=checked),indent=2))


if __name__=='__main__':main()
