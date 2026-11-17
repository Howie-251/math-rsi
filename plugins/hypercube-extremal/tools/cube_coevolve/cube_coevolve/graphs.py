"""Literal cube graphs; no generated code participates in acceptance."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import hashlib
import json


@lru_cache(maxsize=12)
def geometry(n):
    if type(n) is not int or not 1 <= n <= 10:
        raise ValueError("n must be an integer in 1..10")
    edges = tuple((v, v | (1 << i)) for v in range(1 << n)
                  for i in range(n) if not v & (1 << i))
    index = {e: k for k, e in enumerate(edges)}
    squares = []
    incident = [[] for _ in edges]
    for i, j in combinations(range(n), 2):
        for v in range(1 << n):
            if v & ((1 << i) | (1 << j)):
                continue
            a, b, c = v | (1 << i), v | (1 << j), v | (1 << i) | (1 << j)
            row = tuple(index[e] for e in ((v, a), (v, b), (a, c), (b, c)))
            sid = len(squares)
            squares.append(row)
            for eid in row:
                incident[eid].append(sid)
    return edges, index, tuple(squares), tuple(map(tuple, incident))


def normalize(n, edges):
    geometry(n)
    if not isinstance(edges, (list, tuple)):
        raise ValueError("edges must be a list of endpoint pairs")
    if len(edges) > n * (1 << (n - 1)):
        raise ValueError("too many edges")
    result = set()
    for edge in edges:
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            raise ValueError("each edge must have two endpoints")
        u, v = edge
        if type(u) is not int or type(v) is not int:
            raise ValueError("endpoints must be integers, not floats/bools")
        if not 0 <= u < (1 << n) or not 0 <= v < (1 << n) or (u ^ v).bit_count() != 1:
            raise ValueError("edge is not an ambient cube edge")
        e = (min(u, v), max(u, v))
        if e in result:
            raise ValueError("duplicate edge")
        result.add(e)
    return tuple(sorted(result))


def validate(n, edges):
    es = normalize(n, edges)
    ambient, index, squares, _ = geometry(n)
    present = {index[e] for e in es}
    histogram = Counter(sum(e in present for e in s) for s in squares)
    # Independent common-neighbour implementation, also used by the historical verifier.
    adj = [set() for _ in range(1 << n)]
    for u, v in es:
        adj[u].add(v)
        adj[v].add(u)
    pairs = Counter(pair for neighbors in adj for pair in combinations(sorted(neighbors), 2))
    common_c4 = sum(k * (k - 1) // 2 for k in pairs.values()) // 2
    if histogram[4] != common_c4:
        raise AssertionError("independent C4 counters disagree")
    if common_c4:
        raise ValueError(f"graph contains {common_c4} four-cycles")
    return es, {"valid": True, "edges": len(es), "squares": dict(sorted(histogram.items())),
                "c4_common_neighbors": common_c4, "ambient_edges": len(ambient)}


def graph_id(n, es):
    return hashlib.sha256(json.dumps([n, sorted(es)], separators=(",", ":")).encode()).hexdigest()[:20]


def read_edges(path):
    return [list(map(int, line.split())) for line in path.read_text().splitlines()
            if line.strip() and not line.lstrip().startswith("#")]


def greedy(n, rng, initial=(), deletion_count=0, weights=None):
    """Seed-preserving or delete/reinsert construction; always returns a C4-free graph."""
    ambient, index, squares, incident = geometry(n)
    present = {index[e] for e in normalize(n, list(initial))}
    if deletion_count:
        present.difference_update(rng.sample(sorted(present), min(deletion_count, len(present))))
    counts = [sum(e in present for e in square) for square in squares]
    if any(c == 4 for c in counts):
        raise ValueError("greedy initial graph must be C4-free")
    order = [i for i in range(len(ambient)) if i not in present]
    rng.shuffle(order)
    if weights is not None:
        order.sort(key=lambda i: weights[i], reverse=True)
    for i in order:
        if all(counts[s] < 3 for s in incident[i]):
            present.add(i)
            for s in incident[i]:
                counts[s] += 1
    return [list(ambient[i]) for i in sorted(present)]
