---
type: experiment
node_id: exp:dd82-polarity73-complete-variable58-20261018
title: "Complete simultaneous polarity73 deletion and graph completion at58:UNKNOWN"
idea_id: "idea:dd82-polarity73-monotone-reduction"
verdict: partial
confidence: high
date: "2026-10-18"
hardware: "Single pinned CPU,4GiB address space,256MiB/file,no proof output"
duration: "Preparation2.829600CPU/2.870178wall s; solver28.043004CPU/28.198339wall s"
provenance: "computations/dd82/construction/polarity73_reduction_run/complete_variable/n58/result.json; complete_variable/n58/sanity.json; complete_variable/CODE_REVIEW.md"
added: 2026-10-18T07:40:52Z
tags: ["dd82", "polarity73", "construction", "full-graph", "unknown"]
---

# Complete simultaneous polarity73 deletion and graph completion at58:UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-polarity73-monotone-reduction`

## Metrics
173093variables,558930clauses. All73survivors and2304addededge decisions free, exact degree8 and complete real distance2 coverage. Eight explicit-adjacency semantic assignments passed. One30CPU/45wall profile returnedUNKNOWN,exit0 atsoft28. No model,certification,or full59run.

## Reasoning
This model is exact within the full saved polarity73 monotone family, not another weak screen or one fixedD. Both degree bounds are guarded by retention, correcting a reviewer formula that would incorrectly constrain deleted vertices. [Source and scope](../../computations/dd82/construction/polarity73_reduction_run/complete_variable/SCOPE.md), [actual result](../../computations/dd82/construction/polarity73_reduction_run/complete_variable/n58/result.json), [bounded delivery](../../prompts/26101316-1/final.md). UNKNOWN does not exclude any order or the family; no unchanged/minor-clause rerun scheduled. The [actual final same-thread review 4](../../reviews/dd82/20261018_polarity73_complete_final_review.json) returned SUCCESS and accepted the scoped exact model and measured result. The finite mechanism is closed at 4/4; the full monotone 58/59 families remain open and the global interval remains 57–61. Workflow closure is not mathematical completion.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

