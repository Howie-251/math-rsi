"""Two explicit A6/S3 actions: complete undirected orbital-union domains.

Composition p*q means apply q first. Vertices are left cosets gH and the
action is left multiplication. Undirected orbitals are computed directly
on unordered pairs, avoiding any assumption that a directed orbital is
self-paired. No classification of order-six subgroups is assumed.
"""
from collections import Counter,deque
from itertools import combinations,permutations
from pathlib import Path
import argparse
import json
import os
import resource
import time

from hs_augmentation import ROOT,dump,verify

OUT=ROOT/"computations/dd82/construction/coset60_a6_s3_run"
IDENTITY=tuple(range(6))


def multiply(p,q):
    return tuple(p[q[i]] for i in range(6))


def cycles(*items):
    p=list(range(6))
    for cycle in items:
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):p[a]=b
    return tuple(p)


def closure(generators):
    found={IDENTITY};todo=[IDENTITY]
    while todo:
        p=todo.pop()
        for g in generators:
            q=multiply(g,p)
            if q not in found:found.add(q);todo.append(q)
    return found


def prepare():
    start,cpu_start=time.monotonic(),time.process_time()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"preparation.json").exists(),"Do not repeat this preparation"
    group={p for p in permutations(range(6))
           if sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2==0}
    generators=[cycles((0,1,k)) for k in range(2,6)]
    assert len(group)==360 and closure(generators)==group
    involution=cycles((0,1),(3,4))
    subgroups=[("H1",[cycles((0,1,2)),involution]),
               ("H2",[cycles((0,1,2),(3,4,5)),involution])]
    models=[]
    for name,hs_generators in subgroups:
        subgroup=closure(hs_generators)
        assert len(subgroup)==6 and subgroup<=group
        remaining=set(group);cosets=[];representatives=[];coset_of={}
        while remaining:
            representative=min(remaining)
            coset={multiply(representative,h) for h in subgroup}
            assert len(coset)==6 and coset<=remaining
            index=len(cosets)
            for element in coset:coset_of[element]=index
            cosets.append(sorted(coset));representatives.append(representative)
            remaining-=coset
        assert len(cosets)==60 and coset_of[IDENTITY]==0
        actions=[[coset_of[multiply(g,r)] for r in representatives] for g in generators]
        assert all(sorted(a)==list(range(60)) for a in actions)
        # Check action independence of the representative in every coset.
        assert all(coset_of[multiply(g,r)]==actions[k][i]
                   for k,g in enumerate(generators) for i,c in enumerate(cosets) for r in c)
        unused=set(combinations(range(60),2));orbitals=[]
        while unused:
            seed=min(unused);orbit={seed};todo=[seed]
            while todo:
                u,v=todo.pop()
                for action in actions:
                    image=tuple(sorted((action[u],action[v])))
                    if image not in orbit:orbit.add(image);todo.append(image)
            assert orbit<=unused
            unused-=orbit
            degrees=[0]*60
            for u,v in orbit:degrees[u]+=1;degrees[v]+=1
            valency=degrees[0]
            assert valency>0 and degrees==[valency]*60 and len(orbit)==30*valency
            orbitals.append(dict(index=len(orbitals),seed=seed,valency=valency,
                                 edges=sorted(orbit),root_neighbors=sorted(v for u,v in orbit if u==0)))
        assert sum(o["valency"] for o in orbitals)==59
        assert sum(len(o["edges"]) for o in orbitals)==1770
        ways=[1]+[0]*8
        for orbital in orbitals:
            weight=orbital["valency"]
            for d in range(8,weight-1,-1):ways[d]+=ways[d-weight]
        model=dict(name=name,group_order=360,subgroup_generators=hs_generators,
                   subgroup_elements=sorted(subgroup),subgroup_order=6,coset_count=60,
                   cosets=cosets,representatives=representatives,action_generators=actions,
                   orbitals=orbitals,valency_eight_unions=ways[8],degree_subset_counts=ways)
        models.append(model)
        dump(OUT/(name+".model.json"),model)
    report=dict(group="A6 on six letters",group_order=360,group_generators=generators,
        complete=True,models=[dict(name=m["name"],subgroup_order=m["subgroup_order"],
                cosets=m["coset_count"],undirected_orbitals=len(m["orbitals"]),
                valencies=[o["valency"] for o in m["orbitals"]],
                valency_eight_unions=m["valency_eight_unions"],degree_subset_counts=m["degree_subset_counts"])
                for m in models],
        total_valency_eight_unions=sum(m["valency_eight_unions"] for m in models),
        cpu_seconds=time.process_time()-cpu_start,wall_seconds=time.monotonic()-start,
        cpu_budget_seconds=5,search_launched=False,
        scope="Exactly the two supplied order-six subgroups and their A6 left actions on gH. No subgroup classification or nonisomorphism assumption.")
    dump(OUT/"preparation.json",report);print(json.dumps(report),flush=True)


def degree_eight_subsets(weights):
    def visit(index,remaining,chosen):
        if remaining==0:
            yield tuple(chosen);return
        if index==len(weights):return
        if weights[index]<=remaining:
            chosen.append(index)
            yield from visit(index+1,remaining-weights[index],chosen)
            chosen.pop()
        yield from visit(index+1,remaining,chosen)
    yield from visit(0,8,[])


def root_bfs(rows):
    distance=[-1]*60;distance[0]=0;queue=deque([0])
    while queue:
        u=queue.popleft();neighbors=rows[u]
        while neighbors:
            bit=neighbors&-neighbors;neighbors-=bit;v=bit.bit_length()-1
            if distance[v]<0:distance[v]=distance[u]+1;queue.append(v)
    return distance


def save_and_check(model,selected,rows,distance):
    target=OUT/model["name"];target.mkdir(exist_ok=True)
    edges=[(u,v) for u in range(60) for v in range(u+1,60) if rows[u]>>v&1]
    assert len(edges)==240 and all(row.bit_count()==8 for row in rows)
    root_bad=sum(d<0 or d>2 for d in distance)
    dump(target/"candidate.best.json",dict(n=60,edges=edges,group="A6",model=model["name"],
         selected_orbitals=selected,selected_valencies=[model["orbitals"][i]["valency"] for i in selected],
         root_distances=distance,root_bad_targets=root_bad,predicted_bad_pairs=30*root_bad,
         vertices="Coset index in the saved model's ordered gH list"))
    (target/"candidate.best.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in edges))
    checked=json.loads(verify(target/"candidate.best.json"))
    assert checked["n"]==60 and checked["edges"]==240 and checked["max_degree"]==8
    assert checked["bad_pair_count"]==30*root_bad
    return checked


def search():
    start,cpu_start=time.monotonic(),time.process_time()
    before_children=resource.getrusage(resource.RUSAGE_CHILDREN)
    preparation=json.loads((OUT/"preparation.json").read_text())
    assert not (OUT/"search.launch.json").exists(),"Exactly one orbital-union search episode"
    dump(OUT/"search.launch.json",dict(cpu_budget_seconds=30,models=[m["name"] for m in preparation["models"]],
                                      planned_unions=preparation["total_valency_eight_unions"]))
    reports=[];budget_stop=False;target_found=False
    for summary in preparation["models"]:
        model=json.loads((OUT/(summary["name"]+".model.json")).read_text())
        orbit_rows=[]
        for orbital in model["orbitals"]:
            rows=[0]*60
            for u,v in orbital["edges"]:rows[u]|=1<<v;rows[v]|=1<<u
            orbit_rows.append(rows)
        hist=Counter();best_bad=61;best_rows=None;best_selected=None;best_distance=None
        best_unions=[];count=0
        for selected in degree_eight_subsets([o["valency"] for o in model["orbitals"]]):
            if time.process_time()-cpu_start>=29:
                budget_stop=True;break
            rows=[0]*60
            for index in selected:
                for u in range(60):rows[u]|=orbit_rows[index][u]
            assert all(row.bit_count()==8 for row in rows)
            distances=root_bfs(rows)
            bad=sum(d<0 or d>2 for d in distances)
            count+=1;hist[bad]+=1
            if bad<best_bad:
                best_bad=bad;best_rows=rows;best_selected=selected;best_distance=distances;best_unions=[]
            if bad==best_bad:best_unions.append(selected)
            if bad==0:target_found=True;break
        complete=count==model["valency_eight_unions"]
        check=save_and_check(model,best_selected,best_rows,best_distance) if best_rows is not None else None
        report=dict(model=model["name"],expected_unions=model["valency_eight_unions"],
             evaluated_unions=count,complete=complete,
             root_bad_histogram=dict(sorted(hist.items())),minimum_root_bad_targets=best_bad if count else None,
             minimum_bad_pairs=30*best_bad if count else None,selected_best_union=best_selected,
             all_best_unions=best_unions,independent_best_graph_check=check)
        reports.append(report)
        dump(OUT/(model["name"]+".search.json"),report)
        print(json.dumps(report),flush=True)
        if budget_stop or target_found:break
    after_children=resource.getrusage(resource.RUSAGE_CHILDREN)
    resources=dict(complete=len(reports)==len(preparation["models"]) and all(r["complete"] for r in reports),
        target_found=target_found,budget_stop=budget_stop,
        evaluated_unions=sum(r["evaluated_unions"] for r in reports),
        expected_unions=preparation["total_valency_eight_unions"],
        model_summaries=[dict(model=r["model"],complete=r["complete"],evaluated_unions=r["evaluated_unions"],
                             minimum_bad_pairs=r["minimum_bad_pairs"]) for r in reports],
        search_parent_cpu_seconds=time.process_time()-cpu_start,
        independent_bfs_children_cpu_seconds=after_children.ru_utime+after_children.ru_stime-before_children.ru_utime-before_children.ru_stime,
        wall_seconds=time.monotonic()-start,cpu_budget_seconds=30,solver_calls=0,
        scope=preparation["scope"],subgroup_classification_claimed=False,
        action_nonisomorphism_claimed=False)
    dump(OUT/"search.resources.json",resources);print(json.dumps(resources),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("action",choices=["prepare","search"])
    args=parser.parse_args();pin=min(os.sched_getaffinity(0));os.sched_setaffinity(0,{pin})
    budget=5 if args.action=="prepare" else 30
    resource.setrlimit(resource.RLIMIT_CPU,(budget,budget+1))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    {"prepare":prepare,"search":search}[args.action]()
