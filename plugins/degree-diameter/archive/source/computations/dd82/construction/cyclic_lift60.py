#!/usr/bin/env python3
"""Finite Z20 three-orbit voltage design diagnostic; no unrestricted graph search.

The companion proof excludes all quotient patterns. Here we reproduce the
degree/capacity screen and exhaust the residual (0,3,3;4,4,1) design after the
two orbit gauges put C12={0} and 0 in C01. Every retained design is expanded.
"""
import itertools
import json
import math
import time
from pathlib import Path

P = 20
ALL = set(range(P))
OUT = Path(__file__).with_suffix("")


def add(a, b):
    return {(x + y) % P for x in a for y in b}


def neg(a):
    return {(-x) % P for x in a}


def capacity_screen():
    # For a=2r+e: internal sums have <=1+2r^2+2re residues.
    g = {a: min(P, 1 + a + 2 * (a // 2) ** 2 +
                2 * (a // 2) * (a % 2)) for a in range(9)}
    kept = []
    examined = 0
    for a in itertools.combinations_with_replacement(range(9), 3):
        twice = [8-a[0]-a[1]+a[2], 8-a[0]-a[2]+a[1],
                 8-a[1]-a[2]+a[0]]
        if any(x < 0 or x % 2 for x in twice):
            continue
        c01, c02, c12 = (x // 2 for x in twice)
        c = [[0, c01, c02], [c01, 0, c12], [c02, c12, 0]]
        examined += 1
        if any(g[a[i]] + sum(min(19, c[i][j]*(c[i][j]-1))
                            for j in range(3) if i != j) < P
               for i in range(3)):
            continue
        if any(c[i][j]*(1+a[i]+a[j]) + c[i][3-i-j]*c[j][3-i-j] < P
               for i in range(3) for j in range(i+1, 3)):
            continue
        kept.append(dict(internal_degrees=a, cross_sizes=[c01, c02, c12]))
    assert [tuple(x["internal_degrees"]) for x in kept] == [(0,0,0),(0,1,1),(0,3,3)]
    return dict(internal_radius_upper_bounds=g, integer_quotients_examined=examined,
                surviving_quotients=kept)


def full_design(a, b, x, y):
    offsets = [[set(), x, y], [neg(x), {a,10,(-a)%P}, {0}],
               [neg(y), {0}, {b,10,(-b)%P}]]
    missing = []
    weighted_bad_pairs = 0
    for i in range(3):
        for j in range(i, 3):
            reached = set(offsets[i][j])
            if i == j:
                reached.add(0)
            for k in range(3):
                reached |= add(offsets[i][k], offsets[k][j])
            bad = sorted(ALL - reached)
            missing.append(dict(orbits=[i,j], missing_offsets=bad))
            weighted_bad_pairs += len(bad) * (10 if i == j else 20)
    edges = set()
    for i in range(3):
        for j in range(3):
            for t in range(P):
                for s in offsets[i][j]:
                    u,v = i*P+t, j*P+(t+s)%P
                    assert u != v
                    edges.add(tuple(sorted((u,v))))
    assert len(edges) == 240
    return dict(n=60, edges=sorted(edges), parameters=dict(a=a,b=b,
                C01=sorted(x),C02=sorted(y),C12=[0]),
                voltage_bad_pair_count=weighted_bad_pairs, missing_offsets=missing)


def main():
    start = time.process_time()
    result = dict(modulus=P, scope="three equal cyclic orbits; residual 033 exact design",
                  capacity_screen=capacity_screen())
    count = 0
    first_cover = 0
    both_cover = 0
    histogram = {}
    pairs = {}
    best = None
    for a in range(1,10):
        s1 = {0,10,a,(-a)%P}
        for rest in itertools.combinations(range(1,P),3):
            x = {0,*rest}
            count += 1
            xs = add(x,s1)
            if len(xs) != 16:
                continue
            first_cover += 1
            y = ALL-xs
            for b in range(1,10):
                s2 = {0,10,b,(-b)%P}
                ys = add(y,s2)
                if len(ys) != 16 or ys & x:
                    continue
                both_cover += 1
                key = f"{a},{b}"
                pairs[key] = pairs.get(key,0)+1
                obj = full_design(a,b,x,y)
                score = obj["voltage_bad_pair_count"]
                histogram[str(score)] = histogram.get(str(score),0)+1
                assert set([4,8,12,16]) <= set(obj["missing_offsets"][0]["missing_offsets"])
                if best is None or score < best["voltage_bad_pair_count"]:
                    best = obj
    result.update(normalized_a_X_cases=count, first_exact_cross_cover=first_cover,
                  both_exact_cross_covers=both_cover, parameter_counts=pairs,
                  full_graph_bad_pair_histogram=histogram,
                  cpu_seconds=time.process_time()-start,
                  conclusion="No target in the residual family; analytic proof excludes all three quotients.")
    assert set(pairs) == {"2,4","4,2","6,8","8,6"}
    assert best is not None and best["voltage_bad_pair_count"] > 0
    path = OUT.with_name(OUT.name+".best.edges.json")
    path.write_text(json.dumps(best,indent=2)+"\n")
    result["best_candidate_file"] = path.name
    result["best_parameters"] = best["parameters"]
    result["best_bad_pair_count"] = best["voltage_bad_pair_count"]
    OUT.with_suffix(".results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
