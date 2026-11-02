#!/usr/bin/env python3
"""Search-strengthened, certification-safe variant of the coarse-v3 encoder."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping

from sat59.branches.c1_coarse_v3 import (
    C1CoarseV3Encoder,
    generate as _base_generate,
)
from sat59.enc.and_gate import add_simplified_clause, negate
from sat59.enc.clean_imbalance_v3 import add_m0_clean_colour_imbalance


class C1CoarseV3SearchEncoder(C1CoarseV3Encoder):
    """Add two proved no-loss strengthenings used by the 55-core campaign."""

    def _encode_parent_and_d_degrees(self) -> None:
        super()._encode_parent_and_d_degrees()
        # Ordinary second-layer vertices are indistinguishable before D is
        # chosen.  Relabel them so their unique parent colours are monotone.
        ordinary = self.parent_spec.ordinary_vertices
        for left, right in zip(ordinary, ordinary[1:]):
            for high in range(1, 8):
                for low in range(high):
                    add_simplified_clause(
                        self.builder,
                        negate(self.R.r(high, left)),
                        negate(self.R.r(low, right)),
                    )

    def _encode_clean_cover(self) -> None:
        super()._encode_clean_cover()
        if self.m == 0:
            add_m0_clean_colour_imbalance(
                self.builder,
                ordinary_vertices=self.parent_spec.ordinary_vertices,
                clean_terms=self.clean_terms,
                parent_term=self.R.r,
                key=("c1v3", self.case_id, "clean_imbalance"),
            )

    def mapping(self) -> dict[str, object]:
        value = super().mapping()
        compiled = dict(value["compiled_constraints"])
        compiled["m0_clean_imbalance"] = self.m == 0
        compiled["ordinary_parent_colour_order"] = True
        value["compiled_constraints"] = compiled
        value["encoding"] = "sat59-c1-coarse-v3-search"
        return value


def _install_search_encoder() -> None:
    # ``generate`` resolves this module global in c1_coarse_v3 at call time.
    # Installing once keeps the stable build_case surface without duplicating
    # its streaming/error-handling implementation.
    import sat59.branches.c1_coarse_v3 as base

    base.C1CoarseV3Encoder = C1CoarseV3SearchEncoder


def build_case(
    case_path_or_record,
    cnf_path: Path | None = None,
    map_path: Path | None = None,
    *,
    stats_path: Path | None = None,
    cuts_path: Path | None = None,
    case_id: str | None = None,
) -> dict[str, object]:
    import sat59.branches.c1_coarse_v3 as base

    _install_search_encoder()
    return base.build_case(
        case_path_or_record,
        cnf_path,
        map_path,
        stats_path=stats_path,
        cuts_path=cuts_path,
        case_id=case_id,
    )


__all__ = ["C1CoarseV3SearchEncoder", "build_case"]

