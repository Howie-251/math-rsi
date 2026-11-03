#!/usr/bin/env python3
"""Exact semantic timeout splitting for the N59 extremal-root v5 queue.

The functions in this module are deliberately solver-independent.  A split
is always a binary partition on one DIMACS literal from the *current* base
map.  Both signs are materialized, so a scheduler may never mistake a
promising subcase for an exhaustive treatment of its parent.
"""

from __future__ import annotations

import copy
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass


CLOSED_STATES = frozenset(
    {
        "RAW_UNSAT_NEW",
        "RAW_CLOSED_REPRESENTATIVE",
        "CERTIFIED_UNSAT",
        "STATIC_UNSAT",
    }
)
SPLITTABLE_STATES = frozenset({"TIMEOUT", "STALLED_NO_VALID_SPLIT"})


@dataclass(frozen=True)
class SemanticPivot:
    """A proved-exact Boolean predicate exposed by one base variable map."""

    literal: int
    predicate: str
    family: str
    priority: int
    kind: str = "boolean"
    threshold: int | None = None
    minimum: int | None = None
    maximum: int | None = None


def _literal(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value != 0:
        return value
    if isinstance(value, Mapping):
        candidate = value.get("literal")
        if isinstance(candidate, int) and not isinstance(candidate, bool) and candidate != 0:
            return candidate
    return None


def _family_priority(path: tuple[str, ...]) -> int:
    joined = ".".join(path).lower()
    if "nmax" in joined or "n_max" in joined or "max_count" in joined:
        return 0
    if "row" in joined or "r2" in joined or "endpoint" in joined:
        return 1
    if "kernel" in joined or "sigma" in joined or "ell" in joined:
        return 2
    if "triangle" in joined or "exception" in joined or "parent" in joined:
        return 3
    if "edge" in joined:
        return 4
    return 10


def _integer_metadata(value: Mapping[str, object], names: tuple[str, ...], default: int) -> int:
    for name in names:
        candidate = value.get(name)
        if isinstance(candidate, int) and not isinstance(candidate, bool):
            return candidate
    return default


def _threshold_from_path(path: tuple[str, ...], value: object) -> int | None:
    if isinstance(value, Mapping):
        explicit = value.get("threshold")
        if isinstance(explicit, int) and not isinstance(explicit, bool):
            return explicit
    for token in reversed(path):
        match = re.search(r"(?:^|_)(\d+)$", token)
        if match:
            return int(match.group(1))
    return None


def _is_threshold_family(path: tuple[str, ...]) -> bool:
    joined = ".".join(path).lower()
    return "_ge" in joined or ".ge" in joined or "nmax" in joined or "n_max" in joined


def _walk_semantic_table(
    value: object,
    path: tuple[str, ...],
    *,
    minimum: int = 0,
    maximum: int = 59,
) -> Iterable[SemanticPivot]:
    literal = _literal(value)
    if literal is not None:
        if isinstance(value, Mapping):
            predicate = str(value.get("predicate") or value.get("name") or ".".join(path))
            family = str(value.get("family") or (path[0] if path else "semantic"))
            priority = int(value.get("priority", _family_priority(path)))
        else:
            predicate = ".".join(path)
            family = path[0] if path else "semantic"
            priority = _family_priority(path)
        threshold = _threshold_from_path(path, value) if _is_threshold_family(path) else None
        yield SemanticPivot(
            literal,
            predicate,
            family,
            priority,
            kind="threshold_ge" if threshold is not None else "boolean",
            threshold=threshold,
            minimum=minimum if threshold is not None else None,
            maximum=maximum if threshold is not None else None,
        )
        return

    if isinstance(value, Mapping):
        local_minimum = _integer_metadata(value, ("minimum", "min_value", "domain_min"), minimum)
        local_maximum = _integer_metadata(value, ("maximum", "max_value", "domain_max"), maximum)
        for key in sorted(value, key=str):
            if str(key) in {"minimum", "min_value", "domain_min", "maximum", "max_value", "domain_max"}:
                continue
            yield from _walk_semantic_table(
                value[key], path + (str(key),), minimum=local_minimum, maximum=local_maximum
            )
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_semantic_table(
                item, path + (str(index),), minimum=minimum, maximum=maximum
            )


def semantic_split_candidates(base_map: Mapping[str, object]) -> list[SemanticPivot]:
    """Return unique split pivots in mathematical preference order.

    The encoder owns the semantics.  Only the table below
    ``selectors.semantic_split`` is considered; arbitrary SAT variables are
    intentionally not candidates.
    """

    selectors = base_map.get("selectors")
    if not isinstance(selectors, Mapping):
        return []
    table = selectors.get("semantic_split")
    if table is None:
        return []

    candidates = list(_walk_semantic_table(table, ()))
    candidates.sort(key=lambda item: (item.priority, item.family, item.predicate, abs(item.literal)))
    unique: list[SemanticPivot] = []
    seen_variables: set[int] = set()
    for item in candidates:
        variable = abs(item.literal)
        if variable in seen_variables:
            continue
        seen_variables.add(variable)
        unique.append(item)
    return unique


def _threshold_interval(
    candidates: Iterable[SemanticPivot],
    cube_units: Iterable[int],
) -> tuple[int, int]:
    values = list(candidates)
    minimum = max((item.minimum for item in values if item.minimum is not None), default=0)
    maximum = min((item.maximum for item in values if item.maximum is not None), default=59)
    units = {int(value) for value in cube_units}
    lower, upper = minimum, maximum
    for item in values:
        if item.threshold is None:
            continue
        if item.literal in units:
            lower = max(lower, item.threshold)
        elif -item.literal in units:
            upper = min(upper, item.threshold - 1)
    return lower, upper


def choose_semantic_pivot(task: Mapping[str, object], base_map: Mapping[str, object]) -> SemanticPivot | None:
    """Choose an unused exact pivot, bisecting monotone threshold intervals.

    Threshold implications are interpreted semantically.  For example,
    ``not Nmax_ge(2)`` fixes every higher threshold false even when those
    literals do not occur explicitly in the cube.
    """

    units = [int(value) for value in task.get("cube_units", [])]
    fixed = {abs(value) for value in units}
    candidates = semantic_split_candidates(base_map)
    families: dict[str, list[SemanticPivot]] = {}
    for pivot in candidates:
        if pivot.kind == "threshold_ge":
            families.setdefault(pivot.family, []).append(pivot)
    for family in sorted(families, key=lambda name: (min(x.priority for x in families[name]), name)):
        values = families[family]
        lower, upper = _threshold_interval(values, units)
        eligible = [
            item for item in values
            if item.threshold is not None
            and lower < item.threshold <= upper
            and abs(item.literal) not in fixed
        ]
        if eligible:
            midpoint = (lower + upper + 1) // 2
            return min(eligible, key=lambda item: (abs(item.threshold - midpoint), item.threshold))
    for pivot in candidates:
        if pivot.kind == "boolean" and abs(pivot.literal) not in fixed:
            return pivot
    return None


def _slug(value: str) -> str:
    rendered = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return rendered[:40] or "semantic"


def split_timeout_task(
    task: Mapping[str, object],
    pivot: SemanticPivot,
    *,
    child_timeout_seconds: int,
) -> tuple[dict, list[dict]]:
    """Replace one timed-out leaf by two complementary pending children."""

    state = str(task.get("state", ""))
    if state not in SPLITTABLE_STATES:
        raise ValueError(f"only an unresolved timeout can be split, got {state!r}")
    if child_timeout_seconds < 1:
        raise ValueError("child timeout must be positive")
    units = [int(value) for value in task.get("cube_units", [])]
    if abs(pivot.literal) in {abs(value) for value in units}:
        raise ValueError("semantic pivot is already fixed in the parent cube")

    parent = copy.deepcopy(dict(task))
    depth = int(parent.get("depth", 0)) + 1
    stem = f"{parent['task_id']}__d{depth}_{_slug(pivot.predicate)}"
    children: list[dict] = []
    for suffix, literal in (("yes", pivot.literal), ("no", -pivot.literal)):
        child = copy.deepcopy(dict(task))
        child_id = f"{stem}_{suffix}"
        child.update(
            task_id=child_id,
            case_id=child_id,
            parent_task_id=str(task["task_id"]),
            representative_id=str(task.get("representative_id", task["task_id"])),
            state="PENDING",
            depth=depth,
            cube_units=units + [literal],
            children=[],
            split_rule=None,
            timeout_seconds=int(child_timeout_seconds),
            attempts=[],
        )
        predicates = copy.deepcopy(list(task.get("semantic_predicates", [])))
        predicates.append(
            {
                "predicate": pivot.predicate,
                "family": pivot.family,
                "kind": pivot.kind,
                "threshold": pivot.threshold,
                "selector_literal": pivot.literal,
                "assigned_literal": literal,
                "truth": suffix == "yes",
            }
        )
        child["semantic_predicates"] = predicates
        case = copy.deepcopy(dict(child.get("case", {})))
        case.update(
            case_id=child_id,
            parent_task_id=str(task["task_id"]),
            representative_id=child["representative_id"],
            semantic_cube_units=list(child["cube_units"]),
            semantic_predicates=copy.deepcopy(predicates),
            split_predicate=pivot.predicate,
        )
        child["case"] = case
        children.append(child)

    parent.update(
        state="SPLIT_OPEN",
        children=[child["task_id"] for child in children],
        split_rule={
            "kind": "literal_complement",
            "literal": pivot.literal,
            "predicate": pivot.predicate,
            "family": pivot.family,
            "semantic_kind": pivot.kind,
            "threshold": pivot.threshold,
            "minimum": pivot.minimum,
            "maximum": pivot.maximum,
        },
    )
    return parent, children


def aggregate_split(parent: Mapping[str, object], children: Iterable[Mapping[str, object]]) -> str:
    """Return the parent state implied by a complete complementary split."""

    if parent.get("state") not in {"SPLIT_OPEN", "RAW_CLOSED_REPRESENTATIVE", "CERTIFIED_UNSAT"}:
        raise ValueError("parent is not a split node")
    expected_ids = [str(value) for value in parent.get("children", [])]
    lookup = {str(child["task_id"]): child for child in children}
    if len(expected_ids) != 2 or set(expected_ids) != set(lookup):
        return "SPLIT_OPEN"

    rule = parent.get("split_rule")
    if not isinstance(rule, Mapping) or rule.get("kind") != "literal_complement":
        raise ValueError("split parent lacks an exact complementary rule")
    literal = int(rule["literal"])
    base_units = [int(value) for value in parent.get("cube_units", [])]
    expected_cubes = {tuple(base_units + [literal]), tuple(base_units + [-literal])}
    actual_cubes = {tuple(int(value) for value in lookup[item].get("cube_units", [])) for item in expected_ids}
    if actual_cubes != expected_cubes:
        raise ValueError("child cubes do not cover both signs of the declared pivot")
    if any(child.get("template_id") != parent.get("template_id") for child in lookup.values()):
        raise ValueError("a split crossed base-template variable maps")

    states = [str(lookup[item].get("state", "")) for item in expected_ids]
    if all(state == "CERTIFIED_UNSAT" for state in states):
        return "CERTIFIED_UNSAT"
    if all(state in CLOSED_STATES for state in states):
        return "RAW_CLOSED_REPRESENTATIVE"
    return "SPLIT_OPEN"


def aggregate_ancestors(tasks: dict[str, dict], start_task_id: str) -> list[str]:
    """Propagate child closure to all ancestors and return changed IDs."""

    changed: list[str] = []
    current = tasks[start_task_id].get("parent_task_id")
    while current:
        parent = tasks[str(current)]
        children = [tasks[str(child_id)] for child_id in parent.get("children", [])]
        state = aggregate_split(parent, children)
        if state != parent.get("state"):
            parent["state"] = state
            changed.append(str(current))
        current = parent.get("parent_task_id")
    return changed


__all__ = [
    "CLOSED_STATES",
    "SPLITTABLE_STATES",
    "SemanticPivot",
    "aggregate_ancestors",
    "aggregate_split",
    "choose_semantic_pivot",
    "semantic_split_candidates",
    "split_timeout_task",
]
