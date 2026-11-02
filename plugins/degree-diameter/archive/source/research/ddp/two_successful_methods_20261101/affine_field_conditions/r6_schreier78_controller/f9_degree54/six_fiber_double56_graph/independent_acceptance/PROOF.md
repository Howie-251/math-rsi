# Independent complete acceptance: two copies of486 packed full neighborhoods

This scope accepts the complete new graph on57834vertices with degree at most56 and exact diameter3. The original56862-vertex54-regular source and its all-pairs/genuine-Walk proof are already accepted; their finite-field/controller/old-root checks were not rerun. The source's compiled concrete Lean theorem is `DegreeDiameter.Portfolio.F9Graph56862.concrete_order_degree_and_exact_D3`; the present independent scope does not compile Lean.

## Independent center recipe and complete literal binding

Let U=[0,1,2,3,9,15]. For uIndex∈0..5 and a,b∈GF(9), encoded by integers0..8, the source center is

    c=729*U[uIndex]+a+9b+81*GF9mul(4,a).

Multiplication is computed independently as polynomial multiplication inGF(3)[w]/(w²+1), with codea+3b for a+bw. In particular4 denotes1+w and is not an integer scalar modulo9. Baseindexh=81uIndex+9a+b ranges over486centers. The two clone labels are56862+j withj=486copy+h, copy0or1. The verifier hardcodes this authorized recipe and does not import producer pin/PASS or distance-prediction caches.

The verifier reads both complete literal edgefiles. In the new file it checks strict lexicographic edge ordering, valid smaller/larger endpoints and no loops or duplicates. Its1535274old-old edges agree exactly and in order with the entire accepted source edgefile. The remaining52488edges join new vertices to old vertices, with no new-new edges. Each of the972complete new neighborhoods is compared with the exact54-neighbor set of its designated center in the immutable source. Thus both repeated copies are bound, not just the486base centers.

The486base full neighborhoods are pairwise disjoint: their26244pin occurrences are26244distinct old vertices. Using each twice gives old load0at30618vertices and load2at26244vertices. The final literal degrees are checked at every vertex:

    degree54:31590vertices, degree56:26244vertices.

There are exactly57834vertices and1587762edges. These are fresh complete-file checks for the new graph, while the source diameter premise is inherited.

## All-pairs and all-prefix coverage without future clones

For any source graph G of diameter at most3 with no isolated vertices, adding clones adjacent to full immutable source neighborhoods preserves diameter at most3. A path from center c to an old vertexv≠c can have its first vertex replaced by the new clone; the path to c itself is clone–a–c through any old neighbora.

For clones of centersc,d, an old center path of length3 gives clone_c–a–b–clone_d. A center path of length2 gives clone_c–a–clone_d. Adjacent centers give clone_c–d–c–clone_d. Coincident centers give a two-edge path through an old common neighbor. Every interior vertex in these displayed routes is an original source vertex. The graph here has two clones per center, so the coincident-center case is required.

The same argument applies to every initial prefix of the ordered972clones. For any newly added vertex, its54pins have radius-two coverage of the entire current graph: the displayed path to every existing vertex begins with one of those pins and has total length at most3. No route relies on a future clone. Prefix old loads are bounded by their final load2, so every prefix also respects degree56. Source old-old paths are retained.

Collapsing each clone to its original center and fixing all old vertices is a graph homomorphism to the source. It preserves walk lengths, so a diameter-two final graph would force diameter at most2in the source, contradicting the accepted source theorem. Hence the final diameter is exactly3. This proves the complete all-pairs conclusion independently of how many BFS roots were sampled; here all972new roots were checked in addition.

## Falsifiable distance prediction and actual comparison

The same collapse map, together with path replacement, gives exact equality of distances from a clone of c to every oldv≠c with the source distance from c to v. The original center c moves from source distance0to clone distance2. The other clone of c also has distance2. Every one of the970clones of other centers has distance3: no new-new edge gives distance1, disjoint base full neighborhoods exclude distance2, and the path argument gives distance at most3. This remains valid if some source centers are adjacent.

Before the new edgefile is opened, the verifier enumerates only the source radius-two ball for each of the486centers, directly from the accepted source adjacency lists. This is a new prediction calculation with explicit scope and timing, not a source radius-three BFS or a repeat of source all-pairs verification. It uses no coordinate/deck-translation automorphism. For a source radius-two ball of sizeB2, source R2=B2−55 and source R3=56862−B2, the latter inferred from the inherited source D3 theorem.

The predicted new-root histogram is therefore

    (1,54,source_R2+2,source_R3+970).

Every one of the486computed source balls has size2531, yielding source R2=2476 and inherited R3=54331. Consequently every one of the972new roots was predicted to have

    (R0,R1,R2,R3)=(1,54,2478,55301).

All972ordinary queue BFS runs on the new literal graph exactly matched every predicted distance class and reached all57834vertices by radius3. The486pre-newfile predictions are in `BEFORE_NEW_GRAPH_SOURCE_R2_PREDICTIONS.csv`; the972actual-versus-predicted rows are in `NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv`. This is972new-root BFS and486source-R2-only predictions; there were zero old radius-three BFS calls. The uniform histogram is established for these roots only, not claimed for every source vertex or whole fibers.

## Execution and comparison boundary

The one executable batch used1.729770946CPU seconds including compilation, both full edgefile reads, center/pin binding, all486R2predictions, all972new-root BFS and aggregation, below the45CPU cap. The source-R2-only prediction portion used0.003894CPU seconds. The new-root BFS portion used0.415905CPU seconds. All processes terminated successfully; one compiler and one validator were run. Interactive source authoring and preliminary read-only inspection are outside the recorded executable-batch boundary.

There was no old field/controller finite check, old radius-three BFS, other U/copy/plane/degree search, solver, Lean, install or hash operation. The baseline57568is the separately justified direct guarantee from published methods in `public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md`; this graph has266more vertices. This comparison is not global-record or priority certification. Its concrete Lean proof and external reviews are separate tasks.
