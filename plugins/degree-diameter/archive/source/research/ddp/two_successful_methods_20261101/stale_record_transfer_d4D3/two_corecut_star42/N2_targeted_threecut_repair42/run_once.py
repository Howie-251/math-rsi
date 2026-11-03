#!/usr/bin/env python3
"""One finite N2 targeted third-cut repair batch; no source validity BFS."""
import csv
import json
import os
from pathlib import Path
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (4, 4))
HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "N2_N3_all_pairs"
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
SOURCE = REPO / "research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.NORMALIZED_ADJ.json"
PREPARATION = 0.15

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n")

def bfs(adj, root, stop_target=None):
    distance = [-1] * len(adj)
    previous = [-1] * len(adj)
    distance[root] = 0
    queue = [root]
    for u in queue:
        if u == stop_target:
            break
        for v in sorted(adj[u]):
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                previous[v] = u
                queue.append(v)
    return distance, previous

def path(previous, root, target):
    seq = [target]
    while seq[-1] != root:
        seq.append(previous[seq[-1]])
        assert seq[-1] >= 0
    return seq[::-1]

def histogram(distance):
    return {str(d): distance.count(d) for d in sorted(set(distance))}

def first_far(distance, vertices=range(42)):
    return next((v for v in vertices if distance[v] < 0 or distance[v] > 3), None)

def remove(adj, u, v):
    adj[u].remove(v)
    adj[v].remove(u)

def add(adj, u, v):
    assert u != v and v not in adj[u]
    adj[u].add(v)
    adj[v].add(u)

def witness(parameters, stage, distance, previous, root, target):
    return {"parameters": parameters, "stage": stage, "root": root, "target": target,
            "actual_shortest_distance": distance[target],
            "actual_shortest_path": path(previous, root, target) if distance[target] >= 0 else None}

write("HANDLE.json", {"status": "RUNNING", "pid": os.getpid(), "stage": "saved N2 inputs then finite new variants",
                      "single_worker": True, "CPU_cap_seconds": 5, "process_hard_CPU_seconds": 4,
                      "preparation_charge_CPU_seconds": PREPARATION})
source_data = json.loads(SOURCE.read_text())
source_adj = [set(row) for row in source_data["adjacency"]]
source_edges = [(u, v) for u, ns in enumerate(source_adj) for v in sorted(ns) if u < v]
with (OLD / "N2_ALL_PAIR_PARAMETERS.tsv").open() as f:
    saved_parameters = {int(row["configuration"]): row for row in csv.DictReader(f, delimiter="\t")}
with (OLD / "N2_ALL_PAIR_STAGES.tsv").open() as f:
    base_stages = [row for row in csv.DictReader(f, delimiter="\t") if row["stage"] == "OLDOLD_R3_FAIL"]
assert len(base_stages) == 6
base_records = []
for row in base_stages:
    index = int(row["configuration"])
    pars = saved_parameters[index]
    base_records.append({"base_configuration": index,
                         "two_source_cuts": [[int(pars["e0"]), int(pars["e1"])],
                                             [int(pars["f0"]), int(pars["f1"])]],
                         "four_original_pins": [int(pars[f"pin{i}"]) for i in range(4)],
                         "saved_failed_pair": [int(row["failed_root"]), int(row["failed_target"])],
                         "saved_distance": int(row["distance"])})
write("SIX_SAVED_BASES.json", {"source": str(SOURCE.relative_to(REPO)), "bases": base_records,
                               "basis": "Read saved results, not rerun old two-cut candidates"})

counts = {"configurations_visited": 0, "saved_pair_R3_failed": 0, "saved_pair_R3_passed": 0,
          "newroot_R3_failed_after_saved_pair_repaired": 0, "newroot_R3_passed_after_saved_pair_repaired": 0,
          "oldold_failed_after_prior_gates": 0, "complete_hits": 0,
          "newroot_BFS_roots": 0, "final_oldlabel_BFS_roots": 0, "saved_pair_targeted_BFS": 0}
firsts = {}
per_base = []
hit = None
fields = ["variant", "base_configuration", "cut0_u", "cut0_v", "cut1_u", "cut1_v", "p", "a", "b",
          "saved_pair_u", "saved_pair_v", "saved_pair_actual_distance", "stage", "failed_root", "failed_target", "failed_distance"]
with (HERE / "ALL_ACTUAL_VARIANTS.tsv").open("w", newline="") as f:
    output = csv.writer(f, delimiter="\t")
    output.writerow(fields)
    for base in base_records:
        local = {"base_configuration": base["base_configuration"], "variants": 0, "saved_pair_passed": 0,
                 "newroot_passed": 0, "oldold_failures": 0}
        pins = set(base["four_original_pins"])
        original_two_cut_adj = [row.copy() for row in source_adj] + [set()]
        for e in base["two_source_cuts"]:
            remove(original_two_cut_adj, *e)
        for p in sorted(pins):
            add(original_two_cut_adj, 41, p)
        for p in sorted(pins):
            for c, d in source_edges:
                if c in pins or d in pins:
                    continue
                for a, b in ((c, d), (d, c)):
                    if a in source_adj[p]:
                        continue
                    variant = counts["configurations_visited"]
                    counts["configurations_visited"] += 1
                    local["variants"] += 1
                    pars = {**base, "variant": variant, "third_oriented_source_cut": [a, b],
                            "deleted_star_pin": p, "added_old_old_repair": [p, a],
                            "replacement_star_pin": b, "final_star_pins": sorted((pins - {p}) | {b}),
                            "new_label": 41}
                    adj = [row.copy() for row in original_two_cut_adj]
                    remove(adj, a, b)
                    remove(adj, 41, p)
                    add(adj, p, a)
                    add(adj, 41, b)
                    assert all(len(ns) == 4 for ns in adj) and sum(map(len, adj)) == 168
                    u, v = base["saved_failed_pair"]
                    pdist, pprev = bfs(adj, u, v)
                    counts["saved_pair_targeted_BFS"] += 1
                    stage = "SAVED_PAIR_R3_FAIL"
                    failed_root, failed_target, failed_distance = u, v, pdist[v]
                    if pdist[v] < 0 or pdist[v] > 3:
                        counts["saved_pair_R3_failed"] += 1
                        firsts.setdefault("first_saved_pair_still_failed", witness(pars, stage, pdist, pprev, u, v))
                    else:
                        counts["saved_pair_R3_passed"] += 1
                        local["saved_pair_passed"] += 1
                        firsts.setdefault("first_saved_pair_repaired", witness(pars, "SAVED_PAIR_REPAIRED", pdist, pprev, u, v))
                        ndist, nprev = bfs(adj, 41)
                        counts["newroot_BFS_roots"] += 1
                        bad = first_far(ndist, range(41))
                        if bad is not None:
                            stage = "NEWROOT_R3_FAIL_AFTER_PAIR_REPAIR"
                            counts["newroot_R3_failed_after_saved_pair_repaired"] += 1
                            failed_root, failed_target, failed_distance = 41, bad, ndist[bad]
                            firsts.setdefault("first_newroot_failed_after_pair_repair", witness(pars, stage, ndist, nprev, 41, bad))
                        else:
                            counts["newroot_R3_passed_after_saved_pair_repaired"] += 1
                            local["newroot_passed"] += 1
                            firsts.setdefault("first_pair_repaired_and_newroot_preserved", {
                                **witness(pars, "PAIR_REPAIRED_AND_NEWROOT_R3_PASS", pdist, pprev, u, v),
                                "newroot_actual_distance_histogram": histogram(ndist),
                                "newroot_actual_eccentricity": max(ndist)})
                            all_stats = [{"root": 41, "distance_histogram": histogram(ndist), "eccentricity": max(ndist)}]
                            stage = "FULL_GRAPH_R3_PASS"
                            failed_root = failed_target = failed_distance = ""
                            for old_root in range(41):
                                odist, oprev = bfs(adj, old_root)
                                counts["final_oldlabel_BFS_roots"] += 1
                                bad = first_far(odist, range(41))
                                all_stats.append({"root": old_root, "distance_histogram": histogram(odist), "eccentricity": max(odist)})
                                if bad is not None:
                                    stage = "OLDOLD_R3_FAIL_AFTER_PAIR_AND_NEWROOT_PASS"
                                    counts["oldold_failed_after_prior_gates"] += 1
                                    local["oldold_failures"] += 1
                                    failed_root, failed_target, failed_distance = old_root, bad, odist[bad]
                                    firsts.setdefault("first_remaining_oldold_failure", witness(pars, stage, odist, oprev, old_root, bad))
                                    break
                            if stage == "FULL_GRAPH_R3_PASS":
                                counts["complete_hits"] += 1
                                hit = {"parameters": pars, "all_42_final_root_statistics": all_stats,
                                       "distance3_witness": None}
                                far = next(x for x in range(41) if ndist[x] == 3)
                                hit["distance3_witness"] = witness(pars, stage, ndist, nprev, 41, far)
                                edges = [(x, y) for x, ns in enumerate(adj) for y in sorted(ns) if x < y]
                                (HERE / "graph_d4_D3_n42.edges").write_text("42 84\n" + "".join(f"{x} {y}\n" for x, y in edges))
                                write("HIT_PARAMETERS_AND_ALL_ROOTS.json", hit)
                    output.writerow([variant, base["base_configuration"], *base["two_source_cuts"][0], *base["two_source_cuts"][1],
                                     p, a, b, u, v, pdist[v], stage, failed_root, failed_target, failed_distance])
                    if hit:
                        break
                if hit:
                    break
            if hit:
                break
        per_base.append(local)
        if hit:
            break

actual = time.process_time() - START
complete = hit is None and len(per_base) == 6
result = {"status": "HIT_COMPLETE_FINAL_42_GRAPH_PENDING_FRESH_ACCEPTANCE" if hit else "COMPLETE_NO_SIX_BASES_TARGETED_THREECUT_REPAIR42",
          "source_id": "N2", "source_JSON_parse_count": 1, "source_D3_BFS_roots": 0,
          "old_two_cut_batch_repeated": False, "source_validity": "INHERITED",
          "candidate_n": 42, "candidate_m": 84, "candidate_degree": 4,
          "six_base_domain_completed": complete, "cross_base_literal_deduplication": False,
          "scope": "Only saved six N2 newroot-pass/oldold-fail bases; third source cut disjoint from original pins; p-a original nonedge; one specified star-pin replacement",
          "counts": counts, "per_base_counts": per_base, "first_stage_witnesses": firsts,
          "positive_prediction": "At least one variant repairs saved pair and preserves newroot R3",
          "positive_prediction_supported": counts["newroot_R3_passed_after_saved_pair_repaired"] > 0,
          "complete_graph_hit": hit is not None, "actual_process_CPU_seconds": actual,
          "preparation_charge_CPU_seconds": PREPARATION, "wholecase_CPU_seconds": actual + PREPARATION,
          "wholecase_CPU_cap_seconds": 5, "further_sources_or_repairs_authorized": False}
write("RESULT.json", result)
write("TERMINAL.json", {**result, "terminal": True, "active_processes": 0,
                        "next": "STOP; root reviews hit or finite-scope failure; no second repair/N3 batch"})
write("HANDLE.json", {"status": result["status"], "pid": os.getpid(), "terminal": True,
                      "active_processes": 0, "wholecase_CPU_seconds": actual + PREPARATION})
print(json.dumps({k: result[k] for k in ("status", "counts", "positive_prediction_supported", "actual_process_CPU_seconds", "wholecase_CPU_seconds")}))
