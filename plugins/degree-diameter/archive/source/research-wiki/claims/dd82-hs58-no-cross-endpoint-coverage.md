---
type: claim
node_id: claim:dd82-hs58-no-cross-endpoint-coverage
name: "No-cross HS deletion endpoints force auxiliary bad-pair degree sum at least five"
description: ""
node_type: claim
status: verified
provenance: "reviews/dd82/20261012_C17_C18_root_notes.md"
tags: ["dd82", "construction"]
date: 2026-10-12
added: 2026-10-12T06:02:54Z
---

# No-cross HS deletion endpoints force auxiliary bad-pair degree sum at least five

**status:** `verified`

## Statement
For two disjoint HS deletions with no original cross-edge, every full two-port endpoint covers at least seven H labels directly or through H. Every pair at H-distance greater than two has endpoint-degree sum>=5. At five additions, existing67types reduce to type3.

## Honest scope
All old additions and attachments allowed, but only no-cross disjointD. AdjacentD and disjointD with an original cross-edge are not excluded. Repaired exception-budget proof checked locally; no external acceptance or Lean claim.

## Evidence chain
HS58_NO_CROSS_ENDPOINT_COVERAGE.md includes affected-partner additions: at most a exceptional old-neighbor colors; repairing the deleted edge consumes one such allowance. Root checked complete proof and hs58_two_delete_no_cross_filter.py with actual67-to1 witnesses. The rejected shortcut is explicitly withdrawn.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

