"""Read-only graph diagnosis for one simultaneous boundary reconstruction.

No candidate generation, optimizer, solver, or BFS is executed.
"""
import json
import resource
import time
from collections import Counter
from pathlib import Path


def components(vertices, pairs):
    adj = {v: set() for v in vertices}
    for u, v in pairs:
        adj[u].add(v)
        adj[v].add(u)
    unseen = set(vertices)
    result = []
    while unseen:
        todo = [min(unseen)]
        unseen.remove(todo[0])
        part = []
        while todo:
            u = todo.pop()
            part.append(u)
            for v in sorted(adj[u] & unseen):
                unseen.remove(v)
                todo.append(v)
        result.append({"vertices": sorted(part),
                       "degrees": sorted(len(adj[v]) for v in part),
                       "edges": sum(len(adj[v]) for v in part) // 2})
    return result


def bipartite_cover(vertices, pairs):
    adj = {v: set() for v in vertices}
    for u, v in pairs:
        adj[u].add(v)
        adj[v].add(u)
    color = {}
    for root in sorted(vertices):
        if root in color:
            continue
        color[root] = 0
        todo = [root]
        for u in todo:
            for v in sorted(adj[u]):
                if v in color:
                    if color[v] == color[u]:
                        return None
                else:
                    color[v] = 1 - color[u]
                    todo.append(v)
    match = {}
    def augment(u, seen):
        for v in sorted(adj[u]):
            if v in seen:
                continue
            seen.add(v)
            if v not in match or augment(match[v], seen):
                match[v] = u
                return True
        return False
    left = sorted(v for v in vertices if color[v] == 0)
    for u in left:
        augment(u, set())
    used_left = set(match.values())
    reached = set(left) - used_left
    todo = list(sorted(reached))
    for u in todo:
        if color[u] == 0:
            targets = [v for v in adj[u] if match.get(v) != u]
        else:
            targets = [match[u]] if u in match else []
        for v in targets:
            if v not in reached:
                reached.add(v)
                todo.append(v)
    cover = (set(left) - reached) | {v for v in reached if color[v] == 1}
    assert len(cover) == len(match) and all(u in cover or v in cover for u, v in pairs)
    return sorted(cover)


def diagnose(path):
    if path.suffix == ".edges":
        values = [tuple(map(int, line.split())) for line in path.read_text().splitlines()]
        n, m = values[0]
        edges = values[1:]
        assert len(edges) == m
    else:
        data = json.loads(path.read_text())
        n, edges = data["n"], [tuple(e) for e in data["edges"]]
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n and v not in adj[u]
        adj[u].add(v)
        adj[v].add(u)
    assert n in (58, 60) and all(len(a) == 8 for a in adj)
    bad = [(u, v) for u in range(n) for v in range(u + 1, n)
           if v not in adj[u] and not adj[u] & adj[v]]
    patch = set(v for e in bad for v in e)
    outside = set(range(n)) - patch
    fixed = [(u, v) for u, v in edges if u in outside and v in outside]
    cut = [(u, v) for u, v in edges if (u in patch) != (v in patch)]
    inside = [(u, v) for u, v in edges if u in patch and v in patch]
    obligations = [(u, v) for u in sorted(outside) for v in sorted(outside)
                   if u < v and v not in adj[u] and not (adj[u] & adj[v] & outside)]
    residual = {u: 8 - len(adj[u] & outside) for u in outside}
    outside_pair_count = len(outside) * (len(outside) - 1) // 2
    cover = bipartite_cover(patch, bad)
    cover_profile = None
    if cover is not None:
        active = set(cover)
        fixed_vertices = set(range(n)) - active
        capacity = {u: len(adj[u] & active) for u in fixed_vertices}
        zero_obstructions = []
        for u in sorted(fixed_vertices):
            if capacity[u] == 0:
                available = sum(capacity[v] for v in adj[u])
                if available < len(active):
                    zero_obstructions.append({"vertex": u, "available": available,
                                              "required": len(active)})
        cover_profile = {"vertices": cover, "size": len(cover),
                         "scope": "minimum vertex cover of the bipartite bad-pair graph only",
                         "outside_size": len(fixed_vertices),
                         "residual_degree_histogram": dict(sorted(Counter(capacity.values()).items())),
                         "zero_port_obstructions": zero_obstructions,
                         "outside_is_literal_induced_7regular_Moore50": len(fixed_vertices) == 50
                             and all(len(adj[u] & fixed_vertices) == 7 for u in fixed_vertices)
                             and all(len(adj[u] & adj[v] & fixed_vertices) == (0 if v in adj[u] else 1)
                                     for u in fixed_vertices for v in fixed_vertices if u < v)}
    return {
        "source": str(path), "n": n, "bad_pair_count": len(bad), "bad_pairs": bad,
        "minimum_bad_vertex_cover": cover_profile,
        "bad_graph_components": components(patch, bad),
        "patch": sorted(patch), "outside": sorted(outside),
        "fixed_outside_edges": fixed, "seed_cut_edges": cut,
        "seed_inside_patch_edges": inside,
        "outside_residual_degree": residual,
        "outside_residual_degree_histogram": dict(sorted(Counter(residual.values()).items())),
        "outside_pair_obligations": obligations,
        "outside_obligation_components": components(outside, obligations),
        "outside_pairs_covered_by_fixed_edges_or_fixed_two_paths": outside_pair_count - len(obligations),
        "cut_binary_variables": len(patch) * len(outside),
        "inside_patch_binary_variables": len(patch) * (len(patch) - 1) // 2,
        "variable_pair_coverage_constraints": len(obligations) + len(patch) * len(outside)
                                              + len(patch) * (len(patch) - 1) // 2,
    }


if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    cpu, wall = time.process_time(), time.monotonic()
    here = Path(__file__).resolve().parent
    old = here / "fullgraph60_weighted_run"
    paths = [old / "seed.edges", old / "candidate.alternative20.json",
             old / "candidate.current.edges",
             here / "twin59_to_58_deflation_run" / "component.path1.edges"]
    result = {"status": "DIAGNOSTIC_ONLY_NO_SEARCH", "graphs": [diagnose(p) for p in paths]}
    result["cpu_seconds"] = time.process_time() - cpu
    result["wall_seconds"] = time.monotonic() - wall
    output = here / "fullgraph60_boundary_patch_diagnostic.result.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "cpu_seconds": result["cpu_seconds"],
                     "wall_seconds": result["wall_seconds"],
                     "graphs": [{"n": g["n"], "bad": g["bad_pair_count"], "patch_size": len(g["patch"]),
                                 "fixed_edges": len(g["fixed_outside_edges"]),
                                 "cut_edges": len(g["seed_cut_edges"]),
                                 "patch_edges": len(g["seed_inside_patch_edges"]),
                                 "residual": g["outside_residual_degree_histogram"],
                                 "outside_obligations": len(g["outside_pair_obligations"]),
                                 "minimum_bad_vertex_cover": g["minimum_bad_vertex_cover"],
                                 "obligation_component_sizes": [len(c["vertices"]) for c in g["outside_obligation_components"]]}
                                for g in result["graphs"]]}, indent=2))
