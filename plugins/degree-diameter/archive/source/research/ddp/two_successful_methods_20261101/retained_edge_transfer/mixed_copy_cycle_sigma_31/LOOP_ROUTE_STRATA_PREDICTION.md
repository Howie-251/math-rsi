# Refined prediction after the own-radius2 claim was falsified

The first actual diagnostic falsified the stronger own-B2>=7 claim: its
minimum is3. Crucially it supported the FULL model numerator>=7, so the
explicit fractional assignment still appears valid. Do not erase this
failed prediction or label the integer model feasible.

Before inspecting the saved per-kind histogram, predict the following
complete explanation and count table. Use the old saved B-port0 R2 entry
to identify B-distance strata without rerunning any old B neighborhood.

If B coordinate z has old distance2 from b0, its unique factor three-walk
can start with the absolute loop b0--b0. It need not start in one of the
eight nonabsolute neighbors used by R. A G0 target over such z has exactly
three direct R neighbors and no additional R endpoints at distance2.
This is the missed shorter-route category in the first own-B2 prediction.
Those three own pins alone are fractionally short, but the other five
helpers can each use the same three direct old pins after one helper edge.
Thus the actual numerator is3+5*3=18, well above7.

For far B coordinates, the first step is instead a nonabsolute neighbor
of b0 and the seven-entry A-two-support supplies the seven own R endpoints;
there are no direct R neighbors. The two route types complement each other.

|target stratum|count|closed B1 intersect R|closed B2 intersect R|full numerator|
|---|---:|---:|---:|---:|
|old B-distance3 vertices and copies over nonfixed B absolutes|8960|0|7|7|
|old B-distance2 vertices|960|3|3|18|
|the120 selected R vertices|120|1|56|61|
|all F representatives over b0, including15 clones|20|24|56|176|
|the other10 freed U vertices over b0|10|24|72|192|

The five counts sum10070. Reuse FRACTIONAL_ALL_TARGET_COUNTS.tsv and
the actual label recipe to check this prediction; no graph traversal,
new solver or fresh field/Steiner/BFS is needed. Keep each stratum and any
counterexample separately. This data-reuse check stays within the original
120CPU budget, of which95.856266CPU have been used by the one MILP and
first diagnostic. The first own-B2 prediction remains REFUTED even if this
refined explanation is supported.

If confirmed, the full LP witness is an exact rational feasible assignment:
x[h,u]=1/7 on R for every helper, and zero elsewhere. It does not specify
a legal integer allocation. The next construction problem is to allocate
the small A-two-supports and copy/sigma repair routes among six helpers
simultaneously. A larger aggregate capacity estimate or another run of the
same10500-variable MILP is not the next experiment in this batch.
