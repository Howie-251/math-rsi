"""Recover the published 2810 graph, retaining the literal-source mismatch.

No parameter search. Original convention and corrected convention are both
explicit; comparison is by every edge, followed by an independent C++ BFS.
"""
import ast
import json
import subprocess
from collections import Counter, deque
from pathlib import Path

import networkx as nx

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
P, M, R = 281, 5, 86
Q, N = P * M, 2 * P * M
SOURCE_A = (1, 6)
SOURCE_B = (2, 220)
SOURCE_S = [(0, 242), (2, 143), (3, 106), (1, 115), (0, 251)]


def smul(g, h):
    i, x = g
    j, y = h
    return ((i + j) % M, (x * pow(R, j, P) + y) % P)


def sinv(g):
    i, x = g
    return (-i % M, -x * pow(R, -i, P) % P)


def lmul(g, h):
    x, i = g
    y, j = h
    return ((x + pow(R, i, P) * y) % P, (i + j) % M)


def linv(g):
    x, i = g
    return (-pow(R, -i, P) * x % P, -i % M)


def phi(g):
    i, x = g
    return (pow(R, -i, P) * x % P, -i % M)


def source_encode(g):
    return g[0] * P + g[1]


def left_encode(g):
    return g[0] * M + g[1]


def build(a, b, cross, source=False):
    mul, inv, enc = (smul, sinv, source_encode) if source else (lmul, linv, left_encode)
    elements = [(i, x) for i in range(M) for x in range(P)] if source else [
        (x, i) for x in range(P) for i in range(M)
    ]
    edges = set()
    for g in elements:
        v = enc(g)
        for side, u in [(0, a), (1, b)]:
            for voltage in [u, inv(u)]:
                edges.add(tuple(sorted((side * Q + v, side * Q + enc(mul(g, voltage))))))
        for voltage in cross:
            edges.add((v, Q + enc(mul(g, voltage))))
    assert len(edges) == N * 7 // 2
    assert all(u != v for u, v in edges)
    return edges


def remap(edges, permutation):
    assert sorted(permutation) == list(range(N))
    return {tuple(sorted((permutation[u], permutation[v]))) for u, v in edges}


def write_edges(name, edges):
    path = HERE / name
    path.write_text(f"{N} {len(edges)}\n" + "".join(f"{u} {v}\n" for u, v in sorted(edges)))
    return path


def two_roots(edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    assert all(len(row) == 7 for row in adj)
    result = []
    for root in [0, Q]:
        distances = {root: 0}
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in distances:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        assert len(distances) == N
        result.append({
            "root": root,
            "distance_histogram": dict(sorted(Counter(distances.values()).items())),
            "eccentricity": max(distances.values()),
            "missing_within_5": sum(d > 5 for d in distances.values()),
        })
    return result


def main():
    assert [pow(R, i, P) for i in range(6)] == [1, 86, 90, 153, 232, 1]
    public = {
        tuple(sorted(map(int, line.split())))
        for line in (HERE / "deg7_diam5_n2810_edges.txt").read_text().splitlines()
        if line.strip() and not line.startswith("#")
    }
    sage = (HERE / "2810_Dhar_SageMath.txt").read_text()
    assignment = next(line for line in sage.splitlines() if line.startswith("dhar2810 ="))
    literal = assignment[assignment.index("Graph(") + 6:-1]
    graph = nx.from_sparse6_bytes(ast.literal_eval(literal).encode("ascii"))
    sage_edges = {tuple(sorted(edge)) for edge in graph.edges()}
    assert len(graph) == N and sage_edges == public

    # The map is a group isomorphism for the literal printed multiplication.
    phi_permutation = [
        side * Q + left_encode(phi((i, x)))
        for side in range(2) for i in range(M) for x in range(P)
    ]
    printed_source = build(SOURCE_A, SOURCE_B, SOURCE_S, source=True)
    printed_left = build(phi(SOURCE_A), phi(SOURCE_B), list(map(phi, SOURCE_S)))
    assert remap(printed_source, phi_permutation) == printed_left
    write_edges("literal_printed_rule.edges", printed_source)
    write_edges("literal_phi_rule.edges", printed_left)
    printed_checks = two_roots(printed_source)
    assert two_roots(printed_left) == printed_checks

    # Negating all supplied quotient exponents in the printed source rule
    # produces the published graph under phi and the explicit vertex labels.
    negate_exponent = lambda g: (-g[0] % M, g[1])
    corrected_a = negate_exponent(SOURCE_A)
    corrected_b = negate_exponent(SOURCE_B)
    corrected_s = list(map(negate_exponent, SOURCE_S))
    corrected_source = build(corrected_a, corrected_b, corrected_s, source=True)
    a, b = phi(corrected_a), phi(corrected_b)
    cross = list(map(phi, corrected_s))
    left = build(a, b, cross)
    assert remap(corrected_source, phi_permutation) == left
    public_to_left = [
        side * Q + left_encode((x, i))
        for side in range(2) for i in range(M) for x in range(P)
    ]
    assert remap(public, public_to_left) == left

    anchor = cross[0]
    b_normal = lmul(lmul(anchor, b), linv(anchor))
    cross_normal = [lmul(s, linv(anchor)) for s in cross]
    assert cross_normal[0] == (0, 0)
    normalized = build(a, b_normal, cross_normal)
    left_to_normal = [
        side * Q + left_encode((x, i) if side == 0 else lmul((x, i), linv(anchor)))
        for side in range(2) for x in range(P) for i in range(M)
    ]
    assert remap(left, left_to_normal) == normalized
    public_to_normal = [left_to_normal[v] for v in public_to_left]
    assert remap(public, public_to_normal) == normalized

    write_edges("published_with_header.edges", public)
    write_edges("corrected_source_coordinates.edges", corrected_source)
    write_edges("left_action_unanchored.edges", left)
    normalized_path = write_edges("baseline_normalized.edges", normalized)
    roots = two_roots(normalized)
    assert two_roots(corrected_source) == roots
    assert two_roots(public) == roots
    run = subprocess.run(
        [str(PROJECT / "computations/ddp/verify_graph"), str(normalized_path), "7", "5"],
        text=True, capture_output=True,
    )
    assert run.returncode == 0, (run.returncode, run.stdout, run.stderr)
    full = json.loads(run.stdout)
    predicted = Counter()
    for root in roots:
        for distance, count in root["distance_histogram"].items():
            predicted[distance] += Q * count
    assert {str(k): v for k, v in sorted(predicted.items())} == full["ordered_distance_histogram"]
    assert full["min_degree"] == full["max_degree"] == 7
    assert full["n"] == N and full["m"] == 9835 and full["diameter"] == 5
    plain = [left_encode(g) for g in [a, b_normal, *cross_normal[1:]]]
    (HERE / "baseline_normalized_parameters.txt").write_text(" ".join(map(str, plain)) + "\n")
    (HERE / "public_to_normalized_vertices.json").write_text(json.dumps(public_to_normal) + "\n")
    result = {
        "status": "PUBLISHED_BASELINE_RECOVERED_WITH_PRINTED_CONVENTION_DISCREPANCY",
        "p": P, "m": M, "r": R, "group_order": Q, "graph_order": N,
        "source_printed_a": SOURCE_A, "source_printed_b": SOURCE_B, "source_printed_cross": SOURCE_S,
        "literal_printed_rule_roots": printed_checks,
        "literal_phi_full_edge_equality": True,
        "corrected_source_a": corrected_a, "corrected_source_b": corrected_b, "corrected_source_cross": corrected_s,
        "left_unanchored_a": a, "left_unanchored_b": b, "left_unanchored_cross": cross,
        "anchor": anchor,
        "left_normalized_a": a, "left_normalized_a_inverse": linv(a),
        "left_normalized_b": b_normal, "left_normalized_b_inverse": linv(b_normal),
        "left_normalized_cross": cross_normal,
        "normal_label": "side*1405 + x*5 + i",
        "plain_six_values_a_b_s1_s2_s3_s4": plain,
        "all_9835_public_edges_match": True,
        "sage_sparse6_equals_public_edges": True,
        "corrected_source_phi_full_edge_equality": True,
        "cross_anchor_full_edge_equality": True,
        "two_root_checks": roots,
        "independent_cpp_all_root_bfs": full,
    }
    (HERE / "recovery_result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
