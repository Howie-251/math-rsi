# Independent acceptance of the81-point immutable-fullN extension

The source is the already accepted complete56862-vertex54-regular graph of diameter3. This scope inherits its full all-pairs proof from `../../independent_acceptance/PROOF.md` and the actual source measurements in `../../independent_acceptance/BFS_PREDICTION_VS_ACTUAL.csv`. It does not repeat any old-root BFS, controller search, old finite-field axiom check or source route verification.

## Actual new literal graph binding

The independent code recomputes only the81 declared center labels. With GF(9)=GF(3)[w]/(w²+1) encoded a+3b, set

    j=9a+b, c_j=a+9b+81*GF9mul(4,a), z_j=56862+j.

Here4 is the field element1+w; its multiplication is polynomial multiplication modulo w²+1, not integer multiplication. The verifier reads both the entire immutable source edgefile and the entire new edgefile. It checks the1535274 old edges in the latter agree exactly and in order with the former, no old edge is deleted or added, and the4374 remaining edges connect old vertices to new vertices. There are no new-new edges. Every complete literal neighborhood of z_j equals the literal54-neighbor set of c_j in the immutable source. All new labels use the exact prescribed j order.

The81 literal source neighborhoods are pairwise disjoint:4374 pin occurrences are4374 distinct old vertices, so maximum old load is1. Their union consists of six complete729-vertex controller fibers. The full new literal graph has56943 vertices and1539648 edges, is simple by strict global edge order and valid endpoint checks, and has exact degree histogram

    degree54:52569; degree55:4374.

Thus the maximum degree is55. These checks use the old edgefile as immutable data; they do not assume the producer's pin/certificate caches.

## All-pairs and every prefix, with no future clones

For any graph G of diameter at most3, adding any collection of vertices z_c adjacent to the full immutable source neighborhood N_G(c) preserves diameter at most3. To see this using actual paths:

For an old vertex v≠c, take an old shortest path c–a–…–v of length at most3 and replace only its first vertex by z_c. For v=c, use z_c–a–c for any old neighbor a. All interior vertices of these paths remain old.

For two distinct new vertices z_c,z_d, an old center path of length3 gives z_c–a–b–z_d. An old center path c–a–d of length2 gives z_c–a–z_d. If c,d are adjacent, use z_c–d–c–z_d. Coincident centers, if any, would give a length2 path through an old common neighbor. Our81 centers are distinct, but the lemma does not require center independence.

Old-old paths are retained. This proves all-pairs diameter at most3 in the final graph and in every initial prefix of the fixed center sequence; none of the displayed paths requires a new vertex that has not yet been added. Each old pin receives at most one edge during the entire construction, so every prefix also has degree at most55.

The final order56943 exceeds the degree55 radius2 Moore bound1+55+55×54=3026. Its diameter is therefore exactly3.

## Exact distance-class prediction and actual new-root BFS

Map every clone z_j back to its source center c_j and fix all old vertices. This is a graph homomorphism to the source, because every added edge is a literal source-neighborhood edge under the map. Together with the old paths above, it shows that for every old v≠c_j the new graph distance from z_j to v equals the source distance from c_j to v. The old center c_j itself has new distance2. Distances between distinct clones are exactly3: there are no clone-clone edges, and their neighborhoods are disjoint, excluding length2; the lemma supplies length at most3.

Before reading the new edgefile, the driver reads the already accepted independent source BFS rows for the81 recomputed centers. Every center has source histogram(1,54,2476,54331). The precise prediction for each new root is therefore

    (R0,R1,R2,R3)=(1,54,2476+1,54331+80)
                    =(1,54,2477,54411).

Every one of the81 new roots was then tested by an ordinary queue BFS on the new literal graph. All81 exactly matched all four predicted distance classes and reached all56943 vertices by radius3. Per-root predictions, actual histograms and center labels are saved in `NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv`; the independent pre-execution predictions are separately saved in `BEFORE_EXECUTION_DISTANCE_PREDICTIONS.json`. There were zero old-root BFS calls.

## Execution and evidence boundary

One actual compiler and one actual validator process completed successfully. The measured executable batch used1.133168151 CPU seconds, including inherited-data prediction preparation, compilation, both full edgefile reads, complete new-binding checks, all81 new-root BFS and aggregation; the budget was45CPU seconds. Interactive source authoring and initial read-only inspection are outside this explicit measurement boundary. All child processes are terminal. No other plane, fiber, degree, field, solver, install, hash or Lean work was performed here. This establishes mathematical graph acceptance, not Lean completion or public novelty/priority certification.
