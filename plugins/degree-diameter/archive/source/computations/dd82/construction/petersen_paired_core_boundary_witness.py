"""Read-only missing-boundary rectangles after the nonoriginal 23 change."""
import json
import time

from hs_augmentation import dump
from petersen_four_fiber_reassembly import adjacency
from petersen_paired_core_reassembly import OUT

start = time.process_time()
data = json.loads((OUT/"encoding.json").read_text())
ns = adjacency([tuple(e) for e in data["fixed_edges"]])
curves = {}
for i in (0,1,4,5):
    curves[i] = []
    for v in range(10*i,10*i+10):
        pair = [sorted(ns[v]&set(range(10*j,10*j+10))) for j in (2,3)]
        assert all(len(p)==1 for p in pair)
        curves[i].append([p[0] for p in pair])
assert sorted(curves[4]) == sorted(curves[5])
rows = []
for u in range(20):
    missing,counts = {},{}
    for j in (2,3):
        counts[j] = {v:int(v in ns[u])+len(ns[u]&ns[v]) for v in range(10*j,10*j+10)}
        missing[j] = [v for v,c in counts[j].items() if c==0]
    compatible = [pair for pair in curves[4] if pair[0] in missing[2] and pair[1] in missing[3]]
    obstruction = len(missing[2])==len(missing[3])==3 and len(compatible)<2
    rows.append(dict(source=u,missing2=missing[2],missing3=missing[3],
                     fixed_route_counts=counts,
                     twin_signatures_inside_missing_rectangle=compatible,
                     three_missing_targets_with_fewer_than_two_twin_signatures=obstruction))
report = dict(rows=rows,twin_signature_curve=curves[4],
              obstructed_sources=[row["source"] for row in rows if row["three_missing_targets_with_fewer_than_two_twin_signatures"]],
              cpu_seconds=time.process_time()-start,
              scope="Read-only fixed-boundary incidence check, no candidate enumeration or solver")
dump(OUT/"boundary_rectangles.json",report)
print(json.dumps({k:v for k,v in report.items() if k != "rows"}))
