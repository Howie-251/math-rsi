"""One fixed degree-11 variant; one independent final radius-four coverage BFS."""

from collections import Counter, deque
import json
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "pencil_source/deg11_diam5_n37628.txt"


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def limit_probe():
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))


def main():
    started, wall = time.process_time(), time.monotonic()
    child_before = children_cpu()
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "probe.cpp"),
                    "-o", str(HERE / "probe")], check=True)
    compile_cpu = children_cpu() - child_before
    before_probe = children_cpu()
    with (HERE / "run.stderr.txt").open("w") as output:
        done = subprocess.run([str(HERE / "probe"), str(SOURCE), str(HERE / "result.json")],
                              stdout=output, stderr=subprocess.STDOUT, preexec_fn=limit_probe)
    probe_cpu = children_cpu() - before_probe
    if done.returncode != 0:
        (HERE / "terminal.json").write_text(json.dumps({
            "status": "PROBE_PROCESS_TERMINATED_PARTIAL_UNKNOWN",
            "returncode": done.returncode, "probe_child_CPU_seconds": probe_cpu,
            "CPU_hard_limit_seconds": 90, "restarts": 0, "new_lower_bounds": 0,
        }, indent=2) + "\n")
        return
    result = json.loads((HERE / "result.json").read_text())
    result.update({"source": str(SOURCE.relative_to(HERE.parents[3])),
                   "base_degree_cap": 11, "prospective_order": 37629,
                   "pin_categories": ["global_largest_R4", "degree6", "degree7", "degree8",
                                      "degree9", "degree10", "last6_added", "prefix_before37622"],
                   "missing_category_fallback": "largest remaining global R4 ball",
                   "CPU_hard_limit_seconds": 90, "restarts": 0})
    check_start = time.process_time()
    # Read the source independently of C++ bitsets and perform one depth-four
    # multi-source BFS from the final saved neighbour set, only on failure.
    adjacency = []
    for line in SOURCE.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        row = list(map(int, line.split()))
        assert row[0] == len(adjacency)
        adjacency.append(row[1:])
    degrees = list(map(len, adjacency))
    eligible = [v for v, d in enumerate(degrees) if d < 11]
    profile = {
        "n": len(adjacency), "edges": sum(degrees) // 2,
        "degree_cap": 11, "degree_histogram": dict(sorted(Counter(degrees).items())),
        "eligible_count": len(eligible), "eligible_vertices": eligible,
        "all_vertex_degrees": degrees,
        "all_vertex_spare_degree": [11 - d for d in degrees],
        "total_spare_degree": sum(11 - d for d in degrees),
        "last6_vertex_degrees": {v: degrees[v] for v in range(37622, 37628)},
    }
    (HERE / "source_profile.json").write_text(json.dumps(profile, separators=(",", ":")) + "\n")
    neighbours = result["best_neighbors"]
    budget = {
        "new_vertex_degree": len(neighbours), "new_vertex_degree_cap": 11,
        "old_vertices_with_changed_degree": [{"vertex": v, "old_degree": degrees[v],
            "new_degree": degrees[v] + 1, "remaining_spare_degree": 10 - degrees[v]}
            for v in neighbours],
        "all_selected_eligible": all(degrees[v] < 11 for v in neighbours),
        "selected_vertices_unique": len(set(neighbours)) == len(neighbours),
        "all_old_new_degree_caps_satisfied": max(degrees) <= 11 and all(degrees[v] + 1 <= 11 for v in neighbours)
            and len(neighbours) <= 11,
    }
    result["degree_budget"] = budget
    check = {"performed": False, "reason": "Immediate hit; no independent BFS requested for a hit."}
    if result["best_uncovered_vertices"]:
        distance = [-1] * len(adjacency)
        queue = deque(neighbours)
        for v in neighbours:
            distance[v] = 0
        while queue:
            u = queue.popleft()
            if distance[u] == 4:
                continue
            for v in adjacency[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        missing = [v for v, d in enumerate(distance) if d < 0]
        assert missing == result["uncovered_vertices"]
        assert len(missing) == result["best_uncovered_vertices"]
        check = {
            "status": "MATCH", "performed": True, "BFS_runs": 1,
            "method": "One independent depth4 multi-source deque BFS on source adjacency; no saved bitset reused.",
            "sources": neighbours, "radius": 4, "covered_vertices": len(adjacency) - len(missing),
            "uncovered_count": len(missing), "uncovered_vertices": missing,
            "distance_to_selected_histogram_through4": dict(sorted(Counter(d for d in distance if d >= 0).items())),
            "degree_budget": budget, "full_source_BFS_performed": False,
        }
    check["CPU_seconds_including_source_read_and_budget"] = time.process_time() - check_start
    (HERE / "independent_cover_check.json").write_text(json.dumps(check, indent=2) + "\n")
    (HERE / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    terminal = {k: v for k, v in result.items() if k not in ("uncovered_vertices",)}
    terminal.update({
        "independent_final_cover_check": check.get("status", "NOT_PERFORMED_HIT"),
        "independent_multi_source_BFS_runs": int(check["performed"]),
        "compile_CPU_seconds": compile_cpu, "probe_child_CPU_seconds": probe_cpu,
        "driver_CPU_seconds": time.process_time() - started,
        "total_CPU_seconds_including_compile_and_check": children_cpu() - child_before + time.process_time() - started,
        "wall_seconds_including_compile_and_check": time.monotonic() - wall,
        "new_lower_bounds": 0, "full_template_excluded": False,
        "scope": "One fixed eight-pin degree11 profile: greedy up to11 neighbours and exactly one coordinate sweep per nonhit profile; no second batch.",
        "pending": [],
    })
    (HERE / "terminal.json").write_text(json.dumps(terminal, indent=2) + "\n")
    print(json.dumps({k: terminal[k] for k in ("status", "base_vertices", "base_edges", "eligible_vertices",
        "profiles_completed", "best_uncovered_vertices", "pins", "profile_final_misses", "best_neighbors",
        "independent_final_cover_check", "total_CPU_seconds_including_compile_and_check")}, indent=2))


if __name__ == "__main__":
    main()
