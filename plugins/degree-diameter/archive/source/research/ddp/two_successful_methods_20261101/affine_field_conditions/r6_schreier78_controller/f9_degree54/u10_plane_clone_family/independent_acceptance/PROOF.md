# One-rule five-endpoint independent acceptance

Allfive complete graphs from the fixedU10plane rule pass fresh independent acceptance. Their maximumdegrees are55through59and their orders are57672,58482,59292,60102and60912. The source56862-vertex54-regulargraph and its genuine-Walk/all-pairs/exactD3 theorem are inherited, not rerun. The fivecases all use immutable source full neighborhoods, zero new-new edges and the same810center recipe.

## 1. Independent recipe, one source parse and complete file binding

Set U=[31,32,44,45,59,60,61,72,73,74]. For uIndex∈0..9and field codesa,b∈0..8, define

    h=81*uIndex+9a+b,
    c_h=729*U[uIndex]+a+9b+81*GF9mul(4,a).

The arithmetic is independently implemented polynomial multiplication inGF(3)[w]/(w²+1), codea+3b;4 is1+w. No producer pin/PASS/prediction caches are imported. For casek, copy=0..k−1 givesj=810copy+h andnewlabel56862+j.

The accepted complete source edgefile is parsed once and retained as literal adjacency lists and its ordered1535274edges. Each of the810sourcecenter neighborhoods is verified to have54elements; the810sets are pairwise disjoint and contain43740distinct old pins. Consequently13122oldvertices have no pin load. The actual induced graph on the810centers is separately checked to be405K2, which confirms that center independence is not a needed premise.

Each of the five complete new edgefiles is then read exactly once. Valid labels, strict global edge order and smaller endpoints ensure simplicity. Every old-old edge matches the next literal source edge, and the entire source body is retained exactly. Every remaining edge joins an old vertex to a new vertex and belongs to the designated center's immutable sourceN54; there are no new-new edges. The entire literal neighborhood of each new vertex is compared with thatN54, for all810knewvertices, not just810basecenters. Every final vertex degree is checked.

Thus casekhas

    n_k=56862+810k,
    m_k=1535274+43740k,
    degree54 count=13122+810k,
    degree(54+k) count=43740.

Every loaded old vertex gets exactlyknew neighbors. All other old vertices and all new vertices have degree54. These checks establish the full literal graph, including each repeated-copy label.

## 2. Complete all-pairs and every prefix without future vertices

LetGbe the accepted source andclone_c a vertex joined toN_G(c). For oldv≠c, replace the first vertex of an old shortest path fromc tovbyclone_c. Forv=c, takeclone_c–a–c through anyoldneighbora. All such paths have length≤3and originalsource interiorvertices.

For clones of centersc,d, an old center path of length3givesclone_c–a–b–clone_d. A length2center path givesclone_c–a–clone_d. Adjacent centers giveclone_c–d–c–clone_d, and equal centers give a length2path through a common old neighbor. This covers the405sourcecenter matchingedges as well as repeatedcopies; no centerindependence premise is used.

These paths work in every initial prefix of the prescribed copy order. For a newly added clone, the first pin of each such path lies in its immutableN54and reaches every existing vertex in at most2further steps. Hence its pins have the required radius-two coverage in the current complete graph, without a futureclone. Prefix old loads never exceed the case's finalk, so every prefix respectsdegree54+k.

Old-old sourcepaths remain present. Collapsing eachclone to its center and fixing oldvertices gives a graph homomorphism back toG, preservingwalklength. If the final graph had diameter≤2, the accepted source would too, contrary to its closed exactD3theorem. Thus each accepted endpoint has exactdiameter3.

## 3. Prediction before any new graph file is read

Collapsingclones and replacingfirstvertices show that the distance fromclone_c to eacholdv≠cequals the source distance fromc tov. The originalc is atdistance2. Thek−1otherclones ofc are also atdistance2. Each of the809kclones of othercenters hasdistance exactly3: there is no new-newedge, and disjoint baseNsets exclude a sharedpin/length2path; the old-only path argument supplieslength≤3. Adjacentcenters still use the length3case above.

Before opening anynewedgefile, the independent program enumerates only sourceR2balls for all810centers once. TheirR3counts are inferred from the inherited sourceD3theorem; no oldR3BFS is executed, and no fiber/decktranslation automorphism is assumed. Every one of these810balls has size2504, hence sourcehistogram

    (1,54,2449,54358).

This differs from the2476sourceR2counts at the previously chosenU6plane centers. The current calculations explicitly measure the chosen810centers; neither value is extrapolated to an entire fiber or all sourcevertices.

For each of thekcopies of a basecenter, the falsifiable predicted final histogram is

    (1,54,2449+k,54358+809k).

All12150newroots across the fivegraphs were tested by ordinaryqueueR3BFS on their respective complete literal graph. Every distanceclass matched exactly, as shown below and in eachcase's CSV:

|k|Degree|Order|New roots tested|Actual and predicted(R0,R1,R2,R3)|
|---:|---:|---:|---:|---|
|1|55|57672|810|(1,54,2450,55167)|
|2|56|58482|1620|(1,54,2451,55976)|
|3|57|59292|2430|(1,54,2452,56785)|
|4|58|60102|3240|(1,54,2453,57594)|
|5|59|60912|4050|(1,54,2454,58403)|

This is allnewroots for each endpoint, plus one shared810-center sourceR2-only prediction batch. It is not allsource-rootBFS. The actual sourceR2counts are in `BEFORE_ANY_NEW_FILE_SOURCE_R2_PREDICTIONS.csv`; the old/sourceR3values there are explicitly marked as inherited-D3 inference.

## 4. Pilot, costs and evidence boundaries

The firstcase was the requested pilot. Actual bindingCPU0.266110and810-rootBFSCPU0.364636 gave a10.25CPU-second conservative projected remaining cost after a1.5factor and1secondbuffer, compared with more than139CPU seconds remaining in the validator's internalbudget. `PILOT_RESULT.json` therefore records `CONTINUE_WITHIN_BUDGET` beforecases2–5continue.

Allfivecases completed in one validator invocation. The measured executable batch used8.612202832CPU seconds including compilation, oneaccepted-sourceparse,810sharedR2predictions, fivecomplete literalfilebindings, all12150newrootBFS, pilotprojection anddriveraggregation, below150CPU. The sourceR2-only portion used0.006682CPU. There was onecompiler, onevalidator, noLeanprocess and zero oldR3BFS/oldfield-controllerfinitechecks. Allprocesses are terminal; no timer renewal or repeatedsourceparse occurred. Interactive source authoring and preliminary read-only inspection are outside the executable-batch measurement boundary.

The five externalcomparison guarantees are inherited from the separate publicgate `CONTROLLER_U10_DEGREE55_59_WINDOW_20261101.{md,json}`:56540,57568,58596,59624and60652. The current advantages are1132,914,696,478and260. These are comparisons to the explicitly scoped published-methods-derived guarantees, not globalrecord or priority certification. NewconcreteLean and externalreviews belong to other scopes and are not asserted by this acceptance.

No otherU,plane,field,copy count orparameter was tested; k6wasnotgeneratedorvalidated. This acceptance does not turn allpossibleprefixes into separatelycountedresults. The fiveendpointgraphs and percaseevidence are the only deliveredgraphinstances.
