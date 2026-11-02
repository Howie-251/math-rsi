"""Exact unary-threshold cardinality encodings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .and_gate import BoolTerm, assert_term
from .cnf import CNFBuilder


@dataclass(frozen=True)
class UnaryThresholds:
    """Threshold terms for a sum of Boolean literals.

    ``ge(level)`` denotes that at least ``level`` input occurrences are true.
    Repeated literals are retained, so the same variable may intentionally
    contribute an integer weight.
    """

    terms: tuple[BoolTerm, ...]
    input_count: int
    encoded_maximum: int

    def ge(self, level: int) -> BoolTerm:
        if level <= 0:
            return True
        if level > self.input_count:
            return False
        if level > self.encoded_maximum:
            raise ValueError(
                f"threshold {level} was not encoded; maximum is "
                f"{self.encoded_maximum}"
            )
        return self.terms[level - 1]


def _validate_inputs(literals: Iterable[BoolTerm]) -> tuple[BoolTerm, ...]:
    values = tuple(literals)
    for literal in values:
        if isinstance(literal, bool):
            continue
        if not isinstance(literal, int) or literal == 0:
            raise ValueError(
                f"cardinality input must be a nonzero literal or constant: "
                f"{literal!r}"
            )
    return values


def unary_thresholds(
    builder: CNFBuilder,
    literals: Iterable[BoolTerm],
    maximum: int | None,
    key,
    kind: str = "threshold",
) -> UnaryThresholds:
    """Encode exact predicates ``sum(literals) >= 1,...,maximum``.

    Every auxiliary output is equivalent to its threshold predicate, so it is
    safe to use in either polarity and in subsequent weighted equalities.
    """

    inputs = _validate_inputs(literals)
    total_count = len(inputs)
    if maximum is None:
        maximum = total_count
    if maximum < 0:
        raise ValueError("maximum threshold must be nonnegative")
    maximum = min(int(maximum), total_count)

    fixed_true = sum(term is True for term in inputs)
    dynamic = tuple(term for term in inputs if not isinstance(term, bool))
    dynamic_maximum = max(0, maximum - fixed_true)
    previous: dict[int, int] = {}

    for index, literal in enumerate(dynamic, start=1):
        current: dict[int, int] = {}
        for threshold in range(1, min(index, dynamic_maximum) + 1):
            out = builder.var(
                (
                    "unary_threshold",
                    key,
                    len(dynamic),
                    fixed_true,
                    index,
                    threshold,
                ),
                kind,
            )
            current[threshold] = out
            same = previous.get(threshold)
            lower: int | bool = (
                True if threshold == 1 else previous[threshold - 1]
            )

            # same OR (literal AND lower) -> out
            if same is not None:
                builder.add_clause(-same, out)
            if lower is True:
                builder.add_clause(-literal, out)
            else:
                builder.add_clause(-literal, -lower, out)

            # out -> same OR literal, and out -> same OR lower
            if same is None:
                builder.add_clause(-out, literal)
            else:
                builder.add_clause(-out, same, literal)
            if lower is not True:
                if same is None:
                    builder.add_clause(-out, lower)
                else:
                    builder.add_clause(-out, same, lower)
        previous = current

    rendered: list[BoolTerm] = []
    possible = fixed_true + len(dynamic)
    for level in range(1, maximum + 1):
        if level <= fixed_true:
            rendered.append(True)
        elif level > possible:
            rendered.append(False)
        else:
            rendered.append(previous[level - fixed_true])
    return UnaryThresholds(tuple(rendered), total_count, maximum)


def enforce_at_most(
    builder: CNFBuilder,
    literals: Iterable[BoolTerm],
    bound: int,
    key,
) -> UnaryThresholds:
    inputs = _validate_inputs(literals)
    maximum = min(len(inputs), max(0, bound + 1))
    thresholds = unary_thresholds(
        builder, inputs, maximum, ("at_most", key)
    )
    if bound < 0:
        builder.add_clause()
    elif bound < len(inputs):
        assert_term(builder, thresholds.ge(bound + 1), False)
    return thresholds


def enforce_at_least(
    builder: CNFBuilder,
    literals: Iterable[BoolTerm],
    bound: int,
    key,
) -> UnaryThresholds:
    inputs = _validate_inputs(literals)
    maximum = min(len(inputs), max(0, bound))
    thresholds = unary_thresholds(
        builder, inputs, maximum, ("at_least", key)
    )
    if bound > len(inputs):
        builder.add_clause()
    elif bound > 0:
        assert_term(builder, thresholds.ge(bound), True)
    return thresholds


def enforce_exactly(
    builder: CNFBuilder,
    literals: Iterable[BoolTerm],
    target: int,
    key,
) -> UnaryThresholds:
    inputs = _validate_inputs(literals)
    maximum = min(len(inputs), max(0, target + 1))
    thresholds = unary_thresholds(
        builder, inputs, maximum, ("exactly", key)
    )
    if target < 0 or target > len(inputs):
        builder.add_clause()
        return thresholds
    if target > 0:
        assert_term(builder, thresholds.ge(target), True)
    if target < len(inputs):
        assert_term(builder, thresholds.ge(target + 1), False)
    return thresholds


def enforce_exactly_one(
    builder: CNFBuilder,
    literals: Iterable[BoolTerm],
    key,
) -> UnaryThresholds:
    return enforce_exactly(builder, literals, 1, key)

