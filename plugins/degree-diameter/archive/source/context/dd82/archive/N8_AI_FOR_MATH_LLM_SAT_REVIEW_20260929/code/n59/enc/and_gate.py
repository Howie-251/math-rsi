"""Exact Boolean AND gates with constant propagation."""

from __future__ import annotations

from typing import TypeAlias

from .cnf import CNFBuilder


BoolTerm: TypeAlias = int | bool


def _check_term(term: BoolTerm) -> None:
    if isinstance(term, bool):
        return
    if not isinstance(term, int) or term == 0:
        raise ValueError(f"expected a nonzero literal or Boolean constant: {term!r}")


def add_simplified_clause(builder: CNFBuilder, *terms: BoolTerm) -> bool:
    """Add a clause after simplifying Boolean constants and tautologies.

    Return ``True`` exactly when a non-tautological clause was emitted.
    """

    literals: list[int] = []
    seen: set[int] = set()
    for term in terms:
        _check_term(term)
        if term is True:
            return False
        if term is False:
            continue
        literal = int(term)
        if -literal in seen:
            return False
        if literal not in seen:
            literals.append(literal)
            seen.add(literal)
    builder.add_clause(*literals)
    return True


def negate(term: BoolTerm) -> BoolTerm:
    _check_term(term)
    return not term if isinstance(term, bool) else -term


def assert_term(builder: CNFBuilder, term: BoolTerm, value: bool = True) -> None:
    """Assert a literal/constant to the requested truth value."""

    required = term if value else negate(term)
    add_simplified_clause(builder, required)


def encode_iff_and(
    builder: CNFBuilder,
    out: int,
    left: BoolTerm,
    right: BoolTerm,
) -> None:
    """Encode ``out <-> (left AND right)`` in both directions."""

    if not isinstance(out, int) or isinstance(out, bool) or out <= 0:
        raise ValueError("AND output must be a positive DIMACS variable")
    _check_term(left)
    _check_term(right)
    add_simplified_clause(builder, -out, left)
    add_simplified_clause(builder, -out, right)
    add_simplified_clause(builder, out, negate(left), negate(right))


def add_iff_and(
    builder: CNFBuilder,
    left: BoolTerm,
    right: BoolTerm,
    key,
    kind: str = "and",
) -> BoolTerm:
    """Return a term exactly equivalent to ``left AND right``.

    Trivial constant, duplicate, and complementary inputs are simplified
    without allocating an auxiliary variable.  Every nontrivial gate uses the
    full three-clause equivalence, never a one-way witness implication.
    """

    _check_term(left)
    _check_term(right)
    if left is False or right is False:
        return False
    if left is True:
        return right
    if right is True:
        return left
    if left == right:
        return left
    if left == -right:
        return False
    out = builder.var(("and", key), kind)
    encode_iff_and(builder, out, left, right)
    return out

