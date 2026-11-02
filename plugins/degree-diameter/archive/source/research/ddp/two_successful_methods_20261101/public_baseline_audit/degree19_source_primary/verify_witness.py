#!/usr/bin/env python3
"""verify_witness.py -- standalone verification of the graphs claimed in the note "New lower bounds for the
degree-diameter problem from generalized quadrangles and hexagons".

Every graph has a witness in witnesses/ and an explicit list of its edges: graph_dD_kK_nN.adj for the fibre
extensions (line i lists the neighbours of vertex i), graph_dD_kK_nN.edges.xz for the repaired fibre extension and
the attachment graphs (a line 'n m', then one edge 'u v' per line; vertices 0..n-1).  Sharing no code with any
search program, this script checks:

  fibre extensions (Section 2): it rebuilds W(q) from coordinates and the graph from (q, field, X, X', gadget),
      checks that the rebuild equals the shipped adjacency list row by row, checks the hypothesis of Theorem 1
      (the class graph has diameter <= 3), and runs breadth-first search from EVERY vertex.
  the fibre extension repaired by a matching (Section 2.1): it rebuilds the graph in the coordinates of the
      witness from (q, field, X, X', gadget, matching), checks that the rebuild equals the shipped edge list byte
      for byte, that the matching is a matching of points, that without it the pairs at distance > 3 are exactly
      the stated number of pairs of lines of one class in different pencils, and that with it every vertex has
      eccentricity exactly 3.
  attachments (Sections 3 and 4): it reads the shipped edge list (sha256 pinned in the witness), checks
      that the graph is simple with maximum degree d, and then checks the construction the witness describes
      EDGE BY EDGE:
        - every block (tower level) is a (q+1)-regular bipartite graph on 2(q^k - 1)/(q - 1) vertices of
          diameter k, i.e. a bipartite Moore graph, the incidence graph of a generalized k-gon of order q,
          and in a compound all blocks are the same graph;
        - the cross edges are exactly the matchings of the design, minus the listed deletion sets, and the
          deleted points are pairwise non-collinear and the deleted lines pairwise non-concurrent;
        - every attached vertex has exactly one neighbour in each half-block (in each part of each level
          above it), and the attached vertices' own graph has diameter <= k.
      Diameter <= k then follows from Theorem 2 (towers) or Theorem 3 (surgery).  As an independent spot check
      the script also runs breadth-first search from sampled sources of the whole graph.

  python3 verify_witness.py              all graphs as above; the last line is ALL CHECKS PASS
  python3 verify_witness.py --full       in addition, breadth-first search from EVERY vertex of every
                                         attachment graph, by allsources.c (compiled here with gcc -fopenmp);
                                         this takes hours for the largest graphs
  python3 verify_witness.py ID [ID ...]  only these witnesses (file names without .json)

Needs Python 3 and numpy (the fibre-extension part uses the standard library only).  If gcc is available the
block-diameter checks use allsources.c, which is much faster than the numpy fallback.
"""
import glob
import hashlib
import itertools
import json
import lzma
import os
import random
import shutil
import subprocess
import sys
import tempfile
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))

# =============================================================================== fibre extensions (stdlib)


def field(q, p, poly):
    e = len(poly) - 1
    assert p ** e == q and poly[-1] == 1

    def digs(a):
        return [(a // p ** i) % p for i in range(e)]

    def undig(ds):
        return sum(c * p ** i for i, c in enumerate(ds))

    def pmul(a, b):
        A, B = digs(a), digs(b)
        prod = [0] * (2 * e - 1)
        for i, x in enumerate(A):
            for j, y in enumerate(B):
                prod[i + j] = (prod[i + j] + x * y) % p
        for i in range(2 * e - 2, e - 1, -1):
            c, prod[i] = prod[i], 0
            if c:
                for j in range(e):
                    prod[i - e + j] = (prod[i - e + j] - c * poly[j]) % p
        return undig(prod[:e])

    add = [[undig([(x + y) % p for x, y in zip(digs(a), digs(b))]) for b in range(q)] for a in range(q)]
    mul = [[pmul(a, b) for b in range(q)] for a in range(q)]
    neg = [next(b for b in range(q) if add[a][b] == 0) for a in range(q)]
    inv = [None] + [next(b for b in range(1, q) if mul[a][b] == 1) for a in range(1, q)]  # fails if not a field
    return add, mul, neg, inv


def fibre_build(W):
    """The fibre extension of W(q) defined by (X, X', gadget): vertex and edge order as in the note."""
    q = W["q"]
    add, mul, neg, inv = field(q, W["field"]["p"], W["field"]["poly"])

    def canon(v):
        c = next(c for c in v if c)
        return tuple(mul[inv[c]][t] for t in v)

    def form(x, y):  # the alternating form x0 y1 - x1 y0 + x2 y3 - x3 y2
        return add[add[mul[x[0]][y[1]]][neg[mul[x[1]][y[0]]]]][add[mul[x[2]][y[3]]][neg[mul[x[3]][y[2]]]]]

    pts = [v for v in itertools.product(range(q), repeat=4) if any(v) and canon(v) == v]

    def line(x, y):
        S = {canon(x), canon(y)}
        for b in range(1, q):
            S.add(canon(tuple(add[u][mul[b][w]] for u, w in zip(x, y))))
        return frozenset(S)

    L = set()
    for i, x in enumerate(pts):
        for y in pts[i + 1:]:
            if form(x, y) == 0:
                L.add(line(x, y))
    lines_all = sorted(L, key=lambda s: sorted(s))
    assert len(pts) == (q ** 4 - 1) // (q - 1) and len(lines_all) == (q + 1) * (q * q + 1)
    inf = canon((1, 0, 0, 0))
    aff = [v for v in pts if v[1] != 0]                     # points not collinear with inf
    pid = {v: i for i, v in enumerate(aff)}
    lines = [s for s in lines_all if inf not in s]          # lines not through inf
    lid = {s: len(aff) + i for i, s in enumerate(lines)}
    n = len(aff) + len(lines)
    nb = [set() for _ in range(n)]

    def edge(a, b):
        assert a != b
        nb[a].add(b)
        nb[b].add(a)

    for s, j in lid.items():                                # incidence
        for v in s:
            if v in pid:
                edge(pid[v], j)
    for v, i in pid.items():                                # point fibres: p ~ p + x inf, x in X
        w = tuple(mul[inv[v[1]]][t] for t in v)
        for x in W["X"]:
            edge(i, pid[canon((add[w[0]][x], w[1], w[2], w[3]))])

    def z(s, lam):                                          # transvection v -> v + lam v1 inf
        return frozenset(canon((add[v[0]][mul[lam][v[1]]], v[1], v[2], v[3])) for v in s)

    Ms = sorted({line(inf, m) for m in pts if m[1] == 0 and m != inf}, key=lambda s: sorted(s))
    for M in Ms:                                            # one class per line M through inf
        pencils = {}
        for s in lines:
            if s & M:
                pencils.setdefault(next(iter(s & M)), []).append(s)
        assert len(pencils) == q and all(len(v) == q for v in pencils.values())
        label = {}
        for a, (_m, Ls) in enumerate(sorted(pencils.items())):
            base = min(Ls, key=lambda s: sorted(s))
            for l in range(q):
                label[(a, l)] = z(base, l)
            assert set(label[(a, l)] for l in range(q)) == set(Ls)
        for (a, l), s in label.items():                     # pencil edges: Cay(F_q, X') on each pencil
            for x in W["Xp"]:
                edge(lid[s], lid[label[(a, add[l][x])]])
        for u, v in W["gadget"]:                            # the gadget, copied onto every class
            edge(lid[label[(u // q, u % q)]], lid[label[(v // q, v % q)]])
    return n, [sorted(a) for a in nb], len(aff), (add, neg)


def eccentricity(nbrs, s):
    dist = [-1] * len(nbrs)
    dist[s] = 0
    dq = deque([s])
    while dq:
        v = dq.popleft()
        for w in nbrs[v]:
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                dq.append(w)
    assert min(dist) >= 0, "disconnected"
    return max(dist)


def check_fibre(W):
    q, X, Xp = W["q"], set(W["X"]), set(W["Xp"])
    n, nbrs, npts, (add, neg) = fibre_build(W)
    assert n == W["n"] == q ** 3 + (q + 1) * q * q
    assert X.isdisjoint(Xp) and X | Xp == set(range(1, q)), "X, X' do not partition F_q^*"
    assert all(neg[x] in X for x in X) and all(neg[x] in Xp for x in Xp), "X or X' not symmetric"
    cn = [set() for _ in range(q * q)]                      # the class graph on labels a*q + l
    for a in range(q):
        for l in range(q):
            for x in Xp:
                cn[a * q + l].add(a * q + add[l][x])
    for u, v in W["gadget"]:
        cn[u].add(v)
        cn[v].add(u)
    cn = [sorted(s) for s in cn]
    cdiam = max(eccentricity(cn, s) for s in range(q * q))
    assert cdiam <= 3, "class graph has diameter %d > 3" % cdiam
    assert max(len(s) for s in cn) == len(Xp) + W["t"]
    text = "".join(" ".join(map(str, row)) + "\n" for row in nbrs).encode()
    raw = read_bytes(os.path.join(HERE, W["adjacency"]))
    assert raw == text, "shipped %s differs from the rebuild" % W["adjacency"]
    assert hashlib.sha256(raw).hexdigest() == W["adjacency_sha256"], "adjacency sha256 differs from the witness"
    degs = [len(a) for a in nbrs]
    assert all(v not in nbrs[v] for v in range(n))
    assert set(degs[:npts]) == {q + 1 + len(X)} and set(degs[npts:]) == {q + len(Xp) + W["t"]}
    assert max(degs) == W["d"]
    ecc = [eccentricity(nbrs, s) for s in range(n)]
    assert max(ecc) == W["k"] == min(ecc), "eccentricities %d..%d" % (min(ecc), max(ecc))
    return ("fibre extension of W(%d), |X|=%d |X'|=%d t=%d: class graph diameter %d; shipped adjacency == "
            "rebuild; degrees %d/%d; all %d eccentricities = %d"
            % (q, len(X), len(Xp), W["t"], cdiam, q + 1 + len(X), q + len(Xp) + W["t"], n, W["k"]))


def fibre_coordinate_edges(W, matching=True):
    """The fibre extension Gamma(q; X, X'; K) of Definition 1 in the coordinates of the witness: point (a,1,b,c) is
    vertex a q^2 + b q + c, the line beta_w(u, s) is vertex q^3 + w q^2 + u q + s (w = 0..q the classes), the gadget
    is given on labels u q + s and copied onto every class; optionally the point matching.  Sorted unique (u, v)."""
    q = W["q"]
    add, mul, neg, inv = field(q, W["field"]["p"], W["field"]["poly"])
    sub = [[add[a][neg[b]] for b in range(q)] for a in range(q)]
    q2, q3 = q * q, q ** 3
    E = set()

    def edge(x, y):
        if x != y:
            E.add((min(x, y), max(x, y)))

    for a in range(q):
        for b in range(q):
            for c in range(q):
                p = a * q2 + b * q + c
                for w in range(q):                          # incidence, class w < q: the line (w, w b - c, .)
                    u = sub[mul[w][b]][c]
                    edge(p, q3 + w * q2 + u * q + sub[a][mul[u][b]])
                edge(p, q3 + q * q2 + b * q + sub[a][mul[b][c]])   # incidence, class q: the line (q, b, .)
                for x in W["X"]:                             # point fibres p ~ z_x(p)
                    edge(p, add[a][x] * q2 + b * q + c)
    for w in range(q + 1):
        for u in range(q):
            for s in range(q):
                for x in W["Xp"]:                           # pencil edges
                    edge(q3 + w * q2 + u * q + s, q3 + w * q2 + u * q + add[s][x])
        for x, y in W["gadget"]:                            # the gadget, copied onto every class
            edge(q3 + w * q2 + x, q3 + w * q2 + y)
    if matching:
        for x, y in W["matching"]:
            edge(x, y)
    return q3 + (q + 1) * q2, sorted(E)


def ball_bits(n, E, k):
    """For every vertex the set of vertices within distance k, as Python integers used as bit sets."""
    nb = [[] for _ in range(n)]
    for x, y in E:
        nb[x].append(y)
        nb[y].append(x)
    R = [1 << v for v in range(n)]
    for _ in range(k):
        R = [R[v] | _or(R[w] for w in nb[v]) for v in range(n)]
    return R


def _or(it):
    out = 0
    for x in it:
        out |= x
    return out


def check_fibre_matched(W):
    """Section 2.1: a fibre extension whose gadget leaves far pairs, repaired by a matching on the points."""
    q, X, Xp, k = W["q"], set(W["X"]), set(W["Xp"]), W["k"]
    add, mul, neg, inv = field(q, W["field"]["p"], W["field"]["poly"])
    assert X.isdisjoint(Xp) and X | Xp == set(range(1, q)), "X, X' do not partition F_q^*"
    assert all(neg[x] in X for x in X) and all(neg[x] in Xp for x in Xp), "X or X' not symmetric"
    q2, q3 = q * q, q ** 3
    if "voltage" in W:  # Section 2.1: the gadget is the Z_q voltage lift of its arcs, (u, s) ~ (u + delta mod q, s')
        lift = set()
        for s, s2, dl in W["voltage"]["arcs"]:
            for u in range(q):
                x, y = u * q + s, (u + dl) % q * q + s2
                lift.add((min(x, y), max(x, y)))
        assert lift == {(min(x, y), max(x, y)) for x, y in W["gadget"]}, "the gadget is not the voltage lift of its arcs"
    seen = set()
    for x, y in W["matching"]:
        assert 0 <= x < q3 and 0 <= y < q3 and x != y, "matching edge %r is not a pair of points" % ([x, y],)
        assert x not in seen and y not in seen, "a point is matched twice"
        seen.update((x, y))
    n0, E0 = fibre_coordinate_edges(W, matching=False)
    n, E = fibre_coordinate_edges(W)
    assert n == n0 == W["n"] == q3 + q2 * (q + 1)
    assert len(E) == len(E0) + len(W["matching"]), "a matching edge is already an edge of the fibre extension"
    text = ("%d %d\n" % (n, len(E)) + "".join("%d %d\n" % e for e in E)).encode()
    raw = read_bytes(os.path.join(HERE, W["edges"]))
    assert raw == text, "shipped %s differs from the rebuild" % W["edges"]
    assert hashlib.sha256(raw).hexdigest() == W["edges_sha256"], "edge list sha256 differs from the witness"
    deg = [0] * n
    for x, y in E:
        deg[x] += 1
        deg[y] += 1
    assert all(deg[p] == q + 1 + len(X) + (p in seen) for p in range(q3)), "a point has the wrong degree"
    assert set(deg[q3:]) == {q + len(Xp) + W["t"]}, "a line has the wrong degree"
    assert max(deg) == W["d"]
    # without the matching the far pairs are exactly lines of one class in different pencils (Section 2.1)
    R0 = ball_bits(n, E0, k)
    far0 = [(x, y) for x in range(n) for y in range(x + 1, n) if not R0[x] >> y & 1]
    assert len(far0) == W["far_pairs_without_matching"], "%d far pairs without the matching" % len(far0)
    for x, y in far0:
        assert x >= q3 and (x - q3) // q2 == (y - q3) // q2 and (x - q3) % q2 // q != (y - q3) % q2 // q, \
            "a far pair that is not two lines of one class in different pencils"
    per_class = [sum(1 for x, _ in far0 if (x - q3) // q2 == w) for w in range(q + 1)]
    assert len(set(per_class)) == 1, "the classes have different numbers of far pairs: %s" % per_class
    # with it: every vertex has eccentricity exactly k
    R = ball_bits(n, E, k)
    full = (1 << n) - 1
    assert all(r == full for r in R), "a pair is at distance > %d" % k
    R1 = ball_bits(n, E, k - 1)
    assert all(r != full for r in R1), "a vertex has eccentricity < %d" % k
    return ("fibre extension of W(%d) repaired by a matching: |X|=%d |X'|=%d t=%d; %d far pairs without the %d "
            "matching edges, 0 with them; shipped edge list == rebuild; degrees %d..%d; all %d eccentricities = %d"
            % (q, len(X), len(Xp), W["t"], len(far0), len(W["matching"]), min(deg), max(deg), n, k))


# ============================================================================== attachments (numpy)

def read_bytes(path):
    if path.endswith(".xz"):
        with lzma.open(path, "rb") as f:
            return f.read()
    with open(path, "rb") as f:
        return f.read()


def parse_adjacency(raw, n):
    """CSR (off, nbr) of an adjacency list: line i holds the neighbours of vertex i.  Vectorised, in
    line-aligned chunks so that a 600 MB list needs little more than its own CSR in memory."""
    np = NP
    assert not raw or raw[-1:] == b"\n", "the adjacency list must end with a newline"
    offs, vals = [np.zeros(1, dtype=np.int64)], []
    total, row0, pos, L = 0, 0, 0, len(raw)
    while pos < L:
        end = raw.find(b"\n", min(pos + (1 << 25), L - 1))
        end = L if end < 0 else end + 1
        a = np.frombuffer(raw, dtype=np.uint8, count=end - pos, offset=pos)
        bad = (a != 10) & (a != 32) & ((a < 48) | (a > 57))
        assert not bad.any(), "unexpected character in the adjacency list"
        isd = ((a >= 48) & (a <= 57)).astype(np.int8)
        edge = np.diff(np.concatenate(([0], isd, [0])))
        st = np.flatnonzero(edge == 1)
        ln = np.flatnonzero(edge == -1) - st
        v = np.zeros(len(st), dtype=np.int64)
        for i in range(int(ln.max()) if len(ln) else 0):
            sel = ln > i
            v[sel] = v[sel] * 10 + (a[st[sel] + i].astype(np.int64) - 48)
        nl = np.flatnonzero(a == 10)
        cnt = np.bincount(np.searchsorted(nl, st), minlength=len(nl))[:len(nl)]
        offs.append(total + np.cumsum(cnt))
        vals.append(v)
        total += len(st)
        row0 += len(nl)
        pos = end
    assert row0 == n, "adjacency list has %d lines, expected %d" % (row0, n)
    off = np.concatenate(offs)
    nbr = np.concatenate(vals) if vals else np.zeros(0, dtype=np.int64)
    assert len(nbr) == 0 or (nbr.min() >= 0 and nbr.max() < n), "neighbour index out of range"
    return off, nbr.astype(np.int32)


def parse_edge_list(raw):
    """(n, u, v) of an edge list: a line 'n m', then m lines 'u v'."""
    np = NP
    nl = raw.index(b"\n")
    n, m = map(int, raw[:nl].split())
    off, nbr = parse_adjacency(raw[nl + 1:], m)          # each edge line is a row of two numbers
    assert (np.diff(off) == 2).all(), "an edge line does not hold exactly two vertices"
    e = nbr.reshape(-1, 2).astype(np.int64)
    assert m == 0 or e.max() < n, "edge names a vertex >= n"
    return n, e[:, 0], e[:, 1]


def csr(n, u, v):
    """Sorted adjacency (off, nbr) of the undirected graph with edges u_i v_i."""
    np = NP
    s = np.concatenate([u, v])
    t = np.concatenate([v, u])
    o = np.lexsort((t, s))
    s, t = s[o], t[o]
    off = np.concatenate(([0], np.cumsum(np.bincount(s, minlength=n)))).astype(np.int64)
    return off, t.astype(np.int32)


def simple_undirected(off, nbr, n):
    """(no loops, no repeated neighbours, symmetric) as asserts; returns the degree array."""
    np = NP
    deg = np.diff(off)
    src = np.repeat(np.arange(n, dtype=np.int64), deg)
    dst = nbr.astype(np.int64)
    assert not (src == dst).any(), "self-loop"
    fwd = np.sort(src * n + dst)
    assert not (fwd[1:] == fwd[:-1]).any(), "repeated neighbour"
    assert np.array_equal(fwd, np.sort(dst * n + src)), "adjacency is not symmetric"
    return deg


def diameter_at_most(off, nbr, n, k, label):
    """True iff every vertex is within k of every vertex (all sources).  allsources.c if gcc is available,
    else 64-source numpy bitsets."""
    exe = c_checker()
    if exe:
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "g.adj")
            write_adjacency(off, nbr, n, p)
            r = subprocess.run([exe, p, str(n), str(int(NP.diff(off).max())), str(k)],
                               capture_output=True, text=True)
            return r.returncode == 0 and "PASS" in r.stdout
    np = NP
    if n > 100000:
        print("    (numpy all-sources BFS on %s, %d vertices: slow without gcc)" % (label, n), flush=True)
    heads = off[:-1]
    assert (np.diff(off) > 0).all(), "isolated vertex"
    idx = nbr.astype(np.int64)
    for b0 in range(0, n, 64):
        w = min(64, n - b0)
        reach = np.zeros(n, dtype=np.uint64)
        reach[b0:b0 + w] = np.left_shift(np.uint64(1), np.arange(w, dtype=np.uint64))
        full = np.uint64((1 << w) - 1)
        for _ in range(k):
            reach |= np.bitwise_or.reduceat(reach[idx], heads)
            if (reach == full).all():
                break
        if not (reach == full).all():
            return False
    return True


def bfs_ecc(off, nbr, n, s):
    np = NP
    dist = np.full(n, -1, dtype=np.int32)
    dist[s] = 0
    fr = np.array([s], dtype=np.int64)
    d = 0
    while fr.size:
        cnt = off[fr + 1] - off[fr]
        pos = np.repeat(off[fr] - np.concatenate(([0], np.cumsum(cnt)[:-1])), cnt) + np.arange(int(cnt.sum()))
        nb = nbr[pos].astype(np.int64)
        nb = np.unique(nb[dist[nb] < 0])
        if nb.size == 0:
            break
        d += 1
        dist[nb] = d
        fr = nb
    assert (dist >= 0).all(), "disconnected"
    return d


def induced(off, nbr, lo, hi):
    """CSR of the subgraph induced on [lo, hi) (vertices renumbered from 0)."""
    np = NP
    deg = np.diff(off)[lo:hi]
    src = np.repeat(np.arange(lo, hi, dtype=np.int64), deg)
    dst = nbr[off[lo]:off[hi]].astype(np.int64)
    keep = (dst >= lo) & (dst < hi)
    s, t = src[keep] - lo, dst[keep] - lo
    o = np.lexsort((t, s))
    s, t = s[o], t[o]
    m = hi - lo
    offs = np.concatenate(([0], np.cumsum(np.bincount(s, minlength=m))))
    return offs, t.astype(np.int32)


def write_adjacency(off, nbr, n, path):
    with open(path, "w") as f:
        for v in range(n):
            f.write(" ".join(map(str, nbr[off[v]:off[v + 1]].tolist())) + "\n")


def moore_part(q, k):
    """Points (= lines) of a generalized k-gon of order (q, q): (q^k - 1)/(q - 1)."""
    return (q ** k - 1) // (q - 1)


def check_block_is_polygon(off, nbr, lo, P, q, k, label):
    """[lo, lo+2P) is a (q+1)-regular bipartite graph points|lines of diameter <= k: a bipartite Moore graph."""
    boff, bnbr = induced(off, nbr, lo, lo + 2 * P)
    bdeg = NP.diff(boff)
    assert (bdeg == q + 1).all(), "%s is not (q+1)-regular inside" % label
    side = NP.repeat(NP.arange(2 * P) >= P, bdeg)
    assert (side != (bnbr >= P)).all(), "%s is not bipartite points|lines" % label
    assert diameter_at_most(boff, bnbr, 2 * P, k, label), "%s has diameter > %d" % (label, k)
    return boff, bnbr


def check_compound(W, off, nbr, deg):
    np = NP
    q, m, k, d, n = W["q"], W["m"], W["k"], W["d"], W["n"]
    kk = {"GQ": 4, "GH": 6}[W["polygon"]]
    assert kk == k
    P = moore_part(q, k)
    B = 2 * P
    n0 = m * B
    t = n - n0
    assert t == W["attached"] >= 1
    arcs = [tuple(a) for a in W["tournament"]]
    H = {tuple(sorted(e)) for e in W["H"]}
    pairs = list(itertools.combinations(range(m), 2))
    assert sorted(tuple(sorted(a)) for a in arcs) == pairs, "the arcs are not a tournament on the blocks"
    # typed matchings: (type_i, i, type_j, j)
    mats = [("P", i, "L", j) for i, j in arcs] + [("P" if (i, j) in H else "L", i, "P" if (i, j) in H else "L", j)
                                                   for i, j in pairs]
    delP = np.array(sorted(W["deleted_points"]), dtype=np.int64)
    delL = np.array(sorted(W["deleted_lines"]), dtype=np.int64)
    src = np.repeat(np.arange(n, dtype=np.int64), deg)
    dst = nbr.astype(np.int64)
    up = src < dst
    u, v = src[up], dst[up]
    ub, vb = u // B, v // B                     # block (m = attached)
    ub[u >= n0] = m
    vb[v >= n0] = m
    # 1. blocks: identical bipartite polygon incidence graphs
    boff, bnbr = check_block_is_polygon(off, nbr, 0, P, q, k, "block 0")
    same = (ub == vb) & (ub < m)
    ref = None
    for i in range(m):
        s = same & (ub == i)
        loc = np.sort((u[s] - i * B) * B + (v[s] - i * B))
        if ref is None:
            ref = loc
        assert np.array_equal(loc, ref), "block %d differs from block 0" % i
    # 2. cross edges between blocks: exactly the matchings minus the deletion sets
    cross = (ub != vb) & (ub < m) & (vb < m)
    cu, cv = u[cross], v[cross]
    def typ(x):
        return np.where((x % B) < P, 0, 1)      # 0 = point, 1 = line
    ci, cj, ti, tj = cu // B, cv // B, typ(cu), typ(cv)
    xi, xj = (cu % B) % P, (cv % B) % P
    assert (xi == xj).all(), "a cross edge joins different indices"
    code = {}
    for (a, i, b, j) in mats:
        code[(i, 0 if a == "P" else 1, j, 0 if b == "P" else 1)] = (a, i, b, j)
        code[(j, 0 if b == "P" else 1, i, 0 if a == "P" else 1)] = (a, i, b, j)
    keys = list(zip(ci.tolist(), ti.tolist(), cj.tolist(), tj.tolist()))
    per = {mt: [] for mt in mats}
    for kk_, x in zip(keys, xi.tolist()):
        assert kk_ in code, "cross edge between half-blocks the design does not join: %s" % (kk_,)
        per[code[kk_]].append(x)
    allx = np.arange(P, dtype=np.int64)
    for (a, i, b, j), xs in per.items():
        xs = np.array(sorted(xs), dtype=np.int64)
        assert len(np.unique(xs)) == len(xs), "repeated matching edge"
        missing = np.setdiff1d(allx, xs)
        if a != b:
            assert len(missing) == 0, "type-changing matching %s%d-%s%d has deletions" % (a, i, b, j)
        else:
            want = delP if a == "P" else delL
            assert np.array_equal(missing, want), "matching %s%d-%s%d: deletions differ from the witness" % (a, i, b, j)
    # 3. deletion sets pairwise non-collinear / non-concurrent inside the block graph
    mark = np.zeros(2 * P, dtype=np.int64)
    mark[delP] = 1
    on_line = np.add.reduceat(mark[bnbr[boff[P]:boff[2 * P]]], boff[P:2 * P] - boff[P])
    assert on_line.max(initial=0) <= 1, "two deleted points are collinear"
    mark[:] = 0
    mark[P + delL] = 1
    through = np.add.reduceat(mark[bnbr[boff[0]:boff[P]]], boff[0:P])
    assert through.max(initial=0) <= 1, "two deleted lines are concurrent"
    # 4. attached vertices: exactly one neighbour in each of the 2m half-blocks, the rest attached
    host = (ub < m) != (vb < m)
    hb = np.where(ub[host] < m, u[host], v[host])
    ha = np.where(ub[host] < m, v[host], u[host]) - n0
    cls = (hb // B) * 2 + typ(hb)
    cnt = np.zeros((t, 2 * m), dtype=np.int64)
    np.add.at(cnt, (ha, cls), 1)
    assert (cnt == 1).all(), "an attached vertex does not have exactly one neighbour in every half-block"
    # 5. the attached vertices' own graph
    ioff, inbr = induced(off, nbr, n0, n)
    assert int(np.diff(ioff).max()) == W["internal_max_degree"] <= d - 2 * m, "internal graph degree"
    assert diameter_at_most(ioff, inbr, t, k, "the internal graph"), "internal graph has diameter > %d" % k
    assert int(deg.max()) == d
    idiam = "<= %d" % k
    spare = d - (q + m)
    return ("surgery on %s(%d)-compound, m=%d%s: %d identical blocks (bipartite Moore, diameter %d); "
            "design + deletions %d points / %d lines (non-collinear / non-concurrent); %d attached, one host per "
            "half-block, internal max degree %d, diameter %s"
            % ("Q" if k == 4 else "H", q, m, " (spare degree %d)" % spare if spare > 0 else "", m, k, len(delP),
               len(delL), t, int(np.diff(ioff).max()), idiam))


def check_tower(W, off, nbr, deg):
    np = NP
    n, k, d = W["n"], W["k"], W["d"]
    levels = W["levels"]
    starts = [L["first"] for L in levels] + [n]
    for a, L in enumerate(levels):
        P = moore_part(L["q"], k)
        assert starts[a + 1] - starts[a] == 2 * P, "level %d has the wrong size" % a
        check_block_is_polygon(off, nbr, starts[a], P, L["q"], k, "level %d H(%d)" % (a, L["q"]))
    lev = np.searchsorted(np.array(starts[1:]), np.arange(n), side="right")
    src = np.repeat(np.arange(n, dtype=np.int64), deg)
    dst = nbr.astype(np.int64)
    ls, ld = lev[src], lev[dst]
    cross = ls > ld                              # from a lower level to one above it
    s, t_ = src[cross], dst[cross]
    tl = lev[t_]
    tside = (t_ - np.array(starts)[tl]) >= np.array([moore_part(L["q"], k) for L in levels])[tl]
    cnt = np.zeros((n, len(levels), 2), dtype=np.int64)
    np.add.at(cnt, (s, tl, tside.astype(np.int64)), 1)
    for a in range(len(levels)):
        rows = cnt[starts[a]:starts[a + 1]]
        assert (rows[:, :a, :] == 1).all(), "a level-%d vertex lacks one point and one line in a level above" % a
        assert (rows[:, a:, :] == 0).all()
    assert int(deg.max()) == d
    return ("hexagon tower %s: every level a bipartite Moore graph of diameter %d; every vertex has exactly one "
            "point and one line in each level above" % ([L["q"] for L in levels], k))


def c_checker():
    """Compile allsources.c once (gcc -O3 -fopenmp); None if no compiler."""
    global _EXE
    if _EXE is None:
        _EXE = ""
        cc = shutil.which("gcc") or shutil.which("cc")
        if cc:
            out = os.path.join(tempfile.mkdtemp(prefix="allsources"), "allsources")
            r = subprocess.run([cc, "-O3", "-fopenmp", "-o", out, os.path.join(HERE, "allsources.c")],
                               capture_output=True, text=True)
            if r.returncode == 0:
                _EXE = out
    return _EXE or None


_EXE = None
NP = None


def check_attachment(W, full):
    global NP
    import numpy
    NP = numpy
    raw = read_bytes(os.path.join(HERE, W["edges"]))
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == W["edges_sha256"], "edge list sha256 %s differs from the witness" % sha
    n, u, v = parse_edge_list(raw)
    del raw
    assert n == W["n"], "edge list has n=%d, witness says %d" % (n, W["n"])
    off, nbr = csr(n, u, v)
    del u, v
    deg = simple_undirected(off, nbr, n)
    assert int(deg.max()) == W["d"], "maximum degree %d, expected %d" % (int(deg.max()), W["d"])
    desc = {"compound-surgery": check_compound, "hexagon-tower": check_tower}[W["construction"]](W, off, nbr, deg)
    rng = random.Random(W["n"])
    srcs = [rng.randrange(n) for _ in range(6)] + [n - 1 - rng.randrange(min(n, 1000)) for _ in range(2)]
    eccs = [bfs_ecc(off, nbr, n, s) for s in srcs]
    assert max(eccs) <= W["k"], "a sampled source has eccentricity %d" % max(eccs)
    desc += "; BFS from %d sampled sources: eccentricity %d..%d" % (len(srcs), min(eccs), max(eccs))
    if full:
        exe = c_checker()
        assert exe, "--full needs gcc (allsources.c)"
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "g.adj")
            write_adjacency(off, nbr, n, p)
            r = subprocess.run([exe, p, str(n), str(W["d"]), str(W["k"])], capture_output=True, text=True)
        assert r.returncode == 0 and "PASS" in r.stdout, "allsources.c: %s" % r.stdout.strip()[-300:]
        hist = [l for l in r.stdout.splitlines() if l.startswith("eccentricity")]
        desc += "; ALL SOURCES (allsources.c): %s" % (hist[0] if hist else "PASS")
    return desc


def main(argv):
    full = "--full" in argv
    only = [a for a in argv if not a.startswith("-")]
    paths = sorted(glob.glob(os.path.join(HERE, "witnesses", "*.json")))
    if only:
        paths = [p for p in paths if os.path.basename(p)[:-5] in only]
        assert paths, "no witness named %s" % only
    for p in paths:
        W = json.load(open(p))
        if W["construction"] == "fibre-extension":
            desc = check_fibre(W)
        elif W["construction"] == "fibre-extension-matched":
            desc = check_fibre_matched(W)
        else:
            desc = check_attachment(W, full)
        print("PASS (%d,%d) n=%d  %s" % (W["d"], W["k"], W["n"], desc), flush=True)
    print("ALL CHECKS PASS (%d graphs%s)" % (len(paths), ", every source" if full else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
