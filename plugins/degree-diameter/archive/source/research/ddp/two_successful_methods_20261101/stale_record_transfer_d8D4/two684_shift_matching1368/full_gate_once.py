#!/usr/bin/env python3
"""Complete fixed-host H-equivariant matching gate; cached endpoints only."""
import csv
import json
import os
from pathlib import Path
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (7, 7))
HERE = Path(__file__).resolve().parent
PRIOR = 1.846522801
PREPARATION = 0.25
ALL = (1 << 342) - 1

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n")

write("FULL_HANDLE.json", {"status": "RUNNING", "pid": os.getpid(), "single_worker": True,
                           "stage": "read saved endpoints; precompute per-sigma masks; new233586domain",
                           "prior_CPU_seconds": PRIOR, "new_preparation_charge_CPU_seconds": PREPARATION,
                           "process_hard_CPU_seconds": 7, "wholecase_CPU_cap_seconds": 10})
history = json.loads((HERE / "HISTORY_SOURCE_GATE.json").read_text())
recipe = history["actual_recipe"]
elements = [(a,b) for a in range(38) for b in range(9)]
encode = lambda g: 9*g[0] + g[1]
factors = [pow(23,b,38) for b in range(9)]
mul = [[encode(((a+factors[b]*c)%38, (b+d)%9)) for c,d in elements] for a,b in elements]
S = [[list(map(encode, recipe[f"S{sigma}{rho}"])) for rho in range(2)] for sigma in range(2)]
cache = json.loads((HERE / "OLD_LENGTH_LE3_ENDPOINT_SETS.json").read_text())
A = {}
for row in cache["rows"]:
    A[(row["source_type"], row["target_type"], row["length"])] = {
        item["endpoint_group_label"]: item["word"] for item in row["endpoints_and_one_actual_word"]}

# Keep sigma in every key: the two terms use independent t_sigma.
terms = {}
masks = {}
mask_rows = []
for pi in (0,1):
    for sigma in (0,1):
        kappa = sigma ^ pi
        for tau in (0,1):
            for rho in (0,1):
                pairs = {}
                for i in range(4):
                    for j in range(4-i):
                        for a in A[(tau,sigma,i)]:
                            for b in A[(kappa,rho,j)]:
                                pairs.setdefault((a,b), (i,j))
                key = (pi,sigma,2*tau+rho)
                terms[key] = [(a,b,*ij) for (a,b),ij in pairs.items()]
        for t in range(342):
            row = []
            for slot in range(4):
                mask = 0
                for a,b,i,j in terms[(pi,sigma,slot)]:
                    mask |= 1 << mul[mul[a][t]][b]
                row.append(mask)
            masks[(pi,sigma,t)] = row
            mask_rows.append({"pi": "swap" if pi else "id", "sigma": sigma,
                              "t_group_label": t, "four_slot_masks_hex": [hex(m) for m in row]})
write("FULL_PER_SIGMA_MASKS.json", {"slot_order": [[0,0],[0,1],[1,0],[1,1]],
                                   "definition": "C_tau,sigma,rho(t_sigma,pi_sigma), exact old lengths i+j<=3",
                                   "rows": mask_rows})

counts = {"new_candidates_visited": 0, "old_shared_candidates_skipped": 0,
          "new_candidates_failed": 0, "hits": 0, "combined_slots_evaluated": 0}
by_pi = [{"pi": "id", "new_candidates_visited": 0, "old_shared_candidates_skipped": 0,
          "failed_slot_counts": [0,0,0,0], "hits": 0},
         {"pi": "swap", "new_candidates_visited": 0, "old_shared_candidates_skipped": 0,
          "failed_slot_counts": [0,0,0,0], "hits": 0}]
first_failure = None
hit = None
with (HERE / "FULL_ALL_NEW_PARAMETERS.tsv").open("w", newline="") as stream:
    output = csv.writer(stream, delimiter="\t")
    output.writerow(["pi", "t0", "t1", "stage", "first_failed_tau", "first_failed_rho", "missing_count", "first_missing_group_label"])
    for pi in (0,1):
        for t0 in range(342):
            left = masks[(pi,0,t0)]
            for t1 in range(342):
                if pi == 0 and t0 == t1:
                    counts["old_shared_candidates_skipped"] += 1
                    by_pi[pi]["old_shared_candidates_skipped"] += 1
                    continue
                counts["new_candidates_visited"] += 1
                by_pi[pi]["new_candidates_visited"] += 1
                right = masks[(pi,1,t1)]
                failed_slot = None
                for slot in range(4):
                    counts["combined_slots_evaluated"] += 1
                    missing = ALL ^ (left[slot] | right[slot])
                    if missing:
                        failed_slot = slot
                        first_missing = (missing & -missing).bit_length() - 1
                        missing_count = missing.bit_count()
                        counts["new_candidates_failed"] += 1
                        by_pi[pi]["failed_slot_counts"][slot] += 1
                        output.writerow(["swap" if pi else "id", t0,t1,"FAIL",slot//2,slot%2,missing_count,first_missing])
                        if first_failure is None:
                            first_failure = {"pi": "swap" if pi else "id", "t0": t0,"t1": t1,
                                             "slot": [slot//2,slot%2], "actual_missing_count": missing_count,
                                             "first_missing_group_label": first_missing,
                                             "missing_mask_hex": hex(missing)}
                        break
                if failed_slot is None:
                    counts["hits"] += 1
                    by_pi[pi]["hits"] += 1
                    output.writerow(["swap" if pi else "id",t0,t1,"ALL_FOUR_PASS","","",0,""])
                    hit = {"pi": "swap" if pi else "id", "pi_images": [pi,1^pi],
                           "t0_group_label": t0, "t1_group_label": t1,
                           "t0_coordinates": elements[t0], "t1_coordinates": elements[t1]}
                    break
            if hit:
                break
        if hit:
            break

if hit:
    # Build only the first passing graph, from the already literal-bound source recipe.
    old_edges = set()
    for tau in range(2):
        for h in range(342):
            for rho in range(2):
                for s in S[tau][rho]:
                    old_edges.add(tuple(sorted((342*tau+h,342*rho+mul[h][s]))))
    assert len(old_edges) == 2394
    graph_edges = old_edges | {(u+684,v+684) for u,v in old_edges}
    ts = [hit["t0_group_label"], hit["t1_group_label"]]
    for sigma in range(2):
        for h in range(342):
            graph_edges.add((342*sigma+h,684+342*(sigma^pi)+mul[h][ts[sigma]]))
    assert len(graph_edges) == 5472
    degrees = [0]*1368
    for u,v in graph_edges:
        assert 0 <= u < v < 1368
        degrees[u] += 1
        degrees[v] += 1
    assert set(degrees) == {8}
    (HERE / "FULL_graph_d8_D4_n1368.edges").write_text("1368 5472\n"+"".join(f"{u} {v}\n" for u,v in sorted(graph_edges)))
    routes = []
    for tau in range(2):
        for rho in range(2):
            slot = 2*tau+rho
            cover = {}
            for sigma in range(2):
                t = ts[sigma]
                kappa = sigma^pi
                for a,b,i,j in terms[(pi,sigma,slot)]:
                    target = mul[mul[a][t]][b]
                    if target not in cover:
                        prefix = A[(tau,sigma,i)][a]
                        suffix = A[(kappa,rho,j)][b]
                        path = [342*tau]
                        h = 0
                        for s0,s1,port,s in prefix:
                            h = mul[h][s]
                            path.append(342*s1+h)
                        h = mul[h][t]
                        path.append(684+342*kappa+h)
                        for s0,s1,port,s in suffix:
                            h = mul[h][s]
                            path.append(684+342*s1+h)
                        assert path[-1] == 684+342*rho+target and len(path)-1 <= 4
                        assert all(tuple(sorted((u,v))) in graph_edges for u,v in zip(path,path[1:]))
                        cover[target] = {"target_group_label": target, "middle_source_type": sigma,
                                         "middle_target_type": kappa, "t_group_label": t,
                                         "prefix_endpoint": a, "suffix_endpoint": b,
                                         "prefix_word": prefix, "suffix_word": suffix,
                                         "actual_vertex_path": path, "length": len(path)-1}
            assert len(cover) == 342
            routes.append({"source_type": tau, "target_type": rho,
                           "target_routes": [cover[h] for h in range(342)]})
    write("FULL_HIT_PARAMETERS.json", {**hit,"n":1368,"m":5472,"degree":8,
                                       "source_literal_binding": "RUN_SOURCE_LITERAL_BINDING.json",
                                       "source_raw_parsed_again": False,
                                       "all_source_old_edges_preserved_in_each_copy": True,
                                       "cross_word_proof": "FULL_HIT_CROSS_ROUTES.json"})
    write("FULL_HIT_CROSS_ROUTES.json", {"n":1368,"m":5472,"all_four_slots_actual_target_routes":routes,
                                         "route_count":1368,"source_D4_inherited":True,
                                         "source_left_H_covers_all_copy0_roots":True,
                                         "reverse_copy_cross_pairs_follow_by_undirected_symmetry":True,
                                         "allpair_D4": "same-copy old D4 plus all cross routes and inherited left equivariance",
                                         "exact_D4": "Moore(8,3)=457<1368", "BFS_roots":0})

actual = time.process_time() - START
total = PRIOR + PREPARATION + actual
complete = not hit and counts["new_candidates_visited"] == 233586 and counts["old_shared_candidates_skipped"] == 342
result = {"status": "HIT_COMPLETE1368_WORD_PROOF_PENDING_FRESH_ACCEPTANCE" if hit else "COMPLETE_NO_FIXED684_ALL_HLEFT_EQUIVARIANT_MATCHINGS",
          "full_domain_total":233928, "new_domain_total":233586,
          "counts":counts,"by_pi":by_pi,"first_failure":first_failure,"first_hit":hit,
          "new_domain_completed":complete,
          "unvisited_new_parameters":233586-counts["new_candidates_visited"],
          "positive_prediction_supported":bool(hit),
          "source_raw_parse_count_this_batch":0,"old_endpoint_DP_repeated":False,
          "source_or_candidate_BFS_roots":0,"old_shared_candidates_retested":0,
          "unhit_graphs_generated":0,"hit_graphs_generated":1 if hit else 0,
          "mask_count":len(mask_rows),
          "mask_reconstruction": "For row pi,t0,t1, missing=ALL342 XOR (C_sigma0[t0] OR C_sigma1[t1]); full masks stored, suffix uses pi(sigma)",
          "later_slots_after_first_failure":"NOT_TESTED",
          "scope":"Only identical copies of fixed actual684 source and every H-left-equivariant perfect matching pi in S2, independent t0,t1 in H342",
          "prior_wholecase_CPU_seconds":PRIOR,"new_preparation_charge_CPU_seconds":PREPARATION,
          "actual_new_process_CPU_seconds":actual,"wholecase_CPU_seconds":total,"wholecase_CPU_cap_seconds":10,
          "next":"STOP; root fresh-verifies hit or accepts exact fixed-family exclusion; no arbitrary matching or more hosts"}
write("FULL_RESULT.json", result)
write("FULL_TERMINAL.json", {**result,"terminal":True,"active_processes":0})
write("FULL_HANDLE.json", {"status":result["status"],"pid":os.getpid(),"terminal":True,"active_processes":0,"wholecase_CPU_seconds":total})
print(json.dumps(result))
