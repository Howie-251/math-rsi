#!/usr/bin/env python3
"""Reuse six saved automorphisms for adjacent/cross deletion orbits only."""
from collections import deque
from itertools import combinations
from pathlib import Path
import json
import os
import resource
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'hs58_remaining_deletion_orbits_run'
SOURCE=HERE/'hs58_no_cross_deletion_orbit_run/generators.json'

def main():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(2,3))
    start_cpu,start_wall=time.process_time(),time.monotonic()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'result.json').exists(), 'No unchanged rerun'
    saved=json.loads(SOURCE.read_text())
    edges=[tuple(e) for e in saved['HS_edges']]
    edge_id={e:i for i,e in enumerate(edges)}
    ns=[set() for _ in range(50)]
    for x,y in edges:
        ns[x].add(y);ns[y].add(x)
    generators=saved['generators']
    assert len(generators)==6
    actions=[]
    for g in generators:
        assert g['bijection_verified'] and g['image_edge_set_equals_Q']
        p=g['permutation']
        actions.append([edge_id[tuple(sorted((p[x],p[y])))] for x,y in edges])
    domains={'adjacent':set(),'cross':set()}
    for i,j in combinations(range(len(edges)),2):
        e,f=edges[i],edges[j]
        if set(e)&set(f):
            domains['adjacent'].add((i,j))
        elif any(v in ns[u] for u in e for v in f):
            domains['cross'].add((i,j))
    seeds={'adjacent':((0,1),(0,4)),'cross':((0,1),(2,3))}
    reports={}
    for name in ['adjacent','cross']:
        seed=tuple(sorted(edge_id[e] for e in seeds[name]))
        assert seed in domains[name]
        states=[seed];index={seed:0};tree=[dict(parent=None,generator=None)]
        cursor=0
        while cursor<len(states):
            i,j=states[cursor]
            for gid,action in enumerate(actions):
                target=tuple(sorted((action[i],action[j])))
                assert target in domains[name]
                if target not in index:
                    index[target]=len(states)
                    states.append(target)
                    tree.append(dict(parent=cursor,generator=gid))
            cursor+=1
        complete=set(states)==domains[name]
        (OUT/(name+'.orbit.json')).write_text(json.dumps(dict(
            seed_deletions=seeds[name],generator_source=str(SOURCE),
            states=[dict(deletions=[edges[i],edges[j]],**tree[k])
                    for k,(i,j) in enumerate(states)]),indent=2)+'\n')
        reports[name]=dict(seed_deletions=seeds[name],direct_domain_size=len(domains[name]),
            orbit_size=len(states),missing_domain_size=len(domains[name]-set(states)),
            every_orbit_member_in_domain=set(states)<=domains[name],
            orbit_closed_under_saved_generators=True,complete=complete)
    result=dict(complete=all(r['complete'] for r in reports.values()),orbits=reports,
        generator_source=str(SOURCE),reused_generator_count=len(actions),
        new_automorphism_searches=0,no_cross_orbit_repeated=False,
        cpu_seconds=time.process_time()-start_cpu,wall_seconds=time.monotonic()-start_wall,
        cpu_limit_seconds=2,threads=1)
    (OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    usage=resource.getrusage(resource.RUSAGE_SELF)
    resources=dict(user_cpu_seconds=usage.ru_utime,system_cpu_seconds=usage.ru_stime,
        total_process_cpu_seconds=usage.ru_utime+usage.ru_stime,
        wall_since_main_seconds=time.monotonic()-start_wall,
        maximum_resident_kib=usage.ru_maxrss,threads=1,cpu_limits_seconds=[2,3])
    (OUT/'resources.json').write_text(json.dumps(resources,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print(json.dumps(resources,indent=2))

if __name__=='__main__':
    main()
