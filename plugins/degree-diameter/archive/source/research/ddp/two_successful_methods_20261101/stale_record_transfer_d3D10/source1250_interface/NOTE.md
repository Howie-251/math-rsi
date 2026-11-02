# Conder1250: existing non-bipartite source and strict subdivision closure

**Stop by inherited same-source, same-rule NO.** The actual originalsource is ConderC1250.2,not a guessed1250graph. Officialdesc_g10#310 atcachedline23 identifies MarstonConder's2006-08-17 communication andlinks theactualraw `C1250.2.graph.txt`. It cites Conder–Ma, *Arc-transitive abelian regular covers of cubic graphs*,J.Algebra387(2013),215–242,DOI https://doi.org/10.1016/j.jalgebra.2013.02.035 . The2006communication is thecurrentorder'sdate;2013ispublication,not a neworderimprovement.

The sourcewas alreadyacquired andbound in `research/ddp/more_graphs_20261027/d3_D10_current1250_source`. Its `source1250.author.adj` hasoriginal labels1..1250; `source1250.edges` is thezero-based normalization,1250vertices/1875simpleedges/allcubic. ExistingSOURCE_PROFILE records connectivity and **non-bipartiteness by exactparityunion-find**,firstconflict(382,550),without anysource-distance traversal. Authorcensus identifiesgirth16,3-arc-regular Autorder15000,onevertex/edgeorbit,andnon-Cayley. Do not inferbipartiteness fromeven girth16. No newoddcycle/partition wasconstructed because theexisting paritycertificate alreadydecides thepremise. The officialSage sparse6 hasdifferentlabels; no Sage-to-raw labelmapwasassumed.

The localraw/generator endpoints are alreadyavailable: `research/ddp/more_graphs_20261027/d3_D10_current1250_source/source1250.author.adj`, `source1250.edges`, `SOURCE_SageMath.author.py`,and `symmcubicgraphrelations-type3.author.txt`. The source is reconstructible fromthese records. No network request,rawparse,degreecheck,2color orsourceD10/BFS wasperformed inthisinterface. Publicprimary links are inRESULT.json.

## The exact conditional premise

For a genuinelybipartite sourceG withdiameter≤10,edgeendpointsu,v have oppositeparity distances toeacholdtargett andboth distances≤10;hence min(dG(u,t),dG(v,t))≤9. Distancesfrom thesource set{u,v} areunchanged bydeletingtheconnectingedge e: ifa minimizingrouteuses e,startingattheotherendpoint removes thatfirstcrossing. Thus a newdegree2 subdivisionrootz satisfies d(z,t)=1+min(dG(u,t),dG(v,t))≤10. This conditional mathematicalprediction isvalid,but **itsbipartite hypothesis isfalse fortheactualConderC1250.2**.

Evenifnewrootcoveragepasses,old-oldD10wouldstillrequirepreservingallsource-distance10pairs: eachsuchpairneeds asourcegeodesic avoiding e. Pairs atsource-distance≤9 survivewith≤1detour penalty. This opportunity isnot anauthorization toresumea closedsource/operation.

## Authoritative later strictscope

`research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/REPORT.md`, `A_RESULT.json` and `ANALYSIS_PROOF.md` supersede thesource-recovery report'shistorical “noexactoperationyet” stage. The oldactualanchor(0,1) single-subdivision has1251vertices/1876edges,newlabel1250ofdegree2,maxdegree3. Oneactualmodified-newrootR10 query foundtarget1178outsideR10. InheritedsourceD10 givesglobalupper11,so thatcandidatehasexactdiameter11. Publishededgetransitivity transports thisanchored failuretoall1875oldedge subdivisions. It is acompletefamilyNO fromone actualrepresentative plus the inherited edge-transitivity proof,not1875numerical checksorageneral1251graph exclusion. Oldlabel/allrootchecks were0.

The sameoldbatch also completedall5614anchored two-cut/adjacenthelper objects:1870disjointsecondedges×3partitions plus4sharedendpoint objects. EveryonefaileditsfirstnewrootR10 test;secondhelperandoldrootchecks were0. That is aseparateclosedliteral1252architecture,notarbitrary1252graphs. No thirdcut/helperorothermodelisopened here.

Currentdecision: inherit thewhole single-subdivisionstrictNO andstop. Theautomaticbipartite-newroot rationale isunavailable;sourceD10,field/groupfacts andoldnegativecandidates are notrevalidated. Existingoldcompletework isnotcounted asnewwork ornewportfolioresults. This gateonlypreparedthe requested PRED/RESULT/NOTE/TERM andleavesroot/Wiki/globalfilesuntouched.

The inherited witness also gives a direct endpoint-union counterexample: bothoriginal endpointdistances d_G(0,1178) andd_G(1,1178) are10. This follows from theexisting newrootR10 failure, theexactnewroot formula and inheritedsourceD10,not a newdistance computation. Thus thissource has anactualoldtarget outside bothendpointR9balls,exactly the situation thebipartite premise would haveforbidden.
