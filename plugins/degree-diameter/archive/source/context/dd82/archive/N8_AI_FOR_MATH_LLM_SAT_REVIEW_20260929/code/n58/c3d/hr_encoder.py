#!/usr/bin/env python3
"""Exact H_R realization CNF for one valid anonymous 3D block cover.

The input has already fixed a complete phase and eighteen signed four-blocks.
This final layer creates only H_R edges whose unsigned supports are disjoint,
then enforces the four-regular right block equations, H_R connectivity, all
residual R--R diameter constraints, and connected support of B_R.  Its map
has ``full_graph`` semantics and can be passed directly to
``sat58.verify.verify_model_v2``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Sequence

from sat58.branches.common import ProductCache, enforce_regular_graph
from sat58.branches.v2_common import add_connected_spanning_tree
from sat58.v3.c3d.block_cover import load_block_cover_solution
from sat58.v3.c3d.hr_interface import (
    MIDDLE_OFFSET,
    RIGHT_OFFSET,
    RIGHT_SIZE,
    candidate_hr_edges,
    expand_block_occurrences,
    reconstruct_full_matrix,
)
from sat58.v3.c3d.tables import DEFAULT_TABLES_PATH, ParityRoot
from sat59.enc import (
    BoolTerm,
    CNFBuilder,
    CountingCNFBuilder,
    StreamingCNFBuilder,
    add_simplified_clause,
    enforce_exactly,
    unary_thresholds,
    write_json,
)


ENCODING = "sat58-v3-3d-hr-realization-v1"


class C3DHRRealizationEncoder:
    """Build the final exact full-graph formula after the block layer."""

    def __init__(
        self,
        builder: CNFBuilder,
        root: ParityRoot,
        phases: Sequence[Sequence[int]],
        occurrences: Sequence[Sequence[int]],
    ) -> None:
        if len(occurrences) != RIGHT_SIZE:
            raise ValueError("H_R realization requires 18 block occurrences")
        self.builder = builder
        self.root = root
        self.phases = tuple(tuple(map(int, row)) for row in phases)
        self.occurrences = tuple(tuple(map(int, block)) for block in occurrences)
        self.namespace = ("sat58", "v3", "3D", root.branch_id, "H_R")
        candidates = candidate_hr_edges(self.occurrences)
        self.edge_vars = {
            edge: builder.var((self.namespace, "edge", *edge), "H_R_edge")
            for edge in candidates
        }
        self.h_right: tuple[tuple[BoolTerm, ...], ...] = tuple(
            tuple(
                False
                if first == second
                else self.edge_vars.get(tuple(sorted((first, second))), False)
                for second in range(RIGHT_SIZE)
            )
            for first in range(RIGHT_SIZE)
        )
        self.products = ProductCache(builder, (self.namespace, "products"))
        self.hr_connectivity: dict[str, int] = {}
        self.br_connectivity: dict[str, int] = {}
        self.right_equations = 0
        self.rr_diameter_clauses = 0
        self.br_entries = 0

    def _encode_right_graph(self) -> None:
        enforce_regular_graph(
            self.builder,
            self.h_right,
            4,
            (self.namespace, "degree"),
        )
        self.hr_connectivity = add_connected_spanning_tree(
            self.builder,
            self.h_right,
            (self.namespace, "connected"),
        )

    def _encode_right_block_equations(self) -> None:
        block_sets = [set(block) for block in self.occurrences]
        for right, block in enumerate(block_sets):
            support = {item // 2 for item in block}
            for edge in range(12):
                plus_terms = [
                    self.h_right[right][other]
                    for other in range(RIGHT_SIZE)
                    if 2 * edge in block_sets[other]
                ]
                minus_terms = [
                    self.h_right[right][other]
                    for other in range(RIGHT_SIZE)
                    if 2 * edge + 1 in block_sets[other]
                ]
                target = 0 if edge in support else 1
                enforce_exactly(
                    self.builder,
                    plus_terms,
                    target,
                    (self.namespace, "right_equation_plus", right, edge),
                )
                enforce_exactly(
                    self.builder,
                    minus_terms,
                    target,
                    (self.namespace, "right_equation_minus", right, edge),
                )
                self.right_equations += 2

    def _path_terms(self, first: int, second: int) -> list[BoolTerm]:
        terms: list[BoolTerm] = [self.h_right[first][second]]
        terms.extend(
            self.products.product(
                self.h_right[first][other], self.h_right[second][other]
            )
            for other in range(RIGHT_SIZE)
            if other not in (first, second)
        )
        common_signed = len(
            set(self.occurrences[first]) & set(self.occurrences[second])
        )
        terms.extend([True] * common_signed)
        return terms

    def _encode_right_diameter_and_repeat_support(self) -> None:
        b_support: list[list[BoolTerm]] = [
            [False for _ in range(RIGHT_SIZE)] for _ in range(RIGHT_SIZE)
        ]
        for first in range(RIGHT_SIZE):
            for second in range(first + 1, RIGHT_SIZE):
                paths = self._path_terms(first, second)
                self.rr_diameter_clauses += int(
                    add_simplified_clause(self.builder, *paths)
                )
                thresholds = unary_thresholds(
                    self.builder,
                    paths,
                    2,
                    (self.namespace, "B_R_positive", first, second),
                    kind="B_R_threshold",
                )
                positive = thresholds.ge(2)
                b_support[first][second] = b_support[second][first] = positive
                self.br_entries += 1
        self.br_connectivity = add_connected_spanning_tree(
            self.builder,
            b_support,
            (self.namespace, "B_R_support_connected"),
        )

    def encode(self) -> None:
        self._encode_right_graph()
        self._encode_right_block_equations()
        self._encode_right_diameter_and_repeat_support()

    @property
    def fixed_edges(self) -> tuple[tuple[int, int], ...]:
        matrix = reconstruct_full_matrix(self.phases, self.occurrences, ())
        return tuple(
            (first, second)
            for first in range(58)
            for second in range(first + 1, 58)
            if matrix[first][second]
        )

    def mapping(self) -> dict:
        edge_variables = [
            {
                "u": RIGHT_OFFSET + first,
                "v": RIGHT_OFFSET + second,
                "var": variable,
                "kind": "H_R",
                "right_u": first,
                "right_v": second,
            }
            for (first, second), variable in sorted(self.edge_vars.items())
        ]
        return self.builder.variable_map(
            schema_version="sat58-structured-edge-map-v2",
            encoding=ENCODING,
            order=58,
            family="3D",
            branch="3D",
            branch_id=self.root.branch_id,
            quotient_type="3D",
            sat_semantics="full_graph",
            strict_family=True,
            block_sizes=[16, 24, 18],
            block_offsets=[0, MIDDLE_OFFSET, RIGHT_OFFSET],
            quotient=[[2, 6, 0], [4, 1, 3], [0, 4, 4]],
            parity_table_index=self.root.table_index,
            phases=[list(row) for row in self.phases],
            right_blocks=[list(block) for block in self.occurrences],
            fixed_edges=[list(edge) for edge in self.fixed_edges],
            edge_variables=edge_variables,
            split_candidates=[
                {
                    "literal": row["var"],
                    "kind": "H_R_edge",
                    "semantic": f"H_R({row['right_u']},{row['right_v']})",
                }
                for row in edge_variables
            ],
            implicit_edges="all unmapped unordered pairs are false",
            soundness=["EQUIV", "NEC", "REDUNDANT"],
            theory_lemmas=[
                "3D-HL-4C4",
                "3D-complete-phase",
                "3D-anonymous-block-cover",
                "3D-right-block-equations",
                "3D-HR-connected",
                "3D-BR-support-connected",
            ],
            model_verifier=(
                "python3 -B -m sat58.v3.c3d.verify_hr_model "
                "--model MODEL --map MAP"
            ),
        )


def generate(
    *,
    cover_path: Path | str,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
    cnf_path: Path | str | None = None,
    map_path: Path | str | None = None,
    stats_path: Path | str | None = None,
) -> dict:
    root, phases, counts = load_block_cover_solution(
        cover_path, tables_path=tables_path
    )
    occurrences = expand_block_occurrences(phases, counts)
    cnf = None if cnf_path is None else Path(cnf_path)
    builder: CNFBuilder = CountingCNFBuilder() if cnf is None else StreamingCNFBuilder(cnf)
    encoder = C3DHRRealizationEncoder(builder, root, phases, occurrences)
    try:
        encoder.encode()
        builder.finish()
    except BaseException:
        builder.abort()
        raise
    stats = {
        **builder.stats(),
        "encoding": ENCODING,
        "family": "3D",
        "branch_id": root.branch_id,
        "layer": "H_R",
        "sat_semantics": "full_graph",
        "soundness": ["EQUIV", "NEC", "REDUNDANT"],
        "candidate_H_R_edges": len(encoder.edge_vars),
        "forbidden_H_R_edges": 153 - len(encoder.edge_vars),
        "right_block_equations": encoder.right_equations,
        "R_R_diameter_pairs": 153,
        "R_R_nontrivial_diameter_clauses": encoder.rr_diameter_clauses,
        "B_R_entries": encoder.br_entries,
        "H_R_connectivity": encoder.hr_connectivity,
        "B_R_connectivity": encoder.br_connectivity,
        "cached_products": encoder.products.cached_products,
        "fixed_graph_edges": len(encoder.fixed_edges),
    }
    if cnf is not None:
        stats.update(cnf_path=str(cnf), cnf_bytes=cnf.stat().st_size)
    if map_path is not None:
        mapping_path = Path(map_path)
        write_json(mapping_path, encoder.mapping())
        stats.update(map_path=str(mapping_path), map_bytes=mapping_path.stat().st_size)
    if stats_path is not None:
        write_json(Path(stats_path), stats)
    return stats


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cover", type=Path, required=True)
    parser.add_argument("--tables", type=Path, default=DEFAULT_TABLES_PATH)
    parser.add_argument("--cnf", type=Path)
    parser.add_argument("--map", dest="map_path", type=Path)
    parser.add_argument("--stats", dest="stats_path", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(
        json.dumps(
            generate(
                cover_path=args.cover,
                tables_path=args.tables,
                cnf_path=args.cnf,
                map_path=args.map_path,
                stats_path=args.stats_path,
            ),
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
