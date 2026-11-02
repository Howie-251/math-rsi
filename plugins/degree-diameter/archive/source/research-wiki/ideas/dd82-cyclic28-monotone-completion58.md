---
type: idea
node_id: idea:dd82-cyclic28-monotone-completion58
title: "循环28列覆盖源只删旧关联并补两列"
stage: archived
outcome: negative
added: 2026-10-18T10:42:18Z
based_on: []
target_gaps: ["gap:G4", "gap:G13"]
tags: ["DD82", "n58", "construction"]
---

# 循环28列覆盖源只删旧关联并补两列

**stage:** `archived`  ·  **outcome:** `negative`

Complete source family excluded by paper proof before formal input or solver.

## Thesis
Use a concrete six-set cyclic28 cross-incidence source covering all left far pairs, retain/delete old incidences, add two free columns, and choose right factor and matching jointly. A general demand-versus-degree obstruction excludes ALL such far-cover sources, not just the chosen A.

## Key risks
Paper exclusion limited to specified source and monotonicity; full free-C remains open. At least4old columns must gain source nonedges in any successful nonmonotone repair, but no repair exists yet. Do not restart A/seed/cycle/time ladders; unused encode.py is not accepted or tested code.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


## Subsequent bounded diagnosis, not a reopened experiment

[LEFT_FACTOR_FREEDOM_DIAGNOSIS.md](../../computations/dd82/construction/cyclic28_completion58_run/LEFT_FACTOR_FREEDOM_DIAGNOSIS.md) keeps C0 fixed and swaps0/1 in the left circle. Its graph square loses precisely two old near pairs, which two added-column supports can cover before degree-preserving deletions. Thus source and left-cover geometry alone do not force the original labelled C28. The old-high reachable set changes from three translates to S_h union N_H(S_h); for h0 its size actually drops18to17. This is a concrete change in a premise, not a feasible repair or evidence that all capacity obstructions disappear. Actual row-degree restoration, post-deletion left coverage and all right/cross coverage remain unconstructed. No new model, input or solver is authorized or queued by this diagnosis.
