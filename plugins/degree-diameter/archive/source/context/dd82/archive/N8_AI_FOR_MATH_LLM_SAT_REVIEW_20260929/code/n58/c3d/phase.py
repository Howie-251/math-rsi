#!/usr/bin/env python3
"""Exact complete-phase frontend for one live N58 V3 3D parity root.

For a fixed parity signature, every unfixed phase has only two possible
values.  One Boolean high bit therefore represents each ``phi[t,e]`` for
``t=1,2,3``; the first circle is fixed by the safe gauge.  The CNF requires
all sixteen ordered residue pairs to occur among the 24 signed items for
every pair of circles.  This is precisely the cross-circle L--L distance-two
condition, without any signed-support or right-graph variables.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from sat58.branches.common import ProductCache
from sat58.v3.c3d.audits import audit_phase_matrices
from sat58.v3.c3d.tables import (
    CIRCLE_COUNT,
    DEFAULT_TABLES_PATH,
    PAIR_COUNT,
    ParityRoot,
    root_by_index,
)
from sat59.enc import (
    BoolTerm,
    CNFBuilder,
    CountingCNFBuilder,
    StreamingCNFBuilder,
    add_simplified_clause,
    negate,
    write_json,
)
from sat59.solver_output import load_sat_solver_output


ITEM_COUNT = 2 * PAIR_COUNT
PLUS = 0
MINUS = 1
ENCODING = "sat58-v3-3d-complete-phase-v1"


def signed_item(edge: int, sign: int) -> int:
    if not 0 <= edge < PAIR_COUNT or sign not in (PLUS, MINUS):
        raise ValueError((edge, sign))
    return 2 * edge + sign


def item_edge(item: int) -> int:
    if not 0 <= int(item) < ITEM_COUNT:
        raise ValueError(f"signed item must be in 0..{ITEM_COUNT - 1}")
    return int(item) // 2


def item_sign(item: int) -> int:
    if not 0 <= int(item) < ITEM_COUNT:
        raise ValueError(f"signed item must be in 0..{ITEM_COUNT - 1}")
    return int(item) % 2


def item_phase_word(
    phases: Sequence[Sequence[int]], item: int
) -> tuple[int, ...]:
    edge, sign = item_edge(item), item_sign(item)
    return tuple((int(phases[circle][edge]) + 2 * sign) % 4 for circle in range(4))


def validate_phase(
    root: ParityRoot,
    phases: Sequence[Sequence[int]],
) -> dict:
    """Independently check parity, gauge, and all L--L phase coverage."""

    if len(phases) != CIRCLE_COUNT or any(
        len(row) != PAIR_COUNT for row in phases
    ):
        raise ValueError("phase array must have shape 4 by 12")
    normalized = tuple(tuple(map(int, row)) for row in phases)
    if any(value not in range(4) for row in normalized for value in row):
        raise ValueError("phase entries must lie in Z4")
    for circle in range(CIRCLE_COUNT):
        for edge in range(PAIR_COUNT):
            if normalized[circle][edge] % 2 != root.parity(circle, edge):
                raise ValueError(
                    f"phase parity mismatch at circle={circle}, edge={edge}"
                )
    expected_first = tuple(0 if edge < 6 else 1 for edge in range(PAIR_COUNT))
    if normalized[0] != expected_first:
        raise ValueError("the first phase row violates the fixed A0 gauge")

    missing: list[tuple[int, int, int, int]] = []
    words = [item_phase_word(normalized, item) for item in range(ITEM_COUNT)]
    for first in range(CIRCLE_COUNT):
        for second in range(first + 1, CIRCLE_COUNT):
            observed = {(word[first], word[second]) for word in words}
            for left in range(4):
                for right in range(4):
                    if (left, right) not in observed:
                        missing.append((first, second, left, right))
    if missing:
        raise ValueError(f"phase assignment misses {len(missing)} L-L residue pairs")
    matrix_audit = audit_phase_matrices(normalized)
    return {
        "status": "VALID_PHASE",
        "parity_root_id": root.branch_id,
        "phase_entries": CIRCLE_COUNT * PAIR_COUNT,
        "signed_items": ITEM_COUNT,
        "circle_pair_residue_requirements": 6 * 16,
        "matrix_audit": matrix_audit,
    }


def phase_solution_document(
    root: ParityRoot,
    phases: Sequence[Sequence[int]],
) -> dict:
    audit = validate_phase(root, phases)
    return {
        "format": "n58-v3-3d-phase-solution-v1",
        "family": "3D-HL=4C4",
        "parity_root_id": root.branch_id,
        "parity_table_index": root.table_index,
        "phases": [list(map(int, row)) for row in phases],
        "audit": audit,
    }


def load_phase_solution(
    path: Path | str,
    *,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
) -> tuple[ParityRoot, tuple[tuple[int, ...], ...]]:
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    if document.get("format") != "n58-v3-3d-phase-solution-v1":
        raise ValueError("not an N58 V3 3D phase solution")
    root = root_by_index(
        int(document["parity_table_index"]), tables_path, require_live=True
    )
    if document.get("parity_root_id") != root.branch_id:
        raise ValueError("phase solution parity-root id does not match its index")
    phases = tuple(tuple(map(int, row)) for row in document["phases"])
    validate_phase(root, phases)
    return root, phases


class C3DPhaseRootEncoder:
    """CNF for one canonical parity root and its complete phase choices."""

    def __init__(self, builder: CNFBuilder, root: ParityRoot) -> None:
        if not root.is_live:
            raise ValueError(f"{root.branch_id} is already theory-closed")
        self.builder = builder
        self.root = root
        self.namespace = ("sat58", "v3", "3D", root.branch_id, "phase")
        self.high_vars = {
            (circle, edge): builder.var(
                (self.namespace, "high", circle, edge), "phase_high_bit"
            )
            for circle in range(1, CIRCLE_COUNT)
            for edge in range(PAIR_COUNT)
        }
        self.products = ProductCache(builder, (self.namespace, "products"))
        self.coverage_clauses = 0

    def high(self, circle: int, edge: int) -> BoolTerm:
        if circle == 0:
            return False
        return self.high_vars[(circle, edge)]

    def phase_equals(self, circle: int, edge: int, residue: int) -> BoolTerm:
        residue %= 4
        if residue % 2 != self.root.parity(circle, edge):
            return False
        high = self.high(circle, edge)
        return high if residue // 2 else negate(high)

    def item_phase_equals(self, circle: int, item: int, residue: int) -> BoolTerm:
        edge, sign = item_edge(item), item_sign(item)
        return self.phase_equals(circle, edge, (residue - 2 * sign) % 4)

    def encode(self) -> None:
        for first in range(CIRCLE_COUNT):
            for second in range(first + 1, CIRCLE_COUNT):
                for left in range(4):
                    for right in range(4):
                        witnesses = [
                            self.products.product(
                                self.item_phase_equals(first, item, left),
                                self.item_phase_equals(second, item, right),
                            )
                            for item in range(ITEM_COUNT)
                        ]
                        self.coverage_clauses += int(
                            add_simplified_clause(self.builder, *witnesses)
                        )

    def mapping(self) -> dict:
        phase_bits = [
            {
                "circle": circle,
                "edge": edge,
                "parity": self.root.parity(circle, edge),
                "variable": variable,
            }
            for (circle, edge), variable in sorted(self.high_vars.items())
        ]
        return self.builder.variable_map(
            schema_version="sat58-v3-3d-phase-map-v1",
            encoding=ENCODING,
            family="3D",
            branch_id=self.root.branch_id,
            layer="PHASE",
            sat_semantics="frontend_witness",
            soundness=["EQUIV", "NEC"],
            parity_table_index=self.root.table_index,
            cut_plus_sets=[list(row) for row in self.root.cut_plus_sets],
            phase_high_bits=phase_bits,
            split_candidates=[
                {
                    "literal": row["variable"],
                    "kind": "phase_high_bit",
                    "semantic": f"phi[{row['circle']},{row['edge']}]//2",
                }
                for row in phase_bits
            ],
            next_layer="sat58.v3.c3d.block_cover",
        )

    def phases_from_assignment(
        self, values: Mapping[int, bool]
    ) -> tuple[tuple[int, ...], ...]:
        rows: list[tuple[int, ...]] = []
        for circle in range(CIRCLE_COUNT):
            row = []
            for edge in range(PAIR_COUNT):
                parity = self.root.parity(circle, edge)
                high = False if circle == 0 else bool(values[self.high_vars[(circle, edge)]])
                row.append(parity + 2 * int(high))
            rows.append(tuple(row))
        phases = tuple(rows)
        validate_phase(self.root, phases)
        return phases


def generate(
    *,
    root_index: int,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
    cnf_path: Path | str | None = None,
    map_path: Path | str | None = None,
    stats_path: Path | str | None = None,
) -> dict:
    root = root_by_index(root_index, tables_path, require_live=True)
    cnf = None if cnf_path is None else Path(cnf_path)
    builder: CNFBuilder = CountingCNFBuilder() if cnf is None else StreamingCNFBuilder(cnf)
    encoder = C3DPhaseRootEncoder(builder, root)
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
        "layer": "PHASE",
        "sat_semantics": "frontend_witness",
        "soundness": ["EQUIV", "NEC"],
        "parity_table_index": root.table_index,
        "phase_high_bits": len(encoder.high_vars),
        "circle_pair_residue_requirements": 6 * 16,
        "coverage_clauses": encoder.coverage_clauses,
        "cached_products": encoder.products.cached_products,
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


def decode_phase_model(
    *,
    model_path: Path | str,
    map_path: Path | str,
    output_path: Path | str | None = None,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
) -> dict:
    assignment = load_sat_solver_output(Path(model_path))
    mapping = json.loads(Path(map_path).read_text(encoding="utf-8"))
    if mapping.get("schema_version") != "sat58-v3-3d-phase-map-v1":
        raise ValueError("not an N58 V3 3D phase map")
    root = root_by_index(
        int(mapping["parity_table_index"]), tables_path, require_live=True
    )
    records = mapping["phase_high_bits"]
    variables = [int(record["variable"]) for record in records]
    assignment.require_assigned(variables, "phase high-bit")
    values = {
        variable: variable in assignment.positive_variables for variable in variables
    }
    phases = [[root.parity(circle, edge) for edge in range(PAIR_COUNT)] for circle in range(4)]
    for record in records:
        circle, edge, variable = (
            int(record["circle"]),
            int(record["edge"]),
            int(record["variable"]),
        )
        phases[circle][edge] += 2 * int(values[variable])
    document = phase_solution_document(root, phases)
    if output_path is not None:
        write_json(Path(output_path), document)
    return document


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-index", type=int, required=True)
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
                root_index=args.root_index,
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
