#!/usr/bin/env python3
"""Generate and audit the rooted SAT case manifest for the N=62 problem.

The manifest uses only proved reductions:
  * 8-regularity and the rooted repeat budget;
  * every vertex lies in at most one G-triangle;
  * the repeat matrix B has no entry 3;
  * if B is simple, the 4-cycle parity identity forces an odd number of
    G-triangles, so the root may be chosen on a triangle;
  * if B has a double edge, the root may be chosen as an endpoint;
  * the proved local structure around a B-double edge gives the recommended
    five-way refinement of the three coarse double-edge root types.

No SAT solver is called.  The script emits deterministic JSON and checks all
parent counts, fixed degrees from the root layer, and branch-specific local
counts.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

N = 62
ROOT = 0
X = list(range(1, 9))
Y = list(range(9, 62))


@dataclass(frozen=True)
class Exceptional:
    vertex: int
    role: str
    parents: tuple[int, ...]


@dataclass
class Template:
    id: str
    branch: str
    description: str
    H_edges: list[tuple[int, int]]
    exceptional: list[Exceptional]
    global_B_mode: str
    fixed_B: list[tuple[int, int, int]]
    fixed_triangle_membership: dict[int, int]
    triangle_membership_xor: int | None = None
    fixed_extra_edges: list[tuple[int, int]] | None = None
    fixed_extra_nonedges: list[tuple[int, int]] | None = None
    double_local: dict[str, Any] | None = None


def normalize_edges(edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted((min(u, v), max(u, v)) for u, v in edges)


def class_layout(template: Template) -> tuple[dict[int, list[int]], dict[int, int], dict[int, int]]:
    hdeg = {x: 0 for x in X}
    for u, v in template.H_edges:
        hdeg[u] += 1
        hdeg[v] += 1

    exc_inc = {x: 0 for x in X}
    for e in template.exceptional:
        for x in e.parents:
            exc_inc[x] += 1

    # Each root neighbor x has one edge to ROOT, hdeg[x] edges in X, and
    # therefore 7-hdeg[x] edges to Y.  Exceptional incidences are fixed;
    # all remaining Y vertices have one parent and fill singleton classes.
    sizes = {x: 7 - hdeg[x] - exc_inc[x] for x in X}
    assert all(s >= 0 for s in sizes.values())

    first = 9 + len(template.exceptional)
    classes: dict[int, list[int]] = {}
    cursor = first
    for x in X:
        classes[x] = list(range(cursor, cursor + sizes[x]))
        cursor += sizes[x]
    assert cursor == 62, (template.id, cursor, sizes)
    return classes, hdeg, exc_inc


def parent_map(template: Template, classes: dict[int, list[int]]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for e in template.exceptional:
        result[e.vertex] = list(e.parents)
    for x, vertices in classes.items():
        for y in vertices:
            result[y] = [x]
    assert set(result) == set(Y)
    return result


def validate_template(template: Template) -> dict[str, Any]:
    assert template.branch in {"double", "simple"}
    assert template.global_B_mode in {"0/1/2", "simple_0/1"}
    assert len({e.vertex for e in template.exceptional}) == len(template.exceptional)
    assert [e.vertex for e in template.exceptional] == list(range(9, 9 + len(template.exceptional)))
    assert all(set(e.parents) <= set(X) for e in template.exceptional)
    assert all(len(set(e.parents)) == len(e.parents) for e in template.exceptional)

    template.H_edges = normalize_edges(template.H_edges)
    template.fixed_B = sorted((min(u, v), max(u, v), b) for u, v, b in template.fixed_B)
    template.fixed_extra_edges = normalize_edges(template.fixed_extra_edges or [])
    template.fixed_extra_nonedges = normalize_edges(template.fixed_extra_nonedges or [])

    classes, hdeg, exc_inc = class_layout(template)
    pmap = parent_map(template, classes)

    # Rooted defect budget: 2|E(H)| + sum_y(|P(y)|-1) = 3.
    budget = 2 * len(template.H_edges) + sum(len(p) - 1 for p in pmap.values())
    assert budget == 3, (template.id, budget)

    # Root neighbor degrees are completely filled by root, H, and parent edges.
    for x in X:
        y_count = sum(x in p for p in pmap.values())
        assert 1 + hdeg[x] + y_count == 8, (template.id, x, y_count)

    # The fixed root B-row must have total weight 3.
    root_b = sum(b for u, v, b in template.fixed_B if u == ROOT or v == ROOT)
    assert root_b == 3, (template.id, root_b)

    # No parent set of size four remains after triple-edge elimination.
    assert max(len(p) for p in pmap.values()) <= 3

    if template.branch == "double":
        assert template.H_edges == []
        assert len(template.exceptional) == 2
        w, a = template.exceptional
        assert w.role == "double_repeat_of_root" and len(w.parents) == 3
        assert a.role == "single_repeat_of_root" and len(a.parents) == 2
        assert template.global_B_mode == "0/1/2"
        assert template.fixed_triangle_membership.get(ROOT) == 0
        assert template.fixed_triangle_membership.get(w.vertex) == 0
        assert template.double_local is not None

        dl = template.double_local
        S = set(w.parents)
        R = set(X) - S
        assert set(dl["S"]) == S
        assert set(dl["R"]) == R
        counts = {int(k): int(v) for k, v in dl["w_neighbors_in_singleton_classes"].items()}
        assert set(counts) == R
        edge_wa = (min(w.vertex, a.vertex), max(w.vertex, a.vertex))
        if dl["w_adjacent_to_a"]:
            assert edge_wa in template.fixed_extra_edges
            assert sum(counts.values()) == 4
            # w has 3 fixed parents in S, edge wa, and four singleton children.
            assert 3 + 1 + sum(counts.values()) == 8
            b = int(dl["w_single_repeat_neighbor_in_X"])
            assert b in R
            assert (min(w.vertex, b), max(w.vertex, b), 1) in template.fixed_B
            # Cross-label totals from R to N(w)\S: one each, except b twice.
            for r in R:
                total = counts[r] + (1 if r in set(a.parents) else 0)
                assert total == (2 if r == b else 1), (template.id, r, total, b)
        else:
            assert edge_wa in template.fixed_extra_nonedges
            assert sum(counts.values()) == 5
            assert all(v == 1 for v in counts.values())
            assert 3 + sum(counts.values()) == 8
            # If P(a) meets S, wa=0 also follows from triangle-freeness at w.

        # All w-neighbors outside S must avoid parent labels in S.
        assert dl["forbid_w_neighbors_with_parent_intersecting_S"] is True
        assert dl["triangle_free_at_w"] is True

    else:
        assert template.H_edges == [(1, 2)]
        assert len(template.exceptional) == 1
        a = template.exceptional[0]
        assert a.role == "remaining_simple_repeat_of_root" and len(a.parents) == 2
        assert template.global_B_mode == "simple_0/1"
        assert template.triangle_membership_xor == 1
        assert template.fixed_triangle_membership.get(0) == 1
        assert template.fixed_triangle_membership.get(1) == 1
        assert template.fixed_triangle_membership.get(2) == 1
        # The remaining p=2 parent set cannot be exactly the root-triangle edge.
        assert set(a.parents) != {1, 2}

    residual_degree_Y = {y: 8 - len(p) for y, p in pmap.items()}
    assert all(4 <= d <= 7 for d in residual_degree_Y.values())

    return {
        "id": template.id,
        "branch": template.branch,
        "description": template.description,
        "root": ROOT,
        "root_neighbors": X,
        "Y_vertices": Y,
        "H_edges": [list(e) for e in template.H_edges],
        "exceptional": [
            {"vertex": e.vertex, "role": e.role, "parents": list(e.parents)}
            for e in template.exceptional
        ],
        "singleton_classes": {str(x): classes[x] for x in X},
        "singleton_class_sizes": {str(x): len(classes[x]) for x in X},
        "parent_map": {str(y): pmap[y] for y in sorted(pmap)},
        "residual_degree_inside_Y": {str(y): residual_degree_Y[y] for y in sorted(residual_degree_Y)},
        "global_B_mode": template.global_B_mode,
        "fixed_B": [list(row) for row in template.fixed_B],
        "fixed_triangle_membership": {str(k): v for k, v in sorted(template.fixed_triangle_membership.items())},
        "triangle_membership_xor": template.triangle_membership_xor,
        "fixed_extra_edges": [list(e) for e in template.fixed_extra_edges],
        "fixed_extra_nonedges": [list(e) for e in template.fixed_extra_nonedges],
        "double_local": template.double_local,
        "audit": {
            "rooted_repeat_budget": budget,
            "root_B_row_weight": root_b,
            "root_neighbor_H_degrees": {str(x): hdeg[x] for x in X},
            "root_neighbor_exceptional_incidences": {str(x): exc_inc[x] for x in X},
        },
    }


def build_templates() -> list[Template]:
    common_double = {
        "H_edges": [],
        "global_B_mode": "0/1/2",
        "fixed_triangle_membership": {0: 0, 9: 0},
    }

    templates = [
        Template(
            id="D0_MATCH",
            branch="double",
            description="B has a double edge 0--9; P(9) and P(10) are disjoint; 9 is nonadjacent to 10; the forced R-to-(N(9)\\S) incidence is a perfect matching.",
            exceptional=[
                Exceptional(9, "double_repeat_of_root", (1, 2, 3)),
                Exceptional(10, "single_repeat_of_root", (4, 5)),
            ],
            fixed_B=[(0, 9, 2), (0, 10, 1)],
            fixed_extra_nonedges=[(9, 10)],
            double_local={
                "w": 9,
                "a": 10,
                "S": [1, 2, 3],
                "R": [4, 5, 6, 7, 8],
                "w_adjacent_to_a": False,
                "w_neighbors_in_singleton_classes": {"4": 1, "5": 1, "6": 1, "7": 1, "8": 1},
                "w_single_repeat_neighbor_in_X": None,
                "forbid_w_neighbors_with_parent_intersecting_S": True,
                "triangle_free_at_w": True,
            },
            **common_double,
        ),
        Template(
            id="D0_EDGE_BIN",
            branch="double",
            description="Disjoint parent sets; 9--10 is an edge; the single repeat of 9 in X lies in P(10), canonically vertex 4.",
            exceptional=[
                Exceptional(9, "double_repeat_of_root", (1, 2, 3)),
                Exceptional(10, "single_repeat_of_root", (4, 5)),
            ],
            fixed_B=[(0, 9, 2), (0, 10, 1), (9, 4, 1)],
            fixed_extra_edges=[(9, 10)],
            double_local={
                "w": 9,
                "a": 10,
                "S": [1, 2, 3],
                "R": [4, 5, 6, 7, 8],
                "w_adjacent_to_a": True,
                "w_neighbors_in_singleton_classes": {"4": 1, "5": 0, "6": 1, "7": 1, "8": 1},
                "w_single_repeat_neighbor_in_X": 4,
                "forbid_w_neighbors_with_parent_intersecting_S": True,
                "triangle_free_at_w": True,
            },
            **common_double,
        ),
        Template(
            id="D0_EDGE_BOUT",
            branch="double",
            description="Disjoint parent sets; 9--10 is an edge; the single repeat of 9 in X lies outside P(10), canonically vertex 6.",
            exceptional=[
                Exceptional(9, "double_repeat_of_root", (1, 2, 3)),
                Exceptional(10, "single_repeat_of_root", (4, 5)),
            ],
            fixed_B=[(0, 9, 2), (0, 10, 1), (9, 6, 1)],
            fixed_extra_edges=[(9, 10)],
            double_local={
                "w": 9,
                "a": 10,
                "S": [1, 2, 3],
                "R": [4, 5, 6, 7, 8],
                "w_adjacent_to_a": True,
                "w_neighbors_in_singleton_classes": {"4": 0, "5": 0, "6": 2, "7": 1, "8": 1},
                "w_single_repeat_neighbor_in_X": 6,
                "forbid_w_neighbors_with_parent_intersecting_S": True,
                "triangle_free_at_w": True,
            },
            **common_double,
        ),
        Template(
            id="D1_MATCH",
            branch="double",
            description="B has a double edge 0--9; |P(9) intersect P(10)|=1; triangle-freeness at 9 forces 9 nonadjacent to 10 and a perfect matching across the five remaining root labels.",
            exceptional=[
                Exceptional(9, "double_repeat_of_root", (1, 2, 3)),
                Exceptional(10, "single_repeat_of_root", (1, 4)),
            ],
            fixed_B=[(0, 9, 2), (0, 10, 1)],
            fixed_extra_nonedges=[(9, 10)],
            double_local={
                "w": 9,
                "a": 10,
                "S": [1, 2, 3],
                "R": [4, 5, 6, 7, 8],
                "w_adjacent_to_a": False,
                "w_neighbors_in_singleton_classes": {"4": 1, "5": 1, "6": 1, "7": 1, "8": 1},
                "w_single_repeat_neighbor_in_X": None,
                "forbid_w_neighbors_with_parent_intersecting_S": True,
                "triangle_free_at_w": True,
            },
            **common_double,
        ),
        Template(
            id="D2_MATCH",
            branch="double",
            description="B has a double edge 0--9; |P(9) intersect P(10)|=2; triangle-freeness at 9 forces 9 nonadjacent to 10 and a perfect matching across the five remaining root labels.",
            exceptional=[
                Exceptional(9, "double_repeat_of_root", (1, 2, 3)),
                Exceptional(10, "single_repeat_of_root", (1, 2)),
            ],
            fixed_B=[(0, 9, 2), (0, 10, 1)],
            fixed_extra_nonedges=[(9, 10)],
            double_local={
                "w": 9,
                "a": 10,
                "S": [1, 2, 3],
                "R": [4, 5, 6, 7, 8],
                "w_adjacent_to_a": False,
                "w_neighbors_in_singleton_classes": {"4": 1, "5": 1, "6": 1, "7": 1, "8": 1},
                "w_single_repeat_neighbor_in_X": None,
                "forbid_w_neighbors_with_parent_intersecting_S": True,
                "triangle_free_at_w": True,
            },
            **common_double,
        ),
        Template(
            id="S_TOUCH",
            branch="simple",
            description="B is simple; root 0 is chosen on triangle 0-1-2; the remaining root repeat has parent set {1,3}, meeting the triangle edge in one endpoint.",
            H_edges=[(1, 2)],
            exceptional=[Exceptional(9, "remaining_simple_repeat_of_root", (1, 3))],
            global_B_mode="simple_0/1",
            fixed_B=[(0, 1, 1), (0, 2, 1), (0, 9, 1), (1, 2, 1)],
            fixed_triangle_membership={0: 1, 1: 1, 2: 1},
            triangle_membership_xor=1,
        ),
        Template(
            id="S_DISJOINT",
            branch="simple",
            description="B is simple; root 0 is chosen on triangle 0-1-2; the remaining root repeat has parent set {3,4}, disjoint from the triangle edge.",
            H_edges=[(1, 2)],
            exceptional=[Exceptional(9, "remaining_simple_repeat_of_root", (3, 4))],
            global_B_mode="simple_0/1",
            fixed_B=[(0, 1, 1), (0, 2, 1), (0, 9, 1), (1, 2, 1)],
            fixed_triangle_membership={0: 1, 1: 1, 2: 1},
            triangle_membership_xor=1,
        ),
    ]
    return templates



def audit_orbit_counts() -> dict[str, Any]:
    """Brute-force the small stabilizer orbits underlying case coverage."""
    from itertools import combinations, permutations

    universe = tuple(X)

    # Double-edge coarse cases: fix the 3-parent set S={1,2,3}; classify
    # the 2-parent set of a under the setwise stabilizer of S.
    S = frozenset({1, 2, 3})
    perms_S = []
    for image in permutations(universe):
        p = dict(zip(universe, image))
        if frozenset(p[x] for x in S) == S:
            perms_S.append(p)
    pairs = [frozenset(c) for c in combinations(universe, 2)]

    def orbit_partition(objects, perms):
        unseen = set(objects)
        orbits = []
        while unseen:
            seed = next(iter(unseen))
            orb = {frozenset(p[x] for x in seed) for p in perms}
            orb &= set(objects)
            unseen -= orb
            orbits.append(orb)
        return orbits

    double_orbits = orbit_partition(pairs, perms_S)
    double_signatures = sorted({len(next(iter(o)) & S) for o in double_orbits})
    assert len(double_orbits) == 3
    assert double_signatures == [0, 1, 2]

    # Simple-B cases: fix the root triangle edge {1,2}; classify the last
    # 2-parent set under its setwise stabilizer.
    Tedge = frozenset({1, 2})
    perms_T = []
    for image in permutations(universe):
        p = dict(zip(universe, image))
        if frozenset(p[x] for x in Tedge) == Tedge:
            perms_T.append(p)
    simple_orbits = orbit_partition(pairs, perms_T)
    simple_signatures = sorted({len(next(iter(o)) & Tedge) for o in simple_orbits})
    assert len(simple_orbits) == 3
    assert simple_signatures == [0, 1, 2]
    # Signature 2 is forbidden because it creates a second triangle on edge 1-2.

    # Refinement of the disjoint double case: preserve both S and P(a)={4,5};
    # the possible b in R has exactly two orbits.
    Pa = frozenset({4, 5})
    R = frozenset(set(universe) - set(S))
    perms_SP = []
    for image in permutations(universe):
        p = dict(zip(universe, image))
        if (frozenset(p[x] for x in S) == S and
                frozenset(p[x] for x in Pa) == Pa):
            perms_SP.append(p)
    unseen = set(R)
    b_orbits = []
    while unseen:
        seed = next(iter(unseen))
        orb = {p[seed] for p in perms_SP} & set(R)
        unseen -= orb
        b_orbits.append(orb)
    assert {frozenset(o) for o in b_orbits} == {frozenset({4, 5}), frozenset({6, 7, 8})}

    return {
        "double_parent_intersection_orbits": 3,
        "double_parent_intersection_signatures": double_signatures,
        "simple_parent_intersection_orbits_before_forbidden_case": 3,
        "simple_surviving_orbits": 2,
        "disjoint_edge_case_b_orbits": [sorted(o) for o in sorted(b_orbits, key=lambda z: min(z))],
        "recommended_instance_count": 5 + 2,
    }

def main() -> None:
    orbit_audit = audit_orbit_counts()
    templates = build_templates()
    rendered = [validate_template(t) for t in templates]
    payload = {
        "schema": "n62-rooted-sat-manifest-v1",
        "mathematical_status": "exhaustive assuming the proved no-triple-edge lemma and the stated double-edge local lemma",
        "n": N,
        "primary_variable_region": "Only edges with both endpoints in Y={9,...,61} need be primary SAT variables after applying a template.",
        "primary_edge_variable_count": len(Y) * (len(Y) - 1) // 2,
        "coarse_cases": 5,
        "recommended_instances": len(rendered),
        "orbit_audit": orbit_audit,
        "coverage": {
            "double_edge_present": ["D0_MATCH", "D0_EDGE_BIN", "D0_EDGE_BOUT", "D1_MATCH", "D2_MATCH"],
            "B_simple": ["S_TOUCH", "S_DISJOINT"],
        },
        "templates": rendered,
    }
    output = Path("/mnt/data/n62_root_templates.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    print(f"Wrote {output}")
    print(f"Primary Y-Y edge variables per instance: {payload['primary_edge_variable_count']}")
    print(f"Recommended instances: {len(rendered)}")
    print(f"Orbit audit: {orbit_audit}")
    for item in rendered:
        sizes = item["singleton_class_sizes"]
        print(f"  {item['id']}: class sizes {[sizes[str(x)] for x in X]}")
    print("All rooted-template audits passed.")


if __name__ == "__main__":
    main()
