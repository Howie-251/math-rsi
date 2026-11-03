---
type: claim
node_id: claim:dd82-petersen-pair-cycle-budgets
name: "Fifteen Petersen pair-cycle budgets and the double-HS energy floor"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/20261012_C16_root_notes.md"
tags: ["dd82", "n60", "construction", "petersen"]
date: 2026-10-12
added: 2026-10-12T05:00:45Z
---

# Fifteen Petersen pair-cycle budgets and the double-HS energy floor

**status:** `verified`

## Statement
For arbitrary fifteen matching interfaces between six Petersen fibers, each block has exact E_ij=c_ij-r_ij>=0 with r from single/triple matching cycle data. Targets require c=r and r is an integer weighted KG(6,2) degree vector. If deleting either of two fibers gives HS50, total energy is at least50; saved20badseed attains50.

## Honest scope
Necessary conditions, not sixPetersen exclusion or graph witness. DoubleHS impossibility was already covered by the older inducedHS theorem; new result there is quantitative energy floor. Abstract KG feasibility does not imply actual matching realizability.

## Evidence chain
PETERSEN_PAIR_CYCLE_BUDGET.md; actual petersen_pair_cycle_budget.py/.json. Root and C16 read complete proof/source/results. Savedseed T0,F2=0,F3=16,F4=84; solefailedblock45 actualc60 vsrequiredr10. Paper gives explicit abstractKG weighting; script checks necessaryinequalities, no integer-feasibility solver.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

