"""Two concrete a5 old cores, one capacity flow per geometry, no SAT.

The endpoint ports cover both type-3 H bad pairs. Remaining singleton
ports are assigned by minimum-cost capacity flow, minimizing the exact
number of old-old coverage failures for those fixed endpoint ports.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import os
import resource
import time

import networkx as nx

from hs_augmentation import base, dump, verify

HERE = Path(__file__).parent
OUT = HERE / "hs58_a5_remaining_seeds_run"
H = [(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,2),(1,3),(1,4),(1,5)]
DESIGNS = {
    "adjacent": dict(D=[(0,1),(0,4)],
        A=[(1,45),(25,29),(30,34),(35,39),(40,44)],
        fixed_ports={0:[1,6,7], 1:[1], 4:[1,6]}),
    "cross": dict(D=[(0,1),(2,3)],
        A=[(25,26),(30,31),(35,36),(42,43),(47,48)],
        fixed_ports={0:[1,6], 1:[1,7], 2:[1,7], 3:[1,6]}),
}


def construct(name, spec, original, qns):
    begin_cpu, begin_wall = time.process_time(), time.monotonic()
    deleted, added = set(spec["D"]), set(spec["A"])
    assert deleted <= original and not (added & original)
    assert len(deleted) == 2 and len(added) == 5
    old_edges = (original-deleted) | added
    old = [set() for _ in range(50)]
    for x,y in old_edges:
        old[x].add(y); old[y].add(x)
    p = [8-len(s) for s in old]
    assert min(p) >= 0 and sum(p) == 44
    endpoints = sorted(set(x for e in deleted for x in e))
    zeros = [x for x in range(50) if p[x] == 0]
    zero_rows = [dict(vertex=x, neighbors=sorted(old[x]),
                      neighbor_port_counts=[p[y] for y in sorted(old[x])],
                      neighbor_port_sum=sum(p[y] for y in old[x])) for x in zeros]
    assert all(row["neighbor_port_sum"] >= 8 for row in zero_rows)
    assert not any(y in qns[x] for x,y in combinations(zeros,2))
    cross_edges = sorted(e for e in original-deleted if e[0] in endpoints and e[1] in endpoints)
    bad_old = [(x,y) for x,y in combinations(range(50),2)
               if y not in old[x] and not old[x]&old[y]]
    unavoidable = [e for e in bad_old if p[e[0]] == 0 or p[e[1]] == 0]
    fixed = {x:set(row) for x,row in spec["fixed_ports"].items()}
    assert set(fixed) == set(endpoints)
    assert all(len(row) == p[x] for x,row in fixed.items())
    hns = [set() for _ in range(8)]
    for a,b in H:
        hns[a].add(b); hns[b].add(a)
    hbad = [(a,b) for a,b in combinations(range(8),2)
            if b not in hns[a] and not hns[a]&hns[b]]
    assert all(any(a in row and b in row for row in fixed.values()) for a,b in hbad)
    capacities = [8-len(s) for s in hns]
    residual = [capacities[a]-sum(a in row for row in fixed.values()) for a in range(8)]
    assert min(residual) >= 0
    singletons = [x for x in range(50) if x not in fixed and p[x] == 1]
    assert all(p[x] <= 1 for x in range(50) if x not in fixed)
    assert sum(residual) == len(singletons)
    flow = nx.DiGraph()
    for a,cap in enumerate(residual):
        flow.add_node(("color",a), demand=cap)
    costs = {}
    obligations = {}
    for x in singletons:
        flow.add_node(("old",x), demand=-1)
        partners = [y if x==u else u for u,y in bad_old if x in (u,y)]
        assert all(y in fixed or p[y] == 0 for y in partners)
        obligations[x] = partners
        costs[x] = []
        for a in range(8):
            cost = sum(a not in fixed[y] for y in partners if y in fixed)
            costs[x].append(cost)
            flow.add_edge(("old",x), ("color",a), capacity=1, weight=cost)
    # One exact flow; no retry, no random assignment, no annealing.
    assigned = nx.min_cost_flow(flow)
    ports = [set(fixed.get(x,())) for x in range(50)]
    for x in singletons:
        ports[x] = {a for a in range(8) if assigned[("old",x)][("color",a)] == 1}
        assert len(ports[x]) == 1
    assert [len(row) for row in ports] == p
    assert [sum(a in row for row in ports) for a in range(8)] == capacities
    graph = sorted(old_edges | {(50+a,50+b) for a,b in H}
                   | {(x,50+a) for x,row in enumerate(ports) for a in row})
    assert len(graph) == 232
    path = OUT / f"{name}.seed.json"
    dump(path, dict(n=58, edges=graph, old_deletions=sorted(deleted), old_additions=sorted(added),
         auxiliary_catalog_type=3, auxiliary_edges=H, attachments=[sorted(s) for s in ports],
         fixed_endpoint_ports={str(x):sorted(row) for x,row in fixed.items()},
         scope="One explicit old core and endpoint-port design, with remaining singleton attachments chosen by one exact min-cost capacity flow; not a general completion search."))
    path.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x,y in graph))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    checked = json.loads(verify(path))
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    full = json.loads(path.with_suffix(".verification.json").read_text())
    assert full["degrees"] == [8]*58
    categories = Counter("old_old" if row["pair"][1]<50 else
                         "old_new" if row["pair"][0]<50 else "new_new" for row in full["bad_pairs"])
    remaining_old = [e for e in bad_old if not ports[e[0]]&ports[e[1]]]
    assert len(remaining_old) == categories.get("old_old",0)
    row_routes = []
    for x in range(50):
        direct = ports[x]
        via_old = set().union(*(ports[y] for y in old[x]))
        via_h = set().union(*(hns[a] for a in direct))
        row_routes.append(dict(vertex=x, direct=sorted(direct), via_old=sorted(via_old),
             via_H=sorted(via_h), missing=sorted(set(range(8))-direct-via_old-via_h)))
    report = dict(name=name, seed=path.name, graph_check=checked, bad_pair_categories=dict(categories),
        original_deletion_edges_confirmed=True, endpoint_cross_edges=cross_edges,
        zero_vertices=zeros, zero_induced_Q_edges=[], zero_port_capacity_rows=zero_rows,
        all_zero_neighbor_capacity_bounds_pass=True, old_pairs_not_covered_inside_M=bad_old,
        unavoidable_old_pairs_with_zero_endpoint=unavoidable,
        fixed_endpoint_old_pairs_unrepaired=[e for e in remaining_old if e[0] in fixed and e[1] in fixed],
        exact_singleton_flow_cost=nx.cost_of_flow(flow,assigned),
        remaining_old_bad_pairs=remaining_old, singleton_obligations=obligations,
        singleton_label_costs=costs, old_new_route_rows=row_routes,
        parent_cpu_seconds=time.process_time()-begin_cpu,
        independent_BFS_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-begin_wall)
    dump(OUT / f"{name}.analysis.json", report)
    return {k:v for k,v in report.items() if k in ("name","seed","graph_check","bad_pair_categories",
            "endpoint_cross_edges","unavoidable_old_pairs_with_zero_endpoint","exact_singleton_flow_cost",
            "remaining_old_bad_pairs","parent_cpu_seconds","independent_BFS_cpu_seconds","wall_seconds")}


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(5,6))
    cpu, wall = time.process_time(), time.monotonic()
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"result.json").exists(), "One construction per geometry, no unchanged rerun"
    original,qns = base()
    original = set(original)
    results = [construct(name,spec,original,qns) for name,spec in DESIGNS.items()]
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(scope="Two explicit a5 seeds for adjacent and cross-edge deletion geometries; one exact capacity flow each; no SAT or optimization runs.",
                  target_parent_cpu_seconds=5, parent_cpu_seconds=time.process_time()-cpu,
                  independent_BFS_cpu_seconds=after.ru_utime+after.ru_stime-child.ru_utime-child.ru_stime,
                  wall_seconds=time.monotonic()-wall, pinned_cpu=next(iter(os.sched_getaffinity(0))), results=results)
    dump(OUT/"result.json",result)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
