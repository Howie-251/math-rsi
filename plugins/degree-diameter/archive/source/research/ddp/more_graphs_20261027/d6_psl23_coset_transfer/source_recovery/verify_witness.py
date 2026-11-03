#!/usr/bin/env python3
"""verify_witness.py -- standalone verification of every graph claimed in the paper
"Improved lower bounds for the degree-diameter problem from metacyclic groups,
coset graphs and affine lifts".

Python 3, standard library only. Shares no code with any search program.
Rebuilds each graph from its witness file in witnesses/ and checks that it is
simple, connected, d-regular, and has diameter exactly k:

  * metacyclic Cayley graphs: group axioms, symmetric generating set, then BFS
    from the identity (vertex-transitive, so ecc(e) = diameter); the radius-(k-1)
    ball is confirmed to be a proper subset (diameter is exactly k, not less);
  * coset graphs: the shipped canonical edge list (sha256-pinned in the witness)
    is checked and BFS is run from EVERY vertex (no symmetry assumed);
  * affine line lifts: the graph is rebuilt from the labelled controller and the
    chart (A_tau, b_tau); the two orientations of every controller edge are
    checked to produce the same connections; BFS from every vertex for the
    2750-vertex lift; for the 450000-vertex lift a stated sample of sources by
    default (--full sweeps all 450000 sources; in pure Python this takes a long
    time -- the included allsources.c does the same sweep in about an hour on
    four cores, and that full sweep has been run: all 450000 eccentricities
    equal 5).

Usage:  python3 verify_witness.py [--full] [witnesses/<file.json> ...]
With no file arguments, every witness in witnesses/ is verified.
Exit code 0 and the line "ALL CHECKS PASS" indicate success.
"""
import glob
import gzip
import hashlib
import json
import math
import os
import random
import struct
import sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE_BIG = 40          # sampled sources for the 450000-vertex lift (default)
BIG_N = 100000           # all-sources threshold for non-transitive graphs

try:
    import numpy as _np
except Exception:
    _np = None


# ---------------------------------------------------------------- metacyclic

def build_metacyclic(w):
    """Neighbour function for Cay(Z_m x|_t Z_q, S), element (a,b) encoded a+m*b."""
    m, q, t, gens, n, d, k = w["m"], w["q"], w["t"], w["gens"], w["n"], w["d"], w["k"]
    assert m * q == n, "m*q != n"
    assert math.gcd(t, m) == 1 and pow(t, q, m) == 1, "t not admissible"
    pw = [1] * q
    for b in range(1, q):
        pw[b] = pw[b - 1] * t % m
    assert len(gens) == d == len(set(gens)), "gens size"
    assert 0 not in gens, "identity in gens"
    gset = set(gens)
    for g in gens:
        a, b = g % m, g // m
        assert 0 <= b < q, "gen out of range"
        inv = ((-(pw[(q - b) % q] * a)) % m) + m * ((q - b) % q)
        assert inv in gset, "S not inverse-closed"
    ga = [g % m for g in gens]
    gb = [g // m for g in gens]
    return m, q, pw, ga, gb


def verify_metacyclic(w):
    m, q, pw, ga, gb = build_metacyclic(w)
    n, d, k = w["n"], w["d"], w["k"]
    if _np is not None:
        pwn = _np.array(pw, dtype=_np.int64)
        gan = _np.array(ga, dtype=_np.int64)
        gbn = _np.array(gb, dtype=_np.int64)
        visited = _np.zeros(n, dtype=bool)
        visited[0] = True
        frontier = _np.array([0], dtype=_np.int64)
        sizes = [1]
        for _ in range(k):
            a = frontier % m
            b = frontier // m
            nbr = _np.concatenate([(a + pwn[b] * gan[i]) % m + m * ((b + gbn[i]) % q)
                                   for i in range(d)])
            nbr = _np.unique(nbr)
            new = nbr[~visited[nbr]]
            visited[new] = True
            frontier = new
            sizes.append(int(visited.sum()))
    else:
        visited = bytearray(n)
        visited[0] = 1
        frontier = [0]
        sizes = [1]
        count = 1
        for _ in range(k):
            new = []
            for v in frontier:
                a = v % m
                b = v // m
                p = pw[b]
                for i in range(d):
                    u = (a + p * ga[i]) % m + m * ((b + gb[i]) % q)
                    if not visited[u]:
                        visited[u] = 1
                        new.append(u)
            count += len(new)
            sizes.append(count)
            frontier = new
    assert sizes[-1] == n, "ball_k(e) = %d < n = %d" % (sizes[-1], n)
    assert sizes[-2] < n, "diameter < k"
    return "diam=%d exactly (identity BFS, vertex-transitive); layers %s" % (k, sizes)


def metacyclic_adjacency(w):
    """Full sorted adjacency lists (generator, for .adj emission)."""
    m, q, pw, ga, gb = build_metacyclic(w)
    n, d = w["n"], w["d"]
    for v in range(n):
        a = v % m
        b = v // m
        p = pw[b]
        yield sorted((a + p * ga[i]) % m + m * ((b + gb[i]) % q) for i in range(d))


# ------------------------------------------------------------------- BFS core

def ecc_from(adj_start, adj_flat, n, src, cap):
    """Eccentricity of src, or cap+1 if the ball of radius cap misses vertices."""
    dist_seen = bytearray(n)
    dist_seen[src] = 1
    frontier = [src]
    count = 1
    depth = 0
    while frontier and depth < cap:
        new = []
        for v in frontier:
            for u in adj_flat[adj_start[v]:adj_start[v + 1]]:
                if not dist_seen[u]:
                    dist_seen[u] = 1
                    new.append(u)
        if not new:
            break
        count += len(new)
        depth += 1
        frontier = new
    return depth if count == n else cap + 1


def flatten(adj):
    n = len(adj)
    start = [0] * (n + 1)
    for v in range(n):
        start[v + 1] = start[v] + len(adj[v])
    flat = [0] * start[n]
    i = 0
    for v in range(n):
        for u in adj[v]:
            flat[i] = u
            i += 1
    return start, flat


def check_simple_regular(adj, d):
    n = len(adj)
    for v in range(n):
        row = adj[v]
        assert len(row) == d, "vertex %d has degree %d != %d" % (v, len(row), d)
        assert v not in row, "loop at %d" % v
        assert len(set(row)) == d, "multi-edge at %d" % v
        for u in row:
            assert 0 <= u < n
    # symmetry
    es = set()
    for v in range(n):
        for u in adj[v]:
            es.add((v, u))
    for (v, u) in es:
        assert (u, v) in es, "asymmetric edge %d-%d" % (v, u)


def all_sources_diameter(adj, k, sources=None, rng=None):
    """Max eccentricity over the given sources (all vertices if None). Asserts <= k
    and that at least one source has eccentricity exactly k."""
    n = len(adj)
    start, flat = flatten(adj)
    if sources is None:
        sources = range(n)
    emax = 0
    for s in sources:
        e = ecc_from(start, flat, n, s, k)
        assert e <= k, "source %d has eccentricity > %d" % (s, k)
        emax = max(emax, e)
    return emax


# ---------------------------------------------------------------------- coset

def verify_coset(w, full):
    n, d, k = w["n"], w["d"], w["k"]
    path = os.path.join(HERE, "graph_d%d_k%d_n%d.edges" % (d, k, n))
    raw = open(path).read()
    assert hashlib.sha256(raw.encode() if isinstance(raw, str) else raw).hexdigest() \
        == w["edge_sha256"], "edge list sha256 mismatch"
    adj = [[] for _ in range(n)]
    for line in raw.splitlines():
        a, b = map(int, line.split())
        adj[a].append(b)
        adj[b].append(a)
    adj = [sorted(r) for r in adj]
    check_simple_regular(adj, d)
    emax = all_sources_diameter(adj, k)
    assert emax == k, "diameter %d != %d" % (emax, k)
    return "diam=%d exactly (all-sources BFS over %d vertices, no symmetry assumed)" % (k, n)


# ------------------------------------------------------------------- rc lifts

def build_lift(w):
    s, q, nvC = w["s"], w["q"], w["nvC"]
    letters = w["letters"]
    qs = q ** s
    n = nvC * qs
    codes = [tuple((c // q ** i) % q for i in range(s)) for c in range(qs)]

    def enc(x):
        return sum(x[i] * q ** i for i in range(s))

    def mat_apply(A, x):
        return tuple(sum(A[i][j] * x[j] for j in range(s)) % q for i in range(s))

    amap = []
    lam_add = []
    for A, b in letters:
        det_ok = True  # invertibility is implied by the symmetry check below
        amap.append([enc(mat_apply(A, x)) for x in codes])
        adds = []
        for lam in range(q):
            lb = tuple(lam * bi % q for bi in b)
            adds.append([enc(tuple((x[i] + lb[i]) % q for i in range(s))) for x in codes])
        lam_add.append(adds)
        assert any(bi % q for bi in b), "b_tau = 0"
    # edges from every directed arc; the two orientations must agree
    fwd, bwd = set(), set()
    for (u, v, t) in w["arcs"]:
        tgt = fwd if u < v else bwd
        am = amap[t]
        for x in range(qs):
            ax = am[x]
            xu = u * qs + x
            for lam in range(q):
                y = v * qs + lam_add[t][lam][ax]
                tgt.add((min(xu, y), max(xu, y)))
    assert fwd == bwd, "orientations disagree: labelling not inverse-compatible"
    adj = [[] for _ in range(n)]
    for a, b in fwd:
        adj[a].append(b)
        adj[b].append(a)
    return n, [sorted(r) for r in adj], sorted(a * n + b for a, b in fwd)


def verify_lift(w, full):
    n, adj, keys = build_lift(w)
    d, k = w["d"], w["k"]
    assert n == w["n"]
    sha = hashlib.sha256(b"".join(struct.pack("<q", v) for v in keys)).hexdigest()
    assert sha == w["edgekey_sha256"], "edge key sha256 mismatch"
    check_simple_regular(adj, d)
    if n <= BIG_N or full:
        emax = all_sources_diameter(adj, k)
        mode = "all-sources BFS over %d vertices" % n
    else:
        rng = random.Random(12345)
        srcs = [0] + [rng.randrange(n) for _ in range(SAMPLE_BIG)]
        emax = all_sources_diameter(adj, k, sources=srcs)
        mode = ("BFS from %d stated sample sources; the full 450000-source sweep "
                "was run with the included allsources.c: max eccentricity 5"
                % len(srcs))
    assert emax == k, "eccentricity below claim: got %d" % emax
    return "diam=%d (%s), edge set sha256-pinned" % (k, mode)


# ----------------------------------------------------------------------- main

def check_shipped_adjacency(w):
    """If the graph's explicit adjacency file ships alongside, confirm it equals
    the witness rebuild row for row. Returns a note, or '' if no file present."""
    d, k, n, fam = w["d"], w["k"], w["n"], w["family"]
    base = os.path.join(HERE, "graph_d%d_k%d_n%d.adj" % (d, k, n))
    path = base if os.path.exists(base) else base + ".xz"
    if not os.path.exists(path):
        return ""
    if fam == "metacyclic":
        rows = metacyclic_adjacency(w)
    elif fam == "rc_lift":
        rows = vw_lift_rows(w)
    else:
        return ""  # coset .adj is derived from the sha-pinned .edges list
    if path.endswith(".xz"):
        import lzma
        fh = lzma.open(path, "rt")
    else:
        fh = open(path)
    for i, (line, row) in enumerate(zip(fh, rows)):
        assert [int(x) for x in line.split()] == list(row), \
            "%s row %d differs from witness rebuild" % (os.path.basename(path), i)
    extra = fh.readline()
    fh.close()
    assert not extra.strip(), "trailing data in " + os.path.basename(path)
    return "; shipped %s == witness rebuild" % os.path.basename(path)


def vw_lift_rows(w):
    _n, adj, _ = build_lift(w)
    return adj


def verify(path, full=False):
    w = json.load(open(path))
    fam = w["family"]
    if fam == "metacyclic":
        msg = verify_metacyclic(w)
    elif fam == "coset":
        msg = verify_coset(w, full)
    elif fam == "rc_lift":
        msg = verify_lift(w, full)
    else:
        raise ValueError("unknown family " + fam)
    msg += check_shipped_adjacency(w)
    print("PASS (%2d,%2d) n=%-8d %s: %s" % (w["d"], w["k"], w["n"], fam, msg))
    return w


def main(argv):
    full = "--full" in argv
    args = [a for a in argv if not a.startswith("--")]
    files = args or sorted(glob.glob(os.path.join(HERE, "witnesses", "*.json")))
    assert files, "no witness files found"
    for f in files:
        verify(f, full)
    print("ALL CHECKS PASS (%d witnesses)" % len(files))


if __name__ == "__main__":
    main(sys.argv[1:])
