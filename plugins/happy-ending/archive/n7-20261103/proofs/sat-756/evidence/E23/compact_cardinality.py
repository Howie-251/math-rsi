"""Explicit compact cell export and independent SAT replay.

Generate with ``python -m state_charging.compact_cardinality generate``.
This module never launches a solver or publishes a cardinality theorem.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping

from lib.compact_cardinality_cnf import (
    ENCODING, MODES, STRICT, CompactBase, build_compact_base,
)
from lib.downset_state import (
    EXCEPTIONAL_KIND, classify_state, extract_downset_profile, ordinary_states,
)
from state_charging.cardinality_layers import (
    CardinalityCell, audit_profile_cardinality, canonical_dimacs_identity,
    normalize_cell, normalize_complete_assignment, parse_dimacs_sat_output,
)
from state_charging.corpus import audit_signotope_coloring
from state_charging.obligations import ExactCardinalityCNF, encode_at_most_exact, stable_sha256


EXPORT_SCHEMA = "compact_cardinality_export_v1"
AUDIT_SCHEMA = "compact_cardinality_sat_audit_v1"
SOURCE_FILES = (
    "lib/compact_cardinality_cnf.py", "lib/downset_state_cnf.py",
    "lib/downset_state.py", "lib/sat_tseitin.py",
    "state_charging/compact_cardinality.py", "state_charging/cardinality_layers.py",
    "state_charging/corpus.py", "state_charging/obligations.py",
)


@dataclass(frozen=True)
class CompactFormula:
    base: CompactBase
    exceptional_count: int
    components: tuple[ExactCardinalityCNF, ExactCardinalityCNF]

    @property
    def num_vars(self) -> int:
        return self.components[-1].num_vars

    @property
    def count_clauses(self) -> tuple[tuple[int, ...], ...]:
        return self.components[0].clauses + self.components[1].clauses

    @property
    def clauses(self) -> tuple[tuple[int, ...], ...]:
        return self.base.clauses + self.count_clauses

    def metadata(self, *, include_variables: bool = False) -> dict[str, Any]:
        count = {
            "predicate": "sum(exact_exceptional_endpoint_flags) = e",
            "e": self.exceptional_count,
            "derived_m": 25 + self.exceptional_count - self.base.order,
            "m_derivation": "state_injection_and_N=25+e-m",
            "components": [c.to_dict() for c in self.components],
        }
        if include_variables:
            count["variables"] = [
                {"var": v, "name": f"compact_count({name},{v - component.top_id})",
                 "role": "compact_count_auxiliary", "component": name}
                for name, component in zip(("at_most", "at_least"), self.components)
                for v in range(component.top_id + 1, component.num_vars + 1)
            ]
        return {
            "encoding": ENCODING,
            "base": self.base.metadata(include_variables=include_variables),
            "base_dimacs": canonical_dimacs_identity(self.base.num_vars, self.base.clauses),
            "dimacs": canonical_dimacs_identity(self.num_vars, self.clauses),
            "cardinality": count,
        }


def encode_exceptional_count(base: CompactBase, count: int) -> CompactFormula:
    """Count exact endpoint flags with two existing deterministic totalizers."""
    if not isinstance(base, CompactBase):
        raise TypeError("base must be a CompactBase")
    if type(count) is not int or not 0 <= count <= min(10, base.order):
        raise ValueError("exceptional count must be a plain integer in 0..min(10,N)")
    flags = tuple(base.exceptional_flags[v] for v in range(1, base.order + 1))
    upper = encode_at_most_exact(flags, count, top_id=base.num_vars)
    lower = encode_at_most_exact(tuple(-v for v in flags), base.order - count, top_id=upper.num_vars)
    return CompactFormula(base, count, (upper, lower))


@dataclass(frozen=True)
class CompactCell:
    cell: CardinalityCell
    formula: CompactFormula

    def metadata(self, *, include_variables: bool = False) -> dict[str, Any]:
        return {
            "schema": EXPORT_SCHEMA,
            "logical_cell": self.cell.to_dict(),
            **self.formula.metadata(include_variables=include_variables),
            "evidence_policy": {
                "sat": "complete_clause_check_and_independent_coloring_state_count_replay",
                "unsat": "fresh_bound_nonempty_proof_and_independent_checker_required",
                "production_accepted": False,
            },
        }


def build_compact_cell(
    raw_cell: CardinalityCell | Mapping[str, Any], *, mode: str = STRICT,
    bridges: bool = False,
) -> CompactCell:
    cell = normalize_cell(raw_cell)
    base = build_compact_base(cell.order, mode=mode, bridges=bridges)
    return CompactCell(cell, encode_exceptional_count(base, cell.e))


def _require_canonical(formula: CompactFormula) -> None:
    if not isinstance(formula, CompactFormula):
        raise TypeError("formula must be a CompactFormula")
    base = formula.base
    fresh = encode_exceptional_count(
        build_compact_base(base.order, mode=base.mode, bridges=base.bridges),
        formula.exceptional_count,
    )
    if formula != fresh:
        raise ValueError("compact formula/metadata differs from a fresh canonical build")


def audit_compact_assignment(
    formula: CompactFormula, model: Iterable[int], *,
    cell: CardinalityCell | Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Check all clauses, then recompute exact facts from triple colors.

    One-way outer markers are intentionally not interpreted as actual paths.
    A complete canonical rebuild rejects coherently altered literal metadata.
    """
    _require_canonical(formula)
    logical_cell = normalize_cell(cell) if cell is not None else None
    if logical_cell is not None and (
        logical_cell.order != formula.base.order or logical_cell.e != formula.exceptional_count
    ):
        raise ValueError("logical cell differs from the compact formula")
    assignment = normalize_complete_assignment(model, formula.num_vars)
    values = {abs(lit): lit > 0 for lit in assignment}
    for index, clause in enumerate(formula.clauses):
        if not any(values[abs(lit)] == (lit > 0) for lit in clause):
            raise ValueError(f"model falsifies compact clause {index}")
    base = formula.base
    colors = {
        tuple(v + 1 for v in triple): "red" if values[lit] else "blue"
        for triple, lit in base.triples.items()
    }
    signotope = audit_signotope_coloring(colors, order=base.order)
    if signotope.get("pass") is not True:
        raise ValueError("model coloring violates signotope packets")
    # This extractor raises on path-bound violations instead of clipping.
    profile = extract_downset_profile(colors, order=base.order)
    if base.mode == STRICT and profile["first_weak_gon_vertex"] is not None:
        raise ValueError("strict model contains a weak 7-gon")
    vertices = {row["vertex"]: row for row in profile["vertex_states"]}
    occupied = {tuple(row["rows"]) for row in vertices.values()}
    if len(occupied) != base.order or profile["state_injection"]["holds"] is not True:
        raise ValueError("model endpoint states are not injective")
    e = sum(classify_state(state) == EXCEPTIONAL_KIND for state in occupied)
    m = len(set(ordinary_states()) - occupied)
    if e != formula.exceptional_count or m != 25 + e - base.order:
        raise ValueError("independently recomputed e/m counts disagree with the formula")
    for vertex, lit in base.exceptional_flags.items():
        if values[lit] != (classify_state(vertices[vertex]["rows"]) == EXCEPTIONAL_KIND):
            raise ValueError(f"exceptional flag at {vertex} disagrees with the coloring")
    terminal = {tuple(row["terminal_pair"]): row for row in profile["terminal_profiles"]}
    for (family, length, u, v), lit in base.terminal_paths.items():
        if values[lit] != (terminal[u, v][family]["longest_length"] >= length):
            raise ValueError(f"exact terminal path {family,length,u,v} disagrees with the coloring")
    for (v, a, b), lit in base.cells.items():
        if values[lit] != (b <= vertices[v]["rows"][a - 1]):
            raise ValueError(f"exact cell {v,a,b} disagrees with the coloring")
    profile_audit = (
        audit_profile_cardinality(profile, logical_cell, formula_mode=base.mode)
        if logical_cell is not None else None
    )
    return {
        "schema": AUDIT_SCHEMA, "status": "AUDITED_SAT", "pass": True,
        "encoding": ENCODING, "mode": base.mode, "bridges": base.bridges,
        "logical_cell": logical_cell.to_dict() if logical_cell else None,
        "dimacs": canonical_dimacs_identity(formula.num_vars, formula.clauses),
        "complete_assignment": True, "clauses_checked": len(formula.clauses),
        "assignment_sha256": stable_sha256(list(assignment)),
        "coloring_sha256": profile["coloring_sha256"], "order": base.order,
        "e": e, "m": m, "state_injection": True,
        "first_weak_gon_vertex": profile["first_weak_gon_vertex"],
        "exact_terminal_predicates_checked": len(base.terminal_paths),
        "exact_exceptional_flags_checked": len(base.exceptional_flags),
        "exact_cells_checked": len(base.cells),
        "one_way_witnesses_used_as_semantic_facts": False,
        "signotope_audit": signotope, "profile_audit": profile_audit,
        "production_accepted": False,
    }


def _file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _runtime_binding() -> dict[str, Any]:
    root = Path(__file__).resolve().parents[1]
    return {
        "python": list(sys.version_info[:3]),
        "python_sat": importlib.metadata.version("python-sat"),
        "sources": {name: _file_hash(root / name) for name in SOURCE_FILES},
    }


def export_compact_cell(built: CompactCell, directory: str | Path) -> dict[str, Any]:
    """Create a fresh CNF and deterministic sidecar, without running a solver."""
    if not isinstance(built, CompactCell):
        raise TypeError("built must be a CompactCell")
    cell = normalize_cell(built.cell)
    if cell.order != built.formula.base.order or cell.e != built.formula.exceptional_count:
        raise ValueError("cell metadata differs from its formula")
    _require_canonical(built.formula)
    payload = {**built.metadata(include_variables=True), "runtime": _runtime_binding()}
    target = Path(directory)
    target.mkdir(parents=True, exist_ok=False)
    with (target / "formula.cnf").open("x", encoding="ascii", newline="\n") as handle:
        handle.write(f"p cnf {built.formula.num_vars} {len(built.formula.clauses)}\n")
        for clause in built.formula.clauses:
            handle.write((" ".join(map(str, clause)) + " 0\n") if clause else "0\n")
    if _file_hash(target / "formula.cnf") != payload["dimacs"]["sha256"]:
        raise ValueError("written compact CNF differs from its canonical DIMACS hash")
    with (target / "metadata.json").open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, sort_keys=True, indent=2)
        handle.write("\n")
    return payload


def replay_compact_export(directory: str | Path) -> CompactCell:
    """Rebuild all metadata and require exact file/source bindings."""
    root = Path(directory)
    for name in ("metadata.json", "formula.cnf"):
        if (root / name).is_symlink() or not (root / name).is_file():
            raise ValueError(f"compact export {name} must be a regular file")
    payload = json.loads((root / "metadata.json").read_text(encoding="utf-8"))
    if payload.get("schema") != EXPORT_SCHEMA:
        raise ValueError("not a compact cardinality export")
    built = build_compact_cell(
        payload["logical_cell"], mode=payload["base"]["mode"],
        bridges=payload["base"]["bridges"],
    )
    expected = {**built.metadata(include_variables=True), "runtime": _runtime_binding()}
    # JSON comparison distinguishes booleans from integers and rejects extras.
    if stable_sha256(payload) != stable_sha256(expected):
        raise ValueError("export metadata/source bindings do not fresh-replay")
    if _file_hash(root / "formula.cnf") != expected["dimacs"]["sha256"]:
        raise ValueError("export CNF does not fresh-replay")
    return built


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    generate = commands.add_parser("generate", help="export one compact A[r,e] cell")
    generate.add_argument("--r", type=int, required=True)
    generate.add_argument("--e", type=int, required=True)
    generate.add_argument("--mode", choices=MODES, default=STRICT)
    generate.add_argument("--bridges", action="store_true")
    generate.add_argument("--out", required=True, help="new output directory")
    verify = commands.add_parser("verify-export", help="fresh-rebuild the exported CNF and metadata")
    verify.add_argument("--directory", required=True)
    audit = commands.add_parser("audit-sat", help="independently audit a complete external SAT model")
    audit.add_argument("--directory", required=True)
    audit.add_argument("--solver-output", required=True)
    audit.add_argument("--out", required=True, help="new audit JSON path")
    args = parser.parse_args(argv)
    if args.command == "generate":
        built = build_compact_cell({"r": args.r, "e": args.e}, mode=args.mode, bridges=args.bridges)
        result = export_compact_cell(built, args.out)
        print(json.dumps({"schema": result["schema"], "cell": result["logical_cell"], "dimacs": result["dimacs"]}))
    else:
        built = replay_compact_export(args.directory)
        if args.command == "verify-export":
            print(json.dumps({"status": "FRESH_REPLAY_MATCH", "dimacs": built.formula.metadata()["dimacs"]}))
        else:
            model = parse_dimacs_sat_output(Path(args.solver_output).read_text(), built.formula.num_vars)
            result = audit_compact_assignment(built.formula, model, cell=built.cell)
            with Path(args.out).open("x", encoding="utf-8") as handle:
                json.dump(result, handle, sort_keys=True, indent=2)
                handle.write("\n")
            print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
