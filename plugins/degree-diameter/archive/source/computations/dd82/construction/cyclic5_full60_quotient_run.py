"""Compile/run one bounded integer quotient trajectory; no voltage solving."""
from itertools import combinations
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "computations/dd82/construction"
OUT = BASE / "cyclic5_full60_quotient_run"
RUN_ID = "dd82-v3-c5-full60-20261013"
TOTAL_CPU = 60
TOTAL_WALL = 120


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def describe(m):
    assert len(m) == 12 and all(len(row) == 12 for row in m)
    assert all(m[a][b] == m[b][a] for a in range(12) for b in range(12))
    assert all(sum(row) == 8 for row in m)
    assert all(m[a][a] in (0, 2) for a in range(12))
    assert all(0 <= m[a][b] <= 3 for a in range(12) for b in range(12) if a != b)
    d = [[sum(m[a][k]*m[k][b] for k in range(12)) + m[a][b] - 5 - 7*(a == b)
          for b in range(12)] for a in range(12)]
    assert all(sum(row) == 5 for row in d)
    zeros = [a for a in range(12) if m[a][a] == 0]
    row_types = [dict(orbit=a, internal_degree=m[a][a],
        external_multiplicities=sorted((m[a][b] for b in range(12) if b != a and m[a][b]), reverse=True),
        external_square_sum=sum(m[a][b]**2 for b in range(12) if b != a),
        diagonal_defect=d[a][a]) for a in range(12)]
    negative = [[a,b,d[a][b]] for a in range(12) for b in range(12) if d[a][b] < 0]
    double_edges = [[a,b] for a,b in combinations(range(12), 2) if m[a][b] == 2]
    unseen, components = set(range(12)), []
    while unseen:
        start = min(unseen); stack = [start]; vertices = set()
        while stack:
            a = stack.pop()
            if a in vertices: continue
            vertices.add(a); unseen.discard(a)
            stack.extend(b for b in range(12) if b != a and m[a][b] == 2 and b not in vertices)
        edges = [e for e in double_edges if e[0] in vertices]
        degrees = [sum(m[a][b] == 2 for b in vertices if b != a) for a in vertices]
        odd_cycle = len(vertices) % 2 == 1 and len(vertices) >= 3 and all(x == 2 for x in degrees)
        components.append(dict(vertices=sorted(vertices), edges=edges, odd_cycle_component=odd_cycle))
    triangles = [list(t) for t in combinations(range(12), 3)
                 if all(m[a][b] > 0 for a,b in combinations(t,2))]
    return dict(matrix=m, defect=d, independent_orbits=zeros, row_types=row_types,
        negative_defect_entries=negative, negative_defect_sum=-sum(x[2] for x in negative),
        score=-sum(x[2] for x in negative)+8*max(0,2-len(zeros))
              +2*sum(c["odd_cycle_component"] for c in components),
        base_quotient_conditions_pass=not negative and len(zeros) >= 2,
        within_orbit_difference_condition_pass=not any(c["odd_cycle_component"] for c in components),
        quotient_conditions_pass=not negative and len(zeros) >= 2
                                 and not any(c["odd_cycle_component"] for c in components),
        all_even_rows=[a for a in range(12) if all(x % 2 == 0 for x in m[a])],
        support_triangles=triangles, support_triangle_count=len(triangles),
        multiplicity_weighted_triangle_count=sum(m[a][b]*m[a][c]*m[b][c] for a,b,c in triangles),
        double_interface_components=components,
        double_interface_odd_cycle_component_count=sum(c["odd_cycle_component"] for c in components))


def main():
    start_cpu, start_children, start_wall = time.process_time(), child_cpu(), time.monotonic()
    assert 1 in os.sched_getaffinity(0)
    os.sched_setaffinity(0, {1})
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "launch.json").exists(), "One authorized quotient trajectory only"
    source = BASE / "cyclic5_twelve_orbits60_signature_lift_run/seed20/voltages.json"
    voltages = json.loads(source.read_text())
    initial = [[len(cell) for cell in row] for row in voltages["shifts"]]
    initial_info = describe(initial)
    assert initial_info["independent_orbits"] == []
    assert initial_info["negative_defect_entries"] == []
    assert all(initial[a][b] <= 1 for a,b in combinations(range(12),2))
    save(OUT / "initial.json", initial_info)
    (OUT / "input.txt").write_text("\n".join(" ".join(map(str,row)) for row in initial)+"\n")
    save(OUT / "launch.json", dict(run_id=RUN_ID, source=str(source),
        cpu=1, threads=1, total_cpu_budget_seconds=TOTAL_CPU, total_wall_budget_seconds=TOTAL_WALL,
        includes_compile_and_parent_cpu=True, trajectories=1, rng_seed=20261013,
        state_resets=0, solver_calls=0, voltage_search=False,
        score="sum of all negative D entries in absolute value + 8*max(0,2-independent_orbits) + 2*odd q=2 cycle components",
        hard_domain="symmetric M, row sums 8, diagonal 0/2, off-diagonal 0..3",
        temperature="3.5 to 0.25 exponentially over the one trajectory; no restart"))
    before = child_cpu()
    compiled = subprocess.run(["g++", "-O3", "-std=c++17", str(BASE / "cyclic5_full60_quotient_search.cpp"),
                               "-o", str(OUT / "search.bin")], capture_output=True, text=True, timeout=30)
    compile_cpu = child_cpu()-before
    (OUT / "compile.log").write_text(compiled.stdout+compiled.stderr)
    assert compiled.returncode == 0
    remaining_cpu = TOTAL_CPU - (child_cpu()-start_children) - (time.process_time()-start_cpu) - 2
    remaining_wall = TOTAL_WALL - (time.monotonic()-start_wall) - 2
    assert remaining_cpu > 0 and remaining_wall > 0

    def limits():
        os.sched_setaffinity(0, {1})
        cap = max(1, math.ceil(remaining_cpu))
        resource.setrlimit(resource.RLIMIT_CPU, (cap, cap+1))
        resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))

    command = [str(OUT / "search.bin"), str(OUT / "input.txt"), str(OUT / "search.json"),
               str(remaining_cpu), str(remaining_wall)]
    before, search_wall = child_cpu(), time.monotonic()
    with (OUT / "search.log").open("w") as output:
        try:
            rc = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT,
                preexec_fn=limits, timeout=remaining_wall+1).returncode
        except subprocess.TimeoutExpired:
            rc = None
    search_cpu, search_wall = child_cpu()-before, time.monotonic()-search_wall
    result = dict(run_id=RUN_ID, exit_code=rc, command=command, cpu=1, threads=1,
        compile_cpu_seconds=compile_cpu, search_process_cpu_seconds=search_cpu,
        search_process_wall_seconds=search_wall, solver_calls=0, voltage_search=False,
        complete_enumeration=False)
    if rc == 0:
        actual = json.loads((OUT / "search.json").read_text())
        best = describe(actual["best_matrix"])
        last = describe(actual["last_matrix"])
        assert best["defect"] == actual["best_defect"]
        assert best["score"] == actual["best_score"]
        assert last["defect"] == actual["last_defect"]
        assert last["score"] == actual["last_score"]
        assert best["quotient_conditions_pass"] == actual["found"]
        best.update(run_id=RUN_ID, source="one continuous quotient trajectory",
            changed_from_initial=best["matrix"] != initial,
            matrix_l1_change=sum(abs(best["matrix"][a][b]-initial[a][b]) for a in range(12) for b in range(12)),
            voltage_assignment_performed=False, is_complete_60_vertex_graph=False)
        if actual["found"]:
            assert best["changed_from_initial"] and not best["all_even_rows"]
        save(OUT / "best_quotient.json", best)
        save(OUT / "last_quotient.json", last)
        result.update(found=actual["found"], stop_reason=actual["stop_reason"],
            proposals=actual["proposals"], accepted=actual["accepted"],
            accepted_uphill=actual["accepted_uphill"], best_score=actual["best_score"],
            independent_orbits=best["independent_orbits"],
            double_interface_odd_cycle_component_count=best["double_interface_odd_cycle_component_count"],
            status="QUOTIENT_FOUND_NOT_LIFTED" if actual["found"] else "BUDGET_ENDED_NO_FEASIBLE_QUOTIENT")
    else:
        result["status"] = "PROCESS_LIMIT_OR_FAILURE_NO_CONCLUSION"
    result.update(parent_cpu_seconds=time.process_time()-start_cpu,
        total_cpu_seconds=child_cpu()-start_children+time.process_time()-start_cpu,
        total_wall_seconds=time.monotonic()-start_wall)
    save(OUT / "resources.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
