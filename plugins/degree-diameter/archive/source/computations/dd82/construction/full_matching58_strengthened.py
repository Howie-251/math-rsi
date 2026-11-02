"""One strengthened full-false-twin58 discovery run, without proof output.

Preparation preserves the original CNF body and appends 630 proved binary
clauses and all 11 conjugacy types for Q12. Solve is a separate action.
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import argparse
import json
import os
import resource
import shutil
import subprocess
import sys
import time

import full_matching58_prepare as original

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
SOURCE = BASE / "full_matching58_run"
OUT = BASE / "full_matching58_strengthened_run"
RUN_ID = "dd82-v3-f9-c7-20261013-0749"
CPU_SECONDS = 120
WALL_SECONDS = 240
MEMORY_BYTES = 4 * 1024**3


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def cycle_type(p):
    seen, lengths = set(), []
    for start in range(6):
        if start in seen:
            continue
        current, length = start, 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = p[current]
        assert current == start
        lengths.append(length)
    return tuple(sorted(lengths))


def representative(parts):
    p, start = list(range(6)), 0
    for size in parts:
        for a in range(start, start + size):
            p[a] = start + (a - start + 1) % size
        start += size
    assert start == 6 and cycle_type(p) == parts
    return p


def conjugate(p, sigma):
    result = [None] * 6
    for a in range(6):
        result[sigma[a]] = sigma[p[a]]
    return result


def clause_failures(path, values):
    count, failures = 0, []
    for line in path.read_text().splitlines():
        if line.startswith("p "):
            _, _, nv, nc = line.split()
            assert int(nv) == len(values)
        elif line and not line.startswith("c"):
            clause = list(map(int, line.split()))
            assert clause[-1] == 0
            count += 1
            if not any(values[abs(q)] == (q > 0) for q in clause[:-1]):
                failures.append(count)
    assert count == int(nc)
    return failures


def prepare():
    cpu, wall = time.process_time(), time.monotonic()
    assert 0 in os.sched_getaffinity(0)
    os.sched_setaffinity(0, {0})
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "input.cnf").exists(), "Preserve the prepared strengthened input"
    old = json.loads((SOURCE / "encoding.json").read_text())
    mapping = json.loads((SOURCE / "variables.json").read_text())
    edge_vars = {(i, a, j, b): q
                 for i, a, j, b, u, v, q in mapping["edge_variables"]}

    def edge(i, a, j, b):
        return edge_vars[i, a, j, b] if i < j else edge_vars[j, b, i, a]

    binary = []
    for i in range(1, 8):
        for a in range(6):
            targets = [j for j in range(1, 8) if j != i]
            for j, k in combinations(targets, 2):
                binary.append([-edge(i, a, j, a), -edge(i, a, k, a)])
    assert len(binary) == 630
    assert len({tuple(sorted(c)) for c in binary}) == 630

    all_permutations = list(permutations(range(6)))
    counts = Counter(cycle_type(p) for p in all_permutations)
    assert len(all_permutations) == 720 and len(counts) == 11
    types = sorted(counts)
    reps = [representative(parts) for parts in types]
    assert len({tuple(p) for p in reps}) == 11
    assert {cycle_type(p) for p in reps} == set(counts)
    selectors = [old["variables"] + i + 1 for i in range(11)]
    selector_clauses = [selectors[:]]
    selector_records = []
    for q, parts, p in zip(selectors, types, reps):
        selector_records.append(dict(variable=q, cycle_type=list(parts),
                                     permutation=p, labelled_type_count=counts[parts]))
        selector_clauses.extend([-q, edge(1, a, 2, p[a])] for a in range(6))
    assert len(selector_clauses) == 67
    additions = binary + selector_clauses
    nv, nc = old["variables"] + 11, old["clauses"] + len(additions)
    assert (nv, nc) == (37307, 116197)
    with (SOURCE / "input.cnf").open() as src, (OUT / "input.cnf").open("w") as dst:
        assert src.readline().split() == ["p", "cnf", "37296", "115500"]
        dst.write(f"p cnf {nv} {nc}\n")
        shutil.copyfileobj(src, dst)
        for clause in additions:
            dst.write(" ".join(map(str, clause)) + " 0\n")
    old_lines = (SOURCE / "input.cnf").read_text().splitlines()
    new_lines = (OUT / "input.cnf").read_text().splitlines()
    assert new_lines[1:1 + old["clauses"]] == old_lines[1:]
    assert len(new_lines) == nc + 1
    assert [list(map(int, s.split()[:-1])) for s in new_lines[1 + old["clauses"]:]] == additions
    save(OUT / "added_clauses.json", dict(
        original_clause_count=old["clauses"], root_binary_clauses=binary,
        selector_clauses=selector_clauses, new_variable_count=11,
        added_clause_count=697))
    save(OUT / "cycle_types.json", dict(
        enumerated_permutations=720, distinct_cycle_types=11,
        representative_algorithm="Sort cycle lengths, then cycle consecutive labels within each part",
        records=selector_records))
    mapping["selector_variables"] = selector_records
    save(OUT / "variables.json", mapping)
    shutil.copyfile(SOURCE / "coverage.json", OUT / "coverage.json")

    # Relabel every fibre by the same sigma. No fixed scaffold label moves.
    edges = original.read_edges(SOURCE / "seed.edges")
    old_interfaces = original.interfaces_from_edges(edges)
    seed_p = next(item["permutation"] for item in old_interfaces if (item["i"], item["j"]) == (1, 2))
    wanted = representative(cycle_type(seed_p))
    sigma = next(s for s in all_permutations if conjugate(seed_p, s) == wanted)

    def relabel(x):
        return x if x < 10 else 10 + 6*((x-10)//6) + sigma[(x-10) % 6]

    seed = {tuple(sorted((relabel(u), relabel(v)))) for u, v in edges}
    interfaces = original.interfaces_from_edges(seed)
    assert next(item["permutation"] for item in interfaces if (item["i"], item["j"]) == (1, 2)) == wanted
    (OUT / "seed.edges").write_text("58 232\n" + "".join(f"{u} {v}\n" for u, v in sorted(seed)))
    save(OUT / "seed.json", dict(n=58, edges=sorted(seed), source=str(SOURCE / "seed.edges"),
        common_coordinate_relabelling=list(sigma), role="failed seed only; not fixed in CNF"))
    save(OUT / "seed.interfaces.json", dict(interfaces=interfaces))
    values = {q: (u, v) in seed for i, a, j, b, u, v, q in mapping["edge_variables"]}
    for q, p, r in mapping["and_variables"]:
        values[q] = values[p] and values[r]
    for item in selector_records:
        values[item["variable"]] = item["permutation"] == wanted
    assert set(values) == set(range(1, nv+1))
    failures = clause_failures(OUT / "input.cnf", values)
    covered = {item["clause_id"]: item["pair"]
               for item in json.loads((OUT / "coverage.json").read_text())}
    assert all(q in covered for q in failures)
    previous = json.loads((SOURCE / "seed.cnf_check.json").read_text())
    translated_pairs = sorted(sorted((relabel(u), relabel(v))) for u, v in previous["false_pairs"])
    assert sorted(covered[q] for q in failures) == translated_pairs
    assert len(failures) == 105
    (OUT / "seed.assignment.txt").write_text("v " + " ".join(str(q if values[q] else -q) for q in range(1, nv+1)) + " 0\n")
    save(OUT / "sanity.json", dict(
        preserved_original_clause_body=True, checked_actual_added_clauses=697,
        root_binary_clauses=630, conjugacy_selector_clauses=67,
        permutations_checked=720, cycle_types=11, all_types_retained=True,
        seed_coordinate_relabelling=list(sigma), seed_q12=wanted,
        seed_added_clauses_all_satisfied=True,
        seed_false_clause_count=105, false_clause_ids=failures,
        false_pairs=sorted(covered[q] for q in failures),
        old_failed_pairs_preserved_under_relabelling=True,
        new_bfs_runs=0, solver_calls=0))
    record = dict(old)
    record.update(parent_run_id=RUN_ID, status="PREPARED_NOT_RUN", solver_calls=0,
        original_input=str(SOURCE / "input.cnf"), variables=nv, clauses=nc,
        extra_variables=11, extra_clauses=697,
        added_root_binary_clauses=630, added_selector_clauses=67,
        normalization="Root Q0j=I plus Q12 in all 11 S6 conjugacy representatives; no group action",
        discovery_only=True, proof_output_enabled=False,
        preparation_cpu_seconds=time.process_time()-cpu,
        preparation_wall_seconds=time.monotonic()-wall)
    record["clause_groups"] = dict(old["clause_groups"], root_neighbour_matching=630, conjugacy_representatives=67)
    record["cnf_bytes"] = (OUT / "input.cnf").stat().st_size
    save(OUT / "encoding.json", record)
    print(json.dumps({k: record[k] for k in ["status", "variables", "clauses", "extra_variables", "extra_clauses", "preparation_cpu_seconds", "preparation_wall_seconds"]}))


def bounded(command, log, seconds, wall_seconds):
    pin = 0
    assert pin in os.sched_getaffinity(0)

    def limits():
        os.sched_setaffinity(0, {pin})
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds+1))
        resource.setrlimit(resource.RLIMIT_AS, (MEMORY_BYTES, MEMORY_BYTES))

    before, start = resource.getrusage(resource.RUSAGE_CHILDREN), time.monotonic()
    with log.open("w") as output:
        try:
            rc = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT,
                                preexec_fn=limits, timeout=wall_seconds).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command, exit_code=rc, cpu_budget_seconds=seconds,
        wall_budget_seconds=wall_seconds, threads=1, pinned_cpu=pin,
        cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-start)


def decode(log):
    # The old decoder checks all assigned variables and all actual clauses,
    # then uses only primary edge variables to expand the complete graph.
    original.OUT = OUT
    original.decode(log)


def solve():
    assert not (OUT / "launch.json").exists(), "Only one authorized strengthened solver call"
    enc = json.loads((OUT / "encoding.json").read_text())
    assert enc["status"] == "PREPARED_NOT_RUN"
    solver = ROOT / ".tools/lean-4.24.0-linux/bin/cadical"
    command = [str(solver), "-t", str(CPU_SECONDS), str(OUT / "input.cnf")]
    save(OUT / "launch.json", dict(parent_run_id=RUN_ID, command=command,
        cpu_budget_seconds=CPU_SECONDS, wall_budget_seconds=WALL_SECONDS,
        threads=1, memory_limit_bytes=MEMORY_BYTES, proof_output_enabled=False,
        solver_calls=1, retained_internal_solver_state=False,
        change_from_prior="630 redundant binary cuts plus all 11 Q12 conjugacy representatives; proof logging disabled"))
    result = bounded(command, OUT / "solver.log", CPU_SECONDS, WALL_SECONDS)
    rc = result["exit_code"]
    result.update(parent_run_id=RUN_ID, scope=enc["scope"], solver_calls=1,
        variables=enc["variables"], clauses=enc["clauses"],
        proof_output_enabled=False, proof_checked=False, retained_internal_solver_state=False,
        status={10: "SAT_CANDIDATE", 20: "RAW_UNSAT", 0: "UNKNOWN",
                None: "WALL_LIMIT_UNKNOWN", -9: "CPU_LIMIT_UNKNOWN", -24: "CPU_LIMIT_UNKNOWN"}
                .get(rc, "PROCESS_FAILURE_UNKNOWN"))
    save(OUT / "result.json", result)
    print(json.dumps(result), flush=True)
    if rc == 10:
        result["decode_process"] = bounded(
            [sys.executable, str(Path(__file__).resolve()), "decode", "--log", str(OUT / "solver.log")],
            OUT / "decode.log", 10, 20)
        assert result["decode_process"]["exit_code"] == 0
        result["independent_bfs_process"] = bounded(
            [sys.executable, str(BASE / "false_twins58_f9_independent_bfs.py"),
             str(OUT / "candidate.edges"), str(OUT / "candidate.independent_bfs.json")],
            OUT / "independent_bfs.log", 10, 20)
        assert result["independent_bfs_process"]["exit_code"] == 0
        result["independent_graph_check"] = json.loads((OUT / "candidate.independent_bfs.json").read_text())
        result["status"] = "VERIFIED_TARGET" if result["independent_graph_check"]["valid_target"] else "SAT_DECODE_FAILED_TARGET_CHECK"
    elif rc == 20:
        result["mathematical_conclusion"] = "None: UNSAT is unverified because this discovery run emitted no proof"
    else:
        result["mathematical_conclusion"] = "None: UNKNOWN does not decide the family"
    save(OUT / "result.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "solve", "decode"])
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    if args.action == "prepare":
        prepare()
    elif args.action == "solve":
        solve()
    else:
        assert args.log is not None
        decode(args.log)
