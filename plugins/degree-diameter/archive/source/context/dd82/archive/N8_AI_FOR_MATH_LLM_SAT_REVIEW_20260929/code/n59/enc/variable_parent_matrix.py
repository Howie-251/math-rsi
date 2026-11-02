"""Exact variable parent matrix for the N59 ``m=0/m=1`` super-instances.

The fixed-``R`` encoder stores the parent set of every second-layer vertex in
the case record.  A v3 super-instance instead keeps the same rooted coordinate
system but makes the complete ``8 x 50`` matrix ``R`` Boolean.  This module is
deliberately independent of the graph induced on the second layer: it encodes
only parent-set sizes and the eight parent capacities.

No column or adjacency-row symmetry breaking is performed here.  In
particular, callers may use this exact parent layer in certification formulas
without depending on a canonical-labelling argument.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .and_gate import BoolTerm
from .cardinality import enforce_exactly
from .cnf import CNFBuilder


N59_FIRST_LAYER = tuple(range(1, 9))
N59_SECOND_LAYER = tuple(range(9, 59))


@dataclass(frozen=True)
class VariableParentSpec:
    """Audited rooted parent-layer data for one v3 defect partition."""

    partition_id: str
    m: int
    defects: tuple[int, ...]
    parent_capacities: tuple[int, ...]
    first_layer: tuple[int, ...] = N59_FIRST_LAYER
    second_layer: tuple[int, ...] = N59_SECOND_LAYER

    def __post_init__(self) -> None:
        if self.m not in (0, 1):
            raise ValueError("the v3 parent model only supports m=0 or m=1")
        if len(self.first_layer) != 8 or len(set(self.first_layer)) != 8:
            raise ValueError("the first layer must contain eight distinct vertices")
        if len(self.second_layer) != 50 or len(set(self.second_layer)) != 50:
            raise ValueError("the second layer must contain fifty distinct vertices")
        if set(self.first_layer) & set(self.second_layer):
            raise ValueError("the rooted layers must be disjoint")
        if len(self.parent_capacities) != 8:
            raise ValueError("there must be eight parent capacities")
        if any(value < 0 for value in self.parent_capacities):
            raise ValueError("parent capacities must be nonnegative")
        if not self.defects or any(value <= 0 for value in self.defects):
            raise ValueError("a v3 defect partition must have positive parts")
        if tuple(sorted(self.defects, reverse=True)) != self.defects:
            raise ValueError("defect parts must use the supplied descending order")
        if sum(self.defects) != 6 - 2 * self.m:
            raise ValueError("defect partition does not match 6-2m")
        if len(self.defects) > len(self.second_layer):
            raise ValueError("too many exceptional vertices")

        expected_capacities = (7,) * 8 if self.m == 0 else (6, 6) + (7,) * 6
        if self.parent_capacities != expected_capacities:
            raise ValueError(
                f"parent capacities {self.parent_capacities!r} do not match "
                f"the m={self.m} rooted type"
            )
        total_parent_incidence = len(self.second_layer) + sum(self.defects)
        if sum(self.parent_capacities) != total_parent_incidence:
            raise ValueError("parent capacities do not conserve incidences")

    @classmethod
    def from_partition_record(cls, record: Mapping[str, object]) -> "VariableParentSpec":
        """Construct and validate a spec record from the supplied v3 JSON."""

        return cls(
            partition_id=str(record["id"]),
            m=int(record["m"]),
            defects=tuple(map(int, record["defects"])),  # type: ignore[arg-type]
            parent_capacities=tuple(
                map(int, record["parent_capacities"])  # type: ignore[arg-type]
            ),
        )

    @property
    def exceptional_vertices(self) -> tuple[int, ...]:
        return self.second_layer[: len(self.defects)]

    @property
    def ordinary_vertices(self) -> tuple[int, ...]:
        return self.second_layer[len(self.defects) :]

    def parent_count(self, vertex: int) -> int:
        if vertex not in self.second_layer:
            raise ValueError(f"vertex {vertex} is outside the second layer")
        offset = self.second_layer.index(vertex)
        return self.defects[offset] + 1 if offset < len(self.defects) else 1

    def d_degree(self, vertex: int) -> int:
        """Return the exact target degree in ``D=A[X]``."""

        return 8 - self.parent_count(vertex)


class VariableParentMatrix:
    """Boolean ``R[p,x]`` variables with exact row and column cardinalities.

    Parent indices accepted by :meth:`r` are local indices ``0,...,7``.
    Second-layer vertices retain their global labels ``9,...,58``.
    """

    def __init__(self, builder: CNFBuilder, spec: VariableParentSpec, key) -> None:
        self.builder = builder
        self.spec = spec
        self.key = key
        self.variables: dict[tuple[int, int], int] = {
            (parent, vertex): builder.var(
                ("variable_parent_matrix", key, parent, vertex), "R_parent"
            )
            for vertex in spec.second_layer
            for parent in range(8)
        }
        self.constraint_clauses: dict[str, int] = {}
        self._encoded = False

    def r(self, parent: int, vertex: int) -> BoolTerm:
        if not 0 <= parent < 8:
            raise ValueError("parent index must lie in 0,...,7")
        try:
            return self.variables[(parent, vertex)]
        except KeyError as error:
            raise ValueError(f"vertex {vertex} is outside the second layer") from error

    def parent_terms(self, vertex: int) -> tuple[BoolTerm, ...]:
        return tuple(self.r(parent, vertex) for parent in range(8))

    def children_terms(self, parent: int) -> tuple[BoolTerm, ...]:
        return tuple(self.r(parent, vertex) for vertex in self.spec.second_layer)

    def encode(self) -> None:
        """Add exact parent-set sizes and exact first-layer capacities once."""

        if self._encoded:
            raise RuntimeError("variable parent matrix was already encoded")
        before = self.builder.clause_count
        for vertex in self.spec.second_layer:
            enforce_exactly(
                self.builder,
                self.parent_terms(vertex),
                self.spec.parent_count(vertex),
                ("variable_parent_row", self.key, vertex),
            )
        self.constraint_clauses["parent_set_cardinalities"] = (
            self.builder.clause_count - before
        )

        before = self.builder.clause_count
        for parent, capacity in enumerate(self.spec.parent_capacities):
            enforce_exactly(
                self.builder,
                self.children_terms(parent),
                capacity,
                ("variable_parent_capacity", self.key, parent),
            )
        self.constraint_clauses["parent_capacities"] = (
            self.builder.clause_count - before
        )
        self._encoded = True

    def edge_variable_records(self) -> list[dict[str, int | str]]:
        """Return graph-edge records compatible with the full model loader."""

        return [
            {
                "u": self.spec.first_layer[parent],
                "v": vertex,
                "var": variable,
                "kind": "R_parent",
            }
            for (parent, vertex), variable in sorted(self.variables.items())
        ]

    def selected_parent_sets(
        self, positive_variables: set[int]
    ) -> dict[int, tuple[int, ...]]:
        """Decode local parent sets from a complete Boolean assignment."""

        return {
            vertex: tuple(
                parent
                for parent in range(8)
                if self.variables[(parent, vertex)] in positive_variables
            )
            for vertex in self.spec.second_layer
        }

    def validate_selected_parent_sets(
        self, selected: Mapping[int, Sequence[int]]
    ) -> None:
        """Independent integer validation used by focused tests and verifiers."""

        if set(selected) != set(self.spec.second_layer):
            raise ValueError("assignment does not cover the complete second layer")
        capacities = [0] * 8
        for vertex in self.spec.second_layer:
            parents = tuple(map(int, selected[vertex]))
            if len(parents) != len(set(parents)) or any(
                not 0 <= parent < 8 for parent in parents
            ):
                raise ValueError(f"invalid parent set at vertex {vertex}")
            if len(parents) != self.spec.parent_count(vertex):
                raise ValueError(f"wrong parent-set size at vertex {vertex}")
            for parent in parents:
                capacities[parent] += 1
        if tuple(capacities) != self.spec.parent_capacities:
            raise ValueError(
                f"observed capacities {tuple(capacities)!r} differ from "
                f"{self.spec.parent_capacities!r}"
            )

