#!/usr/bin/env python3
"""One current-graph guard model; reuse the established coverage producer."""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
PRED = json.loads((HERE / "PREDICTION.json").read_text())
START = time.process_time()
WALL = time.monotonic()
child0 = resource.getrusage(resource.RUSAGE_CHILDREN)
assert not (HERE / "TERMINAL.json").exists(), "This fixed batch already finished"
source = PROJECT / PRED["source_graph"]
native = PROJECT / "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/cover"
solver = PROJECT / ".tools/lean-4.24.0-linux/bin/cadical"
pins = PRED["mandatory_pins"]
(HERE / "mandatory.pins.txt").write_text(" ".join(map(str, pins)) + "\n")


def run(command, stage, output, wall_limit, cpu_limit=None):
    def limits():
        if cpu_limit:
            resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit + 1))
    with (HERE / output).open("w") as log:
        p = subprocess.Popen(command, stdout=log, stderr=log, cwd=PROJECT, preexec_fn=limits)
        handle = dict(stage=stage, status="RUNNING", pid=p.pid, command=[str(x) for x in command])
        (HERE / "HANDLE.json").write_text(json.dumps(handle, indent=2) + "\n")
        print(json.dumps(handle), flush=True)
        timed_out = False
        try:
            code = p.wait(timeout=wall_limit)
        except subprocess.TimeoutExpired:
            timed_out = True
            p.kill()
            code = p.wait()
    handle.update(status="TERMINAL", exit_code=code, observation_wall_timeout=timed_out)
    (HERE / (stage + "_TERMINAL.json")).write_text(json.dumps(handle, indent=2) + "\n")
    (HERE / "HANDLE.json").write_text(json.dumps(handle, indent=2) + "\n")
    return code


def finish(status, **fields):
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    child_cpu = children.ru_utime + children.ru_stime - child0.ru_utime - child0.ru_stime
    result = dict(status=status, prototype=4580, source_n=51457, new_graphs=0,
                  source_allroot_BFS=0, child_CPU_seconds=child_cpu,
                  driver_CPU_seconds=time.process_time()-START,
                  aggregate_CPU_seconds=child_cpu+time.process_time()-START,
                  wall_seconds=time.monotonic()-WALL, **fields)
    (HERE / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    (HERE / "TERMINAL.json").write_text(json.dumps(result, indent=2) + "\n")
    (HERE / "HANDLE.json").write_text(json.dumps(dict(status="TERMINAL", result="RESULT.json")) + "\n")
    print(json.dumps(result), flush=True)


code = run([str(native), "prepare", str(source), str(HERE / "mandatory.pins.txt"), str(HERE / "prepared"), "13"],
           "PREPARE", "prepare.log", 20)
if code:
    finish("PREPARE_FAILED", exit_code=code)
    raise SystemExit(0)
r = json.loads((HERE / "prepared.json").read_text())
assert r["source_n"] == 51457 and r["source_m"] == 324863
print(json.dumps({k: r[k] for k in ["missing_count", "eligible_anchors", "unique_nonzero_masks", "zero_cover_targets", "exact_two_complete", "exact_one_or_two_found", "CPU_seconds"]}), flush=True)
if r["zero_cover_targets"]:
    finish("UNCOVERABLE_TARGET", targets=r["zero_cover_targets"], solver_calls=0)
    raise SystemExit(0)
if r["exact_one_or_two_found"]:
    guards = r["exact_anchors"]
else:
    import numpy as np
    K, N = len(r["representatives"]), r["missing_count"]
    raw = np.fromfile(HERE / "prepared.masks.u64.bin", dtype=np.uint8).reshape(K, r["mask_words_per_row"] * 8)
    cover = np.unpackbits(raw, axis=1, bitorder="little")[:, :N]
    cnf_body = HERE / "cover.clauses"
    clauses = 0
    with cnf_body.open("w") as out:
        for t in range(N):
            row = np.flatnonzero(cover[:, t]) + 1
            out.write(" ".join(map(str, row)) + " 0\n")
            clauses += 1
        # Prefix counters s(i,j): at least j selected among positions <=i.
        # Forward implications and overflow forbid any fifth selected guard.
        bound = 4
        def s(i, j):
            return K + (i - 1) * bound + j
        for i in range(1, K + 1):
            out.write(f"{-i} {s(i,1)} 0\n")
            clauses += 1
            if i > 1:
                for j in range(1, bound + 1):
                    out.write(f"{-s(i-1,j)} {s(i,j)} 0\n")
                    clauses += 1
                for j in range(2, bound + 1):
                    out.write(f"{-i} {-s(i-1,j-1)} {s(i,j)} 0\n")
                    clauses += 1
                out.write(f"{-i} {-s(i-1,bound)} 0\n")
                clauses += 1
    cnf = HERE / "cover.cnf"
    with cnf.open("wb") as out:
        out.write(f"p cnf {K*5} {clauses}\n".encode())
        with cnf_body.open("rb") as inp:
            while chunk := inp.read(1024*1024):
                out.write(chunk)
    model = dict(status="CNF_READY", source_n=51457, missing_targets=N, binary_guard_selectors=K,
                 prefix_counter_variables=K*4, total_variables=K*5, clauses=clauses,
                 guards_limit=4, constraints="every actual remaining currenttarget covered; <=4 independent currentfree guards",
                 identical_mask_representatives="least eligible label; duplicate masks cannot improve any cover",
                 solver="existing bundled CaDiCaL", solver_calls=1,
                 wall_limit_seconds=60, hard_CPU_limit_seconds=70,
                 encoding_CPU_seconds=time.process_time()-START)
    (HERE / "MODEL.json").write_text(json.dumps(model, indent=2) + "\n")
    print(json.dumps(model), flush=True)
    code = run([str(solver), "-q", "-t", "60", str(cnf)], "SAT", "solver.stdout", 75, 70)
    if code != 10:
        finish("RAW_UNSAT_UNCERTIFIED" if code == 20 else "UNKNOWN", solver_exit_code=code, solver_calls=1)
        raise SystemExit(0)
    values = []
    for line in (HERE / "solver.stdout").read_text().splitlines():
        if line.startswith("v "):
            values.extend(int(x) for x in line[2:].split() if int(x) > 0)
    chosen = [x-1 for x in values if x <= K]
    guards = [r["representatives"][i] for i in chosen]
    assert len(guards) <= 4 and np.all(np.any(cover[chosen], axis=0))

selected = sorted(pins + guards)
assert len(selected) == len(set(selected)) <= 13
(HERE / "selected.pins.txt").write_text(" ".join(map(str, selected)) + "\n")
code = run([str(native), "verify", str(source), str(HERE / "selected.pins.txt"), str(HERE / "selected"), "13"],
           "SELECTED_R4", "selected.log", 15)
assert code == 0
checked = json.loads((HERE / "selected.json").read_text())
assert checked["missing_count"] == 0
hit = dict(prototype=4580, omitted_saturated_pin=45089, mandatory=pins, guards=guards,
           full_neighbor_set=selected, current_source_n=51457, current_source_m=324863,
           selected_R4_covered=51457, selected_R4_missing=0,
           selected_old_degrees=checked["pin_current_degrees"], n=51458, m=324863+len(selected),
           new_vertex=51457, max_degree=13, diameter_at_most=5, all_old_edges_retained=True)
(HERE / "HIT.json").write_text(json.dumps(hit, indent=2) + "\n")
destination = HERE / "graph_d13_D5_n51458.edges"
with source.open() as inp, destination.open("w") as out:
    header = tuple(map(int, inp.readline().split()))
    assert header == (51457, 324863)
    out.write(f"51458 {hit['m']}\n")
    for line in inp:
        out.write(line)
    for v in selected:
        out.write(f"{v} 51457\n")
finish("COMPLETE_NEW_GRAPH_NEEDS_INDEPENDENT_NEWROOT_CHECK", guards=guards,
       full_neighbor_set=selected, graph_file=str(destination), produced_graphs=1,
       n=51458, m=hit["m"], solver_calls=0 if r["exact_one_or_two_found"] else 1)
