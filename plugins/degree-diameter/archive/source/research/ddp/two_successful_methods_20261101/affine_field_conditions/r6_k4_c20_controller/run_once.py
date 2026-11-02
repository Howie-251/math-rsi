#!/usr/bin/env python3
"""Single-worker driver; compilation and search share one 30 CPU-second budget."""
import json
import os
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
os.chdir(HERE)
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
start_self = time.process_time()
start_children = resource.getrusage(resource.RUSAGE_CHILDREN)
def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime - start_children.ru_utime - start_children.ru_stime

compiled = subprocess.run(["g++", "-std=c++17", "-O3", "-o", "search", "search.cpp"], capture_output=True, text=True)
(HERE / "COMPILE.log").write_text(compiled.stdout + compiled.stderr)
compile_cpu = child_cpu()
if compiled.returncode:
    raise SystemExit(compiled.returncode)
remaining = 29.5 - child_cpu() - (time.process_time() - start_self)
if remaining <= 0:
    raise SystemExit("Compilation exhausted the fixed CPU budget")
searched = subprocess.run(["./search", str(remaining)], capture_output=True, text=True)
(HERE / "SEARCH.log").write_text(searched.stdout + searched.stderr)
if searched.returncode:
    raise SystemExit(searched.returncode)
result = json.loads((HERE / "SEARCH_RESULT.json").read_text())
result.update({"compile_CPU_seconds": compile_cpu,
               "total_CPU_seconds": child_cpu() + time.process_time() - start_self,
               "total_CPU_budget_seconds": 30, "workers": 1,
               "controller_vertices": 80, "controller_degree": 6,
               "controller_edges": 240, "precomputed_words_per_base_root": 150,
               "required_translation_classes": 296,
               "required_ordered_same_or_nonadjacent_pairs": 5920,
               "fiber_generated": False, "BFS_calls": 0, "solver_calls": 0,
               "Lean_calls": 0, "old_graphs_revalidated": 0,
               "scope": "g01=1, other five shifts lexicographic in 1..19; no WLOG claim for all Z20 shifts"})
(HERE / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
