"""Bounded fresh S_TOUCH cases from the saturated-row coverage proof.

Three cold starts, 30 solver seconds each, one CPU. A partial LRAT trace or
UNKNOWN is never a branch exclusion. Reuses the existing fresh base and map.
"""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

root = Path(__file__).resolve().parents[3]
base = root / "computations/dd82/n62/s_touch_certificate_profile"
out = root / "computations/dd82/n62/s_touch_three_cases"
out.mkdir(exist_ok=True)
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
mapping = json.loads((base / "maps/S_TOUCH.map.json").read_text())
base_units = {v: bool(value) for v, value, _ in mapping["unit_assignments"]}
cases = [
    ("A", [21, 27, 34, 41, 48, 55], [3, 21]),
    ("C2", [27, 28, 34, 41, 48, 55], [4, 15]),
    ("C3", [27, 28, 34, 41, 48, 55], [4, 21]),
]

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (40, 41))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (192 * 1024**2, 192 * 1024**2))

reports = []
for name, a_targets, b_targets in cases:
    units = {}
    rows = {}
    for key, targets in [("edge_variables", a_targets), ("b1_variables", b_targets)]:
        decoded = []
        for u, v, var in mapping[key]:
            if 9 not in (u, v):
                continue
            neighbor = v if u == 9 else u
            value = neighbor in targets
            assert var not in base_units or base_units[var] == value
            assert var not in units or units[var] == value
            units[var] = value
            if value:
                decoded.append(neighbor)
        assert sorted(decoded) == sorted(targets)
        rows[key] = sorted(decoded)
    assert len(units) == 112
    cnf = out / f"{name}.cnf"
    with (base / "cnf/S_TOUCH.cnf").open() as source, cnf.open("w") as dest:
        for line in source:
            if line.startswith("p cnf "):
                _, _, nv, nc = line.split()
                dest.write(f"p cnf {nv} {int(nc) + len(units)}\n")
            else:
                dest.write(line)
        for var, value in sorted(units.items()):
            dest.write(f"{var if value else -var} 0\n")
    (out / f"{name}.units.json").write_text(json.dumps({
        "case": name, "decoded_rows": rows,
        "literals": [v if value else -v for v, value in sorted(units.items())],
        "fixed_B_neighbor_0": True, "unit_count": len(units),
        "coverage_source": "proofs/dd82/n62/S_TOUCH_THREE_CASE_REDUCTION.md"
    }, indent=2) + "\n")
    proof = out / f"{name}.lrat"
    cmd = [str(root / ".tools/lean-4.24.0-linux/bin/cadical"),
           "--lrat", "-t", "30", str(cnf), str(proof)]
    start = time.monotonic()
    with (out / f"{name}.log").open("w") as log:
        try:
            p = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT,
                               timeout=45, preexec_fn=limits)
            code = p.returncode
            status = {10: "SAT_CANDIDATE", 20: "RAW_UNSAT_WITH_UNCHECKED_LRAT",
                      0: "UNKNOWN"}.get(code, "PROCESS_FAILURE")
        except subprocess.TimeoutExpired:
            code, status = None, "OUTER_WALL_TIMEOUT"
    report = dict(case=name, status=status, exit_code=code,
                  seconds=time.monotonic()-start, cpu_count=1, cold_start=True,
                  solver_seconds_budget=30, unit_count=len(units),
                  proof_bytes=proof.stat().st_size if proof.exists() else 0,
                  proof_checked=False, lean_graph_bridge=False, command=cmd)
    reports.append(report)
    (out / "results.json").write_text(json.dumps(reports, indent=2)+"\n")
    print(json.dumps(report), flush=True)
