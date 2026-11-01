# Fresh P6 selector after the two-small eight-mixed gate

The new run preserves all earlier profiles and adds exactly EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR: exactly8 positive3/4 sets with at most2 triples, no negative triples, at most20 negative quadruples, ground18 and D7. The other dimension-correct gates remain. No L17 gate was applied to L18.

RUN_HIT_ALL_HIGH retains the first eligible-high-hitting pass. RUN.py/json additionally classifies **all15 proper-C blue pairs and all20 proper-C blue triples**, retaining negative pairs/singletons from all-red higher traces and positive pairs from all-blue higher triples. The first necessary inventory is unchanged by that larger selector. CPU0.030seconds. REPLAY.py independently rebuilds the signatures by trace-category formulas: all35 choices match. Eight choices have a negative pair, and two have a positive pair; neither category is deleted.

Only the first high-trace orbit of (n2,n3,n4)=(6,2,0), nine in C at0, was visited. Twenty necessary J inputs were reached: nineteen accepted (thirteen by the new eight-mixed gate, six by the L18 eight-four/two-triple gate), then the first nongated input. This is not complete coverage of an inventory. The remaining three high-trace orbits for nine0, nine at a, (5,1,1),(4,3,0),(3,2,1) were not processed in this first-stop run.

The stopping input has C=01234, a=5, degree vector(9,8,8,8,8,8), higher traces012 and345. J is the simple K4 on{0,1,2,5}:

    01+02+05+12+15+25.

Its pair degrees are(3,3,3,0,0,3), singleton counts are(4,3,3,6,6,4), and n1=26. Thus the35 actual-index trace slots are one C slot, two higher slots, six pair slots and26 singleton slots. The degree equations, all required P-pair support and the necessary18-point P/L coverage capacities hold. Exterior incidence sets were not constructed: P/L realizability is **undetermined**, and this is not an actual H or a non-Property-B example.

Three smallest unresolved high-hitting pair interfaces (all L18/D7) are:

|Blue|Positive4|Positive3|Negative3|Negative4|
|---|---:|---:|---:|---:|
|15 or25|7|1|1|19|
|05|8|1|1|18|
|13,14,23,24|9|0|3|17|

Blue03/04 gives10 positive4, three negative3 and16 negative4. All18 high-hitting three-blue signatures also fail the current catalog; the two other three-blue choices each retain an all-red negative pair and all-blue positive pair. Full source-index signatures are saved in RUN.json.

Other canonical gates were checked for parameter compatibility: the seven-mixed gates stop at total7 positive sets; the old exact eight-mixed theorem has no negative triple; the two-small exact eight-mixed theorem also has no negative triple. The sparse-five and large-union-six gates require fewer positive sets and additional union data, so they do not silently accept this input. The canonical fixed-product gate requires actual intersections not encoded by this necessary P inventory. No new gate was attempted after this stopping record.
