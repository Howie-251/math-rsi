#!/usr/bin/env python3
"""Generate the seven theory-reduced n=62 A+B SAT instances.

Only the 1378 edges inside Y={9,...,61} are primary graph variables.
Auxiliaries encode B=A^2+A-7I-J, B row sums, triangle membership, and the
branch-specific conditions from n62_root_templates_theory.json.
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import shutil
from pathlib import Path
from typing import Sequence

N = 62
ROOT = 0
X = tuple(range(1, 9))
Y = tuple(range(9, 62))
ENCODING_VERSION = "n62_ab_v1_20260824"


def pair(u: int, v: int) -> tuple[int, int]:
    if u == v:
        raise ValueError("a graph pair needs distinct vertices")
    return (u, v) if u < v else (v, u)


class CNFEmitter:
    """Allocate variables and stream a DIMACS body without retaining it."""

    def __init__(self, output: Path | None) -> None:
        self.output = output
        self.variable_count = 0
        self.clause_count = 0
        self.kind_counts: dict[str, int] = {}
        self.body_path: Path | None = None
        self.body = None
        if output is not None:
            output.parent.mkdir(parents=True, exist_ok=True)
            self.body_path = output.with_name(f".{output.name}.body-{os.getpid()}")
            self.body = self.body_path.open("w", encoding="ascii")

    def new_var(self, kind: str) -> int:
        self.variable_count += 1
        self.kind_counts[kind] = self.kind_counts.get(kind, 0) + 1
        return self.variable_count

    def add_clause(self, *literals: int) -> None:
        if any(literal == 0 for literal in literals):
            raise ValueError("zero may not occur inside a clause")
        self.clause_count += 1
        if self.body is not None:
            self.body.write(" ".join(map(str, literals)) + " 0\n")

    def finish(self) -> None:
        if self.output is None:
            return
        assert self.body is not None and self.body_path is not None
        self.body.close()
        with self.output.open("w", encoding="ascii") as target:
            target.write(f"p cnf {self.variable_count} {self.clause_count}\n")
            with self.body_path.open("r", encoding="ascii") as source:
                shutil.copyfileobj(source, target, length=1024 * 1024)
        self.body_path.unlink()
        self.body = None

    def abort(self) -> None:
        if self.body is not None:
            self.body.close()
            self.body = None
        if self.body_path is not None and self.body_path.exists():
            self.body_path.unlink()


def add_iff_and(emitter: CNFEmitter, out: int, a: int, b: int) -> None:
    emitter.add_clause(-out, a)
    emitter.add_clause(-out, b)
    emitter.add_clause(out, -a, -b)


def add_iff_xor(emitter: CNFEmitter, out: int, a: int, b: int) -> None:
    emitter.add_clause(a, b, -out)
    emitter.add_clause(-a, -b, -out)
    emitter.add_clause(a, -b, out)
    emitter.add_clause(-a, b, out)


def unary_thresholds(
    emitter: CNFEmitter,
    inputs: Sequence[int],
    maximum: int,
    kind: str,
) -> tuple[int | None, ...]:
    """Return exact unary thresholds ``sum(inputs) >= 1,...,maximum``.

    The recurrence is encoded in both directions. Repeated input literals are
    valid and let a B=2 selector contribute weight two.
    """
    if maximum < 0:
        raise ValueError("negative unary threshold maximum")
    if maximum == 0:
        return ()
    previous: list[int] = []
    for input_literal in inputs:
        current: list[int] = []
        upto = min(maximum, len(previous) + 1)
        for index in range(upto):
            threshold = index + 1
            out = emitter.new_var(kind)
            current.append(out)
            previous_same = previous[index] if index < len(previous) else None
            if threshold == 1:
                if previous_same is None:
                    emitter.add_clause(-out, input_literal)
                    emitter.add_clause(out, -input_literal)
                else:
                    emitter.add_clause(-previous_same, out)
                    emitter.add_clause(-input_literal, out)
                    emitter.add_clause(-out, previous_same, input_literal)
                continue
            previous_lower = previous[index - 1]
            if previous_same is None:
                emitter.add_clause(-out, input_literal)
                emitter.add_clause(-out, previous_lower)
                emitter.add_clause(out, -input_literal, -previous_lower)
            else:
                emitter.add_clause(-previous_same, out)
                emitter.add_clause(-input_literal, -previous_lower, out)
                emitter.add_clause(-out, previous_same, input_literal)
                emitter.add_clause(-out, previous_same, previous_lower)
        previous = current
    return tuple(
        previous[index] if index < len(previous) else None
        for index in range(maximum)
    )


def forbid_condition(emitter: CNFEmitter, condition: Sequence[int]) -> None:
    emitter.add_clause(*(-literal for literal in condition))


def enforce_exact_under_condition(
    emitter: CNFEmitter,
    condition: Sequence[int],
    thresholds: Sequence[int | None],
    target: int,
    input_count: int,
) -> None:
    """Encode ``AND(condition) -> count == target``."""
    if target < 0 or target > input_count:
        forbid_condition(emitter, condition)
        return
    prefix = [-literal for literal in condition]
    for index, threshold_var in enumerate(thresholds, start=1):
        desired = index <= target
        if threshold_var is None:
            if desired:
                forbid_condition(emitter, condition)
            continue
        emitter.add_clause(*prefix, threshold_var if desired else -threshold_var)


def enforce_exact(
    emitter: CNFEmitter,
    inputs: Sequence[int],
    target: int,
    kind: str,
) -> None:
    if target < 0 or target > len(inputs):
        emitter.add_clause()
        return
    maximum = min(len(inputs), target + 1)
    thresholds = unary_thresholds(emitter, inputs, maximum, kind)
    if target == 0:
        if thresholds:
            assert thresholds[0] is not None
            emitter.add_clause(-thresholds[0])
        return
    target_threshold = thresholds[target - 1]
    assert target_threshold is not None
    emitter.add_clause(target_threshold)
    if target < len(inputs):
        next_threshold = thresholds[target]
        assert next_threshold is not None
        emitter.add_clause(-next_threshold)


class ABEncoder:
    def __init__(self, template: dict, emitter: CNFEmitter) -> None:
        self.template = template
        self.id = str(template["id"])
        self.emitter = emitter
        self.simple_B = template["global_B_mode"] == "simple_0/1"
        if template["global_B_mode"] not in {"simple_0/1", "0/1/2"}:
            raise ValueError(f"unknown B mode in {self.id}")
        self.H = {pair(*edge) for edge in template["H_edges"]}
        self.parents = {
            int(vertex): frozenset(values)
            for vertex, values in template["parent_map"].items()
        }
        self.classes = {
            int(label): tuple(vertices)
            for label, vertices in template["singleton_classes"].items()
        }
        if set(self.parents) != set(Y):
            raise ValueError(f"{self.id}: parent map does not cover Y")

        self.edge_vars: dict[tuple[int, int], int] = {}
        self.b1_vars: dict[tuple[int, int], int] = {}
        self.b2_vars: dict[tuple[int, int], int] = {}
        self.tau_vars: dict[int, int] = {}
        self.unit_values: dict[int, bool] = {}
        self.unit_reasons: dict[int, str] = {}
        self.fixed_B_values: dict[tuple[int, int], int] = {}
        self.dynamic_pairs = tuple(
            (u, v)
            for u in range(1, N)
            for v in range(u + 1, N)
            if not (u in X and v in X)
        )
        for u, v in itertools.combinations(Y, 2):
            self.edge_vars[(u, v)] = emitter.new_var("A_Y_edge")
        if len(self.edge_vars) != 1378:
            raise AssertionError("wrong number of primary Y-Y edge variables")
        for uv in self.dynamic_pairs:
            self.b1_vars[uv] = emitter.new_var("B1_selector")
            if not self.simple_B:
                self.b2_vars[uv] = emitter.new_var("B2_selector")
        for vertex in range(N):
            self.tau_vars[vertex] = emitter.new_var("triangle_member")
        self._compute_fixed_B_values()
        self._static_audit()

    def fixed_A(self, u: int, v: int) -> int | None:
        u, v = pair(u, v)
        if u in Y and v in Y:
            return None
        if u == ROOT:
            return int(v in X)
        if u in X and v in X:
            return int((u, v) in self.H)
        if u in X and v in Y:
            return int(u in self.parents[v])
        raise AssertionError((u, v))

    def edge_var(self, u: int, v: int) -> int:
        uv = pair(u, v)
        if uv not in self.edge_vars:
            raise ValueError(f"{uv} is not a dynamic Y-Y edge")
        return self.edge_vars[uv]

    def _set_unit(self, variable: int, value: bool, reason: str) -> None:
        previous = self.unit_values.get(variable)
        if previous is not None and previous != value:
            raise ValueError(
                f"{self.id}: conflicting units for variable {variable}: "
                f"{self.unit_reasons[variable]} versus {reason}"
            )
        if previous is None:
            self.unit_values[variable] = value
            self.unit_reasons[variable] = reason
            self.emitter.add_clause(variable if value else -variable)

    def _constant_common_count(self, u: int, v: int) -> int:
        total = 0
        for k in range(N):
            if k in (u, v):
                continue
            left = self.fixed_A(u, k)
            right = self.fixed_A(v, k)
            if left == 0 or right == 0:
                continue
            if left is None or right is None:
                raise ValueError(f"{self.id}: pair {(u, v)} is not fully fixed")
            total += left * right
        return total

    def _compute_fixed_B_values(self) -> None:
        for v in range(1, N):
            a = self.fixed_A(ROOT, v)
            assert a is not None
            self.fixed_B_values[(ROOT, v)] = (
                self._constant_common_count(ROOT, v) + a - 1
            )
        for u, v in itertools.combinations(X, 2):
            a = self.fixed_A(u, v)
            assert a is not None
            self.fixed_B_values[(u, v)] = (
                self._constant_common_count(u, v) + a - 1
            )

    def _static_audit(self) -> None:
        if self.template["root"] != ROOT:
            raise ValueError(f"{self.id}: wrong root")
        if tuple(self.template["root_neighbors"]) != X:
            raise ValueError(f"{self.id}: wrong root-neighbor labels")
        if tuple(self.template["Y_vertices"]) != Y:
            raise ValueError(f"{self.id}: wrong Y labels")
        for x in X:
            fixed_degree = 1
            fixed_degree += sum(
                pair(x, other) in self.H for other in X if other != x
            )
            fixed_degree += sum(x in self.parents[y] for y in Y)
            if fixed_degree != 8:
                raise ValueError(
                    f"{self.id}: fixed degree of X vertex {x} is {fixed_degree}"
                )
        root_weight = sum(
            self.fixed_B_values[(ROOT, v)] for v in range(1, N)
        )
        if root_weight != 3:
            raise ValueError(f"{self.id}: root B row has weight {root_weight}")
        maximum = 1 if self.simple_B else 2
        if any(
            value < 0 or value > maximum
            for value in self.fixed_B_values.values()
        ):
            raise ValueError(f"{self.id}: fixed B value outside branch mode")
        for u, v, expected in self.template["fixed_B"]:
            uv = pair(u, v)
            if uv in self.fixed_B_values:
                if self.fixed_B_values[uv] != expected:
                    raise ValueError(
                        f"{self.id}: fixed B mismatch at {uv}: "
                        f"{self.fixed_B_values[uv]} != {expected}"
                    )
        edge_units = {
            pair(*edge): True for edge in self.template["fixed_extra_edges"]
        }
        for edge in self.template["fixed_extra_nonedges"]:
            uv = pair(*edge)
            if edge_units.get(uv) is True:
                raise ValueError(f"{self.id}: fixed edge/nonedge conflict at {uv}")

    def _fixed_f(self, u: int, v: int) -> int:
        """Common neighbors of u,v in {0,...,8}, all template-fixed."""
        return sum(
            int(self.fixed_A(u, k) == 1 and self.fixed_A(v, k) == 1)
            for k in range(0, 9)
            if k not in (u, v)
        )

    def _encode_template_units(self) -> None:
        for u, v in self.template["fixed_extra_edges"]:
            self._set_unit(self.edge_var(u, v), True, "fixed_extra_edge")
        for u, v in self.template["fixed_extra_nonedges"]:
            self._set_unit(self.edge_var(u, v), False, "fixed_extra_nonedge")
        for u, v, value in self.template["fixed_B"]:
            uv = pair(u, v)
            if uv in self.fixed_B_values:
                continue
            b1 = self.b1_vars[uv]
            b2 = self.b2_vars.get(uv)
            self._set_unit(b1, value == 1, "template_fixed_B")
            if b2 is not None:
                self._set_unit(b2, value == 2, "template_fixed_B")
            elif value == 2:
                raise ValueError(f"{self.id}: B=2 in simple-B template")
        for vertex_text, value in self.template[
            "fixed_triangle_membership"
        ].items():
            vertex = int(vertex_text)
            self._set_unit(
                self.tau_vars[vertex],
                bool(value),
                "fixed_triangle_membership",
            )
        local = self.template.get("double_local")
        if local is not None:
            w = int(local["w"])
            S = set(map(int, local["S"]))
            if local["forbid_w_neighbors_with_parent_intersecting_S"]:
                for y in Y:
                    if y != w and self.parents[y] & S:
                        self._set_unit(
                            self.edge_var(w, y),
                            False,
                            "w_parent_intersects_S",
                        )

    def _encode_B_selectors(self) -> None:
        for uv in self.dynamic_pairs:
            b1 = self.b1_vars[uv]
            b2 = self.b2_vars.get(uv)
            if b2 is None:
                continue
            self.emitter.add_clause(-b1, -b2)
            fixed_a = self.fixed_A(*uv)
            if fixed_a == 1:
                self.emitter.add_clause(-b2)
            elif fixed_a is None:
                # An adjacent pair cannot have B=2: that would put each
                # endpoint in two triangles.
                self.emitter.add_clause(-self.edge_var(*uv), -b2)

    def _encode_degrees(self) -> None:
        for y in Y:
            inputs = [self.edge_var(y, z) for z in Y if z != y]
            target = int(
                self.template["residual_degree_inside_Y"][str(y)]
            )
            enforce_exact(
                self.emitter, inputs, target, "A_degree_counter"
            )

    def _q_inputs(self, u: int, v: int) -> list[int]:
        if u in X and v in Y:
            return [
                self.edge_var(v, z)
                for z in Y
                if z != v and u in self.parents[z]
            ]
        if u in Y and v in Y:
            result = []
            for k in Y:
                if k in (u, v):
                    continue
                conjunction = self.emitter.new_var("common_Y_and")
                add_iff_and(
                    self.emitter,
                    conjunction,
                    self.edge_var(u, k),
                    self.edge_var(v, k),
                )
                result.append(conjunction)
            return result
        raise AssertionError((u, v))

    def _B_states(
        self, uv: tuple[int, int]
    ) -> list[tuple[int, list[int]]]:
        b1 = self.b1_vars[uv]
        if self.simple_B:
            return [(0, [-b1]), (1, [b1])]
        b2 = self.b2_vars[uv]
        return [(0, [-b1, -b2]), (1, [b1]), (2, [b2])]

    def _encode_core_pair_equations(self) -> None:
        for u, v in self.dynamic_pairs:
            uv = (u, v)
            q_inputs = self._q_inputs(u, v)
            thresholds = unary_thresholds(
                self.emitter,
                q_inputs,
                min(4, len(q_inputs)),
                "common_Y_threshold",
            )
            if len(q_inputs) >= 4:
                fourth = thresholds[3]
                assert fourth is not None
                self.emitter.add_clause(-fourth)
            fixed_f = self._fixed_f(u, v)
            fixed_a = self.fixed_A(u, v)
            if fixed_a is None:
                edge = self.edge_var(u, v)
                a_states = [(0, [-edge]), (1, [edge])]
            else:
                a_states = [(fixed_a, [])]
            for b_value, b_condition in self._B_states(uv):
                for a_value, a_condition in a_states:
                    target = 1 + b_value - a_value - fixed_f
                    enforce_exact_under_condition(
                        self.emitter,
                        b_condition + a_condition,
                        thresholds,
                        target,
                        len(q_inputs),
                    )

    def _encode_B_row_sums(self) -> None:
        for u in range(N):
            fixed_weight = 0
            tokens: list[int] = []
            for v in range(N):
                if u == v:
                    continue
                uv = pair(u, v)
                if uv in self.fixed_B_values:
                    fixed_weight += self.fixed_B_values[uv]
                    continue
                tokens.append(self.b1_vars[uv])
                if uv in self.b2_vars:
                    tokens.extend([self.b2_vars[uv], self.b2_vars[uv]])
            enforce_exact(
                self.emitter,
                tokens,
                3 - fixed_weight,
                "B_row_counter",
            )

    def _triangle_contribution(
        self, u: int, v: int
    ) -> tuple[int, int | None]:
        """Return a fixed o contribution and an optional o literal."""
        uv = pair(u, v)
        if uv in self.fixed_B_values:
            a = self.fixed_A(*uv)
            assert a is not None
            return int(a == 1 and self.fixed_B_values[uv] == 1), None
        b1 = self.b1_vars[uv]
        a = self.fixed_A(*uv)
        if a == 0:
            return 0, None
        if a == 1:
            return 0, b1
        edge = self.edge_var(*uv)
        out = self.emitter.new_var("triangle_edge_and")
        add_iff_and(self.emitter, out, edge, b1)
        return 0, out

    def _encode_triangle_membership(self) -> None:
        fixed_by_vertex = [0] * N
        inputs_by_vertex: list[list[int]] = [[] for _ in range(N)]
        for u in range(N):
            for v in range(u + 1, N):
                fixed, literal = self._triangle_contribution(u, v)
                fixed_by_vertex[u] += fixed
                fixed_by_vertex[v] += fixed
                if literal is not None:
                    inputs_by_vertex[u].append(literal)
                    inputs_by_vertex[v].append(literal)
        for u in range(N):
            inputs = inputs_by_vertex[u]
            thresholds = unary_thresholds(
                self.emitter,
                inputs,
                min(3, len(inputs)),
                "triangle_row_counter",
            )
            tau = self.tau_vars[u]
            enforce_exact_under_condition(
                self.emitter,
                [-tau],
                thresholds,
                -fixed_by_vertex[u],
                len(inputs),
            )
            enforce_exact_under_condition(
                self.emitter,
                [tau],
                thresholds,
                2 - fixed_by_vertex[u],
                len(inputs),
            )
        if self.template.get("triangle_membership_xor") is not None:
            expected = int(self.template["triangle_membership_xor"])
            values = [self.tau_vars[u] for u in range(N)]
            accumulator = values[0]
            for value in values[1:]:
                out = self.emitter.new_var("triangle_parity_xor")
                add_iff_xor(self.emitter, out, accumulator, value)
                accumulator = out
            self.emitter.add_clause(accumulator if expected else -accumulator)

    def _encode_double_local_counts(self) -> None:
        local = self.template.get("double_local")
        if local is None:
            return
        w = int(local["w"])
        counts = {
            int(label): int(value)
            for label, value in local[
                "w_neighbors_in_singleton_classes"
            ].items()
        }
        for label, target in sorted(counts.items()):
            inputs = [self.edge_var(w, y) for y in self.classes[label]]
            enforce_exact(
                self.emitter,
                inputs,
                target,
                "double_local_class_counter",
            )

    def encode(self) -> None:
        self._encode_template_units()
        self._encode_B_selectors()
        self._encode_degrees()
        self._encode_core_pair_equations()
        self._encode_B_row_sums()
        self._encode_triangle_membership()
        self._encode_double_local_counts()

    def mapping(self) -> dict:
        return {
            "schema": "n62-ab-variable-map-v1",
            "encoding_version": ENCODING_VERSION,
            "template_id": self.id,
            "edge_variables": [
                [u, v, variable]
                for (u, v), variable in sorted(self.edge_vars.items())
            ],
            "b1_variables": [
                [u, v, variable]
                for (u, v), variable in sorted(self.b1_vars.items())
            ],
            "b2_variables": [
                [u, v, variable]
                for (u, v), variable in sorted(self.b2_vars.items())
            ],
            "tau_variables": [
                [vertex, variable]
                for vertex, variable in sorted(self.tau_vars.items())
            ],
            "unit_assignments": [
                [variable, int(value), self.unit_reasons[variable]]
                for variable, value in sorted(self.unit_values.items())
            ],
        }

    def stats(self) -> dict:
        return {
            "encoding_version": ENCODING_VERSION,
            "template_id": self.id,
            "branch": self.template["branch"],
            "global_B_mode": self.template["global_B_mode"],
            "primary_edge_variables": len(self.edge_vars),
            "dynamic_B_pairs": len(self.dynamic_pairs),
            "variables": self.emitter.variable_count,
            "clauses": self.emitter.clause_count,
            "variable_kinds": dict(sorted(self.emitter.kind_counts.items())),
            "fixed_unit_variables": len(self.unit_values),
        }


def load_manifest(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != "n62-rooted-sat-manifest-v1":
        raise ValueError("unexpected n=62 root-template manifest schema")
    if payload.get("n") != N or payload.get("recommended_instances") != 7:
        raise ValueError("manifest is not the seven-instance n=62 handoff")
    ids = [template["id"] for template in payload["templates"]]
    if len(ids) != 7 or len(set(ids)) != 7:
        raise ValueError("manifest must contain seven unique templates")
    return payload


def clause_satisfied(
    clause: Sequence[int], assignment: dict[int, bool]
) -> bool:
    return any(
        assignment[abs(literal)] == (literal > 0) for literal in clause
    )


class MemoryEmitter(CNFEmitter):
    def __init__(self) -> None:
        super().__init__(None)
        self.clauses: list[tuple[int, ...]] = []

    def add_clause(self, *literals: int) -> None:
        super().add_clause(*literals)
        self.clauses.append(tuple(literals))


def audit_unary_threshold_encoder() -> dict:
    """Exhaustively check the primitive counter on 0--4 inputs."""
    checked_main_assignments = 0
    for input_count in range(5):
        emitter = MemoryEmitter()
        inputs = [emitter.new_var("input") for _ in range(input_count)]
        thresholds = unary_thresholds(
            emitter, inputs, 4, "audit_threshold"
        )
        auxiliary = [
            variable
            for variable in range(1, emitter.variable_count + 1)
            if variable not in inputs
        ]
        for main_bits in itertools.product((False, True), repeat=input_count):
            checked_main_assignments += 1
            expected = tuple(
                sum(main_bits) >= level for level in range(1, 5)
            )
            observed: set[tuple[bool, ...]] = set()
            for aux_bits in itertools.product(
                (False, True), repeat=len(auxiliary)
            ):
                assignment = dict(zip(inputs, main_bits))
                assignment.update(zip(auxiliary, aux_bits))
                if all(
                    clause_satisfied(clause, assignment)
                    for clause in emitter.clauses
                ):
                    observed.add(
                        tuple(
                            False
                            if variable is None
                            else assignment[variable]
                            for variable in thresholds
                        )
                    )
            if observed != {expected}:
                raise AssertionError(
                    (input_count, main_bits, expected, observed)
                )
    emitter = MemoryEmitter()
    repeated = emitter.new_var("input")
    thresholds = unary_thresholds(
        emitter, [repeated, repeated], 2, "audit_weighted_threshold"
    )
    auxiliary = list(range(repeated + 1, emitter.variable_count + 1))
    for value in (False, True):
        observed = set()
        for bits in itertools.product((False, True), repeat=len(auxiliary)):
            assignment = {repeated: value}
            assignment.update(zip(auxiliary, bits))
            if all(
                clause_satisfied(clause, assignment)
                for clause in emitter.clauses
            ):
                observed.add(tuple(assignment[var] for var in thresholds))
        expected = (value, value)
        if observed != {expected}:
            raise AssertionError(("weighted", value, expected, observed))
    return {
        "status": "passed",
        "input_sizes": [0, 1, 2, 3, 4],
        "main_assignments_checked": checked_main_assignments,
        "repeated_literal_weight_two_checked": True,
    }


def generate_case(
    template: dict,
    output_dir: Path,
    write_cnf: bool,
) -> dict:
    case_id = template["id"]
    cnf_path = (
        output_dir / "cnf" / f"{case_id}.cnf" if write_cnf else None
    )
    emitter = CNFEmitter(cnf_path)
    try:
        encoder = ABEncoder(template, emitter)
        encoder.encode()
        emitter.finish()
    except BaseException:
        emitter.abort()
        raise
    output_dir.mkdir(parents=True, exist_ok=True)
    map_path = output_dir / "maps" / f"{case_id}.map.json"
    stats_path = output_dir / "stats" / f"{case_id}.json"
    map_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    mapping = encoder.mapping()
    stats = encoder.stats()
    map_path.write_text(
        json.dumps(mapping, indent=2) + "\n", encoding="utf-8"
    )
    stats_path.write_text(
        json.dumps(stats, indent=2) + "\n", encoding="utf-8"
    )
    return {
        "encoding_version": ENCODING_VERSION,
        "template_id": case_id,
        "cnf": None
        if cnf_path is None
        else cnf_path.relative_to(output_dir).as_posix(),
        "map": map_path.relative_to(output_dir).as_posix(),
        "stats": stats_path.relative_to(output_dir).as_posix(),
        "variables": stats["variables"],
        "clauses": stats["clauses"],
    }


def main() -> None:
    default_manifest = Path(__file__).with_name(
        "n62_root_templates_theory.json"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template-manifest", type=Path, default=default_manifest
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--case-id", action="append")
    parser.add_argument("--stats-only", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest(args.template_manifest)
    templates = manifest["templates"]
    by_id = {template["id"]: template for template in templates}
    if args.self_test:
        result = audit_unary_threshold_encoder()
        print(json.dumps({"unary_threshold_encoder": result}, indent=2))
    if args.list:
        print(
            json.dumps(
                [
                    {
                        "id": template["id"],
                        "branch": template["branch"],
                        "description": template["description"],
                    }
                    for template in templates
                ],
                indent=2,
            )
        )
        if args.output_dir is None:
            return
    if args.output_dir is None:
        if args.self_test:
            return
        parser.error("--output-dir is required for generation")

    selected_ids = args.case_id or [
        template["id"] for template in templates
    ]
    unknown = [case_id for case_id in selected_ids if case_id not in by_id]
    if unknown:
        parser.error(f"unknown case IDs: {unknown}")
    records = []
    for case_id in selected_ids:
        record = generate_case(
            by_id[case_id],
            args.output_dir,
            write_cnf=not args.stats_only,
        )
        records.append(record)
        print(json.dumps(record), flush=True)
    manifest_out = {
        "schema": "n62-ab-cnf-manifest-v1",
        "encoding_version": ENCODING_VERSION,
        "source_template_manifest": str(args.template_manifest.resolve()),
        "stats_only": args.stats_only,
        "cases": records,
    }
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest_out, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
