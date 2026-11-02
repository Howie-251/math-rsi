"""Finite local domain for the coherent paired-core change 01 and 23.

The fixed routes through 4 and 5 in block 23 coincide. Its remaining
seven direct/internal routes therefore have a fixed exact support K.
Enumerate every matching M with M+P2*M+M*P3=K, using support exact cover.
No SAT, random search, or graph-neighborhood optimization.
"""
from pathlib import Path
import json
import time

from hs_augmentation import dump, verify
from petersen_four_fiber_reassembly import SOURCE, adjacency, matching, diagnostic

OUT = Path(__file__).with_name("petersen_paired_core_exchange_run")


def main():
    start = time.process_time()
    wall = time.monotonic()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"domain.json").exists(), "No unchanged rerun"
    edges = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    ns = adjacency(edges)
    f = {(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i != j}
    routes = {k:[f[k,3][f[2,k][u]-10*k]-30 for u in range(10)] for k in (0,1,4,5)}
    assert routes[4] == routes[5]
    assert all(len({routes[k][u] for k in (0,1,4)}) == 3 for u in range(10))
    p2 = [{v-20 for v in ns[20+u] if 20 <= v < 30} for u in range(10)]
    p3 = [{v-30 for v in ns[30+u] if 30 <= v < 40} for u in range(10)]
    allowed_cells = {(u,v) for u in range(10) for v in range(10)
                     if v not in {routes[k][u] for k in (0,1,4)}}
    assert len(allowed_cells) == 70
    placements = {}
    domains = []
    for u in range(10):
        domain = []
        for v in range(10):
            cells = {(u,v)} | {(w,v) for w in p2[u]} | {(u,w) for w in p3[v]}
            assert len(cells) == 7
            if cells <= allowed_cells:
                domain.append(v)
                placements[u,v] = sum(1 << (10*a+b) for a,b in cells)
        domains.append(domain)
    order = sorted(range(10),key=lambda u:(len(domains[u]),u))
    state = [-1]*10
    solutions = []
    nodes = 0
    complete = True
    def visit(depth,columns,covered):
        nonlocal nodes,complete
        nodes += 1
        if nodes % 4096 == 0 and time.process_time()-start >= 0.8:
            complete = False
            return
        if not complete:
            return
        if depth == 10:
            assert covered.bit_count() == 70
            solutions.append(state[:])
            return
        u = order[depth]
        for v in domains[u]:
            mask = placements[u,v]
            if not (columns>>v&1) and not (mask&covered):
                state[u] = v
                visit(depth+1,columns|(1<<v),covered|mask)
        state[u] = -1
    visit(0,0,0)
    original = [v-30 for v in f[2,3]]
    if complete:
        assert original in solutions
    report = dict(complete=complete,scope="All M23 with unchanged nine other interfaces except the K4 module; exact block23 equation only",
                  original_matching=original, fixed_routes=routes,
                  allowed_arrow_domains=domains, nodes=nodes,
                  solution_count=len(solutions), solutions=solutions,
                  nonoriginal_solution_count=sum(p!=original for p in solutions),
                  cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall,
                  cpu_budget_seconds=1,solver_runs=0)
    dump(OUT/"domain.json",report)
    print(json.dumps(report))


if __name__ == "__main__":
    main()
