"""Independently generate the labeled a=1 and a=2 B domains and audit the table."""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path
from time import monotonic

HERE = Path(__file__).resolve().parent
TEMPLATES = {
    1: (
        ("zero_six_edges", True, 6, False, 0, range(1, 6)),
        ("seven_edges", False, 7, False, 0, range(1, 5)),
        ("seven_edges_and_V_five_point", False, 7, False, 1, range(3)),
        ("zero_five_edges_four", True, 5, True, 0, (3, 4)),
    ),
    2: (
        ("zero_five_edges", True, 5, False, 0, range(4)),
        ("six_edges", False, 6, False, 0, range(3)),
        ("zero_four_edges_four", True, 4, True, 0, (2,)),
    ),
}
UNITS = tuple(1 << bit for bit in range(6))
BY_WEIGHT = {
    size: tuple(value for value in range(64) if value.bit_count() == size)
    for size in range(7)
}
GEN = tuple(
    tuple(
        value ^ ((value >> bit ^ value >> (bit + 1)) & 1) * (3 << bit)
        for value in range(64)
    )
    for bit in range(5)
)
SOFT_BUDGET = 110.0
START = monotonic()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def loads(group):
    return tuple(sum(bool(value & bit) for value in group) for bit in UNITS)


def orbit(pair):
    seen = {pair}
    todo = [pair]
    for left, right in todo:
        for step in GEN:
            moved = (
                tuple(sorted(step[x] for x in left)),
                tuple(sorted(step[x] for x in right)),
            )
            if moved not in seen:
                seen.add(moved)
                todo.append(moved)
    return seen


def pair_geometry(a, left, right):
    size = 8 - a
    assert len(set(left)) == size and len(set(right)) == size
    assert all(x.bit_count() % 2 == 0 for x in left)
    assert all(y.bit_count() % 2 == 1 for y in right)
    assert all((x ^ y).bit_count() != 5 for x in left for y in right)
    for left_load, right_load in zip(loads(left), loads(right)):
        assert left_load + right_load <= size - 2
        if left_load + right_load == size - 2:
            assert left_load >= 2 and right_load >= 2


def generate(a, template):
    _, has_zero, edge_count, has_quartic, fives, triple_counts = template
    size = 8 - a
    cap = size - 2
    labeled = set()
    for graph_index, edges in enumerate(itertools.combinations(BY_WEIGHT[2], edge_count)):
        if graph_index % 128 == 0 and monotonic() - START > SOFT_BUDGET:
            raise RuntimeError("independent geometry bound exceeded")
        for marker in BY_WEIGHT[4] if has_quartic else (None,):
            left = tuple(sorted((*edges, *((0,) if has_zero else ()), *((marker,) if marker is not None else ()))))
            left_loads = loads(left)
            if max(left_loads) >= cap:
                continue
            # At the full column load, both kinds must contribute at least two.
            # For a fixed L load, all admissible V loads thus form an initial interval.
            room = tuple(
                cap - count if 2 <= count <= cap - 2 else cap - 1 - count
                for count in left_loads
            )
            units, triples, pentads = (
                tuple(value for value in BY_WEIGHT[weight]
                      if all((value ^ x).bit_count() != 5 for x in left)
                      and all(amount or not (value & bit) for amount, bit in zip(room, UNITS)))
                for weight in (1, 3, 5)
            )
            for triple_count in triple_counts:
                unit_count = size - triple_count - fives
                if unit_count > len(units):
                    continue
                for triple_points in itertools.combinations(triples, triple_count):
                    for pentad_points in itertools.combinations(pentads, fives):
                        strong = triple_points + pentad_points
                        wide_load = loads(strong)
                        if any(count > maximum for count, maximum in zip(wide_load, room)):
                            continue
                        permitted = {
                            bit for bit, count, maximum in zip(UNITS, wide_load, room)
                            if count < maximum
                        }
                        for singles in itertools.combinations(sorted(permitted.intersection(units)), unit_count):
                            right = tuple(sorted((*strong, *singles)))
                            pair_geometry(a, left, right)
                            labeled.add((left, right))
    return labeled


def audit(a):
    source = HERE / f"MU0_A{a}_BASIS_PREFLIGHT.json"
    weight = HERE / f"MU0_A{a}_WEIGHT_REDUCTION.md"
    reported = json.loads(source.read_bytes())
    assert reported["status"] == "COMPLETE"
    assert reported["stored_representatives"] == len(reported["representatives"])
    class_counts = {}
    physical = [None] * len(reported["representatives"])
    for family in TEMPLATES[a]:
        title = family[0]
        labeled = generate(a, family)
        inferred = {}
        pending = set(labeled)
        while pending:
            expanded = orbit(next(iter(pending)))
            assert expanded <= pending
            pending.difference_update(expanded)
            inferred[min(expanded)] = len(expanded)
        declared = {}
        for idx, row in enumerate(reported["representatives"]):
            if row["template"] != title:
                continue
            left, right = tuple(row["L"]), tuple(row["V"])
            assert tuple(sorted(left)) == left and tuple(sorted(right)) == right
            assert (left, right) in labeled
            expanded = orbit((left, right))
            key = min(expanded)
            assert key not in declared
            assert len(expanded) == row["orbit_multiplicity"]
            declared[key] = len(expanded)
            holes_alpha = sorted(64 | value for value in left)
            holes_beta = sorted(127 ^ value for value in right)
            assert all(x.bit_count() % 2 == 1 for x in holes_alpha)
            assert all(y.bit_count() % 2 == 0 for y in holes_beta)
            assert all((x ^ y).bit_count() != 1 for x in holes_alpha for y in holes_beta)
            physical[idx] = {"index": idx, "H_alpha": holes_alpha, "H_beta": holes_beta}
        assert inferred == declared
        assert len(labeled) == reported["templates"][title]["valid_labeled_pairs"]
        assert len(inferred) == reported["templates"][title]["pair_orbits"]
        arities = dict(Counter(sum(v.bit_count() == 3 for v in right) for _, right in inferred))
        assert {str(k): v for k, v in arities.items()} == reported["templates"][title]["pair_orbits_by_triple_count"]
        class_counts[title] = {
            "labeled": len(labeled),
            "orbits": len(inferred),
            "orbits_by_triples": arities,
        }
    assert all(physical)
    return {
        "author_basis_sha256": digest(source),
        "weight_source_sha256": digest(weight),
        "labeled": sum(row["labeled"] for row in class_counts.values()),
        "orbits": sum(row["orbits"] for row in class_counts.values()),
        "templates": class_counts,
        "physical_large_face_rows": physical,
    }


def main():
    outputs = {a: audit(a) for a in (1, 2)}
    result = {
        "verdict": "PASS",
        "scope": "Necessary large-face geometries only. No enumeration of small-face holes or prescribed matching, no solver.",
        "audit_source_sha256": digest(Path(__file__).resolve()),
        "cases": outputs,
    }
    (HERE / "MU0_A12_BASIS_REVIEW_check.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    for a, outcome in outputs.items():
        print(f"a={a}: {outcome['labeled']} labeled pairs, {outcome['orbits']} common S6 orbits")
    print(f"wall {monotonic() - START:.3f} seconds")


if __name__ == "__main__":
    main()

