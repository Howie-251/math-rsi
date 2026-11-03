"""Unary representation of an internal defect entry ``B = T - 1``."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .and_gate import BoolTerm, assert_term
from .cardinality import UnaryThresholds, enforce_exactly, unary_thresholds
from .cnf import CNFBuilder


@dataclass(frozen=True)
class DefectThresholds:
    """CNF terms representing one off-diagonal defect entry."""

    thresholds: UnaryThresholds
    support: BoolTerm
    weight_tokens: tuple[BoolTerm, ...]
    max_b: int

    def ge_b(self, level: int) -> BoolTerm:
        """Return the predicate ``B >= level``."""

        if level <= 0:
            return True
        if level > self.max_b:
            return False
        return self.thresholds.ge(level + 1)


def encode_b_entry(
    builder: CNFBuilder,
    terms: Iterable[BoolTerm],
    key,
    max_b: int = 5,
) -> DefectThresholds:
    """Encode ``T=sum(terms)``, ``B=T-1``, and ``0 <= B <= max_b``.

    For a graph pair, ``terms`` normally contains the adjacency literal and
    one exact AND literal for every possible common neighbour.  The returned
    support term is exactly ``B >= 1``.  The weight tokens sum to the integer
    value of ``B`` and can therefore be concatenated for a B-row equality.
    """

    values = tuple(terms)
    if max_b < 0:
        raise ValueError("max_b must be nonnegative")
    thresholds = unary_thresholds(
        builder,
        values,
        min(len(values), max_b + 2),
        ("B_equals_T_minus_one", key),
        kind="B_threshold",
    )
    # T >= 1 is B >= 0.  T <= max_b+1 is B <= max_b.
    assert_term(builder, thresholds.ge(1), True)
    if max_b + 2 <= len(values):
        assert_term(builder, thresholds.ge(max_b + 2), False)

    support = thresholds.ge(2)
    weight_tokens = tuple(
        thresholds.ge(level) for level in range(2, max_b + 2)
    )
    return DefectThresholds(
        thresholds=thresholds,
        support=support,
        weight_tokens=weight_tokens,
        max_b=max_b,
    )


def enforce_b_row_sum(
    builder: CNFBuilder,
    entries: Iterable[DefectThresholds],
    target: int,
    key,
) -> UnaryThresholds:
    """Enforce the exact weighted row sum of several B entries."""

    tokens = tuple(
        token
        for entry in entries
        for token in entry.weight_tokens
    )
    return enforce_exactly(builder, tokens, target, ("B_row_sum", key))


def defect_value_from_total(total: int) -> int:
    if total < 1:
        raise ValueError("a nonnegative defect entry requires T >= 1")
    return total - 1

