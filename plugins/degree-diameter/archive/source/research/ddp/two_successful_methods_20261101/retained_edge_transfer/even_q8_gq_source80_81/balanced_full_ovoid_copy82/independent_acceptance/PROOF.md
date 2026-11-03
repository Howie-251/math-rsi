# Independent degree82 full-ovoid one-copy acceptance argument

**Actual complete degree82 graph acceptance PASS.** RESULT.json and TERMINAL.json record the successful independent compiler/validator batch. This argument does not infer full diameter from a subset of roots alone; it combines complete literal binding, accepted source all-pairs D3, old-only clone routes, all4225new-root BFS and nonD2 inheritance.

## 1. Immutable source, coordinates and entire edge binding

The source is the already mathematically accepted balanced filled graph on342290vertices/13862745edges, all81regular and exactD3. Its original342225vertices are labelled p*585+L; the65sourcefill vertices are342225+j. It is not the Payne graph or a previous clone-expanded graph. Its complete literal/GQ formula and all-pairs proof were accepted in `even_q8_gq_source80_81/independent_acceptance/PROOF.md`; this run repeats no old field, small geometry, projection or old-root distance check.

The independent driver reads only the accepted ordered OVOID65.tsv and SPREAD65.tsv. For h=65i+j, the center is c_h=o_i*585+S_j and the clone label is342290+h. Diagonal centers use the actual spreadowner of o_i, not an assumed identity between row and column. The source-center coordinates and ordering are reconstructed without producer expected/actual-neighborhood caches.

One stream of the source and one stream of the candidate are compared. Every candidate old-old edge must equal the next source edge, both headers are exact, and the source stream must be exhausted. Every candidate edge has valid ordered distinct endpoints and strict global lex order; therefore the graph is simple and no edge appears twice. There are13862745retained old edges,342225old-new edges and zero new-new edges.

During this one source parse, capture the full neighborhoods of all4225centers. Every observed source list has81neighbors. Every new vertex's entire literal neighbor list must equal its center's source list. All342225pins are distinct across centers, and their union must be precisely the source outside its65diagonal centers D, including all65original sourcefill vertices. The literal candidate degrees and CSR slot counts are checked at every vertex:342225sourcepins have degree82; the65oldD and4225clones have degree81.

This establishes equality with the specified full-neighborhood graph, rather than merely a generated formula or sampled adjacency. The actual CSR used below is filled from the candidate edge table.

## 2. Every all-pair route uses only old-source interiors

Old-old pairs retain their accepted source walk of length≤3. For a clone z_c and old vertex v≠c, replace the first vertex in a source walk c–a–…–v by z_c. For v=c, use z_c–a–c through any source neighbor a.

For two present clones z_c,z_d, a length3source path c–a–b–d gives z_c–a–b–z_d. A length2path gives z_c–a–z_d. Adjacent centers give z_c–d–c–z_d, which is needed for the2080matching edges among off-diagonal centers. Equal centers, if considered in the general rule, use any shared source neighbor; this particular endpoint has one clone per center.

Every interior vertex in these routes belongs to the original342290source, including its oldfill vertices. Thus the routes exist separately in every current prefix, without any futureclone. Complete sourceN binding is what makes these genuine graph walks.

Each actual inserted pin list contains81previously unused sourcepins. Those source vertices have degree81 before insertion and82 afterwards; earlier clones have no new-new edges. Every prefix has degree≤82 and diameter≤3. The independently saved4226prefix rows are derived from the checked actual pin lists: after k clones, degree82count=81k and degree81count=342290−80k.

This proof, rather than deleting vertices from a final BFS graph, establishes the prefix claim.

## 3. All4225actual new-root distance distributions

The prediction distinguishes65diagonal roots and4160off-diagonal roots according to the actual O/spreadowner map. Prior sourceR2formulas are5248and5328; no oldradius2ball is enumerated here. A clone has distance2 to its originalcenter rather than distance0. Distinct clones cannot have distance1 or2 because their entire neighborhoods are disjoint and there are no new-new edges. The source-walk routes supply their distance≤3. The predicted histograms are consequently

    diagonal: (1,81,5249,341184),
    off-diagonal: (1,81,5329,341104).

Ordinary queue radius3BFS is performed on the actual candidate CSR from every4225newlabel. Depth3discoveries are marked and counted but need no queue entry because their adjacency is not expanded. Each root must reach all346515vertices and agree in every distance class. Individual results, not just aggregate bad-pair totals, are saved. No orbit or source-translation symmetry replaces any newroot traversal.

The all-pair theorem comes from Section2 plus literal binding; these exhaustive new-root checks additionally verify the predicted class mechanism. They do not replace the old-source all-pair proof.

## 4. Exact diameter via a genuine collapse homomorphism

Fix all source vertices and map each clone z_c back to c. Every old edge remains a source edge; every new edge z_c–v maps to the genuine source edge c–v because the complete new neighborhood equals sourceN(c). There are no new-new edges. Hence any hypothetical length≤2walk between the accepted source witness vertices42705and43363would map to a sourcewalk of length≤2, contradicting accepted source nonD2.

Therefore the candidate and each actual prefix have exact diameter3. No second witness check or oldroot BFS is needed; this is a complete graph homomorphism argument, independent of future clones.

This receipt does not compile new Lean, change root counters, certify priority/globalrecord or authorize another graph. Public comparisons and sourcefill/JGT priority remain separate root-owned obligations.

## 5. Actual closed execution

The literal graph has n346515, m14204970, degree81count4290 and degree82count342225. All13862745sourceedges were retained exactly; all4225new vertices' complete81neighborlists matched their sourcecenter lists. All342225pins were distinct and exactly the source outsideD65, including its65originalfillvertices. All4226orderedprefix rows passed.

All4225actual new-root BFS histograms matched individually:65×(1,81,5249,341184) and4160×(1,81,5329,341104). The sourceR2 values were predictions, not newly enumerated sourceballs. Every source and candidate edge file was parsed once, and there was no oldrootBFS or extra nonD2CSR check; Section4's genuine collapse proof preserves the accepted witness.

Total executable CPU was12.395600852seconds／120, including accepted smallinput binding, onecompile0.923820040CPU, onevalidator-plus-driver11.470264254CPU and aggregation. Complete literal binding cost4.398370CPU and all4225new-rootBFS6.999010CPU. No failed compile or runtime experiment occurred. All processes are terminal; the original exec session was1407 and HANDLE.json now correctly saysTERMINAL／returncode0, rather than claiming a live PID.

Artifacts include INPUT_BINDING.json, ORDERED_SOURCE_N81_BINDING.tsv (4225orderedrows), INDEPENDENT_PREFIX_LOADS.csv (4226rows), ALL_NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv (4225rows), RESULT.json／RESULT.md／SUMMARY.json／TERMINAL.json and thisproof. There was no oldfield／smallgeometry／projection／Lean／solver rerun, no second graph and no rootcounter change. Interactive authoring is excluded from the explicit executable-batch CPU boundary.
