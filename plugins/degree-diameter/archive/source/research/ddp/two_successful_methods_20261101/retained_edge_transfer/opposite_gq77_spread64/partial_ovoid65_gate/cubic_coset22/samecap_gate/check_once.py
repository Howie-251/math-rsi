#!/usr/bin/env python3
"""One bounded fixed-geometry gate. Never opens an edge table or builds a graph."""
import collections
import datetime
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
SOURCE = OUT.parents[2]


def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + "\n")


def B(x, y):
    return (x[0]*y[2] + 3*x[1]*y[3] - x[2]*y[0] - 3*x[3]*y[1]) % 7


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    start = time.process_time()
    assert (OUT / "PRED.json").exists()
    assert not (OUT / "RESULT.json").exists(), "one fixed return only"
    data = json.loads((SOURCE / "PARAMETERS.json").read_text())
    saved_centers = json.loads((OUT.parent / "CENTERS.json").read_text())
    points = [tuple(p) for p in data["points"]]
    lines = [r["points"] for r in data["lines"]]
    through = data["point_incident_lines"]
    spread = data["spread_line_labels"]
    owner = data["point_spread_owner"]
    pid = {p: i for i, p in enumerate(points)}
    O = [(1,t,(t**3+k)%7,(-t*t)%7) for k in (0,2,4) for t in range(7)] + [(0,0,1,0)]
    oid = [pid[p] for p in O]
    oset = set(oid)
    assert len(points) == len(lines) == len(through) == 400
    assert len(spread) == 50
    assert all(len(row) == 8 for row in lines + through)
    assert len(set(oid)) == 22
    assert all(B(x,y) for i,x in enumerate(O) for y in O[:i])
    incidence_counts = [sum(p in row for p in oid) for row in lines]
    assert max(incidence_counts) == 1
    point_counts = [sum(B(p,o) == 0 for o in O) for p in points]
    outside_compatible = [i for i,c in enumerate(point_counts) if i not in oset and c == 0]
    point_rows = [{"point_id":i,"point":p,"in_O22":i in oset,
                   "collinear_O22_including_self_count":point_counts[i]}
                  for i,p in enumerate(points)]
    dump("POINT_COLLINEARITY.json", point_rows)
    residue_table = []
    for a in range(7):
        values = [(s**3-a*s)%7 for s in range(7)]
        image = sorted(set(values))
        sums = sorted({(z+k)%7 for z in image for k in (0,2,4)})
        assert sums == list(range(7))
        residue_table.append({"A":a,"f_A_values_s_0_to_6":values,
                              "image":image,"image_plus_K":sums})
    dump("MAXIMALITY_RESIDUES.json",residue_table)

    def source_neighbors(c):
        if c < 160000:
            p,l = divmod(c,400)
            ns = [400*q+m for q in lines[l] for m in through[p]
                  if 400*q+m != c]
            if p in lines[l]:
                ns.append(160000+owner[p])
        else:
            j = c-160000
            ns = [400*q+m for q in lines[spread[j]] for m in through[q]]
        assert len(ns) == 64
        return ns

    centers = [400*p+l for p in oid for l in spread]
    assert [r["center"] for r in saved_centers] == centers
    # The accepted source-neighborhood recipe, not a passed-status flag,
    # defines exactly which source vertices acquired the one extra edge.
    clone_at_pin = [-1]*160050
    for i,c in enumerate(centers):
        for v in source_neighbors(c):
            assert clone_at_pin[v] == -1
            clone_at_pin[v] = 160050+i
    saturated = [x >= 0 for x in clone_at_pin]
    assert sum(saturated) == 70400
    meeting_O = [i for i,c in enumerate(incidence_counts) if c]
    special_flags = {400*p+spread[owner[p]] for p in oid}
    for p in range(400):
        for l in range(400):
            assert saturated[400*p+l] == (bool(incidence_counts[l]) and 400*p+l not in special_flags)
    assert sum(saturated[:160000]) == 70378
    assert sum(saturated[160000:]) == 22
    source_degree_hist = collections.Counter(64+int(x) for x in saturated)
    all_degree_hist = source_degree_hist + collections.Counter({64:1100})

    group_hists = {"old_product":collections.Counter(),"old_bonus":collections.Counter(),
                   "new_clone":collections.Counter()}
    group_degree_hists = {k:collections.Counter() for k in group_hists}
    minima = {}
    witnesses = {}
    compatible = []
    by_point_count = collections.defaultdict(collections.Counter)
    degree_and_satcount = collections.Counter()
    for c in range(161150):
        if c < 160000:
            group = "old_product"
            ns = source_neighbors(c)
            if clone_at_pin[c] >= 0:
                ns.append(clone_at_pin[c])
        elif c < 160050:
            group = "old_bonus"
            ns = source_neighbors(c)
            if clone_at_pin[c] >= 0:
                ns.append(clone_at_pin[c])
        else:
            group = "new_clone"
            ns = source_neighbors(centers[c-160050])
        degree = len(ns)
        assert degree <= 65
        sat_ns = [v for v in ns if v < 160050 and saturated[v]]
        blocked = len(sat_ns)
        group_hists[group][blocked] += 1
        group_degree_hists[group][degree] += 1
        degree_and_satcount[(degree,blocked)] += 1
        if group not in minima or blocked < minima[group]:
            minima[group] = blocked
            witnesses[group] = {"center":c,"current_degree":degree,
                                "saturated_neighbor_count":blocked,
                                "one_saturated_neighbor":sat_ns[0] if sat_ns else None,
                                "full_current_neighbors":ns,
                                "neighbor_current_degrees":[65 if v < 160050 and saturated[v] else 64 for v in ns]}
        if c < 160000:
            p,l = divmod(c,400)
            r = sum(incidence_counts[m] for m in through[p])
            e = int(any(q in oset and spread[owner[q]] in through[p] for q in lines[l]))
            a = int(p in lines[l] and saturated[c])
            f = int(p in lines[l] and saturated[160000+owner[p]])
            assert blocked == 8*r-e-a+f
            by_point_count[(p in oset,point_counts[p])][blocked] += 1
        elif c < 160050:
            assert blocked == (35 if saturated[c] else 22)
        else:
            assert blocked == 64
        if degree <= 65 and blocked == 0:
            compatible.append({"center":c,"group":group,"current_degree":degree,
                               "full_current_neighbors":ns,
                               "neighbor_current_degrees":[65 if v < 160050 and saturated[v] else 64 for v in ns],
                               "all_neighbors_have_spare_degree":True})
    dump("MINIMUM_BLOCKER_WITNESSES.json",witnesses)
    dump("ACTUAL_COMPATIBLE_CENTERS.json",compatible)
    cpu = time.process_time()-start
    result = {
      "status":"TERMINAL_STRICT_FIXED_GRAPH_FULL_CURRENT_NEIGHBORHOOD_SAMECAP65_OBSTRUCTION" if not compatible else "TERMINAL_COMPATIBLE_CENTER_FOUND_NO_GRAPH_GENERATED",
      "finished_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
      "fixed_graph":{"n":161150,"m":5192000,"cap":65,"degree_histogram":dict(sorted(all_degree_hist.items()))},
      "O22_point_ids":oid,"O22_is_maximal_partial_ovoid":not outside_compatible,
      "collinear_O22_count_includes_self":True,
      "all_400_point_count_histogram":dict(sorted(collections.Counter(point_counts).items())),
      "outside_378_point_count_histogram":dict(sorted(collections.Counter(point_counts[i] for i in range(400) if i not in oset).items())),
      "actual_compatible_outside_point_ids":outside_compatible,
      "residue_classes_checked":7,
      "saturated_original_products":sum(saturated[:160000]),"saturated_old_bonus":sum(saturated[160000:]),
      "special_unsaturated_flags":[{"product":v,"point":v//400,"spread_line":v%400} for v in sorted(special_flags)],
      "all_current_centers_checked":161150,
      "center_classes_checked":{"old_product":160000,"old_bonus":50,"new_clone":1100},
      "center_class_current_degree_histograms":{k:dict(sorted(v.items())) for k,v in group_degree_hists.items()},
      "center_class_saturated_neighbor_histograms":{k:dict(sorted(v.items())) for k,v in group_hists.items()},
      "minimum_saturated_neighbors_by_class":minima,
      "degree_and_saturated_neighbor_histogram":[{"current_degree":d,"saturated_neighbors":s,"centers":c} for (d,s),c in sorted(degree_and_satcount.items())],
      "old_product_by_O_membership_and_collinear_count":[{"point_in_O22":i,"point_collinear_O22_count":c,"saturated_neighbor_histogram":dict(sorted(h.items()))} for (i,c),h in sorted(by_point_count.items())],
      "actual_compatible_current_centers":len(compatible),
      "actual_compatible_current_center_file":"ACTUAL_COMPATIBLE_CENTERS.json",
      "CPU_seconds":cpu,"CPU_budget_seconds":30,"workers":1,
      "large_edge_tables_opened":0,"graph_generated":False,"BFS_calls":0,"Lean_compilations":0,"solver_calls":0,
      "strict_scope":"Fixed accepted161150graph, retained edges, cap65, one clone of a complete current open neighborhood. Arbitrary pins/cooperative helpers/other source/edge changes are not excluded.",
      "next_choice":"Stop this fixed full-current-neighborhood samecap65 operation. Any further fixed-cap65 filling must use a different actual pin-cover rule; no automatic seed/field/controller ladder."
    }
    dump("RESULT.json",result)
    dump("TERMINAL.json",{"status":result["status"],"owned_jobs_running":False,
         "CPU_seconds":cpu,"budget_CPU_seconds":30,"all_planned_finite_checks_complete":True,
         "graph_generated":False,"large_edge_tables_opened":0,
         "BFS_calls":0,"Lean_compilations":0,"solver_calls":0,
         "strict_scope":result["strict_scope"]})
    print(json.dumps({k:result[k] for k in ["status","all_400_point_count_histogram",
          "outside_378_point_count_histogram","minimum_saturated_neighbors_by_class",
          "center_class_saturated_neighbor_histograms","actual_compatible_current_centers","CPU_seconds"]}))


if __name__ == "__main__":
    main()
