"""Complete labeled q4 trace check for the two concentrated high-degree spectra.

Conditional input: all F point-pair codegrees <=4. Reuses the exact general
one-red/tree threshold table, not the old six-degree role filters.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import Counter
import json, time

P = Path(__file__).resolve().parent
start = time.process_time()
old = json.loads((P.parent / "four_nonunit_degree_six_center_20261020/RESULT.json").read_text())
order = ["P", 0, 2, 3, 4]
tables = {tuple(r["types"]): r for r in old["thresholds"]}
assert len(tables) == 70
allowed = [m for m in range(32) if m.bit_count() in (0, 2, 3, 4)]
roles = [(14, 8, 8, 8, 8), (14, 9, 8, 8, 8), (15, 8, 8, 8, 8)]
jobs = []
for ds in roles:
    counts = Counter()
    residual = []
    for tr in combinations_with_replacement(allowed, 4):
        counts["full_trace_labels"] += 1
        if sum(m.bit_count() for m in tr) != sum(ds) - 35:
            continue
        counts["exact_degree_sum"] += 1
        if any(sum(bool(m >> i & 1) and bool(m >> j & 1) for m in tr) > 3
               for i in range(5) for j in range(i)):
            continue
        counts["pair_cap"] += 1
        h = [sum(m >> i & 1 for m in tr) for i in range(5)]
        a = [d - 1 - v for d, v in zip(ds, h)]
        assert min(a) >= 0 and sum(a) == 30
        cert = None
        for v in range(5):
            ts = tuple(sorted(("P" if m >> v & 1 else m.bit_count() for m in tr),
                              key=order.index))
            tab = tables[ts]
            if a[v] not in tab["fails"]:
                cert = dict(v=v, attachment=a[v], **tab["best"][a[v]])
                break
        if cert is not None:
            counts["anchor_strict"] += 1
        else:
            residual.append(dict(traces=tr, attachments=a, degrees=ds))
    counts["nonstrict"] = len(residual)
    assert counts["full_trace_labels"] == 23751
    jobs.append(dict(degrees=ds, counts=dict(counts), residual=residual))
out = dict(scope=__doc__, status="COMPLETE_CONDITIONAL_DIAGNOSTIC",
           jobs=jobs, cpu_seconds=time.process_time()-start)
(P / "RESULT.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(dict(cpu_seconds=out["cpu_seconds"],
                     jobs=[dict(degrees=j["degrees"], counts=j["counts"],
                                residual_head=j["residual"][:3]) for j in jobs])))
