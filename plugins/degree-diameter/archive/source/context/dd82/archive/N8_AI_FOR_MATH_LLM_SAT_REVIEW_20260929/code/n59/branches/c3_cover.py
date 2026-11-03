#!/usr/bin/env python3
"""Generate the 35-point four-cover encoding for the surviving ``c3`` branch.

The first cover labels ``Y`` as five fibres of size seven.  Its ten
inter-fibre perfect matchings parameterize the 4-regular graph ``D``; four
matchings incident with fibre zero are fixed to the identity, leaving six
7-by-7 permutation matrices.  Three additional K5-cover coordinates are
encoded with exact closed-neighbourhood equations.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

from sat59.enc.and_gate import add_iff_and
from sat59.enc.cardinality import (
    enforce_at_least,
    enforce_at_most,
    enforce_exactly,
    unary_thresholds,
)
from sat59.enc.connectivity_cuts import CutLedger, add_ledger_cuts
from sat59.enc.cnf import (
    CNFBuilder,
    CountingCNFBuilder,
    StreamingCNFBuilder,
    write_json,
)
from sat59.enc.threshold import DefectThresholds, encode_b_entry, enforce_b_row_sum
from sat59.theory.branch_specs import BRANCH_SPECS


Term = int | bool
Pair = tuple[int, int]
K = tuple(range(4))
X = tuple(range(4, 24))
Y = tuple(range(24, 59))


def pair(u: int, v: int) -> Pair:
    if u == v:
        raise ValueError("a graph edge needs distinct endpoints")
    return (u, v) if u < v else (v, u)


def x_vertex(coordinate: int, value: int) -> int:
    return 4 + 5 * coordinate + value


def y_vertex(fibre: int, index: int) -> int:
    return 24 + 7 * fibre + index


def y_coordinates(vertex: int) -> tuple[int, int]:
    if vertex not in Y:
        raise ValueError(vertex)
    return divmod(vertex - 24, 7)




class C3CoverEncoder:
    """Exact cover-coordinate encoding of the c3 quotient branch."""

    def __init__(self, builder: CNFBuilder) -> None:
        self.builder = builder
        self.d_vars: dict[Pair, int] = {}
        self.color_vars: dict[tuple[int, int, int], int] = {}
        self.fixed_edges: set[Pair] = set()
        self.b_x: dict[Pair, DefectThresholds] = {}
        self.b_y: dict[Pair, DefectThresholds] = {}
        self.support_x: dict[Pair, Term] = {}
        self.support_y: dict[Pair, Term] = {}
        self.cut_count = 0
        self.connectivity_cut_ledger = CutLedger("c3").to_json()
        self._allocate_primary_variables()

    def _allocate_primary_variables(self) -> None:
        for u, v in itertools.combinations(K, 2):
            self.fixed_edges.add(pair(u, v))
        for r in range(4):
            for s in range(5):
                self.fixed_edges.add(pair(r, x_vertex(r, s)))

        # f_0(y_(a,t))=a fixes the first X-Y cover.
        for a in range(5):
            for t in range(7):
                self.fixed_edges.add(pair(x_vertex(0, a), y_vertex(a, t)))

        # Four matchings from fibre zero are fixed to identity.  Only the six
        # matchings among fibres 1,...,4 remain as permutation matrices.
        for b in range(1, 5):
            for t in range(7):
                self.fixed_edges.add(pair(y_vertex(0, t), y_vertex(b, t)))
        for a in range(1, 5):
            for b in range(a + 1, 5):
                for t in range(7):
                    for u in range(7):
                        left, right = y_vertex(a, t), y_vertex(b, u)
                        self.d_vars[pair(left, right)] = self.builder.var(
                            ("c3", "D", a, b, t, u), "D_matching_edge"
                        )

        for r in range(1, 4):
            for y in Y:
                for s in range(5):
                    self.color_vars[(r, y, s)] = self.builder.var(
                        ("c3", "color", r, y, s), "cover_color"
                    )

    def d(self, u: int, v: int) -> Term:
        if u == v:
            return False
        a, t = y_coordinates(u)
        b, s = y_coordinates(v)
        if a == b:
            return False
        if a > b:
            a, b, t, s = b, a, s, t
        if a == 0:
            return t == s
        return self.d_vars[pair(u, v)]

    def color(self, coordinate: int, y: int, value: int) -> Term:
        if coordinate == 0:
            fibre, _index = y_coordinates(y)
            return fibre == value
        return self.color_vars[(coordinate, y, value)]

    def product(self, left: Term, right: Term, key) -> Term:
        return add_iff_and(
            self.builder,
            left,
            right,
            ("c3", key),
            kind="common_and",
        )

    def _encode_permutation_matrices(self) -> None:
        for a in range(1, 5):
            for b in range(a + 1, 5):
                for t in range(7):
                    enforce_exactly(
                        self.builder,
                        [self.d(y_vertex(a, t), y_vertex(b, u)) for u in range(7)],
                        1,
                        ("c3", "D_matching_row", a, b, t),
                    )
                for u in range(7):
                    enforce_exactly(
                        self.builder,
                        [self.d(y_vertex(a, t), y_vertex(b, u)) for t in range(7)],
                        1,
                        ("c3", "D_matching_column", a, b, u),
                    )

    def _encode_cover_colors(self) -> None:
        for r in range(1, 4):
            for y in Y:
                enforce_exactly(
                    self.builder,
                    [self.color(r, y, s) for s in range(5)],
                    1,
                    ("c3", "color_onehot", r, y),
                )
            for s in range(5):
                enforce_exactly(
                    self.builder,
                    [self.color(r, y, s) for y in Y],
                    7,
                    ("c3", "color_class_size", r, s),
                )

        # Every dynamic color class is an independent perfect code in D.
        for r in range(1, 4):
            for y in Y:
                for s in range(5):
                    terms: list[Term] = [self.color(r, y, s)]
                    for z in Y:
                        if z == y:
                            continue
                        terms.append(
                            self.product(
                                self.d(y, z), self.color(r, z, s),
                                ("perfect_code", r, y, s, z),
                            )
                        )
                    enforce_exactly(
                        self.builder,
                        terms,
                        1,
                        ("c3", "perfect_code_exact", r, y, s),
                    )

    def _encode_joint_symmetry_breaking(self) -> None:
        anchor = y_vertex(0, 0)
        for r in range(1, 4):
            self.builder.add_clause(int(self.color(r, anchor, 0)))

        # The remaining simultaneous S6 action on fibre-zero indices sorts
        # their three-coordinate tuples lexicographically.  No other fibre is
        # sorted independently.
        tuples = tuple(itertools.product(range(5), repeat=3))
        for t in range(1, 6):
            left_y = y_vertex(0, t)
            right_y = y_vertex(0, t + 1)
            for left_tuple in tuples:
                for right_tuple in tuples:
                    if left_tuple <= right_tuple:
                        continue
                    clause = [
                        -int(self.color(r, left_y, left_tuple[r - 1]))
                        for r in range(1, 4)
                    ]
                    clause.extend(
                        -int(self.color(r, right_y, right_tuple[r - 1]))
                        for r in range(1, 4)
                    )
                    self.builder.add_clause(*clause)

    def _intersection_terms(
        self, r: int, value_r: int, s: int, value_s: int
    ) -> list[Term]:
        terms: list[Term] = []
        for y in Y:
            terms.append(
                self.product(
                    self.color(r, y, value_r),
                    self.color(s, y, value_s),
                    ("class_intersection", r, value_r, s, value_s, y),
                )
            )
        return terms

    def _encode_cross_coordinate_intersections(self) -> None:
        for r, s in itertools.combinations(range(4), 2):
            for value_r in range(5):
                for value_s in range(5):
                    enforce_at_least(
                        self.builder,
                        self._intersection_terms(r, value_r, s, value_s),
                        1,
                        ("c3", "nonempty_class_intersection", r, value_r, s, value_s),
                    )

    def _encode_x_repeat_block(self) -> None:
        by_vertex: dict[int, list[DefectThresholds]] = {x: [] for x in X}
        for r, s in itertools.combinations(range(4), 2):
            for value_r in range(5):
                for value_s in range(5):
                    u, v = x_vertex(r, value_r), x_vertex(s, value_s)
                    terms = self._intersection_terms(r, value_r, s, value_s)
                    entry = encode_b_entry(
                        self.builder,
                        terms,
                        ("c3", "B_X", u, v),
                        max_b=5,
                    )
                    uv = pair(u, v)
                    self.b_x[uv] = entry
                    self.support_x[uv] = entry.support
                    by_vertex[u].append(entry)
                    by_vertex[v].append(entry)
        for vertex, entries in by_vertex.items():
            enforce_b_row_sum(
                self.builder, entries, 6, ("c3", "B_X_row", vertex)
            )

    def _same_x_terms(self, u: int, v: int) -> list[Term]:
        terms: list[Term] = []
        for r in range(4):
            for s in range(5):
                terms.append(
                    self.product(
                        self.color(r, u, s), self.color(r, v, s),
                        ("same_X_neighbour", r, s, u, v),
                    )
                )
        return terms

    def _common_d_terms(self, u: int, v: int) -> list[Term]:
        return [
            self.product(
                self.d(u, w), self.d(v, w),
                ("common_D_neighbour", u, v, w),
            )
            for w in Y
            if w not in (u, v)
        ]

    def _encode_y_repeat_block(self) -> None:
        by_vertex: dict[int, list[DefectThresholds]] = {y: [] for y in Y}
        for u, v in itertools.combinations(Y, 2):
            edge = self.d(u, v)
            same_x = self._same_x_terms(u, v)
            common_d = self._common_d_terms(u, v)
            terms: list[Term] = [edge, *same_x, *common_d]
            entry = encode_b_entry(
                self.builder,
                terms,
                ("c3", "B_Y", u, v),
                max_b=5,
            )
            uv = pair(u, v)
            self.b_y[uv] = entry
            self.support_y[uv] = entry.support
            by_vertex[u].append(entry)
            by_vertex[v].append(entry)

            if edge is not False:
                common_terms = [*same_x, *common_d]
                if edge is True:
                    enforce_at_most(
                        self.builder,
                        common_terms,
                        3,
                        ("c3", "adjacent_common_cap", u, v),
                    )
                else:
                    thresholds = unary_thresholds(
                        self.builder,
                        common_terms,
                        4,
                        ("c3", "adjacent_common_cap", u, v),
                        kind="adjacent_common_threshold",
                    )
                    fourth = thresholds.ge(4)
                    if fourth is True:
                        self.builder.add_clause(-int(edge))
                    elif fourth is not False:
                        self.builder.add_clause(-int(edge), -int(fourth))

        for vertex, entries in by_vertex.items():
            enforce_b_row_sum(
                self.builder, entries, 6, ("c3", "B_Y_row", vertex)
            )

    def add_connectivity_cuts(self, ledger: CutLedger) -> None:
        vertices_by_scope = {"X": X, "Y": Y}
        selectors_by_scope = {
            "X": {
                pair(u, v): self.support_x.get(pair(u, v), False)
                for u, v in itertools.combinations(X, 2)
            },
            "Y": {
                pair(u, v): self.support_y[pair(u, v)]
                for u, v in itertools.combinations(Y, 2)
            },
        }
        self.cut_count = add_ledger_cuts(
            self.builder,
            selectors_by_scope,
            ledger,
            branch_id="c3",
            vertices_by_scope=vertices_by_scope,
        )
        self.connectivity_cut_ledger = ledger.to_json()

    def encode(self, cuts: CutLedger) -> None:
        self._encode_permutation_matrices()
        self._encode_cover_colors()
        self._encode_joint_symmetry_breaking()
        self._encode_cross_coordinate_intersections()
        self._encode_x_repeat_block()
        self._encode_y_repeat_block()
        self.add_connectivity_cuts(cuts)

    def mapping(self) -> dict:
        spec = BRANCH_SPECS["c3"]
        edge_variables = []
        for (u, v), variable in sorted(self.d_vars.items()):
            edge_variables.append({"u": u, "v": v, "var": variable})
        for (r, y, s), variable in sorted(self.color_vars.items()):
            edge_variables.append(
                {"u": x_vertex(r, s), "v": y, "var": variable}
            )
        support_variables = [
            {"u": u, "v": v, "term": term, "scope": "X"}
            for (u, v), term in sorted(self.support_x.items())
        ]
        support_variables.extend(
            {"u": u, "v": v, "term": term, "scope": "Y"}
            for (u, v), term in sorted(self.support_y.items())
        )
        return self.builder.variable_map(
            encoding="sat59-c3-cover-v1",
            branch="c3",
            order=59,
            roles=spec.source_roles,
            component_sizes=spec.source_sizes,
            quotient=spec.source_quotient,
            fixed_edges=[list(edge) for edge in sorted(self.fixed_edges)],
            edge_variables=edge_variables,
            support_variables=support_variables,
            support_scopes={"X": list(X), "Y": list(Y)},
            connectivity_mode="finite_cut_relaxation",
            connectivity_cuts=self.cut_count,
            connectivity_cut_ledger=self.connectivity_cut_ledger,
        )


def load_cuts(path: Path | None) -> CutLedger:
    if path is None:
        return CutLedger("c3")
    return CutLedger.load(path, branch_id="c3")


def generate(
    *,
    cnf_path: Path | None = None,
    map_path: Path | None = None,
    stats_path: Path | None = None,
    cuts_path: Path | None = None,
) -> dict:
    builder: CNFBuilder
    if cnf_path is None:
        builder = CountingCNFBuilder()
    else:
        builder = StreamingCNFBuilder(cnf_path)
    encoder = C3CoverEncoder(builder)
    cuts = load_cuts(cuts_path)
    try:
        encoder.encode(cuts)
        builder.finish()
    except BaseException:
        builder.abort()
        raise
    stats = {
        **builder.stats(),
        "encoding": "sat59-c3-cover-v1",
        "branch": "c3",
        "D_permutation_variables": len(encoder.d_vars),
        "cover_color_variables": len(encoder.color_vars),
        "primary_edge_variables": len(encoder.d_vars) + len(encoder.color_vars),
        "fixed_edges": len(encoder.fixed_edges),
        "connectivity_cuts": encoder.cut_count,
        "connectivity_cut_ledger": encoder.connectivity_cut_ledger,
        "connectivity_complete": False,
    }
    if cnf_path is not None:
        stats["cnf_path"] = str(cnf_path)
        stats["cnf_bytes"] = cnf_path.stat().st_size
    if map_path is not None:
        write_json(map_path, encoder.mapping())
        stats["map_path"] = str(map_path)
        stats["map_bytes"] = map_path.stat().st_size
    if stats_path is not None:
        write_json(stats_path, stats)
    return stats


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cnf", type=Path, help="write DIMACS; omit for count-only")
    parser.add_argument("--map", dest="map_path", type=Path)
    parser.add_argument("--stats", dest="stats_path", type=Path)
    parser.add_argument("--cuts", dest="cuts_path", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    stats = generate(
        cnf_path=args.cnf,
        map_path=args.map_path,
        stats_path=args.stats_path,
        cuts_path=args.cuts_path,
    )
    print(json.dumps(stats, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
