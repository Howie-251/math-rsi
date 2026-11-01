---
type: experiment
node_id: exp:m7-424-replay
title: "Author and falling-factorial complete replay"
idea_id: "idea:m7-certificate-scope"
verdict: yes
confidence: high
date: ""
hardware: ""
duration: ""
provenance: "development/propertyb-rebuild/forward-use/COMMANDS.json"
added: 2026-11-01T11:06:40Z
tags: []
---

# Author and falling-factorial complete replay

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:m7-certificate-scope`

## Metrics
M=130; profiles=424; groups=17+337+64+6; integer vectors=2115296; maximum=2257893910847/2257897608351; both exit0.

## Reasoning
For finite simple 7-uniform hypergraphs with at most 130 edges, the supplied mathematical reduction and actual-profile selection connect every original putative counterexample to one of 424 exact probability profiles, whose strict values imply an original proper coloring. Author and independent runs exit 0; all 424 fractions agree. Independent probability representation uses falling-factorial injections and enumerates 2115296 common integer vectors. Maximum is 2257893910847/2257897608351. This is same-family provisional development validation of a computer-assisted candidate; no new Lean, cross-family final audit or public-record novelty check. It does not establish colorability with 131 edges: the new degree budget is 917; the two-lock domain becomes 350 rather than 337; the old 71-vertex selection guarantees only two unit locks; the tested old worst profile in both old layouts is nonstrict. See REPORT.md and SCOPE_RESULTS.json.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

