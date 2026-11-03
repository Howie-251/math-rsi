#!/usr/bin/env python3
"""The fixed H342/shared-right-t cross-word gate, one complete bounded batch."""
import csv
import json
import os
from pathlib import Path
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (7, 7))
HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
SOURCEDIR = REPO / "research/ddp/m1_sources"
READ_GATE_CHARGE = 1.5
NEW_PREPARATION_CHARGE = 0.25

def write(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2) + "\n")

write("RUN_HANDLE.json", {"status": "RUNNING", "pid": os.getpid(), "single_worker": True,
                          "stage": "one source binding, one length<=3 endpoint-set generation,342t gate",
                          "wholecase_cap_CPU_seconds": 10, "inherited_read_gate_CPU_seconds": READ_GATE_CHARGE,
                          "new_preparation_charge_CPU_seconds": NEW_PREPARATION_CHARGE,
                          "process_hard_CPU_seconds": 7})

recipe = json.loads((SOURCEDIR / "684_recovered_construction.json").read_text())
assert (recipe["m"], recipe["n"], recipe["r"]) == (38, 9, 23)
voltages = [[list(map(tuple, cell)) for cell in row] for row in recipe["voltage_sets"]]
factors = [pow(23, b, 38) for b in range(9)]
elements = [(a, b) for a in range(38) for b in range(9)]
encode = lambda g: 9*g[0] + g[1]
multiply = [[encode(((a + factors[b]*c) % 38, (b+d) % 9))
             for c, d in elements] for a, b in elements]
inverse = [encode(((-factors[(-b) % 9]*a) % 38, (-b) % 9)) for a, b in elements]
S = [[[encode(g) for g in cell] for cell in row] for row in voltages]

# Only literal construction-input binding, not an old D4 or field/group-law test.
literal = set()
with (SOURCEDIR / "graph_7_4_n684.txt").open() as source_stream:
    for line in source_stream:
        if not line.strip() or line.startswith("#"):
            continue
        u, v = map(int, line.split())
        literal.add(tuple(sorted((u, v))))
expected = set()
for tau in range(2):
    for h in range(342):
        for rho in range(2):
            for s in S[tau][rho]:
                expected.add(tuple(sorted((342*tau+h, 342*rho+multiply[h][s]))))
assert expected == literal and len(literal) == 2394
write("RUN_SOURCE_LITERAL_BINDING.json", {
    "status": "PASS_LITERAL_H_RIGHT_VOLTAGE_RULE_BINDING",
    "source_raw_parse_count": 1, "source_literal_edges": len(literal),
    "all_literal_edges_equal_actual_recipe": True, "n": 684,
    "left_H_equivariance": "(k*h)*s=k*(h*s) in inherited group law; matching also k*(h*t)=(k*h)*t",
    "source_D4_BFS_roots": 0, "source_recovery_code_executed": False,
    "new_field_or_group_law_verification": False,
    "labels": "342*tau+9*a+b", "operation": "h*s, not s*h"})

# One exact-length endpoint DP. Each stored representative is a word, not a BFS result.
A = [[[{} for _ in range(2)] for _ in range(4)] for _ in range(2)]
for tau in range(2):
    A[tau][0][tau][0] = []
    for length in range(1, 4):
        for sigma in range(2):
            for a, word in A[tau][length-1][sigma].items():
                for rho in range(2):
                    for port_index, s in enumerate(S[sigma][rho]):
                        h = multiply[a][s]
                        A[tau][length][rho].setdefault(h, word + [[sigma, rho, port_index, s]])
endpoint_rows = []
for tau in range(2):
    for length in range(4):
        for rho in range(2):
            endpoint_rows.append({"source_type": tau, "target_type": rho, "length": length,
                                  "count": len(A[tau][length][rho]),
                                  "endpoints_and_one_actual_word": [
                                      {"endpoint_group_label": h, "word": A[tau][length][rho][h]}
                                      for h in sorted(A[tau][length][rho])]})
write("OLD_LENGTH_LE3_ENDPOINT_SETS.json", {"source": "literal bound H342/S recipe", "exact_lengths": [0,1,2,3],
                                           "generated_once": True, "rows": endpoint_rows})
terms = {}
for tau in range(2):
    for rho in range(2):
        slot_terms = {}
        for i in range(4):
            for j in range(4-i):
                for sigma in range(2):
                    for a in A[tau][i][sigma]:
                        for b in A[sigma][j][rho]:
                            slot_terms.setdefault((a, b), (i, j, sigma))
        terms[(tau, rho)] = [(a, b, *details) for (a, b), details in slot_terms.items()]

all_results = []
auto = []
first_failure = None
hit = None
tested_slots = 0
for t in range(342):
    slots = [{"source_type": tau, "target_type": rho, "status": "NOT_TESTED"}
             for tau in range(2) for rho in range(2)]
    is_auto = all({multiply[multiply[inverse[t]][s]][t] for s in S[tau][rho]} == set(S[tau][rho])
                  for tau in range(2) for rho in range(2))
    record = {"t_group_label": t, "t_coordinates": elements[t], "slots": slots}
    if is_auto:
        auto.append(t)
        record["status"] = "PAPER_PRUNED_RIGHTSHIFT_SOURCE_AUTOMORPHISM_CARTESIAN_D5"
        record["prune_binding"] = "All four t^-1*S_tau,rho*t equal their original literal sets"
        for slot in slots:
            slot["status"] = "NOT_TESTED_PAPER_AUTOMORPHISM_PRUNE"
    else:
        saved_cover = {}
        record["status"] = "ALL_FOUR_CROSS_SLOTS_PASS"
        for slot in slots:
            tau, rho = slot["source_type"], slot["target_type"]
            cover = {}
            for a, b, i, j, sigma in terms[(tau, rho)]:
                target = multiply[multiply[a][t]][b]
                cover.setdefault(target, [i, j, sigma, a, b])
            missing = [h for h in range(342) if h not in cover]
            tested_slots += 1
            slot.update({"status": "PASS" if not missing else "FAIL", "actual_covered": len(cover),
                         "actual_missing_count": len(missing), "first_missing_group_label": missing[0] if missing else None,
                         "missing_group_labels": missing,
                         "distinct_word_factor_pairs_evaluated": len(terms[(tau, rho)])})
            if missing:
                record["status"] = "CROSS_SLOT_FAIL"
                record["first_failed_slot"] = [tau, rho]
                record["actual_cross_distance_for_missing_targets"] = "exact5: no<=4 onecross word; inherited same-copy D4 gives<=5"
                if first_failure is None:
                    first_failure = {"t_group_label": t, "t_coordinates": elements[t], "source_type": tau,
                                     "target_type": rho, "missing_group_label": missing[0],
                                     "missing_coordinates": elements[missing[0]], "actual_missing_count": len(missing),
                                     "source_vertex_copy0_label": 342*tau,
                                     "target_vertex_copy1_label": 684+342*rho+missing[0],
                                     "distance": 5, "basis": "complete onecross endpoint exclusion plus inherited D4 upper"}
                break
            saved_cover[(tau, rho)] = cover
        if record["status"] == "ALL_FOUR_CROSS_SLOTS_PASS":
            hit = {"t_group_label": t, "t_coordinates": elements[t], "four_slot_word_witnesses": []}
            for (tau, rho), cover in saved_cover.items():
                hit["four_slot_word_witnesses"].append({"source_type": tau, "target_type": rho,
                    "targets": [{"target_group_label": h, "factor_witness_ilen_jlen_sigma_a_b": cover[h],
                                 "prefix_actual_word": A[tau][cover[h][0]][cover[h][2]][cover[h][3]],
                                 "suffix_actual_word": A[cover[h][2]][cover[h][1]][rho][cover[h][4]]}
                                for h in range(342)]})
            graph_edges = set(literal)
            graph_edges.update((u+684, v+684) for u, v in literal)
            graph_edges.update((342*tau+h, 684+342*tau+multiply[h][t]) for tau in range(2) for h in range(342))
            assert len(graph_edges) == 5472
            degree = [0]*1368
            for u, v in graph_edges:
                assert 0 <= u < v < 1368
                degree[u] += 1
                degree[v] += 1
            assert set(degree) == {8}
            (HERE / "graph_d8_D4_n1368.edges").write_text("1368 5472\n" + "".join(f"{u} {v}\n" for u, v in sorted(graph_edges)))
            write("HIT_PARAMETERS_AND_CROSS_WORD_PROOF.json", hit)
    all_results.append(record)
    if hit:
        break

actual = time.process_time() - START
total = READ_GATE_CHARGE + NEW_PREPARATION_CHARGE + actual
write("ALL342_T_SLOT_RESULTS.json", {"results": all_results, "early_failure_policy": "unvisited slots remain NOT_TESTED",
                                      "word_endpoint_generation_count": 1})
with (HERE / "ALL342_T_SLOT_SUMMARY.tsv").open("w", newline="") as stream:
    out = csv.writer(stream, delimiter="\t")
    out.writerow(["t", "normal", "phase", "status", "source_type", "target_type", "slot_status", "covered", "missing_count", "first_missing"])
    for record in all_results:
        for slot in record["slots"]:
            out.writerow([record["t_group_label"], *record["t_coordinates"], record["status"],
                          slot["source_type"], slot["target_type"], slot["status"],
                          slot.get("actual_covered", ""), slot.get("actual_missing_count", ""), slot.get("first_missing_group_label", "")])
result = {"status": "HIT_1368_WORD_COVER_PENDING_FRESH_ACCEPTANCE" if hit else "COMPLETE_NO_FIXED684_SHARED_RIGHT_T342_FAMILY",
          "source": "actual Michel684 two-fiber H342 right-voltage graph", "domain_size": 342,
          "parameters_completed": len(all_results), "unvisited_parameters": 342-len(all_results),
          "paper_automorphism_pruned_t_labels": auto, "paper_automorphism_pruned_count": len(auto),
          "nonautomorphism_t_evaluated": len(all_results)-len(auto), "cross_slots_evaluated": tested_slots,
          "hit": hit is not None, "positive_prediction_supported": hit is not None,
          "first_actual_cross_failure": first_failure,
          "slot_factor_pair_counts": {f"{tau}->{rho}": len(terms[(tau,rho)]) for tau in range(2) for rho in range(2)},
          "source_raw_parse_count": 1, "source_literal_binding_pass": True,
          "source_D4_BFS_roots": 0, "candidate_BFS_roots": 0,
          "endpoint_sets_generated_once": True, "unhit_candidate_graphs_generated": 0,
          "graphs_written": 1 if hit else 0,
          "scope": "Only fixed actual684 host, identical copies, type-preserving matching shared h->h*t for one t in actual H342",
          "read_gate_conservative_CPU_seconds": READ_GATE_CHARGE,
          "new_preparation_charge_CPU_seconds": NEW_PREPARATION_CHARGE,
          "actual_process_CPU_seconds": actual, "wholecase_CPU_seconds": total, "wholecase_CPU_cap_seconds": 10,
          "next": "STOP; root reviews finite family exclusion or fresh-validates first hit; no independent t0/t1 or another host"}
write("RUN_RESULT.json", result)
write("RUN_TERMINAL.json", {**result, "terminal": True, "active_processes": 0})
write("RUN_HANDLE.json", {"status": result["status"], "pid": os.getpid(), "terminal": True,
                          "active_processes": 0, "wholecase_CPU_seconds": total})
print(json.dumps(result))
