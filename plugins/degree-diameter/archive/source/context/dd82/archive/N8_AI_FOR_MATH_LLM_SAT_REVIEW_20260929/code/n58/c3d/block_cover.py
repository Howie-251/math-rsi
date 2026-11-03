#!/usr/bin/env python3
"""Anonymous 24-item/18-block cover frontend for a fixed 3D phase.

The 18 right vertices are anonymous at this layer.  An allowed block is a
four-set of signed middle items that uses four different mate pairs and is a
transversal of residues 0,1,2,3 in every one of the four C4 coordinates.
The CNF chooses a multiset of such blocks.  A block cannot occur more than
three times because each of its signed items has total multiplicity three;
using three monotone unary count bits is therefore an exact compression of
the nominal count range 0..18.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from sat58.branches.v2_common import enforce_even_parity
from sat58.v3.c3d.audits import audit_block_matrices
from sat58.v3.c3d.phase import (
    ITEM_COUNT,
    item_edge,
    item_phase_word,
    load_phase_solution,
    phase_solution_document,
)
from sat58.v3.c3d.tables import DEFAULT_TABLES_PATH, ParityRoot, root_by_index
from sat59.enc import (
    CNFBuilder,
    CountingCNFBuilder,
    StreamingCNFBuilder,
    add_simplified_clause,
    enforce_exactly,
    negate,
    unary_thresholds,
    write_json,
)
from sat59.solver_output import load_sat_solver_output


BLOCK_SIZE = 4
RIGHT_SIZE = 18
ITEM_MULTIPLICITY = 3
MAX_BLOCK_MULTIPLICITY = ITEM_MULTIPLICITY
ENCODING = "sat58-v3-3d-anonymous-block-cover-v1"


def _enforce_equal_token_sums(builder: CNFBuilder, left, right, key) -> None:
    """Encode equality of two counts known to be at most three."""

    left_thresholds = unary_thresholds(builder, left, 3, (key, "left"))
    right_thresholds = unary_thresholds(builder, right, 3, (key, "right"))
    for level in range(1, 4):
        left_ge = left_thresholds.ge(level)
        right_ge = right_thresholds.ge(level)
        add_simplified_clause(builder, negate(left_ge), right_ge)
        add_simplified_clause(builder, left_ge, negate(right_ge))


def enumerate_allowed_blocks(
    phases: Sequence[Sequence[int]],
) -> tuple[tuple[int, ...], ...]:
    """Enumerate all coordinatewise transversal four-sets deterministically."""

    if len(phases) != 4 or any(len(row) != 12 for row in phases):
        raise ValueError("phase array must have shape 4 by 12")
    words = tuple(item_phase_word(phases, item) for item in range(ITEM_COUNT))
    result = []
    for block in itertools.combinations(range(ITEM_COUNT), BLOCK_SIZE):
        if len({item_edge(item) for item in block}) != BLOCK_SIZE:
            continue
        if all(
            {words[item][circle] for item in block} == {0, 1, 2, 3}
            for circle in range(4)
        ):
            result.append(block)
    return tuple(result)


def required_item_pairs(
    phases: Sequence[Sequence[int]],
) -> tuple[tuple[int, int], ...]:
    """Return non-mate M--M pairs with no common left neighbour."""

    words = tuple(item_phase_word(phases, item) for item in range(ITEM_COUNT))
    return tuple(
        (first, second)
        for first in range(ITEM_COUNT)
        for second in range(first + 1, ITEM_COUNT)
        if item_edge(first) != item_edge(second)
        and all(words[first][circle] != words[second][circle] for circle in range(4))
    )


def _normalize_counts(
    blocks: Sequence[Sequence[int]],
    counts: Mapping[int, int] | Sequence[int],
) -> tuple[int, ...]:
    if isinstance(counts, Mapping):
        values = tuple(int(counts.get(index, 0)) for index in range(len(blocks)))
        extra = set(map(int, counts)) - set(range(len(blocks)))
        if extra:
            raise ValueError(f"unknown block indices: {sorted(extra)}")
    else:
        values = tuple(map(int, counts))
        if len(values) != len(blocks):
            raise ValueError("block count vector has the wrong length")
    if any(not 0 <= value <= MAX_BLOCK_MULTIPLICITY for value in values):
        raise ValueError("each block multiplicity must lie in 0..3")
    return values


def validate_block_cover(
    root: ParityRoot,
    phases: Sequence[Sequence[int]],
    counts: Mapping[int, int] | Sequence[int],
) -> dict:
    """Check all anonymous block-cover equations without reading CNF auxiliaries."""

    phase_solution_document(root, phases)
    blocks = enumerate_allowed_blocks(phases)
    values = _normalize_counts(blocks, counts)
    total = sum(values)
    if total != RIGHT_SIZE:
        raise ValueError(f"expected 18 block occurrences, found {total}")

    item_counts = [
        sum(values[index] for index, block in enumerate(blocks) if item in block)
        for item in range(ITEM_COUNT)
    ]
    if item_counts != [ITEM_MULTIPLICITY] * ITEM_COUNT:
        raise ValueError(f"signed-item multiplicities are not all three: {item_counts}")

    required = required_item_pairs(phases)
    missing = [
        pair
        for pair in required
        if not any(
            values[index] > 0 and pair[0] in block and pair[1] in block
            for index, block in enumerate(blocks)
        )
    ]
    if missing:
        raise ValueError(f"block cover misses {len(missing)} required M-M pairs")

    support_overlaps = []
    signed_balance_pairs = 0
    block_sets = [set(block) for block in blocks]
    for first in range(12):
        for second in range(first + 1, 12):
            intersections = {
                (first_sign, second_sign): sum(
                    values[index]
                    for index, block in enumerate(block_sets)
                    if 2 * first + first_sign in block
                    and 2 * second + second_sign in block
                )
                for first_sign in (0, 1)
                for second_sign in (0, 1)
            }
            if intersections[(0, 0)] != intersections[(1, 1)]:
                raise ValueError(
                    f"signed balance n++=n-- fails for supports {first},{second}"
                )
            if intersections[(0, 1)] != intersections[(1, 0)]:
                raise ValueError(
                    f"signed balance n+-=n-+ fails for supports {first},{second}"
                )
            signed_balance_pairs += 2
            overlap = sum(
                values[index]
                for index, block in enumerate(blocks)
                if first in {item_edge(item) for item in block}
                and second in {item_edge(item) for item in block}
            )
            if overlap % 2:
                raise ValueError(
                    f"unsigned supports {first},{second} have odd overlap {overlap}"
                )
            support_overlaps.append(overlap)
    occurrences = tuple(
        block
        for index, block in enumerate(blocks)
        for _ in range(values[index])
    )
    matrix_audit = audit_block_matrices(phases, occurrences)
    return {
        "status": "VALID_ANONYMOUS_BLOCK_COVER",
        "parity_root_id": root.branch_id,
        "allowed_blocks": len(blocks),
        "selected_block_types": sum(value > 0 for value in values),
        "block_occurrences": total,
        "required_item_pairs": len(required),
        "even_support_pairs": len(support_overlaps),
        "signed_balance_equalities": signed_balance_pairs,
        "matrix_audit": matrix_audit,
    }


def block_cover_document(
    root: ParityRoot,
    phases: Sequence[Sequence[int]],
    counts: Mapping[int, int] | Sequence[int],
) -> dict:
    blocks = enumerate_allowed_blocks(phases)
    values = _normalize_counts(blocks, counts)
    audit = validate_block_cover(root, phases, values)
    return {
        "format": "n58-v3-3d-block-cover-solution-v1",
        "family": "3D-HL=4C4",
        "parity_root_id": root.branch_id,
        "parity_table_index": root.table_index,
        "phases": [list(map(int, row)) for row in phases],
        "allowed_block_count": len(blocks),
        "block_counts": [
            {"block_id": index, "items": list(block), "count": values[index]}
            for index, block in enumerate(blocks)
            if values[index]
        ],
        "audit": audit,
        "next_layer": "sat58.v3.c3d.hr_encoder",
    }


def load_block_cover_solution(
    path: Path | str,
    *,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
) -> tuple[ParityRoot, tuple[tuple[int, ...], ...], tuple[int, ...]]:
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    if document.get("format") != "n58-v3-3d-block-cover-solution-v1":
        raise ValueError("not an N58 V3 3D block-cover solution")
    root = root_by_index(
        int(document["parity_table_index"]), tables_path, require_live=True
    )
    if document.get("parity_root_id") != root.branch_id:
        raise ValueError("block-cover parity-root id does not match its index")
    phases = tuple(tuple(map(int, row)) for row in document["phases"])
    blocks = enumerate_allowed_blocks(phases)
    counts_by_id = {
        int(record["block_id"]): int(record["count"])
        for record in document.get("block_counts", ())
    }
    for record in document.get("block_counts", ()):
        block_id = int(record["block_id"])
        if tuple(map(int, record["items"])) != blocks[block_id]:
            raise ValueError(f"block {block_id} items do not match deterministic enumeration")
    values = _normalize_counts(blocks, counts_by_id)
    validate_block_cover(root, phases, values)
    return root, phases, values


class AnonymousBlockCoverEncoder:
    """Exact unary-multiplicity CNF for one fixed complete phase."""

    def __init__(
        self,
        builder: CNFBuilder,
        root: ParityRoot,
        phases: Sequence[Sequence[int]],
    ) -> None:
        phase_solution_document(root, phases)
        self.builder = builder
        self.root = root
        self.phases = tuple(tuple(map(int, row)) for row in phases)
        self.blocks = enumerate_allowed_blocks(self.phases)
        self.required_pairs = required_item_pairs(self.phases)
        self.namespace = ("sat58", "v3", "3D", root.branch_id, "block_cover")
        self.count_bits = {
            (block, level): builder.var(
                (self.namespace, "count_ge", block, level), "block_count_unary"
            )
            for block in range(len(self.blocks))
            for level in range(1, MAX_BLOCK_MULTIPLICITY + 1)
        }
        self.coverage_clauses = 0
        self.even_overlap_constraints = 0
        self.signed_balance_equalities = 0

    def count_ge(self, block: int, level: int) -> int:
        return self.count_bits[(block, level)]

    def block_tokens(self, block: int) -> tuple[int, ...]:
        return tuple(
            self.count_ge(block, level)
            for level in range(1, MAX_BLOCK_MULTIPLICITY + 1)
        )

    def encode(self) -> None:
        # Unary count semantics: c>=3 -> c>=2 -> c>=1.  Together with the
        # sums below, this is exactly one integer count in 0..3 per block.
        for block in range(len(self.blocks)):
            for level in range(2, MAX_BLOCK_MULTIPLICITY + 1):
                add_simplified_clause(
                    self.builder,
                    -self.count_ge(block, level),
                    self.count_ge(block, level - 1),
                )

        all_tokens = [
            token for block in range(len(self.blocks)) for token in self.block_tokens(block)
        ]
        enforce_exactly(
            self.builder,
            all_tokens,
            RIGHT_SIZE,
            (self.namespace, "block_occurrences"),
        )
        for item in range(ITEM_COUNT):
            tokens = [
                token
                for block_index, block in enumerate(self.blocks)
                if item in block
                for token in self.block_tokens(block_index)
            ]
            enforce_exactly(
                self.builder,
                tokens,
                ITEM_MULTIPLICITY,
                (self.namespace, "item_multiplicity", item),
            )

        for first, second in self.required_pairs:
            present = [
                self.count_ge(block_index, 1)
                for block_index, block in enumerate(self.blocks)
                if first in block and second in block
            ]
            self.coverage_clauses += int(
                add_simplified_clause(self.builder, *present)
            )

        block_supports = [
            {item_edge(item) for item in block} for block in self.blocks
        ]
        block_sets = [set(block) for block in self.blocks]
        for first in range(12):
            for second in range(first + 1, 12):
                signed_tokens = {
                    (first_sign, second_sign): [
                        token
                        for block_index, block in enumerate(block_sets)
                        if 2 * first + first_sign in block
                        and 2 * second + second_sign in block
                        for token in self.block_tokens(block_index)
                    ]
                    for first_sign in (0, 1)
                    for second_sign in (0, 1)
                }
                _enforce_equal_token_sums(
                    self.builder,
                    signed_tokens[(0, 0)],
                    signed_tokens[(1, 1)],
                    (self.namespace, "signed_balance_same", first, second),
                )
                _enforce_equal_token_sums(
                    self.builder,
                    signed_tokens[(0, 1)],
                    signed_tokens[(1, 0)],
                    (self.namespace, "signed_balance_opposite", first, second),
                )
                self.signed_balance_equalities += 2
                tokens = [
                    token
                    for block_index, support in enumerate(block_supports)
                    if first in support and second in support
                    for token in self.block_tokens(block_index)
                ]
                enforce_even_parity(
                    self.builder,
                    tokens,
                    (self.namespace, "even_unsigned_overlap", first, second),
                )
                self.even_overlap_constraints += 1

    def mapping(self) -> dict:
        count_records = [
            {
                "block_id": block,
                "items": list(self.blocks[block]),
                "count_ge_variables": list(self.block_tokens(block)),
            }
            for block in range(len(self.blocks))
        ]
        return self.builder.variable_map(
            schema_version="sat58-v3-3d-block-cover-map-v1",
            encoding=ENCODING,
            family="3D",
            branch_id=self.root.branch_id,
            layer="BLOCK",
            sat_semantics="frontend_witness",
            parameterization_soundness="EQUIV",
            constraint_soundness=["NEC", "REDUNDANT"],
            parity_table_index=self.root.table_index,
            phases=[list(row) for row in self.phases],
            allowed_blocks=count_records,
            count_encoding="three monotone c>=j bits; c<=3 follows from item multiplicity",
            split_candidates=[
                {
                    "literal": record["count_ge_variables"][0],
                    "kind": "block_present",
                    "semantic": f"count(block[{record['block_id']}])>=1",
                }
                for record in count_records
            ],
            next_layer="sat58.v3.c3d.hr_encoder",
        )


def generate(
    *,
    phase_path: Path | str,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
    cnf_path: Path | str | None = None,
    map_path: Path | str | None = None,
    stats_path: Path | str | None = None,
) -> dict:
    root, phases = load_phase_solution(phase_path, tables_path=tables_path)
    cnf = None if cnf_path is None else Path(cnf_path)
    builder: CNFBuilder = CountingCNFBuilder() if cnf is None else StreamingCNFBuilder(cnf)
    encoder = AnonymousBlockCoverEncoder(builder, root, phases)
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
        "layer": "BLOCK",
        "sat_semantics": "frontend_witness",
        "parameterization_soundness": "EQUIV",
        "constraint_soundness": ["NEC", "REDUNDANT"],
        "parity_table_index": root.table_index,
        "allowed_blocks": len(encoder.blocks),
        "block_count_bits": len(encoder.count_bits),
        "required_item_pairs": len(encoder.required_pairs),
        "required_pair_clauses": encoder.coverage_clauses,
        "even_overlap_constraints": encoder.even_overlap_constraints,
        "signed_balance_equalities": encoder.signed_balance_equalities,
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


def decode_block_cover_model(
    *,
    model_path: Path | str,
    map_path: Path | str,
    output_path: Path | str | None = None,
    tables_path: Path | str = DEFAULT_TABLES_PATH,
) -> dict:
    assignment = load_sat_solver_output(Path(model_path))
    mapping = json.loads(Path(map_path).read_text(encoding="utf-8"))
    if mapping.get("schema_version") != "sat58-v3-3d-block-cover-map-v1":
        raise ValueError("not an N58 V3 3D block-cover map")
    root = root_by_index(
        int(mapping["parity_table_index"]), tables_path, require_live=True
    )
    phases = tuple(tuple(map(int, row)) for row in mapping["phases"])
    records = mapping["allowed_blocks"]
    variables = [
        int(variable)
        for record in records
        for variable in record["count_ge_variables"]
    ]
    assignment.require_assigned(variables, "block-count")
    counts = [
        sum(
            int(int(variable) in assignment.positive_variables)
            for variable in record["count_ge_variables"]
        )
        for record in records
    ]
    document = block_cover_document(root, phases, counts)
    if output_path is not None:
        write_json(Path(output_path), document)
    return document


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", type=Path, required=True)
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
                phase_path=args.phase,
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
