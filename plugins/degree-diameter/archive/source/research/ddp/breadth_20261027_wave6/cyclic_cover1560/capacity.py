"""First self-slot obstruction for the saved120 source, ordinary C13 cover."""

import json
from pathlib import Path
import resource
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "context/DD_PORTFOLIO_START_20261026/baselines/d6_D3_known.edges"


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (18, 18))
    started = time.process_time()
    rows = [list(map(int, line.split())) for line in SOURCE.read_text().splitlines() if line.strip()]
    n, m = rows[0]
    edges = [tuple(edge) for edge in rows[1:]]
    assert (n, m) == (120, 360) and len(edges) == 360
    parent = list(range(n))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    tree = []
    for e, (u, v) in enumerate(edges):
        assert 0 <= u < v < n
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
            tree.append(e)
    tree_set = set(tree)
    free = [e for e in range(m) if e not in tree_set]
    assert len(tree) == 119 and len(free) == 241
    adjacency = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        adjacency[u].append((v, e, 1))
        adjacency[v].append((u, e, -1))
    assert all(len(a) == 6 for a in adjacency)
    (HERE / "tree_gauge.json").write_text(json.dumps({
        "source": str(SOURCE.relative_to(ROOT)), "edges": edges,
        "tree_edge_ids": tree, "free_edge_ids": free,
        "orientation": "u<v is positive; reverse edge subtracts the same voltage",
        "gauge_completeness": "For fixed endpoints, differences are circulations. A circulation supported only on a spanning tree is zero overF13, so deleting tree coordinates loses no distinct voltage functions.",
    }, indent=2) + "\n")
    total_walks, root_summaries, obstruction = 0, [], None
    for root in range(n):
        functions = {}
        coefficients, walk = {}, [root]
        walks = 0

        def visit(u, depth):
            nonlocal walks
            walks += 1
            if u == root:
                key = tuple(sorted((e, c % 13) for e, c in coefficients.items()))
                if key not in functions or len(walk) < len(functions[key]):
                    functions[key] = list(walk)
            if depth == 5:
                return
            for v, e, sign in adjacency[u]:
                if e not in tree_set:
                    coefficients[e] = coefficients.get(e, 0) + sign
                    if not coefficients[e]:
                        del coefficients[e]
                walk.append(v)
                visit(v, depth + 1)
                walk.pop()
                if e not in tree_set:
                    coefficients[e] = coefficients.get(e, 0) - sign
                    if not coefficients[e]:
                        del coefficients[e]

        visit(root, 0)
        assert walks == 9331
        total_walks += walks
        summary = {"source": root, "target": root, "walk_length_range": [0, 5],
                   "all_walks_visited_from_root": walks,
                   "mod13_distinct_self_voltage_functions": len(functions)}
        root_summaries.append(summary)
        if len(functions) < 13:
            obstruction = {**summary, "required_sheet_states": 13,
                "forms": [{"free_edge_terms_mod13": terms,
                    "signed_integer_free_terms": [(e, c if c <= 6 else c - 13) for e, c in terms],
                    "representative_walk": rep, "length": len(rep) - 1}
                    for terms, rep in sorted(functions.items())],
                "proof": "Every lifted walk of length<=5 from(root,0) to the same base fiber has voltage equal to one of these functions. Any voltage assignment therefore reaches at most this many of13 sheet states."}
            break
        if time.process_time() - started > 15:
            break
    if obstruction is not None:
        (HERE / "capacity_witness.json").write_text(json.dumps(obstruction, indent=2) + "\n")
    status = "CAPACITY_FAIL_SELF_SLOT_NO_SEARCH" if obstruction else "SELF_SLOTS_PASS_ONLY_FULL_TARGET_CAPACITY_NOT_YET_RUN"
    terminal = {
        "status": status, "source": str(SOURCE.relative_to(ROOT)), "n_base": n, "m_base": m,
        "source_BFS_reused": "context/DD_PORTFOLIO_START_20261026/validation/d6_D3_bfs.json",
        "base_min_degree": 6, "base_max_degree": 6, "cover_sheets": 13,
        "prospective_order": 1560, "target_degree": 6, "target_diameter": 5,
        "saved_threshold": 1518, "tree_edges": 119, "free_voltage_edges": 241,
        "self_slots_checked": len(root_summaries), "root_self_summaries": root_summaries,
        "raw_walks_enumerated": total_walks, "walks_per_complete_root": 9331,
        "all_short_walks_including_immediate_reverse_enumerated": True,
        "voltage_profile_started": False, "voltage_starts_generated": 0, "single_edge_proposals": 0,
        "best_cover_generated": False, "BFS_performed": False, "new_lower_bounds": 0,
        "CPU_seconds": time.process_time() - started, "workers": 1,
        "CPU_hard_limit_seconds": 18, "total_task_CPU_budget_seconds": 20,
        "scope": "Ordinary C13 covers of this fixed saved120 graph, preserving all base edges and adding no extra fiber edges.",
        "pending": [] if obstruction else ["full_target_capacity"]}
    (HERE / "terminal.json").write_text(json.dumps(terminal, indent=2) + "\n")
    print(json.dumps(terminal, indent=2))


if __name__ == "__main__":
    main()
