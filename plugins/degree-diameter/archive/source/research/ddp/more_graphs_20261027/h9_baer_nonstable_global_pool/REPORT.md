# Galois-reduced nonstable Baer pool:2 new N12 neighborhoods

The complete new potential-foldability scope was processed. The native enumeration finds all3640 F3 singular lines, exactly10 Q9 generator planes through each, four F3-stable and six nonstable. The stable RREF set is exactly the old1120-plane set; the21840 nonstable planes are all distinct and each has a unique F3 line. The old1120 Baer occurrences and7560-mask orbit were not rerun.

For current N11 source37631, the new pool is empty. For fixed N12 source42398, two distinct complete folded Baer neighborhoods survive current degree and pin-count budgets. Both have11 mandatory pins and1 anchor slot. They do not duplicate any actual pinset in the old364-flatplane or756-nonflat-F3-plane pools. The frozen prediction of a new N12 source candidate is supported. No R4, anchor completion, BFS or candidate graph was run in this pool task.

The two N12 literal neighborhoods are

    [3417,4332,9943,17286,20272,20535,22347,22604,29558,32811,38917],
    [3417,4332,9943,18126,20272,20535,22347,29558,32567,34919,40451].

Both have the unique F3line index1253, with different plane/Baer witnesses. pool12.json contains their full13 raw point IDs and coordinates, current pin degrees, the exact F3line and generator-plane RREF bases,91bit Baer mask and orbit index. Full witness references are retained. Their actual whole-source coverage is untested; degree eligibility and the geometric oldcore blocking guarantee do not by themselves certify all current source vertices.

## Why this is the remaining finite geometry scope

The parent verified in h9_baer_galois_plane_filter/PAIRING.json that every two-point fiber of the two calibrated fold maps is p paired with p^3, with364 F3-fixed points. That established pairing is reused here without another global fiber audit. If13 raw Baer points fold to at most12 neighbors, two distinct raw points p and tau(p) lie in the same generator plane W. They span a tau-stable singular line L inside W intersection tau(W). If W is tau-stable, its canonical RREF is overF3 and it belongs to the old1120-plane set. Otherwise the intersection is exactly L, a unique F3-defined singular line.

For each of the3640 F3lines, Q9 has10 maximal generator planes through it, of which four are F3-stable and six nonstable. A nonstable plane cannot contain another F3line, since W intersection tau(W) would then span W. Thus3640*6=21840 counts the new planes without duplicates. The root supplies this Galois scope reduction; the native program explicitly calibrates every per-line count and the global unique-plane sets. It does not pretend to enumerate all598600 Q9 generator planes or run their Baer masks. The unlisted planes cannot produce a collision needed for the degree11/12 full-Baer rule under this pairing.

All3640 F3lines are obtained from pairwise-polar singular F3point pairs and canonical two-row RREF. For a line, its common perpendicular contains exactly820 Q9singular points. Removing its two pivot components quotients out the line: the ten points of the line reduce to zero, and the other810 points normalize to exactly ten projective quotient directions. Adjoining each direction gives one generator plane RREF. This yielded four stable and six nonstable planes for every line, with no classification counterexample. The stable RREF set matches all1120 old planes exactly. F3_lines.json, nonstable_planes.json and classification.json preserve every basis, raw point identification and calibration count.

## Source-specific eligible-pair pruning

A stable F3line has four F3-fixed Q9points and three tau-pairs. A collision usable by a legal complete folded Baer neighborhood must be an unsplit pair whose folded old vertex still has degree below the source cap. All collisions of a nonstable plane lie on its unique F3line. Folding13 points to at most11 requires at least two such eligible pairs, while folding to at most12 requires at least one. Lines below those thresholds are mathematically pruned for that source before any Baer bitmap test. These are necessary conditions, followed by actual fold-size and degree tests for all surviving masks.

| Source | Lines pruned | Planes pruned | Nominal masks mathematically pruned | Actual bitmap tests | Final distinct pool |
|---|---:|---:|---:|---:|---:|
|N11/37631|3568|21408|161844480|3265920|0|
|N12/42398|2506|15036|113672160|51438240|2|

The two-source line rule prunes both sources on2446 lines. Each source's pruned nominal occurrences plus actual bitmap tests sums to165110400, the full21840*7560 new-plane occurrence scope. No pruned mask is claimed as executed. For N12,34 raw Baer masks pass olddegree;32 fold to13distinct neighbors and fail the cap, while two fold to11. N11 has no rawdegree-surviving mask in its active scope. All source-pair decisions and the three raw conjugate pairs per line are saved in F3_lines.json.

The previous1120 F3stable-plane degree pools were already empty for N11 on the same37631 source. Combined with this complete Galois-reduced nonstable pool, there is no degree-legal full folded13point Baer neighborhood in the potential-foldability generator-plane scope for that fixed N11 graph. This conclusion uses the stated fold-pairing and geometric classification; it is not a general degree11 graph upper bound or an exclusion of other blocking sets.

## Reuse, witnesses and cost

The old7560 Baer91bit masks and coefficient-point order are reused directly. For each active new plane the program maps all91 coefficient points to the existing66430 Q9point cache, filters masks by current foldedvertex degree, then actually folds all13 surviving raw points and checks distinct neighbor count. Full folded images remain mandatory. Source degrees are fixed at N11/37631 and N12/42398, even if another production branch later grows; future graph production must check its own current degrees again.

The100-F3line profile represents600 potential new planes and4536000 nominal Baer occurrences, but actually tested45360 N11 and1315440 N12 masks after pair pruning. It used0.008670 pool CPU seconds and projected0.884206 total native seconds. Complete geometry calibration used0.528029 native CPU seconds. The full native run used0.953535, compilation3.106015, and the driver measured4.066265 child CPU seconds, below15. All3640 lines reached terminal pool states; none is uncomputed. No incidence graph, WL refinement, old Baer search, graph BFS, anchor solver, graph generation or shared-document edit occurred. The task stops at its two-item N12 pool.
