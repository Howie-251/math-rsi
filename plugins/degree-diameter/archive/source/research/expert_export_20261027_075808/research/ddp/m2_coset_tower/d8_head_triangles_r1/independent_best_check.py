"""The one authorized r=1 saved-best edge rebuild and full-source verification."""
import json
import resource
import subprocess
import time
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
N, LEAVES, BLOCK_START, HEAD_START = 7203, 6174, 6174, 7056
start = time.process_time()
wall_start = time.monotonic()
children_before = resource.getrusage(resource.RUSAGE_CHILDREN)
saved = json.loads((HERE / "production.best.json").read_text())
S = set(saved["S"])
assert len(S) == len(saved["S"]) == 7 and 0 not in S


def decode(g):
    x, k = g % 147, g // 147
    return x % 7, x // 7 % 7, x // 49, k % 7, k // 7


def encode(u, v, w, b, j):
    return u % 7 + 7 * (v % 7) + 49 * (w % 3) + 147 * (b % 7 + 7 * (j % 6))


def multiply(g, h):
    u, v, w, b, j = decode(g)
    z, t, a, d, ell = decode(h)
    scale = pow(3, j, 7)
    # r=1: K is the direct product; both field coordinates have scalar 3^j.
    return encode(u + scale * (z + b * t), v + scale * t, w + a, b + d, j + ell)


def inverse(g):
    u, v, w, b, j = decode(g)
    scale = pow(3, -j % 6, 7)
    return encode(-scale * (u - b * v), -scale * v, -w, -b, -j)


assert {inverse(g) for g in S} == S
assert all(multiply(g, inverse(g)) == multiply(inverse(g), g) == 0 for g in S)
expected = set()
for g in range(LEAVES):
    for s in S:
        other = multiply(g, s)
        assert other != g
        expected.add(tuple(sorted((g, other))))
    x, j = g % 147, g // 147 // 7
    expected.add((g, BLOCK_START + x + 147 * j))
for j in range(6):
    for x in range(147):
        expected.add((BLOCK_START + x + 147 * j, HEAD_START + x))
triangles = set()
for u in range(7):
    for v in range(7):
        h = [HEAD_START + u + 7 * v + 49 * w for w in range(3)]
        triangles.update(((h[0], h[1]), (h[0], h[2]), (h[1], h[2])))
assert len(triangles) == 147
expected |= triangles
assert len(expected) == 28812

edge_path = HERE / "production.best.edges"
data = list(map(int, edge_path.read_text().split()))
n, m = data[:2]
assert (n, m) == (N, 28812) and len(data) == 2 + 2 * m
edges = [tuple(sorted(pair)) for pair in zip(data[2::2], data[3::2])]
actual = set(edges)
assert len(actual) == m and all(0 <= u < v < n for u, v in edges)
assert actual == expected, "r=1 independently reconstructed edges differ from the saved file"
assert {edge for edge in actual if edge[0] >= HEAD_START} == triangles
adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
assert set(map(len, adj)) == {8}

layers = [("leaf", 0, BLOCK_START), ("block", BLOCK_START, HEAD_START), ("head", HEAD_START, N)]
roots = []
for name, root, _ in layers:
    distances = [-1] * n
    distances[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                queue.append(v)
    roots.append({"layer": name, "root": root,
                  "missing": sum(d < 0 or d > 5 for d in distances),
                  "missing_by_target_layer": [sum(d < 0 or d > 5 for d in distances[lo:hi])
                                              for _, lo, hi in layers],
                  "unreachable": distances.count(-1),
                  "distance_histogram": dict(sorted(Counter(distances).items()))})
assert [row["missing"] for row in roots] == saved["root_missing"]
assert [row["missing_by_target_layer"] for row in roots] == saved["root_missing_by_target_layer"]
sizes = [6174, 882, 147]
weighted_hist = Counter()
for size, row in zip(sizes, roots):
    for distance, count in row["distance_histogram"].items():
        weighted_hist[distance] += size * count
ordered_bad = sum(size * row["missing"] for size, row in zip(sizes, roots))
assert ordered_bad % 2 == 0
bad = ordered_bad // 2
assert bad == saved["bad_unordered_pairs"] == 3995460
assert roots[1]["missing_by_target_layer"][1] == saved["original_BB_missing"] == 29

# Exactly one full-source generic checker invocation, on this saved graph only.
process = subprocess.run([str(PROJECT / "computations/ddp/verify_graph"), str(edge_path), "8", "5"],
                         capture_output=True, text=True)
assert process.returncode in (0, 1), process.stderr
full = json.loads(process.stdout)
(HERE / "best.independent_verify.json").write_text(json.dumps(full, indent=2) + "\n")
assert full["roots_checked"] == N
assert full["n"] == N and full["m"] == m
assert full["min_degree"] == full["max_degree"] == 8
assert full["unreachable_unordered_pairs"] == 0
assert full["bad_unordered_pairs"] == bad
assert {int(k): v for k, v in full["ordered_distance_histogram"].items()} == dict(weighted_hist)
assert full["diameter"] == max(weighted_hist)
children_after = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = (children_after.ru_utime + children_after.ru_stime
             - children_before.ru_utime - children_before.ru_stime)
python_cpu = time.process_time() - start
result = {
    "status": "COMPLETE_ONE_R1_SAVED_BEST_INDEPENDENT_CHECK_NO_SEARCH",
    "input_parameters": "production.best.json", "input_edges": "production.best.edges",
    "selection": saved["selection"],
    "group_action": "r=1: (b,j)(u,v,w)=(3^j*(u+b*v),3^j*v,w)",
    "K_multiplication": "(b,j)(d,l)=(b+d mod7,j+l mod6)",
    "producer_arithmetic_tables_used": False,
    "S": sorted(S), "S_coordinates_u_v_w_b_j": [decode(g) for g in sorted(S)],
    "independent_edges_exactly_equal": True, "n": n, "m": m, "simple": True,
    "min_degree": 8, "max_degree": 8, "head_triangle_edges": len(triangles),
    "connected": True, "diameter": full["diameter"],
    "representative_roots": roots, "bad_unordered_pairs": bad,
    "original_BB_missing": roots[1]["missing_by_target_layer"][1],
    "all_source_distance_histogram_matches_weighted_three_roots": True,
    "generic_full_source_checker_invocations": 1,
    "full_source_roots_checked": full["roots_checked"],
    "full_check_file": "best.independent_verify.json",
    "python_cpu_seconds": python_cpu, "checker_cpu_seconds": child_cpu,
    "total_cpu_seconds": python_cpu + child_cpu,
    "wall_seconds": time.monotonic() - wall_start,
    "preflight_rechecked": False,
    "new_candidate_searches": 0,
    "scope": "Only the specified minimum-BB fallback saved graph; not a minimum-bad-pairs claim over the population.",
}
(HERE / "production.best.independent_check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
