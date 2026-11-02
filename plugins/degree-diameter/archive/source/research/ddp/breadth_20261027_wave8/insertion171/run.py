"""Prepare from existing170 source/path caches, then one finite native enumeration."""

import json
import math
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "breadth_20261027_wave7/signed_double340"


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    started, wall, children = time.process_time(), time.monotonic(), child_cpu()
    rows = [list(map(int, s.split())) for s in (SOURCE / "source.edges").read_text().splitlines() if s.strip()]
    assert rows[0] == [170, 595]
    edges = [tuple(e) for e in rows[1:]]
    edge_id = {e: i for i, e in enumerate(edges)}
    distances = json.loads((SOURCE / "source_distances.json").read_text())
    with (HERE / "source_b2.txt").open("w") as out:
        for row in distances:
            words = [0, 0, 0]
            for v, d in enumerate(row):
                if d <= 2:
                    words[v // 64] |= 1 << (v % 64)
            out.write(" ".join(map(str, words)) + "\n")
    cache = json.loads((SOURCE / "distance3_paths.json").read_text())
    assert len(cache) == 10350
    with (HERE / "paths.txt").open("w") as out:
        out.write("10350\n")
        for item in cache:
            u, v = item["pair"]
            assert distances[u][v] == 3 and len(item["paths"]) == item["NB3_path_count"]
            out.write(f"{u} {v} {len(item['paths'])}\n")
            for path in item["paths"]:
                assert path[0] == u and path[-1] == v
                support = [edge_id[tuple(sorted((a, b)))] for a, b in zip(path, path[1:])]
                out.write(" ".join(map(str, support)) + "\n")
    preparation = time.process_time() - started
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "search.cpp"), "-o", str(HERE / "search")], check=True)
    compiled = child_cpu()
    compile_cpu = compiled - children
    hard = max(1, math.floor(15 - compile_cpu - (time.process_time() - started) - 0.1))
    internal = max(0.1, hard - 1)

    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    with (HERE / "production.log").open("w") as out:
        completed = subprocess.run([str(HERE / "search"), str(HERE), str(SOURCE / "source.edges"), str(internal)],
                                   stdout=out, stderr=subprocess.STDOUT, preexec_fn=limit)
    result_file = HERE / "search_result.json"
    d = json.loads(result_file.read_text()) if result_file.exists() else {"status": "PROCESS_TERMINATED_INCOMPLETE_UNKNOWN"}
    d.update({"process_returncode": completed.returncode, "preparation_CPU_seconds": preparation,
              "compile_CPU_seconds": compile_cpu, "search_process_CPU_seconds": child_cpu() - compiled,
              "driver_CPU_seconds": time.process_time() - started,
              "total_CPU_seconds_including_prep_compile_search": child_cpu() - children + time.process_time() - started,
              "wall_seconds": time.monotonic() - wall, "total_CPU_budget_seconds": 15,
              "search_process_CPU_hard_limit_seconds": hard, "workers": 1, "restarts": 0,
              "identical_profile_found_in_limited_history_search": False,
              "source": "wave7/signed_double340/source.edges", "source_path_cache_reused": True,
              "source_BFS_rerun": False, "new_lower_bounds": 0,
              "pending": ["root_unique_selected171_all_source_BFS"]})
    (HERE / "terminal.json").write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
