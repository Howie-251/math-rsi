---
type: experiment
node_id: exp:ddp-stale-d8d4-two684-all-hleft-equivariant-matchings1368-no-20261101
title: "8D4两份684一匹配：全部233928个H左等变参数完整NO；共享342与独立轨道全域两预测均失败"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/HISTORY_SOURCE_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_INTERFACE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/run_gate_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_SOURCE_LITERAL_BINDING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/OLD_LENGTH_LE3_ENDPOINT_SETS.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ALL342_T_SLOT_RESULTS.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ALL342_T_SLOT_SUMMARY.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_EQUIVARIANT_MATCHING_DOMAIN.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/full_gate_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_PER_SIGMA_MASKS.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_ALL_NEW_PARAMETERS.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FINAL_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ROOT_DISPOSITION.json; research/ddp/m1_sources/graph_7_4_n684.txt; research/ddp/m1_sources/684_recovered_construction.json; research/ddp/m1_sources/recover_684.py; research/ddp/m1_sources/SOURCE_NOTES.md"
added: 2026-11-01T20:36:58Z
tags: ["ddp", "method-ledger"]
---

# 8D4两份684一匹配：全部233928个H左等变参数完整NO；共享342与独立轨道全域两预测均失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** complete_fixed_host_equivariant_matching_route_exclusion

**目标与阶数：** (8,4)；L=1100；条件性n=1368（未据此计纪录）

**距目标的证据：** No1368candidate graph emitted orBFS. Complete exact cross-slot endpoint gate excludesD<=4;inherited sourceD4 gives universal candidateD<=5,so rejectedfamily members haveD5 by proof.；初“684是Cayley”前提由实际primary纠正：星号含former672，当前684不vertex-transitive，H342左作用有两个自由轨道，源边为right h*s。保两sourcecopy全部4788旧边＋684matching得名义1368/5472/all8regular；只欠cross≤4。共享t预测失败：342全NO，t0/171为Aut棱柱D5剪枝，其余340均首0→0槽fail。不能据此排独立轨道参数；后由完整left-equivariant域与精确一cross分解正式授权全域。完整233928=旧342严格skip＋233586新案；id116622、swap116964全首0→0槽fail，后三槽NOT_TESTED，0未决/命中。首新(id,0,1)缺138坐标、firstmissing group1。第二全覆盖预测亦失败；累计2.923628479/10CPU，一sourceparse/一≤3endpointDP，full阶段0重parse/重DP/旧342重测，0图/BFS/Lean/付费。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 3201,
  "baseline": 1100,
  "Moore_space": 2101,
  "Moore_space_is_not_constructibility": true,
  "hypothetical_order": 1368,
  "hypothetical_edges": 5472,
  "hypothetical_degree": 8,
  "hypothetical_main_margin_if_legal": 268,
  "source_name": "Michel_684",
  "source_author": "Michel de Messieres",
  "source_communication_date": "2026-10-05",
  "source_n": 684,
  "source_m": 2394,
  "source_degree": 7,
  "source_D4_inherited": true,
  "source_public_reproduction_newgraph_increment": 0,
  "initial_Cayley_assumption_refuted": true,
  "current684_Cayley": false,
  "main_star_also_refers_to_former672": true,
  "source_group_order": 342,
  "source_free_left_orbits": 2,
  "source_forward_edge": "h*s,rightvoltage",
  "actual_group_recipe": {
    "group": "H=C38 semidirect_23 C9, order342",
    "coordinates": "(a,b), 0<=a<38, 0<=b<9",
    "multiplication": "(a,b)*(c,d)=((a+23^b*c) mod38,(b+d) mod9)",
    "inverse": "(a,b)^-1=((-23^(-b)*a) mod38,(-b) mod9)",
    "vertex_label": "342*tau+9*a+b",
    "forward_neighbor": "(tau,h) -> (rho,h*s), s in S[tau][rho]",
    "literal_reconstruction_code_binding": "recover_684.py: u=encode(b,(a,k)); for c and s in S[b][c], v=encode(c,mul((a,k),s)); encode(b,g)=b*m*n+g[0]*n+g[1]. Read only, not imported/executed.",
    "S00": [
      [
        4,
        4
      ],
      [
        8,
        5
      ],
      [
        25,
        3
      ],
      [
        29,
        6
      ]
    ],
    "S01": [
      [
        2,
        2
      ],
      [
        2,
        6
      ],
      [
        24,
        3
      ]
    ],
    "S10": [
      [
        26,
        7
      ],
      [
        24,
        3
      ],
      [
        2,
        6
      ]
    ],
    "S11": [
      [
        10,
        1
      ],
      [
        23,
        6
      ],
      [
        26,
        8
      ],
      [
        29,
        3
      ]
    ],
    "symmetry_used_for_proposed_gate": "common left H multiplication, transitive within each source tau type; not a one-orbit Cayley action"
  },
  "matching_domain": "S2 x H342 x H342",
  "matching": "(h,sigma,0)--(h*t_sigma,pi(sigma),1)",
  "inverse_crossing": "f^-1;no conditiont1=t0^-1",
  "all_sourcecopy_edges_retained": 4788,
  "matching_edges": 684,
  "exact_cross_gate": "one crossing plus oldlegs total<=3;for all4typeslots OR ofindependent meetingtype0/1 masks equalsall342",
  "three_cross_paths_reduce_by_consecutive_inverse_cancellation": true,
  "shared_domain": 342,
  "shared_aut_pruned_labels": [
    0,
    171
  ],
  "shared_nonautomorphism_first00_failures": 340,
  "shared_positive_prediction_supported": false,
  "shared_stage_CPU_seconds": 1.846522801,
  "complete_equivariant_domain": 233928,
  "old_shared_skipped": 342,
  "new_parameters_complete": 233586,
  "pi_id_new": 116622,
  "pi_swap_new": 116964,
  "new_parameters_failed_first_slot": [
    0,
    0
  ],
  "firstslot_evaluations": 233586,
  "later_three_slots": "NOT_TESTED_AFTER_FIRST_FAILURE",
  "unvisited_parameters": 0,
  "full_positive_prediction_supported": false,
  "first_new_failure": {
    "pi": "id",
    "t0": 0,
    "t1": 1,
    "slot": [
      0,
      0
    ],
    "actual_missing_count": 138,
    "first_missing_group_label": 1,
    "missing_mask_hex": "0x2c80890124229d469e17af5af22e421063d86ce0e004a0cae001c20247f9222a5a1544d5872c089222f5be"
  },
  "source_raw_parses_total": 1,
  "old_le3_endpoint_DP_generations": 1,
  "full_stage_source_parses": 0,
  "full_stage_old_DP_repeated": false,
  "shared_parameters_retested": 0,
  "candidate_graphs_generated": 0,
  "source_or_candidate_BFS": 0,
  "Lean_paidreview_runs": 0,
  "wholecase_CPU_seconds": 2.923628479,
  "CPU_budget_seconds": 10,
  "complete_fixed_family_exclusion": true,
  "all_processes_terminal": true,
  "next_readonly_priority": "(5,3)existingGQpairingUNKNOWN actualinterface;nooldtimerresume"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/HISTORY_SOURCE_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/HISTORY_SOURCE_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/run_gate_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/run_gate_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_SOURCE_LITERAL_BINDING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_SOURCE_LITERAL_BINDING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/OLD_LENGTH_LE3_ENDPOINT_SETS.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/OLD_LENGTH_LE3_ENDPOINT_SETS.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/RUN_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ALL342_T_SLOT_RESULTS.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ALL342_T_SLOT_RESULTS.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ALL342_T_SLOT_SUMMARY.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ALL342_T_SLOT_SUMMARY.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_EQUIVARIANT_MATCHING_DOMAIN.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_EQUIVARIANT_MATCHING_DOMAIN.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/full_gate_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/full_gate_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_PER_SIGMA_MASKS.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_PER_SIGMA_MASKS.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_ALL_NEW_PARAMETERS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FULL_ALL_NEW_PARAMETERS.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FINAL_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FINAL_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/ROOT_DISPOSITION.json)；[research/ddp/m1_sources/graph_7_4_n684.txt](../../research/ddp/m1_sources/graph_7_4_n684.txt)；[research/ddp/m1_sources/684_recovered_construction.json](../../research/ddp/m1_sources/684_recovered_construction.json)；[research/ddp/m1_sources/recover_684.py](../../research/ddp/m1_sources/recover_684.py)；[research/ddp/m1_sources/SOURCE_NOTES.md](../../research/ddp/m1_sources/SOURCE_NOTES.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** OnlythefixedactualMichel684simple7regularD4two-orbitright-voltagehost. Keep two identical684copies intact,andaddoneperfectmatchingcommutingwiththecommonfreeLEFT H342action. Precisely f(h,sigma)=(h*t_sigma,pi(sigma)),pi inS2,independentt0,t1 inH342;reversecrossing usesf^-1. Complete233928parameterfamily includesold342sharedid/t0=t1;notarbitrarynon-H-equivariantmatchings,otherhosts,otheraddedconnections or general8D4.

**仍未完成：** Arbitrarynon-H-equivariantmatchings,otherhosts,differentaddedconnections and generalN(8,4) remain open. Source is public reproduction,auxiliaryendpoint gates do not produce newgraph/parameter/Lean/method results.

**启发与重启依据：** STOP thisfixedhost entireH-left-equivariantone-matchingfamily. Sourceprimary correction changedtheactualsymmetryandgenerator beforecomputation. Independentt0/t1andpi were a justified changedrule that mightcomplementtwointermediate-type routes;completefactorization made a finitefull test possible. Allnewcases stillfailthefirstcrossslot,notan aggregatebadpairscore. Do notextendtoarbitrarymatching/anotherhost/field/morecrossedges automatically. Nextrootpriority is read-only inspection of theexisting(5,3)GQpairingUNKNOWN actualinterface,notresumingitsoldtimer or runningfull3cut/othermatchingsearch.

**单独的重启条件：** Anotheropenparameter or a materiallynewroute-generatinginterface with a concrete bounded question. TheexistingGQpairingUNKNOWN may be read for itsactualscope;no numeric continuation authorized here.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

