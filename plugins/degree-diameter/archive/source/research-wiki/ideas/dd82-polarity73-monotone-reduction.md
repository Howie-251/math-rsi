---
type: idea
node_id: idea:dd82-polarity73-monotone-reduction
title: "Variable deletion and monotone completion from polarity73"
stage: archived
outcome: unknown
added: 2026-10-13T16:40:42Z
based_on: []
target_gaps: ["gap:G4"]
tags: ["dd82", "construction", "finite-geometry"]
---

# Variable deletion and monotone completion from polarity73

**stage:** `archived`  ·  **outcome:** `unknown`

Updated 2026-10-18 from terminal profiles and the actual final same-thread review. The bounded mechanism is closed at 4/4; the research Goal remains active under the human-in-loop plan. Choose arbitrary 58/59 survivors of the saved polarity73 geometry, preserve all retained ambient edges, and add missing edges. This is an artificial monotone construction family; arbitrary orders 58–61 remain open.

## Actual results
Pure reductions exclude all monotone 60/61 and require at least 8 deleted outer points at 58/59. The two-fiber 59 shape is excluded by coverage; the saved fixed-label 58 example has a complete 98-node / 7-code exact-cover enumeration, all failing the repair capacity condition.

Both initial variable-deletion screens actually ran and returned SCREEN_SAT_CHECKED: 58 has 2830 variables / 12508 clauses; 59 has 2772 / 12277. Both decoded deletion sets are uncompletable by unit-deficit / saturated-neighbor capacity contradictions. A screen assignment is not a target graph, and these two exclusions do not close the 58/59 family. See [actual experiment](../experiments/dd82-polarity73-initial-screens-20261013.md).

## Thesis
Exact deficits and lost common neighbors give necessary deletion screens before full completion. The observed empty repair domains motivate universal unit-deficit neighbor-choice constraints. Run `dd82-v3-polarity73-reduction-20261013`; task [26101316-1](../../prompts/26101316-1/task.md).

## Final boundary and review status
The [round 2 response](../../reviews/dd82/20261013_V3_polarity73_initial_results_review.json) approved a refinement direction at the historical checkpoint; it did not accept an experiment that had not yet run. The refinement and complete-variable 58 model subsequently ran on 2026-10-18. The [final same-thread round 4](../../reviews/dd82/20261018_polarity73_complete_final_review.json) returned SUCCESS and accepted the scoped delivery, exact complete model and measured UNKNOWN result. The finite loop is closed at 4/4. This does not close the full 58/59 family or the DD82 Goal. No unchanged or minor-clause profile is scheduled. See [final delivery](../../prompts/26101316-1/final.md).

## User feedback and remaining scope
[Progress, remaining 61-point space and user comments](../DD82_PROGRESS_AND_COMMENTS_20261018.md). No change to 57 ≤ N(8,2) ≤ 61. The separate 61-point global-run structure manuscript remains a draft.

## 2026-10-18 actual refinement
The screen was prepared and run once per order without proof logging. At 58 it returned SAT in 0.963712 CPU seconds, but the saved deletion set is impossible by a forced 0–2 edge followed by the empty repair domain of vertex 1. At 59 it returned UNKNOWN in 27.996050 CPU seconds. [Actual refinement experiment](../experiments/dd82-polarity73-refined-screen-20261018.md). Same-thread round 3 accepted these scoped results. Fixed-D completion source was not run because the saved deletion set already has a shorter contradiction.

The exact complete-variable 58 model then ran once: 173093 variables / 558930 clauses, 28.043004 CPU / 28.198339 wall seconds, UNKNOWN. All survivor bits and possible new-edge decisions remained free; both degree bounds were guarded by retention. No complete 59 input or solve was prepared. [Complete-model experiment](../experiments/dd82-polarity73-complete-variable58-20261018.md). The three new solver profiles total 57.002766 CPU seconds; this is not total elapsed research time. No target or full-family exclusion resulted.

## Current handoff
The registered [global matching mechanism](../../computations/dd82/construction/global_matchings58_run/PLAN.md) generates a complete 58-point 8-regular graph from eight perfect matchings, allowing every ambient old edge to be omitted. At this synchronization checkpoint its direction review is in flight and source implementation is in progress; no experiment has run. This is a new generation rule, not a relabeling or budget extension of the closed monotone model. [Current readable progress](../../research/progress.html).

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

