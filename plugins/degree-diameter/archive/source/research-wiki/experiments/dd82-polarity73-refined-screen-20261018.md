---
type: experiment
node_id: exp:dd82-polarity73-refined-screen-20261018
title: "Polarity73 refined screen:58 SAT deletion excluded by forced edge;59 UNKNOWN"
idea_id: "idea:dd82-polarity73-monotone-reduction"
verdict: partial
confidence: high
date: "2026-10-18"
hardware: "One pinned CPU/order,4GiB address space; no proof logging"
duration: "58 CPU0.963712s/wall1.134302s;59 CPU27.996050s/wall28.192344s; preparation0.694486/0.696686CPU s; no parallel wall summation"
provenance: "computations/dd82/construction/polarity73_reduction_run/refined/n58/result.json; refined/n59/result.json; refined/n58/forced_completion_analysis.json; proofs/dd82/construction/POLARITY73_REFINED58_FORCED_EDGE.md"
added: 2026-10-18T07:27:51Z
tags: ["dd82", "construction", "polarity73", "necessary-screen", "human-feedback"]
---

# Polarity73 refined screen:58 SAT deletion excluded by forced edge;59 UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-polarity73-monotone-reduction`

## Metrics
58:18325vars73630clauses,REFINED_SCREEN_SAT_CHECKED,449oldbadpairs,40newedges needed.59:18267vars73399clauses,UNKNOWN exit0 at soft28s. Nine explicit semantic assignments passed for each;58 complete DIMACS/direct predicates checked. Both single discovery runs30CPU/45wall; no proof output.

## Reasoning
[Short fixed-D proof](../../proofs/dd82/construction/POLARITY73_REFINED58_FORCED_EDGE.md) derives forced0-2 from saturated5/61, then unit1 cannot reach saturated0/2 with its one new edge because their fixed neighborhoods are disjoint. This excludes all monotone completions of this one actual deleted set, not the full58family. Arbitrary screen choice overflow72 was not used. [Independent same-family recomputation](../../computations/dd82/construction/polarity73_reduction_run/refined/n58/FIXED_DELETION_PROOF_CHECK.md) confirms the witness.59 remains undecided; no target graph or whole-order exclusion. [Same-thread Gemini round3](../../reviews/dd82/20261018_polarity73_refined_results_review.json) actually returned SUCCESS and accepted the scoped refined results and fixed-D proof. Root corrected its proposed degree equation and unsupported runtime forecast; neither is used in the next complete model. Fixed-D completion source exists but actual input/solve were unnecessary and not executed.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

