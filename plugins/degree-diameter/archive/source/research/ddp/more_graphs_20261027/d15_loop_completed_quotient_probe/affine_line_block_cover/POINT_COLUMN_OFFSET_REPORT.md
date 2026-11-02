The frozen fixed-offset point-column prediction was supported for both sources. Only controller0 and the specified canonical direction/route-witness translation were tested; no alternative point or direction was tried.

|Source|L0 pins|Lp pins|Same full-fibre mask|Point XOR size|First different target|At that fibre: old/new sizes, intersection, union|
|---|---|---|---|---:|---:|---|
|15552|0,16,23|32,36,52|yes,50 blocks|1062|0|39/39,12,66|
|102060|0,151,212|63,133,167|yes,160 blocks|6849|4|177/177,123,231|

For15552, target0 is present only in L0's column. For102060, target4 is present only in Lp's column. Both first differences are in controller0. POINT_COLUMN_OFFSET_RESULT.json preserves each fibre's exact local old/new/intersection/union integer masks and sizes, alongside the complete-column XOR and first target. The total point coverages are4962/4962 and46167/46248 respectively.

Thus equal whole-fibre block columns do not imply equal covered-point columns. This is a concrete reason to preserve the affine offsets in the joint-line cover model; it does not establish that any chosen five lines or15 pins cover all targets.

One worker used0.006358512 CPU seconds. Each source read six existing eligible-pin balls and computed only the two frozen three-ball unions. There was no new ball, BFS, solver, new graph or solver modification. Evidence: POINT_COLUMN_OFFSET_PREDICTION.json, point_column_offset_probe.py and POINT_COLUMN_OFFSET_RESULT.json.
