# Complete132-point PSL2(F11)/C5 orbital-plus-matching batch

**All10 candidates completed with zero hits and zero untested cases.** The frozen existence prediction is refuted. Four graphs are disconnected with component size12; six are connected and every complete identity-radius3 check fails. Negative exact global diameter and ordinary bad-pair counts are null. No all-root BFS, old-source BFS, extra group or changed subgroup was run.

The actual matrix and coset counts match the proposed structure:660 projective matrices, H order5, normalizer order10,132 cosets,55 involutions,5 in the normalizer,50 outside, and10 self-paired25-element doublecosets each containing5 involutions. The normalizer doublecoset provides one matching neighbor; each outside doublecoset provides five distinct neighbors. All10 resulting graphs are actual simple6regular graphs with396 edges, and their adjacency is invariant under changing the coset representative. The producer checked every one of the660 representatives for each graph.

|Case|Outside involution matrix|Connected component|R3 shells|R3 missing|
|---:|---|---:|---|---:|
|0|[1, 1, 9, 10]|12|None|None|
|1|[1, 2, 10, 10]|12|None|None|
|2|[2, 1, 6, 9]|132|[1, 6, 30, 80]|15|
|3|[2, 2, 3, 9]|132|[1, 6, 30, 80]|15|
|4|[3, 1, 1, 8]|12|None|None|
|5|[3, 2, 6, 8]|12|None|None|
|6|[4, 1, 5, 7]|132|[1, 6, 25, 70]|30|
|7|[4, 2, 8, 7]|132|[1, 6, 25, 70]|30|
|8|[5, 1, 7, 6]|132|[1, 6, 25, 70]|30|
|9|[5, 2, 9, 6]|132|[1, 6, 25, 70]|30|

The measured worker process used0.483786 CPU seconds; its driver used0.000700307 seconds, with zero compilation. The worker hard limit was18 seconds and the aggregate allowance20 seconds. Execution exited0 in the initial call, so there is no live handle. The code saved all matrix IDs/inverses/cosets/doublecosets in INPUT_TABLES.json and the full660-by660 group table in an explicitly described uint16 file.

The complete fixed-action scope is proved in[MODEL_SCOPE.md](MODEL_SCOPE.md). In this action the28 stabilizer suborbits consist of the loop, one matching,10 self-paired valency5 suborbits and16 nonselfpaired valency5 suborbits. An undirected nonselfpaired union has degree10; degree at most5 cannot reach132 points in diameter3 by Moore106. Therefore these10 graphs cover every possible diameter3 graph of maximum degree at most6 invariant under this fixed G action. The failure does not exclude all132-point graphs or solve the general(6,3) problem.

The sole Wiki ledger was checked before numerical work. Its prior norm5/PSL2(F11) arithmetic660/D4 item is a different660-vertex rule and gives no result for the present132-coset model. The saved baseline120 was used only as the proposed improvement threshold; no new graph was claimed and no fresh public-table assertion is needed for a negative result. This batch stops without selecting a less-failing case for further adjustment.
