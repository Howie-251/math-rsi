#!/usr/bin/env python3
"""verify_witness.py -- standalone verifier for the graphs of the note
"Large graphs of diameter five from a duality of order four of the split Cayley
hexagon H(9)".

Python 3, standard library only. It shares no code with any program used to find
or build the graphs.

Run with no arguments to check everything that can be checked in a couple of
minutes and print ALL CHECKS PASS:

    python3 verify_witness.py

Add --full to run the all-vertex breadth-first sweep on each graph (exact, slow
in Python: roughly a quarter of an hour per graph), and --geometry to rebuild the
incidence graph of H(9) from its coordinate model, re-derive the duality tau from
tau.txt and re-fold it, reproducing graph_d10k5_n33397.edges edge for edge:

    python3 verify_witness.py --full --geometry

File formats. Each *.edges file is a header line "n m" followed by m lines "u v"
with 0 <= u,v < n. tau.txt is one line of 132860 integers: the image of each
vertex of the incidence graph of H(9) under the duality, points first.
"""
import hashlib
import lzma
import os
import random
import sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))

# name -> (file, n, max degree, diameter, sha256 of the file)
GRAPHS = {
    "F   (10,5) the fold of H(9)":
        ("graph_d10k5_n33397.edges", 33397, 10, 5,
         "e4d196fda251c5651392157d2ade06cfc4becd1635b725dcbdd759e045b20146"),
    "F*  (10,5) the 10-regular completion":
        ("graph_d10k5_n33397_regular.edges", 33397, 10, 5,
         "19c0fa13d1e18dc14a9de1afb11a68d1dd8623262f765be35480b3355de1fc48"),
    "F11 (11,5) F* with 1806 twins":
        ("graph_d11k5_n35203.edges", 35203, 11, 5,
         "1b89b4f1bea83b2d73940f1a7a95fcae7c931331febfa01f23ecad788d33af51"),
    "F12 (12,5) F* with 4770 twins":
        ("graph_d12k5_n38167.edges", 38167, 12, 5,
         "e361ed0eda3bea98262974d8a51eba2a6b8f333ceba5e906c4cd6b2aa8f2c00b"),
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


def check_supergraph(base_path, sup_path):
    """Every edge of base is an edge of sup, on the same first |base| vertices."""
    nb, ab = read_edges(base_path)
    ns, asu = read_edges(sup_path)
    sup = [set(a) for a in asu]
    for u in range(nb):
        for w in ab[u]:
            if w not in sup[u]:
                raise ValueError(f"edge ({u},{w}) of the base is missing")
    return nb, ns


def check_twins(base_path, pad_path):
    """Every vertex of pad beyond |base| is a twin of a base vertex (same neighbourhood,
    not adjacent to it), joined to no other new vertex; and pad induces base on 0..|base|-1."""
    nb, ab = read_edges(base_path)
    npad, ap = read_edges(pad_path)
    base_nbr = {}
    for v in range(nb):
        base_nbr.setdefault(frozenset(ab[v]), []).append(v)
    for u in range(nb):
        induced = frozenset(x for x in ap[u] if x < nb)
        if induced != frozenset(ab[u]):
            raise ValueError(f"the padding changed the base at vertex {u}")
    for v in range(nb, npad):
        s = frozenset(ap[v])
        if any(x >= nb for x in s):
            raise ValueError(f"new vertex {v} is joined to another new vertex")
        if s not in base_nbr:
            raise ValueError(f"new vertex {v} is not a twin of any base vertex")
    return npad - nb


def rebuild_from_geometry():
    """Rebuild the incidence graph of H(9) from the coordinate model, check tau, fold,
    and compare with graph_d10k5_n33397.edges. Stdlib only; a few minutes."""
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

    # orbits, in the order the banked file uses: by smallest member
    orbit_of = [-1] * n
    reps = []
    for u in range(n):
        if orbit_of[u] < 0:
            i = len(reps)
            reps.append(u)
            x = u
            while orbit_of[x] < 0:
                orbit_of[x] = i
                x = tau[x]
    norb = len(reps)
    if norb != 33397:
        raise ValueError(f"the fold has {norb} vertices, expected 33397")
    qe = set()
    for u in range(n):
        for w in adj[u]:
            a, b = orbit_of[u], orbit_of[w]
            if a != b:
                qe.add((min(a, b), max(a, b)))
    nb, ab = read_edges(os.path.join(HERE, "graph_d10k5_n33397.edges"))
    banked = set((min(u, w), max(u, w)) for u in range(nb) for w in ab[u])
    if qe != banked:
        raise ValueError(f"the fold differs from the shipped edge list "
                         f"({len(qe)} vs {len(banked)} edges)")
    return norb, len(qe)


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
    print("verifying the graphs of the duality-fold note")
    if not full:
        print(f"  (sampling {SAMPLE_SOURCES} sources per graph; pass --full for the "
              f"all-vertex sweep)")
    results = {}
    for name, (fn, n, d, k, sha) in GRAPHS.items():
        path = os.path.join(HERE, fn)
        if sha is not None:
            got = sha256(path)
            assert got == sha, f"{fn}: sha256 {got} != {sha}"
        r = verify(path, d, k, full=full)
        assert r["n"] == n, f"{fn}: n = {r['n']}, expected {n}"
        assert r["maxdeg"] <= d, f"{fn}: max degree {r['maxdeg']} > {d}"
        assert r["diameter"] == k, f"{fn}: diameter {r['diameter']} != {k}"
        assert set(r["ecc_hist"]) == {k}, f"{fn}: eccentricities {r['ecc_hist']}"
        results[fn] = r
        print(f"  {name}: n = {r['n']}, m = {r['m']}, degrees "
              f"{r['mindeg']}..{r['maxdeg']}, every eccentricity {k} over "
              f"{r['sources']} sources"
              + ("" if sha is None else ", sha256 pinned"))

    base = os.path.join(HERE, "graph_d10k5_n33397.edges")
    reg = os.path.join(HERE, "graph_d10k5_n33397_regular.edges")
    check_supergraph(base, reg)
    print("  F* contains every edge of F and is 10-regular")
    for fn in ("graph_d11k5_n35203.edges", "graph_d12k5_n38167.edges"):
        c = check_twins(reg, os.path.join(HERE, fn))
        print(f"  {fn}: {c} added vertices, each a twin of a vertex of F*, "
              f"F* induced unchanged")

    if geom:
        print("  rebuilding H(9) from its coordinate model (a few minutes) ...")
        norb, m = rebuild_from_geometry()
        print(f"  H(9) checked, tau checked, fold reproduces the shipped F "
              f"({norb} vertices, {m} edges)")

    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
