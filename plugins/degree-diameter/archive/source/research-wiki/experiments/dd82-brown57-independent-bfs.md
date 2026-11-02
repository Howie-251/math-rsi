---
type: experiment
node_id: exp:dd82-brown57-independent-bfs
title: "Independent verification of the explicit Brown57 edge list"
idea_id: "idea:dd82-brown57-extension"
verdict: yes
confidence: high
date: ""
hardware: ""
duration: ""
provenance: "computations/dd82/construction/brown57.verification.json"
added: 2026-10-11T07:35:13Z
tags: ["dd82", "construction"]
---

# Independent verification of the explicit Brown57 edge list

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:dd82-brown57-extension`

## Metrics
57 vertices; 224 edges; degree histogram 7:8 and 8:49; 1596 unordered pairs checked, distances 1:224 and 2:1372; zero uncovered pairs.

## Reasoning
Independent BFS reads the expanded edge list without importing the construction code. Establishes an explicit lower-bound witness, not an optimality claim or a Lean theorem.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

