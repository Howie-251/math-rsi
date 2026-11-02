"""Exact small weighted encoding of the N59 root ``Q2/Z2`` moment table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping, Sequence

from .and_gate import BoolTerm, add_iff_and, add_simplified_clause, assert_term, negate
from .cardinality import UnaryThresholds, unary_thresholds
from .cnf import CNFBuilder


Pair = tuple[int, int]


def _pair(u: int, v: int) -> Pair:
    if u == v:
        raise ValueError("a moment pair needs distinct vertices")
    return (u, v) if u < v else (v, u)


@dataclass(frozen=True)
class RootMomentEncoding:
    """Unary weighted sums and exact-``Q2`` selectors exposed to cube builders."""

    q2: UnaryThresholds
    z2: UnaryThresholds
    q2_selectors: Mapping[int, BoolTerm]
    weighted_vertices: tuple[tuple[int, int], ...]


def normalize_moment_table(
    q2_domain: Sequence[int], z2_cap_by_q2: Mapping[object, object]
) -> tuple[tuple[int, ...], dict[int, int]]:
    domain = tuple(sorted(set(map(int, q2_domain))))
    if not domain or domain[0] < 0:
        raise ValueError("Q2 domain must be a nonempty set of nonnegative integers")
    caps = {int(key): int(value) for key, value in z2_cap_by_q2.items()}
    if set(caps) != set(domain):
        raise ValueError("Q2 domain and Z2-cap table have different keys")
    if any(value < 0 for value in caps.values()):
        raise ValueError("Z2 caps must be nonnegative")
    return domain, caps


def _exact_value_selector(
    builder: CNFBuilder,
    thresholds: UnaryThresholds,
    value: int,
    key,
) -> BoolTerm:
    if not 0 <= value <= thresholds.input_count:
        return False
    return add_iff_and(
        builder,
        thresholds.ge(value),
        negate(thresholds.ge(value + 1)),
        ("exact_weighted_value", key, value),
        kind="weighted_value_selector",
    )


def add_root_moment_budget(
    builder: CNFBuilder,
    *,
    weighted_vertices: Sequence[tuple[int, int]],
    adjacency: Callable[[int, int], BoolTerm],
    b_entries: Mapping[Pair, object],
    q2_domain: Sequence[int],
    z2_cap_by_q2: Mapping[object, object],
    key,
    exact_q2: int | None = None,
) -> RootMomentEncoding:
    """Encode the exact weighted sums and the supplied strict-moment table.

    ``weighted_vertices`` is ``Y`` from the handoff.  For ``m=0`` it contains
    the exceptional vertices with defect weights.  For ``m=1`` it additionally
    contains the two endpoints of the root-neighbourhood edge with weight one.
    Each repeat entry must provide ``ge_b(level)`` and ``max_b``.
    """

    weighted = tuple((int(vertex), int(weight)) for vertex, weight in weighted_vertices)
    if len({vertex for vertex, _ in weighted}) != len(weighted):
        raise ValueError("moment vertices must be distinct")
    if any(weight <= 0 for _, weight in weighted):
        raise ValueError("moment weights must be positive")
    domain, caps = normalize_moment_table(q2_domain, z2_cap_by_q2)

    q_terms: list[BoolTerm] = []
    z_terms: list[BoolTerm] = []
    for left_index in range(len(weighted)):
        u, u_weight = weighted[left_index]
        for v, v_weight in weighted[left_index + 1 :]:
            multiplicity = u_weight * v_weight
            q_terms.extend([adjacency(u, v)] * multiplicity)
            entry = b_entries[_pair(u, v)]
            for level in range(1, int(entry.max_b) + 1):
                z_terms.extend([entry.ge_b(level)] * multiplicity)

    q2 = unary_thresholds(
        builder,
        q_terms,
        None,
        ("root_moment_Q2", key),
        kind="root_moment_Q2",
    )
    z2 = unary_thresholds(
        builder,
        z_terms,
        None,
        ("root_moment_Z2", key),
        kind="root_moment_Z2",
    )
    selectors = {
        value: _exact_value_selector(builder, q2, value, (key, "Q2"))
        for value in domain
    }

    # Q2 always has one integer value.  Requiring one listed exact selector
    # therefore excludes every value outside the precomputed coarse domain.
    add_simplified_clause(builder, *selectors.values())
    for value, selector in selectors.items():
        cap = caps[value]
        if cap < z2.input_count:
            add_simplified_clause(
                builder,
                negate(selector),
                negate(z2.ge(cap + 1)),
            )

    if exact_q2 is not None:
        if exact_q2 not in selectors:
            raise ValueError(f"Q2={exact_q2} is outside the supplied domain")
        assert_term(builder, selectors[exact_q2], True)

    return RootMomentEncoding(q2, z2, selectors, weighted)


def evaluate_root_moments(
    weighted_vertices: Sequence[tuple[int, int]],
    adjacency_value: Callable[[int, int], int],
    b_value: Callable[[int, int], int],
) -> tuple[int, int]:
    """Direct integer evaluation used by the independent verifier/tests."""

    q2 = 0
    z2 = 0
    weighted = tuple(weighted_vertices)
    for index, (u, u_weight) in enumerate(weighted):
        for v, v_weight in weighted[index + 1 :]:
            factor = int(u_weight) * int(v_weight)
            q2 += factor * int(adjacency_value(int(u), int(v)))
            z2 += factor * int(b_value(int(u), int(v)))
    return q2, z2

