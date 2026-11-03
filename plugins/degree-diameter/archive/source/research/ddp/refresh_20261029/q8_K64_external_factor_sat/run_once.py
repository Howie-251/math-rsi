#!/usr/bin/env python3
"""A single exact auxiliary graph model for the q8 fibre construction."""
from pathlib import Path
import json
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
assert not (HERE / "TERMINAL.json").exists(), "This fixed batch has finished"
START = time.process_time()
WALL = time.monotonic()
children0 = resource.getrusage(resource.RUSAGE_CHILDREN)
body = (HERE / "clauses.tmp").open("w")
variables = clauses = 0
and_cache = {}


def fresh():
    global variables
    variables += 1
    return variables


def clause(values):
    global clauses
    if any(x is True for x in values):
        return
    values = [x for x in values if x is not False]
    body.write(" ".join(map(str, values)) + " 0\n")
    clauses += 1


def neg(x):
    return not x if isinstance(x, bool) else -x


def both(a, b):
    if a is False or b is False:
        return False
    if a is True:
        return b
    if b is True or a == b:
        return a
    key = tuple(sorted((a, b)))
    if key in and_cache:
        return and_cache[key]
    out = fresh()
    and_cache[key] = out
    clause([-out, a])
    clause([-out, b])
    clause([out, -a, -b])
    return out


def either(values):
    if any(x is True for x in values):
        return True
    values = sorted(set(x for x in values if x is not False))
    if not values:
        return False
    if len(values) == 1:
        return values[0]
    out = fresh()
    clause([-out] + values)
    for x in values:
        clause([out, -x])
    return out


adj = [[False] * 64 for _ in range(64)]
edge_vars = {}
for u in range(64):
    for v in range(u + 1, 64):
        if u // 8 == v // 8:
            adj[u][v] = adj[v][u] = ((u ^ v) in (1, 2, 4))
        else:
            q = fresh()
            edge_vars[(u, v)] = q
            adj[u][v] = adj[v][u] = q
assert len(edge_vars) == 1792
for u in range(64):
    xs = [adj[u][v] for v in range(64) if u // 8 != v // 8]
    # At least two: some selected, and a selected edge requires another.
    clause(xs)
    for x in xs:
        clause([-x] + [y for y in xs if y != x])
    # At most two via prefix counters.
    previous = None
    for x in xs:
        one, two = fresh(), fresh()
        clause([-x, one])
        if previous is None:
            clause([-two])
        else:
            p1, p2 = previous
            clause([-p1, one])
            clause([-p2, two])
            clause([-x, -p1, two])
            clause([-x, -p2])
        previous = (one, two)
clause([edge_vars[(0, 8)]])
clause([edge_vars[(0, 16)]])

r2 = [[True if u == v else False for v in range(64)] for u in range(64)]
for u in range(64):
    for v in range(u + 1, 64):
        terms = [adj[u][v]]
        terms.extend(both(adj[u][w], adj[w][v]) for w in range(64) if w not in (u, v))
        r2[u][v] = r2[v][u] = either(terms)
target_pairs = 0
for u in range(64):
    for v in range(u + 1, 64):
        if u // 8 == v // 8:
            continue
        terms = [r2[u][v]]
        terms.extend(both(adj[u][w], r2[w][v]) for w in range(64) if w not in (u, v))
        clause(terms)
        target_pairs += 1
body.close()
cnf = HERE / "auxiliary.cnf"
with cnf.open("wb") as out:
    out.write(f"p cnf {variables} {clauses}\n".encode())
    with (HERE / "clauses.tmp").open("rb") as inp:
        while data := inp.read(1024 * 1024):
            out.write(data)
model = dict(status="CNF_READY", vertices=64, fixed_cube_edges=96, external_edge_variables=1792,
             external_degree=2, fixed_external_edges=[[0,8],[0,16]],
             all_variables=variables, clauses=clauses, target_pairs=target_pairs,
             R2="equivalent actual paths length<=2", R3="all crosspencil pairs have actualpath length<=3",
             wall_limit_seconds=90, hard_CPU_limit_seconds=100,
             driver_CPU_before_solver=time.process_time()-START)
(HERE / "MODEL.json").write_text(json.dumps(model, indent=2) + "\n")
(HERE / "EDGE_VARIABLES.json").write_text(json.dumps([dict(u=u,v=v,var=q) for (u,v),q in edge_vars.items()], separators=(",", ":")) + "\n")
print(json.dumps(model), flush=True)


def solver_limit():
    resource.setrlimit(resource.RLIMIT_CPU, (100, 101))


solver = PROJECT / ".tools/lean-4.24.0-linux/bin/cadical"
command = [str(solver), "-q", "-t", "90", str(cnf)]
with (HERE / "solver.stdout").open("w") as output:
    process = subprocess.Popen(command, stdout=output, stderr=output, preexec_fn=solver_limit)
    handle = dict(status="RUNNING", pid=process.pid, stage="ONE_AUXILIARY_SAT", command=command)
    (HERE / "HANDLE.json").write_text(json.dumps(handle, indent=2) + "\n")
    print(json.dumps(handle), flush=True)
    expired = False
    try:
        code = process.wait(timeout=110)
    except subprocess.TimeoutExpired:
        expired = True
        process.kill()
        code = process.wait()

result = dict(status="RAW_UNSAT_UNCERTIFIED" if code == 20 else "UNKNOWN", solver_exit_code=code,
              solver_calls=1, auxiliary_positive_graphs=0, main1088_graphs=0,
              wall_observation_expired=expired)
if code == 10:
    values = set()
    for line in (HERE / "solver.stdout").read_text().splitlines():
        if line.startswith("v "):
            values.update(int(x) for x in line[2:].split() if int(x) > 0)
    graph = [set(u ^ bit for bit in (1,2,4)) for u in range(64)]
    for (u,v),q in edge_vars.items():
        if q in values:
            graph[u].add(v)
            graph[v].add(u)
    assert all(len(row) == 5 for row in graph)
    checked = 0
    for root in range(64):
        reached = {root}
        for _ in range(3):
            reached |= set(v for u in list(reached) for v in graph[u])
        assert len(reached) == 64
        checked += 1
    edges = [(u,v) for u,row in enumerate(graph) for v in sorted(row) if u<v]
    assert len(edges) == 160
    with (HERE / "K64.edges").open("w") as out:
        out.write("64 160\n")
        for u,v in edges:
            out.write(f"{u} {v}\n")
    (HERE / "K64_ADJACENCY.json").write_text(json.dumps([sorted(row) for row in graph]) + "\n")
    result.update(status="AUXILIARY_K64_D3_HIT_NEEDS_INDEPENDENT_CHECK", auxiliary_positive_graphs=1,
                  producer_roots_checked=checked, degree=5, D_at_most=3, main1088_graphs=0)
children = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = children.ru_utime + children.ru_stime - children0.ru_utime - children0.ru_stime
result.update(child_CPU_seconds=child_cpu, driver_CPU_seconds=time.process_time()-START,
              aggregate_CPU_seconds=child_cpu+time.process_time()-START, wall_seconds=time.monotonic()-WALL)
(HERE / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
(HERE / "TERMINAL.json").write_text(json.dumps(result, indent=2) + "\n")
(HERE / "HANDLE.json").write_text(json.dumps(dict(status="TERMINAL", pid=process.pid, result="RESULT.json")) + "\n")
print(json.dumps(result), flush=True)
