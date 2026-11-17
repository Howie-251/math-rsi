"""Recompute the recorded obstruction from one saved matching and one plan."""

from itertools import combinations
import json
from pathlib import Path


VERTICES = set(range(128))
AXES = range(7)


def color(vertex):
    return vertex.bit_count() % 2


def half(vertices, axis, side):
    return {vertex for vertex in vertices if vertex >> axis & 1 == side}


def counts(vertices, alpha):
    first = sum(color(vertex) == alpha for vertex in vertices)
    return first, len(vertices) - first


def mirrors(vertices, outer):
    return {vertex ^ (1 << outer) for vertex in vertices}


def donor_gate(marked_half, other_half):
    if marked_half in {(0, 4), (1, 5)}:
        return other_half[0] == other_half[1] > 0
    if marked_half in {(0, 5), (1, 6)}:
        return other_half[0] == other_half[1] + 1 and 1 <= other_half[0] <= 16
    if marked_half in {(0, 6), (1, 7)}:
        return other_half in {(2, 0), (3, 1)}
    if marked_half == (2, 5):
        return other_half[1] == other_half[0] + 1 and 0 <= other_half[0] <= 15
    return marked_half == (1, 4) and other_half[1] == other_half[0] + 1


def receiver_choices(holes_a, holes_b, outer, alpha):
    sources = sorted(vertex for vertex in holes_a if color(vertex) != alpha)
    returns = sorted(vertex for vertex in holes_b if color(vertex) == alpha)
    for source in sources:
        mark = source ^ (1 << outer)
        for pair in combinations(returns, 2):
            selected = set(pair)
            modified = (holes_b - selected) | {mark}
            for inner in AXES:
                if inner == outer:
                    continue
                marked_half = half(modified, inner, mark >> inner & 1)
                majority, minority = counts(marked_half, alpha)
                other_majority, other_minority = counts(modified - marked_half, alpha)
                if majority - minority == 2 and other_majority == other_minority:
                    yield source, pair, inner


def assert_light_macros_absent(holes_a, holes_b, outer, alpha):
    r, donor_majority = counts(holes_a, alpha)
    receiver_majority, s = counts(holes_b, alpha)
    k = donor_majority - r
    assert receiver_majority - s == k
    assert (r, donor_majority, receiver_majority, s) not in {(5, 8, 3, 0), (4, 7, 4, 1)}

    columns = [axis for axis in AXES if axis != outer]
    side_one = [counts(half(holes_b, axis, 1), alpha) for axis in columns]
    if (r, donor_majority, receiver_majority, s) == (4, 8, 4, 0):
        assert side_one.count((2, 0)) < 3
    if k == 3:
        for axis in columns:
            allowed = []
            for side in (0, 1):
                major, minor = counts(half(holes_b, axis, side), alpha)
                supply = counts(half(holes_a, axis, side), alpha)[1]
                gap = major - minor
                allowed.append(1 <= gap <= 2 and supply >= gap and (gap == 1 or minor <= 1))
            assert not all(allowed)
    if (r, donor_majority, receiver_majority, s) == (3, 6, 5, 2):
        first, second = (vertex for vertex in holes_b if color(vertex) != alpha)
        scarcity = sum(1 <= major - minor <= 2 for major, minor in side_one)
        assert (first ^ second).bit_count() == 2
        assert scarcity == 0


def check_legacy(holes, partners, plan):
    outer = plan["outer"]
    alpha = plan["alpha_parity"]
    holes_a = half(holes, outer, plan["A_side"])
    holes_b = holes - holes_a
    assert counts(holes_a, alpha) == (4, 8)
    assert counts(holes_b, alpha) == (4, 0)
    sources, returns = set(plan["X"]), set(plan["U"])
    assert sources <= holes_a and counts(sources, alpha) == (0, 2)
    assert returns <= holes_b and counts(returns, alpha) == (2, 0)
    forward, backward = mirrors(sources, outer), mirrors(returns, outer)
    assert (forward, backward) == (set(plan["Y"]), set(plan["V"]))
    assert not ((forward | backward) & holes)
    assert {mark: partners[mark] for mark in forward | backward} == {5: 37, 6: 7, 59: 57, 91: 90}
    assert all((mark ^ partners[mark]) != 1 << outer for mark in forward | backward)

    new_a = (holes_a - sources) | backward
    new_b = (holes_b - returns) | forward
    assert new_a == set(plan["H_prime_A"]) and new_b == set(plan["H_prime_B"])
    marked = half(new_a, 4, 1)
    assert backward <= marked and counts(marked, alpha) == (2, 5)
    assert counts(new_a - marked, alpha) == (2, 3)
    for side, pair in ((0, {6, 126}), (1, {5, 125})):
        assert half(new_b, 0, side) == pair
        assert counts(pair, alpha) == (2, 0) and len(forward & pair) == 1


def main():
    archive = json.loads(Path(__file__).with_name("GLOBAL_PROBE.json").read_text(encoding="utf-8"))
    (entry,) = (row["candidate"] for row in archive["solves"] if row.get("candidate"))
    edges = entry["matching"]
    assert len(edges) == 56
    ends = [vertex for edge in edges for vertex in edge]
    assert len(set(ends)) == 112 and set(ends) <= VERTICES
    assert all((first ^ second).bit_count() == 1 for first, second in edges)
    holes = VERTICES - set(ends)
    even = {vertex for vertex in holes if color(vertex) == 0}
    odd = holes - even
    assert even == set(entry["even_holes"]) and odd == set(entry["odd_holes"])
    assert len(even) == len(odd) == 8
    assert all((first ^ second).bit_count() > 1 for first in even for second in odd)
    reflected_even = {127 ^ vertex for vertex in even}
    assert odd == set(entry["P"]) and reflected_even == set(entry["Q"])
    assert all(color(vertex) == 1 for vertex in odd | reflected_even)
    loads = [len(half(odd, axis, 1)) + len(half(reflected_even, axis, 1)) for axis in AXES]
    assert loads == [5, 3, 4, 2, 5, 3, 4]
    delta = [len(half(even, axis, 1)) - len(half(odd, axis, 1)) for axis in AXES]
    assert delta == [3, 5, 4, 6, 3, 5, 4]

    rows = []
    for outer, gap in enumerate(delta):
        for receiver_side in (0, 1):
            holes_b = half(holes, outer, receiver_side)
            holes_a = holes - holes_b
            even_b, odd_b = counts(holes_b, 0)
            alpha = int(even_b < odd_b)
            assert_light_macros_absent(holes_a, holes_b, outer, alpha)
            if abs(gap) != 3:
                continue
            whole_count, same_side_count, joint_count = 0, 0, 0
            witnesses = []
            for source, pair, inner in receiver_choices(holes_a, holes_b, outer, alpha):
                whole_count += 1
                if not witnesses:
                    witnesses.append((source, pair, inner, (source >> inner) & 1))
                marks = mirrors(set(pair), outer)
                modified = (holes_a - {source}) | marks
                for donor_inner in AXES:
                    if donor_inner == outer:
                        continue
                    marked_half = half(modified, donor_inner, min(marks) >> donor_inner & 1)
                    if marks <= marked_half:
                        same_side_count += 1
                        if donor_gate(counts(marked_half, alpha), counts(modified - marked_half, alpha)):
                            joint_count += 1
            rows.append((outer, receiver_side, whole_count, same_side_count, joint_count))
            print(rows[-1], witnesses[0])

    assert rows == [(0, 0, 12, 48, 0), (0, 1, 15, 60, 0), (4, 0, 38, 152, 0), (4, 1, 12, 48, 0)]
    partners = dict(edges) | {second: first for first, second in edges}
    legacy = archive["legacy_single_input"]
    assert legacy["requires_edge"] is False
    check_legacy(holes, partners, legacy["plan"])
    print("PASS: matching, light macros, all receiver choices, five gates, saved gap-four plan")


if __name__ == "__main__":
    main()
