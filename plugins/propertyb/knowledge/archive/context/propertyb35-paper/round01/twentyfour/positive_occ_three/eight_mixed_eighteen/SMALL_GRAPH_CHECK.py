"""Five positive labels of sizes (3,4,4,4,4), exact small graph domain."""
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import json
import time

CAP = (3, 4, 4, 4, 4)
EDGES = tuple(combinations(range(5), 2))
INDEX = {e: i for i, e in enumerate(EDGES)}
PERMS = tuple((0,) + p for p in permutations(range(1, 5)))
DISJOINT = tuple(tuple(j for j in range(i) if not set(EDGES[i]) & set(EDGES[j])) for i in range(10))


def m2(g):
    return sum(g[i] * g[j] for i in range(10) for j in DISJOINT[i])


def primary():
    g, d = [0] * 10, [0] * 5
    out = set()

    def rec(i, e, m):
        if i == 10:
            if 2 <= e <= 7 and 1 <= m <= 2:
                out.add(tuple(g))
            return
        a, b = EDGES[i]
        inc = sum(g[j] for j in DISJOINT[i])
        for v in range(min(CAP[a] - d[a], CAP[b] - d[b], 7 - e) + 1):
            if m + v * inc > 2:
                break
            g[i] = v
            d[a] += v
            d[b] += v
            rec(i + 1, e + v, m + v * inc)
            d[a] -= v
            d[b] -= v
        g[i] = 0

    rec(0, 0, 0)
    return out


def independent():
    # Assign complete forward rows, and filter M2 only after completing a graph.
    g, d = [0] * 10, [0] * 5
    out = set()

    def rec(a):
        if a == 4:
            if 2 <= sum(g) <= 7 and 1 <= m2(g) <= 2:
                out.add(tuple(g))
            return
        js = tuple(range(a + 1, 5))
        for vals in product(*(range(min(CAP[a], CAP[b] - d[b]) + 1) for b in js)):
            if d[a] + sum(vals) > CAP[a] or sum(g) + sum(vals) > 7:
                continue
            for b, v in zip(js, vals):
                g[INDEX[a, b]] = v
                d[b] += v
            rec(a + 1)
            for b, v in zip(js, vals):
                g[INDEX[a, b]] = 0
                d[b] -= v

    rec(0)
    return out


def image(g, p):
    out = [0] * 10
    for (a, b), v in zip(EDGES, g):
        out[INDEX[tuple(sorted((p[a], p[b])))]] = v
    return tuple(out)


def count(g):
    sets, d, n = [set() for _ in range(5)], [0] * 5, 0
    for (a, b), v in zip(EDGES, g):
        d[a] += v
        d[b] += v
        for _ in range(v):
            sets[a].add(n)
            sets[b].add(n)
            n += 1
    for a in range(5):
        for _ in range(CAP[a] - d[a]):
            sets[a].add(n)
            n += 1
    assert n == 19 - sum(g) <= 17
    direct = sum(all(set(c) & a for a in sets) for c in combinations(range(n), 4))
    ie = 0
    for mask in range(32):
        union = set().union(*(sets[a] for a in range(5) if mask >> a & 1))
        left = n - len(union)
        ie += (-1) ** mask.bit_count() * (comb(left, 4) if left >= 4 else 0)
    assert ie == direct
    return dict(vector=g, E=sum(g), M2=m2(g), degrees=d, union_size=n,
                C4=direct, C4_IE=ie, sets=[sorted(a) for a in sets])


def main():
    start = time.process_time()
    dom = primary()
    other = independent()
    assert dom == other
    left = set(dom)
    rows = []
    while left:
        g = min(left)
        orbit = {image(g, p) for p in PERMS}
        assert orbit <= dom
        rows.append(dict(count(g), orbit_size=len(orbit)))
        left -= orbit
    result = dict(status="PASS", sizes=CAP, edge_order=EDGES,
                  domain="capacity (3,4,4,4,4), 2<=E<=7, 1<=M2<=2, group S4 fixing label 0",
                  labelled_count=len(dom), orbit_count=len(rows),
                  minimum_C4=min(r["C4"] for r in rows), rows=rows,
                  process_seconds=time.process_time()-start)
    assert sum(r["orbit_size"] for r in rows) == len(dom)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}))
    print("minimizers", [r for r in rows if r["C4"] == result["minimum_C4"]])


if __name__ == "__main__":
    main()
