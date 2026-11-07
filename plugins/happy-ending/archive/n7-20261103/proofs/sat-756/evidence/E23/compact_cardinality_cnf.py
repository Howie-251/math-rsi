"""Compact (7,5,6) encoding with exact counting and one-way prohibitions.

This is a separate interface: no legacy ``cap``/``cup`` dictionaries are
exposed. Outer witnesses are closure markers, not exact path predicates.
Terminal predicates, endpoint flags, and optional cells are exact.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from types import MappingProxyType
from typing import Any, Mapping

from lib.downset_state import STATE_756_SPEC
from lib.downset_state_cnf import (
    PATH5_FAMILY,
    PATH6_FAMILY,
    _RawEncoder,
    _build_cells,
    _build_terminal_paths,
)
from lib.sat_tseitin import SATInstance


ENCODING = "compact_cardinality_756_v1"
STRICT = "strict_no_target"
RELAXED = "target_allowed_relaxed"
MODES = (STRICT, RELAXED)
BLUE, RED = -1, 1


@dataclass(frozen=True)
class CompactBase:
    order: int
    mode: str
    bridges: bool
    num_vars: int
    clauses: tuple[tuple[int, ...], ...]
    # Triple/outer/witness keys are zero-based, as in lib.erdos.
    triples: Mapping[tuple[int, int, int], int]
    outer_witnesses: Mapping[tuple[int, int, int, int], int]
    path_witnesses: Mapping[tuple[int, int, int, int, int], int]
    # Exact predicates use the existing one-based down-set API.
    terminal_paths: Mapping[tuple[str, int, int, int], int]
    exceptional_flags: Mapping[int, int]
    cells: Mapping[tuple[int, int, int], int]
    variable_records: tuple[Mapping[str, Any], ...]
    clause_groups: tuple[tuple[str, int], ...]

    def metadata(self, *, include_variables: bool = False) -> dict[str, Any]:
        result = {
            "schema": ENCODING,
            "order": self.order,
            "mode": self.mode,
            "bridges": self.bridges,
            "num_vars": self.num_vars,
            "num_clauses": len(self.clauses),
            "group_clause_counts": dict(self.clause_groups),
            "semantics": STATE_756_SPEC.semantics_dict(),
            "signotope": True,
            "global_no_7_gon": self.mode == STRICT,
            "symmetry_breaking": False,
            "outer_witness_semantics": "one_way_closure_only_not_path_existence",
            "terminal_path_semantics": "exact_terminal_pair_path_existence",
            "exceptional_flag_semantics": "exact_blue4_and_red5_at_same_right_endpoint",
            "state_injection": "complete_coloring_and_path_bounds_lemma",
            "exceptional_literals": [self.exceptional_flags[v] for v in range(1, self.order + 1)],
        }
        if include_variables:
            result["variables"] = [dict(row) for row in self.variable_records]
        return result


def build_compact_base(
    order: int, *, mode: str = STRICT, bridges: bool = False
) -> CompactBase:
    """Build a fresh deterministic base; small orders support semantic tests.

    Reuse the original exact terminal/cell recurrence without changing any
    legacy builder. Each build owns its internal SATInstance; only immutable
    clauses and literal maps escape this function.
    """
    if type(order) is not int or not 1 <= order <= 35:
        raise ValueError("order must be a plain integer in 1..35")
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}")
    if type(bridges) is not bool:
        raise ValueError("bridges must be a boolean")
    instance = SATInstance()
    instance.v = {
        (i, j, k): instance.new_var(
            f"x_{i + 1}_{j + 1}_{k + 1}", role="triple", i=i + 1, j=j + 1, k=k + 1
        )
        for i, j, k in combinations(range(order), 3)
    }
    triples = {key: atom._lit for key, atom in instance.v.items()}
    outer: dict[tuple[int, int, int, int], int] = {}
    witnesses: dict[tuple[int, int, int, int, int], int] = {}

    for color, bound, flip, name in ((BLUE, 5, False, "blue"), (RED, 6, True, "red")):
        raw = _RawEncoder(instance)
        for i, j in combinations(range(order), 2):
            for length in range(2, min(bound, j - i + 1) + 1):
                outer[color, i, j, length] = raw.new_var(
                    f"compact_outer({name},{i + 1},{j + 1},{length})",
                    role="compact_one_way_outer", color=name, start=i + 1,
                    end=j + 1, length=length, exact=False,
                )._lit
        for i, j, k in combinations(range(order), 3):
            top = min(bound, k - j + 2 if flip else j - i + 2)
            witnesses[color, i, j, k, 3] = color * triples[i, j, k]
            for length in range(4, top + 1):
                witnesses[color, i, j, k, length] = raw.new_var(
                    f"compact_witness({name},{i + 1},{j + 1},{k + 1},{length})",
                    role="compact_one_way_witness", color=name, start=i + 1,
                    middle=j + 1, end=k + 1, length=length,
                    middle_role="second" if flip else "penultimate", exact=False,
                )._lit
        for i, j in combinations(range(order), 2):
            raw.add_clause([outer[color, i, j, 2]])
            if j - i + 1 >= bound:
                raw.add_clause([-outer[color, i, j, bound]])
            for length in range(3, min(bound, j - i + 1) + 1):
                raw.add_clause([-outer[color, i, j, length], outer[color, i, j, length - 1]])
        for i, j, k in combinations(range(order), 3):
            top = min(bound, k - j + 2 if flip else j - i + 2)
            for length in range(3, top + 1):
                witness = witnesses[color, i, j, k, length]
                raw.add_clause([-witness, outer[color, i, k, length]])
                if length < bound:
                    for ell in (range(i) if flip else range(k + 1, order)):
                        triple = (ell, i, j) if flip else (j, k, ell)
                        child = ((color, ell, i, k, length + 1) if flip
                                 else (color, i, k, ell, length + 1))
                        raw.add_clause([-witness, -color * triples[triple], witnesses[child]])
        instance.add(raw.clauses, group=f"compact_{name}_path_bound")

    packets = []
    for i, j, k, ell in combinations(range(order), 4):
        p, q, r, s = (triples[t] for t in ((i, j, k), (i, j, ell), (i, k, ell), (j, k, ell)))
        packets.extend(([-p, -s, q], [-q, -s, r], [-p, -r, q],
                        [p, s, -q], [q, s, -r], [p, r, -q]))
    instance.add(packets, group="compact_signotope")
    if mode == STRICT:
        instance.add(
            [[-outer[BLUE, i, j, 4], -outer[RED, i, j, 5]]
             for i, j in combinations(range(order), 2) if j - i + 1 >= 5],
            group="compact_no_weak_7_gon",
        )

    raw = _RawEncoder(instance)
    terminal = _build_terminal_paths(raw, instance, order, STATE_756_SPEC)
    instance.add(raw.clauses, group="compact_exact_terminal")
    raw = _RawEncoder(instance)
    flags = {}
    for vertex in range(1, order + 1):
        exists = []
        for family, length in ((PATH5_FAMILY, 4), (PATH6_FAMILY, 5)):
            atom = raw.new_var(
                f"compact_ending({family},{vertex})", role="compact_exact_ending_path",
                family=family, vertex=vertex, length=length, exact=True,
            )
            raw.equiv_or(atom, [terminal[family, length, u, vertex]._lit for u in range(1, vertex)])
            exists.append(atom._lit)
        flag = raw.new_var(
            f"compact_exceptional({vertex})", role="compact_exact_exceptional",
            vertex=vertex, exact=True,
        )
        raw.equiv_and(flag, exists)
        flags[vertex] = flag._lit
    instance.add(raw.clauses, group="compact_exact_exceptional")

    cells = {}
    if bridges:
        raw = _RawEncoder(instance)
        cells = _build_cells(raw, order, STATE_756_SPEC, terminal)
        instance.add(raw.clauses, group="compact_exact_cells")
        bridge_clauses = []
        for u, v in combinations(range(1, order + 1), 2):
            for a, b in product(range(1, 4), range(1, 5)):
                clause = [-cells[u, a, b]._lit]
                # B5/R6 are false by the retained path prohibitions.
                if a < 3:
                    clause.append(terminal[PATH5_FAMILY, a + 2, u, v]._lit)
                if b < 4:
                    clause.append(terminal[PATH6_FAMILY, b + 2, u, v]._lit)
                bridge_clauses.append(clause)
        instance.add(bridge_clauses, group="compact_state_path_bridges")

    if set(instance._var_roles) != set(range(1, instance._num_vars + 1)):
        raise AssertionError("compact variable ledger is incomplete")
    return CompactBase(
        order, mode, bridges, instance._num_vars,
        tuple(tuple(c) for c in instance._clauses),
        MappingProxyType(triples), MappingProxyType(outer), MappingProxyType(witnesses),
        MappingProxyType({key: atom._lit for key, atom in terminal.items()}),
        MappingProxyType(flags), MappingProxyType({key: atom._lit for key, atom in cells.items()}),
        tuple(MappingProxyType(dict(instance._var_roles[v])) for v in range(1, instance._num_vars + 1)),
        tuple(instance._group_clause_counts.items()),
    )
