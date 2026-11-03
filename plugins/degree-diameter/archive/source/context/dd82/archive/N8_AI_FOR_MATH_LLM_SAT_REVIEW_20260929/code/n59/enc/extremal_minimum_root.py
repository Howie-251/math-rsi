"""Exact SAT predicates for the N59 extremal minimum-triangle root.

The caller supplies the already encoded nonedge-repeat support terms

``s_uv <-> (not A_uv) and (B_uv >= 1)``

and exact triangle counters.  This module deliberately does not rebuild
either graph semantics.  It adds the extremal-root rule and exposes an exact
unary counter for

``N_max = |{v : t(v)=m and k(v)=K}|``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .and_gate import BoolTerm, add_iff_and, add_simplified_clause, assert_term, negate
from .cardinality import UnaryThresholds, unary_thresholds
from .cnf import CNFBuilder
from .triangle_counts import BoundedCount


Pair = tuple[int, int]


def pair(u: int, v: int) -> Pair:
    if u == v:
        raise ValueError("a support pair needs distinct endpoints")
    return (u, v) if u < v else (v, u)


def exact_bounded_count_term(
    builder: CNFBuilder,
    count: BoundedCount,
    value: int,
    *,
    key,
    kind: str,
) -> BoolTerm:
    """Return a term equivalent to ``count == value``."""

    lower, not_upper = count.equals(value)
    return add_iff_and(builder, lower, not_upper, key, kind=kind)


@dataclass(frozen=True)
class ExtremalMinimumRootEncoding:
    """Semantic outputs of :func:`add_extremal_minimum_root`."""

    root: int
    m: int
    K: int
    support_counts: Mapping[int, UnaryThresholds]
    is_minimum_triangle: Mapping[int, BoolTerm]
    has_support_K: Mapping[int, BoolTerm]
    is_extremal: Mapping[int, BoolTerm]
    nmax: UnaryThresholds


def add_extremal_minimum_root(
    builder: CNFBuilder,
    *,
    vertices: Sequence[int],
    root: int,
    m: int,
    K: int,
    nonedge_support: Mapping[Pair, BoolTerm],
    triangle_counts: Mapping[int, BoundedCount],
    key,
) -> ExtremalMinimumRootEncoding:
    """Encode the exact extremal minimum-root contract.

    The resulting formula enforces

    * ``t(root)=m`` and ``k(root)=K``;
    * ``t(v)>=m`` for every vertex;
    * ``t(v)=m -> k(v)<=K`` for every vertex.

    It also defines, in both directions, every ``is_extremal[v]`` predicate
    and every threshold ``N_max>=j``.  These outputs are safe semantic split
    literals; they are not one-way witnesses.
    """

    vertices = tuple(vertices)
    if not vertices or len(set(vertices)) != len(vertices):
        raise ValueError("vertices must be a nonempty duplicate-free sequence")
    if root not in vertices:
        raise ValueError("root is outside the vertex set")
    if m < 0 or K < 0 or K >= len(vertices):
        raise ValueError("invalid extremal-root parameters")
    missing_triangles = set(vertices) - set(triangle_counts)
    if missing_triangles:
        raise ValueError(f"missing triangle counters for {sorted(missing_triangles)}")

    support_counts: dict[int, UnaryThresholds] = {}
    minimum_terms: dict[int, BoolTerm] = {}
    support_K_terms: dict[int, BoolTerm] = {}
    extremal_terms: dict[int, BoolTerm] = {}

    for vertex in vertices:
        incident: list[BoolTerm] = []
        for other in vertices:
            if other == vertex:
                continue
            uv = pair(vertex, other)
            if uv not in nonedge_support:
                raise ValueError(f"missing nonedge-support term for {uv}")
            incident.append(nonedge_support[uv])

        support_count = unary_thresholds(
            builder,
            incident,
            K + 1,
            ("extremal_minimum_root", key, "k", vertex),
            kind="extremal_support_count",
        )
        support_counts[vertex] = support_count

        triangles = triangle_counts[vertex]
        assert_term(builder, triangles.ge(m), True)
        is_minimum = exact_bounded_count_term(
            builder,
            triangles,
            m,
            key=("extremal_minimum_root", key, "t_equals_m", vertex),
            kind="minimum_triangle_vertex",
        )
        minimum_terms[vertex] = is_minimum

        # Exact maximum-root implication.  In particular, this does not
        # impose a lower support bound on other minimum-triangle vertices.
        add_simplified_clause(
            builder,
            negate(is_minimum),
            negate(support_count.ge(K + 1)),
        )

        has_support_K = add_iff_and(
            builder,
            support_count.ge(K),
            negate(support_count.ge(K + 1)),
            ("extremal_minimum_root", key, "k_equals_K", vertex),
            kind="extremal_support_equals_K",
        )
        support_K_terms[vertex] = has_support_K
        extremal_terms[vertex] = add_iff_and(
            builder,
            is_minimum,
            has_support_K,
            ("extremal_minimum_root", key, "is_extremal", vertex),
            kind="extremal_vertex",
        )

    assert_term(builder, minimum_terms[root], True)
    assert_term(builder, support_counts[root].ge(K), True)
    assert_term(builder, support_counts[root].ge(K + 1), False)
    assert_term(builder, extremal_terms[root], True)

    nmax = unary_thresholds(
        builder,
        (extremal_terms[vertex] for vertex in vertices),
        len(vertices),
        ("extremal_minimum_root", key, "N_max"),
        kind="extremal_vertex_count",
    )
    assert_term(builder, nmax.ge(1), True)

    return ExtremalMinimumRootEncoding(
        root=root,
        m=m,
        K=K,
        support_counts=support_counts,
        is_minimum_triangle=minimum_terms,
        has_support_K=support_K_terms,
        is_extremal=extremal_terms,
        nmax=nmax,
    )


__all__ = [
    "ExtremalMinimumRootEncoding",
    "add_extremal_minimum_root",
    "exact_bounded_count_term",
]
