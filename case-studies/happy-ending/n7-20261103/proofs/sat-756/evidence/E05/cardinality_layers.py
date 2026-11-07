"""Order-generic exact-cardinality cells for the 35 down-set states.

This module is deliberately independent of the strict-N25 transition
campaigns.  A logical cell ``A[r,e]`` is materialized from a fresh formula of
order ``N = 26 + e - r`` and constrains the *type occupancy* variables:

``exactly e`` exceptional state types are occupied and exactly ``r - 1``
ordinary state types are missing.  The strict formula contains the global
weak-7-gon exclusion; the relaxed discovery formula omits only that target
layer.

The base :class:`~lib.sat_tseitin.SATInstance` is never mutated by a cell.
Cardinality auxiliaries instead live in an immutable supplemental CNF with an
explicit semantic variable registry.  This permits several N26-spine cells to
share one validated base without cross-cell contamination.

New cells append entailed state-to-terminal-path bridges and F3-main occupied
rank pruning by default. ``bridges=False`` replays pure exact encoding;
``f3_main=False`` with bridges replays the historical bridges-only CNF.
"""

from __future__ import annotations

import importlib.metadata
import hashlib
import itertools
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Iterable, Mapping, Sequence

from lib.downset_state import (
    EXCEPTIONAL_KIND,
    ORDINARY_KIND,
    PROFILE_SCHEMA,
    STATE_756_SPEC,
    classify_state,
    enumerate_states,
    exceptional_states,
    extract_downset_profile,
    ordinary_states,
)
from lib.downset_state_cnf import (
    DOWNSET_STATE_CLAUSE_GROUP,
    PATH5_FAMILY,
    PATH6_FAMILY,
    DownsetStateEncoding,
    add_downset_state_encoding,
)
from lib.erdos import etv_signotope, etv_signotope_extension
from state_charging import corpus as corpus_api
from state_charging import obligations as obligation_api
from state_charging.f3_main_rank import F3MainEncoding, build_f3_main_rank


STRICT_NO_TARGET = "strict_no_target"
TARGET_ALLOWED_RELAXED = "target_allowed_relaxed"
FORMULA_MODES = (STRICT_NO_TARGET, TARGET_ALLOWED_RELAXED)

CELL_SCHEMA = "state_charging_cardinality_cell_v1"
REGISTRY_SCHEMA = "state_charging_cardinality_registry_v1"
SCOPE_SCHEMA = "state_charging_cardinality_formula_scope_v1"
CARDINALITY_PLAN_SCHEMA = "state_charging_exact_em_cardinality_v1"
AUXILIARY_SCHEMA = "state_charging_cardinality_auxiliary_v1"
PROFILE_AUDIT_SCHEMA = "state_charging_cardinality_profile_audit_v1"
SAT_AUDIT_SCHEMA = "state_charging_cardinality_sat_audit_v1"
BRIDGES_CARDINALITY_ENCODING = "legacy_exact_with_state_path_bridges_v1"
DEFAULT_CARDINALITY_ENCODING = "legacy_exact_with_state_path_bridges_f3_main_v1"

ORDINARY_STATE_COUNT = 25
EXCEPTIONAL_STATE_COUNT = 10
TOTAL_STATE_COUNT = ORDINARY_STATE_COUNT + EXCEPTIONAL_STATE_COUNT
MIN_CELL_ORDER = 26
MAX_CELL_ORDER = 35
CELL_COUNT = 55


class CardinalityValidationError(ValueError):
    """Raised when a cell, formula, model, or evidence object fails closed."""


def _plain_int(
    value: Any,
    *,
    label: str,
    minimum: int | None = None,
    maximum: int | None = None,
) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CardinalityValidationError(f"{label} must be a plain integer")
    if minimum is not None and value < minimum:
        raise CardinalityValidationError(f"{label} must be at least {minimum}")
    if maximum is not None and value > maximum:
        raise CardinalityValidationError(f"{label} must be at most {maximum}")
    return value


def _literal(value: Any, *, label: str) -> int:
    if hasattr(value, "_lit"):
        value = value._lit
    if isinstance(value, bool) or not isinstance(value, int) or value == 0:
        raise CardinalityValidationError(f"{label} must be a nonzero SAT literal")
    return value


def _state_token(rows: Sequence[int]) -> str:
    normalized = tuple(
        _plain_int(value, label="state row", minimum=0) for value in rows
    )
    return "G" + "".join(str(value) for value in normalized)


def _same_json(left: Any, right: Any) -> bool:
    """Compare JSON-shaped evidence without Python's ``bool == int`` leak."""

    return obligation_api.stable_sha256(left) == obligation_api.stable_sha256(right)


def _canonical_state_tuple(rows: Sequence[Any], *, label: str) -> tuple[int, ...]:
    if isinstance(rows, (str, bytes)):
        raise CardinalityValidationError(f"{label} must be a state-row sequence")
    try:
        raw = tuple(rows)
    except TypeError as exc:
        raise CardinalityValidationError(
            f"{label} must be a state-row sequence"
        ) from exc
    state = tuple(
        _plain_int(value, label=f"{label} row", minimum=0) for value in raw
    )
    try:
        classify_state(state)
    except ValueError as exc:
        raise CardinalityValidationError(f"{label} is not a canonical state") from exc
    return state


@dataclass(frozen=True, order=True)
class CardinalityCell:
    """One exact bad cell ``A[r,e]`` from the triangular 55-cell registry."""

    r: int
    e: int
    missing_ordinary_count: int = field(init=False, compare=False)
    order: int = field(init=False, compare=False)
    case_id: str = field(init=False, compare=False)

    def __post_init__(self) -> None:
        r = _plain_int(self.r, label="r", minimum=1, maximum=10)
        e = _plain_int(self.e, label="e", minimum=r, maximum=10)
        missing = r - 1
        order = 26 + e - r
        object.__setattr__(self, "r", r)
        object.__setattr__(self, "e", e)
        object.__setattr__(self, "missing_ordinary_count", missing)
        object.__setattr__(self, "order", order)
        object.__setattr__(
            self,
            "case_id",
            f"cardinality_A_r{r:02d}_e{e:02d}_N{order:02d}",
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": CELL_SCHEMA,
            "case_id": self.case_id,
            "r": self.r,
            "e": self.e,
            "missing_ordinary_count": self.missing_ordinary_count,
            "order": self.order,
            "occupied_ordinary_count": ORDINARY_STATE_COUNT
            - self.missing_ordinary_count,
            "occupied_state_count": (
                ORDINARY_STATE_COUNT - self.missing_ordinary_count + self.e
            ),
            "count_identity": "N=(25-m)+e=26+e-r",
        }


def normalize_cell(raw: CardinalityCell | Mapping[str, Any]) -> CardinalityCell:
    """Normalize a cell and reject repaired derived fields or extra keys."""

    if isinstance(raw, CardinalityCell):
        return CardinalityCell(raw.r, raw.e)
    if not isinstance(raw, Mapping):
        raise CardinalityValidationError("cell must be a mapping or CardinalityCell")

    allowed = {
        "schema",
        "case_id",
        "r",
        "e",
        "missing_ordinary_count",
        "order",
        "occupied_ordinary_count",
        "occupied_state_count",
        "count_identity",
    }
    extra = set(raw) - allowed
    if extra:
        raise CardinalityValidationError(
            f"cell has unsupported fields: {sorted(extra)}"
        )
    if "r" not in raw or "e" not in raw:
        raise CardinalityValidationError("cell must contain r and e")
    cell = CardinalityCell(raw["r"], raw["e"])
    canonical = cell.to_dict()
    for key, value in raw.items():
        if key not in canonical or not _same_json(value, canonical[key]):
            raise CardinalityValidationError(
                f"cell field {key!r} disagrees with canonical A[r,e]"
            )
    return cell


def all_cells() -> tuple[CardinalityCell, ...]:
    return tuple(CardinalityCell(r, e) for r in range(1, 11) for e in range(r, 11))


def c1_cells() -> tuple[CardinalityCell, ...]:
    return tuple(cell for cell in all_cells() if cell.r == 1)


def n26_spine_cells() -> tuple[CardinalityCell, ...]:
    return tuple(cell for cell in all_cells() if cell.order == 26)


def registry() -> dict[str, Any]:
    cells = all_cells()
    payload: dict[str, Any] = {
        "schema": REGISTRY_SCHEMA,
        "cell_order": "r_ascending_then_e_ascending",
        "cell_count": len(cells),
        "ordinary_state_count": ORDINARY_STATE_COUNT,
        "exceptional_state_count": EXCEPTIONAL_STATE_COUNT,
        "state_count": TOTAL_STATE_COUNT,
        "formula_modes": list(FORMULA_MODES),
        "cells": [cell.to_dict() for cell in cells],
        "projections": {
            "C1": [cell.case_id for cell in c1_cells()],
            "N26_spine": [cell.case_id for cell in n26_spine_cells()],
        },
        "theorem_cells": {
            "C_r": "exact_e>=r_and_exact_m=r-1_bad_cells",
            "coverage": "1<=r<=e<=10",
        },
    }
    payload["registry_sha256"] = obligation_api.stable_sha256(payload)
    return payload


def validate_registry(raw: Mapping[str, Any]) -> dict[str, Any]:
    """Require byte-shape-equivalent canonical JSON content for the registry."""

    if not isinstance(raw, Mapping):
        raise CardinalityValidationError("registry must be a mapping")
    expected = registry()
    if obligation_api.stable_sha256(dict(raw)) != obligation_api.stable_sha256(expected):
        raise CardinalityValidationError(
            "registry differs from the canonical 55-cell order or identity"
        )
    # Re-run cell normalization so scalar type/range errors have a local gate.
    raw_cells = raw.get("cells")
    if not isinstance(raw_cells, list) or len(raw_cells) != CELL_COUNT:
        raise CardinalityValidationError("registry must contain exactly 55 cells")
    normalized = tuple(normalize_cell(item) for item in raw_cells)
    if normalized != all_cells():
        raise CardinalityValidationError("registry cells are duplicated or reordered")
    return expected


def canonical_state_catalog_sha256() -> str:
    """Return the independently reproducible identity of the 35-state catalog."""

    catalog = enumerate_states()
    if len(catalog) != TOTAL_STATE_COUNT:
        raise CardinalityValidationError("canonical state catalog count drifted")
    return corpus_api.state_catalog_sha256(catalog)


def _normalize_mode(mode: Any) -> str:
    if not isinstance(mode, str) or mode not in FORMULA_MODES:
        raise CardinalityValidationError(
            f"formula mode must be one of {FORMULA_MODES!r}"
        )
    return mode


def canonical_formula_scope(mode: str, order: int) -> dict[str, Any]:
    """Return the exact order-generic scope statement sealed with each formula."""

    mode = _normalize_mode(mode)
    order = _plain_int(
        order,
        label="order",
        minimum=MIN_CELL_ORDER,
        maximum=MAX_CELL_ORDER,
    )
    return {
        "schema": SCOPE_SCHEMA,
        "mode": mode,
        "builder": (
            "lib.erdos.etv_signotope"
            if mode == STRICT_NO_TARGET
            else "lib.erdos.etv_signotope_extension"
        ),
        "order": order,
        "problem": {"n": 7, "a": 5, "b": 6},
        "path_bounds": {
            "path5_forbidden_length": 5,
            "path6_forbidden_length": 6,
        },
        "signotope": True,
        "global_no_7_gon": mode == STRICT_NO_TARGET,
        "state_encoding": "canonical_35_state_no_start_v1",
        "state_injection": "paper_lemma_from_complete_coloring_and_path_bounds",
        "symmetry_breaking": False,
    }


def _base_problem(instance: Any) -> Mapping[str, Any]:
    metadata = getattr(instance, "_metadata", None)
    if not isinstance(metadata, Mapping):
        raise CardinalityValidationError("base formula has no metadata mapping")
    problem = metadata.get("problem")
    if not isinstance(problem, Mapping):
        raise CardinalityValidationError("base formula has no problem metadata")
    return problem


def _exact_triple_order(instance: Any, expected_order: int) -> int:
    triples = getattr(instance, "v", None)
    if not isinstance(triples, Mapping):
        raise CardinalityValidationError("base formula has no triple-variable map")
    expected_keys = set(itertools.combinations(range(expected_order), 3))
    actual_keys = set(triples)
    if actual_keys != expected_keys:
        missing = next(iter(sorted(expected_keys - actual_keys)), None)
        try:
            extra = next(iter(sorted(actual_keys - expected_keys)), None)
        except TypeError:
            extra = next(iter(actual_keys - expected_keys), None)
        raise CardinalityValidationError(
            "base triple map is not exactly the declared order "
            f"(first_missing={missing}, first_extra={extra})"
        )
    inferred = (
        max(max(triple) for triple in actual_keys) + 1
        if actual_keys
        else expected_order
    )
    if inferred != expected_order:
        raise CardinalityValidationError(
            "inferred triple-map order differs from the declared order"
        )
    for triple, atom in triples.items():
        if not isinstance(triple, tuple) or len(triple) != 3:
            raise CardinalityValidationError("base triple-map key is malformed")
        if getattr(atom, "_instance", None) is not instance:
            raise CardinalityValidationError(
                f"base triple atom {triple!r} belongs to another instance"
            )
        literal = _literal(atom, label=f"triple atom {triple!r}")
        if literal < 1:
            raise CardinalityValidationError(
                f"base triple atom {triple!r} is not a positive atom"
            )
    return inferred


def _normalized_base_clauses(instance: Any) -> tuple[tuple[int, ...], ...]:
    num_vars = _plain_int(
        getattr(instance, "_num_vars", None),
        label="base num_vars",
        minimum=0,
    )
    raw_clauses = getattr(instance, "_clauses", None)
    if not isinstance(raw_clauses, list):
        raise CardinalityValidationError("base formula has no raw clause list")
    normalized: list[tuple[int, ...]] = []
    for clause_index, raw_clause in enumerate(raw_clauses):
        if not isinstance(raw_clause, (list, tuple)):
            raise CardinalityValidationError(
                f"base clause {clause_index} is not a literal sequence"
            )
        clause: list[int] = []
        for value in raw_clause:
            literal = _literal(value, label=f"base clause {clause_index} literal")
            if abs(literal) > num_vars:
                raise CardinalityValidationError(
                    f"base clause {clause_index} exceeds num_vars"
                )
            clause.append(literal)
        normalized.append(tuple(clause))
    return tuple(normalized)


def _validate_variable_ledger(instance: Any) -> None:
    num_vars = int(instance._num_vars)
    var_names = getattr(instance, "_var_names", None)
    name_to_var = getattr(instance, "_name_to_var", None)
    var_roles = getattr(instance, "_var_roles", None)
    if not all(isinstance(item, Mapping) for item in (var_names, name_to_var, var_roles)):
        raise CardinalityValidationError("base variable ledgers are missing")
    # Tseitin gates created by Clauses.__and__/__or__ intentionally use
    # SATInstance._fresh_var and are anonymous.  The public ledger therefore
    # covers named semantic atoms, not the whole numeric range.
    named_ids = set(var_names)
    if set(var_roles) != named_ids:
        raise CardinalityValidationError("base named-variable role ledger drifted")
    if any(
        isinstance(variable, bool)
        or not isinstance(variable, int)
        or variable < 1
        or variable > num_vars
        for variable in named_ids
    ):
        raise CardinalityValidationError("base named-variable ID is out of range")
    if len(name_to_var) != len(var_names):
        raise CardinalityValidationError("base variable names are not unique")
    for variable, name in var_names.items():
        if name_to_var.get(name) != variable:
            raise CardinalityValidationError("base variable ledger is not bijective")
        role = var_roles.get(variable)
        if not isinstance(role, Mapping) or role.get("var") != variable or role.get("name") != name:
            raise CardinalityValidationError("base variable-role ledger drifted")


def validate_order_contract(
    instance: Any,
    encoding: DownsetStateEncoding,
    expected_order: int,
) -> None:
    """Reject the prefix-encoding loophole in the public state encoder."""

    expected_order = _plain_int(
        expected_order,
        label="expected order",
        minimum=MIN_CELL_ORDER,
        maximum=MAX_CELL_ORDER,
    )
    problem = _base_problem(instance)
    for field_name, expected in (("n", 7), ("a", 5), ("b", 6), ("N", expected_order)):
        value = problem.get(field_name)
        if isinstance(value, bool) or value != expected:
            raise CardinalityValidationError(
                f"base problem.{field_name} differs from {expected!r}"
            )
    if problem.get("flip_cup") is not True:
        raise CardinalityValidationError("base formula must use flip_cup=True")
    _exact_triple_order(instance, expected_order)
    if encoding.instance is not instance:
        raise CardinalityValidationError("state encoding belongs to another instance")
    if encoding.order != expected_order:
        raise CardinalityValidationError(
            "state encoding order differs from cell/base order"
        )
    if encoding.include_start_endpoints is not False:
        raise CardinalityValidationError(
            "cardinality layer must use the no-start state encoding"
        )


def _validate_state_encoding(
    instance: Any,
    encoding: DownsetStateEncoding,
    order: int,
) -> None:
    validate_order_contract(instance, encoding, order)
    catalog = enumerate_states()
    ordinary = ordinary_states()
    exceptional = exceptional_states()
    if len(catalog) != TOTAL_STATE_COUNT or len(ordinary) != 25 or len(exceptional) != 10:
        raise CardinalityValidationError("canonical 35-state catalog count drifted")
    if encoding.catalog != catalog:
        raise CardinalityValidationError("state encoding catalog order drifted")
    if encoding.spec != STATE_756_SPEC:
        raise CardinalityValidationError("state encoding uses noncanonical semantics")
    if encoding.catalog_sha256 != corpus_api.state_catalog_sha256(catalog):
        raise CardinalityValidationError("state encoding catalog hash drifted")
    if encoding.ordinary_catalog != ordinary or encoding.exceptional_catalog != exceptional:
        raise CardinalityValidationError("ordinary/exceptional catalog split drifted")
    if getattr(instance, "downset_state_encoding", None) is not encoding:
        raise CardinalityValidationError("state encoding is not attached canonically")
    if encoding.group != DOWNSET_STATE_CLAUSE_GROUP:
        raise CardinalityValidationError("state encoding clause group drifted")
    if encoding.start_vars or encoding.start_path_vars:
        raise CardinalityValidationError("no-start encoding unexpectedly created start atoms")

    expected_state_keys = {
        (vertex, state)
        for vertex in range(1, order + 1)
        for state in catalog
    }
    if set(encoding.state_vars) != expected_state_keys:
        raise CardinalityValidationError("state-variable grid is incomplete")
    if tuple(encoding.occupancy_vars) != catalog:
        raise CardinalityValidationError("occupancy-variable order is noncanonical")
    if set(encoding.full_vars) != set(range(1, order + 1)):
        raise CardinalityValidationError("full-state variable map is incomplete")
    if set(encoding.cell_vars) != {
        (vertex, x, y)
        for vertex in range(1, order + 1)
        for x in range(1, STATE_756_SPEC.width + 1)
        for y in range(1, STATE_756_SPEC.height + 1)
    }:
        raise CardinalityValidationError("state-cell variable grid is incomplete")
    handles = (
        *encoding.state_vars.values(),
        *encoding.occupancy_vars.values(),
        *encoding.full_vars.values(),
        *encoding.cell_vars.values(),
        *encoding.terminal_path_vars.values(),
    )
    seen_literals: set[int] = set()
    for atom in handles:
        if getattr(atom, "_instance", None) is not instance:
            raise CardinalityValidationError("state atom belongs to another instance")
        literal = _literal(atom, label="state-encoding atom")
        if literal < 1 or literal > instance._num_vars:
            raise CardinalityValidationError("state atom literal is out of range")
        if literal in seen_literals:
            raise CardinalityValidationError("state encoding reuses an output atom")
        seen_literals.add(literal)


@dataclass(frozen=True)
class CardinalityEnvironment:
    mode: str
    order: int
    instance: Any = field(repr=False, compare=False)
    encoding: DownsetStateEncoding = field(repr=False, compare=False)
    base_num_vars: int
    base_clauses: tuple[tuple[int, ...], ...] = field(repr=False)
    base_sha256: str
    scope: Mapping[str, Any]


def validate_environment(environment: CardinalityEnvironment) -> None:
    if not isinstance(environment, CardinalityEnvironment):
        raise TypeError("environment must be a CardinalityEnvironment")
    mode = _normalize_mode(environment.mode)
    order = _plain_int(
        environment.order,
        label="environment order",
        minimum=MIN_CELL_ORDER,
        maximum=MAX_CELL_ORDER,
    )
    _validate_state_encoding(environment.instance, environment.encoding, order)
    _validate_variable_ledger(environment.instance)
    clauses = _normalized_base_clauses(environment.instance)
    if environment.base_num_vars != environment.instance._num_vars:
        raise CardinalityValidationError("environment base_num_vars drifted")
    if environment.base_clauses != clauses:
        raise CardinalityValidationError("environment base clauses drifted")
    digest = obligation_api.formula_sha256(environment.base_num_vars, clauses)
    if environment.base_sha256 != digest:
        raise CardinalityValidationError("environment base formula hash drifted")

    include_no_gon = getattr(environment.instance, "include_no_gon", None)
    expected_no_gon = mode == STRICT_NO_TARGET
    if include_no_gon is not expected_no_gon:
        raise CardinalityValidationError("formula mode/global target layer mismatch")
    groups = getattr(environment.instance, "_group_clause_counts", None)
    if not isinstance(groups, Mapping):
        raise CardinalityValidationError("base formula has no clause-group ledger")
    if groups.get("pseudolinear", 0) <= 0:
        raise CardinalityValidationError("base formula has no signotope layer")
    if (groups.get("no_7_gon", 0) > 0) is not expected_no_gon:
        raise CardinalityValidationError("no_7_gon clause-group scope mismatch")

    expected_scope = canonical_formula_scope(mode, order)
    if not _same_json(dict(environment.scope), expected_scope):
        raise CardinalityValidationError("formula scope metadata drifted")


def prepare_environment(mode: str, order: int) -> CardinalityEnvironment:
    """Build and validate a fresh strict or target-allowed arbitrary-order base."""

    mode = _normalize_mode(mode)
    order = _plain_int(
        order,
        label="order",
        minimum=MIN_CELL_ORDER,
        maximum=MAX_CELL_ORDER,
    )
    if mode == STRICT_NO_TARGET:
        instance = etv_signotope(7, 5, 6, order)
    else:
        instance = etv_signotope_extension(7, 5, 6, order)
    encoding = add_downset_state_encoding(
        instance,
        order=order,
        include_start_endpoints=False,
    )
    clauses = _normalized_base_clauses(instance)
    num_vars = int(instance._num_vars)
    scope = MappingProxyType(canonical_formula_scope(mode, order))
    environment = CardinalityEnvironment(
        mode=mode,
        order=order,
        instance=instance,
        encoding=encoding,
        base_num_vars=num_vars,
        base_clauses=clauses,
        base_sha256=obligation_api.formula_sha256(num_vars, clauses),
        scope=scope,
    )
    validate_environment(environment)
    return environment


@dataclass(frozen=True)
class CardinalityAuxiliary:
    literal: int
    name: str
    role: str
    component_id: str
    ordinal: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": AUXILIARY_SCHEMA,
            "literal": self.literal,
            "name": self.name,
            "role": self.role,
            "component_id": self.component_id,
            "ordinal": self.ordinal,
        }


@dataclass(frozen=True)
class ExactEMCardinality:
    base_num_vars: int
    num_vars: int
    exceptional_count: int
    missing_ordinary_count: int
    exceptional_literals: tuple[int, ...]
    missing_ordinary_literals: tuple[int, ...]
    clauses: tuple[tuple[int, ...], ...]
    components: tuple[Mapping[str, Any], ...]
    auxiliary_variables: tuple[CardinalityAuxiliary, ...]

    def to_dict(self, *, include_clauses: bool = False) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "schema": CARDINALITY_PLAN_SCHEMA,
            "predicate": "exact_exceptional_occupancy_and_exact_missing_ordinary",
            "base_num_vars": self.base_num_vars,
            "num_vars": self.num_vars,
            "exceptional_count": self.exceptional_count,
            "missing_ordinary_count": self.missing_ordinary_count,
            "exceptional_literals": list(self.exceptional_literals),
            "missing_ordinary_literals": list(self.missing_ordinary_literals),
            "component_count": len(self.components),
            "components": [dict(item) for item in self.components],
            "auxiliary_variable_count": len(self.auxiliary_variables),
            "auxiliary_variables": [item.to_dict() for item in self.auxiliary_variables],
            "auxiliary_variables_sha256": obligation_api.stable_sha256(
                [item.to_dict() for item in self.auxiliary_variables]
            ),
            "clause_count": len(self.clauses),
            "clauses_sha256": obligation_api.stable_sha256(
                [list(clause) for clause in self.clauses]
            ),
            "encoding_backend": "state_charging.obligations.encode_at_most_exact",
            "python_sat_version": _python_sat_version(),
        }
        if include_clauses:
            payload["clauses"] = [list(clause) for clause in self.clauses]
        return payload


def _python_sat_version() -> str:
    try:
        return importlib.metadata.version("python-sat")
    except importlib.metadata.PackageNotFoundError:
        return "unavailable"


def _append_at_most_component(
    *,
    component_id: str,
    meaning: str,
    literals: Sequence[int],
    bound: int,
    top_id: int,
    clauses: list[tuple[int, ...]],
    components: list[Mapping[str, Any]],
    auxiliaries: list[CardinalityAuxiliary],
) -> int:
    encoded = obligation_api.encode_at_most_exact(
        literals,
        bound,
        top_id=top_id,
    )
    component = encoded.to_dict(include_clauses=False)
    component["component_id"] = component_id
    component["meaning"] = meaning
    component["auxiliary_first"] = top_id + 1 if encoded.num_vars > top_id else None
    component["auxiliary_last"] = encoded.num_vars if encoded.num_vars > top_id else None
    components.append(MappingProxyType(component))
    clauses.extend(encoded.clauses)
    for ordinal, literal in enumerate(range(top_id + 1, encoded.num_vars + 1), 1):
        auxiliaries.append(
            CardinalityAuxiliary(
                literal=literal,
                name=f"cardinality_aux({component_id},{ordinal})",
                role="cardinality_totalizer_auxiliary",
                component_id=component_id,
                ordinal=ordinal,
            )
        )
    return encoded.num_vars


def encode_exact_em_cardinality(
    exceptional_literals: Iterable[int],
    missing_ordinary_literals: Iterable[int],
    *,
    exceptional_count: int,
    missing_ordinary_count: int,
    top_id: int,
) -> ExactEMCardinality:
    """Encode exact ``e`` and ``m`` counts with four chained at-most CNFs."""

    top_id = _plain_int(top_id, label="top_id", minimum=0)
    e_count = _plain_int(
        exceptional_count,
        label="exceptional_count",
        minimum=0,
        maximum=EXCEPTIONAL_STATE_COUNT,
    )
    m_count = _plain_int(
        missing_ordinary_count,
        label="missing_ordinary_count",
        minimum=0,
        maximum=ORDINARY_STATE_COUNT,
    )
    exceptional = tuple(
        _literal(value, label="exceptional occupancy literal")
        for value in exceptional_literals
    )
    missing = tuple(
        _literal(value, label="missing ordinary literal")
        for value in missing_ordinary_literals
    )
    if len(exceptional) != EXCEPTIONAL_STATE_COUNT:
        raise CardinalityValidationError("exact e must use all ten exceptional O atoms")
    if len(missing) != ORDINARY_STATE_COUNT:
        raise CardinalityValidationError("exact m must use all 25 negated ordinary O atoms")
    all_inputs = exceptional + missing
    if len({abs(value) for value in all_inputs}) != len(all_inputs):
        raise CardinalityValidationError("e/m occupancy inputs must be distinct variables")
    if any(abs(value) > top_id for value in all_inputs):
        raise CardinalityValidationError("e/m occupancy input exceeds base num_vars")

    clauses: list[tuple[int, ...]] = []
    components: list[Mapping[str, Any]] = []
    auxiliaries: list[CardinalityAuxiliary] = []
    current = top_id
    current = _append_at_most_component(
        component_id="exceptional_at_most",
        meaning="sum(exceptional_O) <= e",
        literals=exceptional,
        bound=e_count,
        top_id=current,
        clauses=clauses,
        components=components,
        auxiliaries=auxiliaries,
    )
    current = _append_at_most_component(
        component_id="exceptional_at_least",
        meaning="sum(exceptional_O) >= e",
        literals=tuple(-value for value in exceptional),
        bound=EXCEPTIONAL_STATE_COUNT - e_count,
        top_id=current,
        clauses=clauses,
        components=components,
        auxiliaries=auxiliaries,
    )
    current = _append_at_most_component(
        component_id="missing_ordinary_at_most",
        meaning="sum(not ordinary_O) <= m",
        literals=missing,
        bound=m_count,
        top_id=current,
        clauses=clauses,
        components=components,
        auxiliaries=auxiliaries,
    )
    current = _append_at_most_component(
        component_id="missing_ordinary_at_least",
        meaning="sum(not ordinary_O) >= m",
        literals=tuple(-value for value in missing),
        bound=ORDINARY_STATE_COUNT - m_count,
        top_id=current,
        clauses=clauses,
        components=components,
        auxiliaries=auxiliaries,
    )
    if auxiliaries and tuple(item.literal for item in auxiliaries) != tuple(
        range(top_id + 1, current + 1)
    ):
        raise AssertionError("cardinality auxiliary IDs are not one canonical chain")
    if any(abs(value) > current for clause in clauses for value in clause):
        raise AssertionError("cardinality clause exceeds final num_vars")
    return ExactEMCardinality(
        base_num_vars=top_id,
        num_vars=current,
        exceptional_count=e_count,
        missing_ordinary_count=m_count,
        exceptional_literals=exceptional,
        missing_ordinary_literals=missing,
        clauses=tuple(clauses),
        components=tuple(components),
        auxiliary_variables=tuple(auxiliaries),
    )


@dataclass(frozen=True)
class BuiltCardinalityCell:
    cell: CardinalityCell
    environment: CardinalityEnvironment = field(repr=False, compare=False)
    formula: obligation_api.ObligationFormula
    cardinality: ExactEMCardinality
    bridges: bool = True
    f3_main: bool = False
    f3_main_encoding: F3MainEncoding | None = None
    bridge_clause_count: int = 0

    @property
    def mode(self) -> str:
        return self.environment.mode

    @property
    def formula_case_id(self) -> str:
        return f"{self.cell.case_id}_{self.mode}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": "state_charging_built_cardinality_cell_v1",
            "logical_cell": self.cell.to_dict(),
            "formula_mode": self.mode,
            "formula_scope": dict(self.environment.scope),
            "formula": self.formula.to_dict(include_clauses=False),
            "cardinality": self.cardinality.to_dict(include_clauses=False),
            "encoding": {
                "name": (
                    DEFAULT_CARDINALITY_ENCODING if self.f3_main else
                    BRIDGES_CARDINALITY_ENCODING if self.bridges else "legacy_exact_v1"
                ),
                "bridges": self.bridges,
                "f3_main": self.f3_main,
                "bridge_clause_count": self.bridge_clause_count,
                "f3_main_clause_count": (
                    len(self.f3_main_encoding.clauses) if self.f3_main_encoding else 0
                ),
            },
            "f3_main_pruning": (
                self.f3_main_encoding.to_dict() if self.f3_main_encoding else None
            ),
            "evidence_policy": {
                "sat": "complete_formula_assignment_plus_independent_state_replay",
                "unsat": "nonempty_external_proof_plus_independent_checker",
                "raw_unsat": "UNKNOWN",
            },
        }


def state_path_bridge_clauses(
    encoding: DownsetStateEncoding,
) -> tuple[tuple[int, ...], ...]:
    """Return entailed C(u,a,b) -> B(a+2,u,v) or R(b+2,u,v) clauses.

    A cell witness has a common predecessor w<u. The color of (w,u,v)
    extends one of its exact terminal paths. Blue-5/red-6 terms are forbidden
    by the base path bounds, so omit them at a=3/b=4. Repeated boundary units
    are deduplicated in first-occurrence order, matching the tested variant.
    This uses neither a cardinality premise nor the weak-7-gon exclusion.
    """
    if not isinstance(encoding, DownsetStateEncoding) or encoding.spec != STATE_756_SPEC:
        raise CardinalityValidationError("bridges require the exact (7,5,6) state encoding")
    order = _plain_int(encoding.order, label="bridge order", minimum=1, maximum=35)
    result: list[tuple[int, ...]] = []
    seen: set[tuple[int, ...]] = set()
    for u, v in itertools.combinations(range(1, order + 1), 2):
        for a, b in itertools.product(range(1, 4), range(1, 5)):
            clause = [-_literal(encoding.cell_vars[u, a, b], label="bridge cell")]
            if a < 3:
                clause.append(_literal(
                    encoding.terminal_path_vars[PATH5_FAMILY, a + 2, u, v],
                    label="bridge blue terminal path",
                ))
            if b < 4:
                clause.append(_literal(
                    encoding.terminal_path_vars[PATH6_FAMILY, b + 2, u, v],
                    label="bridge red terminal path",
                ))
            normalized = tuple(clause)
            if normalized not in seen:
                seen.add(normalized)
                result.append(normalized)
    return tuple(result)


def materialize_cell(
    environment: CardinalityEnvironment,
    raw_cell: CardinalityCell | Mapping[str, Any],
    *,
    bridges: bool = True,
    f3_main: bool | None = None,
) -> BuiltCardinalityCell:
    """Build exact+bridges+F3-main; explicit opt-outs replay old profiles."""
    if type(bridges) is not bool:
        raise CardinalityValidationError("bridges must be a boolean")
    if f3_main is not None and type(f3_main) is not bool:
        raise CardinalityValidationError("f3_main must be None or a boolean")
    resolved_f3 = bridges if f3_main is None else f3_main
    if resolved_f3 and not bridges:
        raise CardinalityValidationError("F3-main requires bridges")
    validate_environment(environment)
    cell = normalize_cell(raw_cell)
    if cell.order != environment.order:
        raise CardinalityValidationError(
            "cell order differs from fresh formula/state-encoding order"
        )
    exceptional_literals = tuple(
        _literal(environment.encoding.occupancy_vars[state], label=f"O[{state}]")
        for state in exceptional_states()
    )
    missing_literals = tuple(
        -_literal(environment.encoding.occupancy_vars[state], label=f"O[{state}]")
        for state in ordinary_states()
    )
    cardinality = encode_exact_em_cardinality(
        exceptional_literals,
        missing_literals,
        exceptional_count=cell.e,
        missing_ordinary_count=cell.missing_ordinary_count,
        top_id=environment.base_num_vars,
    )
    added = state_path_bridge_clauses(environment.encoding) if bridges else ()
    pruning = (
        build_f3_main_rank(environment.encoding, top_id=cardinality.num_vars)
        if resolved_f3 else None
    )
    supplemental = cardinality.clauses + added + (pruning.clauses if pruning else ())
    num_vars = pruning.num_vars if pruning else cardinality.num_vars
    formula_metadata = cardinality.to_dict(include_clauses=False)
    if bridges:
        formula_metadata["pruning"] = {
            "encoding": (
                DEFAULT_CARDINALITY_ENCODING if resolved_f3 else BRIDGES_CARDINALITY_ENCODING
            ),
            "bridge_clause_count": len(added),
            "bridge_clauses_sha256": obligation_api.stable_sha256(
                [list(clause) for clause in added]
            ),
        }
    if pruning is not None:
        formula_metadata["pruning"]["f3_main"] = pruning.to_dict()
    digest = obligation_api._derived_formula_sha256(
        base_sha256=environment.base_sha256,
        base_num_vars=environment.base_num_vars,
        num_vars=num_vars,
        supplemental_clauses=supplemental,
    )
    formula = obligation_api.ObligationFormula(
        case_id=f"{cell.case_id}_{environment.mode}",
        num_vars=num_vars,
        base_num_vars=environment.base_num_vars,
        base_clauses=environment.base_clauses,
        supplemental_clauses=supplemental,
        sha256=digest,
        base_sha256=environment.base_sha256,
        cardinality=MappingProxyType(formula_metadata),
    )
    if max((abs(lit) for clause in formula.clauses for lit in clause), default=0) > formula.num_vars:
        raise AssertionError("materialized cell formula exceeds declared num_vars")
    return BuiltCardinalityCell(
        cell, environment, formula, cardinality, bridges, resolved_f3, pruning, len(added)
    )


def normalize_complete_assignment(model: Iterable[Any], num_vars: int) -> tuple[int, ...]:
    """Require exactly one signed value for every final formula variable."""

    num_vars = _plain_int(num_vars, label="num_vars", minimum=0)
    if isinstance(model, (str, bytes)):
        raise CardinalityValidationError("model must be a signed-literal iterable")
    try:
        entries = tuple(model)
    except TypeError as exc:
        raise CardinalityValidationError("model must be iterable") from exc
    values: dict[int, bool] = {}
    for raw in entries:
        if isinstance(raw, bool) or not isinstance(raw, int):
            raise CardinalityValidationError(
                f"model contains non-integer literal {raw!r}"
            )
        if raw == 0:
            continue
        variable = abs(raw)
        if variable > num_vars:
            raise CardinalityValidationError(
                f"model variable {variable} exceeds formula num_vars"
            )
        if variable in values:
            raise CardinalityValidationError(
                f"model repeats variable {variable}"
            )
        values[variable] = raw > 0
    missing = next(
        (variable for variable in range(1, num_vars + 1) if variable not in values),
        None,
    )
    if missing is not None:
        raise CardinalityValidationError(
            f"model omits formula variable {missing}"
        )
    return tuple(variable if values[variable] else -variable for variable in range(1, num_vars + 1))


def parse_dimacs_sat_output(text: str, num_vars: int) -> tuple[int, ...]:
    """Parse one external solver SAT output into canonical ``(±1,...,±n)``."""

    if not isinstance(text, str):
        raise CardinalityValidationError("solver output must be text")
    statuses = [
        line.strip()[2:].strip()
        for line in text.splitlines()
        if line.strip().startswith("s ")
    ]
    if statuses != ["SATISFIABLE"]:
        raise CardinalityValidationError(
            "solver output must contain exactly one 's SATISFIABLE' line"
        )
    literals: list[int] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("v "):
            continue
        for token in line[2:].split():
            try:
                literals.append(int(token))
            except ValueError as exc:
                raise CardinalityValidationError(
                    f"solver model contains a non-integer token {token!r}"
                ) from exc
    if not literals:
        raise CardinalityValidationError("solver SAT output contains no model lines")
    return normalize_complete_assignment(literals, num_vars)


def _values(assignment: Sequence[int]) -> Mapping[int, bool]:
    return {abs(literal): literal > 0 for literal in assignment}


def _truth(values: Mapping[int, bool], atom: Any, *, label: str) -> bool:
    literal = _literal(atom, label=label)
    if abs(literal) not in values:
        raise CardinalityValidationError(f"assignment omits {label}")
    truth = values[abs(literal)]
    return truth if literal > 0 else not truth


def _audit_formula_clauses(
    formula: obligation_api.ObligationFormula,
    assignment: Sequence[int],
) -> None:
    values = _values(assignment)
    for clause_index, clause in enumerate(formula.clauses):
        if not all(
            not isinstance(literal, bool)
            and isinstance(literal, int)
            and literal != 0
            and abs(literal) <= formula.num_vars
            for literal in clause
        ):
            raise CardinalityValidationError(
                f"formula clause {clause_index} is malformed"
            )
        if not any(values[abs(literal)] is (literal > 0) for literal in clause):
            raise CardinalityValidationError(
                f"assignment falsifies formula clause {clause_index}"
            )


def canonical_dimacs_identity(
    num_vars: int,
    clauses: Iterable[Sequence[int]],
) -> dict[str, Any]:
    """Hash canonical LF DIMACS without materializing a second giant byte blob."""

    num_vars = _plain_int(num_vars, label="DIMACS num_vars", minimum=0)
    if isinstance(clauses, Sequence) and not isinstance(clauses, (str, bytes)):
        rows = clauses
    else:
        rows = tuple(clauses)

    digest = hashlib.sha256()
    size = 0

    def consume(row: bytes) -> None:
        nonlocal size
        digest.update(row)
        size += len(row)

    consume(f"p cnf {num_vars} {len(rows)}\n".encode("ascii"))
    for clause_index, raw_clause in enumerate(rows):
        if isinstance(raw_clause, (str, bytes)):
            raise CardinalityValidationError(
                f"DIMACS clause {clause_index} must be a literal sequence"
            )
        try:
            clause = tuple(
                _literal(value, label=f"DIMACS clause {clause_index} literal")
                for value in raw_clause
            )
        except TypeError as exc:
            raise CardinalityValidationError(
                f"DIMACS clause {clause_index} must be a literal sequence"
            ) from exc
        if any(abs(value) > num_vars for value in clause):
            raise CardinalityValidationError(
                f"DIMACS clause {clause_index} exceeds num_vars"
            )
        if clause:
            consume((" ".join(str(value) for value in clause) + " 0\n").encode("ascii"))
        else:
            consume(b"0\n")
    return {
        "schema": "canonical_dimacs_identity_v1",
        "num_vars": num_vars,
        "num_clauses": len(rows),
        "size_bytes": size,
        "sha256": digest.hexdigest(),
        "format": "ascii_lf_header_then_ordered_clauses_v1",
    }


def _canonical_state_list(raw: Any, *, label: str) -> list[tuple[int, ...]]:
    if not isinstance(raw, list):
        raise CardinalityValidationError(f"{label} must be a list")
    result = [_canonical_state_tuple(item, label=label) for item in raw]
    if result != sorted(result) or len(result) != len(set(result)):
        raise CardinalityValidationError(f"{label} is not canonical and duplicate-free")
    return result


def audit_profile_cardinality(
    profile: Mapping[str, Any],
    raw_cell: CardinalityCell | Mapping[str, Any],
    *,
    formula_mode: str,
) -> dict[str, Any]:
    """Rebuild target status, injection, and ``e,m`` from endpoint rows.

    This function intentionally ignores the profile's scalar counts until the
    independently rebuilt sets are available, then requires every cached
    summary to agree.
    """

    if not isinstance(profile, Mapping) or profile.get("schema") != PROFILE_SCHEMA:
        raise CardinalityValidationError("expected a canonical down-set profile")
    mode = _normalize_mode(formula_mode)
    cell = normalize_cell(raw_cell)
    order = _plain_int(profile.get("order"), label="profile order", minimum=1)
    if order != cell.order:
        raise CardinalityValidationError("profile order differs from cell order")
    if profile.get("semantics") != STATE_756_SPEC.semantics_dict():
        raise CardinalityValidationError("profile uses noncanonical state semantics")
    expected_universe = {
        "all_count": TOTAL_STATE_COUNT,
        "ordinary_count": ORDINARY_STATE_COUNT,
        "exceptional_count": EXCEPTIONAL_STATE_COUNT,
        "ordinary_states": [list(state) for state in ordinary_states()],
        "exceptional_states": [list(state) for state in exceptional_states()],
    }
    if not _same_json(profile.get("state_universe"), expected_universe):
        raise CardinalityValidationError("profile 35-state universe drifted")

    raw_vertices = profile.get("vertex_states")
    if not isinstance(raw_vertices, list) or len(raw_vertices) != order:
        raise CardinalityValidationError("profile has an incomplete vertex-state list")
    states_by_vertex: dict[int, tuple[int, ...]] = {}
    first_weak: int | None = None
    first_exceptional: int | None = None
    for index, raw_vertex in enumerate(raw_vertices, 1):
        if not isinstance(raw_vertex, Mapping):
            raise CardinalityValidationError(f"vertex-state row {index} is malformed")
        vertex = _plain_int(raw_vertex.get("vertex"), label="profile vertex", minimum=1)
        if vertex != index:
            raise CardinalityValidationError("profile vertices are not exactly 1..N")
        state = _canonical_state_tuple(raw_vertex.get("rows"), label=f"vertex {vertex} state")
        kind = classify_state(state)
        if raw_vertex.get("kind") != kind:
            raise CardinalityValidationError(f"vertex {vertex} cached kind drifted")
        path5 = raw_vertex.get("path5_start_endpoints")
        path6 = raw_vertex.get("path6_start_endpoints")
        if not isinstance(path5, list) or not isinstance(path6, list):
            raise CardinalityValidationError(f"vertex {vertex} start sets are missing")
        path5_values = [
            _plain_int(item, label=f"vertex {vertex} path5 start", minimum=1)
            for item in path5
        ]
        path6_values = [
            _plain_int(item, label=f"vertex {vertex} path6 start", minimum=1)
            for item in path6
        ]
        if path5_values != sorted(set(path5_values)) or path6_values != sorted(set(path6_values)):
            raise CardinalityValidationError(f"vertex {vertex} start sets are noncanonical")
        if any(start >= vertex for start in (*path5_values, *path6_values)):
            raise CardinalityValidationError(f"vertex {vertex} has an out-of-range start")
        common = sorted(set(path5_values) & set(path6_values))
        raw_common = raw_vertex.get("common_start_endpoints")
        if not isinstance(raw_common, list) or any(
            isinstance(item, bool) or not isinstance(item, int)
            for item in raw_common
        ):
            raise CardinalityValidationError(
                f"vertex {vertex} common starts are malformed"
            )
        if raw_common != common:
            raise CardinalityValidationError(f"vertex {vertex} common starts drifted")
        weak = bool(common)
        if raw_vertex.get("weak_gon") is not weak:
            raise CardinalityValidationError(f"vertex {vertex} weak-target flag drifted")
        if weak and first_weak is None:
            first_weak = vertex
        split = bool(path5_values) and bool(path6_values)
        if raw_vertex.get("split_witness") is not split:
            raise CardinalityValidationError(f"vertex {vertex} split flag drifted")
        if (kind == EXCEPTIONAL_KIND) is not split:
            raise CardinalityValidationError(
                f"vertex {vertex} state/split equivalence failed"
            )
        if kind == EXCEPTIONAL_KIND and first_exceptional is None:
            first_exceptional = vertex
        states_by_vertex[vertex] = state

    if not _same_json(profile.get("first_weak_gon_vertex"), first_weak):
        raise CardinalityValidationError("profile first weak-target endpoint drifted")
    if not _same_json(
        profile.get("first_exceptional_vertex"), first_exceptional
    ):
        raise CardinalityValidationError(
            "profile first exceptional endpoint drifted"
        )
    if mode == STRICT_NO_TARGET and first_weak is not None:
        raise CardinalityValidationError(
            "strict_no_target SAT witness contains a weak 7-gon"
        )

    universe = enumerate_states()
    ordinary = ordinary_states()
    exceptional = exceptional_states()
    if set(states_by_vertex.values()) - set(universe):
        raise CardinalityValidationError("profile contains a state outside the catalog")
    state_to_vertices: dict[tuple[int, ...], list[int]] = {}
    for vertex, state in states_by_vertex.items():
        state_to_vertices.setdefault(state, []).append(vertex)
    collisions = [
        {"rows": list(state), "vertices": vertices}
        for state, vertices in sorted(state_to_vertices.items())
        if len(vertices) > 1
    ]
    if collisions:
        raise CardinalityValidationError(
            "profile violates the cross-endpoint state-injection theorem"
        )
    expected_injection = {"holds": True, "collisions": []}
    if not _same_json(profile.get("state_injection"), expected_injection):
        raise CardinalityValidationError("profile state-injection summary drifted")

    occupied = set(state_to_vertices)
    occupied_ordinary = tuple(sorted(occupied & set(ordinary)))
    occupied_exceptional = tuple(sorted(occupied & set(exceptional)))
    missing_ordinary = tuple(sorted(set(ordinary) - occupied))
    if _canonical_state_list(
        profile.get("occupied_ordinary_states"),
        label="occupied ordinary states",
    ) != list(occupied_ordinary):
        raise CardinalityValidationError("profile occupied-ordinary summary drifted")
    if _canonical_state_list(
        profile.get("occupied_exceptional_states"),
        label="occupied exceptional states",
    ) != list(occupied_exceptional):
        raise CardinalityValidationError("profile occupied-exceptional summary drifted")
    if _canonical_state_list(
        profile.get("missing_ordinary_states"),
        label="missing ordinary states",
    ) != list(missing_ordinary):
        raise CardinalityValidationError("profile missing-ordinary summary drifted")
    if isinstance(profile.get("occupied_state_count"), bool) or profile.get(
        "occupied_state_count"
    ) != len(occupied):
        raise CardinalityValidationError("profile occupied-state count drifted")

    e_count = len(occupied_exceptional)
    m_count = len(missing_ordinary)
    if e_count != cell.e or m_count != cell.missing_ordinary_count:
        raise CardinalityValidationError(
            "profile exact exceptional/missing counts disagree with the cell"
        )
    if len(occupied) != order:
        raise CardinalityValidationError("injective endpoint states do not total N")
    if order != (ORDINARY_STATE_COUNT - m_count) + e_count:
        raise CardinalityValidationError("N=(25-m)+e identity failed")
    if order != 26 + cell.e - cell.r:
        raise CardinalityValidationError("cell N=26+e-r identity failed")

    defect = e_count - m_count
    if isinstance(profile.get("defect"), bool) or profile.get("defect") != defect:
        raise CardinalityValidationError("profile defect summary drifted")
    identity = profile.get("defect_identity")
    expected_identity = {
        "lhs_order_minus_ordinary_universe": order - ORDINARY_STATE_COUNT,
        "rhs_occupied_exceptional_minus_missing_ordinary": defect,
        "holds": True,
    }
    if not _same_json(identity, expected_identity):
        raise CardinalityValidationError("profile defect identity drifted")

    return {
        "schema": PROFILE_AUDIT_SCHEMA,
        "pass": True,
        "formula_mode": mode,
        "cell": cell.to_dict(),
        "order": order,
        "target_free": first_weak is None,
        "first_weak_gon_vertex": first_weak,
        "state_injection": True,
        "occupied_state_count": len(occupied),
        "occupied_exceptional_count": e_count,
        "missing_ordinary_count": m_count,
        "occupied_ordinary_states": [list(state) for state in occupied_ordinary],
        "occupied_ordinary_state_tokens": [_state_token(state) for state in occupied_ordinary],
        "occupied_exceptional_states": [list(state) for state in occupied_exceptional],
        "occupied_exceptional_state_tokens": [
            _state_token(state) for state in occupied_exceptional
        ],
        "missing_ordinary_states": [list(state) for state in missing_ordinary],
        "missing_ordinary_state_tokens": [_state_token(state) for state in missing_ordinary],
        "count_identity": {
            "N": order,
            "ordinary_occupied": ORDINARY_STATE_COUNT - m_count,
            "exceptional_occupied": e_count,
            "m": m_count,
            "e": e_count,
            "r": cell.r,
            "holds": True,
        },
    }


def _audit_no_start_state_atoms(
    encoding: DownsetStateEncoding,
    profile: Mapping[str, Any],
    assignment: Sequence[int],
) -> dict[str, Any]:
    if encoding.include_start_endpoints is not False or encoding.start_vars:
        raise CardinalityValidationError("SAT checker expected a no-start encoding")
    values = _values(assignment)
    catalog = enumerate_states()
    raw_vertices = profile["vertex_states"]
    expected_by_vertex = {
        int(item["vertex"]): tuple(int(value) for value in item["rows"])
        for item in raw_vertices
    }
    expected_occupied = set(expected_by_vertex.values())
    state_checks = 0
    for vertex in range(1, encoding.order + 1):
        for state in catalog:
            atom = encoding.state_vars.get((vertex, state))
            if atom is None:
                raise CardinalityValidationError(f"encoding omits S[{vertex},{state}]")
            actual = _truth(values, atom, label=f"S[{vertex},{state}]")
            if actual is not (expected_by_vertex[vertex] == state):
                raise CardinalityValidationError(
                    f"S[{vertex},{state}] disagrees with independent extraction"
                )
            state_checks += 1
    occupancy_checks = 0
    for state in catalog:
        atom = encoding.occupancy_vars.get(state)
        if atom is None:
            raise CardinalityValidationError(f"encoding omits O[{state}]")
        actual = _truth(values, atom, label=f"O[{state}]")
        if actual is not (state in expected_occupied):
            raise CardinalityValidationError(
                f"O[{state}] is not the exact bidirectional occupancy value"
            )
        occupancy_checks += 1
    full_checks = 0
    for vertex in range(1, encoding.order + 1):
        atom = encoding.full_vars.get(vertex)
        if atom is None:
            raise CardinalityValidationError(f"encoding omits F[{vertex}]")
        actual = _truth(values, atom, label=f"F[{vertex}]")
        expected = classify_state(expected_by_vertex[vertex]) == EXCEPTIONAL_KIND
        if actual is not expected:
            raise CardinalityValidationError(
                f"F[{vertex}] disagrees with independent extraction"
            )
        full_checks += 1
    return {
        "schema": "state_charging_cardinality_state_atom_audit_v1",
        "pass": True,
        "state_checks": state_checks,
        "occupancy_checks": occupancy_checks,
        "full_checks": full_checks,
        "start_checks": 0,
    }


def audit_cell_assignment(
    built: BuiltCardinalityCell,
    model: Iterable[Any],
) -> dict[str, Any]:
    """Independently replay a complete strict/relaxed SAT cell assignment."""

    if not isinstance(built, BuiltCardinalityCell):
        raise TypeError("built must be a BuiltCardinalityCell")
    validate_environment(built.environment)
    fresh = materialize_cell(
        built.environment, built.cell, bridges=built.bridges, f3_main=built.f3_main
    )
    if not _same_json(fresh.formula.to_dict(include_clauses=True),
                      built.formula.to_dict(include_clauses=True)):
        raise CardinalityValidationError("built cell formula does not fresh-replay")
    if not _same_json(fresh.cardinality.to_dict(include_clauses=True),
                      built.cardinality.to_dict(include_clauses=True)):
        raise CardinalityValidationError("built cardinality metadata does not fresh-replay")
    if not _same_json(fresh.to_dict(), built.to_dict()):
        raise CardinalityValidationError("built pruning metadata does not fresh-replay")

    assignment = normalize_complete_assignment(model, built.formula.num_vars)
    _audit_formula_clauses(built.formula, assignment)
    base_assignment = assignment[: built.environment.base_num_vars]
    coloring = corpus_api.decode_complete_triple_coloring(
        built.environment.instance,
        base_assignment,
        order=built.cell.order,
        true_color="red",
    )
    signotope = corpus_api.audit_signotope_coloring(coloring, order=built.cell.order)
    if signotope.get("pass") is not True:
        raise CardinalityValidationError("SAT coloring violates the signotope axiom")
    profile = extract_downset_profile(coloring, order=built.cell.order)
    profile_audit = audit_profile_cardinality(
        profile,
        built.cell,
        formula_mode=built.mode,
    )
    state_atoms = _audit_no_start_state_atoms(
        built.environment.encoding,
        profile,
        base_assignment,
    )
    return {
        "schema": SAT_AUDIT_SCHEMA,
        "status": "AUDITED_SAT",
        "pass": True,
        "formula_mode": built.mode,
        "cell": built.cell.to_dict(),
        "formula_sha256": built.formula.sha256,
        "base_formula_sha256": built.environment.base_sha256,
        "assignment_sha256": obligation_api.stable_sha256(list(assignment)),
        "coloring_sha256": profile["coloring_sha256"],
        "complete_assignment": True,
        "formula_clause_count": len(built.formula.clauses),
        "formula_clauses_checked": len(built.formula.clauses),
        "signotope_audit": signotope,
        "state_atom_audit": state_atoms,
        "profile_audit": profile_audit,
    }


__all__ = [
    "BRIDGES_CARDINALITY_ENCODING",
    "DEFAULT_CARDINALITY_ENCODING",
    "state_path_bridge_clauses",
    "AUXILIARY_SCHEMA",
    "CARDINALITY_PLAN_SCHEMA",
    "CELL_COUNT",
    "CELL_SCHEMA",
    "EXCEPTIONAL_STATE_COUNT",
    "FORMULA_MODES",
    "MAX_CELL_ORDER",
    "MIN_CELL_ORDER",
    "ORDINARY_STATE_COUNT",
    "PROFILE_AUDIT_SCHEMA",
    "REGISTRY_SCHEMA",
    "SAT_AUDIT_SCHEMA",
    "STRICT_NO_TARGET",
    "TARGET_ALLOWED_RELAXED",
    "TOTAL_STATE_COUNT",
    "BuiltCardinalityCell",
    "CardinalityAuxiliary",
    "CardinalityCell",
    "CardinalityEnvironment",
    "CardinalityValidationError",
    "ExactEMCardinality",
    "all_cells",
    "audit_cell_assignment",
    "audit_profile_cardinality",
    "canonical_formula_scope",
    "canonical_state_catalog_sha256",
    "canonical_dimacs_identity",
    "c1_cells",
    "encode_exact_em_cardinality",
    "materialize_cell",
    "n26_spine_cells",
    "normalize_cell",
    "normalize_complete_assignment",
    "parse_dimacs_sat_output",
    "prepare_environment",
    "registry",
    "validate_environment",
    "validate_order_contract",
    "validate_registry",
]
