---
type: experiment
node_id: exp:m7-131-budget-transfer
title: "Same successful record does not establish 131-edge colorability"
idea_id: "idea:m7-certificate-scope"
verdict: partial
confidence: high
date: ""
hardware: ""
duration: ""
provenance: "development/propertyb-rebuild/forward-use/SCOPE_RESULTS.json"
added: 2026-11-01T11:06:40Z
tags: []
---

# Same successful record does not establish 131-edge colorability

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:m7-certificate-scope`

## Metrics
M=131; degree budget917; two profiles350 versus337; at v71 unit-lock guarantee2; old worst profile has U=2611935984095/2580454409544 and 4064403701937/4014040192624 in the two tested layouts.

## Reasoning
The reusable formulas remain available, but input coverage and strictness are not preserved. This diagnostic tests only the two old layouts of one necessary local profile; it does not prove a noncolorable hypergraph or rule out all other layouts.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

