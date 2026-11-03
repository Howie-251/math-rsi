#!/usr/bin/env python3
"""Variable-parent coarse SAT encoder for the active N59 c1 m=0/m=1 front.

One formula represents a complete defect partition rather than one fixed
parent matrix.  The exact graph variables are the 8x50 parent incidence
matrix ``R`` and the 1,225 possible edges of ``D=A[X]``.  The formula keeps
all thirteen parent super-instances exhaustive; it deliberately uses no raw
prior blockers and no unaudited macro classification.

The encoded core contains exact degrees, every entry and row sum of
``B=A^2+A-7I-J``, exact triangle counts, the nonedge-repeat identity, the
branch B cap, K4 exclusion, equal-set intersection cuts, all parent-subset
and exception cuts, the strict root moment table, and the clean-cover
constraints.  Optional connectivity cuts are a sound lazy strengthening.
Without such cuts, an UNSAT result still proves the original branch UNSAT;
a SAT assignment must pass the independent full verifier.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, Mapping

from sat59.enc.and_gate import (
    BoolTerm,
    add_iff_and,
    add_simplified_clause,
    assert_term,
    negate,
)
from sat59.enc.cardinality import enforce_at_least, enforce_exactly, unary_thresholds
from sat59.enc.cnf import CNFBuilder, CountingCNFBuilder, StreamingCNFBuilder, write_json
from sat59.enc.connectivity_cuts import CutLedger, add_ledger_cuts
from sat59.enc.equal_set_intersection_cuts import add_equal_set_intersection_cuts
from sat59.enc.no_k4 import add_no_k4_clauses
from sat59.enc.parent_subset_cuts import (
    add_exception_internal_cut,
    add_parent_subset_cuts,
)
from sat59.enc.repeat_thresholds import (
    FixedDefectThresholds,
    enforce_adjacent_cap,
    nonedge_weight_tokens,
)
from sat59.enc.root_moment_budget import RootMomentEncoding, add_root_moment_budget
from sat59.enc.threshold import DefectThresholds, encode_b_entry, enforce_b_row_sum
from sat59.enc.triangle_counts import BoundedCount, add_iff_and3, encode_bounded_count
from sat59.enc.variable_parent_matrix import VariableParentMatrix, VariableParentSpec
from sat59.theory.c1_coarse_v3_specs import PARTITION_BY_ID_V3, CoarsePartitionV3


ORDER = 59
ROOT = 0
P = tuple(range(1, 9))
X = tuple(range(9, 59))
ALL = tuple(range(59))
Pair = tuple[int, int]
RepeatEntry = DefectThresholds | FixedDefectThresholds


def pair(u: int, v: int) -> Pair:
    if u == v:
        raise ValueError("a graph pair needs distinct endpoints")
    return (u, v) if u < v else (v, u)


def partition_record(partition: CoarsePartitionV3) -> dict[str, object]:
    value = asdict(partition)
    value["global_B_cap"] = value.pop("global_b_cap")
    value["D_triangle_lower_bound"] = value.pop("d_triangle_lower_bound")
    value["q2_domain"] = list(partition.q2_domain)
    value["z2_cap_by_q2"] = {
        str(q2): cap for q2, cap in partition.q2_z2_caps
    }
    return value


def normalize_case(value: Mapping[str, object]) -> tuple[dict[str, object], CoarsePartitionV3]:
    case = dict(value)
    partition_id = str(case.get("partition_id", case.get("id", "")))
    try:
        partition = PARTITION_BY_ID_V3[partition_id]
    except KeyError as error:
        raise ValueError(f"unknown coarse-v3 partition {partition_id!r}") from error
    q2 = case.get("exact_q2", case.get("q2"))
    if q2 is not None and int(q2) not in partition.q2_domain:
        raise ValueError(f"Q2={q2} is outside {partition_id}'s coarse domain")
    case.setdefault("case_id", partition_id if q2 is None else f"{partition_id}__q2_{int(q2):02d}")
    case["partition_id"] = partition_id
    case["exact_q2"] = None if q2 is None else int(q2)
    case["encoding"] = "sat59-c1-coarse-v3"
    case["branch_family"] = "m0_b4_absent" if partition.m == 0 else "m1_b4_absent"
    case["partition"] = partition_record(partition)
    return case, partition


def load_case(path: Path, case_id: str | None = None) -> dict[str, object]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("case JSON must contain an object")
    records = value.get("cases")
    if records is not None:
        if not isinstance(records, list):
            raise ValueError("case manifest has no cases list")
        selected = records if case_id is None and len(records) == 1 else [
            record for record in records if record.get("case_id") == case_id
        ]
        if len(selected) != 1:
            raise ValueError("a multi-case manifest requires one valid --case-id")
        value = dict(selected[0])
    elif case_id is not None and value.get("case_id") != case_id:
        raise ValueError(f"case {case_id!r} is not the supplied record")
    return normalize_case(value)[0]


def _iff_or(builder: CNFBuilder, terms: Iterable[BoolTerm], key, kind: str) -> BoolTerm:
    values = tuple(term for term in terms if term is not False)
    if any(term is True for term in values):
        return True
    unique = tuple(dict.fromkeys(int(term) for term in values))
    if not unique:
        return False
    if len(unique) == 1:
        return unique[0]
    out = builder.var(("or", key), kind)
    for term in unique:
        add_simplified_clause(builder, -term, out)
    add_simplified_clause(builder, -out, *unique)
    return out


class C1CoarseV3Encoder:
    """Exact variable-parent encoder for one partition or one Q2 slice."""

    def __init__(self, case: Mapping[str, object], builder: CNFBuilder) -> None:
        self.case, self.partition = normalize_case(case)
        self.builder = builder
        self.case_id = str(self.case["case_id"])
        self.m = self.partition.m
        self.global_b_cap = self.partition.global_b_cap
        self.h_edge_set = {(0, 1)} if self.m == 1 else set()
        self.h_neighbours = [set() for _ in range(8)]
        for u, v in self.h_edge_set:
            self.h_neighbours[u].add(v)
            self.h_neighbours[v].add(u)

        parent_record = {
            "id": self.partition.id,
            "m": self.m,
            "defects": list(self.partition.defects),
            "parent_capacities": list(self.partition.parent_capacities),
        }
        self.parent_spec = VariableParentSpec.from_partition_record(parent_record)
        self.R = VariableParentMatrix(builder, self.parent_spec, ("c1v3", self.case_id))
        self.d_vars: dict[Pair, int] = {
            pair(u, v): builder.var(("c1v3", self.case_id, "D", u, v), "D_edge")
            for u, v in itertools.combinations(X, 2)
        }
        self.fixed_edges = {pair(ROOT, p) for p in P}
        self.fixed_edges.update(pair(u + 1, v + 1) for u, v in self.h_edge_set)
        self.b_entries: dict[Pair, RepeatEntry] = {}
        self.support_terms: dict[Pair, BoolTerm] = {}
        self.nonedge_tokens: dict[Pair, tuple[BoolTerm, ...]] = {}
        self.triangle_terms: dict[int, tuple[BoolTerm, ...]] = {}
        self.triangle_counts: dict[int, BoundedCount] = {}
        self.d_triangle_terms: dict[tuple[int, int, int], BoolTerm] = {}
        self.clean_terms: dict[int, BoolTerm] = {}
        self.clean_iso_terms: dict[int, BoolTerm] = {}
        self.moment: RootMomentEncoding | None = None
        self.constraint_counts: dict[str, int] = {}
        self.cut_count = 0
        self.connectivity_cut_ledger = CutLedger(self.case_id).to_json()

    def d(self, u: int, v: int) -> BoolTerm:
        if u == v:
            return False
        if u not in X or v not in X:
            raise ValueError("D is defined only on the second layer")
        return self.d_vars[pair(u, v)]

    def a(self, u: int, v: int) -> BoolTerm:
        if u == v:
            return False
        uv = pair(u, v)
        if uv in self.d_vars:
            return self.d_vars[uv]
        if u == ROOT or v == ROOT:
            return uv in self.fixed_edges
        if u in P and v in P:
            return (u - 1, v - 1) in self.h_edge_set or (v - 1, u - 1) in self.h_edge_set
        if u in P and v in X:
            return self.R.r(u - 1, v)
        if v in P and u in X:
            return self.R.r(v - 1, u)
        return False

    def _fixed_b_entry(self, value: int) -> FixedDefectThresholds:
        if not 0 <= value <= self.global_b_cap:
            self.builder.add_clause()
        return FixedDefectThresholds(value, self.global_b_cap)

    def _encode_parent_and_d_degrees(self) -> None:
        self.R.encode()
        for x in X:
            enforce_exactly(
                self.builder,
                [self.d(x, y) for y in X if y != x],
                self.parent_spec.d_degree(x),
                ("c1v3", self.case_id, "D_degree", x),
            )

    def _encode_repeat_entries(self) -> None:
        # Root entries are determined solely by H and the declared defects.
        for p in P:
            self.b_entries[pair(ROOT, p)] = self._fixed_b_entry(
                len(self.h_neighbours[p - 1])
            )
        for offset, x in enumerate(X):
            defect = self.partition.defects[offset] if offset < len(self.partition.defects) else 0
            self.b_entries[pair(ROOT, x)] = self._fixed_b_entry(defect)

        # B_PP = H + H^2 + RR^T.  encode_b_entry consumes B+1 terms.
        for p_global, q_global in itertools.combinations(P, 2):
            p, q = p_global - 1, q_global - 1
            terms: list[BoolTerm] = [True]
            terms.extend([True] * int(pair(p, q) in self.h_edge_set))
            terms.extend([True] * len(self.h_neighbours[p] & self.h_neighbours[q]))
            for x in X:
                terms.append(
                    add_iff_and(
                        self.builder,
                        self.R.r(p, x),
                        self.R.r(q, x),
                        ("c1v3", self.case_id, "RR_PP", p, q, x),
                        kind="R_common_and",
                    )
                )
            self.b_entries[pair(p_global, q_global)] = encode_b_entry(
                self.builder,
                terms,
                ("c1v3", self.case_id, "B_PP", p_global, q_global),
                max_b=self.global_b_cap,
            )

        # B_PX = HR + RD + R - J.
        for p_global in P:
            p = p_global - 1
            for x in X:
                terms = [self.R.r(p, x)]
                terms.extend(self.R.r(q, x) for q in sorted(self.h_neighbours[p]))
                for y in X:
                    if y == x:
                        continue
                    terms.append(
                        add_iff_and(
                            self.builder,
                            self.R.r(p, y),
                            self.d(x, y),
                            ("c1v3", self.case_id, "RD", p, x, y),
                            kind="RD_common_and",
                        )
                    )
                self.b_entries[pair(p_global, x)] = encode_b_entry(
                    self.builder,
                    terms,
                    ("c1v3", self.case_id, "B_PX", p_global, x),
                    max_b=self.global_b_cap,
                )

        # B_XX = R^T R + D^2 + D - J.
        for x, y in itertools.combinations(X, 2):
            terms: list[BoolTerm] = [self.d(x, y)]
            for p in range(8):
                terms.append(
                    add_iff_and(
                        self.builder,
                        self.R.r(p, x),
                        self.R.r(p, y),
                        ("c1v3", self.case_id, "RR_XX", p, x, y),
                        kind="R_common_and",
                    )
                )
            for z in X:
                if z in (x, y):
                    continue
                terms.append(
                    add_iff_and(
                        self.builder,
                        self.d(x, z),
                        self.d(y, z),
                        ("c1v3", self.case_id, "D_common", x, y, z),
                        kind="D_common_and",
                    )
                )
            self.b_entries[pair(x, y)] = encode_b_entry(
                self.builder,
                terms,
                ("c1v3", self.case_id, "B_XX", x, y),
                max_b=self.global_b_cap,
            )

        if len(self.b_entries) != ORDER * (ORDER - 1) // 2:
            raise AssertionError("repeat encoding did not cover every pair")
        rows: dict[int, list[RepeatEntry]] = {vertex: [] for vertex in ALL}
        for uv, entry in self.b_entries.items():
            u, v = uv
            rows[u].append(entry)
            rows[v].append(entry)
            self.support_terms[uv] = entry.support
            adjacency = self.a(u, v)
            enforce_adjacent_cap(self.builder, entry, adjacency, 3)
            self.nonedge_tokens[uv] = nonedge_weight_tokens(
                self.builder,
                entry,
                adjacency,
                ("c1v3", self.case_id, u, v),
            )
        for vertex in ALL:
            enforce_b_row_sum(
                self.builder,
                rows[vertex],
                6,
                ("c1v3", self.case_id, "B_row", vertex),
            )

    def _encode_triangles(self) -> None:
        incidence: dict[int, list[BoolTerm]] = {vertex: [] for vertex in ALL}
        for u, v, w in itertools.combinations(ALL, 3):
            term = add_iff_and3(
                self.builder,
                self.a(u, v),
                self.a(u, w),
                self.a(v, w),
                ("c1v3", self.case_id, "triangle", u, v, w),
                kind="graph_triangle",
            )
            if term is False:
                continue
            for vertex in (u, v, w):
                incidence[vertex].append(term)
            if u in X:
                self.d_triangle_terms[(u, v, w)] = term
        for vertex in ALL:
            terms = tuple(incidence[vertex])
            self.triangle_terms[vertex] = terms
            self.triangle_counts[vertex] = encode_bounded_count(
                self.builder,
                terms,
                lower=self.m,
                upper=3,
                key=("c1v3", self.case_id, "triangles", vertex),
                kind="triangle_count",
            )

    def _encode_nonedge_repeat_budget(self) -> None:
        for vertex in ALL:
            tokens: list[BoolTerm] = []
            for other in ALL:
                if other != vertex:
                    tokens.extend(self.nonedge_tokens[pair(vertex, other)])
            triangle_tokens = [self.triangle_counts[vertex].ge(level) for level in range(1, 4)]
            tokens.extend(triangle_tokens)
            tokens.extend(triangle_tokens)
            enforce_exactly(
                self.builder,
                tokens,
                6,
                ("c1v3", self.case_id, "nonedge_repeat_plus_2t", vertex),
            )

    def _encode_v3_cuts(self) -> None:
        add_equal_set_intersection_cuts(
            self.builder, self.b_entries, ALL, m=self.m
        )
        add_parent_subset_cuts(
            self.builder,
            self.b_entries,
            P,
            key=("c1v3", self.case_id),
        )
        add_exception_internal_cut(
            self.builder,
            self.b_entries,
            self.parent_spec.exceptional_vertices,
            m=self.m,
            key=("c1v3", self.case_id),
            declared_cap=self.partition.exception_internal_b_weight_cap,
        )

    def _encode_moment(self) -> None:
        weighted: list[tuple[int, int]] = []
        if self.m == 1:
            weighted.extend(((P[0], 1), (P[1], 1)))
        weighted.extend(zip(self.parent_spec.exceptional_vertices, self.partition.defects))
        self.moment = add_root_moment_budget(
            self.builder,
            weighted_vertices=weighted,
            adjacency=self.a,
            b_entries=self.b_entries,
            q2_domain=self.partition.q2_domain,
            z2_cap_by_q2=self.partition.z2_cap_by_q2,
            key=("c1v3", self.case_id),
            exact_q2=self.case.get("exact_q2"),
        )

    def _encode_clean_cover(self) -> None:
        exceptional = self.parent_spec.exceptional_vertices
        ordinary = self.parent_spec.ordinary_vertices
        active_terms: list[BoolTerm] = []
        for x in ordinary:
            dirty = _iff_or(
                self.builder,
                (self.d(x, e) for e in exceptional),
                ("c1v3", self.case_id, "dirty", x),
                "dirty_exception",
            )
            clean = negate(dirty)
            self.clean_terms[x] = clean
            if self.m == 0:
                active = clean
            else:
                isolated_parent = _iff_or(
                    self.builder,
                    (self.R.r(parent, x) for parent in range(2, 8)),
                    ("c1v3", self.case_id, "isolated_parent", x),
                    "isolated_parent",
                )
                active = add_iff_and(
                    self.builder,
                    clean,
                    isolated_parent,
                    ("c1v3", self.case_id, "clean_iso", x),
                    kind="clean_iso",
                )
                self.clean_iso_terms[x] = active
            active_terms.append(active)

            # When active, count_q + R[q,x] = 1 for every parent colour q.
            for q in range(8):
                colour_edges = [
                    add_iff_and(
                        self.builder,
                        self.d(x, y),
                        self.R.r(q, y),
                        ("c1v3", self.case_id, "colour_edge", x, q, y),
                        kind="clean_colour_edge",
                    )
                    for y in ordinary
                    if y != x
                ]
                counts = unary_thresholds(
                    self.builder,
                    colour_edges,
                    2,
                    ("c1v3", self.case_id, "clean_colour_count", x, q),
                    kind="clean_colour_count",
                )
                inactive = negate(active)
                add_simplified_clause(
                    self.builder, inactive, counts.ge(1), self.R.r(q, x)
                )
                add_simplified_clause(self.builder, inactive, negate(counts.ge(2)))
                add_simplified_clause(
                    self.builder,
                    inactive,
                    negate(counts.ge(1)),
                    negate(self.R.r(q, x)),
                )

            if self.m == 1:
                incident_d_triangles = [
                    term for triple, term in self.d_triangle_terms.items() if x in triple
                ]
                add_simplified_clause(
                    self.builder, negate(active), *incident_d_triangles
                )

        enforce_at_least(
            self.builder,
            active_terms,
            self.partition.clean_lower_bound,
            ("c1v3", self.case_id, "clean_lower_bound"),
        )
        if self.m == 1:
            enforce_at_least(
                self.builder,
                self.d_triangle_terms.values(),
                self.partition.d_triangle_lower_bound,
                ("c1v3", self.case_id, "D_triangle_lower_bound"),
            )

    def add_connectivity_cuts(self, ledger: CutLedger) -> None:
        selectors = {uv: self.support_terms[uv] for uv in sorted(self.support_terms)}
        self.cut_count = add_ledger_cuts(
            self.builder,
            {"B": selectors},
            ledger,
            branch_id=self.case_id,
            vertices_by_scope={"B": ALL},
        )
        self.connectivity_cut_ledger = ledger.to_json()

    def _stage(self, name: str, action) -> None:
        before = self.builder.clause_count
        action()
        self.constraint_counts[name] = self.builder.clause_count - before

    def encode(self, cuts: CutLedger) -> None:
        self._stage("R_and_D_degrees", self._encode_parent_and_d_degrees)
        self._stage("repeat_entries_and_rows", self._encode_repeat_entries)
        self._stage("exact_triangles", self._encode_triangles)
        self._stage("nonedge_repeat_budget", self._encode_nonedge_repeat_budget)
        self._stage("intersection_and_subset_cuts", self._encode_v3_cuts)
        self._stage("root_moment_budget", self._encode_moment)
        self._stage("clean_cover", self._encode_clean_cover)
        self._stage("no_K4", lambda: add_no_k4_clauses(self.builder, ALL, self.a))
        self._stage("connectivity_cuts", lambda: self.add_connectivity_cuts(cuts))

    def mapping(self) -> dict[str, object]:
        edge_variables = self.R.edge_variable_records()
        edge_variables.extend(
            {"u": u, "v": v, "var": variable, "kind": "D_edge"}
            for (u, v), variable in sorted(self.d_vars.items())
        )
        return self.builder.variable_map(
            encoding="sat59-c1-coarse-v3",
            branch="c1",
            branch_family=self.case["branch_family"],
            case_id=self.case_id,
            partition_id=self.partition.id,
            exact_q2=self.case.get("exact_q2"),
            order=ORDER,
            root=ROOT,
            first_layer=list(P),
            second_layer=list(X),
            m=self.m,
            defects=list(self.partition.defects),
            exception_vertices=list(self.parent_spec.exceptional_vertices),
            ordinary_vertices=list(self.parent_spec.ordinary_vertices),
            parent_capacities=list(self.partition.parent_capacities),
            global_B_cap=self.global_b_cap,
            fixed_edges=[list(edge) for edge in sorted(self.fixed_edges)],
            edge_variables=edge_variables,
            support_variables=[
                {"u": u, "v": v, "term": term, "scope": "B"}
                for (u, v), term in sorted(self.support_terms.items())
            ],
            support_scopes={"B": list(ALL)},
            connectivity_branch_id=self.case_id,
            connectivity_mode="finite_cut_relaxation",
            connectivity_cuts=self.cut_count,
            connectivity_cut_ledger=self.connectivity_cut_ledger,
            case_record=self.case,
            compiled_constraints={
                "variable_parent_matrix": True,
                "exact_B_and_row_sums": True,
                "exact_triangles": True,
                "equal_set_intersection": True,
                "all_parent_subset_cuts": True,
                "exception_cut": True,
                "root_moment_table": True,
                "clean_cover": True,
                "m0_clean_imbalance": False,
                "macro_kernels": False,
                "raw_prior_blockers": False,
                "parent_symmetry_breaking": False,
            },
        )


def load_cuts(path: Path | None, case_id: str) -> CutLedger:
    if path is None:
        return CutLedger(case_id)
    return CutLedger.load(path, branch_id=case_id)


def generate(
    case: Mapping[str, object],
    *,
    cnf_path: Path | None = None,
    map_path: Path | None = None,
    stats_path: Path | None = None,
    cuts_path: Path | None = None,
) -> dict[str, object]:
    builder: CNFBuilder = CountingCNFBuilder() if cnf_path is None else StreamingCNFBuilder(cnf_path)
    encoder = C1CoarseV3Encoder(case, builder)
    try:
        encoder.encode(load_cuts(cuts_path, encoder.case_id))
        builder.finish()
    except BaseException:
        builder.abort()
        raise
    stats: dict[str, object] = {
        **builder.stats(),
        "encoding": "sat59-c1-coarse-v3",
        "case_id": encoder.case_id,
        "partition_id": encoder.partition.id,
        "exact_q2": encoder.case.get("exact_q2"),
        "m": encoder.m,
        "R_edge_variables": len(encoder.R.variables),
        "D_edge_variables": len(encoder.d_vars),
        "B_entries": len(encoder.b_entries),
        "constraint_clauses": encoder.constraint_counts,
        "connectivity_cuts": encoder.cut_count,
        "connectivity_complete": False,
        "certification_safe": True,
        "omitted_sound_strengthenings": [
            "m0 clean-colour imbalance",
            "macro kernels pending coverage audit",
            "parent symmetry breaking pending canonical-key audit",
        ],
    }
    if cnf_path is not None:
        stats.update(cnf_path=str(cnf_path), cnf_bytes=cnf_path.stat().st_size)
    if map_path is not None:
        write_json(map_path, encoder.mapping())
        stats.update(map_path=str(map_path), map_bytes=map_path.stat().st_size)
    if stats_path is not None:
        write_json(stats_path, stats)
    return stats


def build_case(
    case_path_or_record,
    cnf_path: Path | None = None,
    map_path: Path | None = None,
    *,
    stats_path: Path | None = None,
    cuts_path: Path | None = None,
    case_id: str | None = None,
) -> dict[str, object]:
    case = (
        dict(case_path_or_record)
        if isinstance(case_path_or_record, Mapping)
        else load_case(Path(case_path_or_record), case_id)
    )
    return generate(
        case,
        cnf_path=None if cnf_path is None else Path(cnf_path),
        map_path=None if map_path is None else Path(map_path),
        stats_path=None if stats_path is None else Path(stats_path),
        cuts_path=None if cuts_path is None else Path(cuts_path),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-json", required=True, type=Path)
    parser.add_argument("--case-id")
    parser.add_argument("--cnf", type=Path)
    parser.add_argument("--map", dest="map_path", type=Path)
    parser.add_argument("--stats", dest="stats_path", type=Path)
    parser.add_argument("--cuts", dest="cuts_path", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    stats = generate(
        load_case(args.case_json, args.case_id),
        cnf_path=args.cnf,
        map_path=args.map_path,
        stats_path=args.stats_path,
        cuts_path=args.cuts,
    )
    print(json.dumps(stats, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
