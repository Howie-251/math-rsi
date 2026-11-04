"""Finite adversarial checks of local proof obligations, not a proof of P6."""
from itertools import combinations
from pathlib import Path
import hashlib
import json


def edge(x, y):
    return tuple(sorted((x, y)))


def short(x, y):
    return (x ^ y).bit_count() == 1


def half_layer(m, j, p):
    return {
        edge(x, x ^ (1 << j))
        for x in range(1 << m)
        if not (x & (1 << j)) and (x.bit_count() & 1) == p
    }


def half_layers_in(m, matching):
    return [(j, p) for j in range(m) for p in (0, 1)
            if half_layer(m, j, p) <= matching]


def main():
    results = {"scope": "Finite local-obligation checks only; full P6 remains open."}
    checks = 0
    for m in (5, 6):
        for j in range(m):
            layers = [half_layer(m, j, p) for p in (0, 1)]
            supports = [{v for e in h for v in e} for h in layers]
            assert supports[0].isdisjoint(supports[1])
            assert supports[0] | supports[1] == set(range(1 << m))
            for support in supports:
                for x in support:
                    for k in range(m):
                        assert ((x ^ (1 << k)) in support) == (j == k)
                        checks += 1
    results["half_layer_internal_edge_checks"] = checks

    # The smallest permitted free set is checked for every placement and
    # every possible initial perfect pairing in Q5.
    swap_checks = 0
    no_short_checks = 0
    for a, b, c, d in combinations(range(32), 4):
        pairs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
        for j in range(5):
            for initial in pairs:
                pairing = list(initial)
                while any(x ^ y == 1 << j for x, y in pairing):
                    forbidden = next(i for i, (x, y) in enumerate(pairing)
                                     if x ^ y == 1 << j)
                    x, y = pairing[forbidden]
                    p, q = pairing[1 - forbidden]
                    old_count = sum(r ^ s == 1 << j for r, s in pairing)
                    pairing = [(x, p), (y, q)]
                    new_count = sum(r ^ s == 1 << j for r, s in pairing)
                    assert new_count < old_count
                assert {v for e in pairing for v in e} == {a, b, c, d}
                swap_checks += 1

        remaining = [a, b, c, d]
        greedy = []
        while True:
            candidate = next(((x, y) for x, y in combinations(remaining, 2)
                              if not short(x, y)), None)
            if candidate is None:
                break
            greedy.append(candidate)
            remaining = [v for v in remaining if v not in candidate]
        assert len(remaining) in (0, 2)
        if remaining:
            assert short(*remaining)
            greedy.append(tuple(remaining))
        assert sum(short(*e) for e in greedy) <= 1
        no_short_checks += 1
    results["N12_four_free_vertex_swap_cases"] = swap_checks
    results["N12_no_short_greedy_cases"] = no_short_checks

    # Verified counterexample to extending N12 to exactly two free points.
    full_layer = {edge(x, x ^ 1) for x in range(32) if x % 2 == 0}
    partial = full_layer - {(0, 1), (2, 3)}
    assert not half_layers_in(5, partial)
    assert half_layers_in(5, partial | {(0, 1)}) == [(0, 0)]
    results["N12_two_free_vertex_boundary_counterexample"] = {
        "m": 5, "v": 2, "b": 3, "Y": [0, 1],
        "F": sorted(partial), "unique_completion": [[0, 1]],
        "completed_half_layers": [[0, 0]],
        "status": "Verified outside the stated hypotheses; not a counterexample to N12."
    }
    # Opposite parity of the forbidden vertex and final endpoint in N11
    # cannot be dropped, even if the transformed matching has no half-layer.
    n11_original = full_layer - {(0, 1)}
    n11_transformed = (n11_original - {(2, 3)}) | {(0, 3)}
    assert not half_layers_in(5, n11_transformed)
    assert 1 .bit_count() % 2 == 2 .bit_count() % 2
    assert 0 .bit_count() % 2 != 2 .bit_count() % 2
    assert sum(x.bit_count() % 2 == 0 for x in range(32) if x != 1) == 16
    assert sum(x.bit_count() % 2 == 1 for x in range(32) if x != 1) == 15
    results["N11_wrong_parity_boundary_counterexample"] = {
        "m": 5, "a": 0, "v": 1, "b": 2, "k": 3,
        "L": sorted(n11_original), "T": sorted(n11_transformed),
        "half_layers_in_T": [],
        "obstruction": "A cube path on Q5 minus odd vertex 1 must have two even endpoints; 0 and 2 have opposite parity.",
        "status": "Verified outside the stated hypotheses; not a counterexample to N11."
    }

    # Fixed-coordinate implications and the root-3 symmetry in Z10.
    assert [j for j in range(1, 6)
            if ((0 >> j) & 1) == ((12 >> j) & 1) == ((48 >> j) & 1)] == [1]

    def f(x):
        y = x ^ 3
        return (y & ~3) | ((y & 1) << 1) | ((y & 2) >> 1)

    assert f(3) == 0
    assert {f(x) for x in (0, 3, 13, 49)} == {0, 3, 13, 49}
    for x in range(64):
        assert (x.bit_count() - f(x).bit_count()) % 2 == 0
        assert f(f(x)) == x
        for j in range(6):
            assert short(f(x), f(x ^ (1 << j)))
    results["Z10_symmetry"] = {
        "vertex_cases": 64, "directed_edge_cases": 384,
        "hole_map": {str(x): f(x) for x in (0, 3, 13, 49)},
        "common_zero_coordinate": 1,
    }
    results["status"] = "PASS"
    results["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in results.items()
                      if not k.endswith("boundary_counterexample")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
