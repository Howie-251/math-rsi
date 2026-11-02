"""Bounded necessary-condition check for Brown insertion: an 8-point dominating set.
A SAT result here is only a vertex set, never an order58 graph.
"""
from pathlib import Path
import argparse
import importlib.util
import json
import os
import subprocess
import time

root = Path(__file__).resolve().parents[3]
base = Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument('--exclude-polar-lines', action='store_true')
args = parser.parse_args()
out = base / ("brown_dominating8_nonline" if args.exclude_polar_lines else "brown_dominating8")
out.mkdir(exist_ok=True)
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
rows = [tuple(map(int, s.split())) for s in (base/"brown57.edges").read_text().splitlines()]
n, m = rows[0]
assert (n, m) == (57, 224)
adj = [set() for _ in range(n)]
for u,v in rows[1:]:
    adj[u].add(v); adj[v].add(u)
source = root/"context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py"
spec = importlib.util.spec_from_file_location("counters", source)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
cnf = module.CNFEmitter(out/"dominating8.cnf")
variables = [cnf.new_var("vertex_selected") for _ in range(n)]
for v in range(n):
    cnf.add_clause(*(variables[u] for u in sorted({v}|adj[v])))
if args.exclude_polar_lines:
    points = json.loads((base/'brown57.vertices.json').read_text())
    for p in points:
        line = [i for i,q in enumerate(points) if sum(a*b for a,b in zip(p,q))%7 == 0]
        assert len(line)==8
        cnf.add_clause(*(-variables[i] for i in line))
module.enforce_exact(cnf, variables, 8, "cardinality")
cnf.finish()
cmd=[str(root/".tools/lean-4.24.0-linux/bin/cadical"),"--lrat","--no-binary","-t","5",str(out/"dominating8.cnf"),str(out/"dominating8.lrat")]
started=time.monotonic()
with (out/"solver.log").open("w") as f:
    result=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=15)
report=dict(exit_code=result.returncode,seconds=time.monotonic()-started,cpu_count=1,wall_budget_seconds=5,
            excluded_all_57_polar_lines=args.exclude_polar_lines,
            variables=cnf.variable_count,clauses=cnf.clause_count,scope="Eight-point domination in fixed Brown57 only; not an order58 construction")
if result.returncode==10:
    literals=[int(x) for line in (out/"solver.log").read_text().splitlines() if line.startswith("v ") for x in line.split()[1:]]
    selected=sorted(x-1 for x in literals if 1<=x<=n)
    assert len(selected)==8
    assert all(({v}|adj[v])&set(selected) for v in range(n))
    classes={"C":[v for v in range(n) if len(adj[v])==7]}
    classes["I"]=[v for v in range(n) if len(adj[v])==8 and not adj[v]&set(classes["C"])]
    classes["E"]=sorted(set(range(n))-set(classes["C"])-set(classes["I"]))
    report.update(status="SAT_DOMINATING_SET_INDEPENDENTLY_VERIFIED",selected=selected,
                  selected_classes={k:sorted(set(selected)&set(v)) for k,v in classes.items()})
elif result.returncode==20:
    report.update(status="RAW_UNSAT_WITH_UNCHECKED_LRAT")
else:
    report.update(status="UNKNOWN_OR_PROCESS_FAILURE")
(out/"result.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
