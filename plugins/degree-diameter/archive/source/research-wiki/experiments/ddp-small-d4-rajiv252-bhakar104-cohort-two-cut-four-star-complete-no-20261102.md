---
type: experiment
node_id: exp:ddp-small-d4-rajiv252-bhakar104-cohort-two-cut-four-star-complete-no-20261102
title: "小D4三literal两cut四星完整NO：Rajiv252新根全拒，Bhakar104 a/b新根过而旧旧失败"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-02"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/SOURCE_BINDING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/INPUT_BINDING_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TWO_SOURCE_SCOPE_REVIEW.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/a_unlettered_run/FIRST_OLD_FAILURE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/b_run/FIRST_OLD_FAILURE.json"
added: 2026-11-02T02:12:11Z
tags: ["ddp", "method-ledger"]
---

# 小D4三literal两cut四星完整NO：Rajiv252新根全拒，Bhakar104 a/b新根过而旧旧失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** complete_two_cut_four_star_cohort_exclusion

**目标与阶数：** 多目标：Rajiv252→[5, 4, 253]／L=252；Bhakar104 officialunlettered(aliasa)→[4, 4, 105]／L=104；Bhakar104b→[4, 4, 105]／L=104；Bhakar104c oldonly→[4, 4, 105]／L=104（逐变体，不合成一个距离）

**距目标的证据：** No legalnewtargetgraph. Exactnewroot supportgate for allfixed-source disjointcutpairs; only104a/b surviving16/24cases constructactualin-memorycandidate andrunordinaryoldrootBFS to firstfailure. Savedoldpairs source4/new5,source singlepairdiagnostic oneeach. No sourceD4allroot revalidation.；两cut全端点P给d_(G−cuts)(P,t)=dG(P,t)，所以source closedR3四球并是newroot R4精确门。252：198135raw−2520共享=195615，全拒/max覆盖222，0candidateoldroots。104a/b：各21528−624=20904完整，newroot通过16/24，actualoldold全fail16/24，ordinaryoldrootBFS18/27。首a0→19与b0→22均source4→candidate5，所示旧路含cut0–8；source单pair诊断各1不算source D4验收，不称旧路唯一。旧104c20904No继承0重跑；a仅实验alias，官方raw是104_d4D4.txt。原caseCPU252=2.151099672/10、104双源=.574206988/10分别保留，无重置或重复编译计费。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "single_cohort_research_record": true,
  "new_actual_source_cases": 3,
  "source252": {
    "n": 252,
    "m": 630,
    "degree": 5,
    "rawpairs": 198135,
    "sharedpairs": 2520,
    "legal": 195615,
    "newrootpass": 0,
    "max_sourceR3P": 222,
    "oldrootBFS": 0,
    "newdepth3supports": 252,
    "source_singlepairdiagnostic": 0,
    "caseCPU": 2.151099672,
    "casecap": 10
  },
  "source104a": {
    "officialraw": "104_d4D4.txt",
    "experimentalias": "a_unlettered",
    "n": 104,
    "m": 208,
    "degree": 4,
    "rawpairs": 21528,
    "sharedpairs": 624,
    "legal": 20904,
    "newrootpass": 16,
    "oldoldfail": 16,
    "oldrootBFS": 18,
    "newdepth3supports": 104,
    "source_singlepairdiagnostic": 1,
    "first_failure": {
      "edgeindices": [
        0,
        17
      ],
      "cuts": [
        [
          0,
          8
        ],
        [
          4,
          12
        ]
      ],
      "newroot_cover_pass": true,
      "oldroot": 0,
      "target": 19,
      "newdistance": 5,
      "source_distance": 4,
      "newroute": [
        0,
        14,
        6,
        31,
        23,
        19
      ],
      "one_source_route": [
        0,
        8,
        2,
        27,
        19
      ]
    }
  },
  "source104b": {
    "officialraw": "104b_d4D4.txt",
    "n": 104,
    "m": 208,
    "degree": 4,
    "rawpairs": 21528,
    "sharedpairs": 624,
    "legal": 20904,
    "newrootpass": 24,
    "oldoldfail": 24,
    "oldrootBFS": 27,
    "newdepth3supports": 104,
    "source_singlepairdiagnostic": 1,
    "first_failure": {
      "edgeindices": [
        1,
        16
      ],
      "cuts": [
        [
          0,
          8
        ],
        [
          4,
          12
        ]
      ],
      "newroot_cover_pass": true,
      "oldroot": 0,
      "target": 22,
      "newdistance": 5,
      "source_distance": 4,
      "newroute": [
        0,
        4,
        60,
        52,
        14,
        22
      ],
      "one_source_route": [
        0,
        8,
        16,
        47,
        22
      ]
    }
  },
  "source104ab_jointcaseCPU": 0.574206988,
  "source104ab_casecap": 10,
  "source104c_oldcomplete_domain": 20904,
  "source104c_newrun": false,
  "source_newroot_support_query_is_not_D4validation": true,
  "oldsource_D4validation_BFS": 0,
  "new_field_solver_Lean_ARIS": 0,
  "new_accepted_complete_target_graphs": 0,
  "cutroute_witnesses_not_uniquegeodesic_claims": true,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED",
  "all_processes_terminal": true
}
```



**从属变体：**
```json
[
  {
    "label": "Rajiv252",
    "target": [
      5,
      4,
      253
    ],
    "target_Delta": 5,
    "target_D": 4,
    "savedL": 252,
    "actual_order": null,
    "domain": 195615,
    "newrootpass": 0,
    "max_sourceR3P": 222,
    "oldrootBFS": 0,
    "status": "COMPLETE_NO"
  },
  {
    "label": "Bhakar104 officialunlettered(aliasa)",
    "target": [
      4,
      4,
      105
    ],
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "actual_order": null,
    "domain": 20904,
    "newrootpass": 16,
    "oldoldfail": 16,
    "oldrootBFS": 18,
    "status": "COMPLETE_NO"
  },
  {
    "label": "Bhakar104b",
    "target": [
      4,
      4,
      105
    ],
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "actual_order": null,
    "domain": 20904,
    "newrootpass": 24,
    "oldoldfail": 24,
    "oldrootBFS": 27,
    "status": "COMPLETE_NO"
  },
  {
    "label": "Bhakar104c oldonly",
    "target": [
      4,
      4,
      105
    ],
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "domain": 20904,
    "status": "OLD_COMPLETE_NO_INHERITED_NOT_RERUN"
  }
]
```

**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/SOURCE_BINDING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/SOURCE_BINDING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/INPUT_BINDING_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/INPUT_BINDING_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TWO_SOURCE_SCOPE_REVIEW.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TWO_SOURCE_SCOPE_REVIEW.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/a_unlettered_run/FIRST_OLD_FAILURE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/a_unlettered_run/FIRST_OLD_FAILURE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/b_run/FIRST_OLD_FAILURE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/b_run/FIRST_OLD_FAILURE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** One aggregate researchcohort,notanewmethod. For each actualRajiv252,officialBhakar104unlettered(aliasa),and104b literal independently: delete any unorderedpair ofvertex-disjoint ORIGINAL sourceedges,add onenewvertex joinedtoallfourendpoints,keepallotheredges. Complete195615/20904/20904domainsNo. Old104c same20904No inheritedonly,notrerun. No claimgeneral253/(5,4),105/(4,4),otherhosts,thirdcut,oldoldrepair,othernewneighbors ormultiplehelpers.

**正向保证：** Allcutends inP imply restartatlastcut downstreamendpoint,so minimumsourceP-distance isunchanged bydeletingthecuts; sourceclosedR3exactlydecidesnewrootR4.；Simple-source domainchoose(m,2)minus sumchoose(deg(v),2) iscomplete; engine visits alllegalpairs withoutunprovedsymmetryreduction.；Onlynewrootpass candidates areactuallyconstructed; oldroot BFS includesallnewandoldtargets andstops atfirstactualfailure,which iscompleteforrejectingthatcandidate.；Source4/new5savedpairs demonstrate actualold-route damage. Showingoneoldroutecontains0–8doesnotclaimuniquegeodesic; candidateBFSdistance5 istherefutation.；Source252raw and104raw areheaderlessedgelists,notmisparsedheaders. Internal104a is anexperimentaliasforofficialunlettered104_d4D4.txt.；Old104ccompleteNo islinkedandnotrerun. NewsourceD4validation,field,solver,Lean,ARISandacceptedgraphincrementsarezero.

**仍未完成：** General(5,4)/(4,4),otherfixedsources,threecuts,oldoldrepair,multiplehelpers orotherstarneighbors remainunexcluded. No targetgraph,globalrecord,parameter,Lean orindependentmethodclaim. SourceD4 andcohortnonisomorphism are inheritedprimaryfacts,notnewchecks.

**启发与重启依据：** Newroot-first gate is exactbecause allcutends belongtoP,notbecause sourceD4 survivesedge deletion. The252 newrootexistence prediction is refuted completely;104a/b newrootpredictions supportedyet everyactualsurvivorfailsoldold. Preserve firstshortestdistance5witnesses toidentify theold-route obligation that a newroot coverdoesnotresolve. Stopthisexactarchitecture withoutautomaticthirdcut/repair/seed orsource ladder.

**单独的重启条件：** STOP exactfixedsources/two-disjoint-originalcuts/one4star architecture; no freshpositiveverification andno automaticthirdcut/repair/seed. A separatelyauthorized materiallychangedrule must retainthisclosedscope.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

