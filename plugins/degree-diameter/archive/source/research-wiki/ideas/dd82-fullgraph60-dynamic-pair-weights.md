---
type: idea
node_id: idea:dd82-fullgraph60-dynamic-pair-weights
title: "Release the60-point seed structure through dynamic uncovered-pair weights"
stage: piloted
outcome: mixed
added: 2026-10-13T10:46:08Z
based_on: []
target_gaps: ["gap:G4"]
tags: ["dd82", "construction", "fullgraph"]
---

# Release the60-point seed structure through dynamic uncovered-pair weights

**stage:** `piloted`  ·  **outcome:** `mixed`

Completed unrestricted8-regular graph pilot with adaptive positive coverage weights and exact reversal ban; further unchanged computation paused.

## Thesis
All simple degree-preserving two-switches are eligible except the immediate inverse. Positive pair weights are increased at local minima by an exact first-improvement jump. Direction feedback was implemented; one real run escaped originalC5 and fiber constraints but accepted-trajectory best stayed20. Two same-thread Gemini reviews completed; route paused, general domain open.

## Key risks
No target or arbitrary-graph exclusion. Non-stasis does not imply convergence. Only original representation/permutation was tested. Entropic barrier and a global lower bound20 were not established. No unchanged new search is scheduled.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

