# Resource and existing H9 data inspection

Inspected 2026-10-29 15:13:24 UTC. Read-only extraction of saved inputs and process/resource state; no graph generation, source BFS, radius-ball construction, search or solver was run. Existing Wiki and research plans were not edited.

## Available resources and jobs

- CPU affinity exposes 128 logical CPUs (0–127), but cgroup `cpu.max` is `5500000 100000`, i.e. a 55-CPU aggregate time quota. Do not interpret affinity 128 as a 128-core compute allocation.
- Cgroup memory limit: 300.00 GiB; sampled current usage: 3.45 GiB; cap minus current usage: 296.55 GiB. Host MemAvailable is not the container allocation.
- Full process commands and project cwd inspection found no active graph worker, BFS or solver. Existing Antigravity MCP servers and idle shells are service processes, not running research calculations. The transient extractor itself is excluded.

## Saved accepted results

`research/ddp/more_graphs_20261027/delivery/families.json` still has 103 explicit different-order examples in 3 cells, strongest orders 37631 / 42402 / 51457 for (11,5) / (12,5) / (13,5). Complete Lean graph instances: 0. Its saved date remains 2026-10-27; no later accepted delivery was found in the checked delivery/result entry files. This is extraction of existing state, not a graph revalidation or a claim to have re-audited every experimental output.

## H9 stable-triangle twist missing-target classification

Input directory: `research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension`. Every one of the 30 visited degree-12 cases has an explicit `missing` list in `items/d12_pool00000.json` through `items/d12_pool00029.json`, with `source_n=42402`, `source_m=245937`. No new coverage traversal is needed to perform the requested split.

Intervals are core `[0,41356)`, original published-source exterior `[41356,42342)` (986 vertices), and project additions `[42342,42402)` (60 vertices). Counts below are mandatory-neighborhood misses in the already tested final graph, before guards.

|Pool index|Mandatory pins|All misses|Core misses|Original exterior misses|Project-addition misses|
|---:|---:|---:|---:|---:|---:|
|0|10|40|0|35|5|
|1|11|56|0|52|4|
|2|12|54|0|48|6|
|3|11|47|0|44|3|
|4|12|70|0|64|6|
|5|12|44|0|40|4|
|6|12|38|0|34|4|
|7|12|52|0|46|6|
|8|12|50|0|48|2|
|9|12|53|0|47|6|
|10|10|42|0|40|2|
|11|12|35|0|33|2|
|12|12|45|0|41|4|
|13|11|44|0|39|5|
|14|10|40|0|39|1|
|15|12|48|0|44|4|
|16|12|53|0|50|3|
|17|12|63|0|58|5|
|18|12|60|0|57|3|
|19|12|46|0|42|4|
|20|12|35|0|31|4|
|21|12|81|0|80|1|
|22|12|46|0|40|6|
|23|12|61|0|59|2|
|24|11|42|0|38|4|
|25|12|54|0|48|6|
|26|12|41|0|37|4|
|27|10|47|0|46|1|
|28|10|46|0|44|2|
|29|11|35|0|34|1|

All 30 cases miss both original exterior vertices and project-added vertices. Original exterior counts range from 31 to 80; project-addition counts range from 1 to 6. Across cases there are 1468 missing-target occurrences, split as 0 core + 1358 original exterior + 110 project additions. These are occurrences, not distinct target vertices. The corresponding distinct unions contain 581 original exterior vertices and 46 project-added vertices.

This refutes the proposed explanation that these 30 failures arise only from the 60 project additions. Merely removing project additions cannot improve distances from the same mandatory pins to fixed original exterior targets; deleting edges/vertices cannot create shorter routes. A genuine joint rearrangement could add different routes or free ports and is not excluded. The final-graph masks also do not by themselves decide the rule on the original published graph, since available guards and degrees change when additions are removed.

## Existing support interface

- `pool12.json`, key `records`: `pool_index`, `pins`, `anchor_cap`, `current_pin_degrees`, geometric witness data.
- `items/d12_poolNNNNN.json`: `missing`, `missing_count`, `pins`, `pin_current_degrees`, `representatives`, `mask_words_per_row`, guard-search disposition. In this batch anchor caps are 2, 1 or 0 according to 10, 11 or 12 mandatory pins.
- Corresponding `items/d12_poolNNNNN.masks.u64.bin`: one row per `representatives` entry; each row contains `mask_words_per_row` native uint64 words. Bit j describes whether that representative guard covers target `missing[j]`. All 30 saved file sizes agree with `len(representatives) * mask_words_per_row * 8`. These supports are tied to the tested final source and its eligible guards.
- Writer implementation: `research/ddp/more_graphs_20261027/h9_redei15/production/cover.cpp`, lines 35–36; original caller: `research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/run.py`.

The exact missing-target split is fully available. If the next mathematical question is whether original-exterior misses alone already exhaust the allowed guard budget, the minimal diagnostic is to project these saved guard rows onto the original-exterior indices and test the existing 0/1/2 guard budgets. It needs no new balls or graph traversal. That restricted guard test was not run here. Any claim about newly freed guards after removing project additions requires a new, explicitly defined source/degree interface rather than reusing the final eligible-guard list as complete.
