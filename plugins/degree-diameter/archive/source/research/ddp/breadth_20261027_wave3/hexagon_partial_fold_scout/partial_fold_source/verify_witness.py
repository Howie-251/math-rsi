#!/usr/bin/env python3
"""verify_witness.py -- standalone verifier for the graphs of the paper
"Partial folds of the split Cayley hexagon H(9) and large graphs of diameter five".

Python 3, standard library only. It shares no code with any program used to find
or build the graphs.

Run with no arguments to check the three graphs (the pinned SHA-256 hash of each
edge list, simplicity, the maximum degree, and eccentricity 5 from a fixed sample
of sources) and print ALL CHECKS PASS:

    python3 verify_witness.py

Add --full to run breadth-first search from every vertex of each graph (exact,
slow in Python: roughly a quarter of an hour per graph; anc/allsrc.c does the same
in C), and --geometry to rebuild the incidence graph of H(9) from its coordinate
model, check that tau.txt is a duality of order four whose square fixes the 728
vertices of a subhexagon H(3), and rebuild every graph from its witness in
witnesses/, which must reproduce the shipped edge list edge for edge:

    python3 verify_witness.py --full --geometry

File formats. Each *.edges file is a header line "n m" followed by m lines "u v"
with 0 <= u,v < n. tau.txt is one line of 132860 integers: the image of each
vertex of the incidence graph of H(9) under the duality, points first. The
witness format is described in partial_fold() below.
"""
import hashlib
import json
import lzma
import os
import random
import sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))

# name -> (file, n, max degree, diameter, sha256 of the file)
GRAPHS = {
    "P11 (11,5) a twinned partial fold, delta = 1":
        ("graph_d11k5_n36563.edges", 36563, 11, 5,
         "e21ea4d9bc132d15d6ecdba0326873d07aac3c67192d7ca97d62dfaeebdc61ec"),
    "P12 (12,5) a twinned partial fold, delta = 2":
        ("graph_d12k5_n41699.edges", 41699, 12, 5,
         "3b2a59e4c6a56e5c3012b9fb453e64a72e420b7cdb5a131f4c03130810d97cc6"),
    "P13 (13,5) a twinned partial fold, delta = 3":
        ("graph_d13k5_n50750.edges", 50750, 13, 5,
         "dfc98d664dcdbd42b6732163d88e7c6ad799e3563fdc2a5d56592d0bfe5bdc60"),
}
# the twinned partial folds: shipped edge list -> its witness in witnesses/ (rebuilt by --geometry)
PARTIAL = {
    "graph_d11k5_n36563.edges": "pf_d11_k5_n36563.json",
    "graph_d12k5_n41699.edges": "pf_d12_k5_n41699.json",
    "graph_d13k5_n50750.edges": "pf_d13_k5_n50750.json",
}
SAMPLE_SOURCES = 300


def opentext(path):
    """Open a data file, transparently decompressing the shipped .xz form. The
    hashes pinned below are of the UNCOMPRESSED bytes either way."""
    if os.path.exists(path):
        return open(path)
    if os.path.exists(path + ".xz"):
        return lzma.open(path + ".xz", "rt")
    raise FileNotFoundError(path)


def sha256(path):
    h = hashlib.sha256()
    with opentext(path) as f:
        for chunk in iter(lambda: f.read(1 << 20), ""):
            h.update(chunk.encode())
    return h.hexdigest()


def read_edges(path):
    """-> (n, adj as a list of lists). Rejects self-loops and repeated edges."""
    with opentext(path) as f:
        n, m = (int(x) for x in f.readline().split())
        adj = [[] for _ in range(n)]
        seen = set()
        count = 0
        for line in f:
            u, v = (int(x) for x in line.split())
            if u == v:
                raise ValueError(f"self-loop at {u}")
            key = (u, v) if u < v else (v, u)
            if key in seen:
                raise ValueError(f"repeated edge {key}")
            seen.add(key)
            adj[u].append(v)
            adj[v].append(u)
            count += 1
    if count != m:
        raise ValueError(f"header says {m} edges, found {count}")
    if max(max(a) for a in adj if a) != n - 1:
        raise ValueError("vertex ids are not exactly 0..n-1")
    return n, adj


def ecc(adj, s, n):
    dist = [-1] * n
    dist[s] = 0
    q = deque([s])
    seen = 1
    e = 0
    while q:
        u = q.popleft()
        d = dist[u] + 1
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = d
                if d > e:
                    e = d
                seen += 1
                q.append(w)
    if seen != n:
        raise ValueError(f"graph is disconnected from source {s}")
    return e


def verify(path, d, k, full=False, quiet=True):
    """Check one edge list. Returns a dict of what was measured."""
    n, adj = read_edges(path)
    maxdeg = max(len(a) for a in adj)
    mindeg = min(len(a) for a in adj)
    if full:
        srcs = range(n)
    else:
        rng = random.Random(20260917)
        srcs = [0, n - 1] + [rng.randrange(n) for _ in range(SAMPLE_SOURCES - 2)]
    hist = {}
    for s in srcs:
        e = ecc(adj, s, n)
        hist[e] = hist.get(e, 0) + 1
    diameter = max(hist)
    return {"n": n, "m": sum(len(a) for a in adj) // 2, "maxdeg": maxdeg,
            "mindeg": mindeg, "diameter": diameter, "ecc_hist": hist,
            "sources": len(list(srcs)), "adj": adj}


def build_hexagon():
    """The incidence graph of H(9) from its coordinate model, checked to be a generalized
    hexagon of order (9,9): (number of points, adjacency lists), points 0..66429 first and
    then the lines, in the order tau.txt uses. Stdlib only; a few minutes."""
    import itertools
    p, k = 3, 2
    q = 9
    poly = [1, 0, 1]          # x^2 + 1, irreducible over F_3
    add = [[0] * q for _ in range(q)]
    mul = [[0] * q for _ in range(q)]
    dig = [[(a // p ** i) % p for i in range(k)] for a in range(q)]
    und = lambda dd: sum(x * p ** i for i, x in enumerate(dd))
    for a in range(q):
        for b in range(q):
            add[a][b] = und([(x + y) % p for x, y in zip(dig[a], dig[b])])
            pr = [0] * (2 * k - 1)
            for i, x in enumerate(dig[a]):
                if x:
                    for j, y in enumerate(dig[b]):
                        pr[i + j] = (pr[i + j] + x * y) % p
            for deg in range(2 * k - 2, k - 1, -1):
                c = pr[deg]
                if c:
                    for t in range(k + 1):
                        pr[deg - k + t] = (pr[deg - k + t] - c * poly[t]) % p
            mul[a][b] = und(pr[:k])
    neg = [und([(-x) % p for x in dig[a]]) for a in range(q)]
    inv = [0] * q
    for a in range(1, q):
        inv[a] = next(b for b in range(1, q) if mul[a][b] == 1)

    def norm(v):
        for x in v:
            if x:
                return tuple(mul[inv[x]][y] for y in v)
        return v

    def proj_points(dim):
        out = []
        for lead in range(dim):
            for tail in itertools.product(range(q), repeat=dim - lead - 1):
                out.append((0,) * lead + (1,) + tail)
        return out

    pts = []
    for v in proj_points(7):
        s = add[add[mul[v[0]][v[4]]][mul[v[1]][v[5]]]][mul[v[2]][v[6]]]
        if s == mul[v[3]][v[3]]:
            pts.append(v)
    idx = {v: i for i, v in enumerate(pts)}
    assert len(pts) == 66430, len(pts)

    def nullspace(rows, nc):
        rows = [list(r) for r in rows]
        piv = []
        r = 0
        for c in range(nc):
            pr_ = next((i for i in range(r, len(rows)) if rows[i][c]), None)
            if pr_ is None:
                continue
            rows[r], rows[pr_] = rows[pr_], rows[r]
            iv = inv[rows[r][c]]
            rows[r] = [mul[iv][x] for x in rows[r]]
            for i in range(len(rows)):
                if i != r and rows[i][c]:
                    f = rows[i][c]
                    rows[i] = [add[x][neg[mul[f][y]]] for x, y in zip(rows[i], rows[r])]
            piv.append(c)
            r += 1
        free = [c for c in range(nc) if c not in piv]
        basis = []
        for fc in free:
            v = [0] * nc
            v[fc] = 1
            for i, c in enumerate(piv):
                v[c] = neg[rows[i][fc]]
            basis.append(v)
        return basis

    def span_line(x, y):
        L = {norm(x), norm(y)}
        for lam in range(1, q):
            L.add(norm(tuple(add[a][mul[lam][b]] for a, b in zip(x, y))))
        return frozenset(L)

    EQ = [((1, 2), (3, 4)), ((5, 4), (3, 2)), ((2, 0), (3, 5)),
          ((6, 5), (3, 0)), ((0, 1), (3, 6)), ((4, 6), (3, 1))]
    lines = set()
    for x in pts:
        rows = []
        for (a, b), (c, dd) in EQ:
            row = [0] * 7
            row[b] = add[row[b]][x[a]]
            row[a] = add[row[a]][neg[x[b]]]
            row[dd] = add[row[dd]][neg[x[c]]]
            row[c] = add[row[c]][x[dd]]
            rows.append(row)
        basis = nullspace(rows, 7)
        if len(basis) != 3:
            continue
        plane = set()
        for co in itertools.product(range(q), repeat=3):
            if any(co):
                v = [0] * 7
                for c, bv in zip(co, basis):
                    if c:
                        v = [add[a][mul[c][b]] for a, b in zip(v, bv)]
                plane.add(norm(tuple(v)))
        plane.discard(norm(x))
        seen = set()
        for y in plane:
            if y in seen:
                continue
            L = span_line(x, y)
            seen |= L
            lines.add(L)
    lines = sorted(lines, key=lambda L: sorted(idx[v] for v in L))
    assert len(lines) == 66430, len(lines)
    npts = len(pts)
    n = 2 * npts
    adj = [[] for _ in range(n)]
    for li, L in enumerate(lines):
        v = npts + li
        for x in L:
            adj[idx[x]].append(v)
            adj[v].append(idx[x])
    assert all(len(a) == 10 for a in adj), "H(9) incidence graph is not 10-regular"

    # Moore-bipartite layer profile: girth 12 and diameter 6
    for s in (0, npts):
        dist = [-1] * n
        dist[s] = 0
        qq = deque([s])
        lay = [0] * 8
        lay[0] = 1
        while qq:
            u = qq.popleft()
            for w in adj[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    lay[dist[w]] += 1
                    qq.append(w)
        if lay[:7] != [1, 10, 90, 810, 7290, 65610, 59049] or lay[7] != 0:
            raise ValueError(f"not a generalized hexagon of order (9,9): layers {lay}")
    return npts, adj


def load_tau(npts, adj):
    """tau.txt, checked: a duality of H(9) of order exactly 4 whose square fixes the 728
    vertices of a subhexagon H(3)."""
    n = 2 * npts
    with opentext(os.path.join(HERE, "tau.txt")) as f:
        tau = [int(x) for x in f.read().split()]
    if sorted(tau) != list(range(n)):
        raise ValueError("tau is not a permutation")
    for u in range(n):
        if sorted(tau[w] for w in adj[u]) != sorted(adj[tau[u]]):
            raise ValueError("tau is not an automorphism")
    if not all((tau[u] >= npts) == (u < npts) for u in range(n)):
        raise ValueError("tau does not swap the two parts")
    t2 = [tau[tau[u]] for u in range(n)]
    t4 = [t2[t2[u]] for u in range(n)]
    if t2 == list(range(n)) or t4 != list(range(n)):
        raise ValueError("tau does not have order exactly 4")
    fix2 = [u for u in range(n) if t2[u] == u]
    if len(fix2) != 728:
        raise ValueError(f"|Fix(tau^2)| = {len(fix2)}, expected 728")
    fs = set(fix2)
    if any(sum(1 for w in adj[u] if w in fs) != 4 for u in fix2):
        raise ValueError("Fix(tau^2) does not induce the incidence graph of H(3)")
    return tau


def hexbits(hexs, m):
    """The first m bits of a bit string written in hex, most significant bit first."""
    out = []
    for byte in bytes.fromhex(hexs):
        out.extend((byte >> s) & 1 for s in range(7, -1, -1))
    if len(out) < m:
        raise ValueError(f"bit string has {len(out)} bits, need {m}")
    return out[:m]


def partial_fold(npts, adj, tau, W):
    """Rebuild a twinned partial fold (Section "Partial folds") from its witness W.

    Q'' is the set of tau-orbits of vertices of the incidence graph that contain no point of
    H(3), in the order of their least members (33,033 of them, one per generic fiber
    {p, tau^2 p}). W["split"] and W["colour"] are bit strings over Q''. With eps(p) the colour
    of p's fiber when that fiber is split and 0 otherwise, sigma(p) = tau(p) if eps(p) = 1 and
    tau^-1(p) if eps(p) = 0, and G_eps joins p to every other point of the line sigma(p). A
    fiber that is not split is merged into one vertex. Vertices are labelled by their least
    point and numbered in label order. Then every H(3) point h is blown up into
    1 + W["h3_twins"][i] pairwise non-adjacent copies (h the i-th H(3) point in increasing
    order), each joined to every copy of every neighbour; h keeps its number and the new copies
    are numbered from n on, by h and then by copy. Finally vertex n + i is added as a twin of
    W["pad"][i]: joined to the neighbours of that vertex and to nothing new.
    Returns (number of vertices, set of edges (u, v) with u < v)."""
    N = npts
    tinv = [0] * (2 * N)
    for x in range(2 * N):
        tinv[tau[x]] = x
    least = [-1] * (2 * N)
    for x in range(2 * N):
        if least[x] < 0:
            orb = [x]
            y = tau[x]
            while y != x:
                orb.append(y)
                y = tau[y]
            m = min(orb)
            for y in orb:
                least[y] = m
    h3 = [tau[tau[p]] == p for p in range(N)]
    h3orb = {least[p] for p in range(N) if h3[p]}
    q2 = [r for r in sorted(set(least)) if r not in h3orb]
    if len(q2) != 33033:
        raise ValueError(f"Q'' has {len(q2)} vertices, expected 33033")
    q2i = {r: i for i, r in enumerate(q2)}
    sp = hexbits(W["split"], len(q2))
    col = hexbits(W["colour"], len(q2))
    eps, split = [0] * N, [False] * N
    for p in range(N):
        if not h3[p]:
            v = q2i[least[p]]
            split[p] = bool(sp[v])
            eps[p] = col[v] if sp[v] else 0
    nbrs = [set() for _ in range(N)]
    for p in range(N):
        line = tau[p] if eps[p] else tinv[p]
        if line < N:
            raise ValueError(f"sigma({p}) is not a line")
        for x in adj[line]:
            if x != p:
                nbrs[p].add(x)
                nbrs[x].add(p)
    label = [p if (h3[p] or split[p]) else min(p, tau[tau[p]]) for p in range(N)]
    num = {lab: i for i, lab in enumerate(sorted(set(label)))}
    n = len(num)
    if n != 33397 + sum(sp):
        raise ValueError(f"the partial fold has {n} vertices, expected 33397 + {sum(sp)}")
    E = set()
    for p in range(N):
        u = num[label[p]]
        for x in nbrs[p]:
            w = num[label[x]]
            if u == w:
                raise ValueError(f"an edge inside a merged fiber at point {p}")
            E.add((min(u, w), max(u, w)))
    hpts = [p for p in range(N) if h3[p]]
    tw = W["h3_twins"]
    if len(tw) != len(hpts) or not all(0 <= c for c in tw):
        raise ValueError("h3_twins does not give one count per H(3) point")
    mult = [1] * n
    for c, p in zip(tw, hpts):
        mult[num[p]] += c
    copies, nxt = [], n
    for x in range(n):
        copies.append([x] + list(range(nxt, nxt + mult[x] - 1)))
        nxt += mult[x] - 1
    E = {(min(a, b), max(a, b)) for u, w in E for a in copies[u] for b in copies[w]}
    n = nxt
    if W.get("pad"):
        nb = [[] for _ in range(n)]
        for u, w in E:
            nb[u].append(w)
            nb[w].append(u)
        for i, v in enumerate(W["pad"]):
            E.update((x, n + i) for x in nb[v])
        n += len(W["pad"])
    return n, E


def check_one():
    """--check PATH N D K [--full]: verify a graph this file does not ship, which is what
    a new candidate needs. Same verify() the shipped graphs go through, so the candidate is
    held to the same standard, and anc/allsrc.c is a second implementation to agree with."""
    i = sys.argv.index("--check")
    try:
        path, n, d, k = sys.argv[i + 1], int(sys.argv[i + 2]), int(sys.argv[i + 3]), int(sys.argv[i + 4])
    except (IndexError, ValueError):
        sys.exit("usage: verify_witness.py --check PATH N D K [--full]")
    r = verify(path, d, k, full="--full" in sys.argv)
    bad = []
    if r["n"] != n:
        bad.append(f"n = {r['n']}, claimed {n}")
    if r["maxdeg"] > d:
        bad.append(f"max degree {r['maxdeg']} > {d}")
    if r["diameter"] > k:
        bad.append(f"diameter {r['diameter']} > {k}")
    print(f"  {os.path.basename(path)}: n = {r['n']}, m = {r['m']}, degrees "
          f"{r['mindeg']}..{r['maxdeg']}, diameter {r['diameter']}, "
          f"eccentricities {r['ecc_hist']} over {r['sources']} sources")
    if bad:
        sys.exit("CLAIM FAILS: " + "; ".join(bad))
    print(f"CLAIM HOLDS: n = {n}, maximum degree at most {d}, diameter at most {k}")
    print("  now run anc/allsrc.c on the same file and require it to agree")


def main():
    full = "--full" in sys.argv
    geom = "--geometry" in sys.argv
    if "--check" in sys.argv:
        return check_one()
    print("verifying the graphs of the partial-fold paper")
    if not full:
        print(f"  (sampling {SAMPLE_SOURCES} sources per graph; pass --full for the "
              f"all-vertex sweep)")
    for name, (fn, n, d, k, sha) in GRAPHS.items():
        path = os.path.join(HERE, fn)
        got = sha256(path)
        assert got == sha, f"{fn}: sha256 {got} != {sha}"
        r = verify(path, d, k, full=full)
        assert r["n"] == n, f"{fn}: n = {r['n']}, expected {n}"
        assert r["maxdeg"] <= d, f"{fn}: max degree {r['maxdeg']} > {d}"
        assert r["diameter"] == k, f"{fn}: diameter {r['diameter']} != {k}"
        assert set(r["ecc_hist"]) == {k}, f"{fn}: eccentricities {r['ecc_hist']}"
        print(f"  {name}: n = {r['n']}, m = {r['m']}, degrees "
              f"{r['mindeg']}..{r['maxdeg']}, every eccentricity {k} over "
              f"{r['sources']} sources, sha256 pinned")

    if geom:
        print("  rebuilding H(9) from its coordinate model (a few minutes) ...")
        npts, adj = build_hexagon()
        tau = load_tau(npts, adj)
        print("  H(9) checked (10-regular, layers of a generalized hexagon of order (9,9)); "
              "tau checked (a duality of order four, |Fix(tau^2)| = 728, inducing H(3))")
        for fn, wfile in PARTIAL.items():
            with open(os.path.join(HERE, "witnesses", wfile)) as f:
                W = json.load(f)
            d = next(g[2] for g in GRAPHS.values() if g[0] == fn)
            if W["delta"] != d - 10 or max(W["h3_twins"]) > W["delta"]:
                raise ValueError(f"{wfile}: delta {W['delta']} does not fit degree {d}")
            n, E = partial_fold(npts, adj, tau, W)
            ns, ash = read_edges(os.path.join(HERE, fn))
            shipped = {(u, w) for u in range(ns) for w in ash[u] if u < w}
            if n != ns or E != shipped:
                raise ValueError(f"{fn}: the rebuild from {wfile} differs from the shipped "
                                 f"edge list ({n} vs {ns} vertices, {len(E)} vs {len(shipped)} edges)")
            nsplit = sum(hexbits(W["split"], 33033))
            print(f"  {fn}: rebuilt from {wfile} ({nsplit} split fibers, "
                  f"{sum(W['h3_twins'])} copies of H(3) points, {len(W.get('pad', []))} further "
                  f"twins) edge for edge")

    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
