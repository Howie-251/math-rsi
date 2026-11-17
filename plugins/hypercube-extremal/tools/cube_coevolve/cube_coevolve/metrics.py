"""Exact, inspectable indicator registry with declarative face aggregates."""
from collections import Counter
from itertools import combinations
from math import comb
from .graphs import geometry


def base_descriptions(n):
    descriptions = {"edges": "e=|E|", "min_degree": "minimum retained vertex degree, including isolated vertices",
                    "max_degree": "maximum retained vertex degree", "degree_sq_sum": "sum_v d(v)^2 over all 2^n vertices",
                    "even_squares": "squares_0+squares_2+squares_4", "odd_squares": "squares_1+squares_3",
                    "stars3": "sum_v binomial(d(v),3)", "addable_edges": "number of individual absent edges addable without a C4 (not simultaneous capacity)",
                    "holes_min_side": "min(p0_holes,p1_holes)", "holes_max_side": "max(p0_holes,p1_holes)"}
    for d in range(n + 1):
        descriptions[f"degree_{d}"] = f"number of vertices with degree {d}, both parities"
        for p in (0, 1):
            descriptions[f"p{p}_degree_{d}"] = f"number of degree {d} vertices with popcount parity {p}"
    for p in (0, 1):
        descriptions[f"p{p}_holes"] = f"binomial(n,3)*2^(n-3) - sum over parity {p} vertices of binomial(d(v),3); n<3 gives 0"
    for k in range(5):
        descriptions[f"squares_{k}"] = f"number of ambient two-dimensional faces retaining exactly {k} edges"
    if n == 7:
        descriptions["q7_J"] = "38448 - 126*edges + 27*degree_3 - 44*degree_6 - 128*degree_7; polynomial on Q7, no universal >=73 theorem asserted"
    return descriptions


def base_metrics(n, edges, include_addable=True):
    ambient, index, squares, _ = geometry(n)
    present = {index[tuple(e)] for e in edges}
    degrees = [0] * (1 << n)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    h = Counter(degrees)
    sides = [Counter(degrees[v] for v in range(1 << n) if v.bit_count() % 2 == p) for p in (0, 1)]
    sh = Counter(sum(e in present for e in square) for square in squares)
    faces3 = comb(n, 3) * (1 << (n - 3)) if n >= 3 else 0
    stars = [sum(comb(d, 3) * count for d, count in side.items()) for side in sides]
    holes = [faces3 - value for value in stars]
    m = {"edges": len(edges), "min_degree": min(degrees), "max_degree": max(degrees),
         "degree_sq_sum": sum(d * d for d in degrees),
         "even_squares": sum(sh[k] for k in (0, 2, 4)), "odd_squares": sh[1] + sh[3],
         "stars3": sum(stars), "holes_min_side": min(holes), "holes_max_side": max(holes)}
    for d in range(n + 1):
        m[f"degree_{d}"] = h[d]
        for p in (0, 1):
            m[f"p{p}_degree_{d}"] = sides[p][d]
    for p in (0, 1):
        m[f"p{p}_holes"] = holes[p]
    for k in range(5):
        m[f"squares_{k}"] = sh[k]
    if n == 7:
        m["q7_J"] = 38448 - 126 * len(edges) + 27 * h[3] - 44 * h[6] - 128 * h[7]
    if include_addable:
        blocked = set()
        for square in squares:
            missing = [e for e in square if e not in present]
            if len(missing) == 1:
                blocked.add(missing[0])
        m["addable_edges"] = len(ambient) - len(edges) - len(blocked)
    return m


def faces(n, edges, k):
    """All labelled k-faces, mapped by ascending free axes. p0 is LOCAL parity."""
    es = tuple(map(tuple, edges))
    for axes in combinations(range(n), k):
        mask = sum(1 << i for i in axes)
        for origin in range(1 << n):
            if origin & mask:
                continue
            def local(v):
                return sum(((v >> axis) & 1) << j for j, axis in enumerate(axes))
            yield tuple((local(u), local(v)) for u, v in es
                        if (u & ~mask) == origin and (v & ~mask) == origin)


class Registry:
    def __init__(self, n, definitions=()):
        self.n = n
        self.base_names = set(base_metrics(n, ()))
        self.definitions = []
        self.names = set(self.base_names)
        for definition in definitions:
            self.add(definition)

    def add(self, definition):
        if not isinstance(definition, dict) or set(definition) != {"name", "kind", "dimension", "metric", "aggregate"}:
            raise ValueError("face metric needs name/kind/dimension/metric/aggregate only")
        name, k = definition["name"], definition["dimension"]
        if not isinstance(name, str) or not name.isidentifier() or name in self.names:
            raise ValueError("metric name must be a fresh identifier")
        if definition["kind"] != "face_aggregate" or type(k) is not int or not 1 <= k <= self.n:
            raise ValueError("invalid face dimension/kind")
        if definition["metric"] not in base_metrics(k, (), include_addable=False):
            raise ValueError("unknown base face metric")
        if definition["aggregate"] not in ("min", "max", "sum"):
            raise ValueError("face aggregate must be min/max/sum")
        self.definitions.append(dict(definition))
        self.names.add(name)

    def compute(self, edges):
        result = base_metrics(self.n, edges)
        cache = {}
        for definition in self.definitions:
            k = definition["dimension"]
            if k not in cache:
                cache[k] = [base_metrics(k, face, False) for face in faces(self.n, edges, k)]
            values = [m[definition["metric"]] for m in cache[k]]
            result[definition["name"]] = {"min": min, "max": max, "sum": sum}[definition["aggregate"]](values)
        return result

    def describe(self):
        return {"n": self.n, "base_names": sorted(self.base_names), "definitions": self.definitions,
                "base_definitions": base_descriptions(self.n),
                "face_base_definitions": {str(k): base_descriptions(k) for k in sorted({d["dimension"] for d in self.definitions})},
                "face_contract": "dimension k uses the same formulas with n=k, degree indices 0..k; q7_J available only at k=7; addable_edges not available as face aggregate",
                "parity": "p0/p1 = popcount parity; for face aggregates parity is local after ascending-axis mapping",
                "holes": "number of Q3 faces minus specified-parity retained 3-stars; valid on C4-free graphs",
                "even_squares": "ambient Q2 faces with 0, 2 or 4 retained edges (4 absent in accepted graphs)"}
