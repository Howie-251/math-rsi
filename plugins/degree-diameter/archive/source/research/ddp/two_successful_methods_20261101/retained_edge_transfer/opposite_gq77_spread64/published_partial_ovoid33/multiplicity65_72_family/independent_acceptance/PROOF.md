# Independent acceptance of eightP33 endpoints, with one maximal-graph BFS batch

All eight complete literal graphs atdegrees65through72 pass independent mathematical acceptance. Every endpoint has its own complete edge-table/source-neighborhood/degree binding. Their all-pairs and prefix proofs use the accepted immutable160050-vertex source. Only the maximalendpoint receives the additional13200new-root literal BFS batch. Its BFS is not used to infer distances in smaller prefix graphs.

## 1. Immutable source and independent definition binding

The source is the already accepted graph G on160050vertices and5121600edges, all64regular and exactD3, including the original50fillvertices. Its complete genuine-Walk theorem is already closed in `OppositeGQ77Spread.concrete_order_degree_and_exact_D3`. No field/geometry/old-root validation or Lean compilation is repeated here.

The independent driver reads only the declared33pointlabels in `../../ACTUAL_POINTS.json` and the original source's ordered50spreadline labels to construct the1650center labels

    h=50i+j, c_h=400P[i]+spreadLineID[j].

Their labels and coordinates were separately accepted in the preceding new-set/interface scope. This batch parses the source literal edgefile once, including its n m header, and reads its exact neighborhoods. It checks1650literalN64sets are disjoint. They contain105600distinct originalsource vertices:105567of the original160000point-line labels and33of the original50filllabels. The remaining54450sourcevertices have zero base load. These are literal source neighborhoods, not evolvingcenter neighborhoods after earlier clones.

For endpointk=1..8, the clone label is160050+q, withq=1650copy+h andcopy=0..k−1. Every graph file has its exact n m header checked; the body must have valid smaller/larger endpoints in strict global lex order. Every old-old edge agrees in order with the complete5121600source edges, including source-fill edges. There are no extra or missing oldedges and no new-new edges. Every new vertex's entire64-neighbor literal list equalsN_G(c_(q mod1650)). The comparison is performed for all59400new vertices across the eight endpoints.

Each vertex's literal degree is checked. The resulting exact statistics are

    n_k=160050+1650k,
    m_k=5121600+105600k,
    degree(64+k):105600vertices,
    degree64:54450+1650k vertices.

No assertion about complete graph equality relies only on a producer PASS receipt or on a sampled edge check. The literal binding establishes each endpoint is the stated immutable-fullN graph.

## 2. All endpoints and all current prefixes, independently of maximal BFS

Consider any initial prefix of any endpoint's orderedclones. For a clonez_c and oldsource vertexv≠c, take an oldsource path c–a–…–v oflength≤3 and replace its first vertex byz_c. Forv=c, takez_c–a–c through any oldsource neighbora. Here “oldsource” includes the50originalfillvertices, all present before any of this family's clones.

For two presentclonesz_c,z_d, a sourcecenter path oflength3givesz_c–a–b–z_d; a length2path givesz_c–a–z_d. Adjacentcenters givez_c–d–c–z_d. Equalcenters, including repeatedcopies of the samebasecenter, give a length2path through an oldsource neighbor. All interiorvertices in these routes belong to the fixed160050source; no futureclone is used.

Thus every newly inserted pin setN_G(c) reaches every vertex of the complete current graph in at most2further steps. Each current prefix has diameter≤3. Its sourcepin load never exceeds its endpointk, and each clone hasdegree64, so the correct degreecap is preserved at every prefix. Centerindependence is not assumed; the actualcenter set induces528K2and594isolates.

Map everyclone back to its sourcecenter and fix all originalsource vertices. Every literal edge maps to a genuineGedge, giving the inherited collapseHom. If an endpoint had diameter≤2, this map would give diameter≤2inG, contradicting the accepted source theorem. Hence all eight endpoints have exactdiameter3.

This proof applies separately to each endpoint after its own complete literal binding. A BFS result in the larger graph alone would not suffice: deleting vertices can destroy paths. The old-onlyinterior routes above are the reason the smaller graphs are accepted without repeating their new-root BFS.

## 3. Exact per-center prediction from one sourceR2-only batch

Before reading any new graph file, the program independently enumerates the sourceR2ball at each of the1650centers. It does not BFS any oldroot to radius3. For sourceR2countR, sourceD3 gives its remaining distance3count as

    160050−1−64−R=159985−R.

No orbit or flag-class value is hardcoded. The actual measurements give33centers withR=3185and1617withR=3248, in `SOURCE_R2_ONLY_PREDICTIONS.csv`. These are observations for the chosen1650centers only.

The collapse map and old path replacement show a clone's distance to every oldv≠center equals the source distance; its originalcenter hasdistance2. Its otherk−1samecenter copies also have distance2. All1649kclones of otherbasecenters have distance3: no new-new edge givesdistance1, disjointNsets exclude distance2, and the preceding path proof suppliesdistance≤3. This holds even for adjacentcenters.

Consequently the exact predicted/proof-derived histogram for every newroot is

    (1,64,R+k,159985−R+1649k).

Every endpoint's machine result records the two resulting histogram classes. For k<8 they are proof-derived predictions, with **zero actual new-root BFS calls**. They are not reported as directly measured BFS histograms.

## 4. Actual maximal-graph supplemental BFS

Only k8uses additional literal BFS, from all13200newroots. A CSR adjacency is built from that actual complete graph file in a separate allocation; the immutable source adjacency used for predictions is unchanged. Ordinary queue BFS marks/counts every newly reached vertex throughdepth3. Depth3discoveries do not need queue entries because their adjacency is never expanded. No bitset surrogate, implicit source-radius3 count or field formula replaces these literal BFS traversals.

Every root reaches all173250vertices. Actual and predicted classes match exactly:

|New roots|Actual and predicted(R0,R1,R2,R3)|
|---:|---|
|264|(1,64,3193,169992)|
|12936|(1,64,3256,169929)|

All13200individual rows are saved in `cases/d72_n173250/NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv`. There are no other endpoint BFS batches and no oldrootR3BFS. In particular59400is the count of full-neighborhood bindings, not a BFS-root count.

## 5. Exact endpoints and evidence boundary

|k|Degreecap|Order|Edges|Actual new-root BFS|
|---:|---:|---:|---:|---:|
|1|65|161700|5227200|0|
|2|66|163350|5332800|0|
|3|67|165000|5438400|0|
|4|68|166650|5544000|0|
|5|69|168300|5649600|0|
|6|70|169950|5755200|0|
|7|71|171600|5860800|0|
|8|72|173250|5966400|13200|

The publiccomparison gate is separately recorded in `public_baseline_audit/P33_CLONE_DEGREE65_72_WINDOW_20261101.json`. Its current derivedpublished-method guarantees are160000+1650k, so each accepted endpoint exceeds that scoped guarantee by50vertices. This acceptance does not certify globalrecord, priority, publication or newconcreteLean. Reproducing the known33-point partialovoid itself is not counted as a newrecord.

One compiler and one validator completed, single worker. Measured executable CPU was21.419453053seconds including preparation, compilation, one sourceparse, sharedR2predictions, eight complete bindings, maximal13200-rootBFS and aggregation, below180CPU. SourceR2-only prediction CPU was0.022353; maximal new-root BFS CPU was11.1961. Allprocesses are terminal. Interactive source authoring and initial read-only inspection are outside this explicit executable-batch measurement boundary.

There was no repeated sourcefield/geometry/oldgraph validation, no oldR3BFS, no newLean or externalreview, no install/solver/hash, no additionalk orsource. Counters and newformalization are root-owned and are not changed by this receipt. Eachcase directory has its own binding rows, result, summary, proof and terminalscope.
