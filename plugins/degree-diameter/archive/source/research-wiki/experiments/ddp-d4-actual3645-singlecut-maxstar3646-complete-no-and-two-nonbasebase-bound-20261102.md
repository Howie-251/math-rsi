---
type: experiment
node_id: exp:ddp-d4-actual3645-singlecut-maxstar3646-complete-no-and-two-nonbasebase-bound-20261102
title: "A3645单cut最大star完整20044 NO；缓存界排两cut均非base-base子域，仅paper推论"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-02"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/run_once.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/run.cpp; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/CACHE_BINDING.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/PREPARATION_ATTEMPT1.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ALL_EDGES.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ALL_SOURCE_R3_SUPPORTS.bin; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/CACHED_EDGE_CLASS_CAPACITY_POSTPROCESS.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ONE_CUT_TERMINAL_SCOPE_REVIEW.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/NOTE.md; research/ddp/more_graphs_20261027/d11_D4_current3645/ONE_CUT_STAR_INTERFACE.md"
added: 2026-11-02T02:35:02Z
tags: ["ddp", "method-ledger"]
---

# A3645单cut最大star完整20044 NO；缓存界排两cut均非base-base子域，仅paper推论

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** complete_singlecut_maxstar_exclusion_and_cached_two_cut_bound

**目标与阶数：** (11,4)；L=3645；条件性n=3646（未据此计纪录）

**距目标的证据：** Complete20044single-sourceedge maximal-star newrootgate failsall. No candidateoldoldstage,source singlepairdiagnostic or targetgraphBFSentered. Cached edge-class coverage maxima yield only a paper two-nonbasebase-cut capacity bound,no two-cut enumeration or positivegraph.；实际source只有7个10度free。单cut全端点和7free作最大star合法且支配所有子star，d_(G−cuts)(P,t)=dG(P,t)使sourceR3覆盖为新根精确门。完整20044条旧edge全newrootfail，BB18485/BI914/II645均0pass；最优(108,1643)仍缺305，故oldold未进入而非已安全或受损。复用1993R3/新增1652深3，不重原7free球或sourceD4。缓存743holes的单edge端点max覆盖BB438/BI356/II338，所以两cut若均非BB即使共享端点且P<=11也最多712<743、至少漏31；仅paper推论，没有枚两cut或宣称含BB会过。含准备KeyError保守.1及postprocess.05后final2.943111119/15，0新图/solver/Lean/ARIS。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "single_research_record": true,
  "source_n": 3645,
  "source_m": 20044,
  "source_maxdegree": 11,
  "source_free_vertices": 7,
  "free_degree": 10,
  "singlecut_domain": 20044,
  "singlecut_complete": true,
  "maximalstar_size_atmost": 9,
  "newroot_pass": 0,
  "candidate_oldroot_BFS": 0,
  "source_singlepairdiagnostic": 0,
  "best_missing_holes": 305,
  "best_cut": [
    108,
    1643
  ],
  "source_R3_reused": 1993,
  "new_source_depth3_supports": 1652,
  "old_free_R3_recomputed": false,
  "source_D4_revalidation": false,
  "edgeclasses": {
    "base_base": {
      "edges": 18485,
      "newroot_fail": 18485,
      "newroot_pass": 0,
      "oldold_fail": 0
    },
    "base_inserted": {
      "edges": 914,
      "newroot_fail": 914,
      "newroot_pass": 0,
      "oldold_fail": 0
    },
    "inserted_inserted": {
      "edges": 645,
      "newroot_fail": 645,
      "newroot_pass": 0,
      "oldold_fail": 0
    }
  },
  "cached_class_capacity_paper": {
    "status": "CACHED_CLASS_MAXIMA_IMPLY_TWO_NON_BASEBASE_CUTS_NO",
    "source": "ALL_EDGES.tsv, one completed read of all20044 existingrows;no newballsorcutsearch",
    "holes_to_cover": 743,
    "classes": {
      "base_base": {
        "edges": 18485,
        "maximum_holes_covered": 438,
        "witness": [
          108,
          1643
        ]
      },
      "base_inserted": {
        "edges": 914,
        "maximum_holes_covered": 356,
        "witness": [
          1568,
          3510
        ]
      },
      "inserted_inserted": {
        "edges": 645,
        "maximum_holes_covered": 338,
        "witness": [
          3505,
          3510
        ]
      }
    },
    "two_non_basebase_upper": 712,
    "remaining_holes_at_least": 31,
    "scope": "anytwo distinctsourcecuts,possiblysharedends,bothoutsideinducedfirst3444;oneonlynewoldstar+allfree7,nootheroldedits;P<=11",
    "not_claimed": "two-cutenumeration or feasibilitywhenbasebasepresent",
    "conservative_postprocess_CPU_charge": 0.05
  },
  "two_cut_paper_only_no_new_enum": true,
  "two_cut_sharedends_allowed": true,
  "two_cut_maximalstar_size_atmost": 11,
  "holes": 743,
  "old2673_679_and_purepreserved_scopes_unchanged": true,
  "preparation_failure_charge": 0.1,
  "preparation_failure_type": "KeyError",
  "cached_postprocess_charge": 0.05,
  "numeric_case_CPU_before_post": 2.8931111190000003,
  "samecase_CPU": 2.943111119,
  "case_cap": 15,
  "all_processes_terminal": true,
  "new_solver_Lean_ARIS_accepted_target_graph": 0,
  "B_or_natural364helper14_included": false,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/run_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/run_once.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/run.cpp](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/run.cpp)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/CACHE_BINDING.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/CACHE_BINDING.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/PREPARATION_ATTEMPT1.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/PREPARATION_ATTEMPT1.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ALL_EDGES.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ALL_EDGES.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ALL_SOURCE_R3_SUPPORTS.bin](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ALL_SOURCE_R3_SUPPORTS.bin)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/CACHED_EDGE_CLASS_CAPACITY_POSTPROCESS.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/CACHED_EDGE_CLASS_CAPACITY_POSTPROCESS.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ONE_CUT_TERMINAL_SCOPE_REVIEW.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ONE_CUT_TERMINAL_SCOPE_REVIEW.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/NOTE.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/ONE_CUT_STAR_INTERFACE.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/ONE_CUT_STAR_INTERFACE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixedactual3645/20044 max11/D4 with7degree10freevertices. DeleteexactlyoneORIGINALedgeuv,keepallotheroldedges,andaddonezwithonlynewoldspokes. MaximallegalpoolP=all7free union{u,v},size<=9,dominatesalllegalsubstars. All20044maximalstars failnewrootR4,soevery singlecut/onlystar/nootheroldoldedit variantNO. Separatepapercorollary: anytwo distinctcuts,possiblysharingends,bothnon-basebase(relative to first3444labels),P<=11,onlynewstar/nootheroldedits alsoNO by356+356<743. No claim two-cutdomainenumerated or feasiblewhenonebasebasecutpresent. Notgeneral3646/(11,4),otherhosts,repair/multihelper orbroaderedits.

**正向保证：** Sourceformat/degree/freevertices/sourceD4facts areinherited. Only1993oldR3supports reusedand1652missingrootscomputedforthisnewquestion; old7free-R3unionandD4validationnotrepeated.；For eachcut everylegalnewneighborliesinthe7free/cutends pool; maximalpoolhasatmost9<=11spokes andallsubstarsaresubgraphs. A negative maximalstar thereforeexcludesallitslegalsubsets.；AllcutendsinP implydistance-to-Punchangedbycutdeletion,soall20044maxstarnewrootfailuresareexact,beforeoldoldchecks.；Actualedgeclassesuselabelthreshold3444:18485basebase,914baseinserted,645insertedinserted. No unprovedtransitivityorotherlabelsemanticsassumed.；Cachedcoveragecounts438/356/338supportthepaperunionbound712<743fortwononbasebaseedges,evenwithsharedends. Itisnot two-cutenumeration,notafeasibilityclaimwithbasebasepresent.；PreparationfieldKeyError occurredbeforecompilation/numerics anditsconservative.1costispreserved;postprocess.05alsoincluded. Allprocessesterminal,notimerreset.；NoactualnewrootpassmeansoldoldstageNOT_ENTERED,notoldoldproven;noacceptedtargetgraph,solver,Lean,ARISorpositiveverifier.

**仍未完成：** General(11,4)/3646,otheractualsources,oldoldrepair,otherhelpersandbroadereditsremainunexcluded. Two-cutcaseswithatleastonebasebaseedge remainunclassifiedbythisbound. OldpurepreservedNO,old2673/679 andotherhistoricalrecordsremainunchanged;new743holesmustnotbeconflatedwiththem. No graph/parameter/Lean/method/recordclaim. Bworkandnatural364helper14readgatesarenotpartofthisnode.

**启发与重启依据：** Changingfrompurepreservedappendtooneabsorbededge didnotprovide enoughnewrootcoverage: maximalstar dominanceclosesallitslegalspokesubsets,notjustasample. Classmaximafromsavedrowsgiveaconcretetwo-cutnecessaryrestrictionwithoutanothersearch: at leastonebasebasecutwouldberequired. Stoptheexactsinglecutlinewithoutautomaticsecondcut/repair/seed; broaderquestionsneednewexplicitrules. PreserveoldpurepreservedNOand2673/679 scopeswithoutreinterpretation.

**单独的重启条件：** STOP completefixedsource/singleORIGINALcut/onlynewoldstar/nootheredits. No automaticsecondcut/repair/seed; cachednonbasebasepaperboundmustbe inheritedifafutureseparatelyauthorizedtwo-cutquestionisraised. No positivefreshsuite.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

