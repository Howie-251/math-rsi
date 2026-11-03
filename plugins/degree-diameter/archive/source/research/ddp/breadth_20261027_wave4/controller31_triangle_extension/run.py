"""One complete specified triangle-overlap family; raw NB3 necessary tests only."""

from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import resource
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "mizuno_d3_source"


def edge(u, v):
    return (min(u, v), max(u, v))


def cycle_edges(cycle):
    return {edge(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle))}


def triangles(adjacency):
    return [[u, v, w] for u in range(len(adjacency)) for v in sorted(adjacency[u]) if v > u
            for w in sorted(adjacency[u] & adjacency[v]) if w > v]


def counts_nb3(adjacency):
    n = len(adjacency)
    result = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in adjacency[u]:
            for w in adjacency[v]:
                if w == u:
                    continue
                for x in adjacency[w]:
                    if x != v:
                        result[u][x] += 1
    return result


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    began, wall = time.process_time(), time.monotonic()
    construction = json.loads((SOURCE / "construction.json").read_text())
    structure = json.loads((SOURCE / "controller_structure.json").read_text())
    source_adj = [set(a) for a in construction["controller"]]
    assert len(source_adj) == 30 and all(len(a) == 4 for a in source_adj)
    assert all(u in source_adj[v] for u in range(30) for v in source_adj[u])
    source_edges = {edge(u, v) for u in range(30) for v in source_adj[u]}
    assert len(source_edges) == 60
    original_triangles = triangles(source_adj)
    assert len(original_triangles) == 10
    assert sorted(v for t in original_triangles for v in t) == list(range(30))
    assert original_triangles == structure["triangles"]
    triangle_edges = {edge(u, v) for t in original_triangles for u, v in combinations(t, 2)}
    cycles = structure["external_2factor_cycles"]
    assert len(cycles) == 6 and all(len(c) == 5 for c in cycles)
    assert sorted(v for c in cycles for v in c) == list(range(30))
    external_edges = set().union(*(cycle_edges(c) for c in cycles))
    assert len(external_edges) == 30 and not (external_edges & triangle_edges)
    assert external_edges | triangle_edges == source_edges
    triangle_id, cycle_id = {}, {}
    for i, t in enumerate(original_triangles):
        for v in t:
            triangle_id[v] = i
    for i, c in enumerate(cycles):
        for v in c:
            cycle_id[v] = i
    same_triangle = sum(triangle_id[a] == triangle_id[b] for a, b in combinations(range(30), 2))
    same_cycle = sum(cycle_id[a] == cycle_id[b] for a, b in combinations(range(30), 2))
    both = sum(triangle_id[a] == triangle_id[b] and cycle_id[a] == cycle_id[b]
               for a, b in combinations(range(30), 2))
    pairs = [(a, b) for a, b in combinations(range(30), 2)
             if triangle_id[a] != triangle_id[b] and cycle_id[a] != cycle_id[b]]
    inputs = {
        "source_n": 30, "source_m": 60, "source_triangles": original_triangles,
        "source_external_cycles": cycles, "all_unordered_pairs": 435,
        "same_triangle_pairs": same_triangle, "same_external_cycle_pairs": same_cycle,
        "both_same_triangle_and_cycle": both, "actual_eligible_unordered_pairs": len(pairs),
        "choices_per_pair": 8, "raw_candidates_expected_from_actual_pairs": 8 * len(pairs),
        "anchor_pairs": pairs,
    }
    (HERE / "inputs.json").write_text(json.dumps(inputs, indent=2) + "\n")
    all_summaries, passers, unique_graphs = [], [], set()
    histogram, triangle_histogram, diagonal_histogram = Counter(), Counter(), Counter()
    first_calibrated = False
    best = None
    completed = 0
    internal_limit = False
    for a, b in pairs:
        if time.process_time() - began >= 28:
            internal_limit = True
            break
        assert edge(a, b) not in source_edges
        ca, cb = cycle_id[a], cycle_id[b]
        shortened = [list(c) for c in cycles]
        shortened[ca].remove(a)
        shortened[cb].remove(b)
        assert len(shortened[ca]) == len(shortened[cb]) == 4
        for chosen_cycle in sorted((ca, cb)):
            for position in range(4):
                cycle = shortened[chosen_cycle]
                insertion_edge = edge(cycle[position], cycle[(position + 1) % 4])
                changed = [list(c) for c in shortened]
                changed[chosen_cycle].insert(position + 1, 30)
                final_external = set().union(*(cycle_edges(c) for c in changed))
                new_triangle = {edge(a, b), edge(a, 30), edge(b, 30)}
                edges = triangle_edges | new_triangle | final_external
                assert len(edges) == 62
                assert not ((triangle_edges | new_triangle) & final_external)
                adjacency = [set() for _ in range(31)]
                for u, v in edges:
                    assert u != v
                    adjacency[u].add(v)
                    adjacency[v].add(u)
                assert all(len(a_) == 4 for a_ in adjacency)
                assert sorted(len(c) for c in changed) == [4, 5, 5, 5, 5, 5]
                assert sorted(v for c in changed for v in c) == [v for v in range(31) if v not in (a, b)]
                key = tuple(sorted(edges))
                unique_graphs.add(key)
                nb = counts_nb3(adjacency)
                assert all(sum(row) == 36 for row in nb)
                assert all(nb[u][v] == nb[v][u] for u in range(31) for v in range(31))
                if not first_calibrated:
                    # One formal candidate, separately via the quartic polynomial N3=A^3-7A.
                    a2 = [[len(adjacency[u] & adjacency[v]) for v in range(31)] for u in range(31)]
                    polynomial = [[sum(a2[w][v] for w in adjacency[u]) - 7 * (v in adjacency[u])
                                   for v in range(31)] for u in range(31)]
                    assert polynomial == nb
                    (HERE / "first_calibration.json").write_text(json.dumps({
                        "status": "MATCH", "a": a, "b": b, "insertion_edge": insertion_edge,
                        "scope": "one formal candidate, all31 squared NB3 counts versus A^3-7A",
                        "counts": nb,
                    }, indent=2) + "\n")
                    first_calibrated = True
                missing = [(u, v) for u in range(31) for v in range(31)
                           if v not in adjacency[u] and nb[u][v] < (2 if u == v else 1)]
                actual_triangles = triangles(adjacency)
                triangle_histogram[len(actual_triangles)] += 1
                diagonal_histogram[tuple(sorted(Counter(nb[u][u] for u in range(31)).items()))] += 1
                histogram[len(missing)] += 1
                params = {"a": a, "b": b, "triangle_ids": [triangle_id[a], triangle_id[b]],
                          "external_cycle_ids": [ca, cb], "inserted_cycle": chosen_cycle,
                          "insertion_position": position, "insertion_edge": insertion_edge}
                summary = {"candidate_id": completed, "parameters": params,
                           "n": 31, "m": 62, "regular_degree": 4,
                           "actual_triangle_count": len(actual_triangles),
                           "missing_required_ordered_pairs": len(missing),
                           "first_missing_required_pair": missing[0] if missing else None}
                all_summaries.append(summary)
                detail = {**summary, "edges": key, "NB3_counts": nb,
                          "missing_required_pairs": missing, "actual_triangles": actual_triangles,
                          "external_cycles_after_insertion": changed}
                if not missing:
                    passers.append(detail)
                if best is None or len(missing) < best["missing_required_ordered_pairs"]:
                    best = detail
                completed += 1
    (HERE / "all_candidate_summaries.json").write_text(json.dumps(all_summaries, separators=(",", ":")) + "\n")
    (HERE / "passers.json").write_text(json.dumps(passers, separators=(",", ":")) + "\n")
    if best is not None:
        (HERE / "best_raw_coverage.json").write_text(json.dumps(best, indent=2) + "\n")
    terminal = {
        "status": "CPU_LIMIT_PARTIAL_FAMILY" if internal_limit else
                  "COMPLETE_FINITE_FAMILY_PASSERS_SAVED" if passers else "COMPLETE_FINITE_FAMILY_NO_RAW_NB3_PASSERS",
        "source_vertices": 30, "new_controller_vertices": 31, "new_controller_edges": 62,
        "eligible_unordered_pairs": len(pairs), "insertion_choices_per_pair": 8,
        "raw_candidates_planned": 8 * len(pairs), "raw_candidates_examined": completed,
        "unique_labeled_graphs_examined": len(unique_graphs),
        "all_examined_graphs_simple_four_regular": True,
        "required_pair_condition": "Every nonadjacent ordered pair including diagonal has raw NB3 count>=1; diagonal count>=2.",
        "raw_NB3_row_sum_each_graph": 36,
        "passers": len(passers), "best_missing_required_ordered_pairs": best["missing_required_ordered_pairs"] if best else None,
        "missing_required_pair_histogram": dict(sorted(histogram.items())),
        "actual_triangle_count_histogram": dict(sorted(triangle_histogram.items())),
        "diagonal_count_profile_histogram": [{"profile": list(k), "candidates": v} for k, v in diagonal_histogram.items()],
        "first_candidate_independent_polynomial_calibration": first_calibrated,
        "CPU_seconds": time.process_time() - began, "wall_seconds": time.monotonic() - wall,
        "CPU_internal_limit_seconds": 28, "CPU_hard_limit_seconds": 30,
        "workers": 1, "complete": not internal_limit,
        "q3_pattern_CSP_solved": False, "large_lift_generated": False,
        "full_BFS_performed": False, "new_lower_bounds": 0,
        "scope": "Only the specified different-triangle/different-C5 pair, two C5 suppressions, new shared triangle, insertion into one of its two C4s; no other cycles or arbitrary31 graphs.",
        "pending": [],
    }
    (HERE / "terminal.json").write_text(json.dumps(terminal, indent=2) + "\n")
    print(json.dumps(terminal, indent=2))


if __name__ == "__main__":
    main()
