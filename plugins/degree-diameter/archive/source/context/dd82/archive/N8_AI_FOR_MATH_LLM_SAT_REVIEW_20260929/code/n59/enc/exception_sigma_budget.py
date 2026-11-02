"""Exact local repeat budgets for exceptional second-layer vertices.

For an exceptional vertex ``E_i`` of defect ``e_i``, the c1 identities give

    sum_{z in X - {E_i}} B[E_i,z]
      + ell_i
      + sum_{j != i} e_j D[E_i,E_j] = 6 - e_i,

where ``ell_i`` is absent for ``m=0`` and is the number of the two special
parents used by ``E_i`` for ``m=1``.  The first summand reuses the exact unary
threshold tokens of the already encoded B entries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping, Sequence

from .and_gate import BoolTerm, add_simplified_clause, assert_term, negate
from .cardinality import UnaryThresholds, enforce_exactly
from .cnf import CNFBuilder


Pair = tuple[int, int]


def _pair(u: int, v: int) -> Pair:
    if u == v:
        raise ValueError("a sigma entry needs distinct endpoints")
    return (u, v) if u < v else (v, u)


@dataclass(frozen=True)
class ExceptionSigmaRow:
    """One exact exceptional-vertex budget."""

    vertex: int
    defect: int
    target: int
    b_tokens: tuple[BoolTerm, ...]
    special_parent_terms: tuple[BoolTerm, ...]
    exceptional_edge_tokens: tuple[BoolTerm, ...]
    total: UnaryThresholds


@dataclass(frozen=True)
class ExceptionSigmaEncoding:
    """All exceptional-vertex budgets, keyed by the vertex label."""

    rows: Mapping[int, ExceptionSigmaRow]
    m: int


def add_kernel_sigma_zero_implications(
    builder: CNFBuilder,
    *,
    selector: BoolTerm,
    encoding: ExceptionSigmaEncoding,
    zero_vertices: Sequence[int],
) -> int:
    """Conditionally clear every second-layer B entry with ``sigma_i=0``.

    A root kernel fixes the exceptional adjacencies and special-parent bits,
    hence it fixes each ``sigma_i``.  For every zero row this emits the direct
    clauses ``selector -> not(B[E_i,z] >= k)`` for all unary B tokens.  These
    clauses are redundant with the exact budget but expose the consequence
    immediately when a kernel selector is chosen.
    """

    before = builder.clause_count
    for vertex in map(int, zero_vertices):
        if vertex not in encoding.rows:
            raise ValueError(f"sigma-zero vertex {vertex} is not exceptional")
        for token in encoding.rows[vertex].b_tokens:
            add_simplified_clause(builder, negate(selector), negate(token))
    return builder.clause_count - before


def add_exception_sigma_budgets(
    builder: CNFBuilder,
    *,
    exceptional_vertices: Sequence[int],
    defects: Sequence[int],
    second_layer_vertices: Sequence[int],
    b_entries: Mapping[Pair, object],
    adjacency: Callable[[int, int], BoolTerm],
    m: int,
    special_parent_terms: Mapping[int, Sequence[BoolTerm]] | None = None,
    key,
) -> ExceptionSigmaEncoding:
    """Encode every exceptional ``sigma`` equality from the v4 handoff.

    ``special_parent_terms[x]`` must be ``(R[a,x], R[b,x])`` for ``m=1``.
    For ``m=0`` it is omitted.  Repeating an adjacency literal ``e_j`` times
    represents the exact integer coefficient in the weighted equality.
    """

    if m not in (0, 1):
        raise ValueError("exception sigma budgets only cover m=0 and m=1")
    exceptions = tuple(map(int, exceptional_vertices))
    weights = tuple(map(int, defects))
    second_layer = tuple(map(int, second_layer_vertices))
    if len(exceptions) != len(weights) or len(set(exceptions)) != len(exceptions):
        raise ValueError("exception vertices and defects must be parallel")
    if any(weight <= 0 or weight > 6 for weight in weights):
        raise ValueError("exception defects must lie in 1,...,6")
    if not set(exceptions) <= set(second_layer):
        raise ValueError("every exceptional vertex must lie in the second layer")

    supplied_special = special_parent_terms or {}
    if m == 0 and supplied_special:
        raise ValueError("m=0 has no special-parent ell terms")
    if m == 1 and set(supplied_special) != set(exceptions):
        raise ValueError("m=1 needs two special-parent terms per exception")

    rows: dict[int, ExceptionSigmaRow] = {}
    for index, (vertex, defect) in enumerate(zip(exceptions, weights)):
        b_tokens = tuple(
            token
            for other in second_layer
            if other != vertex
            for token in tuple(b_entries[_pair(vertex, other)].weight_tokens)
        )
        ell_terms = (
            ()
            if m == 0
            else tuple(supplied_special[vertex])
        )
        if m == 1 and len(ell_terms) != 2:
            raise ValueError("each m=1 exception needs exactly two ell terms")

        edge_tokens = tuple(
            adjacency(vertex, other)
            for other_index, (other, other_defect) in enumerate(
                zip(exceptions, weights)
            )
            if other_index != index
            for _ in range(other_defect)
        )
        target = 6 - defect
        terms = b_tokens + ell_terms + edge_tokens
        total = enforce_exactly(
            builder,
            terms,
            target,
            ("exception_sigma", key, vertex),
        )

        # This is redundant with the equality, but exposes the sigma=0 case
        # immediately to the B thresholds and the small root-support literals.
        if target == 0:
            for term in terms:
                assert_term(builder, term, False)

        rows[vertex] = ExceptionSigmaRow(
            vertex=vertex,
            defect=defect,
            target=target,
            b_tokens=b_tokens,
            special_parent_terms=ell_terms,
            exceptional_edge_tokens=edge_tokens,
            total=total,
        )
    return ExceptionSigmaEncoding(rows=rows, m=m)
