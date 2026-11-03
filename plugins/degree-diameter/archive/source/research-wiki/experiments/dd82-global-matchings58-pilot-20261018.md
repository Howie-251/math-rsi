---
type: experiment
node_id: exp:dd82-global-matchings58-pilot-20261018
title: "八轮全局匹配生成8张完整58点八正则图：均非目标"
idea_id: "idea:dd82-global-matchings58"
verdict: partial
confidence: high
date: "2026-10-18"
hardware: "One pinnedCPU,4GiBAS,256MiB/file; no solver or proof log"
duration: "5.450637CPU /5.6254823357wall s including all8 independentBFS"
provenance: "computations/dd82/construction/global_matchings58_run/pilot/{results.json,process_result.json,independent_checks.json,diagnostics.json}"
added: 2026-10-18T07:56:48Z
tags: ["dd82", "construction", "full-graph", "negative-pilot"]
---

# 八轮全局匹配生成8张完整58点八正则图：均非目标

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-global-matchings58`

## Metrics
8/8 complete and independently checked; all n58,m232,degree8,diameter3; badpairs180,200,201,177,199,190,183,194. Bestseed3:16triangles,159oldedgesretained33deleted. Eight different labelededge tables.

## Reasoning
Eight full simple58vertex232edge8regulargraphs were generated; all independently BFSchecked, all diameter3 and177–201badpairs. They remove31–38of192oldgeometricedges, so no longer lie in the earlier fixed-D monotone family. Only labelededge-table distinctness checked, not nonisomorphism. DirectionGemini1 accepted mathematicalrule; actualsource/results accepted by same-thread Gemini round2. No target, completeorder or family exclusion. Prefix capacity diagnosis studies saved intermediategraphs before any nextbatch. See [plan](../../computations/dd82/construction/global_matchings58_run/PLAN.md), [actual CPU result](../../computations/dd82/construction/global_matchings58_run/pilot/process_result.json), [independent BFS](../../computations/dd82/construction/global_matchings58_run/pilot/independent_checks.json) and [diagnostics](../../computations/dd82/construction/global_matchings58_run/pilot/diagnostics.json).

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

