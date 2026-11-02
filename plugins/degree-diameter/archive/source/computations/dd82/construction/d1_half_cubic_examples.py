#!/usr/bin/env python3
"""Explicit 30-vertex half graphs; exact checks, no graph search.

The integer witnesses were obtained from a one-off numerical eigensystem
inspection. Their rejection below uses only integer arithmetic.
"""
import json
import os
from pathlib import Path
import resource
import time
from collections import deque
from itertools import combinations


def perfect_matchings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for b in xs[1:]:
        rest = tuple(x for x in xs if x != a and x != b)
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


def adj_from_edges(edges):
    adj = [set() for _ in range(30)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def stats(edges, colors=None, witness=None):
    edges = sorted(set(tuple(sorted(e)) for e in edges))
    adj = adj_from_edges(edges)
    assert all(len(a) == 3 for a in adj)
    dist = []
    girth = 31
    for s in range(30):
        d = [-1] * 30
        p = [-1] * 30
        d[s] = 0
        todo = deque([s])
        while todo:
            u = todo.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    p[v] = u
                    todo.append(v)
                elif p[u] != v:
                    girth = min(girth, d[u] + d[v] + 1)
        dist.append(d)
    out = {"n": 30, "edges": edges, "degree": 3,
           "connected": all(d >= 0 for d in dist[0]),
           "diameter": max(map(max, dist)), "girth": girth}
    if colors is not None:
        valid = all(sorted(colors[v] for v in adj[u]) == [0, 1, 2]
                    for u in range(30))
        out["quotient_J3_coloring"] = colors
        out["quotient_J3_checked"] = valid
        assert valid
    if witness is not None:
        cw = [sum(witness[v] for v in adj[u]) for u in range(30)]
        # w^T(7I+J-C^2-C)w, using symmetry of C.
        value = (7 * sum(x*x for x in witness) + sum(witness)**2
                 - sum(x*x for x in cw)
                 - sum(x*y for x, y in zip(witness, cw)))
        out["integer_witness"] = witness
        out["witness_sum"] = sum(witness)
        out["gram_quadratic_form"] = value
        assert sum(witness) == 0 and value < 0
    return out


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    if hasattr(os, "sched_getaffinity"):
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    start = time.process_time()
    witnesses = {
        2: [0,12,21,27,29,25,17,6,-6,-17,-25,-29,-27,-21,-12,
            0,9,17,21,22,20,13,5,-5,-13,-20,-22,-21,-17,-9],
        4: [2,-2,-23,-21,0,-1,-13,2,22,13,1,15,21,-1,-13,
            15,18,-28,-24,22,10,-30,-5,35,5,-25,11,33,-11,-28],
        7: [-19,-15,2,18,22,11,-7,-21,-21,-7,11,22,18,2,-15,
            -29,-19,3,23,28,14,-9,-26,-26,-9,14,28,23,3,-19],
    }
    examples = {}
    for k, w in witnesses.items():
        edges = [(i, (i+1) % 15) for i in range(15)]
        edges += [(15+i, 15+(i+k) % 15) for i in range(15)]
        edges += [(i, 15+i) for i in range(15)]
        examples[f"GP(15,{k})"] = stats(edges, [i % 3 for i in range(15)]*2, w)
    duads = list(combinations(range(6), 2))
    synthemes = list(perfect_matchings(tuple(range(6))))
    assert len(duads) == len(synthemes) == 15
    edges = [(duads.index(d), 15+j) for j, s in enumerate(synthemes) for d in s]
    tc = stats(edges)
    tc["point_duads"] = duads
    tc["line_synthemes"] = synthemes
    tc["spectrum_by_analytic_incidence_proof"] = [[3,1],[2,9],[0,10],[-2,9],[-3,1]]
    gram_multiplicities = {25: 1}
    for eigenvalue, multiplicity in tc["spectrum_by_analytic_incidence_proof"][1:]:
        transformed = 7 - eigenvalue * eigenvalue - eigenvalue
        gram_multiplicities[transformed] = gram_multiplicities.get(transformed, 0) + multiplicity
    tc["gram_spectrum_by_analytic_incidence_proof"] = [[value, count] for value, count in gram_multiplicities.items()]
    assert sum(value * count for value, count in gram_multiplicities.items()) == 150
    tc["quotient_J3_impossible"] = "Analytic intersecting-duad proof in D1_HALF_CUBIC_OBLIGATION.md"
    examples["duad_syntheme_Tutte_Coxeter"] = tc
    output = {"scope": "Four explicit half graphs only; no graph enumeration or solver",
              "examples": examples, "cpu_seconds": time.process_time()-start,
              "cpu_limit_seconds": 10, "cpu_cores": 1}
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"output": str(path), "cpu_seconds": output["cpu_seconds"],
                     "checks": {k: {t: v[t] for t in ("girth", "diameter", "gram_quadratic_form") if t in v}
                                for k, v in examples.items()}}, indent=2))


if __name__ == "__main__":
    main()
