#!/usr/bin/env python3
"""Independently verify a complete 59-vertex candidate graph.

The verifier deliberately reconstructs every mathematical quantity from the
adjacency matrix.  It does not trust common-neighbour, repeat, or quotient
auxiliary variables emitted by a SAT encoder.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Iterable, Sequence

from sat59.solver_output import load_sat_solver_output

N = 59
K = 8
EDGE_COUNT = 236


class VerificationError(ValueError):
    """Raised when a proposed graph violates a required property."""


def _empty_matrix() -> list[list[int]]:
    return [[0 for _ in range(N)] for _ in range(N)]


def load_matrix(path: Path) -> list[list[int]]:
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("["):
        matrix = json.loads(text)
    else:
        matrix = [
            [int(value) for value in line.replace(",", " ").split()]
            for line in text.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
    return [[int(value) for value in row] for row in matrix]


def load_edge_list(path: Path) -> list[list[int]]:
    matrix = _empty_matrix()
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        values = stripped.replace(",", " ").split()
        if len(values) != 2:
            raise VerificationError(f"bad edge-list line: {line!r}")
        u, v = map(int, values)
        if not (0 <= u < N and 0 <= v < N) or u == v:
            raise VerificationError(f"bad edge ({u}, {v})")
        matrix[u][v] = matrix[v][u] = 1
    return matrix


def load_model_with_map(model_path: Path, map_path: Path) -> list[list[int]]:
    assignment = load_sat_solver_output(model_path)
    mapping = json.loads(map_path.read_text(encoding="utf-8"))
    if int(mapping.get("order", N)) != N:
        raise VerificationError("variable map does not describe order 59")
    matrix = _empty_matrix()
    for u, v in mapping.get("fixed_edges", []):
        matrix[int(u)][int(v)] = matrix[int(v)][int(u)] = 1
    edge_variables = mapping.get("edge_variables", [])
    if isinstance(edge_variables, dict):
        entries = (
            {"var": int(var), "u": int(key.split(",")[0]),
             "v": int(key.split(",")[1])}
            for key, var in edge_variables.items()
        )
    else:
        entries = iter(edge_variables)
    entries = list(entries)
    assignment.require_assigned(
        (int(entry["var"]) for entry in entries),
        "edge",
    )
    for entry in entries:
        if int(entry["var"]) in assignment.positive_variables:
            u, v = int(entry["u"]), int(entry["v"])
            matrix[u][v] = matrix[v][u] = 1
    return matrix


def common_count(matrix: Sequence[Sequence[int]], u: int, v: int) -> int:
    return sum(matrix[u][w] & matrix[v][w] for w in range(N))


def repeat_matrix(matrix: Sequence[Sequence[int]]) -> list[list[int]]:
    result = [[0 for _ in range(N)] for _ in range(N)]
    for u in range(N):
        for v in range(N):
            a2 = sum(matrix[u][w] * matrix[w][v] for w in range(N))
            result[u][v] = a2 + matrix[u][v] - (7 if u == v else 0) - 1
    return result


def support_components(repeat: Sequence[Sequence[int]]) -> list[tuple[int, ...]]:
    unseen = set(range(N))
    components: list[tuple[int, ...]] = []
    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        component: list[int] = []
        while stack:
            u = stack.pop()
            component.append(u)
            neighbours = [v for v in sorted(unseen) if repeat[u][v] > 0]
            for v in neighbours:
                unseen.remove(v)
                stack.append(v)
        components.append(tuple(sorted(component)))
    return sorted(components, key=lambda values: (len(values), values))


def support_is_bipartite(repeat: Sequence[Sequence[int]]) -> bool:
    colors: dict[int, int] = {}
    for start in range(N):
        if start in colors:
            continue
        colors[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in range(N):
                if repeat[u][v] <= 0:
                    continue
                if v not in colors:
                    colors[v] = 1 - colors[u]
                    stack.append(v)
                elif colors[v] == colors[u]:
                    return False
    return True


def quotient_matrix(
    matrix: Sequence[Sequence[int]],
    components: Sequence[Sequence[int]],
) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for component in components:
        reference: tuple[int, ...] | None = None
        for u in component:
            row = tuple(sum(matrix[u][v] for v in target) for target in components)
            if reference is None:
                reference = row
            elif row != reference:
                raise VerificationError(
                    f"repeat components are not equitable at vertex {u}: "
                    f"{row} != {reference}"
                )
        assert reference is not None
        rows.append(reference)
    return tuple(rows)


def _expected_branch_data(branch: str):
    # Mathematical input is repeated here so this verifier does not depend on
    # the encoder implementation.
    data = {
        "c3": (
            (4, 20, 35),
            ((3, 5, 0), (1, 0, 7), (0, 4, 4)),
        ),
        "c5a": (
            (3, 4, 12, 20, 20),
            (
                (0, 4, 4, 0, 0),
                (3, 0, 0, 0, 5),
                (1, 0, 2, 5, 0),
                (0, 0, 3, 1, 4),
                (0, 1, 0, 4, 3),
            ),
        ),
        "c5b": (
            (6, 6, 12, 15, 20),
            (
                (0, 3, 0, 5, 0),
                (3, 1, 4, 0, 0),
                (0, 2, 1, 0, 5),
                (2, 0, 0, 2, 4),
                (0, 0, 3, 3, 2),
            ),
        ),
    }
    return data[branch]


def verify_quotient_branch(
    matrix: Sequence[Sequence[int]],
    components: Sequence[Sequence[int]],
    branch: str,
) -> tuple[tuple[int, ...], ...]:
    expected_sizes, expected_q = _expected_branch_data(branch)
    if len(components) != len(expected_sizes):
        raise VerificationError(
            f"{branch} needs {len(expected_sizes)} repeat components, "
            f"found {len(components)}"
        )
    actual_sizes = tuple(len(component) for component in components)
    candidates = [
        permutation
        for permutation in itertools.permutations(range(len(components)))
        if tuple(actual_sizes[i] for i in permutation) == expected_sizes
    ]
    for permutation in candidates:
        ordered = [components[i] for i in permutation]
        try:
            actual_q = quotient_matrix(matrix, ordered)
        except VerificationError:
            continue
        if actual_q == expected_q:
            return actual_q
    raise VerificationError(
        f"repeat-component sizes/quotient do not match {branch}; "
        f"component sizes are {actual_sizes}"
    )


def verify_graph(
    matrix: Sequence[Sequence[int]],
    branch: str | None = None,
) -> dict[str, object]:
    if len(matrix) != N or any(len(row) != N for row in matrix):
        raise VerificationError("adjacency matrix must be 59 by 59")
    if any(value not in (0, 1) for row in matrix for value in row):
        raise VerificationError("adjacency entries must be zero or one")
    for u in range(N):
        if matrix[u][u] != 0:
            raise VerificationError(f"loop at vertex {u}")
        for v in range(u + 1, N):
            if matrix[u][v] != matrix[v][u]:
                raise VerificationError(f"asymmetry at ({u}, {v})")

    degrees = [sum(row) for row in matrix]
    if any(degree != K for degree in degrees):
        raise VerificationError(f"degrees are not all 8: {degrees}")
    edges = sum(degrees) // 2
    if edges != EDGE_COUNT:
        raise VerificationError(f"expected 236 edges, found {edges}")

    common = [[0 for _ in range(N)] for _ in range(N)]
    for u in range(N):
        for v in range(u + 1, N):
            common[u][v] = common[v][u] = common_count(matrix, u, v)
            if matrix[u][v] + common[u][v] < 1:
                raise VerificationError(f"vertices {u},{v} have distance greater than 2")
            if matrix[u][v] and common[u][v] > 3:
                raise VerificationError(
                    f"adjacent vertices {u},{v} have {common[u][v]} common neighbours"
                )

    repeat = repeat_matrix(matrix)
    if any(repeat[u][u] != 0 for u in range(N)):
        raise VerificationError("repeat matrix has nonzero diagonal")
    if any(repeat[u][v] < 0 for u in range(N) for v in range(N)):
        raise VerificationError("repeat matrix has a negative entry")
    if any(repeat[u][v] > 5 for u in range(N) for v in range(N)):
        raise VerificationError("repeat matrix has an entry greater than 5")
    row_sums = [sum(row) for row in repeat]
    if any(total != 6 for total in row_sums):
        raise VerificationError(f"repeat row sums are not all 6: {row_sums}")

    components = support_components(repeat)
    actual_q: tuple[tuple[int, ...], ...] | None = None
    if branch == "c1":
        if len(components) != 1:
            raise VerificationError(f"c1 requires connected B support; found {len(components)}")
        if support_is_bipartite(repeat):
            raise VerificationError("c1 repeat support must be non-bipartite")
    elif branch is not None:
        actual_q = verify_quotient_branch(matrix, components, branch)

    triangles = sum(
        matrix[u][v] * matrix[u][w] * matrix[v][w]
        for u, v, w in itertools.combinations(range(N), 3)
    )
    four_cycle_twice = sum(
        math.comb(common[u][v], 2)
        for u, v in itertools.combinations(range(N), 2)
    )
    if four_cycle_twice % 2:
        raise VerificationError("four-cycle count is not integral")
    four_cycles = four_cycle_twice // 2
    parallel_repeat_pairs = sum(
        math.comb(repeat[u][v], 2)
        for u, v in itertools.combinations(range(N), 2)
    )
    identity_rhs = 2 * four_cycles + 3 * triangles - 177
    if parallel_repeat_pairs != identity_rhs:
        raise VerificationError(
            "repeat/cycle identity failed: "
            f"{parallel_repeat_pairs} != {identity_rhs}"
        )

    return {
        "status": "VERIFIED",
        "order": N,
        "degree": K,
        "edges": edges,
        "diameter_at_most": 2,
        "repeat_component_count": len(components),
        "repeat_component_sizes": [len(component) for component in components],
        "repeat_max_entry": max(max(row) for row in repeat),
        "triangles": triangles,
        "four_cycles": four_cycles,
        "parallel_repeat_pairs": parallel_repeat_pairs,
        "branch": branch,
        "quotient": actual_q,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--matrix", type=Path)
    source.add_argument("--edge-list", type=Path)
    source.add_argument("--model", type=Path)
    parser.add_argument("--map", dest="map_path", type=Path)
    parser.add_argument("--branch", choices=("c1", "c3", "c5a", "c5b"))
    parser.add_argument("--json", action="store_true", help="print JSON summary")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.matrix:
            matrix = load_matrix(args.matrix)
        elif args.edge_list:
            matrix = load_edge_list(args.edge_list)
        else:
            if args.map_path is None:
                raise VerificationError("--model requires --map")
            matrix = load_model_with_map(args.model, args.map_path)
        summary = verify_graph(matrix, args.branch)
    except (OSError, ValueError, VerificationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print("VERIFIED")
        for key, value in summary.items():
            if key != "status":
                print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

