"""Opt-in exact CNF encoding of terminal-pair down-set states.

The default :func:`lib.erdos.etv` builder intentionally does not import this
module.  Call :func:`add_downset_state_encoding` explicitly to append the
encoding to an existing ``SATInstance``.  All public vertex indices in this
module are one-based, matching :mod:`lib.downset_state`; the source
``instance.v`` dictionary remains the repository's zero-based triple map.

The encoding is independent of the existing cap/cup auxiliaries.  Its path
recurrences use only the representative literals of ``instance.v``:

``path5_color``
    The color with forbidden path length five (blue for ``STATE_756_SPEC``).

``path6_color``
    The color with forbidden path length six (red for ``STATE_756_SPEC``).

Every introduced variable has an explicit metadata role, and every appended
clause belongs to :data:`DOWNSET_STATE_CLAUSE_GROUP`.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Iterable, Mapping, Sequence

from lib.downset_state import (
    EXCEPTIONAL_KIND,
    STATE_756_SPEC,
    DownsetSpec,
    StateRows,
    classify_state,
    enumerate_states,
)
from lib.sat_tseitin import Clauses


DOWNSET_STATE_CLAUSE_GROUP = "downset_state_encoding"
DOWNSET_STATE_SCHEMA = "downset_state_cnf_v1"

PATH5_FAMILY = "path5_color"
PATH6_FAMILY = "path6_color"


TerminalPathKey = tuple[str, int, int, int]
StartPathKey = tuple[str, int, int, int, int]
StartKey = tuple[str, int, int]
CellKey = tuple[int, int, int]
StateKey = tuple[int, StateRows]


def _catalog_sha256(catalog: Sequence[StateRows]) -> str:
    payload = json.dumps(
        [list(state) for state in catalog],
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _literal(formula: Clauses) -> int:
    if type(formula) is not Clauses:
        raise TypeError("down-set encoding requires lib.sat_tseitin.Clauses values")
    literal = formula._lit
    if type(literal) is not int or literal <= 0:
        raise ValueError("down-set encoding atom has no canonical positive literal")
    return literal


def _freeze(mapping: Mapping[Any, Clauses]) -> Mapping[Any, Clauses]:
    return MappingProxyType(dict(mapping))


def _require_unallocated_variable_names(
    instance: Any,
    names: Iterable[str],
    *,
    label: str,
) -> tuple[str, ...]:
    """Reserve a complete extension namespace before its first allocation."""

    planned = tuple(names)
    if any(type(name) is not str or not name for name in planned):
        raise ValueError(f"{label} has a noncanonical planned variable name")
    if len(set(planned)) != len(planned):
        raise ValueError(f"{label} planned variable names are not unique")

    var_names = getattr(instance, "_var_names", None)
    name_to_var = getattr(instance, "_name_to_var", None)
    if type(var_names) is not dict or type(name_to_var) is not dict:
        raise ValueError("SAT instance has no canonical variable-name ledger")
    if any(
        type(literal) is not int or type(name) is not str
        for literal, name in var_names.items()
    ) or any(
        type(name) is not str or type(literal) is not int
        for name, literal in name_to_var.items()
    ):
        raise ValueError("SAT instance variable-name ledger is noncanonical")
    if len(var_names) != len(name_to_var) or any(
        name_to_var.get(name) != literal
        for literal, name in var_names.items()
    ):
        raise ValueError("SAT instance variable-name ledger is not bijective")

    occupied = set(name_to_var)
    collision = next((name for name in planned if name in occupied), None)
    if collision is not None:
        raise ValueError(
            f"{label} output variable name is already allocated: {collision}"
        )
    return planned


@dataclass(frozen=True)
class DownsetStateEncoding:
    """Public handles for one installed exact state encoding.

    Map values are :class:`~lib.sat_tseitin.Clauses` atoms.  Their
    representative integer literal is available as ``value._lit`` and their
    value in the last loaded solver model as ``value.solution()``.
    """

    order: int
    spec: DownsetSpec
    group: str
    include_start_endpoints: bool
    catalog: tuple[StateRows, ...]
    catalog_sha256: str
    ordinary_catalog: tuple[StateRows, ...]
    exceptional_catalog: tuple[StateRows, ...]
    terminal_path_vars: Mapping[TerminalPathKey, Clauses]
    cell_vars: Mapping[CellKey, Clauses]
    state_vars: Mapping[StateKey, Clauses]
    occupancy_vars: Mapping[StateRows, Clauses]
    full_vars: Mapping[int, Clauses]
    start_path_vars: Mapping[StartPathKey, Clauses]
    start_vars: Mapping[StartKey, Clauses]
    instance: Any = field(repr=False, compare=False)

    @property
    def states(self) -> tuple[StateRows, ...]:
        """Alias for the deterministic canonical state catalog."""

        return self.catalog

    @property
    def path_exists(self) -> Mapping[TerminalPathKey, Clauses]:
        return self.terminal_path_vars

    @property
    def cells(self) -> Mapping[CellKey, Clauses]:
        return self.cell_vars

    @property
    def occupied(self) -> Mapping[StateRows, Clauses]:
        return self.occupancy_vars

    @property
    def full(self) -> Mapping[int, Clauses]:
        return self.full_vars

    @property
    def exceptional_vars(self) -> Mapping[int, Clauses]:
        return self.full_vars

    @property
    def start_presence(self) -> Mapping[StartKey, Clauses]:
        return self.start_vars

    def state_literal(self, vertex: int, rows: Sequence[int]) -> int:
        """Return the exact ``S[vertex, rows]`` representative literal."""

        return _literal(self.state_vars[(vertex, tuple(int(x) for x in rows))])

    def occupancy_literal(self, rows: Sequence[int]) -> int:
        """Return the exact ``O[rows]`` representative literal."""

        return _literal(self.occupancy_vars[tuple(int(x) for x in rows)])


class _RawEncoder:
    """Collect raw exact definitions before appending one clause group."""

    def __init__(self, instance: Any):
        self.instance = instance
        self.clauses: list[list[int]] = []

    def new_var(self, name: str, *, role: str, **metadata: Any) -> Clauses:
        return self.instance.new_var(name, role=role, **metadata)

    def add_clause(self, literals: Iterable[int]) -> None:
        self.clauses.append([int(lit) for lit in literals])

    def equiv_and(self, result: Clauses, terms: Sequence[int]) -> None:
        """Encode ``result <-> AND(terms)`` (empty AND is true)."""

        z = _literal(result)
        for term in terms:
            self.add_clause([-z, term])
        self.add_clause([z, *(-term for term in terms)])

    def equiv_or(self, result: Clauses, terms: Sequence[int]) -> None:
        """Encode ``result <-> OR(terms)`` (empty OR is false)."""

        z = _literal(result)
        for term in terms:
            self.add_clause([-term, z])
        self.add_clause([-z, *terms])


def _validate_and_resolve_order(instance: Any, order: int | None) -> int:
    if hasattr(instance, "downset_state_encoding"):
        raise ValueError("down-set state encoding is already installed")
    for attribute in ("new_var", "add", "set_metadata", "v"):
        if not hasattr(instance, attribute):
            raise TypeError(f"instance must expose {attribute!r}")
    if not isinstance(instance.v, Mapping):
        raise TypeError("instance.v must be a mapping of zero-based triples")

    declared_order = None
    metadata = getattr(instance, "_metadata", None)
    if isinstance(metadata, Mapping):
        problem = metadata.get("problem")
        if isinstance(problem, Mapping):
            declared_order = problem.get("N")

    inferred_order = None
    if instance.v:
        try:
            inferred_order = max(max(triple) for triple in instance.v) + 1
        except (TypeError, ValueError) as exc:
            raise TypeError("instance.v keys must be increasing integer triples") from exc

    if order is None:
        order = declared_order if declared_order is not None else inferred_order
    if type(order) is not int or order < 1:
        raise ValueError("order must be a positive integer")
    if declared_order is not None and order > declared_order:
        raise ValueError(
            f"requested order {order} exceeds instance order {declared_order}"
        )
    if inferred_order is not None and order > inferred_order:
        raise ValueError(
            f"requested order {order} exceeds triple-map order {inferred_order}"
        )

    for triple in itertools.combinations(range(order), 3):
        if triple not in instance.v:
            raise ValueError(f"instance.v is missing triple {triple}")
        atom = instance.v[triple]
        if type(atom) is not Clauses or atom._instance is not instance:
            raise TypeError(f"instance.v[{triple!r}] is not an atom of this instance")
    return order


def _family_definitions(spec: DownsetSpec) -> tuple[tuple[str, str, int], ...]:
    return (
        (PATH5_FAMILY, spec.path5_color, spec.path5_split_length),
        (PATH6_FAMILY, spec.path6_color, spec.path6_split_length),
    )


def _triple_color_literal(
    instance: Any,
    triple: tuple[int, int, int],
    color: str,
) -> int:
    """Return a one-based triple's literal for the requested color."""

    atom = instance.v[tuple(vertex - 1 for vertex in triple)]
    lit = _literal(atom)
    if color == "red":
        return lit
    if color == "blue":
        return -lit
    raise ValueError(f"unsupported path color {color!r}")


def _build_terminal_paths(
    encoder: _RawEncoder,
    instance: Any,
    order: int,
    spec: DownsetSpec,
) -> dict[TerminalPathKey, Clauses]:
    paths: dict[TerminalPathKey, Clauses] = {}

    for family, _color, target_length in _family_definitions(spec):
        for length in range(2, target_length + 1):
            for left, right in itertools.combinations(range(1, order + 1), 2):
                paths[(family, length, left, right)] = encoder.new_var(
                    f"ds_terminal({family},{length},{left},{right})",
                    role="downset_terminal_path",
                    family=family,
                    length=length,
                    terminal_left=left,
                    terminal_right=right,
                )

    for family, color, target_length in _family_definitions(spec):
        for left, right in itertools.combinations(range(1, order + 1), 2):
            encoder.add_clause([_literal(paths[(family, 2, left, right)])])

        for length in range(3, target_length + 1):
            for left, right in itertools.combinations(range(1, order + 1), 2):
                extensions: list[int] = []
                for predecessor in range(1, left):
                    extension = encoder.new_var(
                        "ds_terminal_extension("
                        f"{family},{length},{predecessor},{left},{right})",
                        role="downset_terminal_extension",
                        family=family,
                        length=length,
                        predecessor=predecessor,
                        terminal_left=left,
                        terminal_right=right,
                    )
                    prefix = paths[(family, length - 1, predecessor, left)]
                    color_lit = _triple_color_literal(
                        instance, (predecessor, left, right), color
                    )
                    encoder.equiv_and(
                        extension,
                        [_literal(prefix), color_lit],
                    )
                    extensions.append(_literal(extension))
                encoder.equiv_or(
                    paths[(family, length, left, right)],
                    extensions,
                )
    return paths


def _build_fixed_start_paths(
    encoder: _RawEncoder,
    instance: Any,
    order: int,
    spec: DownsetSpec,
) -> tuple[dict[StartPathKey, Clauses], dict[StartKey, Clauses]]:
    paths: dict[StartPathKey, Clauses] = {}
    starts: dict[StartKey, Clauses] = {}

    for family, _color, target_length in _family_definitions(spec):
        for left, right in itertools.combinations(range(1, order + 1), 2):
            paths[(family, 2, left, left, right)] = encoder.new_var(
                f"ds_start_path({family},2,{left},{left},{right})",
                role="downset_fixed_start_path",
                family=family,
                length=2,
                start_endpoint=left,
                terminal_left=left,
                terminal_right=right,
            )
        for length in range(3, target_length + 1):
            for start, left, right in itertools.combinations(
                range(1, order + 1), 3
            ):
                paths[(family, length, start, left, right)] = encoder.new_var(
                    f"ds_start_path({family},{length},{start},{left},{right})",
                    role="downset_fixed_start_path",
                    family=family,
                    length=length,
                    start_endpoint=start,
                    terminal_left=left,
                    terminal_right=right,
                )

    for family, color, target_length in _family_definitions(spec):
        for left, right in itertools.combinations(range(1, order + 1), 2):
            encoder.add_clause(
                [_literal(paths[(family, 2, left, left, right)])]
            )

        for length in range(3, target_length + 1):
            for start, left, right in itertools.combinations(
                range(1, order + 1), 3
            ):
                extensions: list[int] = []
                for predecessor in range(start, left):
                    prefix = paths.get(
                        (family, length - 1, start, predecessor, left)
                    )
                    if prefix is None:
                        continue
                    extension = encoder.new_var(
                        "ds_start_extension("
                        f"{family},{length},{start},{predecessor},{left},{right})",
                        role="downset_fixed_start_extension",
                        family=family,
                        length=length,
                        start_endpoint=start,
                        predecessor=predecessor,
                        terminal_left=left,
                        terminal_right=right,
                    )
                    color_lit = _triple_color_literal(
                        instance, (predecessor, left, right), color
                    )
                    encoder.equiv_and(
                        extension,
                        [_literal(prefix), color_lit],
                    )
                    extensions.append(_literal(extension))
                encoder.equiv_or(
                    paths[(family, length, start, left, right)],
                    extensions,
                )

        for vertex in range(1, order + 1):
            for start in range(1, vertex):
                presence = encoder.new_var(
                    f"ds_start_present({family},{vertex},{start})",
                    role="downset_start_presence",
                    family=family,
                    target_length=target_length,
                    vertex=vertex,
                    start_endpoint=start,
                    right_endpoint=vertex,
                )
                terms = [
                    _literal(path)
                    for (key_family, length, key_start, _left, right), path in paths.items()
                    if key_family == family
                    and length == target_length
                    and key_start == start
                    and right == vertex
                ]
                encoder.equiv_or(presence, terms)
                starts[(family, vertex, start)] = presence

    return paths, starts


def _build_cells(
    encoder: _RawEncoder,
    order: int,
    spec: DownsetSpec,
    paths: Mapping[TerminalPathKey, Clauses],
) -> dict[CellKey, Clauses]:
    cells: dict[CellKey, Clauses] = {}
    for vertex in range(1, order + 1):
        for x in range(1, spec.width + 1):
            for y in range(1, spec.height + 1):
                cell = encoder.new_var(
                    f"ds_cell({vertex},{x},{y})",
                    role="downset_cell",
                    vertex=vertex,
                    x=x,
                    y=y,
                )
                witnesses: list[int] = []
                for terminal_left in range(1, vertex):
                    witness = encoder.new_var(
                        "ds_cell_witness("
                        f"{vertex},{x},{y},{terminal_left})",
                        role="downset_cell_witness",
                        vertex=vertex,
                        x=x,
                        y=y,
                        terminal_left=terminal_left,
                    )
                    encoder.equiv_and(
                        witness,
                        [
                            _literal(
                                paths[
                                    (PATH5_FAMILY, x + 1, terminal_left, vertex)
                                ]
                            ),
                            _literal(
                                paths[
                                    (PATH6_FAMILY, y + 1, terminal_left, vertex)
                                ]
                            ),
                        ],
                    )
                    witnesses.append(_literal(witness))
                encoder.equiv_or(cell, witnesses)
                cells[(vertex, x, y)] = cell
    return cells


def _build_states(
    encoder: _RawEncoder,
    order: int,
    spec: DownsetSpec,
    catalog: Sequence[StateRows],
    cells: Mapping[CellKey, Clauses],
) -> dict[StateKey, Clauses]:
    states: dict[StateKey, Clauses] = {}
    for vertex in range(1, order + 1):
        vertex_atoms: list[Clauses] = []
        for rows in catalog:
            state = encoder.new_var(
                f"ds_state({vertex},{'_'.join(str(value) for value in rows)})",
                role="downset_state",
                vertex=vertex,
                rows=list(rows),
            )
            pattern: list[int] = []
            for x in range(1, spec.width + 1):
                for y in range(1, spec.height + 1):
                    cell_lit = _literal(cells[(vertex, x, y)])
                    pattern.append(cell_lit if y <= rows[x - 1] else -cell_lit)
            encoder.equiv_and(state, pattern)
            states[(vertex, rows)] = state
            vertex_atoms.append(state)

        # The exact state definitions already imply this one-hot property;
        # keeping it explicit makes S[v,H] a strong public one-hot interface.
        encoder.add_clause([_literal(atom) for atom in vertex_atoms])
        for first, second in itertools.combinations(vertex_atoms, 2):
            encoder.add_clause([-_literal(first), -_literal(second)])
    return states


def _build_occupancy_and_full(
    encoder: _RawEncoder,
    order: int,
    spec: DownsetSpec,
    catalog: Sequence[StateRows],
    states: Mapping[StateKey, Clauses],
) -> tuple[dict[StateRows, Clauses], dict[int, Clauses]]:
    occupied: dict[StateRows, Clauses] = {}
    for rows in catalog:
        atom = encoder.new_var(
            f"ds_occupied({'_'.join(str(value) for value in rows)})",
            role="downset_occupied_state",
            rows=list(rows),
            kind=classify_state(rows, spec),
        )
        encoder.equiv_or(
            atom,
            [_literal(states[(vertex, rows)]) for vertex in range(1, order + 1)],
        )
        occupied[rows] = atom

    exceptional = tuple(
        rows
        for rows in catalog
        if classify_state(rows, spec) == EXCEPTIONAL_KIND
    )
    full: dict[int, Clauses] = {}
    for vertex in range(1, order + 1):
        atom = encoder.new_var(
            f"ds_full({vertex})",
            role="downset_full_state",
            vertex=vertex,
            kind=EXCEPTIONAL_KIND,
        )
        encoder.equiv_or(
            atom,
            [_literal(states[(vertex, rows)]) for rows in exceptional],
        )
        full[vertex] = atom
    return occupied, full


def _planned_state_variable_names(
    order: int,
    spec: DownsetSpec,
    catalog: Sequence[StateRows],
    *,
    include_start_endpoints: bool,
) -> tuple[str, ...]:
    names: list[str] = []
    for family, _color, target_length in _family_definitions(spec):
        for length in range(2, target_length + 1):
            for left, right in itertools.combinations(range(1, order + 1), 2):
                names.append(f"ds_terminal({family},{length},{left},{right})")
        for length in range(3, target_length + 1):
            for left, right in itertools.combinations(range(1, order + 1), 2):
                for predecessor in range(1, left):
                    names.append(
                        "ds_terminal_extension("
                        f"{family},{length},{predecessor},{left},{right})"
                    )

    if include_start_endpoints:
        for family, _color, target_length in _family_definitions(spec):
            path_keys: set[StartPathKey] = set()
            for left, right in itertools.combinations(range(1, order + 1), 2):
                path_keys.add((family, 2, left, left, right))
                names.append(
                    f"ds_start_path({family},2,{left},{left},{right})"
                )
            for length in range(3, target_length + 1):
                for start, left, right in itertools.combinations(
                    range(1, order + 1), 3
                ):
                    path_keys.add((family, length, start, left, right))
                    names.append(
                        "ds_start_path("
                        f"{family},{length},{start},{left},{right})"
                    )
            for length in range(3, target_length + 1):
                for start, left, right in itertools.combinations(
                    range(1, order + 1), 3
                ):
                    for predecessor in range(start, left):
                        prefix = (family, length - 1, start, predecessor, left)
                        if prefix in path_keys:
                            names.append(
                                "ds_start_extension("
                                f"{family},{length},{start},{predecessor},"
                                f"{left},{right})"
                            )
            for vertex in range(1, order + 1):
                for start in range(1, vertex):
                    names.append(
                        f"ds_start_present({family},{vertex},{start})"
                    )

    for vertex in range(1, order + 1):
        for x in range(1, spec.width + 1):
            for y in range(1, spec.height + 1):
                names.append(f"ds_cell({vertex},{x},{y})")
                for terminal_left in range(1, vertex):
                    names.append(
                        "ds_cell_witness("
                        f"{vertex},{x},{y},{terminal_left})"
                    )
        for rows in catalog:
            row_token = "_".join(str(value) for value in rows)
            names.append(f"ds_state({vertex},{row_token})")

    for rows in catalog:
        row_token = "_".join(str(value) for value in rows)
        names.append(f"ds_occupied({row_token})")
    names.extend(f"ds_full({vertex})" for vertex in range(1, order + 1))
    return tuple(names)


def add_downset_state_encoding(
    instance: Any,
    *,
    order: int | None = None,
    spec: DownsetSpec = STATE_756_SPEC,
    include_start_endpoints: bool = True,
) -> DownsetStateEncoding:
    """Append and attach an exact terminal-pair state encoding.

    Installation is deliberately opt-in and may occur at most once per
    instance.  ``order`` defaults to the base instance's ``problem.N``
    metadata, falling back to its complete triple map.  A smaller explicit
    order is allowed to encode a prefix of a larger base instance.
    """

    if not isinstance(spec, DownsetSpec):
        raise TypeError("spec must be a DownsetSpec")
    if type(include_start_endpoints) is not bool:
        raise TypeError("include_start_endpoints must be a boolean")
    order = _validate_and_resolve_order(instance, order)

    catalog = enumerate_states(spec)
    ordinary = tuple(
        rows for rows in catalog if classify_state(rows, spec) != EXCEPTIONAL_KIND
    )
    exceptional = tuple(
        rows for rows in catalog if classify_state(rows, spec) == EXCEPTIONAL_KIND
    )
    catalog_hash = _catalog_sha256(catalog)

    _require_unallocated_variable_names(
        instance,
        _planned_state_variable_names(
            order,
            spec,
            catalog,
            include_start_endpoints=include_start_endpoints,
        ),
        label="down-set state encoding",
    )

    encoder = _RawEncoder(instance)
    terminal_paths = _build_terminal_paths(encoder, instance, order, spec)
    if include_start_endpoints:
        start_paths, starts = _build_fixed_start_paths(
            encoder, instance, order, spec
        )
    else:
        start_paths, starts = {}, {}
    cells = _build_cells(encoder, order, spec, terminal_paths)
    states = _build_states(encoder, order, spec, catalog, cells)
    occupied, full = _build_occupancy_and_full(
        encoder, order, spec, catalog, states
    )

    instance.add(encoder.clauses, group=DOWNSET_STATE_CLAUSE_GROUP)
    encoding = DownsetStateEncoding(
        order=order,
        spec=spec,
        group=DOWNSET_STATE_CLAUSE_GROUP,
        include_start_endpoints=include_start_endpoints,
        catalog=catalog,
        catalog_sha256=catalog_hash,
        ordinary_catalog=ordinary,
        exceptional_catalog=exceptional,
        terminal_path_vars=_freeze(terminal_paths),
        cell_vars=_freeze(cells),
        state_vars=_freeze(states),
        occupancy_vars=_freeze(occupied),
        full_vars=_freeze(full),
        start_path_vars=_freeze(start_paths),
        start_vars=_freeze(starts),
        instance=instance,
    )
    instance.downset_state_encoding = encoding
    instance.set_metadata(
        downset_state_encoding={
            "schema": DOWNSET_STATE_SCHEMA,
            "order": order,
            "group": DOWNSET_STATE_CLAUSE_GROUP,
            "include_start_endpoints": include_start_endpoints,
            "families": {
                PATH5_FAMILY: {
                    "color": spec.path5_color,
                    "target_length": spec.path5_split_length,
                },
                PATH6_FAMILY: {
                    "color": spec.path6_color,
                    "target_length": spec.path6_split_length,
                },
            },
            "catalog": [list(rows) for rows in catalog],
            "catalog_sha256": catalog_hash,
            "catalog_count": len(catalog),
            "ordinary_count": len(ordinary),
            "exceptional_count": len(exceptional),
            "clause_count": len(encoder.clauses),
        }
    )
    return encoding


__all__ = [
    "DOWNSET_STATE_CLAUSE_GROUP",
    "DOWNSET_STATE_SCHEMA",
    "PATH5_FAMILY",
    "PATH6_FAMILY",
    "DownsetStateEncoding",
    "add_downset_state_encoding",
]
