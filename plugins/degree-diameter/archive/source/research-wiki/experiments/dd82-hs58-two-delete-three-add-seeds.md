---
type: experiment
node_id: exp:dd82-hs58-two-delete-three-add-seeds
title: "Four explicit HS58 graphs expose the deleted-endpoint coverage obstruction"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: ""
duration: "Initial parentCPU0.004991111+BFSchild0.059038,wall0.070688259;refinement parentCPU0.005170480+BFSchild0.060285,wall0.069039065;SAT0"
provenance: "computations/dd82/construction/hs58_two_delete_three_add_seeds_run/"
added: 2026-10-12T05:00:46Z
tags: ["dd82", "n58", "construction", "failed-candidate"]
---

# Four explicit HS58 graphs expose the deleted-endpoint coverage obstruction

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
FixedD01/10-11,A25-26/35-41/2-4. TwoHtypes. Initialfull58/232/8reggraphs106/106bad. Deterministic40vertexcapacitymatching coversall16actualM-badoldpairs, produces83/82bad exclusivelyoldnew,diam3. Bothhaveactualbadpairs0-56/0-57.

## Reasoning
Fourfullgraphs independentlyBFSchecked; allfailed. Refinedgraphscoveralloldold/newnew butcannotcoveroldnew. General analytic t2a3 theorem independentlyclosed domain; planned2x10CPU SAT canceled beforelaunch, noCNF/noSATresult. No graphoptimization oradditionalrun.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

