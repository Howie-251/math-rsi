#!/usr/bin/env python3
"""Independently verify a SAT model for one seven-template n=62 A+B CNF."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

N = 62
X = tuple(range(1, 9))
Y = tuple(range(9, 62))


def pair(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def parse_positive_model(path: Path) -> set[int]:
    positive: set[int] = set()
    saw_values = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if stripped.startswith("v "):
            tokens = stripped[2:].split()
        elif stripped and stripped[0] in "-0123456789" and not stripped.startswith("c"):
            tokens = stripped.split()
        else:
            continue
        for token in tokens:
            value = int(token)
            if value != 0:
                saw_values = True
            if value > 0:
                positive.add(value)
    if not saw_values:
        raise ValueError("model file contains no assignment literals")
    return positive


def load_template(manifest_path: Path, case_id: str) -> dict:
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    matches = [t for t in payload["templates"] if t["id"] == case_id]
    if len(matches) != 1:
        raise ValueError(f"template {case_id!r} not found exactly once")
    return matches[0]


def reconstruct_graph(template: dict, mapping: dict, positive: set[int]):
    adjacency = [set() for _ in range(N)]

    def add(u: int, v: int) -> None:
        if u == v or v in adjacency[u]:
            raise AssertionError(f"invalid or duplicate fixed edge {(u, v)}")
        adjacency[u].add(v)
        adjacency[v].add(u)

    for x in X:
        add(0, x)
    for u, v in template["H_edges"]:
        add(u, v)
    for y_text, parents in template["parent_map"].items():
        y = int(y_text)
        for x in parents:
            add(x, y)
    edge_variables = {(u, v): variable for u, v, variable in mapping["edge_variables"]}
    if len(edge_variables) != 1378:
        raise AssertionError("variable map does not contain all 1378 Y-Y edges")
    for (u, v), variable in edge_variables.items():
        if variable in positive:
            add(u, v)
    return adjacency


def compute_B(adjacency):
    B = [[0] * N for _ in range(N)]
    for u in range(N):
        for v in range(u + 1, N):
            common = len(adjacency[u] & adjacency[v])
            value = common + int(v in adjacency[u]) - 1
            B[u][v] = B[v][u] = value
    return B


def verify(template: dict, mapping: dict, positive: set[int]) -> dict:
    if mapping.get("template_id") != template["id"]:
        raise AssertionError("template and variable map IDs differ")
    adjacency = reconstruct_graph(template, mapping, positive)
    degrees = [len(row) for row in adjacency]
    if degrees != [8] * N:
        raise AssertionError(f"degree check failed: {degrees}")
    edge_count = sum(degrees) // 2
    if edge_count != 248:
        raise AssertionError(f"edge count is {edge_count}, expected 248")
    for u in range(N):
        for v in range(u + 1, N):
            if v not in adjacency[u] and adjacency[u].isdisjoint(adjacency[v]):
                raise AssertionError(f"pair {(u, v)} has distance greater than two")

    B = compute_B(adjacency)
    values = [B[u][v] for u in range(N) for v in range(u + 1, N)]
    if min(values) < 0 or max(values) > 2:
        raise AssertionError(f"B range is [{min(values)}, {max(values)}]")
    row_sums = [sum(row) for row in B]
    if row_sums != [3] * N:
        raise AssertionError(f"B row sums are not all three: {row_sums}")
    if template["global_B_mode"] == "simple_0/1" and max(values) > 1:
        raise AssertionError("simple-B template produced a double B edge")

    triangles_at = []
    for u in range(N):
        triangles_at.append(
            sum(v in adjacency[w] for v in adjacency[u] for w in adjacency[u] if v < w)
        )
    if max(triangles_at) > 1:
        raise AssertionError(f"a vertex lies in more than one triangle: {triangles_at}")
    triangle_count = sum(triangles_at) // 3

    for u, v, value in template["fixed_B"]:
        if B[u][v] != value:
            raise AssertionError(f"fixed B[{u},{v}]={B[u][v]} != {value}")
    for u, v in template["fixed_extra_edges"]:
        if v not in adjacency[u]:
            raise AssertionError(f"required edge {(u, v)} is absent")
    for u, v in template["fixed_extra_nonedges"]:
        if v in adjacency[u]:
            raise AssertionError(f"required nonedge {(u, v)} is present")
    for vertex_text, expected in template["fixed_triangle_membership"].items():
        vertex = int(vertex_text)
        if int(triangles_at[vertex] == 1) != expected:
            raise AssertionError(f"triangle membership mismatch at {vertex}")

    local = template.get("double_local")
    if local is not None:
        w = int(local["w"])
        S = set(map(int, local["S"]))
        if local["forbid_w_neighbors_with_parent_intersecting_S"]:
            for y_text, parents in template["parent_map"].items():
                y = int(y_text)
                if y != w and set(parents) & S and y in adjacency[w]:
                    raise AssertionError(f"forbidden w-neighbor {y}")
        for label_text, expected in local["w_neighbors_in_singleton_classes"].items():
            vertices = template["singleton_classes"][str(label_text)]
            actual = sum(y in adjacency[w] for y in vertices)
            if actual != expected:
                raise AssertionError(
                    f"w/class {label_text} count {actual} != {expected}"
                )
    if template.get("triangle_membership_xor") is not None:
        parity = sum(value == 1 for value in triangles_at) % 2
        if parity != template["triangle_membership_xor"]:
            raise AssertionError("triangle-membership parity mismatch")

    b1_map = {(u, v): variable for u, v, variable in mapping["b1_variables"]}
    b2_map = {(u, v): variable for u, v, variable in mapping["b2_variables"]}
    for (u, v), variable in b1_map.items():
        if (variable in positive) != (B[u][v] == 1):
            raise AssertionError(f"model b1 selector disagrees at {(u, v)}")
    for (u, v), variable in b2_map.items():
        if (variable in positive) != (B[u][v] == 2):
            raise AssertionError(f"model b2 selector disagrees at {(u, v)}")
    tau_map = {vertex: variable for vertex, variable in mapping["tau_variables"]}
    for vertex, variable in tau_map.items():
        if (variable in positive) != (triangles_at[vertex] == 1):
            raise AssertionError(f"model tau selector disagrees at {vertex}")

    return {
        "status": "SAT_MODEL_VERIFIED",
        "template_id": template["id"],
        "vertices": N,
        "edges": edge_count,
        "degree": 8,
        "diameter_at_most": 2,
        "triangles": triangle_count,
        "B_double_edges": sum(B[u][v] == 2 for u in range(N) for v in range(u + 1, N)),
    }, adjacency


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template-manifest", type=Path, required=True)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--map", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--edges-out", type=Path)
    args = parser.parse_args()
    template = load_template(args.template_manifest, args.case_id)
    mapping = json.loads(args.map.read_text(encoding="utf-8"))
    positive = parse_positive_model(args.model)
    result, adjacency = verify(template, mapping, positive)
    if args.edges_out is not None:
        edges = [
            (u, v)
            for u in range(N)
            for v in range(u + 1, N)
            if v in adjacency[u]
        ]
        args.edges_out.write_text(
            "".join(f"{u} {v}\n" for u, v in edges), encoding="utf-8"
        )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
