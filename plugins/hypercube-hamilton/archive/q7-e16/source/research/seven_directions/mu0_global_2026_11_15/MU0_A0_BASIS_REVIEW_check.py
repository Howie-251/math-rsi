"""Independent labelled census of the three frozen a=0 templates."""

from collections import Counter, deque
from hashlib import file_digest
from itertools import combinations
import json
from pathlib import Path
from time import perf_counter


HERE = Path(__file__).resolve().parent
UNITS = tuple(1 << i for i in range(6))
EDGES = tuple(v for v in range(64) if v.bit_count() == 2)
TRIPLES = tuple(v for v in range(64) if v.bit_count() == 3)
QUARTETS = tuple(v for v in range(64) if v.bit_count() == 4)
CAPACITY = (5, 4, 3, 3, 1, 0)
SWAPS = tuple(
    tuple(v ^ ((3 << j) if ((v >> j) ^ (v >> (j + 1))) & 1 else 0) for v in range(64))
    for j in range(5)
)
# A triple hits every graph edge iff its complementary triple
# induces no graph edge. Precompute each induced edge mask explicitly.
COMPLEMENT_EDGE_MASK = {
    t: sum(1 << edge_idx for edge_idx, e in enumerate(EDGES) if not (t & e))
    for t in TRIPLES
}


def digest(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


def loads(points):
    return [sum((v >> j) & 1 for v in points) for j in range(6)]


def transport_ok(L, V):
    return all((l ^ v).bit_count() != 5 for l in L for v in V) and all(
        a+b <= 5 or (a, b) == (3, 3) for a, b in zip(loads(L), loads(V))
    )


def build_labelled(edge_count, include_zero, include_four, triple_counts):
    result = set()
    candidate_counts = Counter()
    for indices in combinations(range(15), edge_count):
        graph = tuple(EDGES[i] for i in indices)
        g = loads(graph)
        if max(g) > 3:
            continue
        mask = sum(1 << i for i in indices)
        graph_covers = [t for t, missed in COMPLEMENT_EDGE_MASK.items() if not mask & missed]
        for fourth in QUARTETS if include_four else (0,):
            even_loads = [x + ((fourth >> j) & 1) for j, x in enumerate(g)]
            max_odd = [CAPACITY[d] for d in even_loads]
            L = tuple(sorted((*((0,) if include_zero else ()), *graph, *((fourth,) if include_four else ()))))
            admissible_cover = [
                T for T in graph_covers if not include_four or (T & fourth).bit_count() >= 2
            ]
            for t in triple_counts:
                for triples in combinations(admissible_cover, t):
                    remainder = [a-b for a, b in zip(max_odd, loads(triples))]
                    if min(remainder) < 0:
                        continue
                    possible_units = tuple(
                        u for j, u in enumerate(UNITS)
                        if remainder[j] > 0 and (not include_four or u & fourth)
                    )
                    for units in combinations(possible_units, 8-t):
                        V = tuple(sorted((*units, *triples)))
                        assert transport_ok(L, V)
                        result.add((L, V))
                        candidate_counts[t] += 1
    assert sum(candidate_counts.values()) == len(result)
    return result, dict(sorted(candidate_counts.items()))


def common_orbit(pair):
    reached = {pair}
    tide = deque([pair])
    while tide:
        L, V = tide.popleft()
        for swap in SWAPS:
            moved = tuple(sorted(swap[v] for v in L)), tuple(sorted(swap[v] for v in V))
            if moved not in reached:
                reached.add(moved)
                tide.append(moved)
    return reached


def quotient(pairs):
    remaining, classes = set(pairs), {}
    while remaining:
        first = min(remaining)
        reached = common_orbit(first)
        assert reached <= remaining
        remaining.difference_update(reached)
        classes[first] = len(reached)
    return classes


def main():
    clock = perf_counter()
    inputs = {
        "zero_seven_edges": (7, True, False, range(2, 7)),
        "eight_edges": (8, False, False, range(2, 6)),
        "zero_six_edges_four": (6, True, True, range(4, 6)),
    }
    full = {name: build_labelled(*args) for name, args in inputs.items()}
    classes = {name: quotient(pairs) for name, (pairs, _) in full.items()}
    assert sum(len(pairs) for pairs, _ in full.values()) == len(set().union(*(pairs for pairs, _ in full.values())))
    producer_path = HERE / "MU0_A0_BASIS_PREFLIGHT.json"
    producer = json.loads(producer_path.read_bytes())
    assert producer["status"] == "COMPLETE"
    found = {name: {} for name in inputs}
    physical = []
    for index, row in enumerate(producer["representatives"]):
        group = row["template"]
        pair = tuple(row["L"]), tuple(row["V"])
        generated = common_orbit(pair)
        key = min(generated)
        assert key not in found[group]
        found[group][key] = row["orbit_multiplicity"]
        assert len(generated) == row["orbit_multiplicity"]
        alpha = tuple(sorted(64 + v for v in row["L"]))
        beta = tuple(sorted(127 ^ v for v in row["V"]))
        assert len(alpha) == len(beta) == 8
        assert all(v >= 64 and v.bit_count() % 2 for v in alpha)
        assert all(v >= 64 and v.bit_count() % 2 == 0 for v in beta)
        assert all((a ^ b).bit_count() != 1 for a in alpha for b in beta)
        physical.append({"basis_index": index, "alpha": alpha, "beta": beta,
                         "joint_S6_multiplicity": len(generated)})
    assert found == classes
    expected = {name: (len(full[name][0]), len(classes[name])) for name in inputs}
    assert list(expected.values()) == [(4860, 18), (90, 1), (0, 0)]
    assert len(physical) == 19
    output = {
        "verdict": "PASS",
        "scope": "Complete labelled residual large-face geometry of the three structural templates; no solver or prescribed matchings.",
        "producer_basis_sha256": digest(producer_path),
        "independent_checker_sha256": digest(Path(__file__)),
        "counts": {k: {"labelled_pairs": p, "joint_S6_orbits": n,
                       "labelled_pairs_by_triple_count": full[k][1]} for k, (p, n) in expected.items()},
        "total_labelled_pairs": 4950,
        "total_joint_S6_orbits": 19,
        "physical_hole_sets": physical,
        "seconds": perf_counter() - clock,
    }
    path = HERE / "MU0_A0_BASIS_REVIEW_check.json"
    with path.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=2)
        file.write("\n")
    print(json.dumps({k: v for k, v in output.items() if k != "physical_hole_sets"}))


if __name__ == "__main__":
    main()

