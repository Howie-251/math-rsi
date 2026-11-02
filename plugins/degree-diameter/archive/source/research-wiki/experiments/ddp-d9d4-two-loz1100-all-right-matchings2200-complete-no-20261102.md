---
type: experiment
node_id: exp:ddp-d9d4-two-loz1100-all-right-matchings2200-complete-no-20261102
title: "9D4两Loz1100全1100右匹配NO：phase10有66端点对条目却最多43/55，真实重复覆盖受限"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-02"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PAPER_INTERFACE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PHASE_CAPACITY.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PHASE_ACTUAL_MAXIMA.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ALL_T_RESULTS.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ATTEMPT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/SOURCE_RECIPE_INPUT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/R4_BOUNDARY_SUPPORTS.csv"
added: 2026-11-02T00:49:19Z
tags: ["ddp", "method-ledger"]
---

# 9D4两Loz1100全1100右匹配NO：phase10有66端点对条目却最多43/55，真实重复覆盖受限

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** fixed_Loz1100_two_copy_rightmatching_complete_endpoint_experiment_outside_stale15

**目标与阶数：** (9,4)；L=1768；条件性n=2200（未据此计纪录）

**距目标的证据：** No2200candidategraph/fresh/BFS/Lean/ARIS. Complete1100rightt-domainactualcrossendpointsetsallfailD4; 2200/9900/degree9andmainmargin432areconditionalonly,notconstructionresults.；P1预测某phase可用old-leg endpoint-pair容量<55，被实际全部phase最小66>=55反驳；容量通过不代表pointcover。P2预测存在真实fullU_t，也被全部1100t无hit反驳。闭球B0/B1/B2/B3 sizes1/9/65/426，B3直接取旧674个distance4边界标签补集，不重源R4/D4BFS；精确U_t=union_(a=0..3)B_a*t*B_(3-a)。relativephase10每t的候选端点对条目66，真实最多43/55，首max t115=(2,5)，故映像至少23重复/至少12缺点；66不是独立NB路线数。四phase可局部满55仍救不了phase10。native.795619759，总1.695619759/10CPU含read/prep/root，0新图/参数/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "outside_stale15": true,
  "old_stale_cell_count_increment": 0,
  "source": {
    "n": 1100,
    "m": 4400,
    "degree": 8,
    "D4": "inherited",
    "law": "RIGHT(j,x)(k,v)=(j+k mod20,x*2^k+v mod55)",
    "label": "55*j+x",
    "positive_generators": [
      [
        1,
        0
      ],
      [
        12,
        33
      ],
      [
        11,
        1
      ],
      [
        16,
        19
      ]
    ],
    "inverse_generators": [
      [
        19,
        0
      ],
      [
        8,
        22
      ],
      [
        9,
        38
      ],
      [
        4,
        26
      ]
    ],
    "oldsource_D4_BFS_reruns": 0
  },
  "hypothetical_only": {
    "n": 2200,
    "m": 9900,
    "maxdegree": 9,
    "main_baseline": 1768,
    "conditional_margin": 432,
    "actual_graph": false
  },
  "old_ball_interface": {
    "B_sizes": [
      1,
      9,
      65,
      426
    ],
    "saved_distance4_boundary_count": 674,
    "B3_complement_size": 426,
    "source_R3_reused": true,
    "source_R4_BFS_reruns": 0,
    "closed_four_terms_exact": true
  },
  "complete_rightmatching_domain": {
    "size": 1100,
    "actual_checked": 1100,
    "fullUt_hits": 0,
    "identityroot_via_common_leftH": true,
    "scope_not_arbitrarymatching": true
  },
  "P1": {
    "prediction": "somephaseendpointpaircapacity<55",
    "actual_min_capacity": 66,
    "needed": 55,
    "verdict": "REFUTED",
    "all20_raw_capacities": [
      108,
      102,
      84,
      112,
      120,
      92,
      90,
      110,
      112,
      102,
      66,
      102,
      112,
      110,
      90,
      92,
      120,
      112,
      84,
      102
    ]
  },
  "P2": {
    "prediction": "atleastoneactualfullUt",
    "actualhits": 0,
    "verdict": "REFUTED_COMPLETE_DOMAIN"
  },
  "phase10_bottleneck": {
    "raw_endpointpair_occurrences": 66,
    "not_independent_NB_route_count": true,
    "actual_max_distinct_targets": 43,
    "target_phase_size": 55,
    "min_duplicate_images": 23,
    "min_missing_targets": 12,
    "firstmax_t_label": 115,
    "firstmax_t_coordinates": [
      2,
      5
    ]
  },
  "allphase_actual_maxima": [
    54,
    53,
    51,
    54,
    55,
    53,
    53,
    55,
    54,
    54,
    43,
    54,
    54,
    55,
    53,
    53,
    55,
    54,
    51,
    53
  ],
  "allphase_full55_t_counts": [
    0,
    0,
    0,
    0,
    6,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    6,
    0,
    0,
    0
  ],
  "locally_full_phases": [
    4,
    7,
    13,
    16
  ],
  "local_full_phases_not_global_repair": true,
  "native_CPU": 0.795619759,
  "read_prep_charge": 0.8,
  "pre_root_CPU": 1.595619759,
  "root_disposition_charge": 0.1,
  "final_case_CPU": 1.695619759,
  "case_CPU_cap": 10,
  "all_processes_terminal": true,
  "candidate_BFS_fresh_Lean_ARIS": 0,
  "old_split_ordinary5cover_NO_notrerun": true,
  "no_automatic_otherS_source_or_twindow": true,
  "negative_Lean_required": false,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PAPER_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PAPER_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PHASE_CAPACITY.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PHASE_CAPACITY.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PHASE_ACTUAL_MAXIMA.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/PHASE_ACTUAL_MAXIMA.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ALL_T_RESULTS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ALL_T_RESULTS.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ATTEMPT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/ATTEMPT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/SOURCE_RECIPE_INPUT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/SOURCE_RECIPE_INPUT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/R4_BOUNDARY_SUPPORTS.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/R4_BOUNDARY_SUPPORTS.csv)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** FixedLoz1100RIGHT-lawCayleysource:H=C20 rightaction2 Z55,(j,x)(k,v)=(j+k mod20,x*2^k+v mod55),label55j+x,fixedS8. Preservebothsourcecopiesall8800oldedges;addone1100edgeperfectmatchingM_t(h)=h*t,all1100t. ThisisexhaustiveleftH-equivariantmatchingdomainonthissource,notarbitrarypointmatching/sourceedits/otherS/host/general9D4. Olderadjacentsingle-split1101andordinary5cover5500NOaredistinctscopesnotrerun. This9D4cellisnotinthe15stale-celllistanddoesnotincreaseitsvisitedcellcount.

**正向保证：** B3reuseisexactlysavedR4boundary674-labelcomplementin0..1099,ofsize426;onlyB0/B1/B2newfinitequery. NooldsourceD4/R4BFSvalidationrerun.；Closedballfour-termunion isequaltoexact-lengthsum<=3endpointunion;B0self/B1identityinclusionandnoncommutativeprefix*t*suffixorderarepreserved.；Atmost4crosscopywalksreducebyimmediatematchingbacktracktoonecross;commonleftHpreservesrightsourceedgesandM_t,soidentityU_ttestsallcrosspairs. SourceD4samecopypathsareinheritedandoldedgespreserved.；All1100twereactuallyvisitedonce,andall20phaseactualmaximaarefromthesamerun,notasecondUtpostprocessorparametersearch. P1andP2arebothhonestlyrefuted.；Phase10actualmax43/55atfirstt115with66rawpairentriesmakescollisionandmissing-pointobstructionsconcrete. FourlocalfullphasewitnessesarenotwholeU_tsuccess.

**仍未完成：** Arbitrarynon-equivariantmatching,oldedgechanges,othergenerators/hosts/helpersandgeneral9D4remainunexcluded. Target2200hasnotbeenconstructedandmain1768isnotimprovedhere. Endpointpairmultiplicity66isnotindependentNBroutecount. Thisisoutsideold15cells;noold-cellcountincrement. GoalACTIVE/oldN8n61PAUSED.

**启发与重启依据：** STOPthisfixedLoz1100/allrightmatchingruleandcopy-rightmatchingladder. Hereunlikethe672source,rawsingle-phasecapacitydoesnotexclude;actualendpointcollisionsdo. Relativephase10failsforeveryt,sootherfourlocallyfullphasescannotcompensateandtotalbadscoretuningisnotjustified. PreserveP1/P2refutationsandspecificphasewitnessratherthanclaimnecessarycapacitysuccessasgraphprogress.

**单独的重启条件：** Onlyanewauthorizedboundedstructuralquestionwithmeaningfullychangededge/matchingruleorhost;noautomaticotherS/source/action/twindow/solverladder. New4D5readgateisaseparateunrunquestionandnotthisrecord.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

